# T41 execution handoff — 23 November 2026

## Frozen test and report handoff completed — 23 November

The reduced generic training scope and frozen published-test comparison are now
**executed and verified**. Job **820** completed at 08:45:31 UAE in 1m27s, exit 0:0,
covering all 5,136 original test images. Test AP@[.50:.95] is **41.5886% control /
48.0502% candidate** (+6.4616 percentage points); validation remains **87.7062% /
87.4833%**. All test metrics and fixed-threshold counts independently recomputed
exactly from saved predictions. Test data selected no model or setting.

At confidence 0.25 and IoU 0.50, recall is 48.7516% / 48.2834%; 1,642 / 1,657
annotated boxes were missed. Candidate small-object AP is lower. Keep these
limitations, the large validation/test gap, retained duplicate images and
unverified physical independence alongside the higher test AP. Specific,
repeatability and the original 20-attempt protocol remain explicitly deferred.

[Final results and provenance](t41-results.md) contain checkpoint/prediction/plan
hashes, full metrics, failure examples and timing boundaries. The test evidence
archive and all 46 manifest-listed files passed local hash verification; both
selected weights and training evidence were already backed up. The LaTeX report
now includes these results. The reduced T41 execution/report-evidence scope is
complete; human PR review/integration and whole-report T38 acceptance are separate.
No further training or parameter selection is scheduled.

## Training-only completion record — before the final test

The user-authorized six-attempt generic search and two 100-epoch confirmations
finished at **05:13 UAE on 23 November**. At 08:17 UAE, authenticated Slurm
accounting confirmed completion and no queued/running jobs for the account.
All seven successful allocations exited 0:0; failed attempt 0 remains failed
with null objective. The completion receipt explicitly defers specific and
repeatability and does not claim the original 20-attempt protocol completed.

| Stage | Job(s) | Actual outcome | Slurm elapsed |
|---|---|---|---|
| Search attempt 0 | 755 | Failed during epoch-6 validation; counted | 11m53s |
| Search attempts 1–5 | 758, 759, 762, 764, 767 | Five completed 30-epoch runs | 52m41s, 52m29s, 52m23s, 52m35s, 52m34s |
| Untuned-control confirmation | 770 | Completed 100 epochs, seed 17 | 2h47m35s |
| Best-search-candidate confirmation | 819 | Completed 100 epochs, seed 17 | 2h46m49s |

The successful search and confirmation allocations totaled **9h57m06s**;
including failed search 755 gives **10h08m59s**, excluding pilots/diagnostics.
Each allocation stayed within its four-hour limit. No optimizer continuation,
additional search, specific training or repeatability run was performed.

| Confirmation | Source trial | Selected completed epoch | Validation AP@[.50:.95] |
|---|---|---|---|
| Untuned control | 0 | 68 of 100 | 0.8770615927076139 (87.7062%) |
| Best search candidate | 4 | 84 of 100 | 0.8748334372095157 (87.4833%) |

The best search candidate was **0.2228 AP percentage points lower** than the
control in confirmation. The confirmation validation does not demonstrate an
improvement from tuning; the separately frozen test result is reported above. It is one seed on exploratory validation, not a
significance or repeatability result. Five completed search scores, in attempt
order, were 0.8681149026702543, 0.8611312863765374, 0.8626197061543672,
0.8698530114912326 and 0.8618404439542645. Candidate 4 was selected before
confirmation using validation only. The reduced budget can remain entirely
within the sampler's five startup trials; no TPE convergence is claimed.

Both confirmations started from the same verified general YOLOv10-M initializer
`ff2c559f11d13701abc4e0345f82851d146ecfe7035efaafcc08475cfd8b5f2d`.
The untuned settings were SGD, lr0 0.001, lrf 0.01, weight decay 0.0005 and
mosaic 0.0. Candidate 4 used SGD, lr0 0.00039395937211170054, lrf
0.024891291799007523, weight decay 0.0001327448896014095 and mosaic
0.3943503548394498. Batch 32, FP32, two loader workers, seed 17, task class
0 = Explosive and the shared 9,779/2,445 partition were held fixed.

Selected checkpoint SHA-256 values:

- Control: `8ebadfcf6c91f29c0a235559161f9e4414083d717449c046f0a68c6e82475c91`.
- Candidate 4: `097ff71eb741ce51ba053bc77512ba0916772c69ae8b4d7d50c0ef497e3f65f8`.

At 08:20 UAE, a separate CPU-only verification rehashed **237 bound runtime
files**, the initializer, selected checkpoints and **350 successful epoch
prediction records**, checking compressed/uncompressed hashes, detection counts,
task mapping, all 2,445 validation IDs and partition/annotation identities.
Ali's objective recomputed both selected scores **exactly** from saved
predictions (1,736 control and 1,662 candidate detections; no selected-epoch
outside-box events). No new inference or training ran during this verification.
Confirmation CUDA allocated peaks were 87,649,063,424 / 87,575,683,072 bytes;
Slurm batch MaxRSS was 17,058,344 / 16,725,076 KiB, distinct from process-only RSS.

The published test set was not used for training, selection or this comparison.
Physical group independence remains unverified; all scores are exploratory
training-only validation results. Original annotations, known duplicates and
prior failures remain preserved. Private backup includes both selected final
checkpoints, predictions, logs, manifests and the executable implementation;
raw scan images are excluded. The 378,802,473-byte local backup matches its HPC
archive hash `1d59c206c971b91c2bde673727fea5f4ba9d25c1095666f9a5b8944a2e696b1e`.
All 2,239 members were safely extracted; all 2,238 manifest-listed files were
rehashed, including both selected checkpoints. Report integration and any separately frozen
published-test evaluation remain distinct work. No Git publication was performed.

## Historical study launch - 22 November

