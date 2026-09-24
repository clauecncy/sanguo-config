"""Render manually verified image evidence as hash-addressed Markdown."""
import argparse
import hashlib
import json
from pathlib import Path

from project_data import ROOT, atomic_json, event_dir, read_json, user_dir


MARKER_PREFIX = "IMAGE_TEXT_TRANSCRIPTION_V1"
INVENTORY_TRANSCRIPTIONS = {
    "d46e9d571e40ea2f4eb3150dcbd5a6f06eaa1c6595bf79cecbdd7ce538c33621": {
        "name": "披坚执锐", "type": "指挥", "category": "辅助", "rate": "100%",
        "effect": "战斗开始，使我军随机单体（优先前排）获得披坚：行动前恢复自身兵力（治疗率80%，受目标智力和统率影响），受到兵刃伤害降低20%；使我军武力最高单体获得执锐：普通攻击后，有50%概率对敌军随机单体造成1次100%兵刃伤害。"
    },
    "ffa13f2c2b6dfca80a03206f583d29e4fa77e15316c56127f5b454c9be8c385e": {
        "name": "断敌粮道", "type": "指挥", "category": "谋略", "rate": "100%",
        "effect": "回合开始时，对敌军单体施加断粮，持续2回合。回合结束时，对持有断粮状态的敌军造成113.3%谋略伤害。"
    },
    "a6d19a657a0dce1f45962ef06bb31c8ddd6b4d738a4d577704ecfc56471ab6c3": {
        "name": "五雷轰顶", "type": "主动", "category": "谋略", "rate": "50%",
        "effect": "准备1回合，对敌军随机单体造成160%谋略伤害，施放5次；每次命中持有洪水状态的目标，该次伤害提高40%。"
    },
    "ecf4a39f8d59ef3a144ce02335d971900b0633f1a9cf525d2156fda05cde1e2f": {
        "name": "忘私相助", "type": "被动", "category": "治疗", "rate": "100%",
        "effect": "自身受到伤害前，有50%概率恢复两名友军兵力（治疗率50%，受智力和统率影响）。"
    },
    "06cb852557c17cf7e9c95ca80e49dcd29ffda8452be164f603b67fb59de64a2e": {
        "name": "计袭粮仓", "type": "追击", "category": "谋略", "rate": "45%",
        "effect": "普通攻击后，对攻击目标造成300%谋略伤害，并施加断粮，持续2回合；若目标持有断粮状态，则额外对其造成100%谋略伤害。"
    },
    "6b7441ee93cd1b4f3b2c13510f6759d1993f684db6dc5817215c65dfb2c5905d": {
        "name": "舍生取义", "type": "指挥", "category": "辅助", "rate": "100%",
        "effect": "战斗开始前2回合，我军全体连击率提升30%；我军武力最高单体获得清醒，自身缴械，持续2回合。"
    },
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def marker(digest):
    return f"<!-- {MARKER_PREFIX}:sha256:{digest} -->"


def anchor(digest):
    return f"image-{digest}"


def ref(path, digest):
    return f"{path}#{anchor(digest)}"


def verify_source(root, relative, expected):
    source = root / relative
    if not source.is_file():
        raise ValueError(f"Local image is unavailable for transcription: {relative}")
    actual = sha256(source)
    if actual != expected.lower():
        raise ValueError(f"Image hash mismatch: {relative}")
    return actual


def update_transcription_fields(row, target, fields):
    row["transcription_ref"] = ref(target, row["sha256"])
    row["transcription_status"] = "verified_text"
    row["transcription_marker"] = marker(row["sha256"])
    row["verified_fields"] = sorted(set(fields))
    row["trust_status"] = "可信"
    row["trust_reason"] = "按原图逐字段人工核定并保留内容SHA-256；可信范围仅限verified_fields，不推断未展示字段。"


def render_public(root, index):
    observations = read_json(root / "game/sources/tactic_level_observations.json")["observations"]
    by_id = {row["observation_id"]: row for row in observations}
    rows = [row for row in index if row.get("path", "").startswith("game/sources/evidence/")
            and row.get("availability") == "local_only"]
    lines = [
        "# 图片转译证据：公共技能观察",
        "",
        "本文件由已逐字段核定的战法等级观察生成。原图保留在各工作副本的本地证据目录中，不进入Git；每条以原图SHA-256作锚点，并逐观察保留等级、发动率、正文、红度及来源边界。",
        "可信只覆盖各条明确列出的`verified_fields`；不把技能单图扩大为武将四维、库存拥有状态或其他等级/红度结论。",
        "",
    ]
    for row in rows:
        digest = verify_source(root, row["path"], row["sha256"])
        if not row.get("observations"):
            raise ValueError("Public image has no linked observation: " + row["path"])
        lines.extend([f'<a id="{anchor(digest)}"></a>', "", f"## {Path(row['path']).name}", "", marker(digest),
                      f"- 原图：`{row['path']}`（仅本地保留）",
                      f"- SHA-256 / evidence_id：`{digest}` / `sha256:{digest}`",
                      f"- 角色：{row.get('role', '用户图片证据')}",
                      f"- 可信状态：`{row.get('trust_status', '可信')}`；核定日期：{row.get('verified_at', '未记录')}"])
        verified = set()
        for link in row["observations"]:
            observation = by_id.get(link["observation_id"])
            if not observation:
                raise ValueError(f"Missing observation {link['observation_id']} for {row['path']}")
            verified.update(link.get("verified_fields", []))
            lines.extend(["", f"### 等级观察 {observation['observation_id']}：{observation['name']}",
                          f"- 核定字段：`{', '.join(link.get('verified_fields', []))}`",
                          f"- 品质/类型/伤害类型：{observation.get('quality') or '未显示'} / {observation.get('tactic_type') or '未显示'} / {observation.get('damage_type') or '未显示'}",
                          f"- 等级/发动率：{observation.get('level') if observation.get('level') is not None else '未显示'} / {observation.get('activation_rate') or '未核'}",
                          f"- 红度核定：{observation.get('advancement_confirmed') if observation.get('advancement_confirmed') is not None else '未知'}",
                          f"- 图片转译正文：{observation.get('effect_raw') or '原图未提供完整正文'}",
                          f"- 观察可信状态/复核：`{observation.get('trust_status')}` / `{observation.get('review_state')}`",
                          f"- 核定原因：{observation.get('trust_reason') or '未记录'}",
                          f"- 观察上下文：{observation.get('context') or '未记录'}"])
        update_transcription_fields(row, "game/sources/图片转译证据.md", verified)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n", rows


def render_round_candidate(group):
    if "generals" in group:
        return "武将候选：" + "、".join(group["generals"]), ["general_names"]
    cards = group.get("tactics", [])
    rendered = []
    fields = {"tactic_names"}
    for card in cards:
        if isinstance(card, str):
            rendered.append(card)
            continue
        detail = []
        if card.get("level") is not None:
            detail.append(f"等级{card['level']}")
            fields.add("level")
        if card.get("type"):
            detail.append(card["type"])
            fields.add("tactic_type")
        if card.get("category"):
            detail.append(card["category"])
            fields.add("category")
        if card.get("activation_rate"):
            detail.append(f"发动率{card['activation_rate']}")
            fields.add("activation_rate")
        if card.get("card_summary"):
            detail.append(f"卡面摘要：{card['card_summary']}")
            fields.add("card_summary")
        if card.get("adapted_to"):
            detail.append("卡面适配提示：" + "、".join(card["adapted_to"]))
            fields.add("adapted_to")
        rendered.append(f"{card['name']}（" + "；".join(detail) + "）")
    return "战法候选：" + "；".join(rendered), sorted(fields)


def event_description(root, event_path, event, manifest_row, rounds, report, control, prep,
                      reroll, lineup, chain_text):
    path = manifest_row["path"]
    if path in rounds:
        return render_round_candidate(rounds[path])
    results = [r for r in report.get("results", []) if r.get("source") == path]
    if results:
        bits = []
        for row in results:
            assessment = row.get("assessment")
            text = (f"第{row['round']}轮，对手{row['opponent']}，第{row['team']}队：界面实见{row['final_result']}，"
                    f"己方剩余{row.get('own_remaining', '未显示')}，敌方剩余{row.get('enemy_remaining', '未显示')}"
                    f"（续战：{'是' if row.get('continuation') else '否'}）。")
            if assessment and assessment != row["final_result"]:
                text += f"复盘评估为{assessment}，这是分析字段，不属于截图直接可见结果。"
            bits.append(text)
        return " ".join(bits), ["round", "opponent", "team", "final_result", "own_remaining", "enemy_remaining", "continuation"]
    details = [r for r in report.get("details", []) if r.get("source") == path]
    if details:
        field_names = {
            "guanyu_native_count": "关羽自带战法次数", "guanyu_native_damage": "关羽自带战法伤害",
            "shuiyan_count": "水淹七军次数", "ganglie_damage": "刚烈伤害", "tuntian_heal": "屯田令治疗",
            "pangde_native_count": "庞德自带战法次数", "pangde_native_damage": "庞德自带战法伤害",
            "mu_niu_heal": "木牛流马治疗", "qizheng_damage": "奇正相生伤害", "qizheng_heal": "奇正相生治疗",
            "pangde_jixing_damage": "疾行侧击伤害", "shuiyan_damage": "水淹七军伤害",
            "qingfeng_heal": "清风驱疾治疗", "pozhen_damage": "破阵驰围伤害",
        }
        rendered = []
        fields = {"image", "team", "opponent"}
        for row in details:
            values = [f"{field_names.get(k, k)}{v}" for k, v in row.items()
                      if k not in ("image", "team", "opponent", "source", "note") and v is not None]
            fields.update(k for k in row if k not in ("image", "team", "opponent", "source", "note"))
            note = f" 备注（非截图事实）：{row['note']}" if row.get("note") else ""
            rendered.append(f"第{row['image']}张详情，{row['opponent']}，第{row['team']}队：" + "、".join(values) + note)
        return " ".join(rendered), sorted(fields)
    if path == lineup.get("source"):
        teams = []
        for team in lineup.get("teams", []):
            members = "；".join(f"{m['name']}（{'、'.join(m.get('tactics', []))}）" for m in team.get("members", []))
            teams.append(f"第{team['team']}队 {team['formation']}：{members}")
        return "阵容文字：" + "。".join(teams) + "。截图仍有锁定倒计时，因此本转写不记为已锁定。", ["team", "formation", "members", "tactics"]
    if path.startswith("证据/两场控制补证/"):
        team1 = control["team1"]["received"]
        team2 = control["team2"]["received"]
        def statuses(values):
            return "；".join(name + "：" + "、".join(f"{key}{count}次" for key, count in row.items())
                            for name, row in values.items())
        description = ("六张连续截图合并统计（不把累计字段虚分到单张）：一队受控计数：" + statuses(team1) +
                       f"。关羽八方回合：{control['team1'].get('guanyu_babafang_rounds', [])}。二队受控计数：" + statuses(team2) +
                       f"。画面计数：周瑜自带触发{control['team2'].get('visible_native_zhouyu_count')}次，黄盖苦肉{control['team2'].get('visible_huanggai_kurou_count')}次，"
                       f"黄盖指点{control['team2'].get('visible_huanggai_zhidian_count')}次，敌方忘私相助{control['team2'].get('visible_enemy_wangsi_count')}次；"
                       f"小乔天香显示回合{control['team2'].get('visible_xiaoqiao_tianxiang_rounds', [])}。")
        return description, ["control_counts", "visible_trigger_counts", "visible_rounds"]
    if path.startswith("证据/曹操队续战准备属性/"):
        rows = []
        for general in prep["generals"]:
            stats = [f"{key}={general[key]}" for key in ("force", "intelligence", "command", "initiative", "troops", "max_troops",
                    "damage_dealt_pct", "damage_received_pct", "daoge_pct", "gongxin_pct") if key in general]
            rows.append(f"{general['name']}（{general['troop']}）：" + "，".join(stats))
        logs = "；".join(f"{r['skill']}对{r['target']}：减伤增量{r['reduction_increment']}，结果受伤修正{r['result_damage_received_pct']}%" for r in prep.get("log", []))
        return (f"四张准备属性截图合并转写（不将合计数据虚分到单张）；阶段：{prep.get('phase')}。" + "；".join(rows) +
                "。施加记录：" + logs + "。仅为战斗准备面板及日志，不是武将基础四维。"), ["combat_attributes", "troops", "visible_buff_log"]
    if path == "证据/战法重随结果及三队配置.png":
        members = []
        for team in reroll.get("teams", []):
            roster = "；".join(f"{m['name']}（{'、'.join(m.get('tactics', []))}）" for m in team.get("members", []))
            members.append(f"第{team['team']}队 {team['formation']}：{roster}")
        return ("重随结果：舍生取义→五雷轰顶；出其不意→韬光养晦。配置：" + "。".join(members) +
                "。图片仅证明截图所示配置，不代表已锁定；当前有效建议与更正见重随后优化.md。"), ["reroll_result", "team", "formation", "members", "tactics"]
    if path == "证据/贾诸法配置参考.png":
        text = ("配置参考截图文字：贾诩携战八方、乘间投隙；诸葛亮携狂风大作、谈笑诛心；法正携来好息师、断敌粮道。"
                "这只是配置参考，不是战法正文、个人拥有状态、下一轮选卡或本期已选阵容。")
        if "诸葛亮狂风大作/谈笑诛心" not in chain_text:
            raise ValueError("Reference transcript is missing from the verified chain note")
        return text, ["general_names", "equipped_tactics"]
    if path == "证据/第7轮锦囊规则.png":
        rules = event["rules"]["pouch_details"]
        text = "锦囊规则转写：" + "；".join(f"{name}：{value}" for name, value in rules.items() if name != "source") + "。"
        return text, ["pouch_names", "pouch_rules"]
    raise ValueError("No transcription mapping for event image: " + path)


def render_event(root, event_path, event, manifest, event_json):
    rounds = {}
    for path in sorted(event_path.glob("第[1-6]轮选*.json")):
        data = read_json(path)
        for group in data.get("groups", []):
            rounds[group["source"]] = group
    report = read_json(event_path / "上半场战报.json")
    control = read_json(event_path / "两场控制补证.json")
    prep = read_json(event_path / "曹操队续战准备属性.json")
    reroll = read_json(event_path / "重随后阵容.json")
    lineup = read_json(event_path / "上半场后最新阵容.json")
    chain_text = (event_path / "阵容链条纠正.md").read_text(encoding="utf-8")
    lines = [
        "# 截图转译证据：S2 演武",
        "",
        f"账号：`{event['user_id']}`；期次：`{event['event_id']}`。本目录的原始截图仅保留本地；下列逐图转译以SHA-256和`evidence_id`连接。转写依据为人工核过的结构化资料和现有复盘，不使用自动OCR判真。",
        "`可信`只认证条目列出的可见字段。选卡短摘要不等于完整战法正文；右上选取比例不解释为发动率、胜率或收益。分析判断、阵容推断、未显示的红度和锁定状态均明确排除在截图事实之外；成组证据不会虚构字段与单张图片的对应关系。",
        "",
    ]
    for row in manifest["files"]:
        digest = verify_source(root, f"{event_path.relative_to(root).as_posix()}/{row['path']}", row["sha256"])
        description, fields = event_description(root, event_path, event_json, row, rounds, report, control, prep,
                                                reroll, lineup, chain_text)
        target = f"{event_path.relative_to(root).as_posix()}/截图转译证据.md"
        update_transcription_fields(row, target, fields)
        lines.extend([f'<a id="{anchor(digest)}"></a>', "", f"## {row['path']}", "", marker(digest),
                      f"- 原图SHA-256 / evidence_id：`{digest}` / `sha256:{digest}`（仅本地保留）",
                      f"- 可信状态：`可信`；可信字段：`{', '.join(fields)}`",
                      f"- 转译依据：已有逐字段核对记录；{row.get('role', '本期演武图片证据')}。",
                      f"- 文字转译：{description}", ""])
    return "\n".join(lines).rstrip() + "\n"


def render_inventory(root, inventory_dir, manifest):
    lines = [
        "# 库存战法图片文字转译",
        "",
        "原始详情截图保留在本地；逐图转写限定在图片显示的战法字段。截图没有清晰确认的红度继续保持未知，正文中显示的数值不反向推断红度或额外库存状态。",
        "",
    ]
    indexed = {row["file"].removesuffix(".png"): row for row in manifest["files"]}
    if set(indexed) != set(INVENTORY_TRANSCRIPTIONS):
        raise ValueError("Inventory screenshots and transcription records differ")
    for digest, data in INVENTORY_TRANSCRIPTIONS.items():
        image = inventory_dir / "evidence/current" / f"{digest}.png"
        actual = verify_source(root, image.relative_to(root).as_posix(), digest)
        row = indexed[digest]
        fields = ["name", "quality", "level", "tactic_type", "damage_type", "activation_rate", "effect_raw"]
        target = "user/bixianjue/evidence/current/截图文字转译.md"
        update_transcription_fields(row, target, fields)
        row.update(availability="local_only", evidence_id=f"sha256:{digest}", sha256=actual,
                   bytes=image.stat().st_size)
        lines.extend([f'<a id="{anchor(digest)}"></a>', "", f"## {data['name']}", "", marker(digest),
                      f"- 原图SHA-256 / evidence_id：`{digest}` / `sha256:{digest}`（仅本地保留）",
                      "- 可信状态：`可信`",
                      f"- 可信字段：`{', '.join(fields)}`；战法等级10，品质金色，类型{data['type']}，类别{data['category']}，发动率{data['rate']}。",
                      f"- 图片转译正文：{data['effect']}",
                      "- 边界：红度未由本图明确确认，保留未知；可信不扩展到其他等级、平台或账号状态。", ""])
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--user", required=True)
    parser.add_argument("--event", required=True)
    args = parser.parse_args()
    user_dir(args.user, ROOT)
    event_path = event_dir(args.user, args.event, ROOT)
    if args.user != "bixianjue" or args.event != "s2-2026-09-23":
        raise SystemExit("This checked transcription batch is scoped to bixianjue / s2-2026-09-23.")

    index_path = ROOT / "game/sources/evidence-index.json"
    index = read_json(index_path)
    public_text, public_rows = render_public(ROOT, index)

    event_manifest_path = event_path / "证据清单.json"
    event_manifest = read_json(event_manifest_path)
    event_json = read_json(event_path / "event.json")
    event_text = render_event(ROOT, event_path, event_json, event_manifest, event_json)

    inventory_dir = ROOT / "user" / args.user
    inventory_manifest_path = inventory_dir / "evidence/current/manifest.json"
    inventory_manifest = read_json(inventory_manifest_path)
    inventory_text = render_inventory(ROOT, inventory_dir, inventory_manifest)

    public_local = [r for r in index if r.get("availability") == "local_only"]
    event_local = [r for r in event_manifest["files"] if r.get("availability") == "local_only"]
    event_public_rows = [r for r in public_local if r["path"].startswith(f"user/{args.user}/演武/{args.event}/")]
    event_rows_by_hash = {r["sha256"]: r for r in event_manifest["files"]}
    for row in event_public_rows:
        event_row = event_rows_by_hash.get(row["sha256"])
        if not event_row:
            raise ValueError("Candidate screenshot is not in the event manifest: " + row["path"])
        row["transcription_ref"] = event_row["transcription_ref"]
        row["transcription_status"] = event_row["transcription_status"]
        row["transcription_marker"] = event_row["transcription_marker"]
        row["verified_fields"] = event_row["verified_fields"]
        row["trust_reason"] = event_row["trust_reason"]
    if len(event_public_rows) != 6:
        raise ValueError(f"Expected 6 indexed event-card screenshots, got {len(event_public_rows)}")

    # Point the mechanism fact to the text source while retaining the original evidence identity.
    fact_path = ROOT / "game/facts.json"
    facts = read_json(fact_path)
    for fact in facts["facts"]:
        if fact["id"] == "taoguang-native-active":
            source_row = next(r for r in public_rows if "韬光养晦10级-完整复核" in r["path"])
            fact.update(source="game/sources/图片转译证据.md", source_anchor=anchor(source_row["sha256"]),
                        source_type="游戏内图片转译Markdown", evidence_id=source_row["evidence_id"],
                        source_image_sha256=source_row["sha256"])
            break
    else:
        raise ValueError("Missing taoguang-native-active fact")

    # Expose the new event evidence ledger alongside the other per-event projections.
    if "截图转译证据.md" not in event_json["files"]:
        event_json["files"].append("截图转译证据.md")
    event_json["image_transcription_file"] = "截图转译证据.md"

    (ROOT / "game/sources/图片转译证据.md").write_text(public_text, encoding="utf-8", newline="\n")
    (event_path / "截图转译证据.md").write_text(event_text, encoding="utf-8", newline="\n")
    (inventory_dir / "evidence/current/截图文字转译.md").write_text(inventory_text, encoding="utf-8", newline="\n")
    atomic_json(index_path, index)
    atomic_json(event_manifest_path, event_manifest)
    atomic_json(inventory_manifest_path, inventory_manifest)
    atomic_json(fact_path, facts)
    atomic_json(event_path / "event.json", event_json)
    print(json.dumps({"public_images": len(public_rows), "event_images": len(event_manifest["files"]),
                      "inventory_images": len(inventory_manifest["files"]),
                      "public_candidate_images": len(event_public_rows)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
