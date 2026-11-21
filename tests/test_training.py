"""Synthetic software checks only; checkpoint bytes are not a real model."""

import hashlib
import importlib.abc
import io
import json
import runpy
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

from sdp_xray.baseline import read_record
from sdp_xray.common.run_manifest import validate_run_manifest
from sdp_xray.model_catalog import get_model
from sdp_xray.training import (
    APPROVALS,
    PAIRS,
    SPLITS,
    candidate_manifest,
    category_indices,
    convert_coco,
    inspect_training_sources,
    training_plan,
    write_candidate_record,
    write_training_manifest,
)

ROOT = Path(__file__).resolve().parents[1]


class CandidateManifestTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name)
        self.checkpoint = self.directory / "synthetic-only.pt"
        self.checkpoint.write_bytes(b"synthetic checkpoint bytes, not model weights")
        self.digest = hashlib.sha256(self.checkpoint.read_bytes()).hexdigest()
        self.spec = get_model("author-yolov10m-generic")
        self.run = {
            "run_id": "synthetic-candidate",
            "timestamp_utc": "2026-01-01T00:00:00+00:00",
            "code": {"git_commit": "synthetic", "git_dirty": True,
                     "upstream_revision": "synthetic"},
            "settings": {"imgsz": 640, "batch": 1, "conf": 0.25,
                         "max_det": 300, "augment": False},
            "stages": {
                name: {"status": "absent", "detail": "synthetic software fixture"}
                for name in ("preprocessing", "roi", "features", "postprocessing")
            },
            "requested_device": "cpu",
            "device": "cpu",
            "precision": "float32",
            "inputs": [{"scan_id": "synthetic-scan", "sha256": "c" * 64,
                        "source_run_id": "synthetic-source"}],
            "limitations": ["synthetic software fixture, not inference evidence"],
        }
        self.baseline = {
            **deepcopy(self.run),
            "schema_version": "1.0",
            "run_id": "synthetic-baseline",
            "role": "baseline",
            "status": "ok",
            "model": {
                "id": self.spec.id, "task": self.spec.task, "kind": self.spec.kind,
                "checkpoint_sha256": self.spec.sha256,
                "parent_checkpoint_sha256": None,
                "class_map_sha256": self.spec.class_map_sha256,
                "model_names": {"0": "Explosive"},
                "source_category_map": {"0": "Explosive"},
            },
        }
        self.results = [{
            "schema_version": "1.0", "scan_id": "synthetic-scan", "status": "ok",
            "image": {"width": 100, "height": 80},
            "model": {"id": self.spec.id, "task": self.spec.task,
                      "provenance": f"sha256:{self.digest}"},
            "run": {"id": self.run["run_id"], "provenance": "run_manifest.json"},
            "threshold": 0.25, "error": None,
            "detections": [{
                "id": "synthetic-region", "kind": self.spec.kind,
                "box_xyxy": [2, 3, 20, 30],
                "category": {"namespace": self.spec.task, "label": "Explosive"},
                "confidence": 0.7, "device_id": None,
            }],
        }]

    def build(self):
        return candidate_manifest(self.baseline, self.checkpoint, self.run, self.results)

    def write(self):
        return write_candidate_record(
            self.directory / "record", self.baseline, self.checkpoint, self.run, self.results
        )

    def test_records_actual_candidate_hash_and_agreed_parent(self):
        manifest = self.build()
        self.assertEqual(manifest["role"], "candidate")
        self.assertEqual(manifest["model"]["checkpoint_sha256"], self.digest)
        self.assertEqual(
            manifest["model"]["parent_checkpoint_sha256"],
            "b484d9a6fb37236f6adcc8c019e6a836f11901dc53a0f71d6cce7262413287ff",
        )
        for key in ("task", "kind", "class_map_sha256", "model_names", "source_category_map"):
            self.assertEqual(manifest["model"][key], self.baseline["model"][key])
        self.assertEqual(manifest["model"]["source_category_map"], {"0": "Explosive"})

    def test_rejects_baseline_identity_or_map_changes(self):
        for key, value in (
            ("checkpoint_sha256", "d" * 64),
            ("class_map_sha256", "d" * 64),
            ("source_category_map", {"1": "Explosive"}),
            ("model_names", {"1": "Explosive"}),
            ("task", "another.task"),
            ("kind", "device"),
            ("id", "another-model"),
        ):
            with self.subTest(key=key):
                baseline = deepcopy(self.baseline)
                baseline["model"][key] = value
                with self.assertRaises(ValueError):
                    candidate_manifest(baseline, self.checkpoint, self.run, self.results)

    def test_rejects_candidate_as_original_baseline(self):
        self.baseline["role"] = "candidate"
        self.baseline["model"]["parent_checkpoint_sha256"] = "d" * 64
        with self.assertRaises(ValueError):
            self.build()

    def test_requested_device_is_required(self):
        for value in (None, "", 0):
            with self.subTest(value=value):
                self.run["requested_device"] = value
                with self.assertRaises(ValueError):
                    self.build()
        del self.run["requested_device"]
        with self.assertRaises(ValueError):
            self.build()

    def test_requested_and_actual_devices_are_separate(self):
        self.run["requested_device"] = "cuda:0"
        manifest = self.build()
        self.assertEqual(manifest["requested_device"], "cuda:0")
        self.assertEqual(manifest["device"], "cpu")

    def test_failed_scan_preserves_unresolved_actual_device(self):
        self.run["requested_device"] = "cuda:0"
        self.run["device"] = None
        self.results[0].update(
            status="error", image=None, detections=[],
            error={"code": "synthetic_failure", "message": "synthetic failure before execution"},
        )
        manifest = self.build()
        self.assertEqual(manifest["status"], "error")
        self.assertIsNone(manifest["device"])
        self.assertEqual(manifest["requested_device"], "cuda:0")

    def test_mixed_results_report_failure_and_require_actual_device(self):
        failed = deepcopy(self.results[0])
        failed.update(
            scan_id="failed-scan", status="error", image=None, detections=[],
            error={"code": "synthetic_failure", "message": "synthetic"},
        )
        self.results.append(failed)
        self.run["inputs"].append({
            "scan_id": "failed-scan", "sha256": "d" * 64, "source_run_id": "failed-source",
        })
        self.assertEqual(self.build()["status"], "error")
        self.run["device"] = None
        with self.assertRaises(ValueError):
            self.build()

    def test_rejects_old_predictions_without_relabelling_them(self):
        self.results[0]["model"]["provenance"] = f"sha256:{self.spec.sha256}"
        before = deepcopy(self.results)
        with self.assertRaises(ValueError):
            self.write()
        self.assertEqual(self.results, before)
        self.assertFalse((self.directory / "record").exists())

    def test_changed_checkpoint_is_detected(self):
        self.checkpoint.write_bytes(b"different synthetic checkpoint")
        with self.assertRaises(ValueError):
            self.write()
        self.assertFalse((self.directory / "record").exists())

    def test_predictions_must_match_run_inputs_and_task(self):
        for edit in (
            lambda result: result["run"].update(id="another-run"),
            lambda result: result.update(scan_id="another-scan"),
            lambda result: result["model"].update(task="another.task"),
            lambda result: result.update(threshold=0.5),
            lambda result: result["detections"][0]["category"].update(label="unknown"),
        ):
            with self.subTest(edit=edit):
                results = deepcopy(self.results)
                edit(results[0])
                with self.assertRaises(ValueError):
                    candidate_manifest(self.baseline, self.checkpoint, self.run, results)

    def test_missing_or_duplicate_results_are_rejected(self):
        for results in ([], None, [*self.results, *self.results]):
            with self.subTest(results=results):
                with self.assertRaises(ValueError):
                    candidate_manifest(self.baseline, self.checkpoint, self.run, results)

    def test_training_settings_and_reserved_fields_are_rejected(self):
        for key, value in (
            ("epochs", 5), ("role", "baseline"), ("model", {}),
            ("status", "planned"), ("schema_version", "1.0"),
        ):
            with self.subTest(key=key):
                run = {**self.run, key: value}
                with self.assertRaises(ValueError):
                    candidate_manifest(self.baseline, self.checkpoint, run, self.results)
        self.run["settings"]["lr0"] = 0.01
        with self.assertRaises(ValueError):
            self.build()

    def test_inputs_are_not_mutated_or_shared_with_output(self):
        before = deepcopy((self.baseline, self.run, self.results))
        manifest = self.build()
        self.assertEqual((self.baseline, self.run, self.results), before)
        manifest["model"]["model_names"]["0"] = "changed"
        manifest["settings"]["conf"] = 0.5
        self.assertEqual((self.baseline, self.run, self.results), before)

    def test_record_round_trip_preserves_predictions_and_omits_checkpoint_path(self):
        manifest = self.write()
        loaded_manifest, loaded_results = read_record(self.directory / "record")
        self.assertEqual(loaded_manifest, manifest)
        self.assertEqual(loaded_results, self.results)
        self.assertNotIn(str(self.checkpoint), json.dumps(loaded_manifest))

    def test_existing_output_is_preserved(self):
        output = self.directory / "record"
        output.mkdir()
        sentinel = output / "keep.txt"
        sentinel.write_text("existing work", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            self.write()
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "existing work")

    def test_missing_checkpoint_does_not_create_a_record(self):
        self.checkpoint.unlink()
        with self.assertRaises(OSError):
            self.write()
        self.assertFalse((self.directory / "record").exists())

    def test_shared_validator_rejects_removed_or_null_candidate_parent(self):
        for remove in (True, False):
            with self.subTest(remove=remove):
                manifest = self.build()
                if remove:
                    del manifest["model"]["parent_checkpoint_sha256"]
                else:
                    manifest["model"]["parent_checkpoint_sha256"] = None
                with self.assertRaises(ValueError):
                    validate_run_manifest(manifest)

    def test_other_catalog_parent_requires_explicit_selection(self):
        for model_id in ("author-yolov10m-device", "author-yolov10m-specific"):
            with self.subTest(model_id=model_id):
                spec = get_model(model_id)
                self.baseline["model"].update(
                    id=spec.id, task=spec.task, kind=spec.kind, checkpoint_sha256=spec.sha256,
                    class_map_sha256=spec.class_map_sha256,
                    model_names={str(k): v for k, v in spec.names.items()},
                    source_category_map=spec.source_category_map,
                )
                self.results[0]["model"].update(id=spec.id, task=spec.task)
                self.results[0]["detections"] = []
                with self.assertRaises(ValueError):
                    self.build()
                manifest = candidate_manifest(self.baseline, self.checkpoint, self.run,
                                              self.results, model_id=model_id)
                self.assertEqual(manifest["model"]["parent_checkpoint_sha256"], spec.sha256)
                self.assertEqual(manifest["model"]["source_category_map"], spec.source_category_map)


