"""T41 checkpoint-to-detections bridge; all AP computation belongs to Ali/T42.

The frozen objective mirrors validation_objective.objective() at PR18 commit
6dfa7d6f69ae40aec2885c6d5116a3eb776c6ec1. The live factory checks equality.
No optional package, checkpoint or image is accessed at module import.
"""

import importlib.util
import json
import math
import os
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

from sdp_xray.data.audit import _image_path
from sdp_xray.training import _sha256
from sdp_xray.training_checkpoint import checkpoint_loading
from sdp_xray.validation_objective import objective


def objective_spec():
    """Compatibility alias; the objective now comes directly from Ali's module."""
    return objective()


def check_prediction_settings(settings):
    if (not isinstance(settings, dict) or set(settings) != {"conf", "max_det"}
            or type(settings["conf"]) not in (int, float) or not math.isfinite(settings["conf"])
            or not 0 <= settings["conf"] <= 1
            or type(settings["max_det"]) is not int or settings["max_det"] < 100):
        raise ValueError("freeze validation confidence and at least 100 retained detections explicitly")


def outside_clipping_events(before, clipped, shape):
    """Identify positive original-pixel boxes collapsed by image-boundary clipping.

    Keep these wholly outside detections as unmatched predictions. Do not repair
    raw invalid geometry, alter partially overlapping boxes, or drop detections.
    Coordinates are original-image pixel xyxy, before/after the fork's clipping.
    """
    if len(before) != len(clipped):
        raise ValueError("clipping changed the prediction count")
    events = []
    height, width = shape[:2]
    for index, (raw, bounded) in enumerate(zip(before, clipped, strict=True)):
        if bounded[2] > bounded[0] and bounded[3] > bounded[1]:
            continue
        if (any(not math.isfinite(v) for v in [*raw, *bounded])
                or raw[2] <= raw[0] or raw[3] <= raw[1]
                or not (raw[2] <= 0 or raw[3] <= 0 or raw[0] >= width or raw[1] >= height)):
            raise ValueError("collapsed prediction was not a valid wholly outside box")
        events.append({"prediction_index": index, "original_xyxy": list(raw),
                       "clipped_xyxy": list(bounded), "image_shape": list(shape[:2])})
    return events


class ValidationAdapter:
    """Inject predictor/metric functions for CPU fixtures; never implement COCO AP."""

    def __init__(self, context, predictor_factory, evaluate, *, synthetic=False):
        self.context, self.predictor_factory, self.evaluate = deepcopy(context), predictor_factory, evaluate
        self.synthetic = synthetic
        check_prediction_settings(self.context["definition"]["configuration"].get("validation_prediction"))
        if self.context["definition"]["objective"] != objective_spec():
            raise ValueError("objective differs from Ali's frozen interface")

    def evaluate_checkpoint(self, request, checkpoint):
        from sdp_xray.tuning import validate_objective_result, validation_request

        definition = self.context["definition"]
        checkpoint = Path(checkpoint)
        if request != validation_request(definition, _sha256(checkpoint), request["completed_epoch"]):
            raise ValueError("checkpoint/task/partition/objective differs from validation context")
        annotation = Path(self.context["annotation_file"])
        if _sha256(annotation) != request["annotation_sha256"]:
            raise ValueError("validation annotation bytes changed")
        truth = json.loads(annotation.read_text(encoding="utf-8-sig"))
        if sorted(row["id"] for row in truth["images"]) != sorted(request["validation_ids"]):
            raise ValueError("validation membership differs")
        if not truth["annotations"]:
            raise ValueError("validation AP is undefined without boxes")
        settings = definition["configuration"]["validation_prediction"]
        predictor = self.predictor_factory(checkpoint, settings)
        names = request["task"]["model_names"]
        source_ids = {name: int(identifier) for identifier, name in request["task"]["source_category_map"].items()}
        inventory = {row["id"]: row["sha256"] for row in definition["partition"]["train_inventory"]}
        detections, visited = [], []
        self.geometry_events = []
        for row in sorted(truth["images"], key=lambda row: row["id"]):
            path = _image_path(Path(self.context["image_root"]), row["file_name"])
            if _sha256(path) != inventory[row["id"]]:
                raise ValueError("validation image bytes changed")
            results = predictor(source=str(path), stream=False)
            if len(results) != 1:
                raise ValueError("batch-one predictor must return every requested image exactly once")
            result = results[0]
            actual_names = {str(k): v for k, v in result.names.items()}
            if (actual_names != names or tuple(result.orig_shape) != (row["height"], row["width"])
                    or Path(result.path).resolve() != path.resolve() or result.boxes is None):
                raise ValueError("prediction image, shape or model class map differs")
            boxes = result.boxes.xyxy.cpu().tolist()
            classes = result.boxes.cls.cpu().tolist()
            scores = result.boxes.conf.cpu().tolist()
            if len(boxes) != len(classes) or len(boxes) != len(scores):
                raise ValueError("incomplete prediction rows")
            self.geometry_events.extend({"image_id": row["id"], "file_name": row["file_name"], **event}
                                        for event in getattr(result, "rayguard_geometry_events", []))
            for box, category, score in zip(boxes, classes, scores, strict=True):
                if (type(category) not in (int, float) or not math.isfinite(category)
                        or category != int(category) or str(int(category)) not in names
                        or len(box) != 4 or any(type(v) not in (int, float) or not math.isfinite(v) for v in box)
                        or box[2] <= box[0] or box[3] <= box[1]
                        or type(score) not in (int, float) or not math.isfinite(score) or not 0 <= score <= 1):
                    raise ValueError("invalid detection geometry/class/score")
                detections.append({"image_id": row["id"], "category_id": source_ids[names[str(int(category))]],
                                   "bbox": [box[0], box[1], box[2] - box[0], box[3] - box[1]], "score": score})
            if _sha256(path) != inventory[row["id"]]:
                raise ValueError("validation image changed during prediction")
            visited.append(row["id"])
        if sorted(visited) != sorted(request["validation_ids"]) or _sha256(checkpoint) != request["checkpoint_sha256"]:
            raise ValueError("incomplete validation or changed checkpoint")
        if _sha256(annotation) != request["annotation_sha256"]:
            raise ValueError("validation annotation changed during prediction")
        result = self.evaluate(deepcopy(request), truth, request["annotation_sha256"],
                               request["checkpoint_sha256"], detections)
        validate_objective_result(request, result)
        return result


