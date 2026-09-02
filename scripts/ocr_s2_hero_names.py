import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OCR_RUNTIME = PROJECT_ROOT / "references" / ".ocr-python"
sys.path.insert(0, str(OCR_RUNTIME))

import cv2  # noqa: E402
import numpy as np  # noqa: E402
from rapidocr_onnxruntime import RapidOCR  # noqa: E402


SKIP_CELLS = {"r01-c01", "r01-c02", "r02-c01", "r02-c02"}


def center_y(box: list[list[float]]) -> float:
    return sum(point[1] for point in box) / len(box)


def texts(result: list | None) -> list[dict]:
    return [
        {"text": text, "score": round(float(score), 4)}
        for _box, text, score in (result or [])
    ]


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: ocr_s2_hero_names.py CELL_DIR CELL_OCR_DIR OUTPUT_DIR"
        )

    cell_directory = Path(sys.argv[1])
    cell_ocr_directory = Path(sys.argv[2])
    output_directory = Path(sys.argv[3])
    output_directory.mkdir(parents=True, exist_ok=True)
    engine = RapidOCR()

    for image_path in sorted(cell_directory.glob("*.png")):
        if image_path.stem in SKIP_CELLS:
            continue
        output_path = output_directory / f"{image_path.stem}.json"
        if output_path.exists():
            continue

        cell_ocr = json.loads(
            (cell_ocr_directory / f"{image_path.stem}.json").read_text(encoding="utf-8")
        )
        title_lines = [
            line for line in cell_ocr["lines"] if "阵" in line["text"]
        ]
        title_y = center_y(title_lines[0]["box"]) if title_lines else 180.0

        image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_COLOR)
        y1 = max(0, int(title_y + 455))
        y2 = min(image.shape[0], int(title_y + 585))
        heroes = []

        for index in range(3):
            x1 = index * image.shape[1] // 3
            x2 = (index + 1) * image.shape[1] // 3
            roi = image[y1:y2, x1:x2]
            hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            gold = cv2.inRange(hsv, np.array([7, 35, 90]), np.array([45, 255, 255]))
            binary = 255 - gold
            binary = cv2.resize(binary, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            original = cv2.resize(roi, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            original_result, _ = engine(original)
            binary_result, _ = engine(binary)
            heroes.append(
                {
                    "original": texts(original_result),
                    "gold_mask": texts(binary_result),
                }
            )

        output_path.write_text(
            json.dumps(
                {"title_y": round(title_y, 2), "heroes": heroes},
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()

