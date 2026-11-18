# Single-scan model baseline and fine-tuning plan

**Updated 18 November 2026 — coordinator-prepared student handoff; implementation remains with the task owners.** The owner confirms HPC access and CVMI Lab provision of the models/resources. The agreed research aim is supplied-checkpoint evaluation reproduction, author-training reproduction where settings can be recovered, and a controlled Optuna improvement study on public IEDXray. Generic explosives first, specific explosives second; 20 attempted configurations per task. No new training/evaluation or student contribution is inferred.

The [detailed fine-tuning protocol](finetuning.md) and [HPC handoff](hpc-training.md) govern the new experimental design. They supersede this document's earlier generic-only draft scope, access-as-unavailable wording, and assumption that supplied task weights can initialize an unseen train-derived validation experiment. Faisal owns baseline/shared contracts, Ahmed training/Optuna/Slurm, Ali independent evaluation; Abd and Mohammad review app/report integration. Proposed ownership still needs each student's acceptance. The six core T41 paths are confirmed as a coherent file boundary, with the owner reporting Faisal's non-overlap confirmation.

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
- Use the public IEDXray release as the proposed single-scan data source and the same owner-identified CVMI model already selected for the GUI as the initial baseline. The owner confirms CVMI Lab provision; the historical renewed author link records checkpoint acquisition history. Preserve both descriptions without claiming publisher byte identity. Record source, task and SHA-256 before training/comparison. The local record verifies a generic YOLOv10-M checkpoint but not that the current GUI config points to that exact file. IEDXray's public release is the proposed dataset; local `Train`, `Test` and annotation directories exist outside Git. The audit records 12,224 train / 5,136 test images and generic category ID 0 `Explosive`; resolve filenames through the COCO image table, with boxes `[x,y,width,height]` in original pixels.

### Data and validation blockers

The existing [IEDXray audit](iedxray-audit.md) found four exact image-byte pairs crossing the supplied train/test split, five generic-threat train box-boundary violations, and additional duplicate pairs within each split. The original published split must remain intact; do not silently move/remove images, clip boxes, or rewrite labels. The supplied local archive checksum is unavailable, and the generic checkpoint's complete training-data/config provenance is not established.

No verified physical-group field or independent validation set is currently recorded; the owner selected fresh general pretrained initialization and a fixed training-only validation partition for the controlled study. A random carve-out from training images is not automatically unseen validation, especially for a checkpoint whose training provenance is incomplete. Implementation can proceed through preflight, interfaces and software checks; dependent real runs require the documented validation and duplicate policy. Access itself is confirmed, not a blocker. If an exploratory result is later approved, label the known split/data limitations alongside it.

The dismantled collection's 478 distinct byte payloads count toward documented collection progress and its own dismantled-threat workstream. They are not inputs for the single-scan prototype's training, baseline demo or accuracy evaluation: reviewed detector labels, QC acceptance and verified physical/case grouping are not established. Keep the two evidence tracks separate in the report.

## Proposed work split for Faisal, Ahmed and Ali

These assignments are proposed by the project owner and are not evidence that any student has accepted or completed them. Confirm each student's exact roster name/GitHub account and available time before claiming contribution. Brainstorm shared contracts together, then own separate file sets and use private AI sessions for bounded review. No raw scans, credentials, private paths, filled manifests or session files go to GitHub or AI prompts.

### T40 — Faisal: baseline adapter and run contract

**Goal:** make supplied-checkpoint reproduction and fresh-initialization comparison traceable through the shared contracts, while coordinating the confirmed HPC access and backend qualification with Ahmed. Use explicit generic and specific research task identities; the GUI saved preference does not choose the research task.

Proposed deliverables:

