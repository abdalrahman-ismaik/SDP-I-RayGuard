# T41 research software draft and experimental protocol

Updated 19 November 2026. Local software and synthetic verification only; no model,
real-data, Optuna study or cluster execution. Experimental direction comes from the
[coordinator's pinned brief](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/blob/6d57e5cb362164d12cb9338cf60bd72d3f9bdc6a/docs/finetuning.md).
The [pinned T41 task](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/blob/6d57e5cb362164d12cb9338cf60bd72d3f9bdc6a/docs/tasks.md) records the expanded scope; the local historical backlog is not changed by this draft.

## Current software and usage

The 19 November local implementation extends the existing draft; it does not
claim Faisal/Ali interface approval or an executed training environment.
The previous local guide, API examples and dated checks are preserved in
[legacy draft history](finetuning-legacy-draft.md). The legacy candidate helper
and its original tests remain supported.

| Component | Implemented behavior |
|---|---|
| `training.py` | Original strict conversion, auditor adapter, legacy candidate helper and versioned planner dispatch |
| `training_partition.py` | Pure metadata partitioning and in-memory COCO views; no file writes |
| `training_research.py` | Explicit research task, initialization receipts, fail-closed evidence gates and common-parent candidate records |
| `tuning.py` | Injectable synthetic orchestration, validation boundary, accounting, durable snapshots, confirmation/repeatability plans; gated optional Optuna adapter |
| `scripts/finetune_yolov10.py` | Preflight/planning with explicit research task |
| `scripts/tune_yolov10.py` | Study preflight, resume inspection and synthetic-ledger export |
| `environments/training/train.slurm` | Reviewable resource/environment/signal template; present CLI still blocks live execution |

From the repository root with locked CPU tools available:

```text
uv run --locked python scripts/finetune_yolov10.py
uv run --locked python scripts/tune_yolov10.py --task generic
uv run --locked python scripts/tune_yolov10.py --task specific
uv run --locked python scripts/tune_yolov10.py --config configs/finetune.example.json --output runs/<existing-private-directory>/training-plan.json
```

These commands return **2 / blocked**. They read configuration and optional
`--evidence` JSON, never scans, checkpoints, local GUI settings or model packages.
`--execute` cannot enable execution. Output creation is exclusive and optional;
its parent must already exist. `--resume-from <directory>` checks a stored
configuration/snapshot without resuming work. Exporting an existing **synthetic**
ledger uses `--export-from <directory> --output <new-file.json>` and returns 0.
Console errors omit private paths and raw exceptions.

The example config records the coordinator's project choices below, with generic
first. It leaves initialization, source identities, reviewed policies, interface
agreements, owner/output, batch and qualification evidence unset. There is no
research GUI prerequisite or universal generic-parent hash. A specific-task plan
also requires a generic-completion receipt bound to the same partition hash.
Those receipts are supplied assertions, not authenticated approvals.

### Partition, audit and source preservation

`make_partition(train_inventory, test_inventory, policy)` accepts only metadata.
Each row contains nonnegative `id`, image-byte `sha256`, original physical
`group` or null, and reviewed task-prefixed label memberships. For example,
`generic:Explosive` and `specific:IED Explosive` retain catalog spelling.
Both tasks use **the same saved partition**, not separate random splits.
IDs are scoped to their published split; repeating integer IDs between train/test
are not themselves leakage.

The algorithm connects identical bytes and, when verified, physical groups
transitively. It assigns whole connected components using seed 17, a target
validation fraction of 0.2 and best-effort label balance. It records the actual
fraction, per-class image counts, absent/rare labels and limitations. Large
components can prevent an exact 80/20 ratio. A single connected component blocks.
No group is inferred from a filename. Exploratory exact-byte grouping is explicit
and cannot silently discard supplied group metadata.

Policy receipts bind the exact duplicate/overlap findings via their canonical
JSON SHA-256. Supported dispositions preserve samples and group train duplicates,
and preserve/report published-test overlap. Physical provenance or the exploratory
fallback needs review. Boundary findings remain **blocked invalid geometry**:
this implementation supplies no clipping, deletion, relabeling or derived repair.
An approved transformation would need a separately reviewed implementation with
source hashes, affected IDs and rationale.

`subset_coco(document, partition, "fit" | "validation", catalog_id)` returns
deep-copied views with original IDs and labels, including annotation-empty images.
It writes nothing and does not certify geometry. The existing `convert_coco`
still checks geometry, unsupported annotations, exact maps, category **0**,
output collisions and float32 duplicate/underflow losses. No upstream converter
or blind category-ID subtraction is used.

`inspect_partition_sources(sources, task, partition)` explicitly reuses the
existing auditor/converter, checks derived memberships/image bytes/group metadata
against the saved partition, and returns audit evidence plus a partition binding.
It is not exposed by either CLI. Only tiny generated images exercise it here.
Future real source processing needs separate authorization and a reviewed
original-to-derived annotation provenance record. The planner checks complete
file coverage, source hashes, class maps, conversion counts and all split pairs;
`ok: true` alone is insufficient. Fit/validation overlap always blocks. Reviewed
published-test overlap remains a reported limitation, never independent-test proof.
Missing or aliased validation blocks; a future trainer data file must omit
`test` entirely to prevent upstream fallback.

### Initialization and candidate records

`validate_initialization(receipt, task)` requires general YOLOv10-M pretraining,
a source reference, owner verification of the stated hash, evidence excluding
IEDXray, task identity, initialization procedure, task-head handling and seed.
It rejects the supplied task-checkpoint hashes as general initialization.
The planner never loads/hashes weights and records that fact.

`research_candidate_manifest(task, initialization, checkpoint, run, results,
model_id=...)` hashes an actually supplied output file and reuses the unchanged
shared prediction/run validators. `write_research_record` writes the validated
record exclusively to a new directory. These helpers perform no inference.
The explicit research model ID convention still needs Faisal's agreement.

For common initialization G and outputs U/T:

| Record | Shared role | Output hash | Parent hash |
|---|---|---|---|
| Untuned control U | candidate | actual hash(U) | verified hash(G) |
| Tuned output T | candidate | actual hash(T) | verified hash(G) |

Both retain task/kind, output-class order and source-category map, and separate
requested from actual device. Training settings never enter the strict inference
manifest. Initialization procedure, task-head seed and training/repeat seed remain
separate metadata; repeat seeds do not silently change the initialization receipt.
The original `candidate_manifest` / `write_candidate_record` behavior remains
available for its original catalog-baseline handoff.

Ali's common-initialization matcher is **pending agreement and implementation by
its owner**. The tuned parent must not be changed to hash(U) to satisfy a
direct-parent matcher. Both modes should remain explicit. No shared manifest,
baseline adapter/CLI, evaluator or evaluation configuration was changed here.

### Injectable study boundary and persistence

`make_study_definition` freezes config, initialization, partition/validation
identity, task map and objective. `run_synthetic_study` accepts a fake sampler,
fake trainer and fake validation adapter, each explicitly marked
`synthetic=True`. It performs CPU state-transition checks using synthetic
checkpoint bytes; every exported record says `synthetic_software_check` and
`training_started: false`. It is not an Optuna study or evidence of training.

The proposed validation request includes checkpoint SHA-256, completed epoch,
task/maps, partition SHA-256, annotation SHA-256, exact validation IDs and frozen
objective/evaluator settings. The result echoes these identities with
`status: "ok"`, exact `evaluated_image_ids` and finite AP in [0,1].
Missing/nonfinite results, incomplete/duplicate IDs or mismatches fail the attempt;
they never become zero AP. There is no competing COCO evaluator. Fake scores in
tests are explicitly invented software fixtures, not predictions or metrics.

The sequential loop counts the queued control and failed/pruned configurations
within 20 attempts. Reports use consecutive completed epochs; repeated identical
epochs and final-evaluation callbacks do not report twice. A changed checkpoint
for an already reported epoch fails. Pruning is gated on ten completed epochs
and five completed trials. Checkpoint selection uses the declared validation AP,
not upstream fitness or simply the last epoch.

Each attempt owns a new subdirectory. Linked, append-only JSON snapshots contain
both ledger and sampler state and are flushed to disk. A single-writer lock
rejects concurrent writers. Explicit interrupted retries retain the configuration
number and parameters; trainer invocations are counted separately. Last and best
checkpoint bytes are rechecked on resume. Definition changes, checkpoint changes,
broken snapshot chains, torn writes and stale locks require deliberate recovery.
No automatic cleanup or new study is substituted. Time-budget/stop callbacks stop
new attempts and preserve completed-epoch state; hard kills can lose current work.

The optional Optuna 4.5.0 adapter uses seeded TPE, MedianPruner and persistent
JournalStorage/JournalFileBackend. It is behind recomputed execution gates and
was **not imported or exercised**. It proposes JSON serialization of both TPE and
random-sampler RNGs, with journal-signature checks. Its private RNG fields and
journal locking need qualification against exactly 4.5.0 on the actual storage.
Journal/ledger divergence blocks rather than replaying ask/tell silently.

`confirmation_plan` and `repeatability_plan` create separate compute plans,
not extra search trials. Confirmations include the top completed configurations
and untuned control. Repeatability accepts validation-bound confirmation results,
selects using validation only, reuses matching seed-17 results and plans seeds
29/43. These stages have no production executor yet. The current synthetic loop
requires all 30 epochs for completion; a production early-stop protocol remains
to be connected explicitly. No OOM batch/precision adaptation is implemented.

### Remaining integration and qualification

Local software authorization is not Faisal/Ali acceptance. Still needed:
the validation adapter and common-initialization comparison agreement; verified
initialization and source provenance; reviewed duplicate/boundary/group policy;
qualified shared-interpreter overlay with full training/save/reload evidence;
safe fixed batch, storage locking/resume evidence, measured GPU-hour budget and
a named human owner/output. No live YOLO trainer is connected. Review every
upstream default, download/install hook, callback and checkpoint reload before
connecting it. Root CPU dependencies and GUI code remain unchanged.

HPC access is confirmed; qualification is not. The Slurm template currently
invokes a CLI that returns blocked, and must not be submitted as a training job.
See [the environment proposal](../environments/training/README.md) and
[HPC handoff](hpc-training.md). The coordinator protocol retained below governs
the experiment; passing synthetic checks does not establish model quality.

### Verification record

The earlier 19 November review passed Ruff, 41 T41 tests, and a partial repository
run with 227 passed / 9 Windows symlink skips / 1 prohibited runner test deselected.
Those were pre-expansion results.

The first expanded check found one import-order lint issue (corrected) and
96 passing tests plus a Bash-parser startup failure. Windows denied the Bash
runtime's named-object initialization before it parsed the template. This host
therefore reports that parser check as unavailable, separately from successful
static scheduler checks.

Final expanded verification on 19 November 2026 (Python 3.12.10, locked CPU
environment, offline uv, Python downloads disabled and external pytest plugins
disabled):

| Exact command | Actual result |
|---|---|
| `uv run --locked ruff check .` | Passed, exit 0 |
| `uv run --locked python -m pytest --deselect tests/test_model_catalog.py::test_wrong_task_checkpoint_is_rejected_before_importing_model_packages` | 283 passed, 10 skipped, 1 deselected; exit 0; 20.96 seconds |
| `uv run --locked python scripts/finetune_yolov10.py` | Expected blocked result, `training_started: false`, exit 2 |
| `uv run --locked python scripts/tune_yolov10.py --execute` | Expected blocked result, `training_started: false`, exit 2; no Optuna/model import |

This is a **partial suite**, not an unrestricted full run. Nine existing STCray
symlink checks lack Windows privileges; the tenth skip is the disclosed Bash
runtime startup limitation. The one explicitly deselected test executes the
prohibited inference runner. All 41 legacy T41 tests passed unchanged in behavior;
their original config is retained as a dedicated fixture. No test imported a
model backend, performed training, opened real scans or ran an Optuna study.

Process-local verification restrictions were `UV_OFFLINE=1`, `UV_NO_CONFIG=1`,
`UV_PYTHON_DOWNLOADS=never`, `PYTHONDONTWRITEBYTECODE=1`, a temporary
`UV_CACHE_DIR`, and `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` for pytest. Root dependencies
were unchanged. These software results establish no model-quality claim.
The CLI exit codes were propagated explicitly with PowerShell `exit $LASTEXITCODE`;
without that forwarding the shell wrapper normalized the nonzero code to 1.
The Slurm file was also confirmed UTF-8 with LF-only line endings; this is not
a substitute for the unavailable Bash parser or Linux scheduler qualification.

## Coordinator experimental protocol

The following experimental direction is reconciled from the coordinator-prepared
18 November brief at the pinned commit. It is not a claim of Ahmed's authorship,
executed experiments, recovered author settings or another student's approval.

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
  Do not edit Faisal's shared manifest, baseline adapter or CLI, or Ali's evaluator.
- **Ali / T42:** independent COCO evaluator, validation objective interface,
  untouched-test protocol, reproduction and matched candidate metrics, class/size
  errors and latency. Ahmed calls Ali's interface; do not create a competing
  evaluator inside the trainer.
- **Abd and Mohammad / T39,T43:** app integration and report/demo interpretation;
  coordinate reviews and actual GUI selection separately from research studies.

Pending owner agreement for live integration: validation function inputs are candidate checkpoint identity,
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
