"""Verify inventory, max-level semantics, foreign keys and replay safety."""
from __future__ import annotations
import json
import sqlite3
from pathlib import Path
from account_inventory import load_account, apply_max_level_policy, create_views
from sync_game_data import load_tactic_level_observations, seed_steam_data

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "三国谋定天下_Steam_S1.sqlite3"


def check(conn, require_stats=True):
    payload = json.loads((ROOT / "data/account_inventory.json").read_text(encoding="utf-8"))
    assert conn.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
    assert not conn.execute("PRAGMA foreign_key_check").fetchall()
    actual = set(conn.execute("""SELECT g.name,a.variant,a.advancement FROM account_generals a
        JOIN generals g ON g.id=a.general_id"""))
    expected = {(r["name"],r.get("variant","普通"),r["advancement"]) for r in payload["generals"]}
    assert actual == expected
    assert len(actual) == 45
    assert ("张梁","普通",2) in actual and ("张梁","英雄",3) in actual
    assert {("夏侯渊","普通",1),("张飞","普通",1),("小乔","普通",1)} <= actual
    tactics = set(conn.execute("""SELECT t.name,t.quality,a.advancement FROM account_tactics a
        JOIN tactics t ON t.id=a.tactic_id"""))
    assert tactics == {(r["name"],r["quality"],r["advancement"]) for r in payload["tactics"]}
    assert len(tactics) == 62 and sum(r[1]=="紫" for r in tactics) == 31
    assert ("破军袭敌","金",None) in tactics
    assert ("烈火焚营","金",2) in tactics
    assert conn.execute("SELECT count(*) FROM generals WHERE quality='紫'").fetchone()[0] == 0
    assert conn.execute("""SELECT count(*) FROM account_generals a JOIN generals g ON g.id=a.general_id
        WHERE g.quality<>'金' OR a.level IS NOT NULL OR a.current_team IS NOT NULL""").fetchone()[0] == 0
    assert conn.execute("SELECT count(*) FROM account_tactics WHERE level IS NOT NULL OR current_holder IS NOT NULL").fetchone()[0] == 0
    assert conn.execute("SELECT count(*) FROM tactic_level_observations WHERE level<>10").fetchone()[0] == 0
    assert conn.execute("SELECT count(*) FROM tactics WHERE description_raw IS NOT NULL AND description_level IS NOT 10").fetchone()[0] == 0
    assert conn.execute("SELECT count(*) FROM v_owned_generals WHERE availability='常驻'").fetchone()[0] == 44
    assert conn.execute("SELECT force FROM v_owned_generals WHERE variant='英雄'").fetchone()[0] is None
    assert conn.execute("SELECT value FROM meta WHERE key='default_season'").fetchone()[0] == "s2"
    assert conn.execute("SELECT first_season FROM tactics WHERE name='韬光养晦'").fetchone()[0] == "s2"
    assert conn.execute("SELECT first_season FROM generals WHERE name='陆逊'").fetchone()[0] == "s2"
    if require_stats:
        assert conn.execute("""SELECT count(*) FROM v_owned_generals WHERE variant='普通'
            AND (force IS NULL OR intelligence IS NULL OR command IS NULL OR initiative IS NULL)""").fetchone()[0] == 0
        assert conn.execute("SELECT force FROM v_owned_generals WHERE name='甘宁'").fetchone()[0] == 225
    observations = json.loads((ROOT / "data/tactic_level_observations.json").read_text(encoding="utf-8-sig"))["observations"]
    for row in observations:
        if row["level"] == 10:
            stored = conn.execute("SELECT description_raw,description_level FROM tactics WHERE name=?", (row["name"],)).fetchone()
            assert stored == (row["effect_raw"], 10), row["name"]
    assert conn.execute("SELECT advancement FROM v_owned_tactics WHERE name='如有神助'").fetchone()[0] is None


def replay(conn):
    load_account(conn)
    seed_steam_data(conn)
    load_tactic_level_observations(conn)
    apply_max_level_policy(conn)
    create_views(conn)


def main():
    conn = sqlite3.connect(f"{DB.as_uri()}?mode=ro", uri=True)
    check(conn)
    memory = sqlite3.connect(":memory:")
    conn.backup(memory)
    memory.execute("PRAGMA foreign_keys=ON")
    replay(memory)
    check(memory)
    first = list(memory.iterdump())
    replay(memory)
    assert list(memory.iterdump()) == first, "Repeated import changed data"
    # A fresh schema must work too, independent of the migration path.
    fresh = sqlite3.connect(":memory:")
    fresh.executescript((ROOT / "data/schema.sql").read_text(encoding="utf-8"))
    fresh.execute("INSERT INTO generals(name,quality,updated_at) VALUES('紫将测试','紫','test')")
    replay(fresh)
    check(fresh, require_stats=False)
    try:
        fresh.execute("INSERT INTO account_generals(general_id,variant,level,last_verified_at) VALUES(1,'test',5,'test')")
    except sqlite3.IntegrityError:
        pass
    else:
        raise AssertionError("Current general level was accepted")
    report = {
        "integrity": "ok", "foreign_keys": "ok", "repeat_import": "ok", "fresh_schema": "ok",
        "permanent_gold_generals": 44, "temporary_hero_snapshots": 1,
        "tactics": 62, "purple_generals": 0, "level50_stat_coverage": "44/44",
        "known_owned_max_level_details": conn.execute("SELECT count(*) FROM v_owned_tactics WHERE description_level=10").fetchone()[0],
        "unknown_tactic_advancement": conn.execute("SELECT count(*) FROM account_tactics WHERE advancement IS NULL").fetchone()[0],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    memory.close()
    fresh.close()
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
