"""Evaluate one frozen T41 checkpoint pair in a Slurm GPU allocation.

The private plan binds code, checkpoints, general initialization, test annotations,
image bytes and fixed settings before any test prediction. Outputs are COCO-native
original-pixel xywh: positive wholly outside predictions remain in the evaluation.
This is not a GUI record, whose box contract requires in-image coordinates.
"""

import argparse
import hashlib
import json
import math
import os
import statistics
import time
from pathlib import Path


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write(path, value):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


def checked_plan(plan, code_root):
    if plan["schema"] != "t41-frozen-test-pair-1":
        raise ValueError("unknown evaluation plan")
    if plan["settings"] != {"conf": 0.001, "max_det": 300}:
        raise ValueError("frozen prediction settings differ")
    if plan["operating_point"] != {"threshold": 0.25, "iou": 0.5}:
        raise ValueError("frozen operating point differs")
    if [row["role"] for row in plan["models"]] != ["control", "search_selected"]:
        raise ValueError("evaluate exactly the preselected control and candidate")
    if len({row["sha256"] for row in plan["models"]}) != 2:
        raise ValueError("two different selected checkpoints required")
    for row in [plan["ground_truth"], plan["initialization"], *plan["models"],
                *plan["training_receipts"]]:
        if sha256(row["path"]) != row["sha256"]:
            raise ValueError("frozen artifact changed")
    for row in plan["code_files"]:
        path = (code_root / row["path"]).resolve()
        if not path.is_relative_to(code_root.resolve()) or sha256(path) != row["sha256"]:
            raise ValueError("frozen executable source changed")
    return json.loads(Path(plan["ground_truth"]["path"]).read_text(encoding="utf-8"))


