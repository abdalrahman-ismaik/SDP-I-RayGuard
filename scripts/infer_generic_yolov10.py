"""One real generic-threat forward pass using the pinned original YOLOv10 fork.

This is a CPU reference, not the complete P1 pipeline or an evaluation tool.
Only load author-supplied, inspected checkpoints with their recorded SHA-256.
"""

import argparse
import hashlib
import importlib.metadata as metadata
import json
import os
import platform
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter
from unittest.mock import patch

UPSTREAM_REVISION = "453c6e38a51e9d1d5a2aa5fb7f1014a711913397"
UPSTREAM_URL = f"https://github.com/THU-MIG/yolov10/archive/{UPSTREAM_REVISION}.zip"


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", type=Path)
    parser.add_argument("image", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--checkpoint-sha256", required=True)
    parser.add_argument("--confidence", type=float, default=0.25)
    args = parser.parse_args()
    if not 0 <= args.confidence <= 1:
        parser.error("confidence must be between zero and one")
    checkpoint = args.checkpoint.resolve(strict=True)
    image_path = args.image.resolve(strict=True)
    if sha256(checkpoint) != args.checkpoint_sha256:
        parser.error("checkpoint SHA-256 differs from the inspected artifact")
    distribution = metadata.distribution("ultralytics")
    source = json.loads(distribution.read_text("direct_url.json") or "{}")
    if distribution.version != "8.1.34" or source.get("url") != UPSTREAM_URL:
        parser.error("use the original fork pinned in docs/first-inference.md")

    args.output.mkdir(parents=True, exist_ok=False)
    os.environ["YOLO_CONFIG_DIR"] = str(args.output.resolve() / "yolo-config")
    os.environ["YOLO_AUTOINSTALL"] = "false"
    os.environ["HF_HUB_OFFLINE"] = "1"
    manifest = {
        "status": "started",
        "timestamp_utc": datetime.now(UTC).isoformat(),
        "command": [sys.executable, *sys.argv],
        "script_sha256": sha256(Path(__file__)),
        "git_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "git_status": subprocess.check_output(["git", "status", "--porcelain"], text=True),
        "checkpoint": str(checkpoint),
        "checkpoint_sha256": args.checkpoint_sha256,
        "input": str(image_path),
        "input_sha256": sha256(image_path),
        "upstream_revision": UPSTREAM_REVISION,
        "upstream_distribution": source,
        "python": platform.python_version(),
        "platform": platform.platform(),
        "device": "cpu",
        "precision": "float32",
        "seed": None,
        "seed_policy": "not set; evaluation-mode inference with augmentation disabled",
        "annotations_used_for_prediction": False,
        "task": "iedxray.generic_explosive_detection",
        "source_category_map": {"0": "Explosive"},
        "settings": {"imgsz": 640, "batch": 1, "conf": args.confidence,
                     "max_det": 300, "augment": False},
        "preprocessing": "original fork LetterBox auto=True for one PT image; RGB / 255",
        "postprocessing": "original fork one-to-one head, top-k, no NMS",
        "limitations": ["single-image smoke test; no accuracy metrics",
                        "CPU cold-run timing; not benchmark FPS",
                        "author's exact source revision/environment unverified"],
    }
    try:
        import torch
        from PIL import Image, ImageDraw
        from ultralytics import YOLOv10
        from ultralytics.utils import SETTINGS

        from sdp_xray.common.contracts import validate_scan_result

        SETTINGS.update({"sync": False})
        manifest["packages"] = {
            package: metadata.version(package) for package in
            ("torch", "torchvision", "ultralytics", "numpy", "opencv-python", "Pillow")
        }
        original_load = torch.load

        def load_inspected_file(path, *positional, **kwargs):
            # The original fork predates PyTorch's weights_only default. Limit this
            # compatibility override to the one explicitly hashed author artifact.
            if Path(path).resolve() != checkpoint:
                raise ValueError("unexpected checkpoint load")
            kwargs["weights_only"] = False
            return original_load(path, *positional, **kwargs)

        start = perf_counter()
        with patch("torch.load", load_inspected_file):
            model = YOLOv10(str(checkpoint))
        manifest["load_seconds"] = perf_counter() - start
        if model.names != {0: "Explosive"}:
            raise ValueError(f"expected the inspected generic task; got {model.names}")
        manifest["model_names"] = model.names
        manifest["model_yaml"] = model.model.yaml
        input_shapes = []
        hook = model.model.register_forward_pre_hook(
            lambda module, inputs: input_shapes.append(list(inputs[0].shape))
        )
        start = perf_counter()
        try:
            prediction = model.predict(
                source=str(image_path), device="cpu", half=False, save=False, verbose=False,
                **manifest["settings"],
            )[0]
        finally:
            hook.remove()
        manifest["predict_call_seconds"] = perf_counter() - start
        manifest["forward_input_shapes_including_warmup"] = input_shapes
        manifest["prediction_input_shape"] = input_shapes[-1]
        manifest["upstream_stage_milliseconds"] = prediction.speed
        with Image.open(image_path) as image:
            overlay = image.convert("RGB")
        result = {
            "schema_version": "1.0", "scan_id": image_path.stem, "status": "ok",
            "image": {"width": overlay.width, "height": overlay.height},
            "model": {"id": "author-yolov10m-generic", "task": manifest["task"],
                      "provenance": f"sha256:{args.checkpoint_sha256}"},
            "run": {"id": args.output.name, "provenance": "manifest.json"},
            "threshold": args.confidence, "detections": [], "error": None,
        }
        for index, box in enumerate(prediction.boxes):
            class_id = int(box.cls.item())
            if class_id != 0:
                raise ValueError(f"unexpected predicted class {class_id}")
            result["detections"].append({
                "id": f"threat-{index}", "kind": "suspicious_region",
                "box_xyxy": box.xyxy[0].cpu().tolist(),
                "category": {"namespace": manifest["task"], "label": model.names[class_id]},
                "confidence": float(box.conf.item()), "device_id": None,
            })
        validate_scan_result(result)
        draw = ImageDraw.Draw(overlay)
        for detection in result["detections"]:
            box = detection["box_xyxy"]
            draw.rectangle(box, outline="red", width=2)
            draw.text((box[0], max(0, box[1] - 12)),
                      f'Explosive {detection["confidence"]:.3f}', fill="red")
        draw.text((5, 5), "MODEL PREDICTIONS - smoke test", fill="red")
        overlay.save(args.output / "overlay.png")
        (args.output / "predictions.json").write_text(json.dumps(result, indent=2) + "\n")
        manifest.update(status="ok", detection_count=len(result["detections"]),
                        output_sha256={name: sha256(args.output / name)
                                       for name in ("overlay.png", "predictions.json")})
        print(json.dumps({"status": "ok", "detections": len(result["detections"]),
                          "output": str(args.output)}))
    except Exception as error:
        manifest.update(status="error", error=f"{type(error).__name__}: {error}")
        raise
    finally:
        (args.output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
