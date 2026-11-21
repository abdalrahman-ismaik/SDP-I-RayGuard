"""Evaluate saved shared run records against COCO ground truth (T42).

Runs no model. Reads a T40 record directory (run_manifest.json + predictions.jsonl), a COCO
ground-truth file and a frozen protocol, then writes one JSON report. Needs pycocotools:

  uv run --locked --with-requirements environments/evaluation.in \
    python scripts/evaluate_generic_yolov10.py evaluate --record runs/<record> \
    --ground-truth <binary_explosive_det_test.json> \
    --protocol configs/evaluation/generic-explosive-test.json --output runs/<report>.json

  ... compare --baseline runs/<baseline> --candidate runs/<candidate> (same other options)
  ... compare-candidates --untuned runs/<untuned> --tuned runs/<tuned> (same other options)

compare: supplied original checkpoint vs a model fine-tuned from it.
compare-candidates: two models trained from the same general starting weights.

Reports go under ignored runs/. A report from a draft protocol is not a project metric.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

from sdp_xray.baseline import MANIFEST_NAME, read_record
from sdp_xray.coco_metrics import coco_bbox_metrics, evaluator_version
from sdp_xray.evaluation import (
    build_report,
    check_ground_truth,
    check_protocol,
    coco_detections,
    dumps_report,
    matched_pair_differences,
    operating_point,
    validate_protocol,
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate_record(record: Path, ground_truth_path: Path, protocol: dict, allow_subset: bool):
    manifest, results = read_record(record)
    ground_truth = json.loads(ground_truth_path.read_text(encoding="utf-8"))
    gt_sha256 = _sha256(ground_truth_path)
    index = check_ground_truth(ground_truth, manifest["model"]["source_category_map"])
    check_protocol(protocol, manifest, index["summary"], gt_sha256)
    version = evaluator_version()
    if version != protocol["evaluator"]["version"]:
        raise ValueError(f"pycocotools {version} differs from protocol version")
    prepared = coco_detections(manifest, results, index, allow_subset=allow_subset)
    metrics = coco_bbox_metrics(ground_truth, prepared["detections"], prepared["image_ids"])
    point = operating_point(ground_truth, index, prepared["detections"], prepared["image_ids"],
                            protocol["operating_point"]["threshold"],
                            protocol["operating_point"]["iou"])
    report = build_report(protocol, index["summary"], gt_sha256, manifest,
                          _sha256(record / MANIFEST_NAME), version, prepared, metrics, point,
                          index)
    return manifest, report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    one = commands.add_parser("evaluate", help="evaluate one record")
    one.add_argument("--record", type=Path, required=True)
    pair = commands.add_parser("compare", help="evaluate a matched baseline/candidate pair")
    pair.add_argument("--baseline", type=Path, required=True)
    pair.add_argument("--candidate", type=Path, required=True)
    tuned = commands.add_parser("compare-candidates",
                                help="evaluate untuned vs tuned models from the same start")
    tuned.add_argument("--untuned", type=Path, required=True)
    tuned.add_argument("--tuned", type=Path, required=True)
    for command in (one, pair, tuned):
        command.add_argument("--ground-truth", type=Path, required=True)
        command.add_argument("--protocol", type=Path, required=True)
        command.add_argument("--output", type=Path, required=True)
        command.add_argument("--allow-subset", action="store_true",
                             help="permit a labelled subset (missing or failed scans)")
    args = parser.parse_args(argv)

    if args.output.exists():
        parser.error("output already exists; reports are never overwritten")
    try:
        protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
        validate_protocol(protocol)
        if args.command == "evaluate":
            _, report = evaluate_record(args.record, args.ground_truth, protocol,
                                        args.allow_subset)
            text = dumps_report(report)
        else:
            if args.command == "compare":
                mode, names = "baseline_vs_candidate", ("baseline", "candidate")
                paths = (args.baseline, args.candidate)
            else:
                mode, names = "untuned_vs_tuned", ("untuned", "tuned")
                paths = (args.untuned, args.tuned)
            first, _ = read_record(paths[0])
            second, _ = read_record(paths[1])
            problems = matched_pair_differences(first, second, mode)
            if problems:
                raise ValueError("not a matched pair: " + "; ".join(problems))
            _, first_report = evaluate_record(paths[0], args.ground_truth, protocol,
                                              args.allow_subset)
            _, second_report = evaluate_record(paths[1], args.ground_truth, protocol,
                                               args.allow_subset)
            # Differences are reported as numbers only; no "better/worse" verdict here.
            difference = {
                name: (None if value is None or second_report["metrics"][name] is None
                       else second_report["metrics"][name] - value)
                for name, value in first_report["metrics"].items()
            }
            text = json.dumps({
                "schema_version": "1.0", "comparison": mode,
                names[0]: json.loads(dumps_report(first_report)),
                names[1]: json.loads(dumps_report(second_report)),
                f"{names[1]}_minus_{names[0]}": difference,
            }, allow_nan=False, sort_keys=True, indent=2)
    except (OSError, ValueError, KeyError) as error:
        print(json.dumps({"status": "error", "message": str(error)}), file=sys.stderr)
        return 2

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text + "\n", encoding="utf-8")
    summary = json.loads(text)
    first = summary.get("baseline") or summary.get("untuned") or summary
    print(json.dumps({"status": "ok", "output": args.output.name,
                      "evidence": first["evidence"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
