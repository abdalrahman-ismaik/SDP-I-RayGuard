"""Synthetic checkpoint/box bridge tests. AP is supplied by a fake, never computed here."""

import hashlib
import json
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace

import pytest
from test_training_backend import bundle_case
from test_tuning import FakeEvaluator

from sdp_xray.training_research import example_research_config, task_identity
from sdp_xray.training_validation import (
    ValidationAdapter,
    check_prediction_settings,
    objective_spec,
    outside_clipping_events,
)
from sdp_xray.tuning import make_study_definition, validation_request


class TensorStandIn:
    def __init__(self, values):
        self.values = values

    def cpu(self):
        return self

    def tolist(self):
        return deepcopy(self.values)


def validation_case(tmp_path, task="generic", change=None):
    config, _, sources, partition, checkpoint = bundle_case(tmp_path, task)
    annotation, images = sources["validation"]
    truth = json.loads(annotation.read_text())
    first = truth["images"][0]
    category = int(next(iter(task_identity(task)["source_category_map"])))
    truth["annotations"] = [{"id": 0, "image_id": first["id"], "category_id": category,
                             "bbox": [1, 2, 3, 4], "area": 12, "iscrowd": 0}]
    annotation.write_text(json.dumps(truth))
    config["sources"]["validation"]["annotation_sha256"] = hashlib.sha256(annotation.read_bytes()).hexdigest()
    config["objective"] = objective_spec()
    config["validation_prediction"] = {"conf": 0.001, "max_det": 100}  # Invented fixture settings.
    definition = make_study_definition(config, partition, config["sources"]["validation"]["annotation_sha256"])
    context = {"definition": definition, "annotation_file": str(annotation), "image_root": str(images)}
    calls, evaluated = [], []
    def predictor_factory(weights, settings):
        assert weights == checkpoint and settings == config["validation_prediction"]
        def predictor(source, stream):
            calls.append(source)
            populated = Path(source).name == first["file_name"]
            result = SimpleNamespace(path=source, orig_shape=(8, 8),
                                     names={int(k): v for k, v in task_identity(task)["model_names"].items()},
                                     boxes=SimpleNamespace(xyxy=TensorStandIn([[1, 2, 4, 6]] if populated else []),
                                                           cls=TensorStandIn([0] if populated else []),
                                                           conf=TensorStandIn([0.9] if populated else [])))
            if change:
                change(result)
            return [result]
        return predictor
    def metric(request, document, annotation_hash, checkpoint_hash, detections):
        evaluated.append(deepcopy(detections))
        assert document == truth and annotation_hash == request["annotation_sha256"]
        assert checkpoint_hash == request["checkpoint_sha256"]
        return FakeEvaluator().evaluate(request)
    adapter = ValidationAdapter(context, predictor_factory, metric, synthetic=True)
    request = validation_request(definition, hashlib.sha256(checkpoint.read_bytes()).hexdigest(), 1)
    return adapter, request, checkpoint, calls, evaluated, context


@pytest.mark.parametrize("task,category", [("generic", 0), ("specific", 1)])
def test_bridge_preserves_category_namespace_empty_images_and_inputs(tmp_path, task, category):
    adapter, request, checkpoint, calls, evaluated, context = validation_case(tmp_path, task)
    originals = {p: p.read_bytes() for p in (tmp_path / "originals").iterdir()}
    response = adapter.evaluate_checkpoint(request, checkpoint)
    assert response["evaluated_image_ids"] == request["validation_ids"]
    assert len(calls) == len(request["validation_ids"])
    assert evaluated == [[{"image_id": context["definition"]["validation_ids"][0],
                           "category_id": category, "bbox": [1, 2, 3, 4], "score": 0.9}]]
    assert originals == {p: p.read_bytes() for p in (tmp_path / "originals").iterdir()}


@pytest.mark.parametrize("kind", ["class_map", "geometry", "fractional_class", "shape", "path", "score"])
def test_invalid_predictions_fail_before_metric(tmp_path, kind):
    def change(result):
        if kind == "class_map":
            result.names = {0: "wrong"}
        elif kind == "shape":
            result.orig_shape = (7, 8)
        elif kind == "path":
            result.path = "wrong.png"
        else:
            result.boxes.xyxy = TensorStandIn([[1, 1, 0, 2]] if kind == "geometry" else [[1, 1, 2, 2]])
            result.boxes.cls = TensorStandIn([0.5] if kind == "fractional_class" else [0])
            result.boxes.conf = TensorStandIn([float("nan")] if kind == "score" else [0.9])
    adapter, request, checkpoint, _, evaluated, _ = validation_case(tmp_path, change=change)
    with pytest.raises(ValueError):
        adapter.evaluate_checkpoint(request, checkpoint)
    assert not evaluated


