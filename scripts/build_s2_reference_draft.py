import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "references" / ".ocr-python"))

import cv2  # noqa: E402
import numpy as np  # noqa: E402
OCR_DIR = ROOT / "references" / "S2阵容大全" / "assets" / "rapidocr-team-cells"
OUTPUT = ROOT / "references" / "S2阵容大全" / "阵容校正稿.md"
SKIP = {"r01-c01", "r01-c02", "r02-c01", "r02-c02"}

TIERS = [
    "T1.5", "T1", "T0.5", "T1",
    "T1", "T0.5", "T1", "T1.5",
    "T0.5", "T1", "T1.5", "T0.5", "T0.5", "T2",
    "T0", "T1", "T1", "T1", "T1", "T1.5",
    "T1", "T1", "T0.5", "T1", "T1.5", "T1.5",
    "T1", "T1.5", "T1.5", "T1.5", "T0", "T1",
    "T1.5", "T1.5", "T1", "T1.5", "T1", "T1",
    "T1", "T1", "T0", "T0.5", "T0.5", "T1",
    "T1", "T0.5", "T1", "T1", "T1", "T1",
]

TITLES = [
    "徐貂甘方圆阵", "英董虎卫-锥形阵", "英角吕布-箕形阵", "英角胖胖-箕形阵",
    "貂蔡梁-箕形阵", "貂田梁-箕形阵", "赵黄法-锥形阵", "曹甄庞-箕形阵",
    "追击辽-一字阵", "曹褚渊-方圆阵", "曹荀程-箕形阵", "英董吕-箕形阵",
    "英三孙-箕形阵", "英华雄-箕形阵", "徐黄鱼-雁形阵", "双减关羽-箕形阵",
    "黄龙骑-锥形阵", "大黄诸-雁形阵", "双曹陆-箕形阵", "田袁董-锥形阵",
    "甄小香-方圆阵", "徐甄香-方圆阵", "白门骑-箕形阵", "甄虎卫-锥形阵",
    "桃园-箕形阵", "贾夫妻-箕形阵", "徐甲鱼-箕形阵", "貂田辽-锥形阵",
    "一字辽-一字阵", "曹甄辽-一字阵", "神火弓-箕形阵", "徐荀陆-箕形阵",
    "孙鲁关-箕形阵", "曹褚郃-箕形阵", "孙鲁陆-箕形阵", "徐鲁陆-箕形阵",
    "孙小陆-箕形阵", "肉都督-一字阵", "荀夫妻-锥形阵", "云夫妻-鱼鳞阵",
    "草原马-箕形阵", "徐袁马-箕形阵", "黄马马-箕形阵", "大袁马-箕形阵",
    "徐孙陆-箕形阵", "双皇陆-箕形阵", "桃元马-箕形阵", "刘法马-箕形阵",
    "赵黄马-鱼鳞阵", "五虎马-鱼鳞阵",
]

HEROES = [
    ["徐盛", "貂蝉", "甘宁"], ["曹操", "典韦", "董卓"], ["张角", "陈宫", "吕布"], ["张角", "董卓", "庞德"],
    ["貂蝉", "蔡文姬", "张梁"], ["貂蝉", "田丰", "张梁"], ["赵云", "黄月英", "法正"], ["曹操", "甄洛", "庞德"],
    ["夏侯惇", "貂蝉", "甄洛"], ["曹操", "许褚", "夏侯渊"], ["曹操", "荀彧", "程昱"], ["董卓", "陈宫", "吕布"],
    ["孙坚", "孙权", "孙尚香"], ["甄洛", "田丰", "邢道荣"], ["周瑜", "徐盛", "黄盖"], ["夏侯惇", "郭嘉", "关羽"],
    ["刘备", "赵云", "貂蝉"], ["诸葛亮", "大乔", "黄盖"], ["曹仁", "曹操", "陆逊"], ["袁绍", "董卓", "田丰"],
    ["甄洛", "小乔", "孙尚香"], ["徐盛", "甄洛", "孙尚香"], ["曹操", "陈宫", "吕布"], ["曹操", "典韦", "甄洛"],
    ["刘备", "关羽", "张飞"], ["贾诩", "诸葛亮", "黄月英"], ["徐盛", "贾诩", "周瑜"], ["貂蝉", "张辽", "田丰"],
    ["张辽", "貂蝉", "甄洛"], ["曹操", "张辽", "甄洛"], ["曹操", "荀彧", "陆逊"], ["徐盛", "荀彧", "陆逊"],
    ["鲁肃", "孙权", "关羽"], ["曹操", "许褚", "张郃"], ["孙权", "鲁肃", "陆逊"], ["徐盛", "鲁肃", "陆逊"],
    ["孙权", "小乔", "陆逊"], ["鲁肃", "周瑜", "陆逊"], ["荀彧", "诸葛亮", "黄月英"], ["赵云", "诸葛亮", "黄月英"],
    ["曹操", "袁绍", "马超"], ["徐盛", "袁绍", "马超"], ["黄月英", "马超", "马云禄"], ["大乔", "袁绍", "马超"],
    ["徐盛", "孙权", "陆逊"], ["曹操", "孙权", "陆逊"], ["刘备", "马超", "张飞"], ["刘备", "法正", "马超"],
    ["赵云", "马超", "黄月英"], ["赵云", "马超", "张飞"],
]


