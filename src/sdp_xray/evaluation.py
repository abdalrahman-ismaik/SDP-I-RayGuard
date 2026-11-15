"""Prepare shared run records for COCO box evaluation and compare matched records (T42).

Pure Python with no model or metric dependencies. The COCO metrics themselves come from
pycocotools in coco_metrics.py. See docs/single-scan-evaluation-protocol.md.

Coordinate conventions:
- Shared records (sdp_xray.common.contracts) use original-image pixel ``box_xyxy``.
- COCO ground truth and COCO detections use original-image pixel ``[x, y, width, height]``.

Category namespaces:
- A detection's ``category.label`` belongs to the model task namespace (``model.task``).
- COCO ``category_id`` is the dataset's own ID. Labels are mapped to IDs only through the
  manifest's ``model.source_category_map``. Model output indices are never used as COCO IDs.
  For the generic task, ID 0 ``Explosive`` is valid and is not renumbered.

Nothing here infers benign outcomes. An ``ok`` scan with no detections means the model
reported nothing. A failed scan is reported as a failure, never as an empty prediction.
"""

import json
import math
from pathlib import PurePath
from typing import Any

from sdp_xray.common.contracts import SCHEMA_VERSION, _number, _object, _score, _text
from sdp_xray.common.run_manifest import _sha256, validate_prediction_set

# Fields that must agree for a baseline and a candidate to be compared as a matched pair.
MATCHED_MODEL_FIELDS = ("task", "kind", "model_names", "source_category_map")
MATCHED_TOP_FIELDS = ("settings", "stages", "precision")

PROTOCOL_FIELDS = {
    "schema_version",
    "protocol_id",
    "status",
    "task",
    "ground_truth",
    "evaluator",
    "score_floor",
    "operating_point",
    "flagged_images",
    "limitations",
}


# --- coordinates -------------------------------------------------------------------------


def xyxy_to_xywh(box: list[float]) -> list[float]:
    """Original-pixel corners [x1, y1, x2, y2] to COCO [x, y, width, height]."""
    x1, y1, x2, y2 = box
    if not (x2 > x1 and y2 > y1):
        raise ValueError("box must have positive width and height")
    return [x1, y1, x2 - x1, y2 - y1]


def iou_xywh(a: list[float], b: list[float]) -> float:
    """Intersection over union of two COCO [x, y, width, height] boxes."""
    left, top = max(a[0], b[0]), max(a[1], b[1])
    right, bottom = min(a[0] + a[2], b[0] + b[2]), min(a[1] + a[3], b[1] + b[3])
    inter = max(0.0, right - left) * max(0.0, bottom - top)
    union = a[2] * a[3] + b[2] * b[3] - inter
    return inter / union if union > 0 else 0.0


# --- ground truth ------------------------------------------------------------------------


def check_ground_truth(ground_truth: Any, category_map: dict[str, str]) -> dict[str, Any]:
    """Check a COCO ground-truth file against a model's category map, without changing it.

    Returns an index: ``images_by_stem`` (scan ID -> image record) and a summary with
    counts and boxes outside the image. Out-of-bounds boxes are reported, never clipped.
    """
    if not isinstance(ground_truth, dict):
        raise ValueError("ground truth must be a COCO object")
    for key in ("images", "annotations", "categories"):
        if not isinstance(ground_truth.get(key), list):
            raise ValueError(f"ground truth must contain a {key} list")

    categories = {}
    for category in ground_truth["categories"]:
        if type(category.get("id")) is not int:
            raise ValueError("category IDs must be integers")
        categories[str(category["id"])] = category.get("name")
    if categories != category_map:
        raise ValueError(
            f"ground-truth categories {categories} differ from the model's "
            f"source_category_map {category_map}; this is not the model's task"
        )

    images_by_id: dict[int, dict[str, Any]] = {}
    images_by_stem: dict[str, dict[str, Any]] = {}
    for image in ground_truth["images"]:
        image_id = image.get("id")
        if type(image_id) is not int or image_id in images_by_id:
            raise ValueError("image IDs must be unique integers")
        for key in ("width", "height"):
            if type(image.get(key)) is not int or image[key] <= 0:
                raise ValueError(f"image {image_id}: {key} must be a positive integer")
        _text(image.get("file_name"), f"image {image_id} file_name")
        # The runner names each scan after its image file stem; the stem must be unique.
        stem = PurePath(image["file_name"].replace("\\", "/")).stem
        if stem in images_by_stem:
            raise ValueError(f"two ground-truth images share the file stem {stem!r}")
        images_by_id[image_id] = image
        images_by_stem[stem] = image

    out_of_bounds = []
    for annotation in ground_truth["annotations"]:
        if annotation.get("image_id") not in images_by_id:
            raise ValueError("annotation refers to an unknown image ID")
        if str(annotation.get("category_id")) not in category_map:
            raise ValueError("annotation refers to an unknown category ID")
        # COCOeval reads area and iscrowd; refuse to guess them.
        if "area" not in annotation or annotation.get("iscrowd") not in (0, 1):
            raise ValueError("annotations need area and iscrowd (0 or 1) for COCOeval")
        box = annotation.get("bbox")
        if not isinstance(box, list) or len(box) != 4:
            raise ValueError("annotation bbox must be [x, y, width, height]")
        for value in box:
            _number(value, "annotation bbox value")
        if box[2] <= 0 or box[3] <= 0:
            raise ValueError("annotation bbox must have positive width and height")
        image = images_by_id[annotation["image_id"]]
        x, y, w, h = box
        if x < 0 or y < 0 or x + w > image["width"] or y + h > image["height"]:
            out_of_bounds.append(image["file_name"])

    annotated = {annotation["image_id"] for annotation in ground_truth["annotations"]}
    return {
        "images_by_id": images_by_id,
        "images_by_stem": images_by_stem,
        "summary": {
            "images": len(images_by_id),
            "annotations": len(ground_truth["annotations"]),
            "annotation_empty_images": len(images_by_id) - len(annotated),
            "boxes_outside_image": len(out_of_bounds),
            "crowd_annotations": sum(a["iscrowd"] == 1 for a in ground_truth["annotations"]),
        },
    }