**User deadline amendment, 22 November:** generic only, six attempted
configurations total (including failed attempt 0), then best completed candidate
and untuned control at 100 epochs, seed 17. Specific and repeatability are deferred.
The original 20-attempt definition, journal, RNG and failure remain preserved;
new allocation records bind the separate reduced-scope authorization.

**Job 755 failed in 11m53s**, exit 1:0, during epoch-6 validation after five saved
epoch reports. Its first configuration remains failed with a null objective,
not zero AP. No search attempt is complete. Diagnostic **756 completed** in 25s:
all 2,445 validation images produced 5,880 predictions, including 293 positive
boxes entirely outside the image across 124 images. The fork's clipping collapsed
those boxes; class/score values were valid. Epoch-6 checkpoint SHA-256:
`7cf78283d92dc5cf49522295e8e2b3cca12e7a198207a7921b95abb2a496b0d9`.
The bridge fix preserves original geometry for those detections, retaining them
as unmatched predictions and logging both coordinate sets; it never drops them
or fabricates positive extents. Ali's evaluator is unchanged. GPU qualification **757 completed** in 1m19s, exit 0:0: the prior pilot and
epoch-5 predictions/AP matched exactly; epoch 6 retained all 5,880 detections
including the 293 outside boxes. Diagnostic AP was 0.7858186634414229 and is
excluded from search selection. Selected pilot/epoch-5 AP remained
0.7826704420959958 / 0.7823796805665215. **Job 758 was submitted** for configuration
1 under the revised scope. At 19:20 UAE it was running with one completed validation
epoch (AP 0.5269629247129693, 25,665 detections; no outside-box events). This is
intermediate validation evidence, not a completed comparison. The first
failure can be followed only after a hash-bound implementation amendment; no
completed configurations from different implementations are pooled.

The owned driver schedules one whole attempt per
allocation and resumes only terminal ledger states, preserving Optuna RNG/journal
identity. Only the two authorized generic confirmations follow the six attempts;
the sequence then stops. All jobs use the requested one-GPU/four-CPU/32-GB/four-hour limits;
logs precede submission. The chain stops on failures, interrupted runs, source
changes, insufficient quota, or a projected 100-epoch duration above its bound.
No interrupted optimizer continuation is implemented or promised.

**Pilot 754 completed, exit 0:0, in 7m17s**, qualifying two loader workers and
recorded best/latest checkpoint retention. Its three real validation AP values
were **0.5792557069477533 / 0.7204527031792007 / 0.7826704420959958**. The selected
checkpoint `112ffa3fc937a00bae4e98f0dffacadcc3b14fadb856573ffff18e0b8c73e71f`
passed fresh-process FP32 reload and the generic class map. Full predictions are
losslessly compressed; all three records were independently rehashed and the
selected Ali objective was recomputed exactly. Two unselected snapshot retirements
were checked against saved epoch hashes. Earlier pilot outputs remain intact.
Steady epochs took **99.30 / 99.38 seconds**, versus 166.08 seconds with zero
workers in pilot 750. Batch 32, FP32, partition, initialization and protocol remain
fixed for the study. Allocated CUDA peak was 67,912,593,920 bytes; Slurm MaxRSS was
10,329,168 KiB, including the worker processes. The process-only RSS measurement
is separately retained. These are pilot validation results, not final comparisons.

Latest required local checks: Ruff passed; **490 passed, 13 skipped in 43.06 s**.
Latest Linux validation/allocation/workflow checks: 90 passed; revised controller:
4 passed. Earlier qualified allocation checks follow.
Linux allocation/IPC/retention tests: **108 passed**. Controller tests: **4 passed**
with mocked scheduler calls only. Final Linux launch checks: **39 passed**.
All 203 pinned-fork files and all four original annotation hashes were rechecked.
No shared packages, unrelated projects/jobs, Git history or remote PRs were changed.
The measured full protocol extends beyond the 23 November evidence freeze; report
unfinished stages as unfinished rather than reducing the agreed budgets silently.

The remaining sections retain earlier states and commands. The current study
summary above supersedes their older pending/zero-execution statements.

## Historical successful real pilot and allocation follow-up

**Pilot 750 completed, exit 0:0, in 7m53s** on H100 NVL. Two actual generic-task
epochs trained with the verified general initializer, batch 32, FP32, multi-scale
enabled and zero loader workers. Ali's unchanged evaluator consumed saved real
predictions for all 2,445 validation images each epoch. AP@[.50:.95] values were
**0.5731871184215221** and **0.7126292118034144**. These are exploratory validation
pilot values, not final model comparisons or published-test scores.

Selected checkpoint SHA-256:
`7480a40d365b82e491f765ac3aa8741b046dddf24ee56dd6ee382703160eac9b`.
Fresh-process reload took 2.58 seconds, verified class 0 = Explosive, saved epoch
1 (zero-based), preserved optimizer state and a finite FP32 forward. This proves
reload, not interrupted optimizer continuation. Peak CUDA allocated/reserved
memory was 67,749,156,352 / 94,722,064,384 bytes; process peak host RSS was
3,461,056 KiB. Slurm reported MaxRSS 3,135,536 KiB; these distinct measurement
boundaries are retained. Published test data was not used.

The conservative slowest-epoch projection is 33.79 search + 22.53 confirmation +
22.53 repeatability GPU hours per task, excluding queue/retries. This is a
projection, not completed work. A 100-epoch run at that speed exceeds the requested
four-hour allocation. Account quota inspection found 100 GiB hard limit with
about 51 GiB used. A snapshot is 132,930,921 bytes, so retaining every epoch would
also exceed quota. No 20-configuration search has started yet.

