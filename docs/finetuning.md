# IEDXray reproduction and Optuna improvement protocol

**21 November implementation handoff:** the protocol below remains the coordinator's
agreed research brief. Ahmed's branch `ahmed/t41-software-draft` at `32091bc` now
contains planning/partition/provenance and synthetic orchestration software plus a
Slurm template; its CLIs block live execution. Faisal's PR #21 supplies starting-weight
provenance/receipt, and Ali's PR #18 at `6dfa7d6` implements the safeguards, validation objective and common-parent comparison; re-review/integration remain pending.
See the [current integration sequence](plan.md#latest-team-integration-review--21-november)
and T40–T42. No trainer/backend qualification or real study is verified. Reconcile
Ahmed's branch-local same-named guide with this protocol during human PR review,
preserving actual implementation history rather than overwriting either record.

Updated 18 November 2026. **Planning and student handoff only.** No trainer,
Optuna integration, Slurm launcher, training environment, new run or result is
implemented or verified by this update. The sole backlog is [tasks](tasks.md).
This protocol refines T40–T42 in the [single-scan plan](single-scan-ml-pipeline-plan-2026-11.md).

## Aim, evidence and success criteria

**Owner direction:** reproduce the paper's results, then attempt to improve them
on the same public IEDXray dataset. Run generic explosives first, specific
explosives second. Use Optuna and the available HPC. The owner confirms access
to HPC and the supplied models/resources through CVMI Lab. This is a sound SDP
experimental contribution if the comparison is reproducible and fairly selected;
an improved score is a hypothesis, not a completion requirement or guaranteed outcome.

Keep three experiments distinct:

| Experiment | Initialization and data | Claim it can support |
|---|---|---|
| Supplied-checkpoint reproduction | Original task checkpoint, matching published test annotations and frozen evaluator | Whether this project recovers the supplied model's benchmark score; no training reproduction claim |
| Author-training reproduction | Author initialization, complete original training protocol and published split, if recovered | Reproduction of training with every deviation disclosed; exact reproduction remains unresolved without author settings |
| Controlled improvement | General pretrained YOLOv10-M excluding IEDXray; fixed training-only fit/validation partition | Matched untuned-versus-tuned improvement; compare to paper separately because withholding validation changes training data |

The primary hypothesis is that tuning improves held-out detection relative to an
equally trained untuned baseline. Surpassing the paper's same-task YOLOv10-M AP
is a secondary goal. Beating this YOLO baseline does not establish state of the
art: the paper reports higher AP for Grounding DINO. An honest negative result,
search analysis and reproducible pipeline are still useful contributions. Optuna
systematizes parameter selection; it does not by itself prove novelty, causality
or better generalization. HPC access establishes available access, not a tested backend.

## Paper findings and implementation evidence

The [IEDXray paper](https://www.nature.com/articles/s41597-026-07263-7),
Tables 3–4, reports YOLOv10-M generic AP/AP50/AR **35.1/58.0/48.4** and
specific **36.8/59.1/49.0**, in percent. These are published values, not team
metrics. The paper describes pretrained initialization, standard framework
augmentation including flips and multi-scale resizing, and no additional
task-specific augmentation. It identifies miniature threats, clutter, occlusion,
imbalance and single-scanner acquisition as limitations. It does not supply a
proven Optuna search space or guarantee that continued training improves accuracy.

The [official YOLOv10 implementation](https://github.com/THU-MIG/yolov10)
supports pretrained fine-tuning. Its COCO recipe is not an exact IEDXray recipe.
The project's inspected fork is pinned to
`453c6e38a51e9d1d5a2aa5fb7f1014a711913397`. Its trainer/default config were
inspected for training controls and callbacks; this is **artifact inspection**,
not an executed training compatibility check. The fork's `on_fit_epoch_end`
also runs during final evaluation; a pruning callback must avoid duplicate epoch
reports. Verify checkpoint selection: upstream best fitness need not equal pure
AP@[.50:.95]. Save the checkpoint matching the declared selection metric.

The [Optuna 4.5.0 FAQ](https://github.com/optuna/optuna/blob/v4.5.0/docs/source/faq.rst)
supports seeded sequential studies for reproducibility and warns against SQLite
on NFS. The training dependency proposal starts with Optuna 4.5.0, subject to
the qualified environment. Use persistent JournalStorage with its JournalFileBackend
after verifying locking on the actual filesystem. Keep sampler state as well as
the study: storage alone does not preserve sampler RNG state on restart.

## Data and validation protocol

1. Faisal inventories the supplied generic and specific checkpoints by task,
   source, SHA-256 and backend. Ali freezes task-specific COCO evaluation.
   Resource provenance is CVMI Lab provision; the older record of a renewed author
   link describes checkpoint acquisition history, not a conflicting supplier.
   Publisher checksums and exact author training history remain distinct unknowns.
2. Ahmed and Ali establish a single fixed approximately 80/20 fit/validation
   partition **within published training images only**, seed 17. Use verified
   physical-configuration groups and keep identical image bytes together. Share
   the image-ID assignment across generic and specific studies; stratify by
   reviewed task labels where grouping permits and report absent/rare classes.
3. Recover physical-group metadata from the lab/model owners. If unavailable,
   exact-duplicate grouping is a minimum software guard, not proof of physical
   independence. Mark that partition exploratory and record the limitation;
   never invent group IDs from filename patterns or claim independent assemblies.
4. Use the same inspected general pretrained initialization in each task's
   untuned and tuned experiments, recording source, hash and evidence it excludes
   IEDXray. This retains transfer learning; it is not training from random weights.
   Supplied task weights may have seen the entire published training set, so they
   cannot establish unseen validation on a carve-out from that set.
5. Preserve the published test split and all source labels. The existing audit
   records four cross-split exact-byte pairs and five train threat-box boundary
   findings. Ali/Ahmed document a reviewed duplicate and boundary policy; no silent
   clipping, deleting, moving or relabeling. A derived transformation, if approved,
   must retain source hashes, affected IDs and rationale. Final reporting retains
   these caveats and cannot assert physical independence beyond evidence.
6. Optuna, early stopping, augmentation choice, operating-point choice and seed
   selection never use the published test set. Preserve the original checkpoint
   reproduction protocol and freeze candidate choices before final comparison.
   Do not use dismantled collection scans in this single-scan study.

## Training and Optuna design decisions

These are **project experiment choices**, not author-reported optimal settings.
Ahmed records the final versioned config and rationale before submitting jobs.

| Control | Initial decision |
|---|---|
| Studies | Generic first, then specific; separate histories and output directories |
| Search budget | 20 attempted configurations per task, including queued untuned control; failed/pruned trials stay in the accounting |
| Sampler | Seeded TPE, seed 17, five startup trials, one active trial at a time |
| Trial ceiling | 30 epochs, same initialization and seed 17, resolution 640 |
| Pruning | Median pruning after ten completed epochs and five completed startup trials; equal epoch steps, nonfinite/missing metrics fail explicitly |
| Primary search objective | Validation COCO AP@[.50:.95], maximize; Ali supplies the matching evaluator interface |
| Interim metric | Framework AP may be used as an explicitly named proxy during integration; no claim it is identical to official COCO AP; freeze one objective before the actual study |
| Optimizer/LR | SGD with log LR 1e-4–1e-2; AdamW with log LR 1e-5–1e-3 |
| Other search dimensions | Log weight decay 1e-5–1e-3; log terminal LR fraction 0.01–0.1; Mosaic probability 0–0.5 |
| Fixed controls | Horizontal flip 0.5; multi-scale resizing enabled; no hue/saturation shifts, MixUp or copy-paste initially; record every inherited default |
| Untuned control | Proposed SGD LR 0.001, weight decay 0.0005, terminal LR fraction 0.01, Mosaic 0; same fixed controls and initialization |
| Batch/precision | Pilot measures a safe fixed batch at 640; begin FP32, compare AMP only after compatibility/parity check; freeze effective batch and precision for a study |
| Full-budget selection | Re-run the top three completed configurations and untuned control at up to 100 epochs, seed 17; choose only using validation AP |
| Repeatability | Compare selected and untuned configurations using seeds 17, 29, 43 with identical 100-epoch ceilings; reuse matching seed-17 runs; no test-selected seed |

The top-three confirmation stage reduces the risk that a winner at 30 epochs is
a poor choice at 100. Count this extra compute separately from the 20-trial
search. If fewer than three trials finish, report that and confirm all completed
ones; if none finish, there is no selected candidate. Failed jobs are not zero AP.
Never silently change batch or precision after an OOM; investigate, then version
and restart a comparable study if settings change.

After generic confirmation, a controlled 640-versus-896 experiment can test small
object sensitivity using identical labels and a batch that fits both. Freeze its
outcome before test evaluation. Sliced fine-tuning/inference, staged freezing,
additional augmentation and architecture/loss changes are later hypotheses, each
requiring an isolated ablation. [SAHI](https://arxiv.org/abs/2202.06934) motivates
slicing for small objects; it is not evidence of gains on IEDXray. No arbitrary
attention module, model replacement or synthetic-data expansion is required.

## Student ownership and interfaces

- **Faisal / T40:** supplied-checkpoint and initialization identity, baseline
  adapter, shared manifest/prediction contract and reproducible environment/run
  evidence. Coordinate HPC prerequisites with Ahmed. Existing shared contract
  work is present; student acceptance and explain-back are recorded separately.
- **Ahmed / T41:** data preflight and training-only partition tooling, training
  runner/config, Optuna search and resume/export, training environment proposal,
  scheduler templates and training records. Core six paths are
  `src/sdp_xray/training.py`, `scripts/finetune_yolov10.py`,
  `configs/finetune.example.json`, `tests/test_training.py`,
  `environments/training/README.md`, and this `docs/finetuning.md`.
  This document is a coordinator-prepared brief for Ahmed to continue, not a claim
  that Ahmed wrote it. Plan extra helpers under `scripts/tune_yolov10.py` and
  `environments/training/` as T41 extensions, with file ownership recorded first.
  These are default contacts, not exclusive file ownership. Prioritize assigned work; a teammate blocked by a small dependency may
  implement missing shared/evaluator changes after recording scope and notifying others,
  without waiting for a reply. Coordinate active collisions and retain independent review.
- **Ali / T42:** independent COCO evaluator, validation objective interface,
  untouched-test protocol, reproduction and matched candidate metrics, class/size
  errors and latency. Ahmed calls Ali's interface; do not create a competing
  evaluator inside the trainer.
- **Abd and Mohammad / T39,T43:** app integration and report/demo interpretation;
  coordinate reviews and actual GUI selection separately from research studies.

Agree before coding: validation function inputs are candidate checkpoint identity,
validation image IDs and task annotation source, and frozen evaluator settings;
outputs contain finite AP, evaluator identity and the evaluated split hash.
Training records are separate from prediction run manifests. At evaluation time,
use Faisal's candidate role and parent checkpoint hash in the existing shared
contract. Keep class order, source COCO IDs and original-pixel xyxy predictions
explicit; conversion starts from COCO original-pixel xywh.

## HPC execution and acceptance

See [HPC training handoff](hpc-training.md). Pilot environment qualification,
then time one short training run and estimate the study's total GPU hours before
launching the search. High server capacity does not override student quotas or
prove that the pinned backend trains correctly. No remote login, package install,
job submission or new training is evidenced by this planning update.

Required software checks after student code changes: `uv run --locked ruff check .`
and `uv run --locked python -m pytest`. Cover task/category mapping, invalid boxes,
split/byte/group overlap, path resolution, config identity, run isolation,
metric/pruning steps, failure/interrupt handling and resume/export with synthetic
fixtures. Independently inspect label conversion and leakage guards. Then execute
one allocated GPU forward/backward/save/reload test and a bounded training pilot.

Ali reports original checkpoint scores, paper scores and matched local controls
in separate rows. Include AP/AP50/AR, specific-task per-class results, small-object
errors, all seeds, search budget, pruning/failures and identical latency boundaries.
Compare H100 training/inference evidence with the paper's RTX 4090 context honestly.
Report actual deltas and seed variation; parameter-importance plots are descriptive.
Share sanitized summaries only, retaining full predictions, study storage,
checkpoints, package inventory and Slurm accounting privately.

The 19 November draft/review target does not promise completion of both studies.
Use pilot timing and real student availability to date runs. The working report
cutoff remains 24 November 17:00 UTC+4, with the conflicting 27 November notice
unresolved. Preserve earlier T10/Q9 schedule conflicts; no advisor deadline is waived.
