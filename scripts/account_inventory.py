"""Offline inventory migration and max-level-only database policy."""
from __future__ import annotations
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DB = DATA / "三国谋定天下_Steam_S1.sqlite3"


def columns(conn, table):
    return {r[1] for r in conn.execute(f"PRAGMA table_info({table})")}


def load_account(conn):
    payload = json.loads((DATA / "account_inventory.json").read_text(encoding="utf-8"))
    generals, tactics = payload["generals"], payload["tactics"]
    keys = [(r["name"], r.get("variant", "普通")) for r in generals]
    if len(set(keys)) != len(keys) or len({r["name"] for r in tactics}) != len(tactics):
        raise ValueError("Duplicate inventory keys")
    for row in generals + tactics:
        red = row["advancement"]
        if red is not None and (type(red) is not int or not 0 <= red <= 5):
            raise ValueError(f"Invalid advancement: {row}")
    if any(r["quality"] not in ("金", "紫") for r in tactics):
        raise ValueError("Only gold/purple tactics are supported")
    table_sql = conn.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='account_generals'").fetchone()[0]
    if "variant" not in columns(conn, "account_generals") or "CHECK(level IS NULL)" in table_sql:
        conn.execute("DROP TABLE account_generals")
        conn.execute("""CREATE TABLE account_generals (
            general_id INTEGER NOT NULL REFERENCES generals(id),
            variant TEXT NOT NULL DEFAULT '普通',
            availability TEXT NOT NULL DEFAULT '常驻',
            advancement INTEGER CHECK(advancement BETWEEN 0 AND 5),
            level INTEGER CHECK(level BETWEEN 1 AND 60),
            allocated_force INTEGER, allocated_intelligence INTEGER,
            allocated_command INTEGER, allocated_initiative INTEGER,
            current_team TEXT,
            last_verified_at TEXT NOT NULL, notes TEXT,
            PRIMARY KEY(general_id, variant))""")
    for column, definition in {
        "advancement": "INTEGER CHECK(advancement BETWEEN 0 AND 5)",
        "advancement_verified_at": "TEXT", "advancement_source": "TEXT",
    }.items():
        if column not in columns(conn, "account_tactics"):
            conn.execute(f"ALTER TABLE account_tactics ADD COLUMN {column} {definition}")
    conn.execute("DELETE FROM account_generals")
    conn.execute("DELETE FROM account_tactics")
    verified = payload["verified_at"]
    for row in generals:
        # Inventory evidence proves identity and quality, not reference stats.
        conn.execute("""INSERT INTO generals(name,quality,faction,first_season,updated_at)
            VALUES(?,'金',?,?,?) ON CONFLICT(name) DO UPDATE SET
            quality='金',faction=excluded.faction,
            first_season=COALESCE(excluded.first_season,generals.first_season)""",
            (row["name"], row["faction"], row.get("first_season"), verified))
        gid = conn.execute("SELECT id FROM generals WHERE name=?", (row["name"],)).fetchone()[0]
        conn.execute("""INSERT INTO account_generals
            (general_id,variant,availability,level,advancement,current_team,last_verified_at,notes)
            VALUES(?,?,?,?,?,?,?,?)""", (gid, row.get("variant", "普通"),
            row.get("availability", "常驻"), row.get("level"), row["advancement"], row.get("current_team"), row.get("verified_at", verified),
            row.get("notes", payload["source"])))
    for row in tactics:
        conn.execute("""INSERT INTO tactics(name,quality,first_season,updated_at)
            VALUES(?,?,?,?) ON CONFLICT(name) DO UPDATE SET quality=excluded.quality,
            first_season=COALESCE(excluded.first_season,tactics.first_season)""",
            (row["name"], row["quality"], row.get("first_season"), verified))
        tid = conn.execute("SELECT id FROM tactics WHERE name=?", (row["name"],)).fetchone()[0]
        known = row["advancement"] is not None
        conn.execute("""INSERT INTO account_tactics(tactic_id,level,advancement,
            advancement_verified_at,advancement_source,last_verified_at,notes)
            VALUES(?,?,?,?,?,?,?)""", (tid, row.get("level"), row["advancement"],
            payload["tactic_advancement_verified_at"] if known else None,
            payload["tactic_advancement_source"] if known else None, verified,
            "红度沿用历史核定，本次未展示" if known else "红度未知，本次截图未展示"))
    purple = "SELECT id FROM generals WHERE quality='紫'"
    conn.execute(f"DELETE FROM general_stat_observations WHERE general_id IN ({purple})")
    conn.execute(f"UPDATE strategy_books SET exclusive_general_id=NULL WHERE exclusive_general_id IN ({purple})")
    conn.execute(f"DELETE FROM generals WHERE id IN ({purple})")
    for key, value in {"schema_version": "3", "default_season": payload["season"],
                       "inventory_verified_at": verified}.items():
        conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", (key, value))


