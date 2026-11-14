# Single-scan model baseline and fine-tuning plan

**Status: requirements and artifacts verified; three complementary ML work packages proposed; no training run started.** The immediate aim is a first integrated prototype draft that can be defended against the original project proposal. Faisal owns the verified baseline/run interface, Ahmed the fine-tuning candidate, and Ali the independent evaluation candidate. They should compare compatible components through shared contracts, then integrate only reviewed work with evidence; three separate end-to-end pipelines would waste the short schedule and create integration risk.

## Requirement check

| Source | Requirement/finding | Effect on this work |
|---|---|---|
| Proposal / Meeting 01, retained P1 scope and A8 | Develop a single-scan explosive/IED detection pipeline; preprocess, detect, train or fine-tune, test/evaluate on unseen data, and document it. | Fine-tuning and evaluation are real project requirements. A GUI or single-image smoke run alone does not complete P1. |
| Meeting 02, D6 and A9 | Adapt and retrain the available model rather than build the multi-package model from zero; adapt/train/test/document after usable Batch 1. Inspect model access early. | Use a verified existing model as the initialization. The meeting did not identify its checkpoint/config/class map, validation split or metrics; verify rather than assume. |
| Meeting 02, D1/A10 and M01 distributed scope | Separately collect components across multiple packages, then broaden collection and retrain. | Multi-image/case-level detection is a different workstream. Do not relabel the single-image generic checkpoint as a multi-image model. |
| Detection-evaluation workflow and handbook report rubric | A report's results/evaluation section is assessed; methods and limitations must be explained. | Build a baseline-versus-fine-tuned evaluation path with a frozen test protocol and honest limitations. |

The historical 8/15 October prototype dates and 15 October Batch 1 milestone remain unreconciled in T10/Q9. This plan does not silently waive them. The proposed implementation sprint is for report/demo evidence by the November deadlines, not a claim that the earlier full P1/P2 obligations are complete.

## What is actually available now

### Checkpoint inventory

The three files below exist in the local ignored `data/IEDXray/model-weights/` directory. `git ls-files` found no tracked checkpoint/model-weight files; the checkpoints are not in the public repository. The generic checkpoint's current SHA-256 matches [the recorded inference artifact](first-inference.md).

| Local task checkpoint | Size | SHA-256 | Appropriate current role |
|---|---:|---|---|
| `yolov10_generic_exp.pt` | 33,482,415 bytes | `b484d9a6fb37236f6adcc8c019e6a836f11901dc53a0f71d6cce7262413287ff` | Single-image generic explosive detector; use as the proposed baseline/initialization after verifying training provenance |
| `yolov10_device_detection.pt` | 33,482,479 bytes | `8106dc79234473def8335e863585623f2c0de17e57a6b6c0a7d1c61bf2691f2d` | Per-image device detector; separate four-class task |
| `yolov10_specific_exp.pt` | 33,496,111 bytes | `4464ad8a9c02d550b79fe616ea1c39869f5f9c2e604025ef3dd9de4f544f0172` | Per-image five-class specific-explosive detector; separate task |

These are the three inspected YOLOv10-M tasks. They are **not** multi-image fusion checkpoints. Other inspected checkpoint families are unavailable locally or have unresolved task/backend mappings.

### Existing baseline and code

