import hashlib
import json
import os
import shutil
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "game" / "game.sqlite3"
STAGED = ROOT / "game" / "game.staged.sqlite3"
EVIDENCE = ROOT / "game" / "sources" / "screenshots" / "2026-09-12"
INDEX = ROOT / "game" / "sources" / "evidence-index.json"
OBS = ROOT / "game" / "sources" / "tactic_level_observations.json"
BASELINE = ROOT / "game" / "sources" / "public-baseline.sql"
TEMP = Path(r"C:\Users\BIXIAN~1\AppData\Local\Temp")
NOW = "2026-09-12T00:00:00+08:00"

RAW = '''临机制胜|指挥|谋略|100%|战斗中，敌我全体被施加异常状态时，自身有70%概率触发制胜：立刻对敌军随机两人造成60%谋略伤害。每回合制胜最多触发4次。累积触发4次制胜后，恢复我军全体兵力（治疗率40%，受智力影响）|7af77f06-0970-4022-a03f-fcc962c998fb
苦肉计|主动|防御|50%|自身受到伤害降低30%（受统率影响），持续2回合。令智力最高友军对自身造成60%兵刃伤害，对敌军随机两人造成220%谋略伤害，并施加火攻，持续2回合|78e79dd2-0230-4d55-aca5-3f1a81e68774
百里疑城|指挥|防御|100%|战斗开始前4回合，我军全体受到伤害前有25%概率（受统率影响）获得1层抵御，第4回合开始时，自身统率提升40点，并对敌军全体施加洪水状态，持续2回合|f6f9a958-0311-431d-8b7b-1876d04b584c
天香|主动|治疗|40%|对敌军随机两人施加虚弱，持续1回合。恢复我军随机两人兵力（治疗率为250%，受智力影响）|bd384053-48cf-4171-b9ac-ce06f0abcdfc
火烧连营|主动|谋略|60%|对敌军随机单体施加火攻，持续2回合，然后对已持有火攻状态的敌军目标施加1层焚烧状态，持续2回合，同时造成220%谋略伤害，并有40%概率（受智力影响）额外施加1层焚烧状态|aaa8243d-3ccb-44cd-91ce-0df462183322
虎踞江东|指挥|辅助|100%|自身每学习一个主动战法，我军全体提升7%主动战法发动率，受到兵刃伤害降低5%。自身每学习一个非主动战法，我军全体提升28%连击率，受到谋略伤害降低5%（所有效果均受自身最高属性影响）|a3f22f62-c216-49de-a461-fa4c322cb16e
荐计阻敌|主动|辅助|60%|使我军统率最高单体获得1层抵御，武力、智力、先攻提升40点（受最高属性影响），使敌军统率最低单体武力、智力、先攻降低40点（受最高属性影响），持续2回合|ba25294b-fa54-4f0e-abfc-8c8717b4313f
智令从计|指挥|辅助|100%|每个回合开始时，使我军武力最高单体获得1回合从计：受到谋略伤害降低15%（受智力影响），发动追击战法后对敌军随机单体造成140%谋略伤害（受目标武力影响）|d35df04c-a039-4628-b2c7-8a0440941674
骁勇无前|主动|兵刃|40%|自身造成兵刃伤害和谋略伤害提升20%，持续2回合，然后对敌军随机两人造成200%兵刃伤害，若目标携带控制状态，则改为造成400%兵刃伤害|71f69436-4622-4983-9383-039ac3674e71
七进七出|被动|兵刃|100%|提升自身35%规避率，成功规避后触发龙胆：立刻对敌军随机两人造成90%兵刃伤害，当前回合下一次龙胆的伤害系数降低10%。龙胆每个回合可触发7次|73892924-9174-4d59-86b0-3c2196332391
巧言眩惑|指挥|谋略|100%|战斗开始时，使敌军随机两人造成兵刃伤害降低30%（受智力影响），持续2回合。第3回合开始时降低这两名目标30点智力（受智力影响），持续3回合，并对其造成500%谋略伤害（受智力差影响）|9978746f-8634-4c11-9bd9-2335503f5bab
红妆缭乱|追击|兵刃|70%|普通攻击后，对攻击目标施加畏惧，持续2回合，然后造成220%兵刃伤害，有80%概率额外造成220%兵刃伤害|4d7bf681-bfa5-44c1-b94b-cdd6686c27d5
勇冠贲育|主动|谋略|60%|使敌军随机单体产生逃兵（受智力影响），之后对其造成360%谋略伤害，若目标为前排则伤害系数提高80%|3bf28ea3-540d-4da4-b50a-0003d1c2c380
流风回雪|指挥|辅助|100%|每个回合开始时，恢复自身兵力（治疗率为140%，受智力影响），并使随机一名队友（优先选择后排）获得1回合洛神：恢复自身兵力（治疗率为140%，受智力影响），造成伤害提升25%，获得洛神后的首次非普通攻击伤害必定触发会心和奇谋|19f580f9-d62c-48e1-8f06-43681595cdb5
国色|指挥|辅助|100%|每个回合开始时，敌军随机两人受到伤害提升20%，持续1回合，恢复我军随机两人兵力（治疗率180%，受智力影响）|9120da46-ad5a-4d4a-a118-8591c52a830a
闭月|被动|防御|100%|自身受到来自异性的伤害降低30%（受最高属性影响）。每个回合结束时，令友军武力最高单体兵刃伤害提升15%，并对本回合内伤害过貂蝉的目标造成1次60%无视统率的兵刃伤害（无法触发会心）|c5b85923-6650-46d0-b0e7-d22f64df519d
诡道玄机|指挥|谋略|100%|每个回合开始时有90%概率对敌军随机单体和一名队友施加混乱，持续2回合，若敌军目标已持有混乱状态，则额外造成300%谋略伤害，若友军目标已持有混乱状态，则额外恢复其和自身兵力（治疗率110%，受智力影响）。我军全体对自身和友军造成的伤害降低60%。|6b8fc6cf-efb9-4391-8403-53b11e5a1b23
裸衣血战|被动|兵刃|100%|战斗开始时，自身先攻和武力提升20点，连击率提升100%，统率降低15点。我军全体每累计进行4次普通攻击时，提升全体2%破甲（受武力影响），可叠加，持续到战斗结束|b0fc3ff0-22a6-4f47-953e-b6184e9ea17d
古之恶来|被动|兵刃|100%|自身反击率提升60%，自身受到伤害后提升自身20%反击伤害和20点统率，持续2回合，可叠加5次|d7598378-3406-4acc-ae9a-bfe812d0029e
算无遗策|指挥|谋略|100%|战斗开始时，提升自身及智力最高友军6%主动战法发动率。自身成功发动主动战法后，有70%概率额外再发动一次（准备战法不需要再次准备）|4f7215da-c970-4d1c-b2ed-73a29b3e6cff
持军毅重|被动|防御|100%|自身统率提升30点，每回合首次受到伤害后使敌军随机两人受到伤害提升10%（受统率影响），并有60%概率使攻击者缴械，持续2回合|690df37d-34f7-49dd-be29-0d33b19513d3
大破街亭|主动|兵刃|60%|提升自身5%破甲，持续到战斗结束，可叠加4次。然后对敌军随机两人造成220%兵刃伤害，并有65%概率施加缴械，持续1回合，若目标已持有缴械状态，则该次伤害提升30%|92696f93-fe87-4828-b62f-581df96916e0
长驱直入|主动|兵刃|60%|对敌军随机单体造成350%兵刃伤害，并施加技穷，持续1回合，若目标已持有技穷状态或是敌军兵力最低单体，则该次伤害值提升30%|f31fbc67-d4a4-4030-b75a-6ba99ed79ad9
神速奔袭|被动|兵刃|100%|每个回合行动时自身武力值提升，提升值为先攻值的40%，持续1回合。自身先攻每高过一名敌军，则获得1层神速效果：造成伤害和会心几率提升5%（受先攻影响），持续1回合，并对其造成30%兵刃伤害|9e8d9262-b8bc-40be-96d9-f040cf18d298
固镇襄樊|指挥|防御|100%|奇数回合自身受到来自后排的伤害降低30%（受统率影响），来自前排的伤害降低15%（受统率影响）。偶数回合开始时有75%概率对敌军随机两人施加技穷，持续1回合，每个目标的概率独立判定|7066c084-3d92-40f9-84ef-1e22d1ce807a
威震华夏|主动|兵刃|50%|提升自身8%主动战法发动率，每有1个带有畏惧状态的敌军额外提升3%，持续2回合。然后对敌军全体造成180%兵刃伤害，若目标持有控制状态，则使目标产生逃兵（受武力影响）|a53b62fa-0ce4-4160-909b-204de9c1ac86
万人之敌|主动|兵刃|55%|对敌军全体造成140%兵刃伤害，并施加畏惧，持续2回合。若目标已持有畏惧状态，则有30%概率造成震慑，持续1回合|1b91a4e8-8ff3-493e-bdd8-2536d18ed8ec
折节学问|主动|文武|65%|对敌军随机单体造成220%谋略和兵刃伤害。若目标武力大于智力，则造成缴械，反之造成技穷，持续1回合|95cad603-0299-4524-93d0-0cfca181f1f7
睹事知机|主动|谋略|100%|对敌军全体施加睹事：下一次受到非普通攻击伤害后为攻击者恢复兵力（治疗率80%，受智力影响），并额外受到来自法正的120%谋略伤害|0518fcd2-2c48-426a-98d2-e9349b9f3a92
龙吟四海|被动|兵刃|100%|自身造成兵刃伤害后有75%概率触发龙吟：对目标施加畏惧，持续2回合，若目标已处于畏惧状态，则改对其造成100%兵刃伤害。每回合可触发4次龙吟|cfbe627d-8af7-4f88-b83a-6ba4de3a5482
忠烈勇武|被动|防御|100%|每个回合行动时恢复自身兵力（治疗率200%，受智力和统率影响），有45%概率对敌军随机两人施加嘲讽和畏惧状态，持续2回合|de14ac02-a0f7-49f8-abc8-e1a32bc7cd9f
制霸江东|主动|兵刃|65%|对敌军随机两人造成250%兵刃伤害，并恢复自身和己方随机单体兵力（治疗率65%，受武力影响）|93af23ef-5e6c-43d0-9ac8-a1015dd8670f
划湘分荆|主动|防御|45%|对敌我全体随机4个目标施加缴械，持续1回合。若选中我方目标，则使目标受到伤害降低20%（受智力影响），持续1回合；若选中敌方目标，则使目标受到伤害提升20%（受智力影响），持续1回合|b07676bd-af42-4a8b-87c7-ab2a328efbda
锦帆渠魁|被动|兵刃|100%|普通攻击伤害提升150%，普通攻击前提升自身12点武力，持续2回合，可叠加4次|e56b4041-f8dd-4550-9d1e-ec431148b6ab
兴王定霸|指挥|辅助|100%|我军全体造成兵刃伤害后有60%概率恢复兵力（治疗率40%，受智力和统率影响），造成谋略伤害后有60%概率使受到伤害降低14%，持续2回合，可叠加2次|8ecb0856-60ca-4963-981e-37b15abcf580
白衣渡江|主动|谋略|70%|对敌军随机两人造成180%谋略伤害，并施加断粮，持续2回合，若目标已处于断粮状态则额外对目标造成80%谋略伤害|919faa7c-3118-4b5a-93ed-c690d9a8b2b9
悲愤诗|主动|治疗|65%|恢复我军全体兵力（治疗率120%，受智力影响），并施加1层抵御。若目标为前排，则额外恢复兵力（治疗率50%，受智力影响）|052bf244-bc6d-4c11-b6e3-5cda23bcd33c
黄天当立|主动|谋略|60%|准备1回合，对敌军全体造成300%谋略伤害，目标每多一种负面状态，谋略伤害系数提升30%，可提升3次，并使自身获得黄天：发动准备战法时，有50%概率跳过1回合准备，持续4回合|58b155b4-ab5b-4ecf-9ff1-143b7db81674
膂力过人|追击|兵刃|100%|普通攻击后，对当前攻击目标造成150%兵刃伤害，若目标武力低于自身额外造成70%兵刃伤害|48f81893-8eb2-42cc-ad57-b61cf68ecd07
交锋震威|追击|兵刃|55%|普通攻击后，获得必中状态，持续2回合，然后对敌军兵力最低单体造成280%兵刃伤害|56c21d8b-f6a8-4c98-823e-6b5c3292714c
麻沸散|指挥|辅助|100%|回合结束时，使友军兵力最低单体受到伤害降低16%（受智力影响），对其施加清醒，持续1回合。并恢复其兵力（治疗率240%，受智力影响）|33e963a1-a6bb-40da-b625-6d10c1e7c465
陷阵蹈难|被动|兵刃|100%|战斗第3、5回合自身行动时，降低敌军全体30点统率和智力（受武力影响），持续2回合，随后造成340%兵刃伤害|6eac14db-758f-4a14-809a-91f69d447a6f
顾盼生姿|被动|辅助|100%|战斗开始时，我军全体获得顾盼：受到的伤害、追击战法伤害、主动战法伤害降低16%。自身受到伤害后使我军全体顾盼效果降低2%，持续到回合结束，每回合最多降低8次。第4回合起，每回合行动时，恢复我军随机两人兵力（治疗率140%，受智力影响）|00e0a9c6-eeed-45e1-a10b-8078ab8a5e2f
妖武|主动|兵刃|65%|自身倒戈和规避率提升25%，持续2回合，然后对敌军随机两人造成220%兵刃伤害，并施加妖术，持续2回合|dbc56868-74e2-40a4-9424-ec591bfc06f6
妖风大作|主动|谋略|60%|对敌军随机两人造成280%谋略伤害，并施加妖术和风暴状态，持续2回合，若目标已持有妖术状态，则该次伤害提升35%|a7616c59-49ff-44d3-b054-adb72f2b52c6'''

