"""Derive report figures from the saved T41 frozen-test predictions.

Usage (from the repository root, with the evaluation extras):
  uv run --locked --with-requirements environments/evaluation.in --with pillow \
      python docs/report/tools/t41_figures.py --run <runs/generic-frozen-test-20261123> \
      --annotations <binary_explosive_det_test.json> --images <IEDXray/Test>

Writes:
  docs/report/figures/t41-pr.csv          precision at 101 recall points (IoU 0.50, 0.75)
  docs/report/figures/private/t41-ex-*.png  annotated test images (ignored by Git)

Nothing is re-predicted: the script reads the saved predictions, checks their SHA-256
against the published values and confirms that AP@[.50:.95] reproduces exactly.
"""

import argparse
import contextlib
import csv
import hashlib
import io
import json
from pathlib import Path

PREDICTIONS = {  # docs/t41-results.md
    "control": "8160c3635f985b225b491be0694e11d252d84ed634cd4bc01d03c7e3c83a5431",
    "search_selected": "186474c38d6ea56a56dd7130c76c5917dd19b3e82023682ece20760a3f167ea3",
}
ANNOTATIONS_SHA256 = "1aad3787ba4964456e58bc07366dfcc6ce29db8a6ca06cc5c377a2add8d8ca43"
EXPECTED_AP = {"control": 41.5886, "search_selected": 48.0502}  # percent, 4 decimals
EXAMPLES = {1: "miss", 4918: "false-positive", 71: "label-question"}
THRESHOLD = 0.25
OUT = Path(__file__).resolve().parents[1] / "figures"


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_predictions(run, role):
    path = Path(run) / role / "predictions.jsonl"
    if sha256(path) != PREDICTIONS[role]:
        raise SystemExit(f"{path}: hash differs from docs/t41-results.md")
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
    return [d for r in records for d in r["detections"]]


def precision_curves(truth_path, detections):
    from pycocotools.coco import COCO
    from pycocotools.cocoeval import COCOeval

    with contextlib.redirect_stdout(io.StringIO()):
        truth = COCO(str(truth_path))
        result = truth.loadRes(detections)
        evaluator = COCOeval(truth, result, "bbox")
        evaluator.evaluate()
        evaluator.accumulate()
        evaluator.summarize()
    precision = evaluator.eval["precision"]  # [IoU, recall, class, area, maxDets]
    # IoU index 0 = 0.50, 5 = 0.75; class 0; area "all"; maxDets 100.
    return evaluator.stats[0] * 100, precision[0, :, 0, 0, 2], precision[5, :, 0, 0, 2]


def draw_examples(truth, images_dir, predictions):
    from PIL import Image, ImageDraw, ImageFont

    names = {image["id"]: image["file_name"] for image in truth["images"]}
    boxes = {}
    for annotation in truth["annotations"]:
        boxes.setdefault(annotation["image_id"], []).append(annotation["bbox"])
    colours = {"control": (31, 60, 160), "search_selected": (214, 110, 0)}
    (OUT / "private").mkdir(exist_ok=True)
    for image_id, tag in EXAMPLES.items():
        panels = []
        for role in ("control", "search_selected"):
            image = Image.open(Path(images_dir) / names[image_id]).convert("RGB")
            draw = ImageDraw.Draw(image)
            width = max(3, image.width // 160)
            font = ImageFont.load_default(size=max(14, image.height // 16))
            for x, y, w, h in boxes.get(image_id, []):  # ground truth: magenta
                draw.rectangle([x, y, x + w, y + h], outline=(200, 0, 200), width=width)
            own = sorted((d for d in predictions[role] if d["image_id"] == image_id),
                         key=lambda d: -d["score"])
            for rank, d in enumerate(own):
                x, y, w, h = d["bbox"]
                # Detections at the operating point in the model colour; otherwise only the
                # highest-scoring detection, in dark grey, so a near miss is visible.
                if d["score"] >= THRESHOLD or rank == 0:
                    style = colours[role] if d["score"] >= THRESHOLD else (70, 70, 70)
                    draw.rectangle([x, y, x + w, y + h], outline=style, width=width)
                    label = f"{d['score']:.3f}"
                    box = draw.textbbox((x, y), label, font=font)
                    top = max(0, y - (box[3] - box[1]) - 6)
                    draw.rectangle([x, top, x + box[2] - box[0] + 6, top + box[3] - box[1] + 6],
                                   fill="white")
                    draw.text((x + 3, top + 1), label, fill=style, font=font)
            panels.append(image)
        gap = 12
        canvas = Image.new("RGB", (panels[0].width * 2 + gap, panels[0].height), "white")
        canvas.paste(panels[0], (0, 0))
        canvas.paste(panels[1], (panels[0].width + gap, 0))
        canvas.save(OUT / "private" / f"t41-ex-{tag}.png")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--run", required=True)
    parser.add_argument("--annotations", required=True)
    parser.add_argument("--images", required=True)
    args = parser.parse_args()
    if sha256(args.annotations) != ANNOTATIONS_SHA256:
        raise SystemExit("test annotations differ from the frozen plan")
    truth = json.loads(Path(args.annotations).read_text(encoding="utf-8"))
    predictions = {role: load_predictions(args.run, role) for role in PREDICTIONS}

    curves = {}
    for role, detections in predictions.items():
        ap, p50, p75 = precision_curves(args.annotations, detections)
        if round(ap, 4) != EXPECTED_AP[role]:
            raise SystemExit(f"{role}: AP {ap:.4f} does not reproduce {EXPECTED_AP[role]}")
        curves[role] = (p50, p75)
        print(f"{role}: AP {ap:.4f} reproduced")

    with (OUT / "t41-pr.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["recall", "control_iou50", "candidate_iou50",
                         "control_iou75", "candidate_iou75"])
        for i in range(101):
            row = [i / 100]
            values = [curves["control"][0][i], curves["search_selected"][0][i],
                      curves["control"][1][i], curves["search_selected"][1][i]]
            writer.writerow(row + [f"{max(v, 0) * 100:.4f}" for v in values])
    draw_examples(truth, args.images, predictions)
    print("wrote t41-pr.csv and private example images")


if __name__ == "__main__":
    main()
