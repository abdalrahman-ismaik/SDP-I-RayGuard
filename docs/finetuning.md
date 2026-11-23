# T41 research software draft and experimental protocol

## Final generic evaluation — 23 November 2026

Job 820 completed the frozen 5,136-image published-test comparison, exit 0:0.
Test AP is 41.5886% control / 48.0502% candidate; all metrics independently
recomputed from saved predictions. No test-based model or parameter selection.
See [final results and limitations](t41-results.md). Earlier unused-test statements
below describe the training stage before this final evaluation. No additional
training is scheduled under the completed reduced scope.

## Verified completion - 23 November 2026

The user-authorized reduced generic protocol completed at 05:13 UAE: six attempts
(five complete, one failed), then two complete 100-epoch confirmations. Ali's
validation AP was 87.7062% for the untuned control and 87.4833% for the best search
candidate, independently recomputed exactly. All 350 successful epoch prediction
records were verified. The published test set was unused; physical independence
remains exploratory. Specific/repeatability are deferred; the original 20-attempt
protocol is not complete. See [the current handoff](t41-handoff.md) for actual jobs,
checkpoint hashes, timings, scope and limitations. No further GPU job was started.

## Historical launch and implementation record

Updated 22 November 2026. Public inputs and read-only data audits are now verified
on HPC; bounded environment job 741 passed after job 740's font-discovery failure.
The user's subsequent explicit execution authorization supersedes the wait for
further human approval, without claiming Abd's review. Derived repairs and both
training bundles are complete; the shared seed-17 partition has 9,779 fit and
2,445 validation images. All original annotation hashes remain unchanged. The
real generic pilots 750 and 754 completed training, checkpoint reload, class
mapping and Ali validation. Generic control job 755 failed during epoch-6
validation after five completed epoch reports; its failed attempt remains counted.
Diagnostic 756 verified clipping of wholly outside detections as the cause.
The preservation fix passed GPU qualification 757; configuration 1 was submitted
as job 758 under the revised deadline scope. Pilot 754's validation AP
0.57926 / 0.72045 / 0.78267 is exploratory, not a final comparison. The earlier
environment probes used synthetic inputs and produced no model metric.
See [current executed evidence and next steps](t41-handoff.md).

**User deadline amendment, 22 November:** run generic only, six attempted
configurations total including the failed control attempt, then the best completed
candidate and original control for 100 epochs each at seed 17. Defer specific and
repeatability. Preserve the original scientific definition and append the explicit
execution-scope amendment; do not label the original full protocol complete.
The five-startup-trial TPE setting remains unchanged. With one failed attempt,
this small search can remain entirely in startup sampling; it does not establish
TPE convergence or repeatability. The prediction-geometry correction and evidence
are recorded in [the data/validation policy](t41-data-policy.md).