Throughput pilot **752 failed** before its first update: the offline guard blocked
Unix IPC needed by two loader workers. The local fix permits Unix worker IPC while
IPv4/IPv6 and subprocess dispatch remain blocked. New execution support stops a
search allocation between whole attempts and resumes only closed study ledgers;
it does not resume an interrupted checkpoint. Optional retention keeps the
validation-selected best and latest snapshots, recording retired file hashes;
full predictions can be stored losslessly as gzip JSON. Existing pilot outputs
remain intact. Required local Ruff passed; tests returned **465 passed, 12 skipped
in 35.54 s** (including a Windows-only lack of AF_UNIX). A bounded follow-up pilot
is being qualified before using these changes for the study.

## Earlier actual trainer pilot attempts

Generic two-epoch Slurm pilot **749 failed**, exit 1:0, after 2m02s. The pinned
fork transferred **787/799** pretrained weight items into the one-class head;
all 9,779 fit and 2,445 validation images loaded with zero corrupt samples. It
then failed before the first optimizer update: Python 3.12 rejects the integral
floating-point bounds passed by upstream multi-scale `random.randrange`.
No epoch checkpoint, validation AP or search configuration resulted.
Peak host RSS measured inside the process was 1,310,092 KiB; CUDA allocated peak
was 448,966,656 bytes. These are startup measurements, not training capacity.

A scoped adapter converts only integral range bounds to integers during upstream
batch preprocessing. It retains the range, stride rounding, seeded RNG and
multi-scale protocol; installed upstream files are unchanged. Fractional/nonfinite
bounds fail rather than being rounded. Ruff passed; full local tests returned
**457 passed, 11 skipped in 35.25 s**. HPC backend/multi-scale tests returned
**37 passed in 1.45 s**. Retry **750** was submitted with a new output directory;
its result remains pending. Neither pilot counts toward the 20 search attempts.

## Latest execution authorization and prepared data

On 22 November the user explicitly instructed execution without further human
approval. The private authorization records that instruction and scope; it does
not claim Abd reviewed or approved PR22. This supersedes the review wait in the
historical sections below. The remote PR and Git history remain unchanged.

The actual repair command completed for both verified training exports with
`--expected 5`. Only IDs 860, 1435, 2452, 3118 and 3209 changed bbox/area; all other
fields and the original files were checked unchanged. Changed area is derived
bbox width × height. Shared seed-17 membership contains **9,779 fit / 2,445
validation images**, with all task classes present on both sides. Membership
SHA-256: `3a1f364ff80e6e9f6db9cd5fbfc8783270fa42e2968aa136043611d09b1f9e85`.
Exact duplicates are grouped; unverified physical groups retain the exploratory
qualification. Both strict source audits and isolated training bundles completed
in 351.46 seconds; the final check confirmed all four original annotation hashes
unchanged. Test data is absent from both trainer YAML files.

Runtime changes add path/hash-scoped full-object checkpoint loading, verified
local Arial provisioning, in-memory label caches and failure tracebacks. They
preserve shared packages and dataset bundles. Ruff passed; the full local suite
returned **453 passed, 11 skipped in 41.05 s**. Targeted HPC CPU tests returned
**91 passed in 2.54 s**. These checks do not qualify real detector training.
Two-epoch generic pilot inputs passed every execution gate. Training, fresh
checkpoint reload, actual class mapping, Ali's objective and resource timings
still require the pilot. Checkpoint continuation remains unsupported.

## Historical PR22 review follow-up (before execution authorization)

The three supplied review requests are addressed locally, extending Ali's
`ea9a21b` source rather than replacing his tool:

1. The example receipt uses `decision: pending`, with null owner/reference. It
   does not satisfy the policy approval predicate; no human decision was filled.
2. The actual five affected annotations are box-only and source area equals
   bbox width × height. The proposed repair recalculates area for changed boxes
   only and records `source_area`, `derived_area` and the chosen `area_field`
   treatment in schema 1.1. Unaffected annotations/source/test bytes stay unchanged.
3. Repair requires both the verified training file-byte hash and full canonical
   document hash. Membership, categories and annotations are bound to the
   published archive's two inspected train exports. A renamed test/unknown/mixed
   copy cannot pass by its filename or overlapping image IDs.

The new read-only `check --verify-training-source` passed on both real train
exports (five corresponding sub-0.001 px findings). Both actual test exports and
test documents presented with a claimed train hash were rejected. The revised
repair suite passed **16 tests on HPC**. Local Ruff passed; the full requested
suite returned **450 passed, 11 skipped in 34.92 s**, without deselections.
Details and chosen area semantics: [policy](single-scan-data-policy.md).

Private evidence and a four-file patch are in the ignored session's `review-fixes/`
directory. Original PR22 bytes and transfer receipts are retained. These are
**local proposed changes, not a commit/push or a remote PR update**. Human review
remains pending; no actual repair, partition or task training has run. The
23 November evidence freeze and generic-first/specific-second protocol remain
unchanged. Continue at the reviewed repair/pilot gates below after approval.

## Earlier 22 November input and environment evidence

Agent-assisted continuation of Ahmed's workstream, preserving the existing dirty
checkout and untracked files. No commit, reset, push or merge. Authenticated SSH
was established through the user's interactive login; credentials were not saved.
An isolated project directory was created in assigned storage. The unrelated
football project and shared environment were not modified. Private paths, full
logs, package inventories, source manifests and review drafts remain in ignored
`runs/t41-hpc-20261122/`; the authenticated transport records remain in the prior
day's ignored session directory.

The current implementation was transferred as a 124-file archive, SHA-256
`fb8508aa75e584fb8f487c33ff8c238956d263e03d136766fe89a2dc8cdb2eb5`.
Every extracted file was checked against its manifest. A later two-file update
to the offline guard and its tests was applied only after checking the previous
hashes; originals and before/after hashes were retained. The guard now reports
blocked network connections as `OSError`, matching the pinned fork's import-time
connectivity probe; network and subprocess dispatch remain prohibited.