# --- record to COCO detections -----------------------------------------------------------


def coco_detections(
    manifest: dict[str, Any],
    results: list[dict[str, Any]],
    index: dict[str, Any],
    allow_subset: bool = False,
) -> dict[str, Any]:
    """Convert a validated shared record into COCO detections for one ground-truth file.

    Every scan must name a ground-truth image with the same dimensions. Unless
    ``allow_subset`` is set, every ground-truth image must have an ``ok`` result: a missing
    image or a failed scan stops the full evaluation instead of silently shrinking it.
    """
    validate_prediction_set(manifest, results)
    label_to_id = {label: int(key) for key, label in manifest["model"]["source_category_map"].items()}
    detections, evaluated, failed = [], [], []
    for result in results:
        image = index["images_by_stem"].get(result["scan_id"])
        if image is None:
            raise ValueError(f"{result['scan_id']}: scan is not in the ground-truth images")
        if result["status"] != "ok":
            failed.append(result["scan_id"])
            continue
        if result["image"] != {"width": image["width"], "height": image["height"]}:
            raise ValueError(f"{result['scan_id']}: image size differs from the ground truth")
        evaluated.append(image["id"])
        for detection in result["detections"]:
            detections.append({
                "image_id": image["id"],
                "category_id": label_to_id[detection["category"]["label"]],
                "bbox": xyxy_to_xywh(detection["box_xyxy"]),
                "score": detection["confidence"],
            })
    missing = len(index["images_by_id"]) - len(evaluated) - len(failed)
    if not allow_subset and (missing or failed):
        raise ValueError(
            f"{missing} ground-truth images have no result and {len(failed)} scans failed; "
            "a full evaluation needs every image (use allow_subset only for a labelled subset)"
        )
    return {
        "detections": detections,
        "image_ids": sorted(evaluated),
        "coverage": {
            "evaluated_images": len(evaluated),
            "failed_scans": sorted(failed),
            "images_without_result": missing,
            "subset": bool(missing or failed),
        },
    }


# --- operating point ---------------------------------------------------------------------