rows = [line.split("|", 5) for line in RAW.splitlines()]
assert len(rows) == 45 and all(len(row) == 6 for row in rows)

def quote(v):
    if v is None: return "NULL"
    return "'" + str(v).replace("'", "''") + "'"

def main():
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    copied = []
    for name, *_rest, token in rows:
        src = TEMP / f"codex-clipboard-{token}.png"
        dst = EVIDENCE / f"{name}-10级.png"
        if not src.exists(): raise FileNotFoundError(src)
        shutil.copy2(src, dst)
        copied.append((name, dst))

    if STAGED.exists(): STAGED.unlink()
    shutil.copy2(DB, STAGED)
    c = sqlite3.connect(STAGED)
    try:
        c.execute("PRAGMA foreign_keys = ON")
        c.execute("BEGIN IMMEDIATE")
        existing = {r[0] for r in c.execute("select name from tactics")}
        missing = [row[0] for row in rows if row[0] not in existing]
        # 法正的自带战法此前不在公共表中；由这张 Steam 满级截图创建基础实体。
        if set(missing) - {"巧言眩惑"}:
            raise ValueError(f"public tactics missing: {missing}")
        if "巧言眩惑" in missing:
            entity_id = "tactic:" + hashlib.sha256("巧言眩惑".encode("utf-8")).hexdigest()[:20]
            c.execute("insert into tactics(name, quality, is_self_tactic, first_season, verification_status, updated_at, description_level, platform, entity_id) values (?,?,?,?,?,?,?,?,?)", ("巧言眩惑", "金色", 1, "S2", "待核", NOW, 10, "Steam", entity_id))
        for name, typ, dmg, rate, desc, token in rows:
            rel = f"game/sources/screenshots/2026-09-12/{name}-10级.png"
            source_name = f"Steam截图-{name}-10级-20260912"
            c.execute("delete from sources where name=?", (source_name,))
            source_id = c.execute("insert into sources(name,url,source_type,platform,season,trust_rank,fetched_at,notes) values (?,?,?,?,?,?,?,?)", (source_name, rel, "游戏内截图", "Steam", "S2", 100, NOW, "用户提供；满级预览/10级截图；公共战法证据")).lastrowid
            c.execute("update tactics set tactic_type=?, damage_type=?, activation_rate=?, description_raw=?, description_level=10, verification_status=?, source_id=?, updated_at=?, platform=? where name=?", (typ, dmg, rate, desc, "Steam截图已核", source_id, NOW, "Steam", name))
        c.commit()
    finally:
        c.close()

    index = json.loads(INDEX.read_text(encoding="utf-8"))
    items = index if isinstance(index, list) else index.get("items", [])
    existing_paths = {item.get("path") for item in items}
    for name, path in copied:
        rel = path.relative_to(ROOT).as_posix()
        if rel not in existing_paths:
            items.append({"path": rel, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "source_type": "游戏内截图", "platform": "Steam", "season": "S2", "notes": f"{name} 10级满级预览，用户提供"})
    if isinstance(index, list): index = items
    else: index["items"] = items
    INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    obs = json.loads(OBS.read_text(encoding="utf-8"))
    old = obs if isinstance(obs, list) else obs.get("observations", [])
    names = {r[0] for r in rows}
    old = [x for x in old if x.get("tactic_name") not in names]
    for name, typ, dmg, rate, desc, token in rows:
        old.append({"tactic_name": name, "level": 10, "effect_json": {"tactic_type": typ, "damage_type": dmg, "activation_rate": rate, "description_raw": desc}, "source": "Steam游戏内截图", "observed_at": "2026-09-12", "screenshot_path": f"game/sources/screenshots/2026-09-12/{name}-10级.png"})
    if isinstance(obs, list): obs = old
    else: obs["observations"] = old
    OBS.write_text(json.dumps(obs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    c = sqlite3.connect(STAGED)
    try:
        dump = "\n".join(c.iterdump()) + "\n"
    finally:
        c.close()
    BASELINE.write_text(dump, encoding="utf-8")
    os.replace(STAGED, DB)
    print(json.dumps({"updated": len(rows), "evidence": len(copied)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