### Public inputs and read-only audit

Assigned storage was inspected before downloading. The public Figshare
`IEDXray_Data_Descriptor.zip` (file 60096533) is 482,371,434 bytes; MD5
`45962e6c4cf2a7acd0d637943f160f58` and SHA-256
`94b691e6a06830e45b84097fad33f937821712b1492272a1300dbad2a4e705f3`
were verified on HPC. Archive paths and CRCs passed before extraction.
The exact THU-MIG v1.1 `yolov10m.pt` is 66,924,323 bytes and matches
`ff2c559f11d13701abc4e0345f82851d146ecfe7035efaafcc08475cfd8b5f2d`.
It is the common general initializer, not an IEDXray task checkpoint.

All **12,224 training and 5,136 test images** were decoded, dimension-checked and
byte-hashed. Generic/specific image tables and annotation geometry correspond.
The findings contain **5 within-train, 112 within-test and 4 cross-split exact-byte
duplicate groups**. Physical groups are absent, not verified independent.
Canonical findings SHA-256:
`4e5ff81087cc7a7b0bcbbf1abf45806e96ebd7936aca35b583d7f33e471ce9f7`.

Ali's four PR22 files were copied unchanged from
`ea9a21b192efaa18101db90c156d38bfac31e509`, with Git blob and SHA-256 checks.
`uv run --locked python scripts/repair_train_boxes.py check --annotations ...`
was executed separately for both actual training exports. In addition to exit
codes, explicit assertions checked **exactly five** matching annotation IDs,
image IDs, filenames and original boxes; every overshoot is strictly below
0.001 px. IDs and values are recorded in [the data-policy follow-up](t41-data-policy.md).
Original annotation hashes stayed unchanged. A preview of original annotations
was inspected; it contains no model predictions or repaired labels.

**The repair has not run.** The user's policy agreement is already recorded in
PR22. The latest inspected PR review/comment lists are empty. The user's quoted
Abd approval concerns merged PR18's evaluator, not PR22's repair implementation
or policy receipt. Abd's implementation review and the human-filled receipt
therefore remain pending. A findings-bound `policy-review.pending.json` has
`review: null`; no agent approval was invented. No fit/validation partition or
YOLO training bundle exists. Published test membership and bytes are unchanged.

### Isolated environment and real Slurm outcomes

The existing Python-3.12 environment is **3.12.16**, with CPU-only Torch and an
incomplete dependency set. The shared Python is **3.10.22**, outside RayGuard's
supported range; its stock Ultralytics is unsuitable. Neither was modified.
A new isolated environment uses Python 3.12.16, Torch **2.9.0+cu126**,
torchvision **0.24.0+cu126**, NumPy **2.2.6**, Optuna **4.5.0** and
pycocotools **2.0.11**. The pinned fork archive matched
`ac5262ab1c7f2ad916496cdf6a00cad62cc5d92c2c6254833d9282d26d4e728f`;
all **203** installed Python/YAML source files matched the extracted revision
`453c6e38a51e9d1d5a2aa5fb7f1014a711913397`. Dependency checks passed.
Exact installed pins, candidate artifact hashes and package inspection records
are retained privately; they are not a completed training qualification lock.

Logs were created before `sbatch`. Both jobs requested the user's
`gpu-student` partition/QoS, one GPU/node/task, four CPUs, 32 GB and four hours;
the environment probe itself had a 20-minute process timeout. GPU work ran only
inside these allocations, on an **NVIDIA H100 NVL**, CUDA 12.6, cuDNN 91002,
with 99,981,918,208 device-memory bytes reported by Torch.

| Job | Scheduler outcome | Executed scope |
|---|---|---|
| 740 | FAILED, exit 1:0, 8 seconds | Tensor forward/backward/update and state-dict reload passed; fork import failed because Matplotlib font discovery attempted a prohibited `fc-list` subprocess. Optuna API/state check passed; general-model reload was not run. |
| 741 | COMPLETED, exit 0:0, 14 seconds | After a CPU-prepared local Matplotlib font cache: kernels, pinned-fork import, hash-verified general initializer load, finite synthetic-input forward, model save and fresh-process reload all passed. Optuna journal/sampler-state roundtrip passed. |

The tiny tensor probe took 0.228 seconds in job 741 and peaked at 68,165,632
Torch-allocated bytes (69,206,016 reserved). These measurements do **not**
estimate detector training time, safe batch or full training memory. GPU samples,
scheduler CPU/time records, errors and checkpoint hashes were preserved. Slurm
did not supply MaxRSS for these short jobs; no host-memory peak is invented.
A separate CPU probe verified two concurrent Optuna journal writers on the
assigned filesystem from one host. Cross-node locking remains untested.
Synthetic Optuna entries are **not T41 configurations**.

The model probe used explicit full-object loading only for a verified source
file and its own hashed roundtrip artifact. This does **not** qualify the actual
trainer's initialization, per-epoch validation, stripping or reload paths under
Torch 2.9. Those paths still need a scoped loading strategy and a real pilot;
do not enable a global unsafe-load override. The live workflow also needs its
required local font assets provisioned for newly created runtime settings.
Task-head transfer, fixed batch, actual Ali validation objective, detector
optimizer updates, finalization, throughput and repeatability remain unmeasured.
Interrupted-checkpoint continuation remains deliberately rejected.

### Checks and next authorized steps

- `uv run --locked ruff check .`: passed.
- `uv run --locked python -m pytest -rN`: **442 passed, 11 skipped in 35.94 s**,
  with no deselections. Skips: nine Windows symlink cases and two optional COCO
  modules in the root CPU environment.
- HPC isolated environment: evaluator/objective/repair tests **32 passed**;
  updated offline workflow tests **36 passed** in the HPC CPU environment.
