"""Allocation boundaries and storage retention use synthetic artifacts only."""

import hashlib
import json
import socket
from copy import deepcopy
from types import SimpleNamespace
from unittest.mock import patch

import pytest
from test_training_backend import FakeBoundEvaluator, FakeUpstreamTrainer, prepared_case
from test_training_research import init_receipt
from test_training_workflow import StageTrainer
from test_tuning import FakeEvaluator, FakeSampler, FakeTrainer, definition

from sdp_xray.training_backend import (
    CheckpointValidationAdapter,
    YoloTrainerAdapter,
    _retain_checkpoints,
)
from sdp_xray.training_workflow import (
    deadline_confirmation_plan,
    deadline_protocol,
    experiment_identity,
    offline_runtime,
    run_stage,
    verify_search_runtime,
)
from sdp_xray.tuning import confirmation_plan, run_synthetic_study


def test_whole_attempt_allocations_preserve_sampler_sequence(tmp_path):
    expected = run_synthetic_study(definition(), tmp_path / "continuous", FakeSampler(),
                                   FakeTrainer(), FakeEvaluator(), attempt_limit=3)
    first = run_synthetic_study(definition(), tmp_path / "chunked", FakeSampler(),
                                FakeTrainer(), FakeEvaluator(), attempt_limit=1)
    assert first["attempted_configurations"] == 1
    assert first["trials"][0]["status"] == "complete"
    assert len(first["trials"][0]["reports"]) == 30
    resumed_trainer = FakeTrainer()
    resumed = run_synthetic_study(definition(), tmp_path / "chunked", FakeSampler(),
                                  resumed_trainer, FakeEvaluator(), resume=True, attempt_limit=2)
    assert resumed["trials"] == expected["trials"]
    assert [call["number"] for call in resumed_trainer.calls] == [1, 2]
    assert all(call["completed_epochs"] == 0 and call["resume_checkpoint"] is None
               for call in resumed_trainer.calls)


@pytest.mark.parametrize("limit", [0, 21, True, 1.5])
def test_invalid_allocation_limit_never_creates_output(tmp_path, limit):
    output = tmp_path / "invalid"
    with pytest.raises(ValueError, match="allocation attempt limit"):
        run_synthetic_study(definition(), output, FakeSampler(), FakeTrainer(), FakeEvaluator(),
                            attempt_limit=limit)
    assert not output.exists()


def test_retention_keeps_ap_best_and_latest_across_study_allocations(tmp_path):
    _, _, weights, bundle, study_definition = prepared_case(tmp_path)
    root = tmp_path / "retained-study"
    def trainer():
        return YoloTrainerAdapter(FakeUpstreamTrainer, weights, bundle,
                                  checkpoint_retention="best_validation_and_latest")
    first = run_synthetic_study(study_definition, root, FakeSampler(), trainer(),
                                CheckpointValidationAdapter(FakeBoundEvaluator()), attempt_limit=1)
    row = first["trials"][0]
    assert len(row["reports"]) == 30 and row["value"] == 0.8
    assert row["best_checkpoint"]["path"].endswith("epoch-002.pt")
    snapshots = (root / row["best_checkpoint"]["path"]).parent
    assert {p.name for p in snapshots.glob("*.pt")} == {"epoch-002.pt", "epoch-030.pt"}
    retired = [item for p in snapshots.glob("retention-*-completed.json")
               for item in json.loads(p.read_text())["removed"]]
    assert len(retired) == 28 and all(len(item["sha256"]) == 64 for item in retired)
    second = run_synthetic_study(study_definition, root, FakeSampler(), trainer(),
                                 CheckpointValidationAdapter(FakeBoundEvaluator()),
                                 resume=True, attempt_limit=1)
    assert second["attempted_configurations"] == 2
    assert second["trials"][0] == row


