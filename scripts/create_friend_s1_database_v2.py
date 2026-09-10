"""Build the friend S1 database, including screenshot-only purple generals."""
from __future__ import annotations

import json
import shutil
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "朋友S1" / "data" / "三国谋定天下_朋友_S1.sqlite3"
SOURCE = ROOT / "data" / "三国谋定天下_Steam_S1.sqlite3"
SEED = ROOT / "朋友S1" / "data" / "account_inventory.json"


def main() -> None:
    if TARGET.exists():
        raise FileExistsError(f"Refusing to overwrite {TARGET}")
    shutil.copy2(SOURCE, TARGET)
    payload = json.loads(SEED.read_text(encoding="utf-8"))
    conn = sqlite3.connect(TARGET)
    try:
        conn.execute("PRAGMA foreign_keys=ON")
        conn.execute("DELETE FROM account_generals")
        conn.execute("DELETE FROM account_tactics")
        for item in payload["generals"]:
            quality = item.get("quality", "金")
            row = conn.execute("SELECT id, quality FROM generals WHERE name=?", (item["name"],)).fetchone()
            if row is None:
                conn.execute(
                    """INSERT INTO generals(name, faction, quality, first_season, updated_at,
                       verification_status, strategy_recommendation_status)
                       VALUES (?, ?, ?, 's1', ?, '截图已核', '待可靠来源')""",
                    (item["name"], item["faction"], quality, payload["verified_at"]),
                )
                row = conn.execute("SELECT id, quality FROM generals WHERE name=?", (item["name"],)).fetchone()
            if row[1] != quality:
                raise ValueError(f"General quality mismatch: {item['name']}")
            conn.execute(
                """INSERT INTO account_generals
                   (general_id, variant, availability, advancement, last_verified_at, notes)
                   VALUES (?, '普通', '常驻', ?, ?, ?)""",
                (row[0], item["advancement"], payload["verified_at"], payload["source"]),
            )
        for item in payload["tactics"]:
            row = conn.execute("SELECT id, quality FROM tactics WHERE name=?", (item["name"],)).fetchone()
            if row is None or row[1] != item["quality"]:
                raise ValueError(f"Tactic reference mismatch: {item['name']}")
            conn.execute(
                """INSERT INTO account_tactics(tactic_id, last_verified_at, notes)
                   VALUES (?, ?, ?)""",
                (row[0], payload["verified_at"], payload["source"]),
            )
        conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('default_season','s1')")
        conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('account_label','朋友S1')")
        conn.commit()
        assert conn.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
        assert not conn.execute("PRAGMA foreign_key_check").fetchall()
        assert conn.execute("SELECT count(*) FROM account_generals").fetchone()[0] == 52
        assert conn.execute("SELECT count(*) FROM account_tactics").fetchone()[0] == 23
    except Exception:
        conn.close()
        TARGET.unlink(missing_ok=True)
        raise
    conn.close()
    print(TARGET)


if __name__ == "__main__":
    main()
