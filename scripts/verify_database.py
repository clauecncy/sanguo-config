#!/usr/bin/env python3
"""Run high-signal integrity and business-rule checks for the local database."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "三国谋定天下_Steam_S1.sqlite3"
INVENTORY = ROOT / "data" / "account_inventory.json"


def row_dicts(cursor):
    return [dict(row) for row in cursor]


def main() -> int:
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    report = {
        "integrity": conn.execute("PRAGMA integrity_check").fetchone()[0],
        "counts": dict(conn.execute(
            """SELECT
            (SELECT count(*) FROM generals) AS generals,
            (SELECT count(*) FROM v_s1_generals) AS s1_generals,
            (SELECT count(*) FROM v_s1_gold_generals) AS s1_gold_generals,
            (SELECT count(*) FROM tactics) AS tactics,
            (SELECT count(*) FROM v_s1_tactics) AS s1_tactics,
            (SELECT count(*) FROM v_recommendable_tactics) AS recommendable_tactics,
            (SELECT count(*) FROM v_recommendable_strategy_books) AS recommendable_strategy_books,
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
        "hebei": row_dicts(conn.execute(
            """SELECT b.name,b.activation_count,b.effect_raw,b.verification_status,
                      count(bm.general_id) AS members
               FROM bonds b LEFT JOIN bond_members bm ON bm.bond_id=b.id
               WHERE b.name='河北庭将' GROUP BY b.id"""
        )),
        "account_out_of_scope_generals": conn.execute(
            "SELECT count(*) FROM account_generals a JOIN generals g ON g.id=a.general_id WHERE g.quality<>'金' OR g.quality IS NULL"
        ).fetchone()[0],
        "account_out_of_scope_tactics": conn.execute(
            "SELECT count(*) FROM account_tactics a JOIN tactics t ON t.id=a.tactic_id WHERE t.quality NOT IN ('金','紫') OR t.quality IS NULL"
        ).fetchone()[0],
        "latest_inventory_checks": row_dicts(conn.execute(
            """SELECT '武将' AS kind,g.name,a.level,g.quality,a.current_team AS status,
                      g.verification_status
               FROM account_generals a JOIN generals g ON g.id=a.general_id
               WHERE g.name IN ('关平','关羽','徐晃','夏侯渊','徐庶','周仓')
               UNION ALL
               SELECT '战法',t.name,a.level,t.quality,COALESCE(a.current_holder,'未装备'),
                      t.verification_status
               FROM account_tactics a JOIN tactics t ON t.id=a.tactic_id
               WHERE t.name IN ('锐不可当','烈火焚营','乘虚而入','勇冠三军','上兵伐谋','临危勇烈')
               ORDER BY kind,name"""
        )),
    }
    conn.close()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    checks = [
        report["integrity"] == "ok",
        report["counts"]["s1_generals"] > 0,
        report["s1_missing_four_stats"] == 0,
        report["counts"]["account_generals"] == len(inventory["generals"]),
        report["counts"]["account_tactics"] == len(inventory["tactics"]),
        report["account_out_of_scope_generals"] == 0,
        report["account_out_of_scope_tactics"] == 0,
        len(report["steam_observations"]) == 2,
        len(report["hebei"]) == 1 and report["hebei"][0]["activation_count"] == 2,
        len(report["latest_inventory_checks"]) == 12,
    ]
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