def example_config():
    # Preserve every original gate test against the original schema as research evolves.
    return json.loads((ROOT / "tests/fixtures/legacy_finetune_config.json").read_text(encoding="utf-8"))


def synthetic_evidence():
    """Invented receipts for gate unit checks, never real approval or audit evidence."""
    spec = get_model("author-yolov10m-generic")
    row = {"images": 2, "annotations": 1, "image_files_checked": 2,
           "image_file_checks": "complete", "exact_file_duplicate_groups": [],
           "physical_group_key": "synthetic_group", "physical_group_checks": "complete",
           "physical_group_count": 2, "category_map": spec.source_category_map}
    report = {"ok": True, "errors": [], "warnings": [], "summary": {
        "primary": row, "other": deepcopy(row), "split_overlap": {
            "filenames": [], "physical_group_values": [], "exact_file_duplicates": [],
            "exact_file_checks": "checked_available_files", "category_maps_match": True,
        },
    }}
    return {
        "sources": {split: {"annotation_sha256": str(i) * 64,
                            "image_inventory_sha256": str(i + 4) * 64}
                    for i, split in enumerate(SPLITS, 1)},
        "conversions": {split: {"images": 2, "annotations": 1,
                                "class_map_sha256": spec.class_map_sha256} for split in SPLITS},
        "audits": {f"{left}_{right}": deepcopy(report) for left, right in PAIRS},
    }


class PlanningTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name)
        self.config = example_config()
        self.config["model_id"] = "author-yolov10m-generic"
        self.evidence = synthetic_evidence()
        self.config["sources"] = deepcopy(self.evidence["sources"])

    def plan(self):
        return training_plan(self.config, self.evidence)

    def test_example_has_no_selected_model_or_fabricated_training_values(self):
        config = example_config()
        result = training_plan(config)
        self.assertIsNone(result["model"])
        self.assertTrue(all(value is None for value in config["hyperparameters"].values()))
        self.assertIn("model:selection_unconfirmed", result["blockers"])
        self.assertIn("document:docs/tasks.md:T41", result["blockers"])
        self.assertFalse(result["checkpoint_verification"]["performed_by_this_planner"])
        self.assertEqual(result["outputs"], {"checkpoint_sha256": None, "metrics": None})

    def test_category_mapping_zero_and_reordered_device_rows(self):
        self.assertEqual(category_indices("author-yolov10m-generic",
                                         [{"id": 0, "name": "Explosive"}]), {0: 0})
        spec = get_model("author-yolov10m-device")
        categories = [{"id": int(k), "name": v} for k, v in spec.source_category_map.items()]
        self.assertEqual(category_indices(spec.id, list(reversed(categories))),
                         {1: 0, 2: 1, 3: 2, 4: 3})
        for rows in ([{"id": 1, "name": "Explosive"}], [{"id": False, "name": "Explosive"}],
                     [{"id": 0, "name": "Wrong"}], [{"id": 0, "name": "Explosive"}] * 2):
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                category_indices("author-yolov10m-generic", rows)

    def test_ok_without_checks_never_clears_preflight(self):
        self.evidence["audits"] = {"train_validation": {"ok": True}}
        self.assertTrue(any(b.startswith("audit:") for b in self.plan()["blockers"]))

    def test_each_missing_audit_field_blocks(self):
        for field in ("images", "image_files_checked", "image_file_checks",
                      "exact_file_duplicate_groups", "physical_group_key",
                      "physical_group_checks", "physical_group_count", "category_map"):
            with self.subTest(field=field):
                evidence = deepcopy(self.evidence)
                del evidence["audits"]["train_validation"]["summary"]["primary"][field]
                result = training_plan(self.config, evidence)
                self.assertTrue(any(b.startswith("audit:") for b in result["blockers"]))

    def test_errors_warnings_duplicates_overlap_and_empty_validation_block(self):
        edits = [
            lambda r: r.update(errors=["invalid geometry"]),
            lambda r: r.update(warnings=["unresolved policy"]),
            lambda r: r["summary"]["primary"].update(exact_file_duplicate_groups=[["a", "b"]]),
            lambda r: r["summary"]["other"].update(images=0, image_files_checked=0),
            lambda r: r["summary"].update(split_overlap="not_checked"),
            lambda r: r["summary"]["split_overlap"].update(exact_file_duplicates=[{"sha256": "a"}]),
            lambda r: r["summary"]["split_overlap"].update(physical_group_values=["shared"]),
            lambda r: r["summary"]["primary"].update(category_map={"1": "Explosive"}),
        ]
        for edit in edits:
            with self.subTest(edit=edit):
                evidence = deepcopy(self.evidence)
                edit(evidence["audits"]["train_validation"])
                result = training_plan(self.config, evidence)
                self.assertTrue(any(b.startswith("audit:") for b in result["blockers"]))

    def test_validation_missing_test_fallback_and_false_independence_block(self):
        self.config["sources"]["validation"] = None
        self.assertIn("sources:validation:missing_hashes", self.plan()["blockers"])
        self.config["sources"]["validation"] = self.config["sources"]["test"]
        self.assertIn("validation:train_or_test_fallback", self.plan()["blockers"])
        self.config["validation"] = {"origin": "published_test", "membership_reference": "synthetic",
                                     "independent_of_author_checkpoint": True,
                                     "test_used_for_tuning": True}
        self.assertIn("validation:design_and_author_exposure_unresolved", self.plan()["blockers"])

    def test_approvals_owner_environment_and_parameters_required(self):
        blockers = self.plan()["blockers"]
        for approval in APPROVALS:
            self.assertIn(f"approval:{approval}", blockers)
        for name in ("owner", "requested_device", "output_directory"):
            self.assertIn(f"execution:{name}_required", blockers)
        self.assertIn("environment:training_save_reload_unqualified", blockers)
        self.assertIn("hyperparameters:unapproved_or_invalid", blockers)

    def test_selected_task_does_not_silently_replace_intended_parent(self):
        self.config["model_id"] = "author-yolov10m-device"
        result = self.plan()
        self.assertEqual(result["model"]["task"], "iedxray.device_detection")
        self.assertIn("model:intended_parent_conflicts_with_selection", result["blockers"])
        self.assertIn("model:sanitized_gui_confirmation", result["blockers"])

    def test_malformed_evidence_is_blocked_and_empty_mapping_is_not_clearance(self):
        self.evidence["audits"] = ["invalid"]
        self.assertIn("audit:malformed_evidence", self.plan()["blockers"])
        with self.assertRaises(ValueError):
            training_plan(self.config, [])

    def test_supplied_receipts_cannot_enable_execution(self):
        self.config["approvals"] = {key: {"decision": "approved", "owner": "synthetic",
                                          "reference": "synthetic"} for key in APPROVALS}
        self.config["hyperparameters"] = {"epochs": 1, "batch": 1, "imgsz": 32,
                                           "lr0": 0.001, "seed": 0}
        result = self.plan()
        self.assertIn("execution:software_draft_only", result["blockers"])
        self.assertEqual(result["execution"], {"training_started": False, "device": None})
        self.assertIn("checkpoint:fresh_byte_verification_required", result["blockers"])

    def test_changed_source_identity_and_conversion_counts_block(self):
        self.evidence["sources"]["train"]["annotation_sha256"] = "f" * 64
        self.evidence["conversions"]["validation"]["images"] = 1
        blockers = self.plan()["blockers"]
        self.assertIn("sources:identity_evidence", blockers)
        self.assertIn("conversion:validation:missing_or_inconsistent", blockers)

    def test_output_collisions_and_manifest_tampering(self):
        self.config["output_directory"] = str(self.directory)
        self.assertIn("execution:output_collision", self.plan()["blockers"])
        output = self.directory / "training_manifest.json"
        result = self.plan()
        write_training_manifest(output, result)
        self.assertEqual(json.loads(output.read_text()), result)
        with self.assertRaises(FileExistsError):
            write_training_manifest(output, result)
        for field, value in (("outputs", {"checkpoint_sha256": "a" * 64, "metrics": {}}),
                             ("execution", {"training_started": True, "device": "cpu"}),
                             ("status", "executed"), ("blockers", [])):
            with self.subTest(field=field):
                changed = deepcopy(result)
                changed[field] = value
                with self.assertRaises(ValueError):
                    write_training_manifest(self.directory / "tampered.json", changed)
                self.assertFalse((self.directory / "tampered.json").exists())

    def test_planning_preserves_inputs(self):
        before = deepcopy((self.config, self.evidence))
        result = self.plan()
        result["configuration"]["sources"].clear()
        result["evidence"].clear()
        self.assertEqual((self.config, self.evidence), before)

    def test_cli_default_and_execute_never_import_models_read_artifacts_or_dispatch(self):
        class NoModels(importlib.abc.MetaPathFinder):
            def find_spec(self, fullname, path=None, target=None):
                if fullname.split(".")[0] in {"torch", "torchvision", "ultralytics"}:
                    raise AssertionError("model package import attempted")
        finder = NoModels()
        sys.meta_path.insert(0, finder)
        self.addCleanup(sys.meta_path.remove, finder)
        main = runpy.run_path(str(ROOT / "scripts/finetune_yolov10.py"))["main"]
        with patch("subprocess.Popen", side_effect=AssertionError("process dispatch")), \
                patch("sdp_xray.training.inspect_training_sources",
                      side_effect=AssertionError("data audit attempted")), \
                patch("sdp_xray.training._sha256", side_effect=AssertionError("artifact access")):
            for argv in ([], ["--execute"], ["--output", str(self.directory / "plan.json")]):
                with self.subTest(argv=argv), redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(main(argv), 2)
                    result = json.loads(output.getvalue())
                    self.assertEqual(result["status"], "blocked")
                    self.assertFalse(result["training_started"])
        self.assertTrue((self.directory / "plan.json").exists())

    def test_cli_invalid_config_and_collision_have_sanitized_errors(self):
        main = runpy.run_path(str(ROOT / "scripts/finetune_yolov10.py"))["main"]
        path = self.directory / "config.json"
        path.write_text("[]")
        for argv in (["--config", str(path)], ["--output", str(path)]):
            with self.subTest(argv=argv), redirect_stdout(io.StringIO()) as output:
                self.assertEqual(main(argv), 2)
                self.assertEqual(json.loads(output.getvalue())["status"], "blocked")
                self.assertNotIn(str(self.directory), output.getvalue())
        self.assertEqual(path.read_text(), "[]")


