#!/usr/bin/env python3
"""Synchronize the local 三国谋定天下 database from public reference pages.

The database deliberately separates network reference data from Steam screenshot
overrides. Network values are never allowed to silently replace Steam-confirmed
facts.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import re
import sqlite3
import ssl
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

from lxml import html


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DEFAULT_DB = DATA_DIR / "三国谋定天下_Steam_S1.sqlite3"
BASE_URL = "https://www.sgmdtx.com"
WIKI_URL = "https://wiki.ldmnq.com/sanguo_modingtianxia"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) CodexLocalGameArchive/1.0"
NOW = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).isoformat(timespec="seconds")


def clean_text(node) -> str:
    return " ".join("".join(node.itertext()).replace("\xa0", " ").split())


def fetch(url: str, attempts: int = 3) -> str:
    encoded_url = urllib.parse.quote(url, safe=":/?=&%")
    request = urllib.request.Request(encoded_url, headers={"User-Agent": USER_AGENT})
    context = ssl.create_default_context()
    error = None
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=25, context=context) as response:
                return response.read().decode("utf-8")
        except Exception as exc:  # Network failures are retried and logged by caller.
            error = exc
            time.sleep(0.6 * (attempt + 1))
    raise RuntimeError(f"GET {url} failed: {error}")


def unique_detail_links(list_url: str, prefix: str) -> list[str]:
    # List pages are hydrated client-side, while the public sitemap is complete
    # and stable enough for reproducible crawling.
    sitemap = html.fromstring(fetch(f"{BASE_URL}/sitemap-0.xml").encode("utf-8"))
    urls = {
        value.strip()
        for value in sitemap.xpath("//*[local-name()='loc']/text()")
        if f"{prefix}" in value
    }
    if urls:
        return sorted(urls)
    # Fallback for a future sitemap layout change.
    doc = html.fromstring(fetch(list_url))
    paths = {a.get("href") for a in doc.xpath(f"//a[starts-with(@href, '{prefix}')]") if a.get("href")}
    return [urllib.parse.urljoin(BASE_URL, path) for path in sorted(paths)]


def chip_texts(doc) -> list[str]:
    values = []
    for node in doc.xpath("//main//div[contains(@class, 'MuiChip-root')]"):
        value = clean_text(node)
        if value and value not in values:
            values.append(value)
    return values


def parse_stat(doc, label: str) -> tuple[float | None, float | None]:
    nodes = doc.xpath(f"//*[@role='group' and @aria-label='{label}']")
    if not nodes:
        return None, None
    text = clean_text(nodes[0])
    match = re.search(rf"{label}\s*([0-9.]+)\s*\(([0-9.]+)\)", text)
    if not match:
        return None, None
    return float(match.group(1)), float(match.group(2))


def parse_general(url: str) -> dict:
    doc = html.fromstring(fetch(url))
    headings = doc.xpath("//main//h5")
    if not headings:
        raise ValueError(f"No general heading: {url}")
    name = clean_text(headings[0])
    chips = chip_texts(doc)
    faction = next((v for v in chips if v in {"魏", "蜀", "吴", "群"}), None)
    troop_type = next((v for v in chips if v in {"盾", "弓", "枪", "骑"}), None)
    season = next((v.lower() for v in chips if re.fullmatch(r"s\d+", v.lower())), None)

    stats = {label: parse_stat(doc, label) for label in ("武力", "智力", "统帅", "先攻")}
    tactic_links = doc.xpath("//p[normalize-space()='自带战法']/following::a[starts-with(@href, '/zf/')][1]")
    self_tactic = None
    self_tactic_url = None
    if tactic_links:
        self_tactic_url = urllib.parse.urljoin(BASE_URL, tactic_links[0].get("href"))
        self_tactic = urllib.parse.unquote(tactic_links[0].get("href").strip("/").split("/")[-1])

    bonds = []
    for heading in doc.xpath("//main//h6[@aria-label]"):
        bond_name = clean_text(heading)
        effect = heading.get("aria-label") or ""
        container = heading.getparent()
        members = []
        for _ in range(7):
            anchors = container.xpath(".//a[starts-with(@href, '/wj/')]")
            current = []
            for anchor in anchors:
                href = anchor.get("href")
                member = urllib.parse.unquote(href.strip("/").split("/")[-1])
                if member not in current:
                    current.append(member)
            if current:
                members = current
                break
            container = container.getparent()
            if container is None:
                break
        bonds.append({"name": bond_name, "effect": effect, "members": members})

    return {
        "name": name,
        "url": url,
        "faction": faction,
        "troop_type": troop_type,
        "season": season,
        "base_force": stats["武力"][0],
        "growth_force": stats["武力"][1],
        "base_intelligence": stats["智力"][0],
        "growth_intelligence": stats["智力"][1],
        "base_command": stats["统帅"][0],
        "growth_command": stats["统帅"][1],
        "base_initiative": stats["先攻"][0],
        "growth_initiative": stats["先攻"][1],
        "self_tactic": self_tactic,
        "self_tactic_url": self_tactic_url,
        "bonds": bonds,
    }


def field_after_label(doc, label: str) -> str | None:
    labels = doc.xpath(f"//main//p[normalize-space()='{label}']")
    if not labels:
        return None
    following = labels[0].xpath("following::p[1]")
    return clean_text(following[0]) if following else None


def parse_tactic(url: str) -> dict:
    doc = html.fromstring(fetch(url))
    headings = doc.xpath("//main//h5")
    if not headings:
        raise ValueError(f"No tactic heading: {url}")
    name = clean_text(headings[0])
    chips = chip_texts(doc)
    tactic_types = {"主动", "追击", "指挥", "被动"}
    damage_types = {"兵刃", "谋略", "治疗", "辅助", "防御", "文武"}
    tactic_type = next((v for v in chips if v in tactic_types), None)
    damage_type = next((v for v in chips if v in damage_types), None)
    activation_rate = field_after_label(doc, "发动概率")
    description = None
    desc_headings = doc.xpath("//main//h5[normalize-space()='战法说明']")
    if desc_headings:
        paragraphs = desc_headings[0].xpath("following::p[1]")
        description = clean_text(paragraphs[0]) if paragraphs else None
    troop_names = []
    for value in ("盾兵", "弓兵", "长枪兵", "骑兵"):
        if doc.xpath(f"//main//*[normalize-space()='{value}']"):
            troop_names.append(value)
    return {
        "name": name,
        "url": url,
        "tactic_type": tactic_type,
        "damage_type": damage_type,
        "activation_rate": activation_rate,
        "troop_limit": "、".join(troop_names) if troop_names else None,
        "description": description,
    }


def parse_effects(url: str) -> list[dict]:
    doc = html.fromstring(fetch(url))
    result = []
    for table in doc.xpath("//table"):
        heading = table.xpath("preceding::*[self::h2 or self::h3][1]")
        category = clean_text(heading[0]) if heading else "未分类"
        for row in table.xpath(".//tbody/tr"):
            cells = [clean_text(cell) for cell in row.xpath("./th|./td")]
            if len(cells) < 2 or not cells[0]:
                continue
            result.append({
                "name": cells[0],
                "category": category,
                "exact_effect": cells[1],
                "functional": any("功能" in cell for cell in cells[2:]),
                "control": any("控制" in cell for cell in cells[2:]),
            })
    return result


def wiki_catalog(section: str) -> list[tuple[str, str]]:
    index_url = f"{WIKI_URL}/{section}/"
    doc = html.fromstring(fetch(index_url))
    result = {}
    for anchor in doc.xpath(f"//a[contains(@href, '/{section}/')]"):
        href = anchor.get("href") or ""
        name = clean_text(anchor)
        if not name or not href.endswith(".html"):
            continue
        result[name] = urllib.parse.urljoin(index_url, href)
    return sorted(result.items())


def wiki_tactic_quality_catalog() -> list[dict]:
    index_url = f"{WIKI_URL}/zhanfa/"
    doc = html.fromstring(fetch(index_url))
    colors = {"#FFFF33": "金", "#871F78": "紫", "#38B0DE": "蓝"}
    result = []
    for anchor in doc.xpath("//a[contains(@href, '/zhanfa/')]"):
        href = anchor.get("href") or ""
        name = clean_text(anchor)
        if not name or not href.endswith(".html"):
            continue
        style = " ".join(anchor.xpath(".//*[@style]/@style"))
        quality = next((value for color, value in colors.items() if color.lower() in style.lower()), None)
        result.append({
            "name": name,
            "url": urllib.parse.urljoin(index_url, href),
            "quality": quality,
            "combat_role": None,
        })
    return sorted(result, key=lambda row: row["name"])


def parse_wiki_quality(item: tuple[str, str], include_role: bool = False) -> dict:
    name, url = item
    doc = html.fromstring(fetch(url))
    body = clean_text(doc)
    quality = None
    for marker, value in (("橙卡", "金"), ("紫卡", "紫"), ("蓝卡", "蓝")):
        if marker in body:
            quality = value
            break
    role = None
    if include_role:
        match = re.search(r"战法推荐\s*主[：:]\s*(兵刃|谋略|治疗|防御|辅助|文武)", body)
        role = match.group(1) if match else None
    return {"name": name, "url": url, "quality": quality, "combat_role": role}


def parallel_parse(urls: list[str], parser, workers: int) -> tuple[list[dict], list[str]]:
    rows, errors = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(parser, url): url for url in urls}
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                rows.append(future.result())
            except Exception as exc:
                errors.append(f"{url}: {exc}")
    rows.sort(key=lambda row: row["name"])
    return rows, errors


def source_id(conn: sqlite3.Connection, name: str, url: str, source_type: str,
              trust_rank: int, platform: str | None = None,
              season: str | None = None, notes: str | None = None) -> int:
    conn.execute(
        """INSERT INTO sources(name,url,source_type,platform,season,trust_rank,fetched_at,notes)
           VALUES(?,?,?,?,?,?,?,?)
           ON CONFLICT(name,url) DO UPDATE SET fetched_at=excluded.fetched_at, notes=excluded.notes""",
        (name, url, source_type, platform, season, trust_rank, NOW, notes),
    )
    return conn.execute("SELECT id FROM sources WHERE name=? AND url=?", (name, url)).fetchone()[0]


def upsert_tactic(conn: sqlite3.Connection, row: dict, src_id: int) -> int:
    conn.execute(
        """INSERT INTO tactics(name,url,tactic_type,damage_type,activation_rate,troop_limit,
                               description_raw,verification_status,source_id,updated_at)
           VALUES(?,?,?,?,?,?,?,?,?,?)
           ON CONFLICT(name) DO UPDATE SET url=excluded.url,tactic_type=excluded.tactic_type,
             damage_type=excluded.damage_type,activation_rate=excluded.activation_rate,
             troop_limit=excluded.troop_limit,
             description_raw=COALESCE(excluded.description_raw,tactics.description_raw),
             source_id=excluded.source_id,updated_at=excluded.updated_at""",
        (row["name"], row.get("url"), row.get("tactic_type"), row.get("damage_type"),
         row.get("activation_rate"), row.get("troop_limit"), row.get("description"),
         "跨赛季参考", src_id, NOW),
    )
    return conn.execute("SELECT id FROM tactics WHERE name=?", (row["name"],)).fetchone()[0]


def load_account(conn: sqlite3.Connection) -> None:
    inventory = json.loads((DATA_DIR / "account_inventory.json").read_text(encoding="utf-8"))
    verified = inventory["verified_at"]
    gold = {
        "威名显赫", "伏兵四起", "五雷轰顶", "王佐之才", "铁骑横冲",
        "势如破竹", "战八方", "清风驱疾", "无难之志", "攻其不备",
    }
    for name, level, team in inventory["generals"]:
        conn.execute(
            """INSERT INTO generals(name,quality,updated_at,verification_status) VALUES(?,?,?,?)
               ON CONFLICT(name) DO UPDATE SET quality='金',updated_at=excluded.updated_at,
               verification_status='Steam已核'""",
            (name, "金", NOW, "Steam已核"),
        )
        general_id = conn.execute("SELECT id FROM generals WHERE name=?", (name,)).fetchone()[0]
        conn.execute(
            """INSERT INTO account_generals(general_id,level,current_team,last_verified_at)
               VALUES(?,?,?,?) ON CONFLICT(general_id) DO UPDATE SET level=excluded.level,
               current_team=excluded.current_team,last_verified_at=excluded.last_verified_at""",
            (general_id, level, team, verified),
        )
    for name, level, holder in inventory["tactics"]:
        conn.execute(
            """INSERT INTO tactics(name,quality,first_season,verification_status,updated_at)
               VALUES(?,?,?,?,?) ON CONFLICT(name) DO UPDATE SET quality=excluded.quality,
               first_season='s1',verification_status='Steam已核',updated_at=excluded.updated_at""",
            (name, "金" if name in gold else "紫", "s1", "Steam已核", NOW),
        )
        tactic_id = conn.execute("SELECT id FROM tactics WHERE name=?", (name,)).fetchone()[0]
        conn.execute(
            """INSERT INTO account_tactics(tactic_id,level,current_holder,last_verified_at)
               VALUES(?,?,?,?) ON CONFLICT(tactic_id) DO UPDATE SET level=excluded.level,
               current_holder=excluded.current_holder,last_verified_at=excluded.last_verified_at""",
            (tactic_id, level, holder, verified),
        )


def seed_steam_data(conn: sqlite3.Connection) -> None:
    steam_src = source_id(
        conn, "用户Steam S1截图", "local:evidence/steam_s1/", "截图",
        100, "Steam", "s1", "按日期保存的当前账号游戏内截图；较新截图优先并覆盖网络资料。",
    )
    web_src = source_id(
        conn, "三谋助手资料站", BASE_URL, "第三方结构化资料", 60, None, None,
        "保存基础属性、成长、自带战法、缘分与战法正文；按赛季字段过滤。",
    )
    rules_src = source_id(
        conn, "武将系统说明", "https://www.taptap.cn/moment/531478269581592397",
        "官方社区攻略", 80, None, "s1", "每升一阶获得10点自由属性。",
    )
    strategy_src = source_id(
        conn, "韬略重修说明", "https://www.taptap.cn/moment/531462563137849323",
        "官方社区攻略", 80, None, "s1", "三个韬略位、重修随机三选一、专属韬略限制与保底。",
    )
    user_mechanic_src = source_id(
        conn, "用户当前机制说明", "local:conversation/2026-08-05", "用户口述", 90,
        "Steam", "s1", "每名武将可查看自己的可能获得韬略列表；抽取规则未知。",
    )
    formations = [
        ("一字阵", 3, 0, "前排受到伤害降低8%", "效果Steam已核；站位S1参考"),
        ("箕形阵", 1, 2, "前排受到伤害降低6%；后排造成伤害提升12%", "效果Steam已核；站位S1参考"),
        ("雁形阵", 2, 1, "前排统率提升20点；后排造成伤害提升15%", "Steam已核"),
        ("方圆阵", 2, 1, "前排受到伤害降低5%；后排普通攻击率提升40%", "效果Steam已核；站位S1参考"),
        ("锥形阵", 1, 2, "前排造成伤害提升16%；后排受到伤害降低5%", "效果Steam已核；站位S1参考"),
        ("鱼鳞阵", 1, 2, "前排规避率提升12%；后排会心、奇谋几率提升8%", "效果Steam已核；站位S1参考"),
    ]
    for name, front, rear, effect, status in formations:
        conn.execute(
            """INSERT INTO formations(name,front_slots,rear_slots,effect_raw,verification_status,source_id,updated_at)
               VALUES(?,?,?,?,?,?,?) ON CONFLICT(name) DO UPDATE SET front_slots=excluded.front_slots,
               rear_slots=excluded.rear_slots,effect_raw=excluded.effect_raw,
               verification_status=excluded.verification_status,source_id=excluded.source_id,updated_at=excluded.updated_at""",
            (name, front, rear, effect, status, steam_src, NOW),
        )
    rules = [
        ("level_stat", "displayed_estimate = round(base_level5 + displayed_growth * (level - 5)) + allocated",
         "网络基础四维为5级基准；公开成长只显示两位小数，推算裸面板可能与客户端相差1点。阈值判断优先使用general_stat_observations中的实测面板。", "Steam截图交叉核验；估算值需保留±1误差", steam_src),
        ("level_free_points", "10 * floor(level / 10)",
         "武将每到10的倍数等级获得10点自由属性；50级共50点。", "Steam截图与官方攻略交叉核验", rules_src),
        ("advancement_free_points", "10 * advancement",
         "武将每升一阶获得10点自由分配属性。", "官方社区攻略", rules_src),
    ]
    for key, formula, description, status, src in rules:
        conn.execute(
            """INSERT INTO progression_rules(rule_key,formula,description,verification_status,source_id)
               VALUES(?,?,?,?,?) ON CONFLICT(rule_key) DO UPDATE SET formula=excluded.formula,
               description=excluded.description,verification_status=excluded.verification_status,source_id=excluded.source_id""",
            (key, formula, description, status, src),
        )
    strategy_rules = [
        ("unlock_slots", "25、30、35级分别解锁第1、2、3个韬略位。", "官方社区攻略", rules_src),
        ("refit_requires_three", "三本韬略全部研读后才能开启重修。", "官方社区攻略", strategy_src),
        ("refit_three_choices", "每次选择一本韬略重修，该韬略随机出现3个选项，可保留重修前结果。", "官方社区攻略", strategy_src),
        ("exclusive_limit", "一名武将同时只能应用1个专属韬略；同一武将可能存在多个专属候选。", "官方社区攻略", strategy_src),
        ("exclusive_guarantee", "单将10次重修内必出专属；出过专属且仍有其他专属时，后续3次内再出专属，但可能重复。", "官方社区攻略", strategy_src),
        ("candidate_list", "每名武将均可查看自己的可能获得韬略列表；应按武将逐项保存候选关系。", "Steam截图已核", steam_src),
        ("draw_algorithm", "候选列表如何生成、各韬略抽取权重及是否按职业共享池，目前未知。", "待Steam或官方规则核验", user_mechanic_src),
    ]
    for key, text, status, src in strategy_rules:
        conn.execute(
            """INSERT INTO strategy_rules(rule_key,rule_text,verification_status,source_id)
               VALUES(?,?,?,?) ON CONFLICT(rule_key) DO UPDATE SET rule_text=excluded.rule_text,
               verification_status=excluded.verification_status,source_id=excluded.source_id""",
            (key, text, status, src),
        )
    visible_books = [
        ("神勇", "金", "金色候选（归属待确认）", "自身规避率和倒戈提升5%"),
        ("作战·善本", "紫", "通用候选", "兵刃伤害提升6.5%"),
        ("胜战·善本", "紫", "通用候选", "战斗前4回合，兵刃伤害提升8%"),
        ("久战·善本", "紫", "通用候选", "造成兵刃伤害后，兵刃伤害提升1.8%，最多叠加5次"),
    ]
    for name, quality, scope, effect in visible_books:
        conn.execute(
            """INSERT INTO strategy_books(name,quality,book_scope,effect_raw,source_id)
               VALUES(?,?,?,?,?) ON CONFLICT(name) DO UPDATE SET quality=excluded.quality,
               book_scope=excluded.book_scope,effect_raw=excluded.effect_raw,source_id=excluded.source_id""",
            (name, quality, scope, effect, steam_src),
        )
    observations = [
        ("大乔", 50, None, 0, 50, 0, 0, 40, 242, 182, 113, "演武大会固定50级，全智力+50"),
        ("甘宁", 50, None, 50, 0, 0, 0, 275, 144, 186, 188, "演武大会固定50级，全武力+50"),
    ]
    for row in observations:
        general = conn.execute("SELECT id FROM generals WHERE name=?", (row[0],)).fetchone()
        if not general:
            continue
        exists = conn.execute(
            "SELECT 1 FROM general_stat_observations WHERE general_id=? AND context=?", (general[0], row[-1])
        ).fetchone()
        if not exists:
            conn.execute(
                """INSERT INTO general_stat_observations(
                   general_id,level,advancement,allocated_force,allocated_intelligence,
                   allocated_command,allocated_initiative,observed_force,observed_intelligence,
                   observed_command,observed_initiative,context,source_id,observed_at)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (general[0], *row[1:-1], row[-1], steam_src, "2026-08-05"),
            )
    conn.execute(
        "UPDATE generals SET faction='吴', verification_status='Steam已核' WHERE name='徐盛'"
    )
    conn.execute(
        "UPDATE bonds SET activation_count=2, effect_raw='部队中缘分武将统率提升10点，受到伤害降低3%', verification_status='Steam已核', source_id=? WHERE name='江表虎臣'",
        (steam_src,),
    )
    conn.execute(
        "UPDATE bonds SET activation_count=2, effect_raw='部队中缘分武将武力提升20点', verification_status='Steam已核', source_id=? WHERE name='河北庭将'",
        (steam_src,),
    )
    conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('network_source_id',?)", (str(web_src),))