def apply_max_level_policy(conn):
    conn.execute("DELETE FROM tactic_level_observations WHERE level<>10")
    if "description_level" not in columns(conn, "tactics"):
        conn.execute("ALTER TABLE tactics ADD COLUMN description_level INTEGER CHECK(description_level=10)")
    # Unlabelled legacy descriptions include level-1 values. Never guess scaling.
    conn.execute("UPDATE tactics SET description_raw=NULL,activation_rate=NULL WHERE description_level IS NULL")
    conn.execute("DELETE FROM tactic_effects")
    rows = conn.execute("""SELECT o.tactic_id,o.activation_rate,o.effect_raw,
            o.verification_status,o.source_id FROM tactic_level_observations o
            JOIN sources s ON s.id=o.source_id WHERE o.level=10
            ORDER BY s.trust_rank,o.observed_at,o.id""").fetchall()
    for tid, rate, effect, status, source in rows:
        conn.execute("""UPDATE tactics SET description_raw=?,description_level=10,
            activation_rate=?,verification_status=?,source_id=? WHERE id=?""",
            (effect, rate, status, source, tid))
    for tid, effect in conn.execute("SELECT id,description_raw FROM tactics WHERE description_level=10"):
        for eid, name in conn.execute("SELECT id,name FROM effects"):
            if name in effect and name not in {"特殊增益状态", "常规负面状态", "控制状态", "属性降低状态"}:
                conn.execute("INSERT OR IGNORE INTO tactic_effects VALUES(?,?,?,?)",
                             (tid, eid, "产生或依赖", effect))


def create_views(conn):
    statements = [
        "DROP VIEW IF EXISTS v_owned_generals",
        """CREATE VIEW v_owned_generals AS SELECT g.name,a.variant,a.availability,
            g.faction,a.advancement,a.last_verified_at,
            CASE WHEN a.variant='普通' THEN s.force END AS force,
            CASE WHEN a.variant='普通' THEN s.intelligence END AS intelligence,
            CASE WHEN a.variant='普通' THEN s.command END AS command,
            CASE WHEN a.variant='普通' THEN s.initiative END AS initiative,
            CASE WHEN a.variant<>'普通' THEN '英雄版本四维未核定'
                 ELSE '50级未加点估算，误差约1点；不含红度自由点' END AS stat_basis
            FROM account_generals a JOIN generals g ON g.id=a.general_id
            LEFT JOIN v_general_level50_estimate s ON s.name=g.name""",
        "DROP VIEW IF EXISTS v_owned_tactics",
        """CREATE VIEW v_owned_tactics AS SELECT t.name,t.quality,a.advancement,
            a.advancement_verified_at,a.advancement_source,a.last_verified_at,
            t.tactic_type,t.activation_rate,t.description_level,t.description_raw AS max_level_effect,
            CASE WHEN t.description_level=10 THEN t.verification_status
                 ELSE '缺少可信满级详情，不使用旧低等级正文' END AS detail_status,
            s.url AS detail_source
            FROM account_tactics a JOIN tactics t ON t.id=a.tactic_id
            LEFT JOIN sources s ON s.id=t.source_id""",
    ]
    for sql in statements:
        conn.execute(sql)