1. Verify each research checkpoint source/hash, task/class map, original-pixel box convention, upstream revision, preprocessing and environment against the existing inference evidence. Generic and specific tasks retain separate records; GUI model selection is an integration concern, not a research prerequisite.
2. Define the shared input, prediction and run-manifest contract with Ahmed and Ali. Predictions must retain confidence, explicit source category namespace and original-image `xyxy` coordinates.
3. Connect the existing inference path to batch-one invocation and the agreed manifest/evaluator handoff with the smallest justified adapter. Keep model dependencies in the separately locked model environment.
4. Use the owner-confirmed HPC access and inspected manuals; qualify the backend/allocation privately; never put credentials in Git or an AI prompt. A real run occurs only with an approved input, assigned owner/output directory and confirmed task pairing.
5. Record whether the proposal's preprocessing/ROI stages are implemented, inherited from the checkpoint, or still absent. Do not describe direct detector boxes as a completed independent segmentation/feature-analysis stage.

Suggested scope is an owned adapter/manifest/test file set, not a second trainer or evaluator. Synthetic checks are software evidence only; a real baseline statement requires an executed and reviewed run.

### T41 — Ahmed: training, Optuna and HPC execution

Own the six core paths requested in the handoff: `src/sdp_xray/training.py`,
`scripts/finetune_yolov10.py`, `configs/finetune.example.json`,
`tests/test_training.py`, `environments/training/README.md`, and `docs/finetuning.md`.
The coordinator has prepared the latter as the protocol; Ahmed continues it with
implementation evidence. Additional Optuna/Slurm helpers are T41 extensions whose
file ownership must be recorded before editing. Faisal's shared manifest, baseline
adapter and CLI, and Ali's evaluation files are excluded.

Implement the [protocol](finetuning.md): fail-closed preflight, fixed training-only
group partition, general pretrained initialization excluding IEDXray, one-run
training/config/provenance, separate qualified environment, sequential resumable
Optuna studies, trial export and scheduler templates. Generic first, specific
second; 20 attempted trials/task, bounded confirmations and matched seeds.
Use Ali's validation metric interface and Faisal's existing candidate handoff.
Training records and shared prediction manifests have different purposes.

Real training follows documented data/validation policy and an allocated GPU
smoke/pilot. HPC access is confirmed; backend/environment compatibility, available
job allocation and actual results still need execution evidence. Ahmed/Ali review
label conversion/leakage independently; Faisal reviews provenance/interfaces.

### T42 — Ali: reproduction and independent matched evaluation

**Goal:** implement supplied-checkpoint reproduction and independent matched baseline-versus-Optuna evaluation for generic then specific explosives. Supply Ahmed a validation-objective interface. Use the research task identity independently of the GUI saved selection; preserve the published test split. Follow [the detailed protocol](finetuning.md).

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

1. Confirm the three owners/handles and agree the image, prediction and manifest contracts. Verify supplied research checkpoints and fresh initialization source/hash/task pairing; use the public IEDXray release as the single-scan dataset source.
2. Faisal maps the baseline to the shared contract and checks HPC prerequisites; no credentials enter AI prompts or Git.
3. Ahmed and Ali jointly resolve T03/T10/Q5/Q9 data and validation blockers with the advisor/model owner. Drafts can proceed; real training and final test interpretation wait for an approved policy.
4. Implement the baseline adapter, train preflight/config and evaluator on separate owned files/branches. Cross-review interfaces, run required code checks, and merge small increments.
5. Only after data, checkpoint, environment, validation, compute and output-directory gates pass, run one owned bounded pilot. Inspect logs/weights and sample predictions manually.
6. Freeze model and threshold choices before final test comparison. Run baseline and fine-tuned candidates under the same eligible protocol once; report metrics, errors, latency and data limits.
7. Integrate a working vertical slice: authorized image intake, declared preprocessing, verified inference, result display/review and run-linked record. Rehearse on the presentation machine. Present multi-image work separately until labels and grouping are accepted.

The training and evaluation code can be a substantial student contribution even if data gates prevent a valid final metric before the deadline. An honest blocked result is stronger assessment evidence than an unsupported number. Owners, hours, training runs, metrics and acceptance remain unreported until the students and reviewers supply evidence.