- Optuna 4.5 journal API and sampler-state restoration were exercised with
  explicitly synthetic values; no scientific metric was produced.

Once the required human receipt and implementation review exist, recheck the
source hashes and apply Ali's `repair --expected 5` separately into new generic
and specific directories. Verify only the intended boxes changed, preserve
source/test hashes, and distinguish the repair record's canonical-content
fingerprint from its file-byte SHA-256. Generate the shared seed-17 training-only
partition, inspect class coverage and produce the reviewed bundles. Complete
runtime asset/loading integration, then run the bounded real-data Slurm pilot
and evaluate actual validation predictions through Ali's objective. Only after
its required evidence passes proceed generic first, specific second, with
20 attempted configurations per task and the documented confirmation/repeatability
stages. Failed/pruned attempts count; synthetic probes do not.

**Current total: zero repaired exports, zero partitions, zero real training
pilots, zero T41 attempted configurations, zero model metrics.** The task is
in progress and the 23 November evidence freeze is unchanged.

## Historical 21 November software completion check


The final review fixed a circular prerequisite in `prepare_training_bundle`:
data preparation required completed training qualification, although the pilot
needs that bundle to perform qualification. Preparation now checks configuration,
task, source identity, partition, audits, conversion and data reviews separately
from execution requirements. No review receipt is filled automatically. Five
regression cases cover both tasks and each required data review. The Slurm
template now explicitly requests one node and one task as well as one GPU.
The HPC output supplied by the user showed shared Python 3.10.22, which is
outside this project's supported range. Inventory and execution now explicitly
reject unsupported Python versions before model access; three regression cases
cover this boundary. The user also listed a separate Python-3.12-named
environment, whose installed packages and suitability remain unverified.

Executed and verified locally:

- `uv run --locked ruff check .`: passed.
- `uv run --locked python -m pytest -rN`: **429 passed, 12 skipped in 43.59 s**;
  the full repository suite was requested, with no deselected tests. After adding
  the Python compatibility checks, the final run returned **432 passed,
  12 skipped in 43.11 s**; Ruff also passed again.
- `uv run --locked python -m pytest tests/test_training_backend.py -q`:
  **33 passed in 12.87 s**.
- Generic and specific planning commands reported `training_started: false`
  and the missing evidence; the package inventory completed without model imports.
- `git diff --check`: passed.

The skips are nine Windows symlink tests, one unavailable Bash runtime, and two
optional COCO metric modules. An isolated evaluation-dependency test invocation
failed during dependency resolution because PyPI DNS was unavailable; no COCO
metric execution is claimed. The default uv cache was not writable in this
session, so checks used a temporary `UV_CACHE_DIR`, `UV_NO_CONFIG=1`,
`UV_PYTHON_DOWNLOADS=never` and `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`.

The software draft is ready for human integration review. The complete T41
experiment remains in progress: actual annotation-policy resolution, a fixed
real partition, execution-host initialization, runtime qualification, pilot,
studies and comparisons are still required. Native interrupted-checkpoint
continuation remains unqualified and blocked. The user reports an HPC login;
the local command session cannot access that separate PuTTY connection. No
training or scheduler submission was performed during these local checks.
A direct SSH attempt from this session returned permission denied. User-supplied
HPC output identified an unrelated football project, no current account jobs,
stock Ultralytics, and missing Optuna/pycocotools in the shared environment.
No approved IEDXray or starting-weight location has been supplied yet. These are
reported terminal observations, not an independently executed HPC qualification.

Current task/status/progress entries now record this distinction. The sections
below preserve the earlier implementation and integration history; their older
counts and statements about untouched status files describe those earlier steps.

## Earlier implementation and integration record

This is local software and synthetic evidence for Ahmed to review. It is not a
completed training study, environment qualification, or a claim of student hours.
The coordinator protocol remains intact. No Git operation, model inference,
real-data processing, training, Optuna study or HPC job was performed.

**Later 21 November integration:** Ali's ten non-progress files from merged
commit `9350482` and Faisal's initialization module/document from `b325c28` are
now present locally, with exact source-byte checks. They retain Ali/Faisal's
authorship; no existing shared file was replaced. The config now calls Ali's
`objective()` and fixes prediction confidence 0.001 / max detections 300 as
explicit project controls. Approval receipts remain unset. A read-only
`training_qualification` module inventories packages and optionally hashes
weights without loading a model. See [data-policy review](t41-data-policy.md)
and [first HPC connection](t41-hpc-first-run.md). The earlier change table and
362-test record below describe the preceding implementation, not this follow-up.

### Follow-up integration checks and remaining scope

Added unchanged from Ali's merged `9350482`: `src/sdp_xray/evaluation.py`,
`coco_metrics.py`, `validation_objective.py`; `scripts/evaluate_generic_yolov10.py`;
`configs/evaluation/generic-explosive-test.json`; `environments/evaluation.in`;
`docs/single-scan-evaluation-protocol.md`; and `tests/test_evaluation.py`,
`test_coco_metrics.py`, `test_validation_objective.py`. His progress entry was
not copied. Added unchanged from Faisal's `b325c28`:
`src/sdp_xray/initialization.py` and `docs/initialization-provenance.md`.
All twelve files matched the pinned source byte identities. No Git command was
used; this is local file integration, not a claim that PR21 was merged or that
the local branch's Git history was updated.

T41 follow-up changes: direct use of Ali's objective in `training_research.py`
and `training_validation.py`; explicit prediction settings in the example;
`training_qualification.py` and `tests/test_training_qualification.py`; installed
interface tests in `tests/test_training_validation.py`; and the policy/HPC guides
linked above. Faisal's shared CLI and his CLI-dependent test file were not copied.
The dedicated T41 tests check his receipt API for both tasks and all three seeds.
His original document retains earlier statements about the matcher/CLI and layer
freezing; the current T41 guides distinguish these from integrated behavior and
the pinned trainer's inherited `.dfl` freezing.