class ConversionTests(unittest.TestCase):
    """These tests require the root project's Pillow dependency, never model packages."""
    def setUp(self):
        from PIL import Image

        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name)
        self.sources = {}
        for i, split in enumerate(SPLITS):
            root = self.directory / split
            root.mkdir()
            images = []
            for j in range(2):
                name = f"{split}-{j}.png"
                Image.new("RGB", (100, 80), (i * 60, j * 80, 70)).save(root / name)
                images.append({"id": j, "file_name": name, "width": 100, "height": 80,
                               "synthetic_group": f"{split}-{j}"})
            document = {"images": images, "categories": [{"id": 0, "name": "Explosive"}],
                        "annotations": [{"id": 0, "image_id": 0, "category_id": 0,
                                         "bbox": [10, 20, 30, 40], "iscrowd": 0}]}
            annotation = self.directory / f"{split}.json"
            annotation.write_text(json.dumps(document), encoding="utf-8")
            self.sources[split] = (annotation, root)
        self.path = self.sources["train"][0]

    def edit(self, change):
        document = json.loads(self.path.read_text())
        change(document)
        self.path.write_text(json.dumps(document), encoding="utf-8")

    def convert(self):
        return convert_coco(self.path, "author-yolov10m-generic")

    def test_zero_category_conversion_and_empty_image_preservation(self):
        before = {p: p.read_bytes() for p in self.directory.rglob("*") if p.is_file()}
        result = self.convert()
        self.assertEqual([float(v) for v in result["train-0.txt"].split()],
                         [0, 0.25, 0.5, 0.3, 0.5])
        self.assertEqual(result["train-1.txt"], "")
        self.assertEqual(before, {p: p.read_bytes() for p in self.directory.rglob("*") if p.is_file()})

    def test_invalid_geometry_is_rejected_without_repair(self):
        original = self.path.read_bytes()
        for box in ([-0.0001, 0, 1, 1], [0, 0, 100.00001, 1], [0, 0, 0, 1],
                    [0, 0, float("nan"), 1], [0, 0, 1e-50, 1]):
            with self.subTest(box=box):
                self.path.write_bytes(original)
                self.edit(lambda d: d["annotations"][0].update(bbox=box))
                invalid = self.path.read_bytes()
                with self.assertRaises(ValueError):
                    self.convert()
                self.assertEqual(self.path.read_bytes(), invalid)

    def test_crowd_segmentation_missing_iscrowd_and_unknown_fields_block(self):
        original = self.path.read_bytes()
        for change in (lambda a: a.update(iscrowd=1), lambda a: a.pop("iscrowd"),
                       lambda a: a.update(segmentation=[[1, 2, 3, 4, 5, 6]]),
                       lambda a: a.update(ignore=1)):
            with self.subTest(change=change):
                self.path.write_bytes(original)
                self.edit(lambda d: change(d["annotations"][0]))
                with self.assertRaises(ValueError):
                    self.convert()

    def test_duplicate_annotations_at_float32_precision_block(self):
        self.edit(lambda d: d["annotations"].append({**d["annotations"][0], "id": 1}))
        with self.assertRaisesRegex(ValueError, "duplicate label"):
            self.convert()
        self.edit(lambda d: d["annotations"][1].update(bbox=[10 + 1e-9, 20, 30, 40]))
        with self.assertRaisesRegex(ValueError, "duplicate label"):
            self.convert()

    def test_label_filename_collisions_block(self):
        self.edit(lambda d: d["images"][1].update(file_name="TRAIN-0.jpg"))
        with self.assertRaisesRegex(ValueError, "collision"):
            self.convert()

    def test_real_auditor_is_reused_and_incomplete_group_evidence_blocks(self):
        evidence = inspect_training_sources(self.sources, "author-yolov10m-generic")
        config = example_config()
        config.update(model_id="author-yolov10m-generic", sources=evidence["sources"])
        result = training_plan(config, evidence)
        self.assertTrue(any("physical_groups" in b for b in result["blockers"]))
        complete = inspect_training_sources(self.sources, "author-yolov10m-generic", "synthetic_group")
        result = training_plan(config, complete)
        self.assertFalse(any(b.startswith(("audit:", "conversion:")) for b in result["blockers"]))
        self.assertEqual(result["status"], "blocked")

    def test_exact_byte_duplicates_and_test_overlap_block(self):
        train_root = self.sources["train"][1]
        (train_root / "train-1.png").write_bytes((train_root / "train-0.png").read_bytes())
        test_root = self.sources["test"][1]
        (test_root / "test-0.png").write_bytes((train_root / "train-0.png").read_bytes())
        evidence = inspect_training_sources(self.sources, "author-yolov10m-generic", "synthetic_group")
        config = example_config()
        config.update(model_id="author-yolov10m-generic", sources=evidence["sources"])
        result = training_plan(config, evidence)
        self.assertIn("audit:train_test:overlap_evidence", result["blockers"])
        self.assertIn("audit:train_validation:train:image_evidence", result["blockers"])

    def test_empty_or_missing_validation_never_falls_back(self):
        sources = dict(self.sources)
        del sources["validation"]
        with self.assertRaisesRegex(ValueError, "explicit train"):
            inspect_training_sources(sources, "author-yolov10m-generic")
        document = json.loads(self.sources["validation"][0].read_text())
        document.update(images=[], annotations=[])
        self.sources["validation"][0].write_text(json.dumps(document))
        with self.assertRaisesRegex(ValueError, "empty image split"):
            inspect_training_sources(self.sources, "author-yolov10m-generic")


if __name__ == "__main__":
    unittest.main()