@pytest.mark.parametrize("kind", ["checkpoint", "annotation", "partition", "objective"])
def test_changed_validation_identity_blocks_before_prediction(tmp_path, kind):
    adapter, request, checkpoint, calls, _, context = validation_case(tmp_path)
    if kind == "checkpoint":
        checkpoint.write_bytes(b"changed synthetic bytes")
    elif kind == "annotation":
        Path(context["annotation_file"]).write_text("{}")
    elif kind == "partition":
        request["partition_sha256"] = "0" * 64
    else:
        request["objective"]["scale"] = "percent"
    with pytest.raises(ValueError):
        adapter.evaluate_checkpoint(request, checkpoint)
    assert not calls


def test_empty_predictions_are_valid_complete_coverage_not_missing_images(tmp_path):
    def empty(result):
        result.boxes = SimpleNamespace(xyxy=TensorStandIn([]), cls=TensorStandIn([]), conf=TensorStandIn([]))
    adapter, request, checkpoint, calls, evaluated, _ = validation_case(tmp_path, change=empty)
    adapter.evaluate_checkpoint(request, checkpoint)
    assert evaluated == [[]] and len(calls) == len(request["validation_ids"])


def test_example_uses_ali_objective_and_declared_prediction_controls_without_approval():
    config = example_research_config()
    assert config["objective"] == objective_spec()
    assert config["objective"]["settings"]["version"] == "2.0.11"
    assert config["validation_prediction"] == {"conf": 0.001, "max_det": 300}
    check_prediction_settings(config["validation_prediction"])
    assert all(value is None for value in config["approvals"].values())


@pytest.mark.parametrize("settings", [{"conf": float("nan"), "max_det": 100},
                                      {"conf": 0.1, "max_det": 10}, {"conf": True, "max_det": 100}])
def test_invalid_prediction_settings_block(settings):
    with pytest.raises(ValueError):
        check_prediction_settings(settings)


@pytest.mark.parametrize("raw,clipped", [
    ([-4, 2, -1, 5], [0, 2, 0, 5]),
    ([2, -4, 5, -1], [2, 0, 5, 0]),
    ([11, 2, 14, 5], [10, 2, 10, 5]),
    ([2, 11, 5, 14], [2, 10, 5, 10]),
    ([-2, -2, 0, 0], [0, 0, 0, 0]),
])
def test_wholly_outside_predictions_preserve_original_geometry_and_count(raw, clipped):
    before = [[-1, 2, 3, 5], raw, [1, 1, 2, 2]]
    after = [[0, 2, 3, 5], clipped, [1, 1, 2, 2]]
    original = deepcopy((before, after))
    assert outside_clipping_events(before, after, (10, 10, 3)) == [
        {"prediction_index": 1, "original_xyxy": raw, "clipped_xyxy": clipped, "image_shape": [10, 10]}]
    assert (before, after) == original


@pytest.mark.parametrize("raw", [[1, 1, 0, 2], [1, 1, 1, 2],
                                 [1, float("nan"), 2, 3], [1, 1, 2, 2]])
def test_clipping_does_not_repair_invalid_raw_or_inside_geometry(raw):
    with pytest.raises(ValueError, match="valid wholly outside"):
        outside_clipping_events([raw], [[0, 0, 0, 0]], (10, 10))


def test_wholly_outside_positive_boxes_reach_evaluator_as_detections(tmp_path):
    def outside(result):
        result.boxes.xyxy = TensorStandIn([[2, -4, 5, -1]])
        result.boxes.cls = TensorStandIn([0])
        result.boxes.conf = TensorStandIn([0.002])
        result.rayguard_geometry_events = outside_clipping_events(
            [[2, -4, 5, -1]], [[2, 0, 5, 0]], (8, 8))
    adapter, request, checkpoint, calls, evaluated, _ = validation_case(tmp_path, change=outside)
    adapter.evaluate_checkpoint(request, checkpoint)
    assert len(evaluated[0]) == len(calls) == len(adapter.geometry_events)
    assert all(row["bbox"] == [2, -4, 3, 3] and row["score"] == 0.002 for row in evaluated[0])


@pytest.mark.parametrize("task", ["generic", "specific"])
def test_installed_ali_factory_uses_actual_interface_with_fake_predictor_and_metric(tmp_path, monkeypatch, task):
    from sdp_xray import coco_metrics, evaluation, training_validation, validation_objective

    adapter, request, checkpoint, calls, _, context = validation_case(tmp_path, task)
    context["qualified_sources"] = [{"path": module.__file__,
                                      "sha256": hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()}
                                     for module in (coco_metrics, evaluation, validation_objective)]
    monkeypatch.setattr(training_validation, "_predictor_factory", adapter.predictor_factory)
    monkeypatch.setattr(validation_objective, "evaluator_version", lambda: "2.0.11")
    metric_calls = []
    def metric(truth, detections, ids):
        metric_calls.append((truth, detections, ids))
        return {"AP@[.50:.95]": 0.42}  # Explicit fake value; no COCO execution here.
    monkeypatch.setattr(validation_objective, "coco_bbox_metrics", metric)
    installed = training_validation.create(context)
    assert installed.evaluate_checkpoint(request, checkpoint)["value"] == 0.42
    assert len(calls) == len(request["validation_ids"]) and len(metric_calls) == 1
    context["qualified_sources"][0]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="reviewed source"):
        training_validation.create(context)
