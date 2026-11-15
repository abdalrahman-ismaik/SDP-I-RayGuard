"""Evaluate saved shared run records against COCO ground truth (T42).

Runs no model. Reads a T40 record directory (run_manifest.json + predictions.jsonl), a COCO
ground-truth file and a frozen protocol, then writes one JSON report. Needs pycocotools:

  uv run --locked --with-requirements environments/evaluation.in \
    python scripts/evaluate_generic_yolov10.py evaluate --record runs/<record> \
    --ground-truth <binary_explosive_det_test.json> \
    --protocol configs/evaluation/generic-explosive-test.json --output runs/<report>.json

  ... compare --baseline runs/<baseline> --candidate runs/<candidate> (same other options)

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
    for command in (one, pair):
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
            baseline, _ = read_record(args.baseline)
            candidate, _ = read_record(args.candidate)
            problems = matched_pair_differences(baseline, candidate)
            if problems:
                raise ValueError("not a matched pair: " + "; ".join(problems))
            _, base_report = evaluate_record(args.baseline, args.ground_truth, protocol,
                                             args.allow_subset)
            _, cand_report = evaluate_record(args.candidate, args.ground_truth, protocol,
                                             args.allow_subset)
            # Differences are reported as numbers only; no "better/worse" verdict here.
            difference = {
                name: (None if base is None or cand_report["metrics"][name] is None
                       else cand_report["metrics"][name] - base)
                for name, base in base_report["metrics"].items()
            }
            text = json.dumps({"schema_version": "1.0", "baseline": json.loads(
                dumps_report(base_report)), "candidate": json.loads(dumps_report(cand_report)),
                "candidate_minus_baseline": difference}, allow_nan=False, sort_keys=True,
                indent=2)
    except (OSError, ValueError, KeyError) as error:
        print(json.dumps({"status": "error", "message": str(error)}), file=sys.stderr)
        return 2

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text + "\n", encoding="utf-8")
    summary = json.loads(text)
    print(json.dumps({"status": "ok", "output": args.output.name,
                      "evidence": summary.get("evidence") or summary["baseline"]["evidence"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
