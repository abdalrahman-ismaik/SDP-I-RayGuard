---
name: iedxray-data-audit
description: Inspect authorized IEDXray COCO annotations and images, category meanings, negatives, split overlap and physical-group provenance before conversion or training.
---

Use for IEDXray COCO audits or task-map changes; STCray uses its separate native audit below.
Inputs: authorized JSON/image paths, annotation task, published split provenance and any
verified physical-group field.
Paths below are relative to the repository root. Read `AGENTS.md`, `docs/status.md`, active
task, `data/README.md`, `docs/iedxray-audit.md` and `docs/research.md`.
For new distributed collection, inspect the lab format, approved taxonomy and case/group
provenance first; the published-data commands do not establish that protocol or its labels.

1. Inventory source/rights, file sizes/hashes and task-specific category IDs/names. Distinguish
   complete/device/generic/specific annotations; never invent IDs or host-to-region links.
2. Run `uv run --locked python -m sdp_xray.cli audit-coco` with the actual annotations,
   image roots and other split where available. Supply `--group-key` only for verified metadata.
   For the secondary STCray dataset, use `audit-stcray <extracted-parent>` instead: its native
   `Json_BB` files use per-image rectangles, not COCO. Do not assume folder numbers are class IDs.
3. Inspect counts, negatives, IDs/references, boxes and errors. Save JSON output under ignored
   `runs/<run_id>/`. Missing roots/group fields leave checks explicitly incomplete.
4. Inspect representative original images with task-specific overlays. A general ground-truth
   overlay CLI is not implemented; earlier private preview helpers are not shipped in this repo.
   Add a small reviewed renderer when needed; never call an unimplemented command or call
   ground truth a prediction.
5. Preserve test split; investigate duplicates and physical relationships. Do not infer physical
   independence from filenames. Keep original/counterfactual variants together.

Output: inventory, category map, actual audit report, reviewed overlays, split/group provenance
and unresolved fields. Verify with real files plus synthetic regression checks where code changes.
Stop dependent conversions/training on unresolved label mapping or invalid boxes; continue
independent inventory. No artifact access: record the exact blocker; do not download large data
under setup authority. Update `docs/tasks.md` and `docs/progress.md` with commands, evidence
and next action. Detailed private outputs/journals stay ignored and are not clone prerequisites.
