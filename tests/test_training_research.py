"""Invented metadata and tiny generated images only; no real approvals or ML metrics."""

import hashlib
import importlib.abc
import io
import json
import runpy
import sys
from contextlib import redirect_stdout
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

import pytest
import test_training as legacy

from sdp_xray.training import PAIRS, SPLITS, convert_coco, training_plan, write_training_manifest
from sdp_xray.training_partition import (
    fingerprint,
    make_partition,
    partition_findings,
    subset_coco,
    validate_partition,
)
from sdp_xray.training_research import (
    APPROVALS,
    TASKS,
    audit_findings,
    example_research_config,
    inspect_partition_sources,
    research_candidate_manifest,
    research_plan,
    task_identity,
    validate_initialization,
    write_research_record,
)

ROOT = Path(__file__).resolve().parents[1]


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def review():
    return {"decision": "approved", "owner": "synthetic fixture", "reference": "not real approval"}


def inventory():
    train = [{"id": i, "sha256": digest(f"synthetic train {i}"), "group": None,
              "labels": ["generic:Explosive", "specific:IED Explosive" if i % 2 else
                         "specific:Laptop Explosive"]} for i in range(10)]
    test = [{"id": 100 + i, "sha256": digest(f"synthetic test {i}"), "group": None,
             "labels": []} for i in range(2)]
    return train, test


def partition_policy(train, test, mode="exploratory_exact_bytes"):
    return {"review": review(), "findings_sha256": fingerprint(partition_findings(train, test)),
            "duplicate_action": "preserve_and_group", "test_overlap_action": "preserve_and_report",
            "grouping": mode, "physical_group_evidence": review() if mode == "verified_physical" else None,
            "group_key": "synthetic_group" if mode == "verified_physical" else None,
            "label_review_reference": "synthetic label membership"}


def init_receipt(task="generic"):
    sha = digest("synthetic initialization bytes")
    return {"kind": "general_pretrained", "architecture": "YOLOv10-M", "checkpoint_sha256": sha,
            "source_reference": "synthetic only", "verification": {**review(), "verified_sha256": sha},
            "excludes_iedxray": review(), "procedure": "synthetic load procedure",
            "task_head": "synthetic task head procedure, never executed", "seed": 17,
            "task": task_identity(task)}


def research_case(task="generic"):
    config = example_research_config()
    train, test = inventory()
    partition = make_partition(train, test, partition_policy(train, test))
    counts = {"train": len(partition["fit_ids"]), "validation": len(partition["validation_ids"]), "test": 2}
    identity = task_identity(task)
    summaries = {split: {"images": n, "annotations": 1, "image_files_checked": n,
                         "image_file_checks": "complete", "exact_file_duplicate_groups": [],
                         "physical_group_key": None, "physical_group_checks": "not_checked",
                         "physical_group_count": 0, "category_map": identity["source_category_map"]}
                 for split, n in counts.items()}
    sources = {split: {"annotation_sha256": digest(split + " annotations"),
                       "image_inventory_sha256": digest(split + " images")} for split in SPLITS}
    evidence = {"sources": sources, "partition": partition, "audits": {}, "conversions": {
        split: {"images": n, "annotations": 1, "class_map_sha256": identity["class_map_sha256"]}
        for split, n in counts.items()}}
    for left, right in PAIRS:
        evidence["audits"][f"{left}_{right}"] = {
            "ok": True, "errors": [], "warnings": ["Physical-group metadata not checked: synthetic"],
            "summary": {"primary": deepcopy(summaries[left]), "other": deepcopy(summaries[right]),
                        "split_overlap": {"filenames": [], "physical_group_values": [],
                                          "exact_file_duplicates": [], "category_maps_match": True,
                                          "exact_file_checks": "checked_available_files"}}}
    evidence["partition_binding"] = {"partition_sha256": partition["membership_sha256"],
                                     "sources_sha256": fingerprint(sources), "task": task,
                                     "image_membership_and_bytes_checked": True}
    config.update(task=task, initialization=init_receipt(task), partition_sha256=partition["membership_sha256"],
                  sources=deepcopy(sources), source_provenance=review(), batch=1,
                  owner="synthetic", requested_device="cpu", output_directory="synthetic-uncreated-output",
                  approvals={name: review() for name in APPROVALS},
                  generic_completion={**review(), "partition_sha256": partition["membership_sha256"]})
    config["objective"].update(evaluator_id="synthetic-adapter", settings={"max_detections": 100})
    config["environment"].update(lock_sha256=digest("synthetic lock"), qualification=review(),
                                  journal_locking=review(), effective_defaults_sha256=digest("defaults"))
    config["data_policy"] = {"review": review(), "audit_findings_sha256": fingerprint(audit_findings(evidence)),
                             "duplicate_action": "preserve_and_group", "test_overlap_action": "preserve_and_report",
                             "boundary_action": "block_invalid_geometry"}
    return config, evidence