def operating_point(
    ground_truth: dict[str, Any],
    index: dict[str, Any],
    detections: list[dict[str, Any]],
    image_ids: list[int],
    threshold: float,
    iou: float = 0.5,
) -> dict[str, Any]:
    """Counts at one fixed score threshold, using greedy same-category matching.

    Detections are taken in descending score order; each takes the unmatched ground-truth
    box of its category with the highest IoU at or above ``iou``. Crowd boxes are not
    supported here. This is a fixed-threshold summary, not a COCO metric.
    """
    _score(threshold, "threshold")
    _score(iou, "iou")
    wanted = set(image_ids)
    truth: dict[int, list[dict[str, Any]]] = {image_id: [] for image_id in wanted}
    for annotation in ground_truth["annotations"]:
        if annotation["image_id"] in wanted:
            if annotation["iscrowd"]:
                raise ValueError("crowd annotations are not supported at the operating point")
            truth[annotation["image_id"]].append(annotation)

    kept = [d for d in detections if d["image_id"] in wanted and d["score"] >= threshold]
    kept.sort(key=lambda d: d["score"], reverse=True)
    used: set[int] = set()
    true_pos, false_pos = 0, []
    for detection in kept:
        best, best_iou = None, iou
        for annotation in truth[detection["image_id"]]:
            key = id(annotation)
            if key in used or annotation["category_id"] != detection["category_id"]:
                continue
            overlap = iou_xywh(detection["bbox"], annotation["bbox"])
            if overlap >= best_iou:
                best, best_iou = key, overlap
        if best is None:
            false_pos.append(detection)
        else:
            used.add(best)
            true_pos += 1

    misses = [a for image_id in sorted(wanted) for a in truth[image_id] if id(a) not in used]
    total_truth = sum(len(boxes) for boxes in truth.values())
    empty_images = {image_id for image_id, boxes in truth.items() if not boxes}

    def name(image_id: int) -> str:
        return index["images_by_id"][image_id]["file_name"]

    return {
        "threshold": threshold,
        "iou": iou,
        "true_positives": true_pos,
        "false_positives": len(false_pos),
        "missed_boxes": len(misses),
        # Wording is deliberate: annotation-empty is not the same as benign.
        "false_positives_on_annotation_empty_images": sum(
            d["image_id"] in empty_images for d in false_pos
        ),
        "precision": true_pos / len(kept) if kept else None,
        "recall": true_pos / total_truth if total_truth else None,
        "missed_examples": [
            {"file_name": name(a["image_id"]), "bbox": a["bbox"]} for a in misses
        ],
        "false_positive_examples": [
            {"file_name": name(d["image_id"]), "bbox": d["bbox"], "score": d["score"]}
            for d in false_pos
        ],
    }


# --- protocol ----------------------------------------------------------------------------


def validate_protocol(protocol: Any) -> None:
    """Raise ValueError unless this is a complete frozen evaluation protocol."""
    _object(protocol, PROTOCOL_FIELDS, "protocol")
    if protocol["schema_version"] != SCHEMA_VERSION:
        raise ValueError(f"protocol schema_version must be {SCHEMA_VERSION!r}")
    for key in ("protocol_id", "task"):
        _text(protocol[key], key)
    if protocol["status"] not in ("draft", "approved"):
        raise ValueError("protocol status must be draft or approved")
    gt = protocol["ground_truth"]
    _object(gt, {"file_name", "sha256", "images", "annotations"}, "protocol.ground_truth")
    _text(gt["file_name"], "ground_truth.file_name")
    if gt["sha256"] is not None:
        _sha256(gt["sha256"], "ground_truth.sha256")
    for key in ("images", "annotations"):
        if type(gt[key]) is not int or gt[key] < 0:
            raise ValueError(f"ground_truth.{key} must be a nonnegative integer")
    _object(protocol["evaluator"], {"package", "version", "iou_type"}, "protocol.evaluator")
    if protocol["evaluator"]["iou_type"] != "bbox":
        raise ValueError("only bbox evaluation is supported")
    _score(protocol["score_floor"], "score_floor")
    point = protocol["operating_point"]
    _object(point, {"threshold", "iou", "basis"}, "protocol.operating_point")
    _score(point["threshold"], "operating_point.threshold")
    _score(point["iou"], "operating_point.iou")
    _text(point["basis"], "operating_point.basis")
    for key in ("flagged_images", "limitations"):
        if not isinstance(protocol[key], list):
            raise ValueError(f"{key} must be a list")
    for item in protocol["flagged_images"]:
        _object(item, {"file_name", "reason"}, "flagged image")
        _text(item["file_name"], "flagged_images.file_name")
        _text(item["reason"], "flagged_images.reason")
    for item in protocol["limitations"]:
        _text(item, "limitation")


def check_protocol(
    protocol: dict[str, Any],
    manifest: dict[str, Any],
    summary: dict[str, Any],
    ground_truth_sha256: str,
) -> None:
    """Refuse to evaluate a record that does not fit the frozen protocol."""
    validate_protocol(protocol)
    if manifest["model"]["task"] != protocol["task"]:
        raise ValueError("record task differs from the protocol task")
    if manifest["settings"]["conf"] > protocol["score_floor"]:
        raise ValueError(
            f"record was run at conf={manifest['settings']['conf']}, above the protocol "
            f"score floor {protocol['score_floor']}; AP needs low-score predictions"
        )
    if protocol["operating_point"]["threshold"] < manifest["settings"]["conf"]:
        raise ValueError("operating threshold is below the record's score floor")
    expected = protocol["ground_truth"]
    if expected["sha256"] is not None and expected["sha256"] != ground_truth_sha256:
        raise ValueError("ground-truth file hash differs from the protocol")
    if (summary["images"], summary["annotations"]) != (expected["images"], expected["annotations"]):
        raise ValueError("ground-truth image/annotation counts differ from the protocol")


# --- matched comparison ------------------------------------------------------------------


