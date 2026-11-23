# Preserved T41 draft and verification history — 17 November 2026

This is the prior local document, retained without deleting its API examples or verification history. The research workflow now follows [the current guide](finetuning.md). Earlier GUI prerequisites, generic-parent intent, universal physical-group gates, Windows-first environment proposal and missing-November-document statements below apply to that historical draft, not the new research design. The legacy Python helpers remain supported. Test results below are historical, not current verification.

# T41 single-scan fine-tuning software draft

Updated 17 November 2026. This extends the existing candidate-record helper with
CPU planning, strict conversion checks and a separate training manifest. There is
**no training dispatch**. `--execute` always returns blocked, including when a
configuration claims approvals. No real scans or checkpoints were opened for this
draft. Training settings remain outside the shared inference schema.

## Explain the draft in three steps

1. Select a model explicitly and collect evidence: exact GUI identity, public
   source hashes, complete audits and human policy decisions. A recorded hash or
   an auditor's `ok` alone cannot clear training.
2. Check that every original label can be represented without loss. Map source
   category IDs to catalog output indices and convert pixel `xywh` to normalized
   center `xywh`. Preserve every image, including annotation-empty images.
3. Save a planning manifest listing unresolved gates. After separately authorized
   future execution, use the existing strict candidate inference-record helper to
   retain the actual new weight hash, parent hash and original task/maps.

## Files and usage

| File | Purpose |
|---|---|
| `src/sdp_xray/training.py` | Planning gates, auditor adapter, in-memory conversion and candidate record helpers |
| `scripts/finetune_yolov10.py` | Planning CLI; reads config/evidence only and cannot launch training |
| `configs/finetune.example.json` | Unset model, hyperparameters, policies, owner and output; only the supplied parent intent and documented upstream revision are recorded |
| `tests/test_training.py` | Synthetic checks; no models or real scans |
| [Training environment proposal](../environments/training/README.md) | Pinned upstream training/save/reload inspection and qualification gates |

With the locked CPU tools available, from the repository root:

```text
uv run --locked python scripts/finetune_yolov10.py
uv run --locked python scripts/finetune_yolov10.py --config configs/finetune.example.json --output runs/<existing-private-run-directory>/training_manifest.json
```

Both are planning operations and return exit code **2 / blocked**. No output file
is created without `--output`; its parent must already exist, and the file must
not exist. `--evidence` accepts previously produced, sanitized audit JSON. The CLI
does not inspect scans, checkpoints or local GUI settings. It prints gate codes,
not source paths or raw exception messages. Malformed input and output collisions
also block. Keep generated manifests/private configs under ignored storage.

The configuration's `output_directory` describes a proposed future training run;
it is separate from the optional planning-manifest file. It must be a new directory
with an assigned human owner. Creating a planning file grants no execution approval.

## Exact model/data pairing remains unconfirmed

The catalog and [first inference record](first-inference.md) document these pairs:

| Explicit catalog ID | COCO annotation prefix | Source IDs to output indices | Task / kind |
|---|---|---|---|
| `author-yolov10m-generic` | `binary_explosive_det` | 0 to 0: Explosive | `iedxray.generic_explosive_detection` / `suspicious_region` |
| `author-yolov10m-device` | `device_detection` | 1 to 0: Laptop; 2 to 1: Mobile; 3 to 2: Pager; 4 to 3: Walkie-Talkie | `iedxray.device_detection` / `device` |
| `author-yolov10m-specific` | `specific_explosive_det` | 1 to 0: IED Explosive; 2 to 1: Laptop Explosive; 3 to 2: Mobile Phone Explosive; 4 to 3: Pager Explosive; 5 to 4: Walkie-Talkie Explosive | `iedxray.specific_explosive_detection` / `suspicious_region` |

The supplied intended parent hash below matches the recorded generic catalog hash.
It does **not** confirm the effective GUI selection. Provide a sanitized identity
confirmation containing model ID, task, kind, checkpoint hash/source and both class
maps, with a confirming owner and source reference. Do not provide settings files,
private paths or scans. If selection differs from the supplied parent, resolve that
conflict explicitly; the planner does not change the parent or selection silently.
Checkpoint hashes in the catalog are recorded evidence, not freshly verified here.

`gui_confirmation` contains `model`, `confirmed_by`, and `source_reference`.
`model` must equal the planner's catalog-derived `model` object (including
`recorded_checkpoint_sha256`, class-map hash and string-keyed maps). This checks
consistency of a human-supplied statement; it does not inspect GUI state.

## Evidence gates and conversion boundary