Actual commands in this follow-up, using the locked CPU environment and disabled
pytest plugin autoload:

```text
uv run --locked ruff check .
uv run --locked python -m pytest tests/test_training_qualification.py tests/test_training_validation.py tests/test_evaluation.py -q
uv run --locked python -m pytest --deselect tests/test_model_catalog.py::test_wrong_task_checkpoint_is_rejected_before_importing_model_packages -rN
uv run --locked python -m sdp_xray.training_qualification
```

Ruff passed. Targeted checks: **78 passed in 3.04 s**. The latest partial
repository suite: **423 passed, 12 skipped, 1 deselected in 39.28 s**. All 41
legacy T41 tests passed. Nine skips are Windows symlink privilege, one is Bash
startup, and two are Ali's optional metric-test modules because pycocotools is
absent. The explicitly deselected test executes the prohibited inference runner.
The local Windows inventory exited 0, reported absent model/evaluation packages
and no Slurm allocation, and correctly retained `qualified_for_training: false`.
It read no actual checkpoint and is not an HPC verification.

The actual COCO metric checks were attempted separately:

```text
uv run --locked --with-requirements environments/evaluation.in python -m pytest tests/test_coco_metrics.py tests/test_validation_objective.py -q
uv run --locked --default-index https://pypi.org/simple --with-requirements environments/evaluation.in python -m pytest tests/test_coco_metrics.py tests/test_validation_objective.py -q
```

The first used `UV_OFFLINE=1` and exited 1 because numpy 2.2.6 was absent from
the cache. The second used `UV_OFFLINE=0` and exited 2 because PyPI DNS resolution
failed after retries. No metric test ran in either attempt; no dependency was
installed and root dependencies were not changed. The remaining checks used
`UV_OFFLINE=1`, `UV_NO_CONFIG=1`, `UV_PYTHON_DOWNLOADS=never`,
`PYTHONDONTWRITEBYTECODE=1`, `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` and the same
temporary UV cache. Interface integration tests use a clearly fake metric
backend; their values are not actual COCO results.

Actual HPC hashing, model qualification, pilot and continuation remain unexecuted.
The required first connection is documented from the supplied KU manual:
FortiClient/KU-VPN off campus, then PuTTY/SSH port 22 using the private host in
the manual. No login host, account, credential or private file location is
committed. Human policy review must resolve the train-box findings before the
pilot; no approval is fabricated by this integration.

Suggested follow-up progress note for Ahmed to verify: "Integrated Ali's merged
evaluation source and Faisal's initialization API locally without changing their
implementations. T41 now calls the published objective directly and records
explicit prediction controls. Added a read-only environment/weights inventory
and policy/HPC preparation guides. Ruff and 423 partial-suite tests passed;
12 skips and one prohibited-runner exclusion are recorded. Optional metric tests
could not run because dependencies were unavailable offline and PyPI DNS failed.
No real model metrics, HPC weights verification or training occurred. Remaining:
human Git integration, data-policy/partition approval and an allocated pilot."

## What changed in this update

| File | Purpose |
|---|---|
| `src/sdp_xray/training_workflow.py` (new) | Conditional execution receipts; isolated pilot, search, confirmation and repeatability orchestration; honest timing/accounting and stop handling |
| `src/sdp_xray/training_validation.py` (new) | Convert batch-one detector boxes into Ali's COCO input namespace; call his evaluator with exact identities and coverage; keep model imports lazy |
| `src/sdp_xray/training_backend.py` | Accept bounded pilot stages, retain training-start evidence, recheck approved config/output, preserve the allocated GPU mask |
| `src/sdp_xray/training_research.py` | Keep old candidate behavior; accept separate execution authorization; freeze Ali's objective while retaining old draft inspection |
| `src/sdp_xray/tuning.py` | Separate synthetic and approved orchestration, preserve execution labels, enforce the authorized time budget and reject unqualified live checkpoint continuation |
| `scripts/finetune_yolov10.py`, `scripts/tune_yolov10.py` | Planning by default; incomplete request template; explicit authorization/runtime arguments; no dispatch from planning |
| `configs/finetune.example.json` | Ali's exact objective; unapproved prediction confidence and retained-detection count remain null |
| `tests/test_training_workflow.py` (new) | Fake stage orchestration, execution gates, output collisions, runtime guards, timing, signals/stop behavior and CLI dispatch boundaries |
| `tests/test_training_validation.py` (new) | Generic/specific mapping, valid category zero, empty-image coverage, changed identities and invalid prediction rejection |
| `tests/test_tuning.py` | Update scheduler checks for the four explicit JSON arguments |
| `environments/training/train.slurm` | Forward config/evidence/authorization/runtime, preserve the GPU mask and forward termination; Python reserves the output exclusively |
| `environments/training/README.md` | Document conditional dispatch, offline guard, source qualification and remaining resume limitations |
| `docs/finetuning.md`, `docs/hpc-training.md` | Reconcile current interfaces with the retained coordinator protocol and accurately labelled earlier checks |
| `docs/t41-handoff.md` (new) | This review, usage, remaining decisions, report explanation and progress-entry draft |

Shared manifests, baseline adapter/CLI, evaluator, GUI, root dependencies,
`docs/tasks.md` and `docs/progress.md` were not edited.

## Ali and Faisal interfaces

Ali's [PR18 at 6dfa7d6](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/tree/6dfa7d6f69ae40aec2885c6d5116a3eb776c6ec1)
was inspected after his message. It now provides:

- `sdp_xray.validation_objective.objective()` and `evaluate_validation(...)`.
  The example objective matches it exactly, including pycocotools 2.0.11.