def test_example_uses_documented_choices_without_fabricated_identity():
    config = json.loads((ROOT / "configs/finetune.example.json").read_text())
    assert config == example_research_config()
    assert config["task"] == "generic" and config["batch"] is None and config["initialization"] is None
    assert "gui_confirmation" not in config and "intended_parent_checkpoint_sha256" not in config
    assert config["study"]["attempts"] == 20
    assert config["study"]["control"]["lr0"] == 0.001
    plan = research_plan(config)
    assert plan["outputs"] == {"checkpoint_sha256": None, "metrics": None}
    assert plan["checkpoint_verification"]["performed_by_this_planner"] is False


@pytest.mark.parametrize("task", ["generic", "specific"])
def test_complete_synthetic_receipts_only_clear_evidence_gates(task):
    config, evidence = research_case(task)
    plan = research_plan(config, evidence)
    assert plan["blockers"] == ["execution:software_draft_only", "integration:live_trainer_not_connected"]
    assert plan["model"] == task_identity(task)
    assert plan["execution"] == {"training_started": False, "device": None}


def test_all_experiment_types_remain_distinct():
    config, evidence = research_case()
    for mode, blocker in (("supplied_checkpoint_reproduction", "faisal_ali_evaluation_handoff_no_training"),
                          ("author_training_reproduction", "author_protocol_not_qualified")):
        config["experiment"] = mode
        plan = research_plan(config, evidence)
        assert f"experiment:{blocker}" in plan["blockers"]
        assert config["author_training_details"] is None


@pytest.mark.parametrize("field", ["verification", "excludes_iedxray", "procedure", "task_head", "task", "seed"])
def test_initialization_receipt_requires_exposure_procedure_head_and_seed(field):
    receipt = init_receipt()
    receipt[field] = None
    with pytest.raises(ValueError):
        validate_initialization(receipt, "generic")


def test_supplied_task_hash_is_not_general_pretraining():
    receipt = init_receipt()
    receipt["checkpoint_sha256"] = legacy.get_model(TASKS["generic"]).sha256
    receipt["verification"]["verified_sha256"] = receipt["checkpoint_sha256"]
    with pytest.raises(ValueError):
        validate_initialization(receipt, "generic")


def test_two_research_outputs_share_the_actual_starting_hash(tmp_path):
    old = legacy.CandidateManifestTests()
    old.setUp()
    try:
        init = init_receipt()
        records = []
        before = deepcopy((old.run, old.results))
        for name in ("untuned", "tuned"):
            checkpoint = tmp_path / (name + ".bin")
            checkpoint.write_bytes(("synthetic " + name).encode())
            results = deepcopy(old.results)
            results[0]["model"].update(id="research-fixture", provenance="sha256:" + digest("synthetic " + name))
            record = write_research_record(tmp_path / name, "generic", init, checkpoint, old.run,
                                            results, model_id="research-fixture")
            records.append(record)
        assert records[0]["model"]["checkpoint_sha256"] != records[1]["model"]["checkpoint_sha256"]
        assert all(r["role"] == "candidate" and r["model"]["parent_checkpoint_sha256"] == init["checkpoint_sha256"]
                   for r in records)
        assert records[1]["model"]["parent_checkpoint_sha256"] != records[0]["model"]["checkpoint_sha256"]
        assert (old.run, old.results) == before
        with pytest.raises(ValueError):
            research_candidate_manifest("generic", init, checkpoint, {**old.run, "epochs": 10},
                                        results, model_id="research-fixture")
        with pytest.raises(FileExistsError):
            write_research_record(tmp_path / "tuned", "generic", init, checkpoint, old.run,
                                  results, model_id="research-fixture")
    finally:
        old.doCleanups()