def run(plan_path, output):
    if not os.environ.get("SLURM_JOB_ID") or os.environ.get("SLURM_CPUS_PER_TASK") != "4":
        raise ValueError("requires the declared Slurm allocation")
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    code_root = Path(__file__).resolve().parents[1]
    truth = checked_plan(plan, code_root)
    import torch

    from sdp_xray.coco_metrics import coco_bbox_metrics, evaluator_version
    from sdp_xray.evaluation import check_ground_truth, operating_point
    from sdp_xray.training_validation import _predictor_factory

    if not torch.cuda.is_available() or torch.cuda.device_count() != 1:
        raise ValueError("exactly one allocated GPU required")
    if evaluator_version() != "2.0.11":
        raise ValueError("frozen evaluator version differs")
    torch.set_num_threads(4)
    index = check_ground_truth(truth, {"0": "Explosive"})
    images = sorted(truth["images"], key=lambda row: row["id"])
    ids = [row["id"] for row in images]
    if len(images) != 5136 or len(truth["annotations"]) != 3204:
        raise ValueError("published generic test membership differs")
    inventory = {row["id"]: row for row in plan["images"]}
    if sorted(inventory) != ids:
        raise ValueError("frozen image inventory differs")
    output.mkdir(parents=True, exist_ok=False)
    write(output / "frozen-plan.json", plan)
    summaries = []
    for model in plan["models"]:
        folder = output / model["role"]
        folder.mkdir()
        torch.cuda.reset_peak_memory_stats()
        predictor = _predictor_factory(Path(model["path"]), plan["settings"])
        if predictor.model.names != {0: "Explosive"}:
            raise ValueError("checkpoint class order differs")
        # Warm up on validation only; no settings or model choices are changed.
        warmup = plan["warmup"]
        if sha256(warmup["path"]) != warmup["sha256"]:
            raise ValueError("validation warmup image changed")
        for _ in range(5):
            list(predictor(source=warmup["path"], stream=False))
        torch.cuda.synchronize()
        detections, timings, model_ms, events = [], [], [], []
        started = time.perf_counter()
        with (folder / "predictions.jsonl").open("x", encoding="utf-8") as stream:
            for image in images:
                path = Path(plan["image_root"]) / image["file_name"]
                if sha256(path) != inventory[image["id"]]["sha256"]:
                    raise ValueError("published image bytes changed")
                torch.cuda.synchronize()
                before = time.perf_counter()
                result, = predictor(source=str(path), stream=False)
                torch.cuda.synchronize()
                elapsed = time.perf_counter() - before
                if list(result.orig_shape) != [image["height"], image["width"]]:
                    raise ValueError("prediction image dimensions differ")
                current = []
                for box, score, category in zip(result.boxes.xyxy.cpu().tolist(),
                                                 result.boxes.conf.cpu().tolist(),
                                                 result.boxes.cls.cpu().tolist(), strict=True):
                    if (category != 0 or not math.isfinite(score) or not 0 <= score <= 1
                            or any(not math.isfinite(v) for v in box)
                            or box[2] <= box[0] or box[3] <= box[1]):
                        raise ValueError("invalid model-produced detection")
                    current.append({"image_id": image["id"], "category_id": 0,
                                    "bbox": [box[0], box[1], box[2] - box[0], box[3] - box[1]],
                                    "score": score})
                geometry = getattr(result, "rayguard_geometry_events", [])
                events.extend({"image_id": image["id"], **event} for event in geometry)
                record = {"image_id": image["id"], "status": "ok", "detections": current,
                          "synchronized_predict_seconds": elapsed, "speed_ms": result.speed,
                          "geometry_events": geometry}
                stream.write(json.dumps(record, allow_nan=False) + "\n")
                detections.extend(current)
                timings.append(elapsed)
                model_ms.append(float(result.speed["inference"]))
                if len(timings) % 500 == 0:
                    stream.flush()
                    print(model["role"], len(timings), "images", flush=True)
        if sha256(model["path"]) != model["sha256"]:
            raise ValueError("checkpoint changed during inference")
        metrics = coco_bbox_metrics(truth, detections, ids)
        point = operating_point(truth, index, detections, ids, **plan["operating_point"])
        row = {"role": model["role"], "checkpoint_sha256": model["sha256"],
               "parent_sha256": plan["initialization"]["sha256"], "images": len(timings),
               "detections": len(detections), "metrics": metrics, "operating_point": point,
               "geometry_events": events, "predictions_sha256": sha256(folder / "predictions.jsonl"),
               "wall_seconds": time.perf_counter() - started,
               "predict_p50_seconds": statistics.median(timings),
               "predict_p95_seconds": sorted(timings)[math.ceil(0.95 * len(timings)) - 1],
               "model_p50_ms": statistics.median(model_ms),
               "model_p95_ms": sorted(model_ms)[math.ceil(0.95 * len(model_ms)) - 1],
               "model_timing_boundary": "pinned predictor inference Profile; preprocessing/postprocessing excluded",
               "timing_boundary": "synchronized predictor call including load/preprocess/model/postprocess; excludes input hashing and record writing",
               "warmup_images": 5, "peak_cuda_allocated": torch.cuda.max_memory_allocated(),
               "peak_cuda_reserved": torch.cuda.max_memory_reserved()}
        write(folder / "evaluation.json", row)
        summaries.append(row)
        del predictor
        torch.cuda.empty_cache()
    assert sha256(plan["ground_truth"]["path"]) == plan["ground_truth"]["sha256"]
    report = {"status": "complete", "slurm_job_id": os.environ["SLURM_JOB_ID"],
              "gpu": torch.cuda.get_device_name(0), "plan_sha256": sha256(plan_path),
              "code_commit": plan["code_commit"], "models": summaries,
              "candidate_minus_control": {key: None if value is None or summaries[1]["metrics"][key] is None
                                          else summaries[1]["metrics"][key] - value
                                          for key, value in summaries[0]["metrics"].items()},
              "limitations": plan["limitations"], "training_started": False}
    write(output / "comparison.json", report)
    print(json.dumps({"status": "complete", "job": report["slurm_job_id"],
                      "metrics": [row["metrics"] for row in summaries]}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run(args.plan, args.output)
