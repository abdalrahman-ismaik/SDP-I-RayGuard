"""Synthetic checks of the pycocotools wrapper and evaluation script (T42).

Skipped unless pycocotools is installed (environments/evaluation.in). These prove that the
software calls the official evaluator correctly on tiny fixtures, not model accuracy.
"""

import importlib.util
import json
from pathlib import Path

import pytest
from test_evaluation import ground_truth, manifest, protocol, result, results

from sdp_xray.baseline import write_record
from sdp_xray.coco_metrics import coco_bbox_metrics, evaluator_version

# coco_metrics imports pycocotools only when called, so the imports above are safe.
pytest.importorskip("pycocotools")

SCRIPT = Path(__file__).parents[1] / "scripts" / "evaluate_generic_yolov10.py"


def _script():
    spec = importlib.util.spec_from_file_location("evaluate_generic_yolov10", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_perfect_predictions_with_category_zero_score_one():
    truth = ground_truth()
    detections = [{"image_id": a["image_id"], "category_id": 0, "bbox": a["bbox"], "score": 0.9}
                  for a in truth["annotations"]]
    metrics = coco_bbox_metrics(truth, detections, [10, 11, 12])
    assert metrics["AP@[.50:.95]"] == pytest.approx(1.0)
    assert metrics["AP50"] == pytest.approx(1.0)
    assert metrics["AR@100"] == pytest.approx(1.0)
    # No large ground-truth boxes exist in the fixture: undefined, not zero.
    assert metrics["AP_large"] is None


def test_no_predictions_scores_zero_not_error():
    metrics = coco_bbox_metrics(ground_truth(), [], [10, 11, 12])
    assert metrics["AP@[.50:.95]"] == 0.0
    assert metrics["AR@100"] == 0.0


def test_one_of_two_boxes_found_gives_half_recall():
    truth = ground_truth()
    detections = [{"image_id": 10, "category_id": 0, "bbox": [10, 10, 20, 20], "score": 0.9}]
    metrics = coco_bbox_metrics(truth, detections, [10, 11, 12])
    assert metrics["AR@100"] == pytest.approx(0.5)
    assert metrics["AP50"] == pytest.approx(0.5, abs=0.01)


def test_ground_truth_is_not_modified():
    truth = ground_truth()
    before = json.dumps(truth, sort_keys=True)
    coco_bbox_metrics(truth, [], [10, 11, 12])
    assert json.dumps(truth, sort_keys=True) == before


def _write(tmp_path, name, record, items):
    write_record(tmp_path / name, record, items)
    return tmp_path / name


def _files(tmp_path):
    (tmp_path / "gt.json").write_text(json.dumps(ground_truth()), encoding="utf-8")
    value = protocol()
    value["evaluator"]["version"] = evaluator_version()
    (tmp_path / "protocol.json").write_text(json.dumps(value), encoding="utf-8")
    return ["--ground-truth", str(tmp_path / "gt.json"),
            "--protocol", str(tmp_path / "protocol.json")]


def test_script_evaluates_a_saved_record(tmp_path, capsys):
    record = _write(tmp_path, "baseline", manifest(), results())
    code = _script().main(["evaluate", "--record", str(record), *_files(tmp_path),
                           "--output", str(tmp_path / "report.json")])
    assert code == 0
    report = json.loads((tmp_path / "report.json").read_text(encoding="utf-8"))
    assert report["evidence"] == "draft-protocol"
    assert report["operating_point"]["true_positives"] == 1
    assert report["coverage"]["evaluated_images"] == 3
    assert str(tmp_path) not in json.dumps(report)
    assert json.loads(capsys.readouterr().out)["status"] == "ok"


def test_script_refuses_overwrite_and_gui_threshold_record(tmp_path):
    args = _files(tmp_path)
    gui = manifest(conf=0.25)
    record = _write(tmp_path, "gui", gui, results(gui))
    assert _script().main(["evaluate", "--record", str(record), *args,
                           "--output", str(tmp_path / "r.json")]) == 2
    assert not (tmp_path / "r.json").exists()
    (tmp_path / "r.json").write_text("{}", encoding="utf-8")
    with pytest.raises(SystemExit):
        _script().main(["evaluate", "--record", str(record), *args,
                        "--output", str(tmp_path / "r.json")])


def test_script_compares_only_matched_pairs(tmp_path):
    args = _files(tmp_path)
    baseline = _write(tmp_path, "baseline", manifest(), results())
    cand = manifest(role="candidate", checkpoint="b" * 64, parent="a" * 64)
    items = results(cand)
    items[2] = result("Test000003", [([50, 40, 80, 60], 0.7)], cand)
    candidate = _write(tmp_path, "candidate", cand, items)
    out = tmp_path / "compare.json"
    assert _script().main(["compare", "--baseline", str(baseline), "--candidate",
                           str(candidate), *args, "--output", str(out)]) == 0
    compared = json.loads(out.read_text(encoding="utf-8"))
    assert compared["candidate_minus_baseline"]["AR@100"] == pytest.approx(0.5)
    assert "better" not in json.dumps(compared) and "improv" not in json.dumps(compared)

    assert compared["comparison"] == "baseline_vs_candidate"

    unmatched = manifest(role="candidate", checkpoint="b" * 64, parent="c" * 64)
    other = _write(tmp_path, "unmatched", unmatched, results(unmatched))
    assert _script().main(["compare", "--baseline", str(baseline), "--candidate", str(other),
                           *args, "--output", str(tmp_path / "no.json")]) == 2
    assert not (tmp_path / "no.json").exists()


def test_script_compares_untuned_and_tuned_from_same_start(tmp_path):
    args = _files(tmp_path)
    start = "d" * 64
    untuned = manifest(role="candidate", checkpoint="b" * 64, parent=start)
    tuned = manifest(role="candidate", checkpoint="c" * 64, parent=start)
    items = results(tuned)
    items[2] = result("Test000003", [([50, 40, 80, 60], 0.7)], tuned)
    first = _write(tmp_path, "untuned", untuned, results(untuned))
    second = _write(tmp_path, "tuned", tuned, items)
    out = tmp_path / "tuning.json"
    assert _script().main(["compare-candidates", "--untuned", str(first), "--tuned",
                           str(second), *args, "--output", str(out)]) == 0
    compared = json.loads(out.read_text(encoding="utf-8"))
    assert compared["comparison"] == "untuned_vs_tuned"
    assert compared["tuned_minus_untuned"]["AR@100"] == pytest.approx(0.5)
    # A supplied baseline is not accepted in this mode.
    baseline = _write(tmp_path, "baseline", manifest(), results())
    assert _script().main(["compare-candidates", "--untuned", str(baseline), "--tuned",
                           str(second), *args, "--output", str(tmp_path / "x.json")]) == 2