def matched_pair_differences(baseline: dict[str, Any], candidate: dict[str, Any]) -> list[str]:
    """List every reason two manifests are not a fair matched pair. Empty means matched."""
    problems = []
    if baseline["role"] != "baseline":
        problems.append("first record is not role=baseline")
    if candidate["role"] != "candidate":
        problems.append("second record is not role=candidate")
    if candidate["model"]["parent_checkpoint_sha256"] != baseline["model"]["checkpoint_sha256"]:
        problems.append("candidate was not initialized from the baseline checkpoint")
    for key in MATCHED_MODEL_FIELDS:
        if baseline["model"][key] != candidate["model"][key]:
            problems.append(f"model.{key} differs")
    for key in MATCHED_TOP_FIELDS:
        if baseline[key] != candidate[key]:
            problems.append(f"{key} differs")
    if baseline["code"]["upstream_revision"] != candidate["code"]["upstream_revision"]:
        problems.append("code.upstream_revision differs")
    inputs = {item["scan_id"]: item["sha256"] for item in baseline["inputs"]}
    if inputs != {item["scan_id"]: item["sha256"] for item in candidate["inputs"]}:
        problems.append("input scans or image hashes differ")
    return problems


# --- report ------------------------------------------------------------------------------

REPORT_FIELDS = {
    "schema_version",
    "evidence",
    "protocol",
    "ground_truth",
    "record",
    "evaluator",
    "coverage",
    "metrics",
    "operating_point",
    "flagged_images_present",
    "limitations",
}


def build_report(
    protocol: dict[str, Any],
    summary: dict[str, Any],
    ground_truth_sha256: str,
    manifest: dict[str, Any],
    manifest_sha256: str,
    evaluator_version: str,
    prepared: dict[str, Any],
    metrics: dict[str, float | None],
    point: dict[str, Any],
    index: dict[str, Any],
) -> dict[str, Any]:
    """Assemble one evaluation report. It holds file names and hashes, never local paths."""
    names = {index["images_by_id"][image_id]["file_name"] for image_id in prepared["image_ids"]}
    return {
        "schema_version": SCHEMA_VERSION,
        # Synthetic fixtures and unapproved protocols must never read as project metrics.
        "evidence": "approved-protocol" if protocol["status"] == "approved" else "draft-protocol",
        "protocol": {"id": protocol["protocol_id"], "status": protocol["status"]},
        "ground_truth": {"file_name": protocol["ground_truth"]["file_name"],
                         "sha256": ground_truth_sha256, **summary},
        "record": {
            "run_id": manifest["run_id"],
            "role": manifest["role"],
            "status": manifest["status"],
            "model_id": manifest["model"]["id"],
            "task": manifest["model"]["task"],
            "checkpoint_sha256": manifest["model"]["checkpoint_sha256"],
            "parent_checkpoint_sha256": manifest["model"]["parent_checkpoint_sha256"],
            "manifest_sha256": manifest_sha256,
            "score_floor": manifest["settings"]["conf"],
            "device": manifest["device"],
        },
        "evaluator": {"package": "pycocotools", "version": evaluator_version, "iou_type": "bbox"},
        "coverage": prepared["coverage"],
        "metrics": metrics,
        "operating_point": point,
        "flagged_images_present": [
            item for item in protocol["flagged_images"] if item["file_name"] in names
        ],
        "limitations": [
            "an empty detection list is not a benign or safe result",
            "annotation-empty images are not verified benign images",
            *protocol["limitations"],
            *manifest["limitations"],
        ],
    }


def validate_report(report: Any) -> None:
    """Check report structure and that every metric is finite or null."""
    _object(report, REPORT_FIELDS, "report")
    if report["schema_version"] != SCHEMA_VERSION:
        raise ValueError(f"report schema_version must be {SCHEMA_VERSION!r}")
    if report["evidence"] not in ("draft-protocol", "approved-protocol"):
        raise ValueError("report evidence must be draft-protocol or approved-protocol")
    if not isinstance(report["metrics"], dict) or not report["metrics"]:
        raise ValueError("metrics must be a nonempty object")
    for name, value in report["metrics"].items():
        if value is not None and (type(value) is not float or not math.isfinite(value)):
            raise ValueError(f"metric {name} must be a finite float or null")
    if not isinstance(report["limitations"], list) or not report["limitations"]:
        raise ValueError("a report must carry its limitations")


def dumps_report(report: dict[str, Any]) -> str:
    """Validate and serialize a report; NaN and infinity are rejected."""
    validate_report(report)
    return json.dumps(report, allow_nan=False, sort_keys=True, indent=2)


__all__ = [
    "build_report",
    "check_ground_truth",
    "check_protocol",
    "coco_detections",
    "dumps_report",
    "iou_xywh",
    "matched_pair_differences",
    "operating_point",
    "validate_protocol",
    "validate_report",
    "xyxy_to_xywh",
]
