"""Check, then clamp, the tiny out-of-image training boxes into a derived copy (T41/T42).

Reads one COCO training annotation file and never writes to it. Writes two new files:
the derived annotations and a change record. Refuses test files, any overshoot of 0.001 px
or more, a count other than --expected, and existing outputs.

  uv run --locked python scripts/repair_train_boxes.py check --annotations <train.json>
  uv run --locked python scripts/repair_train_boxes.py repair --annotations <train.json> \
      --expected 5 --output-dir runs/<derived-annotations>

Keep outputs under ignored runs/. See docs/single-scan-data-policy.md#invalid-boxes.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

from sdp_xray.box_repair import find_overshoots, repair_training_copy, verify_training_source


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check", help="list boxes outside the image; change nothing")
    check.add_argument("--verify-training-source", action="store_true",
                       help="also require the exact verified published training export")
    repair = commands.add_parser("repair", help="write a derived training-only copy")
    for command in (check, repair):
        command.add_argument("--annotations", type=Path, required=True)
    repair.add_argument("--expected", type=int, required=True)
    repair.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)

    try:
        source = args.annotations.read_bytes()
        document = json.loads(source)
        if args.command == "check":
            split = (verify_training_source(document, hashlib.sha256(source).hexdigest())
                     if args.verify_training_source else None)
            found = find_overshoots(document)
            print(json.dumps({"status": "ok", "file": args.annotations.name,
                              "verified_source": split,
                              "boxes_outside_image": len(found), "boxes": found}, indent=2))
            return 0
        if args.output_dir.exists():
            raise ValueError("output directory already exists; outputs are never overwritten")
        derived, record = repair_training_copy(document, args.annotations.name,
                                               hashlib.sha256(source).hexdigest(), args.expected)
    except (OSError, ValueError) as error:
        print(json.dumps({"status": "error", "message": str(error)}), file=sys.stderr)
        return 2

    args.output_dir.mkdir(parents=True)
    name = args.annotations.stem + ".derived.json"
    (args.output_dir / name).write_text(json.dumps(derived), encoding="utf-8")
    record["derived_file_name"] = name
    (args.output_dir / "repair-record.json").write_text(
        json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": "ok", "changed_boxes": len(record["changes"]),
                      "output": [name, "repair-record.json"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