`inspect_training_sources(sources, model_id, group_key)` is a read-only Python
adapter around the existing COCO auditor. Its sources map contains exactly
`train`, `validation`, `test`, each as `(annotation_path, image_root)`. It does
not choose a split. It computes annotation and image-inventory hashes, checks
conversion, and audits all three split pairs. **Only synthetic fixtures were
attempted in this task; real use requires separate authorization.** The CLI never
calls this adapter. Errors stop conversion; no partial label output is written.

The returned `sources`, `conversions`, `audits` object can later be supplied as
evidence; config `sources` must match its three identities. Each identity has
`annotation_sha256` and `image_inventory_sha256`. The latter hashes canonical JSON
of sorted `(image_id, file_name, image_sha256)` rows, with compact separators.
These are snapshot identities, not proof of publication origin or membership in
an untouched published training set. Source preservation/membership must also be
reviewed against the originals; this draft does not create or certify subsets.

Preflight requires nonempty splits, complete image decoding/dimensions/hash
coverage, matching class maps, complete verified physical-group metadata and no
unresolved auditor errors/warnings. Missing duplicate/group/overlap checks block
even when `ok` is true. All pairwise filename, physical-group and exact-byte
overlap findings and all within-split duplicates block. No fabricated group key,
automatic deduplication, repaired geometry or policy bypass is implemented.

`convert_coco` reads annotations and returns a dictionary of label-file names to
text **in memory**. It never copies images or writes labels/YAML. It reuses the
auditor's strict geometry checks and requires exact catalog IDs/names, including
ID **0**. It rejects crowd annotations, missing `iscrowd`, nonempty segmentation,
unknown annotation fields, unsupported image extensions, colliding label paths,
float32 duplicate labels and boxes that lose their size at float32 precision.
Empty image labels remain empty strings, without calling the image benign. It
does not use the upstream COCO converter or subtract one from IDs.

The current validation design schema only represents an explicitly reviewed
`published_train_subset`, with a `membership_reference`,
`independent_of_author_checkpoint: false`, and `test_used_for_tuning: false`.
This records possible author-checkpoint exposure; it does not establish unseen or
physically independent validation, or approve it for tuning. Missing validation,
empty validation, train-as-validation and test-as-validation all block. Another
validation design needs an explicit reviewed extension. No split is generated.
A future trainer dataset YAML must contain explicit nonempty train/val and omit
test, because the pinned upstream trainer otherwise falls back to test.

## Separate training manifest

`training_plan` records schema `t41-training-draft-1`, the supplied configuration,
catalog identity, evidence, missing documents and blocker codes. Status remains
`blocked`, `training_started` is false, actual device is null, and output hash and
metrics are null. Fresh checkpoint verification is always an outstanding gate;
the planner never pretends that supplied hashes were computed by it.

Approvals remain null until supplied by the responsible humans. Each approval
receipt needs `decision: "approved"`, `owner`, and `reference`, covering data,
source identity, annotations, duplicates, groups, validation, environment and
scope. Receipts are recorded claims, not authenticated approvals or a switch that
enables execution. Environment evidence separately needs the exact revision,
lock hash and train/save/reload qualification reference. Small config parameters
are explicit proposals only; eventual execution must record all effective upstream
defaults and transforms, not just these five fields.

`write_training_manifest` recomputes the plan to reject inconsistent model/gate/
output claims, uses exclusive file creation, and cannot overwrite existing work.
This file is distinct from the strict inference `run_manifest.json`. It is not a
completed-run record and must not be passed to the shared inference validator.

## Remaining inputs before real work

- Supply `docs/single-scan-ml-pipeline-plan-2026-11.md` and the November T41 backlog/
  ownership entry (local `docs/tasks.md` contains T07 but no T41). No branch was
  switched or fetched. The older October prototype/collection deadline conflict
  remains unresolved in the local documents; no replacement date is invented.
- Confirm the effective GUI identity and parent source, then separately authorize
  fresh byte verification. Author training revision/YAML and publisher byte identity
  are not established by existing inference evidence.
- Approve public IEDXray source identity and policies for the recorded invalid
  boxes, cross/within-split duplicates, Mobile/Pager disagreements where relevant,
  missing physical provenance, and a defensible validation design. The published
  test split and original annotations stay untouched. Current historical audit
  findings do not pass these conservative gates; acknowledgments alone do not
  repair the findings or authorize a cleanup.
- Approve the separate environment and qualification task, bounded settings,
  compute budget, named human owner and new output directory. A future execution
  implementation/review is also required; this draft has no model import or
  dispatch path. Dismantled scans and HPC submission are outside this workstream.

## Agreed baseline and output fields

The intended parent is the catalog entry `author-yolov10m-generic`, with recorded
SHA-256 `b484d9a6fb37236f6adcc8c019e6a836f11901dc53a0f71d6cce7262413287ff`.
This records the supplied baseline identity, not the current GUI selection or
a new verification of the original checkpoint bytes.