- An approved evaluation protocol must include the ground-truth file SHA-256.
- Matched comparisons require clean and matching inference-code identity.
- `compare-candidates`, with two candidate records sharing the actual starting
  checkpoint hash and retaining distinct output hashes.

Those evaluation modules have now been integrated locally, unchanged from Ali's
merged source. Commit/history integration remains the human-owned Git workflow.
The T41 factory checks that the
installed evaluation source files match the reviewed runtime source hashes.

`training_validation.create(context)` is the production factory entry for the
execution request. It checks the installed objective, predicts every declared
validation image once, maps model indices through class names to original COCO
IDs, converts pixel xyxy boxes to pixel xywh and passes detections to Ali's
function. It does not implement AP. Empty detections remain valid coverage;
missing results, wrong identities or nonfinite metrics fail. Validation requires
original valid `area` and `iscrowd` fields and at least one ground-truth box.

Faisal's general initialization is recorded as official v1.1 `yolov10m.pt`,
66,924,323 bytes, SHA-256
`ff2c559f11d13701abc4e0345f82851d146ecfe7035efaafcc08475cfd8b5f2d`.
This update did not inspect or hash the real file. Both U and T retain this
hash as parent only after the actual initialization receipt verifies it.
The legacy supplied-generic helper retains its original parent behavior.
Training metadata and inference manifests remain separate.

## Planning and future execution inputs

Safe planning commands from the repository root:

```text
uv run --locked python scripts/finetune_yolov10.py
uv run --locked python scripts/tune_yolov10.py --execute
```

Both remain blocked with the unfilled example; `--execute` alone gives no model
access. To prepare an **incomplete** execution request, use a new private path:

```text
uv run --locked python scripts/tune_yolov10.py --config <private-config.json> --evidence <private-evidence.json> --stage pilot --write-execution-template <new-private-request.json>
```

This writes null review/runtime values and returns blocked until actual evidence
exists. Template creation is not approval. Do not commit filled requests, local
paths, weights, scans, runtime logs or receipts containing private information.

The request records stage, config/evidence/implementation hashes, runtime JSON
hash, explicit maximum seconds, pilot epoch budget, interpreter/package versions,
reviewed source-file hashes and the validation factory path/hash. `checks` covers
data conversion, validation adapter, offline behavior, allocated resources,
execution-host weights and environment preflight. `review.scope_sha256` is
`execution_scope(request)`, and a review includes decision, owner and reference.
These fields bind supplied assertions; they do not authenticate a person's approval.
Never populate them merely to clear a gate.
The original research planning-manifest format retains its historical draft gate
labels for compatibility. The CLI's execution assessment replaces those labels
with the actual missing execution receipt and evidence; it does not claim the
newly connected adapter is absent.

The separately reviewed runtime JSON supplies:

| Key | Meaning |
|---|---|
| `weights` | Absolute existing initialization file; bytes must match the receipt |
| `bundle` | Absolute audited derived fit/validation bundle; no test or download key |
| `validation_context.annotation_file` | Validation-only COCO file, bound to the config hash |
| `validation_context.image_root` | Root containing the declared validation images |
| `pilot` | For post-pilot stages: `{path, sha256}` of the completed real pilot stage result |
| `study` | For confirmation/repeatability: `{path, sha256}` of the closed search export |
| `confirmations` | For repeatability: `{path, sha256}` of the confirmation stage result |
| `initialization_receipts` | For repeatability: separately verified receipts keyed by `29` and `43`; never silently rewrite seed 17 |

The factory is the absolute installed `training_validation.py` path, name
`create`, with its actual file hash. Include the installed Ali `evaluation.py`,
`coco_metrics.py` and `validation_objective.py` files in reviewed `runtime_files`,
alongside the actual qualified upstream/runtime sources. `implementation_identity`
binds T41 code; the environment inventory must identify the actual installed fork.
Changing source after review invalidates the request. Freeze
`validation_prediction.conf=0.001` and `max_det=300` are now explicit draft controls;
review them with Ali before pilot selection/study. There is no hidden confidence threshold.

Only after separate real-execution approval, a qualified environment and all
inputs exist does the CLI accept `--authorization <request> --runtime <runtime>
--execute`. Its stage comes from the request. Each stage uses a new owned config
output directory. The Slurm template takes the same four absolute JSON paths;
create `logs` before any separately authorized human submission. It requests one
GPU, four CPUs, 32 GB RAM and four hours under `gpu-student` partition/QoS.

Pilot qualification cannot require a claim that the pilot already happened:
the pilot gate requires reviewed environment preflight. Search and later stages
also require completed train/save/reload qualification, a matching real pilot
receipt, and the full existing study approvals. A fake pilot cannot qualify a
real study. The timer projects epoch-based search/confirmation/repeatability
ceilings; it is not a compute approval or an actual study duration.

The search still counts 20 attempted configurations, including control and
failed/pruned attempts. Confirmation/repeatability are separate stages. Failed
metrics never become zero AP. Stop signals are handled at completed-epoch
boundaries; the Slurm time margin must account for real epoch and checkpoint
duration. Hard kills can leave partial private records.

**Resume limit:** synthetic interrupted resume and sampler-state persistence are
tested. The authorized study API can resume clean trial boundaries; the CLI's
`--resume-from` is inspection only. Real incomplete-checkpoint continuation is
explicitly blocked before a retry because upstream optimizer/RNG/output restoration
has not been qualified. This is a remaining software/runtime recovery task before
promising unattended multi-allocation studies. No silent replay or new independent
configuration substitutes for an interrupted attempt.

## Remaining decisions and actual execution work

1. Integrate the T41 draft, Ali's PR18 and Faisal's initialization receipt through
   the team's human Git/PR review workflow. This update did not open a PR.