Experimental direction comes from the
[coordinator's pinned brief](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/blob/6d57e5cb362164d12cb9338cf60bd72d3f9bdc6a/docs/finetuning.md).
The [pinned T41 task](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/blob/6d57e5cb362164d12cb9338cf60bd72d3f9bdc6a/docs/tasks.md) records the expanded scope; the local historical backlog is not changed by this draft.

The [21 November coordinator update](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/blob/1b911128e034c38f0087227f375f0f4d99856419/docs/finetuning.md)
retains this experimental protocol and adds the integration/report handoff.
Its teamwork amendment makes named owners default contacts: briefly announce a
bounded blocking task, coordinate overlapping edits/GPU outputs, and proceed
without waiting for a person-specific permission. Independent review and the
scientific checks still apply. The existing config approval keys naming Faisal
or Ali identify review topics, not required reviewer names. No approval is
inferred from a message announcing work. This change stays in T41 files.

The software draft was pushed by Ahmed at `32091bc`, according to his supplied
terminal output. A PR against `main` and its human review remain his actions;
this local update performs no Git operations. Report evidence is due for the
23 November review/content freeze; the owner confirms submission on 24 November
at 17:00 UAE time. Unfinished experiments must be reported as unfinished.

## Current allocated execution

The owned HPC driver uses `run_workflow` with a hash-bound runtime
`search_chunk: {index, attempt_limit: 1}` for one whole search attempt per job.
Only terminal study ledgers can continue in the next allocation; interrupted
optimizer checkpoints still cannot. A hash-bound `stage_output_keys` list selects
one declared 100-epoch confirmation or repeatability run per job; the controller
requires every scheduled result before advancing the stage. It enforces the
20-attempt total and generic-before-specific order. Public planning examples remain
incomplete templates; the private driver supplies actual evidence and authorization.

Optional `checkpoint_retention: best_validation_and_latest` retains the checkpoints
selected by Ali's validation AP and the latest saved epoch, with hashes and planned/
completed retirement records for unselected snapshots created by that attempt.
The default remains `all`. Full per-epoch predictions are preserved losslessly as
gzip JSON, with compressed and uncompressed hashes. Existing pilot outputs remain
intact. Two loader workers are qualified within the four-CPU allocation; local
worker IPC is allowed while IP networking and subprocess dispatch remain blocked.
The fixed batch is 32 with FP32. Quota and measured duration are checked before
each allocation. The full measured protocol extends beyond the report freeze.

## Earlier software and planning usage

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
| `training_backend.py` | Audited isolated data copies, explicit fork arguments, synchronous saved-epoch callback adapter and private validation-path binding; exercised with fake trainers only |
| `training_workflow.py` | Separate execution receipts, conditional CLI dispatch, pilot/confirmation/repeatability stages and timing estimates; actual execution remains unqualified |
| `training_validation.py` | Batch-one checkpoint/detection bridge to Ali's evaluator, explicit source-category mapping and complete coverage checks; no COCO evaluator implemented here |
| `tuning.py` | Separate synthetic/authorized entry points, accounting, durable snapshots, confirmation/repeatability plans and gated Optuna adapter; actual Optuna 4.5 API/state roundtrip and same-host shared-storage writes checked with synthetic values only |
| `scripts/finetune_yolov10.py` | Preflight/planning with explicit research task |
| `scripts/tune_yolov10.py` | Study preflight, resume inspection, labelled ledger export and separately authorized stage dispatch |
| `environments/training/train.slurm` | Resource/environment/signal template requiring four private inputs; missing execution evidence blocks |

From the repository root with locked CPU tools available:

```text
uv run --locked python scripts/finetune_yolov10.py
uv run --locked python scripts/tune_yolov10.py --task generic
uv run --locked python scripts/tune_yolov10.py --task specific
uv run --locked python scripts/tune_yolov10.py --config configs/finetune.example.json --output runs/<existing-private-directory>/training-plan.json
```

These commands return **2 / blocked**. They read configuration and optional
`--evidence` JSON, never scans, checkpoints, local GUI settings or model packages.
`--execute` alone cannot enable execution. A separate reviewed execution request
and runtime inputs must satisfy conditional gates; see [the handoff](t41-handoff.md).
Output creation is exclusive and optional;
its parent must already exist. `--resume-from <directory>` checks a stored
configuration/snapshot without resuming work. Exporting an existing closed
ledger uses `--export-from <directory> --output <new-file.json>` and returns 0;
its synthetic/model-training label is preserved, never inferred from file presence.
Console errors omit private paths and raw exceptions.

The example config records the coordinator's project choices below and Ali's
exact `validation_objective.objective()` at PR18 commit `6dfa7d6`, with generic
first. It leaves initialization, source identities, reviewed policies, interface
agreements, owner/output, batch and qualification evidence unset. There is no
research GUI prerequisite or universal generic-parent hash. A specific-task plan
also requires a generic-completion receipt bound to the same partition hash.
Those receipts are supplied assertions, not authenticated approvals.
The follow-up integration fixes `validation_prediction.conf=0.001` and
`max_det=300` as explicit project settings; approval receipts remain unset.
See [the policy review](t41-data-policy.md) for rationale and unresolved geometry. The
prediction settings are distinct from Ali's frozen COCO objective and are part
of the study identity, so changing them cannot silently change the objective.

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

`validate_initialization(receipt, task, expected_seed=17)` requires general YOLOv10-M pretraining,
a source reference, owner verification of the stated hash, evidence excluding
IEDXray, task identity, initialization procedure, task-head handling and seed.
It rejects the supplied task-checkpoint hashes as general initialization.
The planner never loads/hashes weights and records that fact.

`research_candidate_manifest(task, initialization, checkpoint, run, results,
model_id=...)` hashes an actually supplied output file and reuses the unchanged
shared prediction/run validators. `write_research_record` writes the validated
record exclusively to a new directory. These helpers perform no inference.
Faisal proposes `research-yolov10m-<generic|specific>-<untuned|tuned>-seed<N>`.
The local helper accepts an explicit ID; no shared interface or owner approval
is changed by documenting this convention.

Faisal's [initialization evidence at b325c28](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/blob/b325c28/docs/initialization-provenance.md)
identifies official THU-MIG/yolov10 **v1.1** `yolov10m.pt`, 66,924,323 bytes,
SHA-256 `ff2c559f11d13701abc4e0345f82851d146ecfe7035efaafcc08475cfd8b5f2d`.
This is Faisal's recorded artifact inspection, not a hash computed against real
weights during this T41 change. His receipt code was inspected read-only; its
shape was checked against this validator with synthetic bytes for both tasks.
The documented COCO metadata and upload chronology support exclusion of public
IEDXray, with the limits stated in his document. The actual HPC copy still needs
transfer and rehash. The example initialization remains null until a real receipt
is supplied; no owner approval is manufactured from the recorded hash.

For common initialization G and outputs U/T:

| Record | Shared role | Output hash | Parent hash |
|---|---|---|---|
| Untuned control U | candidate | actual hash(U) | verified hash(G) |
| Tuned output T | candidate | actual hash(T) | verified hash(G) |

Both retain task/kind, output-class order and source-category map, and separate
requested from actual device. Training settings never enter the strict inference
manifest. Initialization procedure, task-head seed and training/repeat seed remain
separate metadata. Search/confirmation require 17. Repeat records explicitly pass
`expected_seed=29` or `expected_seed=43` to the validator and candidate/writer
helpers with a matching receipt. No receipt is rewritten automatically. All
these runs retain the same starting-file hash; task-head initialization varies
with the declared seed. The default call still rejects non-17 receipts.
The original `candidate_manifest` / `write_candidate_record` behavior remains
available for its original catalog-baseline handoff.

Ali's common-initialization matcher is implemented on PR18 at `6dfa7d6` as
`compare-candidates` / `mode="untuned_vs_tuned"`. PR18 was subsequently merged
as `9350482`; its unchanged files are now integrated into this local worktree.
Git history, commits and pushing remain human actions. The tuned
parent must not be changed to hash(U) to satisfy the separate direct-parent
mode. Both modes remain explicit. No shared manifest,
baseline adapter/CLI, evaluator or evaluation configuration was changed here.

### Injectable study boundary and persistence

`make_study_definition` freezes config, initialization, partition/validation
identity, task map and objective. `run_synthetic_study` accepts a fake sampler,
fake trainer and fake validation adapter, each explicitly marked
`synthetic=True`. It performs CPU state-transition checks using synthetic
checkpoint bytes; every exported record says `synthetic_software_check` and
`training_started: false`. It is not an Optuna study or evidence of training.

The validation request, now supplied by Ali's matching PR18 interface, includes checkpoint SHA-256, completed epoch,
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
29/43. These stages now have conditional execution through `training_workflow`,
but the actual model runtime has not been qualified. The current synthetic loop
requires all 30 epochs for completion; a production early-stop protocol remains
to be connected explicitly. No OOM batch/precision adaptation is implemented.

### Saved-epoch adapter and isolated dataset preparation (21 November)

`prepare_training_bundle(config, sources, partition, output)` reruns the existing
full auditor and source binding, then requires the planner's data evidence gates.
Data-policy, source-identity and validation-design reviews are required. GPU
qualification, batch selection, initialization and compute approval belong to
execution and are not prerequisites for preparing this bundle. This avoids
requiring a completed pilot before the pilot's dataset can be prepared. Preparing
data does not clear any execution gate or change a review receipt.
It copies fit/validation image bytes and strict converted labels into a new,
separate directory. Original COCO IDs remain in a membership receipt; generated
filenames use those IDs. Annotation-empty images get empty label files. Test
images are audited but never copied or referenced in `data.yaml`; no `test` or
`download` key is accepted. Source hashes are rechecked before the completion
receipt is written. A failure leaves an incomplete directory for deliberate
inspection, never automatically deletes or reuses it. This API is not exposed
by the CLI and has only been exercised on generated images.

`check_training_bundle` checks its receipt, exact membership and copied-file
coverage/hashes against the configured partition/source identities. It rejects
missing validation, fallback, changed classes/labels, extra images and collisions.
These hashes detect changes, not authenticated approval: the actual generated
bundle still needs independent conversion/label review before a real pilot.

`training_arguments` binds full absolute local weights to the initialization
hash, an explicit seed, fixed batch, FP32 (`amp=False`, `half=False`) and one
device (`cpu` for software fixtures or allocation-relative `0`). It supplies
the protocol optimizer/augmentation choices, all images (`fraction=1`) and no
class collapsing. The adapter proposes zero data-loader workers for the initial
single-process qualification. Framework early stopping is disabled (`patience=0`)
so the declared AP/pruner, rather than upstream fitness, controls trial selection.
These integration controls still need pilot review; no batch size is invented.

`YoloTrainerAdapter(fake_class, weights, bundle).run_with_callback(request, on_epoch)`
uses the inspected `YOLOv10DetectionTrainer(overrides=...)`, `add_callback`, `train`
API shape with an explicitly fake class. Each `on_model_save` copies `last.pt`
exclusively into `completed-epochs/epoch-NNN.pt` before reporting. Copies survive
the upstream final rewrite of last/best weights. Identical duplicate save events
report once; changed duplicates/missing epochs fail. There is no final-evaluation
callback registration. Pruning, failures and interruption propagate immediately,
before another fake epoch runs. All effective arguments stay in the private
attempt directory, separate from inference records.

The synthetic study loop now accepts this synchronous adapter alongside its
original generator trainer. `CheckpointValidationAdapter` passes the checkpoint
path separately to `delegate.evaluate_checkpoint(request, checkpoint)`, verifies
its bytes before/after, and validates the unchanged portable result. Ali must
supply the production delegate. AP remains finite official validation AP on a
0-1 scale with exact checkpoint/task/partition/annotation/settings identities
and complete image coverage. No metric or prediction implementation is added here.

`live_trainer_class(plan, authorization)` recomputes execution gates before its
lazy upstream import. The CLI now has conditional dispatch through a separately
reviewed request, runtime source hashes, allocation and output reservation.
No real execution was performed, and the example still blocks. In particular, upstream
`check_resume` restores prior arguments/output paths, and final evaluation strips
optimizer state from normal checkpoints. The new adapter explicitly rejects
checkpoint resume until isolated output and full optimizer/RNG continuation are
qualified. Existing synthetic ledger/generator resume behavior remains supported.
The public authorized study API supports clean trial-boundary resume; live
unfinished trials block before another attempt. CLI resume remains inspection
only. This limitation must be resolved/qualified before promising unattended
multi-allocation studies; interrupted runs are never relabelled as zero AP.

Read-only upstream inspection also found font-download, package-install and
integration callbacks that still need offline qualification. Faisal's task-head
transfer description is expected behavior, not pilot evidence. Preserve the
`Transferred N/M` log; note that pinned BaseTrainer always freezes `.dfl` layers
even when there is no requested additional layer freezing. Saved checkpoint
tensors may be half precision even when training uses FP32. Save/reload and
head transfer therefore still require executed qualification.

### Data-policy proposal for independent review

This is a proposal, not approval or a claim to have processed real IEDXray:

| Finding | Proposed disposition |
|---|---|
| Exact duplicates within published training | Retain every sample; keep byte-identical and verified related images in the same fit/validation component |
| Published train/test overlap | Preserve both published splits, record affected identities and report leakage limitations; never tune on test |
| Physical groups unavailable | Use the documented reviewed exploratory exact-byte fallback; explicitly state that physical independence is unknown |
| Invalid boxes/boundary findings | Continue blocking conversion/training; seek authoritative corrected labels or a separately reviewed derived repair with original hashes and affected IDs |

No box repair, clipping, deletion, relabeling or invented grouping is implemented.

### Pending production integration

Local software authorization is not runtime qualification. Ali's PR18 update at
`6dfa7d6f69ae40aec2885c6d5116a3eb776c6ec1` now supplies
`validation_objective.evaluate_validation`, its frozen `objective()`, and
`compare-candidates` for common-initialization records. The T41 bridge calls that
function and checks its result; it does not replace Ali's evaluator. Its source
was checked in memory with synthetic inputs and a fake AP backend. Actual COCO
metric execution was not tested in this root environment. Ali's modules and
their tests/protocol are now present from merged commit `9350482`, byte-checked
against the pinned authored sources. The config calls his `objective()` directly.
Faisal's initialization module/document are integrated unchanged from `b325c28`;
his PR21 is still open and his shared CLI changes were not copied.

Still needed: review of the now-explicit prediction thresholds/limits, verified
initialization and source provenance; reviewed duplicate/boundary/group policy;
qualified shared-interpreter overlay with full training/save/reload evidence;
safe fixed batch, storage locking/resume evidence, measured GPU-hour budget and
a named human owner/output. Only the fake-backed trainer/predictor connection is tested. Review every
upstream default, download/install hook, callback and checkpoint reload before
connecting it. Root CPU dependencies and GUI code remain unchanged.

HPC access is confirmed; qualification is not. The Slurm template now passes
config, evidence, authorization and runtime inputs to the conditional CLI.
The current example and missing qualifications still block; no submission was authorized here.
See [the environment proposal](../environments/training/README.md) and
[HPC handoff](hpc-training.md). The coordinator protocol retained below governs
the experiment; passing synthetic checks does not establish model quality.

### Verification record

Later local dependency integration passed Ruff and **423 tests, 12 skips,
1 explicit prohibited-runner exclusion in 39.28 s**. This includes Ali's pure
evaluation checks and direct initialization/validation API integration tests.
The two additional skips are optional metric modules: their requirements were
not cached, and the separate PyPI attempt failed DNS resolution. Actual COCO
metric tests therefore did not execute. See [the handoff](t41-handoff.md) for
exact commands, source credits and all exclusions. The counts below are earlier
verification history.

The preceding 21 November workflow/validation update passed Ruff and the permitted
partial repository suite: **362 passed, 10 skipped, 1 deselected in 38.91 s**.
The skips remain nine Windows symlink-privilege failures and one unavailable
Bash runtime; the explicit exclusion remains the prohibited inference-runner
test. All 41 legacy tests passed. See [the handoff](t41-handoff.md) for commands,
the pinned Ali compatibility check, changed files and remaining qualifications.
These are software results only; no actual training, model inference or COCO
scoring was performed. The records below are preserved historical runs.

Earlier 21 November integration update (before the conditional workflow and
Ali's new interface), locked CPU environment with `UV_OFFLINE=1`,
`UV_NO_CONFIG=1`, `UV_PYTHON_DOWNLOADS=never`, `PYTHONDONTWRITEBYTECODE=1`,
`PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` and a temporary UV cache:

```text
uv run --locked ruff check .
uv run --locked python -m pytest --deselect tests/test_model_catalog.py::test_wrong_task_checkpoint_is_rejected_before_importing_model_packages
```

Ruff passed. The permitted **partial repository suite** passed with **311 passed,
10 skipped, 1 deselected** in 31.17 seconds. Nine skips were unavailable Windows
symlink privileges; one was Bash named-object startup denial. The deselected test
executes the explicitly prohibited inference runner. No other tests were
deselected. This includes all 41 legacy T41 tests and 28 new backend/seed tests.
The initial targeted run had 121 passed, one failed and one skipped: the new
specific-task fixture incorrectly used source category 0. The auditor rejected
it; the fixture was corrected to the catalog's source ID 1, retaining model
index 0. The final results above are from the corrected code.

No model, real scans, inference, real Optuna study or HPC job was executed.
These checks do not measure model quality or qualify the trainer environment.
The records below retain earlier verification history, not current counts.

An additional `uv run --locked python -` in-memory compatibility check executed
Faisal's inspected receipt module at `b325c28` with its expected identity replaced
by a tiny synthetic file. All six generic/specific and seed 17/29/43 combinations
passed `validate_initialization(..., expected_seed=seed)`. Model/Optuna imports
were blocked by an import guard. This checked schema compatibility, not the real
checkpoint, HPC copy or human approval. No receipt was saved to the repository.

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
  The 21 November teamwork amendment supersedes exclusive ownership here:
  announce bounded blocking work, coordinate active edits and retain independent
  review. This T41 update leaves shared manifest/adapter/CLI and evaluator files unchanged.
- **Ali / T42:** independent COCO evaluator, validation objective interface,
  untouched-test protocol, reproduction and matched candidate metrics, class/size
  errors and latency. Ahmed calls Ali's interface; do not create a competing
  evaluator inside the trainer.
- **Abd and Mohammad / T39,T43:** app integration and report/demo interpretation;
  coordinate reviews and actual GUI selection separately from research studies.

The original brief's pending interface is now supplied by Ali at `6dfa7d6`
(see the current implementation notes above). Its requirements remain:
validation function inputs are candidate checkpoint identity,
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