`sdp_xray.training.candidate_manifest` retains its original generic-parent default
for this specific handoff. Another confirmed catalog pairing requires an explicit
`model_id=` argument in both candidate helpers; there is no GUI-default inference.
It validates the supplied baseline against that pairing, reads the candidate checkpoint only to calculate its
SHA-256, and sets:

| Field | Source |
|---|---|
| `role` | `"candidate"` |
| `model.checkpoint_sha256` | SHA-256 calculated from the supplied new checkpoint file |
| `model.parent_checkpoint_sha256` | Original baseline checkpoint hash above |
| `model.task`, `model.kind`, `model.model_names`, `model.source_category_map` | Preserved from the checked baseline |
| `model.id`, `model.class_map_sha256` | Preserved from the checked baseline |
| `requested_device` | Required actual candidate-run metadata; never inherited from the baseline |
| `device` | Separately supplied actual inference device; may be null only when every scan failed |
| `status` | `"error"` if any scan failed, otherwise `"ok"` |

The source category map remains `{"0": "Explosive"}`; source category ID zero is
valid. Output boxes remain original-image pixel `xyxy`, as required by the
[shared contract](baseline-run-contract.md). No conversion or relabelling happens here.

The helper calls the existing `validate_run_manifest` and
`validate_prediction_set` checks. Predictions must already contain the candidate
checkpoint hash, matching run ID, inputs, task and threshold. Baseline predictions
are rejected instead of being relabelled as candidate output. Boxes and scores are
preserved. Empty successful detections do not establish a benign scan.

## Use after an authorized training and inference run

No fine-tuned checkpoint or genuine candidate predictions exist as a result of
this implementation. The following is integration guidance for later actual runs:

```python
from pathlib import Path

from sdp_xray.baseline import read_record
from sdp_xray.training import write_candidate_record

baseline, _ = read_record(Path("runs/<baseline-record>"))

# These variables must come from the actual candidate inference run.
run_metadata = {
    "run_id": candidate_run_id,
    "timestamp_utc": recorded_timestamp_utc,
    "code": recorded_code_provenance,
    "settings": actual_inference_settings,
    "stages": actual_stage_records,
    "requested_device": requested_device,
    "device": actual_device,
    "precision": actual_precision,
    "inputs": actual_input_hash_records,
    "limitations": actual_limitations,
}

manifest = write_candidate_record(
    Path("runs/<new-candidate-record>"),
    baseline,
    Path("runs/<approved-training-run>/weights/best.pt"),
    run_metadata,
    candidate_scan_results,
)
```

The caller supplies completed scan results and sanitized metadata, including code
revision/dirty state from the human owner. The helper invokes no Git command and
imports no model library. It never runs the existing inference script.

Run metadata uses exactly the fields shown above; the helper supplies
`schema_version`, `role`, `status` and `model`. Do not copy the baseline's
execution metadata or put epochs, learning rates or planned statuses here.
Both the baseline manifest and candidate metadata must conform to the unchanged
[shared contract](baseline-run-contract.md).

`write_candidate_record` reuses the existing record writer to create
`run_manifest.json` and `predictions.jsonl` in a new directory. It validates
before creating that directory and refuses to overwrite an existing directory.
The candidate checkpoint path is not added to either record. Callers remain
responsible for supplying metadata without private paths or credentials.

## Validation and remaining limits

The new tests use invented metadata, boxes and byte files clearly marked
synthetic. They cover hash ancestry, category zero, required requested device,
failed scans, stale predictions, changed checkpoints, schema restrictions,
record round trips and preservation of existing output.

Run the required CPU lint and test checks in the locked audit environment when
available. The full pytest suite currently includes
`tests/test_model_catalog.py::test_wrong_task_checkpoint_is_rejected_before_importing_model_packages`,
which launches the prohibited inference runner. The following explicitly excludes
that test and must be reported as a **partial suite**, not a complete suite:

```text
uv run --locked ruff check .
uv run --locked python -m pytest --deselect tests/test_model_catalog.py::test_wrong_task_checkpoint_is_rejected_before_importing_model_packages
```

A dependency-free check of candidate records and planning is also available;
this selects two classes and does not exercise Pillow-dependent conversion:

```text
python -B -c "import sys, unittest; sys.path[:0] = ['src', 'tests']; unittest.main(module=None, argv=['unittest', 'test_training.CandidateManifestTests', 'test_training.PlanningTests', '-v'])"
```

Hashing does not deserialize or validate a checkpoint, prove it was trained,
prove its ancestry, or prove predictions actually came from that file. Those
claims require separate training/inference evidence. A candidate record alone
does not establish a matched baseline evaluation; settings, stages and input
hashes must also match under the shared comparison protocol.

