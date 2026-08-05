#!/usr/bin/env python3
"""Run high-signal integrity and business-rule checks for the local database."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "三国谋定天下_Steam_S1.sqlite3"


def row_dicts(cursor):
    return [dict(row) for row in cursor]


def main() -> int:
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    report = {
        "integrity": conn.execute("PRAGMA integrity_check").fetchone()[0],
        "counts": dict(conn.execute(
            """SELECT
            (SELECT count(*) FROM generals) AS generals,
            (SELECT count(*) FROM v_s1_generals) AS s1_generals,
            (SELECT count(*) FROM tactics) AS tactics,
            (SELECT count(*) FROM v_s1_tactics) AS s1_tactics,
            (SELECT count(*) FROM effects) AS effects,
            (SELECT count(*) FROM bonds) AS bonds,
            (SELECT count(*) FROM tactic_effects) AS tactic_effects,
            (SELECT count(*) FROM account_generals) AS account_generals,
            (SELECT count(*) FROM account_tactics) AS account_tactics"""
        ).fetchone()),
        "s1_missing_four_stats": conn.execute(
            """SELECT count(*) FROM v_s1_generals
               WHERE base_force IS NULL OR growth_force IS NULL
                  OR base_intelligence IS NULL OR growth_intelligence IS NULL
                  OR base_command IS NULL OR growth_command IS NULL
                  OR base_initiative IS NULL OR growth_initiative IS NULL"""
        ).fetchone()[0],
        "tactics_missing_full_description": conn.execute(
            "SELECT count(*) FROM tactics WHERE description_raw IS NULL"
        ).fetchone()[0],
        "missing_description_names": [row[0] for row in conn.execute(
            "SELECT name FROM tactics WHERE description_raw IS NULL ORDER BY name"
        )],
        "level50_unallocated": row_dicts(conn.execute(
            "SELECT * FROM v_general_level50_estimate WHERE name IN ('大乔','甘宁') ORDER BY name"
        )),
        "steam_observations": row_dicts(conn.execute(
            """SELECT g.name,o.allocated_force,o.allocated_intelligence,
                      o.observed_force,o.observed_intelligence,o.observed_command,
                      o.observed_initiative,o.context
               FROM general_stat_observations o
               JOIN generals g ON g.id=o.general_id ORDER BY g.name"""
        )),
        "jiangbiao": row_dicts(conn.execute(
            """SELECT b.name,b.activation_count,b.effect_raw,b.verification_status,
                      count(bm.general_id) AS members
               FROM bonds b LEFT JOIN bond_members bm ON bm.bond_id=b.id
               WHERE b.name='江表虎臣' GROUP BY b.id"""
        )),
    }
    conn.close()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    checks = [
        report["integrity"] == "ok",
        report["counts"]["s1_generals"] > 0,
        report["s1_missing_four_stats"] == 0,
        report["counts"]["account_generals"] == 17,
        report["counts"]["account_tactics"] == 36,
        len(report["steam_observations"]) == 2,
    ]
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