def write_report(conn):
    generals = conn.execute("SELECT * FROM v_owned_generals ORDER BY faction,name,variant").fetchall()
    tactics = conn.execute("SELECT * FROM v_owned_tactics ORDER BY quality,name").fetchall()
    verified = conn.execute("SELECT value FROM meta WHERE key='inventory_verified_at'").fetchone()[0]
    permanent = sum(r[2] == "常驻" for r in generals)
    gold = sum(r[1] == "金" for r in tactics)
    lines = ["# 当前武将战法库存", "", f"更新日期：{verified}。唯一种子：data/account_inventory.json。",
             f"{permanent}名常驻金将，另有{len(generals)-permanent}张限时快照；{gold}金色、{len(tactics)-gold}紫色战法。",
             "不维护当前等级、编队、携带者。紫色武将不入库。", "",
             "## 武将与50级默认四维", "",
             "四维顺序：武力、智力、统率、先攻。普通武将为未加点估算，约±1误差，不含50点等级自由点、红度自由点或战斗增益。英雄版不套普通版四维。", "",
             "| 武将 | 版本 | 状态 | 阵营 | 红度 | 50级四维 |", "| --- | --- | --- | --- | ---: | --- |"]
    for r in generals:
        stats = " / ".join(str(x) if x is not None else "未知" for x in r[6:10])
        lines.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {stats} |")
    lines += ["", "## 战法与红度", "",
              "红度日期2026-09-02表示沿用历史记录，本次截图未显示；未知不等于0红。满级正文仅采用有等级依据的资料。", "",
              "| 战法 | 品质 | 红度 | 红度核定日期 | 满级详情状态 |", "| --- | --- | ---: | --- | --- |"]
    for r in tactics:
        lines.append(f"| {r[0]} | {r[1]} | {r[2] if r[2] is not None else '未知'} | {r[3] or '未展示'} | {r[10]} |")
    lines += ["", "满级详情和来源请查询SQLite的v_owned_tactics；历史活动资料不是账号库存。", ""]
    (ROOT / "武将战法库存.md").write_text("\n".join(lines), encoding="utf-8")
    missing = [r[0] for r in tactics if r[8] != 10]
    report = ["# 当前库存覆盖率", "", f"- 常驻金将：{sum(r[2]=='常驻' for r in generals)}；限时快照：{sum(r[2]!='常驻' for r in generals)}。",
              f"- 战法：{len(tactics)}；已有可信满级详情：{len(tactics)-len(missing)}；缺口：{len(missing)}。",
              f"- 战法红度未知：{sum(r[2] is None for r in tactics)}；其余沿用2026-09-02记录。",
              "- 数据库不保留1至9级战法正文；旧网页快照和历史文档保留作原始归档，不用于当前满级计算。",
              "", "## 缺少满级详情的已有战法", "", "、".join(missing), ""]
    (DATA / "覆盖率报告.md").write_text("\n".join(report), encoding="utf-8")


def main():
    from sync_game_data import load_tactic_level_observations
    backup_dir = ROOT / "notes" / "backups" / "2026-09-08-1800" / "data"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup = backup_dir / DB.name
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys=ON")
    if not backup.exists():
        with sqlite3.connect(backup) as target:
            conn.backup(target)
    try:
        with conn:
            load_account(conn)
            load_tactic_level_observations(conn)
            apply_max_level_policy(conn)
            create_views(conn)
            assert conn.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
            assert not conn.execute("PRAGMA foreign_key_check").fetchall()
        write_report(conn)
        print(json.dumps({"backup": str(backup), "generals": conn.execute("SELECT count(*) FROM account_generals").fetchone()[0],
                          "tactics": conn.execute("SELECT count(*) FROM account_tactics").fetchone()[0]}, ensure_ascii=False))
    finally:
        conn.close()


if __name__ == "__main__":
    main()
