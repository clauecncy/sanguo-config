import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OCR_RUNTIME = PROJECT_ROOT / "references" / ".ocr-python"
sys.path.insert(0, str(OCR_RUNTIME))

from rapidocr_onnxruntime import RapidOCR  # noqa: E402


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(
            "usage: ocr_s2_crops_incremental.py INPUT_DIRECTORY OUTPUT_DIRECTORY"
        )

    input_directory = Path(sys.argv[1])
    output_directory = Path(sys.argv[2])
    output_directory.mkdir(parents=True, exist_ok=True)
    engine = RapidOCR()

    for image_path in sorted(input_directory.glob("*.png")):
        output_path = output_directory / f"{image_path.stem}.json"
        if output_path.exists():
            continue

        result, elapsed = engine(str(image_path))
        lines = []
        for box, text, score in result or []:
            lines.append(
                {
                    "box": [[round(float(x), 2), round(float(y), 2)] for x, y in box],
                    "text": text,
                    "score": round(float(score), 4),
                }
            )
        output_path.write_text(
            json.dumps({"elapsed": elapsed, "lines": lines}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