- `docs/first-inference.md` records an executed generic YOLOv10-M CPU smoke using the original THU-MIG fork at commit `453c6e38a51e9d1d5a2aa5fb7f1014a711913397`, model class `Explosive` at source category ID 0, image size 640 and batch one. The generic input/checkpoint pairing is verified.
- The smoke used three images. It retained a miss on an annotated modified-laptop test image, one positive training-image output, and one annotation-empty ordinary-laptop output. These are diagnostic examples, not dataset metrics or benign decisions.
- The checkpoint stores an author mAP@[.50:.95] value of 0.34517. The paper reports 35.1% for YOLOv10-M generic detection. Neither is a metric measured by this project. No project full-test AP, AP50, AR, per-image failure analysis or end-to-end benchmark is recorded.
- `scripts/infer_generic_yolov10.py` implements single-image inference and saves real predictions/overlay/manifest. The P1 `predict()` and P2 `fuse()` modules remain stubs. No training/fine-tuning entry point, dataset training adapter or COCO metric evaluation script was found under `scripts/`, `src/` or `tests/`.
- The managed profiles in `environments/` pin the inference fork/dependencies. Their README explicitly says training/export extras are not installed. The root project lock is CPU audit tooling. Fine-tuning needs a separately inspected and locked training environment; do not add Torch/training dependencies to the root CPU lock or assume the inference lock can train.
- Use the public IEDXray release as the proposed single-scan data source and the same owner-identified CVMI model already selected for the GUI as the initial baseline. The owner identifies it as CVMI-provided; existing artifact records describe the local weights as author-supplied after a renewed link, so reconcile that provenance against the exact GUI-configured file before citing it. Record source, task and SHA-256 before training/comparison. The local record verifies a generic YOLOv10-M checkpoint but not that the current GUI config points to that exact file. IEDXray's public release is the proposed dataset; local `Train`, `Test` and annotation directories exist outside Git. The audit records 12,224 train / 5,136 test images and generic category ID 0 `Explosive`; resolve filenames through the COCO image table, with boxes `[x,y,width,height]` in original pixels.

### Data and validation blockers

The existing [IEDXray audit](iedxray-audit.md) found four exact image-byte pairs crossing the supplied train/test split, five generic-threat train box-boundary violations, and additional duplicate pairs within each split. The original published split must remain intact; do not silently move/remove images, clip boxes, or rewrite labels. The supplied local archive checksum is unavailable, and the generic checkpoint's complete training-data/config provenance is not established.

No verified physical-group field or independent validation set is currently recorded. A random carve-out from training images is not automatically unseen validation, especially for a checkpoint whose training provenance is incomplete. Until the model/data owners approve a validation and duplicate policy, code can implement preflight and the pipeline scaffold, but a tuned “strong” final metric is blocked. If an exploratory result is later approved, label the known split/data limitations alongside it.

The dismantled collection's 478 distinct byte payloads count toward documented collection progress and its own dismantled-threat workstream. They are not inputs for the single-scan prototype's training, baseline demo or accuracy evaluation: reviewed detector labels, QC acceptance and verified physical/case grouping are not established. Keep the two evidence tracks separate in the report.

## Proposed work split for Faisal, Ahmed and Ali

These assignments are proposed by the project owner and are not evidence that any student has accepted or completed them. Confirm each student's exact roster name/GitHub account and available time before claiming contribution. Brainstorm shared contracts together, then own separate file sets and use private AI sessions for bounded review. No raw scans, credentials, private paths, filled manifests or session files go to GitHub or AI prompts.

### T40 — Faisal: baseline adapter and run contract

**Goal:** make the exact task-matched checkpoint already selected in the GUI the reproducible starting path for the integrated prototype, while coordinating (not assuming) CS-HPC readiness. The current records support generic YOLOv10-M as the expected pairing; confirm the GUI's local configured hash before implementation.

Proposed deliverables:

1. Verify the GUI-configured checkpoint's source/hash, task/class map, original-pixel box convention, upstream revision, preprocessing and environment against existing inference evidence. If the config selects generic YOLOv10-M, reuse its recorded pairing; if not, stop and resolve the task-matched adapter before code.
2. Define the shared input, prediction and run-manifest contract with Ahmed and Ali. Predictions must retain confidence, explicit source category namespace and original-image `xyxy` coordinates.
3. Connect the existing inference path to batch-one invocation and the agreed manifest/evaluator handoff with the smallest justified adapter. Keep model dependencies in the separately locked model environment.
4. Prepare the HPC prerequisites from the supplied manuals. Verify access privately; never put credentials in Git or an AI prompt. A real run occurs only with an approved input, assigned owner/output directory and confirmed task pairing.
5. Record whether the proposal's preprocessing/ROI stages are implemented, inherited from the checkpoint, or still absent. Do not describe direct detector boxes as a completed independent segmentation/feature-analysis stage.

Suggested scope is an owned adapter/manifest/test file set, not a second trainer or evaluator. Synthetic checks are software evidence only; a real baseline statement requires an executed and reviewed run.