FIELD_OVERRIDES = {
    (2, 2): {"specs": "屹然 / 不动"},
    (2, 3): {"troop": "重盾", "specs": "屹然 / 不动"},
    (4, 3): {"troop": "轻骑", "specs": "乘胜 / 追击"},
    (6, 1): {"troop": "重骑", "specs": "铁马 / 金戈"},
    (8, 3): {"troop": "轻骑", "specs": "乘胜 / 追击"},
    (15, 2): {"position": "前排"},
    (15, 3): {"position": "前排"},
    (18, 1): {"troop": "弩兵"},
    (19, 3): {"troop": "弩兵", "specs": "釜底 / 抽薪"},
    (20, 3): {"troop": "剑盾", "specs": "铁壁 / 如山", "adds": "二速"},
    (21, 3): {"troop": "弩兵"},
    (22, 3): {"troop": "弩兵"},
    (27, 1): {"adds": "全统率"},
    (27, 3): {"troop": "弩兵"},
    (31, 3): {"troop": "弩兵", "specs": "釜底 / 抽薪"},
    (32, 3): {"troop": "弩兵", "specs": "釜底 / 抽薪"},
    (36, 3): {"troop": "弩兵"},
    (37, 3): {"troop": "弩兵", "specs": "釜底 / 抽薪"},
    (38, 2): {"troop": "弩兵"},
    (38, 3): {"troop": "弩兵", "specs": "釜底 / 抽薪"},
    (40, 2): {"troop": "弩兵"},
    (44, 3): {"troop": "轻骑", "specs": "纵马 / 持矛"},
    (45, 3): {"troop": "弩兵"},
}

def center(box, axis):
    return sum(float(point[axis]) for point in box) / len(box)