def _predictor_factory(checkpoint, settings):
    """Pinned upstream batch-one predictor; invoked only inside the reviewed workflow."""
    import torch
    from ultralytics.models.yolov10.predict import YOLOv10DetectionPredictor
    from ultralytics.utils import ops

    class PreserveOutsidePredictor(YOLOv10DetectionPredictor):
        def postprocess(self, preds, img, orig_imgs):
            events = []
            original_clip = ops.clip_boxes

            def clip_and_preserve(boxes, shape):
                before = boxes.clone()
                result = original_clip(boxes, shape)
                found = outside_clipping_events(before.cpu().tolist(), boxes.cpu().tolist(), shape)
                for event in found:
                    boxes[event["prediction_index"]] = before[event["prediction_index"]]
                events.extend(found)
                return result

            with patch.object(ops, "clip_boxes", clip_and_preserve):
                results = super().postprocess(preds, img, orig_imgs)
            if len(results) != 1:
                raise ValueError("outside-prediction accounting requires batch one")
            results[0].rayguard_geometry_events = events
            return results

    mask = os.environ.get("CUDA_VISIBLE_DEVICES")
    if not mask or not torch.cuda.is_available() or torch.cuda.device_count() != 1:
        raise ValueError("one allocated visible GPU required for validation")
    arguments = {**settings, "model": str(checkpoint.resolve()), "task": "detect", "mode": "predict",
                 "imgsz": 640, "batch": 1, "device": "0", "half": False, "augment": False,
                 "classes": None, "save": False, "save_txt": False, "save_conf": False,
                 "save_crop": False, "show": False, "verbose": False,
                 "project": str(checkpoint.parent), "name": "validation", "exist_ok": False}
    predictor = PreserveOutsidePredictor(overrides=arguments)
    if any(getattr(predictor.args, key, None) != value for key, value in arguments.items()):
        raise ValueError("upstream changed validation controls")
    with checkpoint_loading({checkpoint.resolve(): _sha256(checkpoint)}), \
            patch("ultralytics.engine.predictor.select_device", lambda *a, **k: torch.device("cuda:0")):
        predictor.setup_model(model=str(checkpoint.resolve()), verbose=False)
    if os.environ.get("CUDA_VISIBLE_DEVICES") != mask or predictor.model.fp16:
        raise ValueError("validation changed allocated mask or FP32 precision")
    return predictor


def create(context):
    """Reviewed factory entry; Ali's implementation must already be integrated/qualified."""
    qualified = {Path(row["path"]).resolve(): row["sha256"] for row in context["qualified_sources"]}
    for name in ("validation_objective", "evaluation", "coco_metrics"):
        spec = importlib.util.find_spec(f"sdp_xray.{name}")
        if spec is None or not spec.origin:
            raise ValueError("Ali's evaluation modules are not integrated in this environment")
        path = Path(spec.origin).resolve()
        if path not in qualified or _sha256(path) != qualified[path]:
            raise ValueError("installed evaluator source is not the reviewed source")
    from sdp_xray.validation_objective import evaluate_validation, objective

    if objective() != objective_spec():
        raise ValueError("Ali's installed objective differs from the frozen configuration")
    return ValidationAdapter(context, _predictor_factory, evaluate_validation)
