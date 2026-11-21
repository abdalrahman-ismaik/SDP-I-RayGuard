"""T41 planning CLI. No data/model access, dependency installation, or training."""

import argparse
import json
import re
from pathlib import Path

from sdp_xray.training import training_plan, write_training_manifest

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "configs/finetune.example.json")
    parser.add_argument("--evidence", type=Path, help="Previously produced, sanitized CPU evidence JSON")
    parser.add_argument("--output", type=Path, help="New training manifest file; parent must exist")
    parser.add_argument("--task", choices=("generic", "specific"), help="Explicit research task")
    parser.add_argument("--execute", action="store_true", help="Always blocked in this software draft")
    args = parser.parse_args(argv)
    try:
        config = json.loads(args.config.read_text(encoding="utf-8-sig"))
        if args.task:
            if config.get("schema_version") != "t41-research-1":
                raise ValueError("--task requires research configuration")
            config["task"] = args.task
        evidence = json.loads(args.evidence.read_text(encoding="utf-8-sig")) if args.evidence else None
        missing = []
        plan = "docs/single-scan-ml-pipeline-plan-2026-11.md"
        research = config.get("schema_version") == "t41-research-1"
        if not research and not (ROOT / plan).is_file():
            missing.append(plan)
        tasks = ROOT / "docs/tasks.md"
        if not research and (not tasks.is_file() or not re.search(
            r"\|\s*T41\s*\|", tasks.read_text(encoding="utf-8")
        )):
            missing.append("docs/tasks.md:T41")
        manifest = training_plan(config, evidence, tuple(missing))
        if args.output:
            write_training_manifest(args.output, manifest)
        print(json.dumps({"status": "blocked", "training_started": False,
                          "execution_requested": args.execute, "blockers": manifest["blockers"]}))
    except (OSError, UnicodeError, ValueError, TypeError, KeyError, AttributeError):
        # Do not echo exception strings that could contain private paths or input.
        print(json.dumps({"status": "blocked", "training_started": False,
                          "blockers": ["unreadable_or_invalid_input_or_output_collision"]}))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