def normalize(text):
    replacements = {
        "TO.": "T0.", "TO": "T0", "方园阵": "方圆阵", "箕型阵": "箕形阵",
        "曹褚邻": "曹褚郃", "涂盛": "徐盛", "吃然": "屹然", "百战不始": "百战不殆",
        "签底": "釜底", "擦尚香": "孙尚香", "沐尚香": "孙尚香", "用羽": "关羽",
        "鸳兵": "弩兵", "金底": "釜底", "灰斗": "疾斗", "鬼道": "鬼谋",
        "谈笑心": "谈笑诛心", "青發": "青囊", "青襄": "青囊", "生取义": "舍生取义",
        "运筹惟崛": "运筹帷幄", "运筹惟": "运筹帷幄", "烈火营": "烈火焚营",
        "舍舍生取义": "舍生取义", "时利等计": "时利 / 夺计",
        "见谋机动励心": "鬼谋 / 机动 / 励心", "度火": "渡火",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.strip()


def select(lines, title_y, column, low, high):
    values = []
    for line in lines:
        x = center(line["box"], 0)
        y = center(line["box"], 1)
        if column * 450 <= x < (column + 1) * 450 and title_y + low <= y <= title_y + high:
            values.append((y, normalize(line["text"]), float(line["score"])))
    return [value for _y, value, _score in sorted(values)]


def select_colored_books(lines, title_y, column, image):
    gold = []
    purple = []
    for line in lines:
        x = center(line["box"], 0)
        y = center(line["box"], 1)
        if not (column * 450 <= x < (column + 1) * 450 and title_y + 800 <= y <= title_y + 900):
            continue
        xs = [int(point[0]) for point in line["box"]]
        ys = [int(point[1]) for point in line["box"]]
        roi = image[max(0, min(ys)):min(image.shape[0], max(ys) + 1), max(0, min(xs)):min(image.shape[1], max(xs) + 1)]
        if roi.size == 0:
            continue
        median_bgr = np.median(roi.reshape(-1, 3), axis=0)
        target = gold if median_bgr[0] < 120 else purple
        target.append(normalize(line["text"]))
    return " / ".join(gold) or "未标注", " / ".join(purple) or "未标注"

def main():
    entries = []
    for path in sorted(OCR_DIR.glob("*.json")):
        if path.stem in SKIP:
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        lines = data["lines"]
        title_candidates = [line for line in lines if "阵" in line["text"]]
        if not title_candidates:
            raise RuntimeError(f"missing title: {path.stem}")
        title_line = title_candidates[0]
        title = normalize(title_line["text"])
        title_y = center(title_line["box"], 1)
        entries.append((path.stem, title, title_y, lines))

    if len(entries) != 50:
        raise RuntimeError(f"expected 50 teams, got {len(entries)}")

    out = [
        "# S2 阵容大全：阵容校正稿", "",
        "> 状态：已按原图 6 列 x 9 行切成单队格并完成字段化转录；正文仍在逐项人工校字。`>` 表示左侧优先、右侧替代，`/` 表示同级二选一。", "",
        "## 字段说明", "",
        "每队保存梯度、阵型、三名武将，并逐将保存进阶兵种、两项兵种专精、加点、两格战法、金色韬略、紫色韬略和装备/坐骑推荐属性。黄色标签与文字归入金色韬略，紫色文字归入紫色韬略；上卷、下卷属于金色韬略的卷别。演武只读取其中适用字段，不带入坐骑、装备和韬略。", "",
    ]

    for index, ((cell, _ocr_title, title_y, lines), tier, heroes, title) in enumerate(zip(entries, TIERS, HEROES, TITLES), 1):
        image_path = ROOT / "references" / "S2阵容大全" / "assets" / "team-cells" / f"{cell}.png"
        image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_COLOR)
        out.extend([
            f"## {index:02d}. {title}（{tier}）", "",
            f"- 原图格：`{cell}`；[局部图](assets/team-cells/{cell}.png)", "",
            "| 顺序 | 武将 | 站位 | 进阶兵种 | 兵种专精 | 加点 | 战法一 | 战法二 | 金色韬略 | 紫色韬略 | 装备/坐骑属性 |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ])
        for column in range(3):
            positions = [value for value in select(lines, title_y, column, 100, 190) if value in {"前排", "后排"}]
            position = " / ".join(positions) or "未标注"
            troop_values = [value for value in select(lines, title_y, column, 185, 240) if value not in {"前排", "后排"}]
            troop = " / ".join(troop_values) or "?"
            specs = " / ".join(select(lines, title_y, column, 230, 360)) or "?"
            adds = " / ".join(select(lines, title_y, column, 410, 510)) or "?"
            tactics = select(lines, title_y, column, 590, 790)
            gold_book, purple_books = select_colored_books(lines, title_y, column, image)
            gear = " / ".join(select(lines, title_y, column, 910, 1010)) or "?"
            override = FIELD_OVERRIDES.get((index, column + 1), {})
            position = override.get("position", position)
            troop = override.get("troop", troop)
            specs = override.get("specs", specs)
            adds = override.get("adds", adds)
            tactic_one = tactics[0] if tactics else "?"
            tactic_two = tactics[1] if len(tactics) > 1 else "?"
            out.append(
                f"| {column + 1} | {heroes[column]} | {position} | {troop} | {specs} | {adds} | {tactic_one} | {tactic_two} | {gold_book} | {purple_books} | {gear} |"
            )
        out.append("")

    OUTPUT.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {len(entries)} teams to {OUTPUT}")


if __name__ == "__main__":
    main()
