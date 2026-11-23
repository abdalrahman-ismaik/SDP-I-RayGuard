"""T41 study planning/export and separately authorized workflow execution."""

import argparse
import json
from pathlib import Path

from sdp_xray.training import write_training_manifest
from sdp_xray.training_research import research_plan
from sdp_xray.training_workflow import add_execution_arguments, dispatch_cli
from sdp_xray.tuning import StudyLedger, export_study

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "configs/finetune.example.json")
    parser.add_argument("--evidence", type=Path, help="Sanitized, previously produced evidence JSON")
    parser.add_argument("--task", choices=("generic", "specific"))
    parser.add_argument("--output", type=Path, help="New planning manifest or export; never overwrite")
    add_execution_arguments(parser)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--resume-from", type=Path, help="Check stored configuration; do not resume work")
    action.add_argument("--export-from", type=Path, help="Export a closed study ledger with its execution label")
    args = parser.parse_args(argv)
    try:
        if args.export_from:
            if args.execute or not args.output:
                raise ValueError("export requires a new output and cannot execute")
            exported = export_study(args.export_from, args.output)
            print(json.dumps({"status": "exported", "training_started": exported["training_started"],
                              "execution_kind": exported["execution_kind"],
                              "attempted_configurations": exported["attempted_configurations"]}))
            return 0
        config = json.loads(args.config.read_text(encoding="utf-8-sig"))
        if args.task:
            config["task"] = args.task
        evidence = json.loads(args.evidence.read_text(encoding="utf-8-sig")) if args.evidence else None
        manifest = research_plan(config, evidence)
        if args.resume_from:
            if args.execute:
                raise ValueError("CLI resume is inspection only; checkpoint continuation is not qualified")
            definition = json.loads((args.resume_from / "study.json").read_text(encoding="utf-8"))
            if definition["configuration"] != config:
                raise ValueError("resume configuration differs")
            StudyLedger(args.resume_from, definition, resume=True).load()
        if args.output:
            write_training_manifest(args.output, manifest)
        return dispatch_cli(manifest, args)
    except (OSError, UnicodeError, ValueError, TypeError, KeyError, AttributeError):
        # No private paths, receipt contents or raw exception strings in console output.
        print(json.dumps({"status": "blocked", "training_started": False,
                          "blockers": ["unreadable_invalid_or_blocked_request"]}))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