Real pipeline execution, approved validation design, data-policy resolutions,
GUI identity confirmation, training environment qualification and named run
owner/output directory remain blocked. No training, model smoke test, real-scan
access, checkpoint download, HPC job or accuracy measurement occurred.

Historical manifest-helper verification on 15 November 2026: the locked Ruff command passed. The
permitted locked pytest command above reported **203 passed, 9 skipped and 1
deselected**; the skips were existing Windows symlink tests without the required
privilege, and the deselected test launches the prohibited inference runner. All
17 new candidate-manifest tests also passed independently through unittest. CPU
verification used a temporary isolated environment; the root dependency files
were unchanged. These results establish software behavior only.

## Current verification: 17 November 2026

These are fresh results for this expanded draft, not reused November 15 counts.

| Command/check | Actual outcome |
|---|---|
| `uv run --locked ruff check .` | Could not start: `uv` is not available in this session; shell exit 1. Lint remains unverified. |
| `uv run --locked python -m pytest` | Could not start for the same reason; shell exit 1. No full-suite result. Independently, the runner-launching test identified above conflicts with the current execution restriction. |
| Candidate/planning unittest command below | 33 tests passed, exit 0; includes all 17 original candidate tests and the explicit other-task extension. |
| Full T41 unittest discovery below | 41 tests attempted: 33 passed, 8 setup errors because `PIL` is unavailable; exit 1. No skips/deselections. Conversion/auditor integration remains unverified in this session. |
| Default CLI command below | Reported `blocked`, `training_started: false`; exit 2. Wrote no output file. |
| Python AST / JSON parsing | All three Python files and the example JSON parsed successfully. This is not a replacement for Ruff. |
| Local documentation links | No broken local links in these two documentation files. |

Exact test and default CLI commands:

```text
python -B -c "import sys, unittest; sys.path[:0] = ['src', 'tests']; unittest.main(module=None, argv=['unittest', 'test_training.CandidateManifestTests', 'test_training.PlanningTests', '-v'])"
python -B -c "import sys, unittest; sys.path.insert(0, 'src'); unittest.main(module=None, argv=['unittest', 'discover', '-s', 'tests', '-p', 'test_training.py'])"
python -B -c "import sys, runpy; sys.path.insert(0, 'src'); runpy.run_path('scripts/finetune_yolov10.py', run_name='__main__')"
```

The current interpreter also lacks pytest and Ruff. A temporary isolated CPU
tooling environment was created with `python -m venv <temporary-tooling-directory>`.
An attempted `<temporary-tooling-python> -m pip --isolated install uv --index-url
https://pypi.org/simple --disable-pip-version-check` failed with DNS resolution
error `getaddrinfo failed`; no CPU packages were installed. The temporary paths
are deliberately omitted from this shared record. No model dependencies were
installed and root dependency files were not edited. Restore the locked CPU tools
and run the complete T41 tests and the explicitly permitted repository checks
before accepting conversion behavior. Do not call the earlier successful locked
checks current verification.

Factual progress-note material: extended the existing candidate-record handoff
within the six authorized files; added a blocked-by-default planner, catalog-based
COCO conversion checks, separate training manifest and pinned-source environment
proposal. Current tests: 33 pass; eight conversion/auditor checks cannot run without
Pillow. Lint/full pytest remain unavailable. November planning/backlog, GUI identity,
data/validation decisions and training qualification remain open. No real data,
model execution, Git actions or shared-interface/progress-file edits occurred.
Software tests do not establish model quality.

Follow-up tooling recovery on 17 November: uv **0.13.8** was recovered from a
cached Windows wheel and installed with `pip --isolated install --no-index
--no-deps <cached-uv-wheel>` into the temporary CPU tooling environment. The
cached Pillow wheel is **12.2.0 / CPython 3.10**, incompatible with this session's
CPython 3.12.10 and different from the locked Pillow 12.3.0; it was not installed.
The locked Ruff check was retried through the temporary uv executable, with
`UV_PROJECT_ENVIRONMENT` and `UV_CACHE_DIR` pointing to temporary directories,
`UV_PYTHON_DOWNLOADS=never`, and `UV_NO_CONFIG=1`. With `UV_OFFLINE=1`, it failed
because Ruff 0.16.8 was not cached (exit 1). A normal network retry with
`UV_HTTP_TIMEOUT=10` and `UV_HTTP_RETRIES=0` failed resolving
`files.pythonhosted.org` while fetching Pluggy (OS error 11001, exit 2).
Thus uv itself is recovered, but locked dependencies, lint and the eight
Pillow-dependent checks remain blocked. No new test success is claimed from
these tooling retries; the 33/8 results above are unchanged.