2. Review the duplicate/invalid-box/group policy with Ali and Abd. Proposed:
   retain all samples; group exact duplicates and verified related training images;
   preserve/report published-test overlap; use the labelled exploratory duplicate-only
   fallback when physical groups are unknown. Invalid geometry stays blocked.
   A repair policy would require a separately reviewed implementation, source hashes
   and affected IDs; no clipping/deletion/relabeling is implemented.
3. Freeze validation prediction settings, verify the real annotation/partition
   evidence and review generated labels. No real IEDXray files were processed here.
4. Faisal verifies the transferred HPC weights. Qualify the shared-interpreter
   overlay, source/package lock, GPU kernels, training/save/reload, actual head-transfer
   log, effective defaults, safe batch, disk budget and storage locking. Do not
   modify shared packages or reuse inference compatibility as training proof.
5. Approve one named owner, output and bounded pilot. Record measured timings,
   failures and Slurm evidence; then agree study compute and continuation strategy.
6. Execute generic search/confirmation/repeats before specific, and freeze model
   choices before untouched-test evaluation. Report supplied-checkpoint reproduction
   separately from controlled U/T results and paper benchmarks.

These are real dependencies, not additional approval requests for the local
software work already authorized. The report can describe the completed software
now while stating that real experiments remain pending.

## Verification actually performed

The locked CPU environment was used with `UV_OFFLINE=1`, `UV_NO_CONFIG=1`,
`UV_PYTHON_DOWNLOADS=never`, `PYTHONDONTWRITEBYTECODE=1`,
`PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` and `UV_CACHE_DIR` set to the temporary
`rayguard-t41-review-uv-cache` directory. Test/setup paths were inspected first.

```text
uv run --locked ruff check .
uv run --locked python -m pytest --deselect tests/test_model_catalog.py::test_wrong_task_checkpoint_is_rejected_before_importing_model_packages
uv run --locked python -m pytest --deselect tests/test_model_catalog.py::test_wrong_task_checkpoint_is_rejected_before_importing_model_packages -rN
```

Final results: Ruff passed; **362 passed, 10 skipped, 1 deselected in 38.91 s**.
The preceding run took 39.01 s with the same counts. The final rerun followed
the CLI diagnostic adjustment; `-rN` only suppresses repetitive skip-path details.
This is a **partial repository suite**. The one explicit exclusion executes the
prohibited inference runner. Nine tests skipped because Windows symlink creation
lacks privilege; the Bash parser test skipped because Bash cannot initialize its
Windows named objects. Scheduler static checks passed; Bash syntax is not claimed
verified. All 41 original legacy-helper tests passed.

Intermediate commands included `uv run --locked python -m pytest
tests/test_training_workflow.py -q` (initially 30 passed / one timing-fixture failure;
later 34 passed), and `uv run --locked python -m pytest
tests/test_training_validation.py tests/test_training_workflow.py -q` (51 passed).
The fake-clock fixture was corrected; no sleeps or relaxed metric checks were added.
Two import-order findings were fixed with `uv run --locked ruff check --fix
tests/test_training_workflow.py tests/test_training_validation.py` before final Ruff.

A separate temporary Python script executed Ali's inspected source at `6dfa7d6`
in memory with a fake metric backend and blocked optional-package imports. It
passed exact objective equality, both task bridges, the shared-parent comparison,
dirty/different-code rejection and required ground-truth hash checks. No pycocotools,
model or actual AP computation ran. The initial long shell invocation could not
start the packaged shell; running the same check from a temporary script succeeded.
Ali's own optional metric suite was not installed or run in this checkout.
Both default CLI commands above returned exit 2 with `training_started: false`.
A separate whitespace check of the 16 edited files passed, including LF-only
line endings for the Slurm script; no Git command was used for that check.

## Suggested PR description for Ahmed's own GitHub action

Title: Connect T41 training stages to the reviewed validation interface

The T41 draft now has a conditional workflow for a bounded pilot, sequential
search, confirmation and repeatability. It uses Ali's frozen objective and calls
his evaluator through an explicit checkpoint/detection adapter, while preserving
the existing candidate helper, public-test isolation and common-initialization
provenance. Default execution remains blocked by missing real evidence.

Validation: locked Ruff and the permitted partial CPU suite passed. Only fake
trainers/predictors and tiny synthetic files were used. Remaining qualifications
include the actual execution environment, data-policy disposition, HPC weights,
prediction controls and live checkpoint continuation. Shared interfaces and
evaluation files are unchanged; integrate the corresponding PR18 code before
runtime qualification. Full check details are recorded above.

## Plain-English presentation explanation

The pipeline checks the data and starting weights before it permits training.
It keeps the published test set separate and builds one fixed validation partition
for both tasks. The untuned and tuned models start from the same verified weights,
so their comparison measures the training choices rather than different starting
models. Each completed epoch gets a saved checkpoint; Ali's evaluator scores its
validation predictions. The search records failures and interruptions instead of
turning them into successful results. The tests check these software rules using
tiny invented inputs. They do not show that the model detects explosives accurately.

## Draft progress entry for Ahmed to verify and add personally

21 November 2026 — Extended the T41 local software with conditional execution
requests, pilot/confirmation/repeatability orchestration and a checkpoint-to-detection
bridge to Ali's PR18 validation interface. Updated the example to the published
objective and retained explicit unresolved prediction settings. Checked common-parent
compatibility without changing shared interfaces. Ruff passed; the permitted partial
repository suite had 362 passed, 10 platform skips and one prohibited-runner test
excluded. No real data, weights, training, Optuna studies or HPC jobs were used.
Remaining work: human integration/review, data-policy decisions, verified HPC
initialization/environment, real checkpoint-resume qualification and an approved
bounded pilot. Software checks do not establish model quality. This entry needs
Ahmed's verification; no student hours or independent implementation claim is implied.