def test_wrong_map_missing_approvals_and_specific_sequence_block():
    config, evidence = research_case("specific")
    config["approvals"]["common_initialization_comparison"] = None
    config["generic_completion"] = None
    evidence["audits"]["train_validation"]["summary"]["primary"]["category_map"] = {"0": "Explosive"}
    blockers = research_plan(config, evidence)["blockers"]
    assert "approval:common_initialization_comparison" in blockers
    assert "sequence:generic_confirmation_first" in blockers
    assert "audit:train:wrong_class_map" in blockers


@pytest.mark.parametrize("field", ["images", "image_files_checked", "image_file_checks",
                                   "exact_file_duplicate_groups", "physical_group_checks"])
def test_incomplete_audit_never_clears_from_ok(field):
    config, evidence = research_case()
    del evidence["audits"]["train_validation"]["summary"]["primary"][field]
    assert any(b.startswith("audit:") for b in research_plan(config, evidence)["blockers"])


def test_reviewed_test_overlap_is_retained_but_geometry_and_fit_overlap_block():
    config, evidence = research_case()
    report = evidence["audits"]["train_test"]
    report["summary"]["split_overlap"]["exact_file_duplicates"] = [{"sha256": digest("overlap")}]
    report.update(ok=False, errors=["Exact file content overlaps across splits: 1 hashes"])
    assert "data:reviewed_findings_dispositions_required" in research_plan(config, evidence)["blockers"]
    config["data_policy"]["audit_findings_sha256"] = fingerprint(audit_findings(evidence))
    assert not any(b.startswith("audit:") for b in research_plan(config, evidence)["blockers"])
    report["errors"].append("Annotation 0 bbox exceeds image bounds")
    config["data_policy"]["audit_findings_sha256"] = fingerprint(audit_findings(evidence))
    assert "audit:train_test:errors_or_missing" in research_plan(config, evidence)["blockers"]
    evidence["audits"]["train_validation"]["summary"]["split_overlap"]["exact_file_duplicates"] = [{}]
    assert "validation:fit_overlap" in research_plan(config, evidence)["blockers"]


def test_missing_validation_and_source_binding_are_blocked():
    config, evidence = research_case()
    config["sources"]["validation"] = config["sources"]["test"]
    evidence.pop("partition_binding")
    blockers = research_plan(config, evidence)["blockers"]
    assert "validation:train_or_test_fallback" in blockers
    assert "data:partition_source_binding_required" in blockers


def test_research_manifest_is_separate_consistent_and_exclusive(tmp_path):
    config, evidence = research_case()
    plan = training_plan(config, evidence, ())
    write_training_manifest(tmp_path / "plan.json", plan)
    with pytest.raises(FileExistsError):
        write_training_manifest(tmp_path / "plan.json", plan)
    plan["outputs"]["checkpoint_sha256"] = "a" * 64
    with pytest.raises(ValueError):
        write_training_manifest(tmp_path / "tampered.json", plan)
    config["output_directory"] = str(tmp_path)
    assert "execution:output_collision" in research_plan(config, evidence)["blockers"]


def test_partition_preserves_groups_duplicates_sources_and_shared_task_membership():
    train, test = inventory()
    train[0]["sha256"] = train[1]["sha256"]
    for row in [*train, *test]:
        row["group"] = str(row["id"])
    train[1]["group"] = train[2]["group"]
    before = deepcopy((train, test))
    policy = partition_policy(train, test, "verified_physical")
    result = make_partition(train, test, policy)
    assert (train, test) == before
    assert result == make_partition(list(reversed(train)), test, policy)
    assert set(result["fit_ids"]) | set(result["validation_ids"]) == set(range(10))
    assert not set(result["fit_ids"]) & set(result["validation_ids"])
    assert set((0, 1, 2)).issubset(result["fit_ids"]) or set((0, 1, 2)).issubset(result["validation_ids"])
    assert not {100, 101} & set(result["fit_ids"] + result["validation_ids"])
    validate_partition(result)
    result["validation_ids"] = result["fit_ids"]
    with pytest.raises(ValueError):
        validate_partition(result)


def test_exploratory_partition_is_explicit_and_overlap_review_is_bound():
    train, test = inventory()
    test[0]["sha256"] = train[0]["sha256"]
    policy = partition_policy(train, test)
    result = make_partition(train, test, policy)
    assert result["validation_fraction_actual"] == 0.2
    assert any("physical independence" in line for line in result["limitations"])
    assert result["findings"]["train_test_bytes"]
    test[0]["sha256"] = digest("changed")
    with pytest.raises(ValueError):
        make_partition(train, test, policy)


