"""Tiny generated images, text checkpoint stand-ins and a fake upstream trainer only."""

import hashlib
import json
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest
import test_training as legacy
from PIL import Image
from test_training_research import (
    init_receipt,
    inventory,
    partition_policy,
    research_case,
)
from test_tuning import FakeEvaluator, FakeSampler

from sdp_xray.training_backend import (
    CheckpointValidationAdapter,
    YoloTrainerAdapter,
    check_training_bundle,
    live_trainer_class,
    prepare_training_bundle,
    training_arguments,
)
from sdp_xray.training_partition import fingerprint, make_partition, subset_coco
from sdp_xray.training_research import (
    TASKS,
    audit_findings,
    inspect_partition_sources,
    research_candidate_manifest,
    research_plan,
    task_identity,
    validate_initialization,
)
from sdp_xray.tuning import make_study_definition, run_synthetic_study


def bundle_case(tmp_path, task="generic"):
    inputs = tmp_path / "originals"
    inputs.mkdir()
    train, test = inventory()
    for split, rows in (("train", train), ("test", test)):
        for row in rows:
            path = inputs / f"{split}-{row['id']}.png"
            Image.new("RGB", (8, 8), (row["id"], 5, 9)).save(path)
            row["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    partition = make_partition(train, test, partition_policy(train, test))
    categories = [{"id": int(k), "name": v}
                  for k, v in task_identity(task)["source_category_map"].items()]
    document = {"images": [{"id": row["id"], "file_name": f"train-{row['id']}.png",
                             "width": 8, "height": 8} for row in train],
                "categories": categories, "annotations": [
                    {"id": 0, "image_id": 0, "category_id": categories[0]["id"],
                     "bbox": [1, 1, 2, 2], "iscrowd": 0}]}
    sources = {}
    for split in ("fit", "validation"):
        annotation = inputs / f"{split}.json"
        annotation.write_text(json.dumps(subset_coco(document, partition, split, TASKS[task])))
        sources["train" if split == "fit" else split] = (annotation, inputs)
    test_path = inputs / "test.json"
    test_path.write_text(json.dumps({"images": [
        {"id": row["id"], "file_name": f"test-{row['id']}.png", "width": 8, "height": 8}
        for row in test], "categories": categories, "annotations": []}))
    sources["test"] = (test_path, inputs)
    config, _ = research_case(task)
    evidence = inspect_partition_sources(sources, task, partition)
    config.update(partition_sha256=partition["membership_sha256"], sources=evidence["sources"])
    config["generic_completion"]["partition_sha256"] = partition["membership_sha256"]
    config["data_policy"]["audit_findings_sha256"] = fingerprint(audit_findings(evidence))
    weights = tmp_path / "synthetic.pt"
    weights.write_bytes(b"synthetic initialization bytes")
    return config, evidence, sources, partition, weights


@pytest.mark.parametrize("task", ["generic", "specific"])
@pytest.mark.parametrize("seed", [17, 29, 43])
def test_explicit_repeat_seed_receipts_and_search_default(task, seed):
    receipt = init_receipt(task)
    receipt["seed"] = seed
    before = deepcopy(receipt)
    validate_initialization(receipt, task, expected_seed=seed)
    assert receipt == before
    if seed != 17:
        with pytest.raises(ValueError):
            validate_initialization(receipt, task)
        config, evidence = research_case(task)
        config["initialization"] = receipt
        assert "initialization:verified_general_pretraining_receipt_required" in research_plan(
            config, evidence)["blockers"]


@pytest.mark.parametrize("seed", [True, "29", 0, 18, None])
def test_unplanned_or_noninteger_repeat_seed_is_rejected(seed):
    with pytest.raises(ValueError):
        validate_initialization(init_receipt(), "generic", expected_seed=seed)


def test_repeat_candidate_keeps_common_parent_without_training_fields():
    original = legacy.CandidateManifestTests()
    original.setUp()
    try:
        for seed in (29, 43):
            receipt = init_receipt()
            receipt["seed"] = seed
            record = research_candidate_manifest(
                "generic", receipt, original.checkpoint, original.run, original.results,
                model_id=original.spec.id, expected_seed=seed)
            assert record["model"]["parent_checkpoint_sha256"] == receipt["checkpoint_sha256"]
            assert record["model"]["checkpoint_sha256"] == original.digest
            assert record["requested_device"] == "cpu" and record["role"] == "candidate"
            assert "seed" not in record and "epochs" not in record
    finally:
        original.doCleanups()


@pytest.mark.parametrize("task", ["generic", "specific"])
def test_bundle_preserves_originals_empty_images_category_zero_and_test(tmp_path, task):
    config, evidence, sources, partition, _ = bundle_case(tmp_path, task)
    original = {p: p.read_bytes() for p in (tmp_path / "originals").iterdir()}
    output = prepare_training_bundle(config, sources, partition, tmp_path / "bundle")
    receipt = check_training_bundle(output, config)
    assert receipt["sources"] == evidence["sources"]
    assert original == {p: p.read_bytes() for p in (tmp_path / "originals").iterdir()}
    labels = list((output / "labels").rglob("*.txt"))
    assert len(labels) == 10 and sum(bool(p.read_text()) for p in labels) == 1
    assert next(p.read_text() for p in labels if p.read_text()).startswith("0 ")
    assert len(list((output / "images").rglob("*.png"))) == 10
    data = json.loads((output / "data.yaml").read_text())
    assert "test" not in data and "download" not in data
    assert data["nc"] == (1 if task == "generic" else 5)


@pytest.mark.parametrize("task", ["generic", "specific"])
def test_bundle_precedes_training_qualification_without_approving_execution(tmp_path, task):
    config, _, sources, partition, _ = bundle_case(tmp_path, task)
    config.update(initialization=None, batch=None, requested_device=None,
                  owner=None, output_directory=None, generic_completion=None)
    config["environment"] = None
    for name in ("compute_scope", "faisal_provenance_interface", "ali_validation_interface",
                 "common_initialization_comparison"):
        config["approvals"][name] = None
    original = deepcopy(config)
    output = prepare_training_bundle(config, sources, partition, tmp_path / "before-pilot")
    check_training_bundle(output, config)
    assert config == original
    plan = research_plan(config, inspect_partition_sources(sources, task, partition))
    assert "environment:allocated_train_save_reload_and_storage_unqualified" in plan["blockers"]
    assert "initialization:verified_general_pretraining_receipt_required" in plan["blockers"]
    assert plan["execution"]["training_started"] is False


@pytest.mark.parametrize("approval", ["data_policy", "source_identity", "validation_design"])
def test_bundle_still_requires_each_data_review_before_pilot(tmp_path, approval):
    config, _, sources, partition, _ = bundle_case(tmp_path)
    config["environment"] = None
    config["approvals"][approval] = None
    output = tmp_path / "unapproved"
    with pytest.raises(ValueError, match="reviewed source/partition"):
        prepare_training_bundle(config, sources, partition, output)
    assert not output.exists()


def test_bundle_policy_geometry_and_output_fail_closed(tmp_path):
    config, _, sources, partition, _ = bundle_case(tmp_path)
    output = tmp_path / "bundle"
    broken = deepcopy(config)
    broken["data_policy"]["review"] = None
    with pytest.raises(ValueError, match="reviewed"):
        prepare_training_bundle(broken, sources, partition, output)
    assert not output.exists()
    with pytest.raises(ValueError, match="separate"):
        prepare_training_bundle(config, sources, partition, tmp_path / "originals" / "nested")
    output.mkdir()
    with pytest.raises(FileExistsError):
        prepare_training_bundle(config, sources, partition, output)
    annotation = sources["train" if 0 in partition["fit_ids"] else "validation"][0]
    document = json.loads(annotation.read_text())
    document["annotations"][0]["bbox"] = [-1, 0, 4, 2]
    annotation.write_text(json.dumps(document))
    with pytest.raises(ValueError, match="geometry"):
        prepare_training_bundle(config, sources, partition, tmp_path / "invalid")
    assert not (tmp_path / "invalid").exists()


@pytest.mark.parametrize("change", ["test", "empty", "class_map", "extra_image", "labels"])
def test_bundle_rejects_fallback_missing_validation_and_changed_files(tmp_path, change):
    config, _, sources, partition, _ = bundle_case(tmp_path)
    root = prepare_training_bundle(config, sources, partition, tmp_path / "bundle")
    data = json.loads((root / "data.yaml").read_text())
    if change in ("test", "empty", "class_map"):
        if change == "test":
            data["test"] = data.pop("val")
        elif change == "empty":
            data["val"] = ""
        else:
            data["names"] = ["wrong class"]
        (root / "data.yaml").write_text(json.dumps(data))
        # Even updating the untrusted receipt cannot make a test fallback acceptable.
        receipt = json.loads((root / "bundle.json").read_text())
        receipt["files"]["data.yaml"] = hashlib.sha256((root / "data.yaml").read_bytes()).hexdigest()
        receipt["sha256"] = fingerprint({k: v for k, v in receipt.items() if k != "sha256"})
        (root / "bundle.json").write_text(json.dumps(receipt))
    elif change == "extra_image":
        (root / "images" / "validation" / "extra.png").write_bytes(b"not an image")
    else:
        next((root / "labels").rglob("*.txt")).write_text("changed")
    with pytest.raises(ValueError):
        check_training_bundle(root, config)


class FakeUpstreamTrainer:
    synthetic = True
    duplicate = False
    saved = []

    def __init__(self, overrides):
        self.args = SimpleNamespace(**overrides)
        self.save_dir = Path(overrides["project"]) / overrides["name"]
        (self.save_dir / "weights").mkdir(parents=True)
        self.last = self.save_dir / "weights" / "last.pt"
        self.callbacks = {}

    def add_callback(self, event, callback):
        self.callbacks.setdefault(event, []).append(callback)

    def train(self):
        for self.epoch in range(self.args.epochs):
            self.last.write_text(f"synthetic seed {self.args.seed}, epoch {self.epoch + 1}")
            self.saved.append(self.epoch + 1)
            for callback in self.callbacks.get("on_model_save", []):
                callback(self)
                if self.duplicate:
                    callback(self)
        self.last.write_text("synthetic upstream final rewrite")
        for callback in self.callbacks.get("on_fit_epoch_end", []):
            callback(self)


class FakeBoundEvaluator:
    synthetic = True

    def __init__(self):
        self.paths = []

    def evaluate_checkpoint(self, request, checkpoint):
        self.paths.append(checkpoint)
        assert checkpoint.read_text().endswith(f"epoch {request['completed_epoch']}")
        result = FakeEvaluator().evaluate(request)
        result["value"] = 0.8 if request["completed_epoch"] == 2 else 0.2
        return result


def prepared_case(tmp_path):
    config, evidence, sources, partition, weights = bundle_case(tmp_path)
    bundle = prepare_training_bundle(config, sources, partition, tmp_path / "bundle")
    definition = make_study_definition(config, partition, config["sources"]["validation"]["annotation_sha256"])
    return config, evidence, weights, bundle, definition


def test_callback_training_bridge_selects_ap_and_preserves_completed_checkpoints(tmp_path):
    _, _, weights, bundle, definition = prepared_case(tmp_path)
    sampler, evaluator = FakeSampler(), FakeBoundEvaluator()
    class DuplicateTrainer(FakeUpstreamTrainer):
        duplicate = True
    trainer = YoloTrainerAdapter(DuplicateTrainer, weights, bundle)
    exported = run_synthetic_study(definition, tmp_path / "study", sampler, trainer,
                                    CheckpointValidationAdapter(evaluator),
                                    stop_requested=lambda: len(sampler.tells) == 1)
    trial = exported["trials"][0]
    assert trial["status"] == "complete" and trial["value"] == 0.8
    assert len(trial["reports"]) == len(evaluator.paths) == 30
    assert trial["best_checkpoint"]["path"].endswith("epoch-002.pt")
    assert exported["training_started"] is False
    assert evaluator.paths[1].read_text().endswith("epoch 2")
    args_path = next((tmp_path / "study").rglob("effective-arguments.json"))
    args = json.loads(args_path.read_text())
    assert args["model"] == str(weights.resolve()) and args["amp"] is False and args["seed"] == 17
    assert args["resume"] is False and args["patience"] == 0 and args["batch"] == 1


def test_callback_pruning_and_interrupt_stop_before_another_epoch(tmp_path):
    _, _, weights, bundle, definition = prepared_case(tmp_path)
    FakeUpstreamTrainer.saved = []
    sampler = FakeSampler(prune=True)
    trainer = YoloTrainerAdapter(FakeUpstreamTrainer, weights, bundle)
    result = run_synthetic_study(definition, tmp_path / "pruned", sampler, trainer,
                                 CheckpointValidationAdapter(FakeBoundEvaluator()),
                                 stop_requested=lambda: len(sampler.tells) == 6)
    assert [t["status"] for t in result["trials"]] == ["complete"] * 5 + ["pruned"]
    assert len(FakeUpstreamTrainer.saved) == 5 * 30 + 10
    FakeUpstreamTrainer.saved = []
    interrupted = run_synthetic_study(definition, tmp_path / "interrupted", FakeSampler(), trainer,
                                      CheckpointValidationAdapter(FakeBoundEvaluator()),
                                      stop_requested=lambda: len(FakeUpstreamTrainer.saved) == 2)
    assert interrupted["trials"][0]["status"] == "interrupted"
    assert interrupted["trials"][0]["value"] is None and len(FakeUpstreamTrainer.saved) == 2


def test_validation_failure_is_failed_attempt_not_zero_or_continued_training(tmp_path):
    _, _, weights, bundle, definition = prepared_case(tmp_path)
    class BrokenMetric(FakeBoundEvaluator):
        def evaluate_checkpoint(self, request, checkpoint):
            result = super().evaluate_checkpoint(request, checkpoint)
            result["value"] = float("nan")
            return result
    sampler = FakeSampler()
    FakeUpstreamTrainer.saved = []
    result = run_synthetic_study(definition, tmp_path / "failed", sampler,
                                 YoloTrainerAdapter(FakeUpstreamTrainer, weights, bundle),
                                 CheckpointValidationAdapter(BrokenMetric()),
                                 stop_requested=lambda: len(sampler.tells) == 1)
    assert result["trials"][0]["status"] == "failed" and result["trials"][0]["value"] is None
    assert FakeUpstreamTrainer.saved == [1]


def test_arguments_reject_bad_weights_controls_resume_and_output(tmp_path):
    config, _, weights, bundle, _ = prepared_case(tmp_path)
    output = tmp_path / "attempt"
    output.mkdir()
    request = {"configuration": config, "parameters": config["study"]["control"], "epochs": 30,
               "initialization": config["initialization"], "output_directory": output}
    assert training_arguments(request, weights, bundle)["amp"] is False
    for change in ({"resume_checkpoint": weights}, {"completed_epochs": 1}, {"seed": 29}):
        with pytest.raises(ValueError):
            training_arguments({**request, **change}, weights, bundle)
    for device in ("", "0,1", None):
        invalid = deepcopy(request)
        invalid["configuration"]["requested_device"] = device
        with pytest.raises(ValueError):
            training_arguments(invalid, weights, bundle)
    for bad_weights in (Path("synthetic.pt"), tmp_path / "missing.pt"):
        with pytest.raises(ValueError):
            training_arguments(request, bad_weights, bundle)
    weights.write_bytes(b"changed")
    with pytest.raises(ValueError):
        training_arguments(request, weights, bundle)
    weights.write_bytes(b"synthetic initialization bytes")
    (output / "preserve").write_text("existing work")
    with pytest.raises(ValueError, match="empty"):
        training_arguments(request, weights, bundle)
    assert (output / "preserve").read_text() == "existing work"


@pytest.mark.parametrize("seed", [29, 43])
def test_repeat_arguments_use_matching_receipt_without_changing_search_config(tmp_path, seed):
    config, _, weights, bundle, _ = prepared_case(tmp_path)
    before = deepcopy(config)
    receipt = init_receipt()
    receipt["seed"] = seed
    output = tmp_path / "repeat-attempt"
    output.mkdir()
    request = {"configuration": config, "parameters": config["study"]["control"], "epochs": 100,
               "initialization": receipt, "output_directory": output,
               "stage": "repeatability", "seed": seed}
    arguments = training_arguments(request, weights, bundle)
    assert arguments["seed"] == seed and arguments["epochs"] == 100
    assert config == before and config["initialization"]["seed"] == 17
    request["initialization"] = config["initialization"]
    with pytest.raises(ValueError):
        training_arguments(request, weights, bundle)


def test_validation_binding_rejects_checkpoint_replacement(tmp_path):
    path = tmp_path / "synthetic.pt"
    path.write_bytes(b"original")
    request = {"checkpoint_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    class ReplacesCheckpoint:
        synthetic = True

        def evaluate_checkpoint(self, request, checkpoint):
            checkpoint.write_bytes(b"changed")
            return {}
    adapter = CheckpointValidationAdapter(ReplacesCheckpoint())
    with pytest.raises(ValueError, match="changed during"):
        adapter.evaluate_checkpoint(request, path)
    with pytest.raises(ValueError, match="identity mismatch"):
        adapter.evaluate_checkpoint(request, path)


def test_live_factory_blocks_before_import_or_file_access():
    config, evidence = research_case()
    plan = research_plan(config, evidence)
    plan["blockers"] = []
    with patch("builtins.__import__", side_effect=AssertionError("model import")), \
            patch("sdp_xray.training_backend._sha256", side_effect=AssertionError("weights read")):
        with pytest.raises(ValueError, match="live execution blocked"):
            live_trainer_class(plan)
    with pytest.raises(ValueError, match="synthetic"):
        YoloTrainerAdapter(object, "unread", "unread")
    with pytest.raises(ValueError, match="live execution blocked"):
        YoloTrainerAdapter(object, "unread", "unread", plan=plan)