def write_database(db_path: Path, snapshot_path: Path, workers: int) -> tuple[dict, list[str]]:
    started = NOW
    general_urls = unique_detail_links(f"{BASE_URL}/wujiang/", "/wj/")
    tactic_urls = unique_detail_links(f"{BASE_URL}/zhanfa/", "/zf/")
    generals, general_errors = parallel_parse(general_urls, parse_general, workers)
    tactics, tactic_errors = parallel_parse(tactic_urls, parse_tactic, workers)
    # A few pages occasionally return partially hydrated HTML. Retry incomplete
    # records once in sequence before accepting a coverage gap.
    for index, row in enumerate(generals):
        if any(row.get(key) is None for key in ("base_force", "growth_force", "base_initiative", "growth_initiative")):
            try:
                generals[index] = parse_general(row["url"])
            except Exception as exc:
                general_errors.append(f"retry {row['url']}: {exc}")
    for index, row in enumerate(tactics):
        if not row.get("description"):
            try:
                tactics[index] = parse_tactic(row["url"])
            except Exception as exc:
                tactic_errors.append(f"retry {row['url']}: {exc}")
    effects = parse_effects(f"{BASE_URL}/buff/")
    wiki_generals, wiki_general_errors = parallel_parse(
        wiki_catalog("wujiangtujian"), lambda item: parse_wiki_quality(item, True), workers
    )
    wiki_tactics = wiki_tactic_quality_catalog()
    wiki_tactic_errors = []
    errors = general_errors + tactic_errors + wiki_general_errors + wiki_tactic_errors

    snapshot = {
        "generated_at": NOW,
        "source": BASE_URL,
        "generals": generals,
        "tactics": tactics,
        "effects": effects,
        "quality_reference": {"generals": wiki_generals, "tactics": wiki_tactics},
        "errors": errors,
    }
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")

    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path)
    conn.executescript((DATA_DIR / "schema.sql").read_text(encoding="utf-8"))
    src_id = source_id(conn, "三谋助手资料站", BASE_URL, "第三方结构化资料", 60)
    buff_src_id = source_id(conn, "三谋助手状态词典", f"{BASE_URL}/buff/", "第三方状态资料", 65)
    quality_src_id = source_id(
        conn, "雷电模拟器三谋图鉴", f"{WIKI_URL}/", "第三方品质参考", 50,
        notes="仅补充金/紫/蓝品质和武将主定位；不覆盖Steam截图。",
    )
    conn.execute("INSERT INTO sync_runs(started_at,status) VALUES(?,?)", (started, "running"))
    run_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

    tactic_ids = {}
    for row in tactics:
        tactic_ids[row["name"]] = upsert_tactic(conn, row, src_id)
    for row in generals:
        if row.get("self_tactic") and row["self_tactic"] not in tactic_ids:
            detail = {"name": row["self_tactic"], "url": row.get("self_tactic_url")}
            if row.get("self_tactic_url"):
                try:
                    detail = parse_tactic(row["self_tactic_url"])
                except Exception as exc:
                    errors.append(f"self tactic {row['self_tactic_url']}: {exc}")
            tactic_ids[row["self_tactic"]] = upsert_tactic(conn, detail, src_id)
        conn.execute(
            """INSERT INTO generals(name,url,faction,troop_type,first_season,reference_level,
               base_force,growth_force,base_intelligence,growth_intelligence,base_command,growth_command,
               base_initiative,growth_initiative,self_tactic_id,verification_status,source_id,updated_at)
               VALUES(?,?,?,?,?,5,?,?,?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(name) DO UPDATE SET url=excluded.url,faction=excluded.faction,
               troop_type=excluded.troop_type,first_season=excluded.first_season,
               base_force=excluded.base_force,growth_force=excluded.growth_force,
               base_intelligence=excluded.base_intelligence,growth_intelligence=excluded.growth_intelligence,
               base_command=excluded.base_command,growth_command=excluded.growth_command,
               base_initiative=excluded.base_initiative,growth_initiative=excluded.growth_initiative,
               self_tactic_id=excluded.self_tactic_id,source_id=excluded.source_id,updated_at=excluded.updated_at""",
            (row["name"], row["url"], row["faction"], row["troop_type"], row["season"],
             row["base_force"], row["growth_force"], row["base_intelligence"], row["growth_intelligence"],
             row["base_command"], row["growth_command"], row["base_initiative"], row["growth_initiative"],
             tactic_ids.get(row.get("self_tactic")),
             "S1参考" if row.get("season") == "s1" else "跨赛季参考", src_id, NOW),
        )
        if row.get("season") == "s1" and row.get("self_tactic"):
            conn.execute(
                "UPDATE tactics SET first_season=COALESCE(first_season,'s1'),is_self_tactic=1 WHERE id=?",
                (tactic_ids.get(row.get("self_tactic")),),
            )
        elif row.get("self_tactic"):
            conn.execute("UPDATE tactics SET is_self_tactic=1 WHERE id=?", (tactic_ids.get(row.get("self_tactic")),))

    for row in wiki_generals:
        conn.execute(
            """UPDATE generals SET quality=COALESCE(?,quality),combat_role=COALESCE(?,combat_role)
               WHERE name=?""",
            (row.get("quality"), row.get("combat_role"), row["name"]),
        )
    for row in wiki_tactics:
        conn.execute(
            "UPDATE tactics SET quality=COALESCE(?,quality),first_season=COALESCE(first_season,'s1') WHERE name=?",
            (row.get("quality"), row["name"]),
        )

    for row in generals:
        for bond in row["bonds"]:
            conn.execute(
                """INSERT INTO bonds(name,effect_raw,source_id) VALUES(?,?,?)
                   ON CONFLICT(name) DO UPDATE SET effect_raw=CASE WHEN bonds.verification_status='Steam已核'
                   THEN bonds.effect_raw ELSE excluded.effect_raw END, source_id=CASE WHEN bonds.verification_status='Steam已核'
                   THEN bonds.source_id ELSE excluded.source_id END""",
                (bond["name"], bond["effect"], src_id),
            )
            bond_id = conn.execute("SELECT id FROM bonds WHERE name=?", (bond["name"],)).fetchone()[0]
            for member in bond["members"]:
                member_row = conn.execute("SELECT id FROM generals WHERE name=?", (member,)).fetchone()
                if member_row:
                    conn.execute("INSERT OR IGNORE INTO bond_members(bond_id,general_id) VALUES(?,?)", (bond_id, member_row[0]))

    effect_ids = {}
    for effect in effects:
        conn.execute(
            """INSERT INTO effects(name,category,exact_effect,is_control,is_functional,source_id,updated_at)
               VALUES(?,?,?,?,?,?,?) ON CONFLICT(name) DO UPDATE SET category=excluded.category,
               exact_effect=excluded.exact_effect,is_control=excluded.is_control,
               is_functional=excluded.is_functional,source_id=excluded.source_id,updated_at=excluded.updated_at""",
            (effect["name"], effect["category"], effect["exact_effect"], int(effect["control"]),
             int(effect["functional"]), buff_src_id, NOW),
        )
        effect_ids[effect["name"]] = conn.execute("SELECT id FROM effects WHERE name=?", (effect["name"],)).fetchone()[0]
    for tactic in tactics:
        description = tactic.get("description") or ""
        for effect_name, effect_id in effect_ids.items():
            if effect_name in description and effect_name not in {"特殊增益状态", "常规负面状态", "控制状态", "属性降低状态"}:
                conn.execute(
                    "INSERT OR IGNORE INTO tactic_effects(tactic_id,effect_id,relation,evidence_text) VALUES(?,?,?,?)",
                    (tactic_ids[tactic["name"]], effect_id, "产生或依赖", description),
                )

    load_account(conn)
    seed_steam_data(conn)
    conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('schema_version','1')")
    conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('default_platform','Steam')")
    conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('default_season','s1')")
    conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('last_sync_at',?)", (NOW,))
    status = "partial" if errors else "complete"
    conn.execute(
        "UPDATE sync_runs SET finished_at=?,status=?,generals_count=?,tactics_count=?,effects_count=?,error_text=? WHERE id=?",
        (NOW, status, len(generals), len(tactics), len(effects), "\n".join(errors) or None, run_id),
    )
    conn.commit()
    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    counts = {
        "generals": conn.execute("SELECT count(*) FROM generals").fetchone()[0],
        "s1_generals": conn.execute("SELECT count(*) FROM v_s1_generals").fetchone()[0],
        "s1_gold_generals": conn.execute("SELECT count(*) FROM v_s1_gold_generals").fetchone()[0],
        "tactics": conn.execute("SELECT count(*) FROM tactics").fetchone()[0],
        "recommendable_tactics": conn.execute("SELECT count(*) FROM v_recommendable_tactics").fetchone()[0],
        "effects": conn.execute("SELECT count(*) FROM effects").fetchone()[0],
        "bonds": conn.execute("SELECT count(*) FROM bonds").fetchone()[0],
        "account_generals": conn.execute("SELECT count(*) FROM account_generals").fetchone()[0],
        "account_tactics": conn.execute("SELECT count(*) FROM account_tactics").fetchone()[0],
        "integrity": integrity,
    }
    conn.close()
    return counts, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--snapshot", type=Path, default=DATA_DIR / "snapshots" / "sgmdtx-latest.json")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    args.db.parent.mkdir(parents=True, exist_ok=True)
    try:
        counts, errors = write_database(args.db, args.snapshot, max(1, min(args.workers, 12)))
    except Exception as exc:
        print(f"sync failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(counts, ensure_ascii=False, indent=2))
    if errors:
        print(f"partial sync: {len(errors)} page(s) failed", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