def test_no_invented_groups_no_empty_partition_or_silent_group_discard():
    train, test = inventory()
    with pytest.raises(ValueError):
        make_partition(train, test, partition_policy(train, test, "verified_physical"))
    for row in train:
        row["sha256"] = digest("one connected component")
    with pytest.raises(ValueError):
        make_partition(train, test, partition_policy(train, test))
    train, test = inventory()
    train[0]["group"] = "supplied group"
    with pytest.raises(ValueError):
        make_partition(train, test, partition_policy(train, test))


def test_real_auditor_binding_and_conversion_on_generated_images(tmp_path):
    from PIL import Image

    train, test = inventory()
    for split, rows in (("train", train), ("test", test)):
        for row in rows:
            path = tmp_path / f"{split}-{row['id']}.png"
            Image.new("RGB", (8, 8), (row["id"], 5, 9)).save(path)
            row["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    partition = make_partition(train, test, partition_policy(train, test))
    config, _ = research_case()
    sources = {}
    original = None
    for task in ("generic", "specific"):
        identity = task_identity(task)
        categories = [{"id": int(k), "name": v} for k, v in identity["source_category_map"].items()]
        document = {"images": [{"id": row["id"], "file_name": f"train-{row['id']}.png",
                                 "width": 8, "height": 8} for row in train],
                    "categories": categories, "annotations": [
                        {"id": 0, "image_id": 0, "category_id": categories[0]["id"],
                         "bbox": [1, 1, 2, 2], "iscrowd": 0}]}
        original = deepcopy(document)
        for split in ("fit", "validation"):
            derived = subset_coco(document, partition, split, TASKS[task])
            path = tmp_path / f"{task}-{split}.json"
            path.write_text(json.dumps(derived))
            converted = convert_coco(path, TASKS[task])
            assert len(converted) == len(partition[split + "_ids"])
            assert sum(bool(v) for v in converted.values()) <= 1  # Empty images remain.
            sources["train" if split == "fit" else split] = (path, tmp_path)
        assert document == original
        test_doc = {"images": [{"id": row["id"], "file_name": f"test-{row['id']}.png",
                                 "width": 8, "height": 8} for row in test],
                    "categories": categories, "annotations": []}
        test_path = tmp_path / (task + "-test.json")
        test_path.write_text(json.dumps(test_doc))
        sources["test"] = (test_path, tmp_path)
        before = {p: p.read_bytes() for p in tmp_path.iterdir() if p.is_file()}
        evidence = inspect_partition_sources(sources, task, partition)
        assert before == {p: p.read_bytes() for p in tmp_path.iterdir() if p.is_file()}
        config.update(task=task, initialization=init_receipt(task), sources=evidence["sources"],
                      partition_sha256=partition["membership_sha256"])
        config["generic_completion"]["partition_sha256"] = partition["membership_sha256"]
        config["data_policy"]["audit_findings_sha256"] = fingerprint(audit_findings(evidence))
        assert research_plan(config, evidence)["blockers"] == [
            "execution:software_draft_only", "integration:live_trainer_not_connected"]
    with pytest.raises(ValueError):
        subset_coco(original, partition, "test", TASKS["specific"])


@pytest.mark.parametrize("script", ["finetune_yolov10.py", "tune_yolov10.py"])
def test_both_clis_block_without_optional_imports_or_subprocesses(script, tmp_path):
    class NoOptional(importlib.abc.MetaPathFinder):
        def find_spec(self, fullname, path=None, target=None):
            if fullname.split(".")[0] in {"optuna", "numpy", "torch", "torchvision", "ultralytics"}:
                raise AssertionError("optional backend imported on planning path")
    finder = NoOptional()
    sys.meta_path.insert(0, finder)
    try:
        main = runpy.run_path(str(ROOT / "scripts" / script))["main"]
        with patch("subprocess.Popen", side_effect=AssertionError("process launched")), \
                patch("sdp_xray.training_research._sha256", side_effect=AssertionError("artifact read")):
            for args in ([], ["--execute"], ["--task", "specific"],
                         ["--output", str(tmp_path / "plan.json")]):
                with redirect_stdout(io.StringIO()) as stream:
                    assert main(args) == 2
                    result = json.loads(stream.getvalue())
                    assert result["status"] == "blocked" and result["training_started"] is False
    finally:
        sys.meta_path.remove(finder)