### T41 — Ahmed: training/fine-tuning pipeline draft

**Goal:** implement a small, reproducible generic-explosive training path around the verified `yolov10_generic_exp.pt` checkpoint and the exact upstream fork. Start with a written design decision record and data preflight, then code the smallest usable runner.

Proposed deliverables:

1. **Model/data pairing note:** verified GUI checkpoint hash/source; fork commit; source task/class ID 0 `Explosive` if that generic checkpoint is confirmed; public IEDXray image-table/path resolution; coordinate conversion from COCO `xywh`; preprocessing actually applied; data license/provenance; unresolved training-data/checkpoint history.
2. **Fail-closed data preflight:** validate required JSON/image references, source category map, image decode, box bounds and split identity. Report the known duplicates/box findings; never auto-fix them. Require a reviewed policy before training on or evaluating affected records.
3. **Training config/CLI:** initialize from the existing generic checkpoint, pin all choices (seed, optimizer/schedule, image size, epochs/early-stop, augmentation, batch, precision and save points) in a versioned config/manifest. Values must come from inspected author artifacts or a documented student/advisor decision, not AI guesses.
4. **Separate training environment:** inspect what the original fork supports at the pinned commit and create a training-specific lock/profile only if compatible and feasible. Do not alter `pyproject.toml`/`uv.lock` CPU dependencies or reuse an inference lock without proof.
5. **Synthetic software checks:** exercise config validation, path resolution, class mapping, split guard and manifest creation with tiny generated fixtures. These tests prove software behavior, not detector quality.
6. **Run gate:** a batch-one training/forward smoke or short pilot is permitted only after checkpoint/task verification, the data policy, validation plan, compute owner/output directory and supervisor/team scope are agreed. No long training job is implied by this draft.

Suggested owned files, after checking for conflicts: a new `scripts/train_generic_yolov10.py`, a focused training config under `configs/`, training-specific environment files under `environments/`, and matching synthetic tests under `tests/`. Do not place weights, data, predictions or run outputs in Git.

### T42 — Ali: independent baseline/fine-tuned evaluation pipeline

**Goal:** implement a reproducible, independent evaluator for the verified GUI-selected single-scan task, then compare the frozen original checkpoint with an approved fine-tuned/same-task candidate on the same untouched public test split.

Proposed deliverables:

1. **Evaluation protocol decision record:** exact GUI checkpoint/hash, task/class mapping, IEDXray split hashes, approved duplicate/boundary policy, official evaluator/version, score floor/max detections, coordinate convention, frozen operating point, and which choices are validation-only. State unresolved gates explicitly.
2. **Full-split prediction export:** run the pinned model on the selected split, resolve `file_name` through COCO, convert model predictions to the evaluator's required original-pixel format, retain confidence and model/run identity, and save a private manifest. Do not feed annotations into inference.
3. **Official detection metrics:** use the verified COCO bounding-box evaluator for the one-class generic task. Report AP@[.50:.95], AP50 and AR; also report precision/recall and false-positive/miss examples at a threshold frozen using acceptable validation evidence. Keep annotation-empty images described as annotation-empty, not “benign.”
4. **Failure and timing report:** review misses/false positives and box/score behavior. Measure model latency separately from total pipeline latency, recording hardware, backend, precision, batch, warm-up/synchronization and timing boundaries. Do not claim stable p50/p95 from too few samples.
5. **Matched comparison:** compare original checkpoint and fine-tuned checkpoint with identical preprocessing, class map, evaluator and untouched test files. Keep any threshold selection or model selection out of test results.
6. **Synthetic software checks:** test category/path mapping, coordinate conversion, empty predictions, invalid boxes, evaluator input and report serialization using fixtures. They do not establish real-data accuracy.

Suggested owned files, after checking for conflicts: a new `scripts/evaluate_generic_yolov10.py`, focused evaluation functions and synthetic tests, plus `docs/single-scan-evaluation-protocol.md`. Save full predictions and per-image outputs under ignored `runs/`; share only reviewed aggregate findings and material limitations.

### Joint design session

Faisal, Ahmed and Ali should use one short design session before implementation to agree:

- One image input contract, a shared run-manifest schema and unique run ID linking baseline inference, training config/checkpoint, evaluation metrics and output hashes.
- The boundary between baseline inference, training and evaluation code, including the exact prediction interface and original-image coordinate convention.
- Whether they can implement code while real-data runs remain blocked; the proposed answer is yes for preflight, interfaces and synthetic tests, but no accuracy claims or long jobs.
- A written status for the four cross-split duplicates, five generic train boundary findings, checkpoint training provenance and lack of a verified validation split.
- Review order: Ali reviews Ahmed's data/split guards; Ahmed reviews Ali's evaluator/coordinate mapping; Faisal reviews shared inference/manifest integration. Each student explains their own changes and evidence.

The three ML lanes are complementary parts of one prototype, not three competing end-to-end stacks. The existing generic, device and specific-explosive checkpoints represent different class tasks, so they are not interchangeable generic-explosive candidates. Each student may propose alternatives on paper; implement alternatives only where a real uncertainty exists and they can be compared fairly under one protocol.

## Private AI-assisted student workflow

Students may give their own AI tool the task ID, public project docs and an approved file list, then request a requirements map, design critique, draft or review. Keep prompts and transcripts in the student's private session. Do not supply credentials, raw scans, private paths or filled manifests. The agent may edit agreed working files but must not set Git identity, stage, commit, push, create a PR/review or add an agent identity. It may suggest commands; the student personally inspects and runs them under their own GitHub account. Follow [human-only GitHub authorship](../CONTRIBUTING.md#human-only-github-authorship-and-git-operations).

## Evidence expected for report, demo and marking

| Report/presentation claim | Evidence required | Safe wording before that evidence exists |
|---|---|---|
| Existing single-scan detector works | Executed model/checkpoint pairing, exact task/class map, real prediction/overlay/run manifest | “Generic YOLOv10-M smoke inference was executed on three examples; one annotated test miss is retained.” |
| Strong single-scan baseline | Full eligible test evaluation with verified task map, frozen evaluator/protocol, checkpoint hash, split policy and failure analysis | “A full-dataset baseline is planned; current project metrics are not available.” |
| Fine-tuned model improves baseline | Approved training/validation protocol, reproducible training manifest, matched evaluation and an untouched eligible test set | “Fine-tuning pipeline is in development; improvement has not been measured.” |
| Multi-image dismantled detector works | Reviewed component labels, case/physical grouping, scanner/session provenance, QC and case-disjoint evaluation | “The collection inventory is available; labels/group links and multi-image model evaluation are not yet established.” |

Do not substitute the paper's 35.1%, checkpoint-stored 0.34517, synthetic test results or image counts for local model performance. The first two can be cited only as published/checkpoint metadata with their evidence labels.

## Suggested completion sequence

1. Confirm the three owners/handles and agree the image, prediction and manifest contracts. Resolve the exact GUI-configured CVMI checkpoint/source/hash and verify its task pairing; use the public IEDXray release as the single-scan dataset source.
2. Faisal maps the baseline to the shared contract and checks HPC prerequisites; no credentials enter AI prompts or Git.
3. Ahmed and Ali jointly resolve T03/T10/Q5/Q9 data and validation blockers with the advisor/model owner. Drafts can proceed; real training and final test interpretation wait for an approved policy.
4. Implement the baseline adapter, train preflight/config and evaluator on separate owned files/branches. Cross-review interfaces, run required code checks, and merge small increments.
5. Only after data, checkpoint, environment, validation, compute and output-directory gates pass, run one owned bounded pilot. Inspect logs/weights and sample predictions manually.
6. Freeze model and threshold choices before final test comparison. Run baseline and fine-tuned candidates under the same eligible protocol once; report metrics, errors, latency and data limits.
7. Integrate a working vertical slice: authorized image intake, declared preprocessing, verified inference, result display/review and run-linked record. Rehearse on the presentation machine. Present multi-image work separately until labels and grouping are accepted.

The training and evaluation code can be a substantial student contribution even if data gates prevent a valid final metric before the deadline. An honest blocked result is stronger assessment evidence than an unsupported number. Owners, hours, training runs, metrics and acceptance remain unreported until the students and reviewers supply evidence.
