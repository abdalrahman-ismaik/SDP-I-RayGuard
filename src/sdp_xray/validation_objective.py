"""Validation objective for T41 tuning: one checkpoint's COCO AP on declared validation images.

This is the T42 side of the interface that T41 (``sdp_xray.tuning``) calls. It never touches
the published test split: the ground truth must contain exactly the request's validation
image IDs, and its file hash must equal the request's ``annotation_sha256``.

Request (built by ``tuning.validation_request``), every field required:
  checkpoint_sha256, completed_epoch, task (catalog task identity), partition_sha256,
  validation_ids, annotation_sha256, objective
Result (checked by ``tuning.validate_objective_result``):
  status "ok", the same identities, evaluated_image_ids, value = AP@[.50:.95] on a 0-1 scale

Coordinates: detections are COCO original-pixel ``[x, y, width, height]``. Categories are
dataset COCO IDs from the task's ``source_category_map``, never model output indices.
A failure raises ValueError; it is never reported as zero AP.
"""

import math
from copy import deepcopy
from typing import Any

from sdp_xray.coco_metrics import coco_bbox_metrics, evaluator_version
from sdp_xray.common.run_manifest import _sha256
from sdp_xray.evaluation import check_ground_truth
from sdp_xray.model_catalog import MODELS

OBJECTIVE_NAME = "coco_bbox_AP_50_95"
EVALUATOR_ID = "sdp_xray.validation_objective/pycocotools-bbox-1"
# Copy these into the T41 config's objective.settings. A request with other settings is refused.
OBJECTIVE_SETTINGS = {
    "package": "pycocotools",
    "version": "2.0.11",
    "iou_type": "bbox",
    "parameters": "COCOeval defaults; AP over IoU 0.50:0.95, maxDets 100",
    "coordinates": "original-pixel xywh",
    "categories": "dataset COCO IDs from source_category_map",
}
REQUEST_FIELDS = {"checkpoint_sha256", "completed_epoch", "task", "partition_sha256",
                  "validation_ids", "annotation_sha256", "objective"}


def objective() -> dict[str, Any]:
    """The objective block T41 should freeze in its study config."""
    return {"name": OBJECTIVE_NAME, "direction": "maximize", "scale": "fraction",
            "evaluator_id": EVALUATOR_ID, "settings": deepcopy(OBJECTIVE_SETTINGS)}


def _catalog_task(task: Any) -> dict[str, Any]:
    """Confirm the request's task identity is one inspected catalog pairing."""
    for spec in MODELS.values():
        expected = {"task": spec.task, "kind": spec.kind, "class_map_sha256": spec.class_map_sha256,
                    "model_names": {str(k): v for k, v in spec.names.items()},
                    "source_category_map": spec.source_category_map}
        if task == expected:
            return expected
    raise ValueError("request task identity is not an inspected catalog task")


def check_request(request: Any) -> None:
    if not isinstance(request, dict) or set(request) != REQUEST_FIELDS:
        raise ValueError(f"validation request must have exactly {sorted(REQUEST_FIELDS)}")
    _sha256(request["checkpoint_sha256"], "checkpoint_sha256")
    _sha256(request["partition_sha256"], "partition_sha256")
    _sha256(request["annotation_sha256"], "annotation_sha256")
    if type(request["completed_epoch"]) is not int or request["completed_epoch"] < 0:
        raise ValueError("completed_epoch must be a nonnegative integer")
    ids = request["validation_ids"]
    if (not isinstance(ids, list) or not ids or any(type(i) is not int for i in ids)
            or len(set(ids)) != len(ids)):
        raise ValueError("validation_ids must be a nonempty list of unique integers")
    if request["objective"] != objective():
        raise ValueError("request objective differs from this evaluator's frozen objective")
    _catalog_task(request["task"])


def evaluate_validation(
    request: dict[str, Any],
    ground_truth: dict[str, Any],
    ground_truth_sha256: str,
    checkpoint_sha256: str,
    detections: list[dict[str, Any]],
) -> dict[str, Any]:
    """Score one checkpoint's validation detections and return the T41 result object.

    ``checkpoint_sha256`` is the hash of the weights that produced ``detections``; it must be
    the requested checkpoint. ``ground_truth`` is the validation-only COCO document whose
    file hash is ``ground_truth_sha256``.
    """
    check_request(request)
    if checkpoint_sha256 != request["checkpoint_sha256"]:
        raise ValueError("detections come from a different checkpoint than requested")
    if ground_truth_sha256 != request["annotation_sha256"]:
        raise ValueError("validation annotation file hash differs from the request")
    if evaluator_version() != OBJECTIVE_SETTINGS["version"]:
        raise ValueError("installed pycocotools version differs from the frozen objective")

    category_map = request["task"]["source_category_map"]
    index = check_ground_truth(ground_truth, category_map)
    image_ids = sorted(index["images_by_id"])
    if image_ids != sorted(request["validation_ids"]):
        raise ValueError("ground truth must contain exactly the requested validation images")
    if index["summary"]["annotations"] == 0:
        raise ValueError("validation images have no boxes; AP is undefined, not zero")

    wanted, categories = set(image_ids), {int(key) for key in category_map}
    for detection in detections:
        if not isinstance(detection, dict) or set(detection) != {"image_id", "category_id",
                                                                 "bbox", "score"}:
            raise ValueError("each detection needs exactly image_id, category_id, bbox, score")
        if detection["image_id"] not in wanted:
            raise ValueError("detection on an image outside the validation set")
        if detection["category_id"] not in categories:
            raise ValueError("detection category is not in the task's source_category_map")
        box, score = detection["bbox"], detection["score"]
        if (not isinstance(box, list) or len(box) != 4
                or any(type(v) not in (int, float) or not math.isfinite(v) for v in box)
                or box[2] <= 0 or box[3] <= 0):
            raise ValueError("detection bbox must be finite [x, y, width, height] with positive size")
        if type(score) not in (int, float) or not 0 <= score <= 1:
            raise ValueError("detection score must be between 0 and 1")

    value = coco_bbox_metrics(ground_truth, detections, image_ids)["AP@[.50:.95]"]
    if value is None:
        raise ValueError("COCOeval returned an undefined AP; this is a failure, not zero")
    return {
        "status": "ok",
        "checkpoint_sha256": request["checkpoint_sha256"],
        "completed_epoch": request["completed_epoch"],
        "task": deepcopy(request["task"]),
        "partition_sha256": request["partition_sha256"],
        "annotation_sha256": request["annotation_sha256"],
        "objective": deepcopy(request["objective"]),
        "evaluated_image_ids": image_ids,
        "value": value,
    }


__all__ = ["EVALUATOR_ID", "OBJECTIVE_NAME", "OBJECTIVE_SETTINGS", "check_request",
           "evaluate_validation", "objective"]