def test_changed_snapshot_blocks_retention_before_any_removal(tmp_path):
    identities = {}
    for name in ("epoch-001.pt", "epoch-002.pt", "epoch-003.pt"):
        path = tmp_path / name
        path.write_bytes(name.encode())
        identities[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    (tmp_path / "epoch-003.pt").write_bytes(b"changed")
    with pytest.raises(ValueError, match="identity changed"):
        _retain_checkpoints(tmp_path, identities, {"epoch-001.pt", "epoch-003.pt"}, 3)
    assert (tmp_path / "epoch-002.pt").is_file()
    assert not list(tmp_path.glob("retention-*.json"))


def test_confirmation_allocation_runs_only_a_declared_full_length_run(tmp_path):
    exported = run_synthetic_study(definition(), tmp_path / "search", FakeSampler(),
                                   FakeTrainer(), FakeEvaluator(), attempt_limit=3)
    selected = confirmation_plan(exported)[1]
    trainer = StageTrainer()
    result = run_stage(exported, "confirmation", tmp_path / "confirmation", trainer,
                       FakeEvaluator(), {"17": init_receipt()},
                       output_keys=[selected["output_key"]])
    assert len(trainer.calls) == len(result["results"]) == 1
    assert trainer.calls[0]["epochs"] == 100 and trainer.calls[0]["seed"] == 17
    assert result["results"][0]["status"] == "complete"
    assert result["results"][0]["source_trial"] == selected["source_trial"]
    with pytest.raises(ValueError, match="declared stage runs"):
        run_stage(exported, "confirmation", tmp_path / "invalid-confirmation", trainer,
                   FakeEvaluator(), {"17": init_receipt()}, output_keys=["unplanned"])
    assert not (tmp_path / "invalid-confirmation").exists()


@pytest.mark.skipif(not hasattr(socket, "AF_UNIX"), reason="Unix IPC socket family unavailable")
def test_offline_guard_allows_worker_ipc_but_blocks_ip_networks(tmp_path):
    local, ipv4, ipv6 = (SimpleNamespace(family=f) for f in (socket.AF_UNIX, socket.AF_INET, socket.AF_INET6))
    with patch.object(socket.socket, "connect", return_value=None) as connect, \
            patch.object(socket.socket, "connect_ex", return_value=0) as connect_ex:
        with offline_runtime(tmp_path / "settings"):
            assert socket.socket.connect(local, "/synthetic/worker.sock") is None
            assert socket.socket.connect_ex(local, "/synthetic/worker.sock") == 0
            for remote in (ipv4, ipv6):
                with pytest.raises(OSError, match="network dispatch"):
                    socket.socket.connect(remote, ("127.0.0.1", 80))
                with pytest.raises(OSError, match="network dispatch"):
                    socket.socket.connect_ex(remote, ("127.0.0.1", 80))
        connect.assert_called_once_with(local, "/synthetic/worker.sock")
        connect_ex.assert_called_once_with(local, "/synthetic/worker.sock")


def amendment_case(tmp_path):
    def bound(path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value))
        return {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    before = {"implementation_sha256": "a" * 64, "python_version": "3.12.16",
              "packages": {"torch": "synthetic"},
              "runtime_files": [{"path": "/synthetic/bridge.py", "sha256": "a" * 64}],
              "evaluator": {"file": "/synthetic/evaluator.py", "factory": "create", "sha256": "c" * 64}}
    after = deepcopy(before)
    after["implementation_sha256"] = "b" * 64
    after["runtime_files"][0]["sha256"] = "b" * 64
    receipt = {"schema_version": "t41-first-failure-amendment-1", "reason": "Synthetic repair fixture only",
               "authorization": {"decision": "approved", "owner": "synthetic", "reference": "fixture"},
               "original_identity": before, "replacement_identity": after,
               "changed_files": [{"path": "/synthetic/bridge.py", "before": "a" * 64, "after": "b" * 64}],
               "failed_boundary": bound(tmp_path / "allocations/000/workflow-result.json",
                                         {"attempted_configurations": 1,
                                          "trials": [{"number": 0, "status": "failed", "value": None}]}),
               "qualification": bound(tmp_path / "qualification.json",
                                       {"implementation_sha256": "b" * 64, "status": "passed",
                                        "all_detections_retained": True, "untouched_predictions_equal": True,
                                        "ali_evaluator_unchanged": True})}
    return before, after, receipt, bound


def test_runtime_repair_requires_bound_evidence_and_preserves_original_result(tmp_path):
    before, after, receipt, bound = amendment_case(tmp_path)
    failure = (tmp_path / "allocations/000/workflow-result.json").read_bytes()
    entry = bound(tmp_path / "amendment.json", receipt)
    verify_search_runtime(before, before, None, tmp_path)
    with pytest.raises(ValueError, match="without a bound"):
        verify_search_runtime(before, after, None, tmp_path)
    verify_search_runtime(before, after, entry, tmp_path)
    assert (tmp_path / "allocations/000/workflow-result.json").read_bytes() == failure
    after["implementation_sha256"] = "d" * 64
    with pytest.raises(ValueError, match="does not match"):
        verify_search_runtime(before, after, entry, tmp_path)


@pytest.mark.parametrize("change", ["complete", "pruned", "attempt_count", "boundary_path",
                                    "unlisted_file", "qualification", "package", "no_authorization"])
def test_runtime_amendment_rejects_mixed_or_unqualified_history(tmp_path, change):
    before, after, receipt, bound = amendment_case(tmp_path)
    if change in ("complete", "pruned", "attempt_count", "boundary_path"):
        prior = {"attempted_configurations": 2 if change == "attempt_count" else 1,
                 "trials": [{"number": 0, "status": change if change in ("complete", "pruned") else "failed",
                             "value": None}]}
        path = tmp_path / ("other.json" if change == "boundary_path" else "allocations/000/workflow-result.json")
        receipt["failed_boundary"] = bound(path, prior)
    elif change == "unlisted_file":
        receipt["changed_files"] = []
    elif change == "qualification":
        receipt["qualification"] = bound(tmp_path / "qualification.json", {"status": "failed"})
    elif change == "package":
        after["packages"]["torch"] = "changed"
    else:
        receipt["authorization"]["decision"] = "pending"
    with pytest.raises(ValueError):
        verify_search_runtime(before, after, bound(tmp_path / "amendment.json", receipt), tmp_path)


@pytest.mark.parametrize("change", [None, "missing_authorization", "attempts", "specific", "repeatability", "identity"])
def test_deadline_scope_requires_exact_authorized_generic_protocol(tmp_path, change):
    config = definition()["configuration"]
    receipt = {"schema_version": "t41-deadline-protocol-1", "experiment_sha256": experiment_identity(config),
               "authorization": {"decision": "approved", "owner": "synthetic", "reference": "fixture"},
               "terms": {"task": "generic", "attempted_configurations": 6, "search_epochs": 30,
                         "confirmation": "best_completed_and_control", "confirmation_epochs": 100,
                         "seeds": [17], "deferred": ["specific", "repeatability"]}}
    if change == "missing_authorization":
        receipt["authorization"] = None
    elif change == "attempts":
        receipt["terms"]["attempted_configurations"] = 7
    elif change == "specific":
        config["task"] = "specific"
    elif change == "identity":
        receipt["experiment_sha256"] = "0" * 64
    path = tmp_path / "deadline.json"
    path.write_text(json.dumps(receipt))
    entry = {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    if change is None:
        assert deadline_protocol(entry, config, "search") == receipt
        assert deadline_protocol(None, config, "search") is None
    else:
        with pytest.raises(ValueError, match="generic-only"):
            deadline_protocol(entry, config, "repeatability" if change == "repeatability" else "search")


def test_deadline_confirmation_includes_failed_control_and_only_best_completed_candidate():
    rows = [{"number": n, "status": "failed" if n == 0 else "complete",
             "value": None if n == 0 else 0.4 + n / 100, "parameters": {"fixture": n}} for n in range(6)]
    rows[4]["value"] = rows[5]["value"]
    selected = deadline_confirmation_plan({"trials": rows, "definition_sha256": "a" * 64})
    assert [r["source_trial"] for r in selected] == [0, 4]
    assert all(r["epochs"] == 100 and r["seed"] == 17 for r in selected)
    assert deadline_confirmation_plan({"trials": [rows[0]]}) == []
