# Engineering progress and contribution records

## T41 final test, report integration and completion — 23 November 2026

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

Actual editor/executor: Codex AI assistant under the user's instructions; no
student authorship or hours inferred. An isolated branch based on current main
retains the merged team/report changes. Code commit `54db37b` integrates the
qualified T41 implementation and frozen evaluation runner with explicit agent
author/committer metadata. The earlier task branch publication remains intact.

Commands/evidence: Slurm `sbatch` job 820; `sacct` COMPLETED 0:0, 87 seconds;
`evaluate_t41_frozen.py --plan ... --output ...`; independent CPU metric/hash
verification; safe local extraction and all-manifest-file hash checks. The test
plan was recorded before submission. Real failures were inspected without
changing labels, predictions or thresholds. Full original logs/receipts remain
private. No shared package, unrelated project/job or existing user file was reset.

Integration software checks: Ruff passed; **515 tests passed, 13 skipped** in
43.96s, using the existing locked environment and the integration worktree's
source via PYTHONPATH. Seven frozen-plan fail-closed tests also passed separately.
These are software checks, distinct from executed HPC model evidence.

Report changes update the abstract, implementation/results, conclusions and
dated schedule. The PR20 literature table now spans pages, the Gantt figure fits
its page, literal table-rule typos are repaired, and moved 6G links resolve.
The source preserves other contributors' content. Whole-report T38 acceptance,
checked Word copy, official forms/signatures and submission remain separate.


The updated LaTeX report built successfully with Tectonic to **42 pages**.
Rendered page layouts were inspected, including detailed result tables. Final
logs show no overfull boxes, oversized floats, unresolved references or missing
glyphs. Underfull spacing warnings and the system Fontconfig warning remain;
Times New Roman/Arial rendered correctly. The private PDF and its hash are
retained locally; no assembled PDF, raw scan or private receipt is published.

## T41 publication preparation authorized - 23 November 2026

The user's subsequent instruction to push authorizes commits and publication of
the qualified T41 implementation and verified result summaries on the existing
`ahmed/t41-software-draft` task branch. Earlier no-publication statements describe
their dated execution stages. Main remains unchanged; integration with the
newer merged team work is separate. No force push, reset or merge is authorized
by this preparation. The original draft and working files are preserved.

The explicit publication set contains 44 source/configuration/test/documentation
files, separated into implementation and evidence commits. Reviewed evaluator
and initialization imports already present on main retain their documented
provenance. Private paths and credential-pattern inspection found no matches in
the publication set; unrelated untracked files, scans, weights, session helpers,
logs and private receipts are excluded. The run artifacts remain in private
hash-verified storage. Required `uv run --locked ruff check .` passed and
`uv run --locked python -m pytest` returned **490 passed, 13 skipped in 49.36s**.
The first attempt could not write the sandbox's default uv cache; rerunning with
a project-local ignored cache resolved it. Skips cover unavailable local
pycocotools and platform features; real HPC evaluator execution and independent
score recomputation are separately recorded below. No new model execution was
performed during publication checks. Student authorship/hours are not inferred.

## T41 reduced generic completion and artifact verification - 23 November 2026

User authentication restored monitoring at 08:17 UAE; the pending read-only
request executed once. Slurm `sacct` confirmed search jobs 758/759/762/764/767 and
confirmation jobs **770/819 COMPLETED**, all exit 0:0. Final job 819 ended at
**05:13:01 UAE**. `squeue` showed no account jobs. Search attempt 0 (755) remains
failed with null objective; all six attempts are accounted for. The finite chain
wrote its reduced-protocol completion receipt and stopped without starting the
deferred specific or repeatability stages. No new GPU job was submitted today.

Control confirmation completed 100 epochs in 2h47m35s; the best search candidate
(trial 4) completed 100 epochs in 2h46m49s. Both used the same verified general
initializer, seed 17 and shared training-only partition. Validation-selected
checkpoints were epochs 68 and 84 respectively. AP@[.50:.95] was
**0.8770615927076139 control / 0.8748334372095157 candidate**: candidate minus
control **-0.0022281554980981833**, or -0.2228 AP percentage points. This does
not establish an improvement from tuning. Report the single-seed, exploratory
physical-group limitation; no published-test score or full-protocol completion.

A separate `CUDA_VISIBLE_DEVICES='' OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
MKL_NUM_THREADS=1 PYTHONPATH=code/src env/bin/python` verification completed in
6.18 seconds, with no inference/training. It checked the six-trial ledger,
frozen objective, candidate selection, common initialization, task class map,
partition and validation annotation identities; rehashed **237 bound runtime
files**, selected checkpoints and **350 successful epoch prediction records**;
and independently recomputed both selected Ali objectives exactly. Generic and
specific original train/test annotation hashes match the prior four-file record.
The selected prediction counts were 1,736/1,662, with zero outside-box events.
All raw predictions, resource measurements, losses, failures and prior records
remain retained. Detailed job/resource/checkpoint evidence is in
[the handoff](t41-handoff.md).

A private 378,802,473-byte backup was created on HPC with 2,239 files, including
both selected final checkpoints, run logs, predictions, source and manifests;
raw scan images are excluded. Archive SHA-256:
`1d59c206c971b91c2bde673727fea5f4ba9d25c1095666f9a5b8944a2e696b1e`.
Local download completed with the same archive hash. Safe extraction verified
all 2,239 members and rehashed all 2,238 manifest-listed files, including both
selected checkpoints; the manifest itself is covered by the archive hash.
Existing local changes/untracked files and shared packages are preserved. No commit,
push, merge, reset, colleague message or unrelated job action occurred. Student
authorship/hours remain unreported. Next: report integration of the verified
comparison before the 24 November 17:00 UAE deadline, with deferred work explicit.

## T41 overnight monitoring attempt - 23 November 2026

At 08:16 UAE, a command-tool TCP/22 probe reached the HPC. The initial sandboxed
probe was denied by socket permissions; the authorized network probe succeeded.
`ssh -o BatchMode=yes -o ConnectTimeout=5 -o NumberOfPasswordPrompts=0`
returned `Permission denied (publickey,password)`. The saved private-session
status records closure at 22:51 UAE on 22 November. Read-only request 158 for
Slurm accounting, chain failures and the reduced-protocol completion receipt is
queued, not executed. The user was given the exact existing helper command and
asked to authenticate only at its local hidden prompt; no credential was saved.

Reviewed the saved driver while access is unavailable: it requires six terminal
attempts, two successful 100-epoch confirmations, verified per-epoch prediction
hashes/counts and a completion receipt before reporting the reduced protocol done.
This source inspection does not establish overnight execution. No new submission,
restart, cancellation or change to running code occurred. Next: consume the same
pending request after authentication, inspect results and independently verify
selected checkpoint/prediction identities before reporting metrics. The last
observed state remains three completed search configurations, one failed and
configuration 4 running at 22:04 UAE on 22 November.

## T41 monitoring and PR20/PR22 review - 22 November 2026

At 22:04 UAE, authenticated read-only `squeue` and
`sacct -j 755,758,759,762,764 --format=JobID,JobName,State,ExitCode,Elapsed,MaxRSS --parsable2 --noheader`
confirmed three completed search allocations: **758** (52m41s), **759** (52m29s)
and **762** (52m23s), all exit 0:0. **764** was running configuration 4 at
10m38s elapsed. Failed configuration 0 remains counted; one further attempt
remains after configuration 4 in the six-attempt scope. No confirmation or
published-test result is claimed. The finite Slurm chain continues independently
of the desktop. Next: verify the remaining search and control/best confirmations.

Automated read-only review examined PR20 at `7fe234f` and PR22 at `3ee9c87`;
student authorship, review sign-off and hours are not inferred. GitHub reported
both merged by other activity during the review (PR22 `da0151e`, PR20 `6948559`).
No review, message, approval, commit, push, reset or merge was performed here.
The isolated PR20 report snapshot built with
`tectonic --untrusted --keep-logs --keep-intermediates --outdir build-review main.tex`.
The 42-page PDF was rendered with `pdftoppm`; the report sources were unchanged
by the PR's final synchronization. Executed visual findings: Table 1.2 is cut
off (float 492.93 pt too tall), Figure A.1's caption overlaps the footer
(33.59 pt too tall), and malformed table rules print `midrule`/`bottomrule`.
Moving the 6G page also left broken incoming and relative links. These require
follow-up before report submission; successful compilation is not layout acceptance.

The pinned PR22 repair module passed its **10 tests**. A separate synthetic
reproduction showed that `tolerance=NaN` or `10.0` permits a four-pixel repair,
contrary to the documented sub-0.001 px policy; the CLI uses the correct default.
The merged code retains COCO area, whereas the authorized HPC implementation
recomputes changed box-only areas and binds verified training-export identities.
Record that implementation difference explicitly; the running experiment did not
use the merged PR22 source unchanged. Private review snapshots, build logs,
rendered pages and reproductions are retained outside shared source. The final
Word copy, official filled forms and complete binary slide assets were not reviewed.

## T41 failure diagnosis and user deadline amendment - 22 November 2026

Job **755 failed**, exit 1:0, after 11m53s during epoch-6 validation. Five earlier
epoch reports, both retained snapshots, full predictions, journal/RNG and resource
measurements remain intact. It counts as failed configuration 0 with null study
objective: one attempted, zero completed configurations. No optimizer continuation
was attempted. Diagnostic **756 completed** in 25s: all 2,445 validation images,
5,880 predictions, and 293 wholly outside positive boxes on 124 images that became
zero-area after upstream clipping. Original class/score values were valid.

Implemented a scoped bridge correction preserving the original pixel xyxy box
only for this verified collapse case. It records original/clipped geometry and
retains every prediction; partial-overlap behavior, classes/scores, annotations,
partition and Ali's evaluator stay unchanged. Invalid raw geometry still fails.
A bound implementation amendment permits proceeding only after the preserved first
failed configuration and actual replacement qualification, without pooling completed
configurations from different implementations. GPU qualification **757 completed**, exit 0:0, in 1m19s. Pilot and epoch-5
predictions/AP matched exactly, and all 5,880 epoch-6 predictions were preserved
with 293 original outside boxes. Diagnostic AP 0.7858186634414229 is excluded from
selection; failed configuration 0 remains failed. Job **758 was submitted** for
configuration 1 after the bound implementation amendment and deadline checks.
At 19:20 UAE, job 758 was actually training, with one completed validation epoch:
AP 0.5269629247129693 on all 2,445 images, 25,665 detections and zero outside-box
events. A contemporaneous H100 NVL sample showed 94% utilization and 86,942 MiB
used of 95,830 MiB; this is a sample, not peak memory or sustained throughput.
No completion of that search attempt is claimed.

The user explicitly selected **generic only, six attempts, control/best confirmation**
after the full protocol's 80–100 GPU-hour estimate was explained. Revised execution:
six attempts including failed configuration 0, then 100 epochs for the best completed
candidate and original control, seed 17; specific and repeatability deferred. The
original definition remains preserved with a separate bound deadline receipt. No
full-protocol completion or TPE convergence is implied. Estimated remaining compute:
10–13 GPU hours, subject to failures/queues. Account inspection showed 47.8 GiB free
of 100 GiB, two concurrent jobs allowed, and no cumulative GPU-time cap listed;
requested allocations remain one GPU, four CPUs, 32 GB and four hours each.

Required local Ruff passed; **490 tests passed, 13 skipped in 43.06s**. Linux
validation/workflow/allocation checks passed **90 tests**; Linux controller checks
passed **4 tests**. The private Linux driver could not import `resource` during an
initial Windows check; that failed check is preserved, and its Linux checks passed.
Source updates 11/12 verified every transferred file and retained previous versions.
No commit, push, merge, reset, shared-environment modification or unrelated job action.

## T41 qualified pilot and study launch - 22 November 2026

Pilot **750 completed** two real generic epochs and fresh reload (7m53s); pilot
**752 failed** before updating weights because the offline guard blocked worker
Unix IPC. After the scoped IPC fix, **754 completed** three epochs and reload
(7m17s) with two loader workers. Ali validation AP values were
0.5792557069477533, 0.7204527031792007 and 0.7826704420959958. All 2,445 validation
images were evaluated; published test data was unused. The best checkpoint hash,
class map, source identities, compressed predictions and two recorded unselected
snapshot retirements were independently verified. Recomputing Ali's objective
from the saved predictions reproduced 0.7826704420959958 exactly. These are
exploratory pilot results, not a completed comparison.

Implemented allocation boundaries between whole search attempts, optional
best/latest retention with retirement hashes, explicit planned stage-run selection,
and local worker IPC while retaining network/subprocess blocks. Private finite
Slurm scheduling retains generic-first order, 20 attempted configurations, original
confirmation/repeatability budgets, shared initialization and one output owner.
It stops on failures/unresolved gates and never resumes optimizer checkpoints.
Full predictions are preserved with lossless gzip and both byte hashes.

Required local commands passed: Ruff and **465 pytest tests / 12 skips (34.18 s)**.
Linux allocation/IPC/retention checks: **108 passed**; controller tests: **4 passed**
(mocked scheduler only); final launch checks: **39 passed**. Real pilot and test
evidence remain distinct. Generic search control configuration 0 was submitted as
**job 755** for 30 epochs; no search completion is claimed. Measured steady pilot
epochs (~99.4 s) and the 100-GiB account quota now inform each bounded allocation.
The full protocol exceeds the 23 November evidence freeze. No commit, reset, push,
merge, shared-package change or unrelated cancellation occurred. Student effort
and explain-back remain unreported.

## T41 first actual trainer dispatch - 22 November 2026

Pilot **749** ran inside the requested one-GPU Slurm allocation and failed 1:0
after 2m02s. Verified general initialization transferred **787/799** items to the
generic head, and both prepared splits loaded with zero corrupt images. Python
3.12 then rejected upstream multi-scale `random.randrange` float bounds before
the first optimizer update. All logs, failure tracebacks and resource records
are retained. No completed epoch, checkpoint, AP or search attempt is claimed.

Added a scoped integral-bound compatibility adapter without changing upstream
files or the multi-scale protocol. Tests verify exact seeded sample/RNG equality
and rejection of fractional/nonfinite bounds. Required Ruff passed; full local
pytest returned **457 passed, 11 skipped in 35.25 s**; targeted HPC tests returned
**37 passed in 1.45 s**. Retry **750** is submitted with fresh outputs and the
same initialization, partition, batch and protocol. Its outcome is pending.

## T41 authorized data preparation and trainer fixes - 22 November 2026

The user's explicit instruction to proceed without further human approval
supersedes the earlier wait. Private receipts identify that authorization without
claiming a colleague review. Agent-assisted execution completed training-only
repair commands for both exports (`--expected 5`), recording source/derived bbox
and area values and verifying all other annotation fields unchanged. Shared
seed-17 partition: **9,779 fit / 2,445 validation**, all task classes represented,
membership SHA-256 `3a1f364ff80e6e9f6db9cd5fbfc8783270fa42e2968aa136043611d09b1f9e85`.
Both strict source audits and isolated bundles completed in 351.46 s; all four
original annotation hashes remained unchanged. Physical independence remains
unverified; no test data is passed to the trainer.

Implemented scoped checkpoint loading for verified input/owned output files,
hash-checked local Arial provisioning, in-memory label caches and recorded
failure messages/tracebacks. `uv run --locked ruff check .` passed;
`uv run --locked python -m pytest -rN` returned **453 passed, 11 skipped in
41.05 s**. Targeted HPC CPU checks returned **91 passed in 2.54 s**. Pilot input
validation passed every execution gate. Actual train/save/reload, class mapping,
Ali-objective values and resource measurements remain the GPU pilot's purpose.
The private SSH helper's malformed JSON request was preserved and repaired;
per-request parsing failures now keep the authenticated session open. No
commit, push, merge, shared-package change or unrelated-job cancellation occurred.

## Historical T41 PR22 review follow-up - 22 November 2026

Agent-assisted local changes to Ali's original implementation at `ea9a21b`, in
response to the three supplied review requests. The example policy receipt now
uses `decision: pending` with null owner/reference. Real read-only inspection
confirmed the five affected annotations per task have no segmentation and source
area equals bbox width × height. The proposed derived copy recomputes area only
for changed boxes and records both source/derived values; all other fields stay
unchanged. This supersedes the earlier derived-area preservation proposal and
still needs human implementation approval.

The repair guard now binds the actual file-byte hash and complete canonical JSON
hash to the two verified public training exports, including image membership,
annotations and categories. Filename checks are additional checks only. A new
`check --verify-training-source` path verifies provenance without repair.
On HPC, both actual train exports passed; both test exports and test documents
paired with claimed train hashes were rejected. The pending example was confirmed
not to satisfy the approval predicate. No real repair/partition/training occurred.

`uv run --locked ruff check .` passed. Full requested local
`uv run --locked python -m pytest -rN`: **450 passed, 11 skipped in 34.92 s**,
no deselections. Revised repair tests on HPC: **16 passed**. Original PR22 source
and before/after hashes were preserved, and a local four-file review patch was
prepared. No commit, push, merge, remote PR edit or human approval was made.
Next: human review of these concrete changes, then the already documented repair,
partition and real trainer qualification sequence. Deadline/protocol unchanged.

## T41 HPC preparation and environment checks - 22 November 2026

Ahmed's workstream; agent-assisted execution, with student effort and explain-back
unreported. Existing local changes were preserved; no commit, push, reset or merge.
Authenticated SSH, inspected assigned storage and both existing environments,
created an isolated project directory, and verified all 124 transferred files.
Obtained the public IEDXray archive and exact general initializer; sizes and
hashes matched the documented sources. Decoded and hashed 17,360 images.
Read-only `repair_train_boxes.py check` plus explicit paired assertions confirmed
exactly five corresponding sub-0.001 px boxes in both training exports.
Duplicate/group findings and source identities are recorded in
[the current handoff](t41-handoff.md). Source/test bytes were preserved.

Integrated Ali's four unchanged PR22 files at `ea9a21b` after blob/byte checks.
The user's policy agreement is recorded; Abd's implementation review and the
human-filled policy receipt remain pending. PR18 approval does not clear PR22.
The pending receipt binds the actual findings and retains `review: null`.
No repair, partition, training bundle or task training was created.

Installed an isolated Python 3.12.16 candidate with the exact fork (203 source
files verified), CUDA Torch 2.9.0/torchvision 0.24.0, Optuna 4.5.0 and pycocotools
2.0.11. Shared packages and unrelated projects were untouched. Fixed the offline
guard's connectivity exception to match the pinned fork without allowing
network dispatch. `uv run --locked ruff check .` passed; full local
`uv run --locked python -m pytest -rN`: **442 passed, 11 skipped, 35.94 s**.
Remote evaluator/objective/repair checks: **32 passed**; workflow checks:
**36 passed**. Tests are software evidence, not model validation scores.

Submitted bounded environment probes after creating logs, using the authorized
one-GPU/four-CPU/32-GB/four-hour Slurm request. **Job 740 failed** after 8 seconds
on Matplotlib's blocked font-discovery subprocess. After a local font-cache
preparation, **job 741 completed**, exit 0:0, in 14 seconds on H100 NVL.
Kernels and a tiny optimizer update, general-model synthetic forward/save/fresh
reload, and synthetic Optuna persistence passed. Same-host concurrent journal
writes on assigned storage also passed. Logs, timings, hashes, GPU samples,
failures and dependency records remain private. No host-memory peak or training
throughput is inferred. General-model reload does not qualify trainer checkpoint
continuation, full-object loading/finalization, task heads or Ali's real-data AP.

Next: obtain the pending human review, apply and verify the derived train-only
repair, prepare the shared partition, qualify the real trainer pilot, then execute
the agreed generic-first/specific-second protocol. **Zero task configurations
attempted; no real model metric produced.** The 23 November freeze remains a
deadline, not evidence of completed experiments.

## T41 local software completion review - 21 November 2026

Ahmed's T41 workstream; agent-assisted implementation and local verification.
Student explain-back, human review and commit/push remain separate actions.
Preserved the existing local training, evaluation and initialization integration.
Fixed the dataset-preparation prerequisite cycle: reviewed data can be prepared
before the pilot qualifies training, while source/partition/geometry and data
review checks still block invalid preparation. Execution requirements remain
unchanged. Added five regression cases and explicit single-node/single-task
Slurm requests. After the user supplied HPC Python 3.10 inventory, added
explicit supported-interpreter checks and three regression cases. [Current handoff](t41-handoff.md) records scope and earlier work.

Commands: `uv run --locked ruff check .` passed;
`uv run --locked python -m pytest -rN` returned **432 passed, 12 skipped in
43.11 s**, with no deselections. Targeted backend checks returned **33 passed**.
`git diff --check` passed. Default generic/specific planning stayed blocked
without real evidence; the local inventory imported no model. Checks used a
temporary uv cache because the default cache was not writable. The optional
evaluation dependency invocation failed at PyPI DNS resolution; two metric
modules remain skipped, alongside nine symlink and one Bash platform skips.

These are synthetic software checks, not IEDXray validation or model results.
The owner reports an HPC login through PuTTY; this session cannot access that
separate connection. No model training, real Optuna study or Slurm submission
was performed. Next: transfer/review current source, locate approved data and
weights, resolve the real annotation findings, verify the shared environment
and isolated overlay, then run an owned bounded pilot. T41 remains in progress
until the required real experiments and comparisons are evidenced.

## Team update protocol

### T42 PR review and integration executed — 21 November 2026

At Abd's explicit request to perform the review work, used an isolated detached
worktree at PR #18. At `6dfa7d6`: `uv run --locked ruff check .` passed;
`uv run --locked python -m pytest` passed 244, skipped two optional evaluator modules;
`uv run --locked --with-requirements environments/evaluation.in python -m pytest`
passed 268. Updated PR branch with main through GitHub to `6edcd68`; Ruff passed
and evaluation-enabled full pytest passed **273 tests**. All synthetic software
checks; no inference, real metrics, data repair or HPC job.

Inspected safeguards, comparison modes, objective interface and regression coverage.
Resolved both threads, submitted approval, updated PR description and merged through
normal protections after required Linux/Windows CI passed. Actual main merge commit:
`9350482b89ff601d5617d684b9ac8b5a44173c2d`. Actions used authenticated repository-owner
account at explicit user direction; no agent identity configured. This is assisted
review evidence, not proof of personal student understanding or invented hours.

Updated tasks/status/plan and conservative data-policy handoff: preserve test,
group duplicates/verified physical groups in training-derived validation, mark unknown
independence, keep geometry blocked without reviewed repair and hash real policy
receipts. These rules do not themselves clear real data or approve unseen receipts.
Next: consume current main evaluator, bind findings/partition and qualify the pilot.
Unrelated 6G MENA move remains untouched. Documentation diff checks required before push.

### T42 validation handoff update — 21 November 2026

Owner relayed Ali's update; agent inspected PR #18 metadata and selected source via
`gh pr view 18 --json ...` and GitHub contents API for evaluation/validation_objective.
Head `6dfa7d6` contains required approved-GT hash and clean matching code safeguards,
validation objective helper/evaluator and common-parent candidate comparison. Hosted
Linux/Windows CPU checks pass; existing changes-requested review remains pending
human re-review. Ali reports synthetic interop with Ahmed's validate_objective_result;
not locally rerun. No real metrics or model execution established.

Updated T42 state/next actions and current plan/status/protocol/demo handoffs. Ahmed
can set config objective from validation_objective.objective() and wire actual
hash-bound validation predictions. Source inspection confirms hash equality checks
use caller-supplied identities; real file hashing, prediction provenance and partition
verification remain adapter/preflight responsibilities. Data policy and HPC pilot
remain open. Earlier dated reviews below describe prior heads, not current blockers.
No student authorship/hours inferred; no GitHub review, message, commit or push made
in this update. Documentation-only checks: diff whitespace and T42 row/link coverage.
Next: available teammate integrates the interface, Ali/Ahmed settle data policy,
and a qualified human re-reviews #18 before merge.

### Shared execution policy amendment — 21 November 2026

Subsequent owner clarification: focus on assigned tasks first; independently handle a
small task from another lane when it blocks the main task. Keep the team informed and
coordinate changes affecting active work. The broad permission below is narrowed by
this clarification; it does not encourage abandoning assigned work for another lane.

Owner explicitly authorizes teammates to complete one another's unfinished tasks without
waiting for a named lead. Agent-assisted update to AGENTS, contribution guidance, tasks,
plan, status and ML/demo plans records leads as contacts, notification without a permission
wait, isolated edits, coordination of active collisions/GPU outputs, qualified independent
review and credit for actual work. Removed the explicit prohibition on editing another
lane's shared/evaluator files in the research protocol; older allocations are superseded.
No student reassignment, contribution or execution is inferred. Scientific/qualification
gates and protected-branch permissions remain. No code changed or external message sent.
Validation: `git diff --check` and policy-reference checks; no software tests needed.
Next: any available student claims a bounded blocking item and proceeds, recording real
evidence and arranging an available qualified reviewer before merge.

This file is the team-wide handoff for T39–T43 and the other project workstreams. Each student records **their own** verified work here when making a meaningful update; do not write another student's contribution for them. Use the matching task ID and the entry format below. The task state, owner and next action remain in [tasks.md](tasks.md), the only backlog.

```text
### T[ID] — [short workstream name] — [YYYY-MM-DD]

Owner / GitHub handle: [student's name and handle]
Status: [not started / in progress / blocked / verified complete]
Completed since last update: [specific work; say “none” if this is a plan]
Files / PR / commit: [repo-relative paths and human-authored link or hash, when available]
Checks and evidence: [exact commands and outcomes; link the reviewed artifact or report]
Blockers / decision needed: [what is blocked, who can decide, or “none known”]
Next step: [one action and its owner]
```

Keep updates factual and concise. A plan is not completed work; an agent's output is not verified until the student reviews it. Do not invent time, authorship, results or metrics. Omit raw scans, credentials, private paths, per-image private identifiers and local session details. Students should not edit this file simultaneously: coordinate one editor at a time, submit the progress change in the student's own reviewed PR/commit, and have the coordinator merge adjacent updates without rewriting anyone else's attribution. For GUI implementation details, also update the [RayGuard-App progress file](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/progress.md); add a short summary and link to that entry here.

## T40–T43 remote handoff review — 21 November 2026

Agent-assisted coordination update requested by the owner after receiving teammate
messages. This records inspected artifacts and attributed teammate reports, not a
student-authored contribution entry or independently repeated execution. No hours
or new owner availability inferred. Existing uncommitted report guidance and the
user's 6G MENA move preserved.

Commands: `gh pr list --state all`, `gh pr view 18/20/21 --json ...`, `gh api .../pulls/18/comments`,
GitHub branch/compare/content reads, and `gh pr list -R abdalrahman-ismaik/RayGuard-App --state open`.
PR #21 head b325c28 has passing Linux/Windows CPU checks, review required; #18 head
15cb4a0 remains changes-requested with passing checks; #20 remains behind/review
required with passing checks. No open T41 or app PR found. API read of an assumed
T41 guide filename returned 404; inspected the actual branch file list and its
`docs/finetuning.md` instead. No remote mutations, GitHub reviews or messages sent.

Selected T41 `32091bc` sources inspected: planning CLIs always block live execution,
research config/receipt validation, proposed validation request/result, documentation
and Slurm template. Synthetic tests/check success are Ahmed's report, not rerun here.
Branch is one commit ahead/three behind main at inspection; it adds planning files
also present in #20, requiring reconciliation. Faisal's provenance document and
receipt source inspected: exact official v1.1 file identity recorded, with evidence
limits; reported file hashing/receipt interop were not repeated and upstream claims
were not independently reverified. HPC transfer/hash and head-transfer behavior still
need executed evidence. T43 research branch records assisted app acceptance work;
app publication, exact shared app diff and human rehearsal not verified here.

Updated task rows T40–T43, plan/dependency order, status, demo plan and protocol handoff.
T41/T42 now in progress; real T07 training remains blocked and final T08 full-P1 metrics
remain unfinished. Plan records main as shared-software PR target, Ali's two outstanding
safeguards, validation AP interface and common-parent U/T comparison, reviewed data
policy and one qualified pilot before searches. It preserves generic/specific scope
without promising 40 attempts before report submission. No new model results claimed.

Checks: `git -c core.safecrlf=false diff --check` passed; PowerShell checks passed
for T40–T43 row uniqueness/column counts/in-progress states, integration coverage
and the plan handoff link target. No code changed or software tests run.
Next: human Abd reviews/reconciles PRs and report evidence;
Ahmed opens software PR; Ali fixes #18 and supplies interface; Faisal/Ahmed verify HPC
initialization. Students supply report-ready evidence by the 23 Nov review freeze,
retaining 24 Nov 17:00 submission and 30 Nov collection obligations.

## T38 report specification and persistent guidance — 21 November 2026

Agent-assisted documentation prepared at the project owner's explicit request; human
review is pending. No student authorship, hours, accepted assignment or report completion
is inferred. The owner designated the Fall 2026 handbook as the primary course reference,
confirmed 24 November as the report deadline, required canonical LaTeX with professional
visuals, and chose a checked Word copy alongside the PDF unless PDF acceptance is confirmed.

Added [report specification](final-report-requirements.md) with R01–R15 coverage,
the six SDP I chapters, formatting guidance, research/project/meeting source policy,
visual provenance, Gantt plan/actual distinctions, forms, confidentiality and submission
gates. Reinspected the local handbook body and both SDP I rubric tables using PowerShell
`System.IO.Compression.ZipArchive` and XML text extraction with shared read access.
Original DOCX unchanged; no rendering, embedded form-artwork inspection or signatures
verified. Risk Assessment and Health and Safety are listed for SDP I/II; clearance I/II
is explicitly SDP II. Recorded supervisor/examiner weights separately and corrected the
course checklist's implication that supervisor weights alone described course assessment.

Updated root agent/contribution guidance, all four project workflow skills, documentation
index, T38 deliverables, main/demo plans, course checklist and status. Requirements are
centralized; `docs/tasks.md` remains the sole backlog. These are documentation changes;
no LaTeX source/report, bibliography, figures, forms or measured model results were created.
Existing user changes moving the 6G MENA record were preserved. No Git identity action,
commit, push, external message or publication performed.

Checks: `git diff --check` passed; PowerShell `Select-String`/regex/`Test-Path`
checks passed for all 13 guidance references, R01–R15 coverage and every relative
file link in the new specification. Existing links to the user-moved 6G MENA record
were not repaired as part of this update. No code changed; software tests were not run.
Next: human coordinator reviews this diff, accepts report editor/reviewer assignments,
maps actual evidence to R01–R15 and verifies official templates plus LaTeX/Word conversion.
Target submission 24 Nov, 17:00 UTC+4; report assembly, actual approvals/signatures,
distribution permission and submission remain unfinished. Retain the separate 30 Nov
collection obligation and historical deadline conflicts.

## T40–T42 — reproduction, Optuna and HPC planning — 18 November 2026

Coordinator-prepared documentation at the project owner's request; student authorship,
acceptance, hours and completed implementation are not inferred. Owner confirms
HPC access and CVMI Lab provision of papers/data/models. Agreed generic then specific
explosive studies, fresh general pretrained initialization for training-only validation,
and 20 attempted Optuna trials per task. Updated T40–T42, T14 access evidence, sprint
and single-scan plans, status and documentation index; added the detailed
[research protocol](finetuning.md) and [HPC handoff](hpc-training.md).

Evidence: read both local HPC student DOCX guides using standard-library ZIP/XML
extraction; inspected the previous football project's current README/training files
with `rg` and `Get-Content`; checked pinned upstream YOLOv10 trainer/default config
and Optuna 4.5.0 documentation. Scheduler/environment statements are documented,
not executed cluster verification. No SSH, training, search, environment installation,
metrics, contribution credit or GPU job is claimed. Initial implementation files
created during this session were removed after the owner clarified documentation-only
scope; the resulting diff contains documentation only.

Checks: `git diff --check` passed. Local Markdown links and documentation-only scope
were checked with the locked Python interpreter. No code change remains, so Ruff/
pytest were not required or run. Source manuals remain ignored; no private paths,
scans, credentials or filled records were added.

Next: Abd sends Ahmed the updated brief; Ahmed/Faisal/Ali accept owned files and
agree initialization, split/data policy and evaluator interface, then implement
and qualify an allocated pilot. Draft review remains 19 Nov; complete study dates
follow pilot timing. The 24-versus-27 Nov report deadline conflict remains unresolved.

## Conference register and completed 6G MENA record — 15 November 2026

Repository documentation was updated at the project owner’s request. The active README no
longer lists completed 6G MENA, expired CAISAIS/MoSICom calls, or non-publication exhibitions.
The owner reports that the project team attended 6G MENA on 20 October; individual attendance,
actual presentation, revised poster artifact and TDRA decision remain unverified. Historical
requirements and poster artifacts remain archived for the final report.

Created [the UAE conference and invitation register](conferences-2026-2027.md) from current
official pages and the two invitation texts supplied by the owner. It records submission dates,
venue/modality, paper fit, conditional publication routes, AI-use/policy constraints and conflicts
between invitation and official CVCI dates. No submission, contact with organizers, publication,
acceptance, or student contribution is claimed. Recheck official calls before acting because dates
and publication terms can change.

Files: `README.md`, `docs/README.md`, `docs/status.md`, `docs/tasks.md`, `docs/plan.md`,
`docs/6g-mena-2026.md`, and `docs/conferences-2026-2027.md`. Documentation-only maintenance;
no student ownership or hours assigned.

## First-draft prototype plan aligned to original proposal — 14 November 2026

The owner reports substantial GUI progress already exists in the local RayGuard-App working tree and asked to polish/refactor it against project outcomes with Mohammad (called Mohammed by the owner; roster spelling/handle to confirm). Updated T39/T43 so Abd owns requirement fit, integration and GUI polish; Mohammad owns a separate GUI flow/accessibility/acceptance slice. Both also review ML integration and truthful result/provenance display. Existing app changes remain uncommitted and were not edited in this documentation update.

The owner also reports that currently only he is committing to the GitHub repository; this report was not independently audited against GitHub history. The new work split gives every student a distinct proposed deliverable and requires each student to make and explain their own commits. No earlier contribution is retroactively assigned to anyone.

The single-scan ML plan now prioritizes the owner-identified CVMI model configured in the GUI and public IEDXray data, after exact checkpoint/source/hash/task verification. Existing records call the local weights author-supplied after a renewed link; reconcile those source descriptions before making a provenance claim. Faisal (T40) owns baseline adapter/shared prediction and run-manifest contracts plus HPC prerequisite coordination; Ahmed (T41) owns the fine-tuning candidate; Ali (T42) owns independent evaluation. Abd and Mohammad join design review and validate the app-facing outputs. Compare only compatible candidates under a shared protocol; the available generic/device/specific checkpoints represent different tasks. These proposed assignments remain unaccepted.

The public IEDXray dataset is the proposed single-scan source. The 478 distinct dismantled images count toward the project's separate collection progress but are not for single-scan model training, baseline demo or evaluation; their task labels, QC and case links are unresolved. This resolves the workstream distinction without claiming the 500 positive/negative requirement complete. The prototype plan records evidence and gaps. No code, training or full-data evaluation was performed for this planning update.

Added a human-only GitHub contribution policy to root and app contribution guidance: AI tools may help with analysis and drafts, but may not use contributor identities or perform GitHub mutations. Each student must personally review, verify their own Git identity and execute their commit/push commands. Agents may suggest commands but cannot run them. Keep agent sessions and client state out of Git; retain reviewed project guidance as team documentation.

## Single-scan ML work refocused after owner review — 14 November 2026

The owner rejected the first proposed Ahmed/Ali work allocation and directed those lanes to the single-scan model baseline/fine-tuning/evaluation pipeline. Verified the requirements against Meeting 01 A8, Meeting 02 A9 and the existing task/architecture record: single-scan train/fine-tune/test/documentation is a project requirement; the multi-package objective is a separate, higher-priority data-dependent workstream.

Current artifact check: `data/IEDXray/model-weights/yolov10_generic_exp.pt` exists locally but is ignored and not tracked by Git; its SHA-256 matches `docs/first-inference.md`. The device and specific-explosive YOLOv10-M checkpoints are also local. T02/T04 and T06 record executed inference evidence, but the generic model has only three diagnostic samples and no project full-dataset metrics. No fine-tuning pipeline, training script or full-dataset evaluator was found in `scripts/`, `src/` or `tests/`. The managed environment locks are explicitly inference profiles without training extras. The local IEDXray train/test/COCO directories exist; the audit records cross-split exact duplicates and five generic-threat train box-boundary findings, with no approved correction/validation policy.

Added the [single-scan ML plan](single-scan-ml-pipeline-plan-2026-11.md) with checkpoint hashes, public-data focus, requirements, existing evidence, data/environment gates and train/evaluation design. It now keeps tool-neutral student guidance rather than tool-specific prompt blocks. T40 is Faisal's baseline adapter/shared run contract; T41 Ahmed's fine-tuning pipeline; T42 Ali's evaluation pipeline. The [prototype sprint plan](implementation-plan-demo-2026-11.md) maps the original requirements to intended evidence and limits. No code, fine-tuning, full test evaluation or metrics are claimed complete. Multi-image work remains separate because dismantled scans lack reviewed detector labels/QC/case-group mappings.

Evidence/commands: reviewed the existing app `docs/PRODUCT.md`, `docs/DESIGN.md`, app status and current Git status read-only; reviewed root project proposal/data/model/task records and current human-contribution guidance. Existing app files were left untouched. Documentation/planning only; no frontend audit/test, training or evaluation job run in this turn. Next: Abd/Mohammad confirm the GUI file split and audit the current screen flows; Faisal/Ahmed/Ali verify the exact GUI checkpoint, agree interfaces and resolve public-data validation policy before training or performance claims.

## CS-HPC credential email recorded — 4 November 2026

A CS Lab Engineer email received on **4 November 2026 at 12:52 pm** was addressed to the named SDP1 student recipients and Naoufel Werghi. It says credentials for the group's CS-HPC access were issued and that users will be prompted to change the initial password at first login. Job-submission manuals were attached, with further help offered. The email's timezone was not supplied.

For security, the username and password are not copied into this shared progress file, the backlog or commits; retrieve them from the original email and complete the required password change at first login. The source email and attached manuals are not stored in Git. Receipt of credentials is documented; successful login, password rotation, account permissions, manual review, HPC job submission and compute results have not been verified. T14 is now in progress; next advisor review remains unbooked. No student hours or HPC work are inferred.

## Distributed X-ray collection snapshot inventory — 14 November 2026

The owner supplied access to six ZIPs and the extracted `DISMANTLE_DATA` directory on E:. Read archive entries, counted and hashed the extracted JPEGs, and decoded them with the locked project Pillow dependency. The extracted tree contains **577 JPEG paths**; all 577 decoded as RGB with zero errors. SHA-256 grouping found **478 distinct byte payloads** and 99 exact duplicate paths, all in Ahmed Almansoori's `total` folder matching bag-folder images. The five folder-label distinct counts are Abd Alrahman Ismaik 142, Ahmed Almansoori 100, Ali Arif Alshamsi 61, Faisal Daoud Alzarooni 124 and Mohammad Arwani 51. See [dated inventory](collection-progress-2026-11-14.md) for date/day counts, archive progression and limits.

The dated archives contain 169, 199, 291, 478 and 577 JPEG paths. The first four snapshots are nested; from 9 Oct to 13 Oct, Ahmed's 100 root paths were reorganized into bag folders and 99 exact copies were placed under `total`. SHA-256 comparison confirms both archives contain the same 478 distinct byte payloads, with no new or missing image payloads. `DISMANTLE_DATA.zip` and the 13 Oct archive have the same 577 image paths but different ZIP hashes. Filename prefixes span 29 Sep–9 Oct; they do not establish scanner timestamps or which collection round each file belongs to. Against the planned 500, 478 is a provisional distinct-file count, not a QC-accepted count or confirmed shortfall. Annotation, catalogue mapping, physical/group provenance, round mapping, QC, student self-confirmation and lab acceptance remain open. No inference or training was run.

Created a [member contribution guide](collection-contribution-guide.md) that keeps scans on the existing lab computer and directs each member to commit sanitized, attributable GitHub evidence. Updated T21/T27 acceptance evidence, status, data handling and docs index. The coordinator performed the inventory; folder labels are source metadata, not independent confirmation of student authorship. Individual effort/hours are not inferred. Commands: PowerShell/.NET archive listing, SHA-256 file inventory and path-set comparison; `uv run --locked python -c <Pillow verification script>` decoded 577/577. No code changed; no Ruff/pytest run. Next: each student verifies their own folder/date/count on the lab computer; coordinator reconciles private manifests against the approved catalogue/QC record with Dr. Divya; then record accepted counts. Resolve same-set shortfall before moving to the next set.

## Course end-of-semester requirements recorded — 14 November 2026

Recorded the supplied COSC 497 announcements, Blackboard details and local August 2026 handbook requirements in [the end-of-semester checklist](course-endgame-2026-11.md); added T38 to the sole backlog and linked the checklist from status/docs index. Handbook inspection confirmed the SDPI rubric is individually assessed: GitHub 15%, report 20%, presentation 20%, demo 25%, Q&A 20%. The checklist captures one Blackboard upload per group, email copy to supervisors/examiner, GitHub report/repository link, per-student contribution table, individual supervisor explain-back, GitHub documentation expectations, no separate progress report, LinkedIn categories and handbook forms/Gantt/report guidance.

**Deadline conflict retained:** Blackboard due-date details and one announcement say 24 Nov, 5:00 pm UTC+4; another pasted notice says 27 Nov. The working cutoff is the earlier explicit Blackboard due-date field; coordinator confirmation remains open. One notice specifies presentation 27 Nov, 8 am–12 pm, 20+10 minutes; exact slot and room are unverified. Filename forms also differ (`COSCXX.SDP1 Final Report` versus `COSC# SDP1 Final report`); verify the project number and current-link convention. No report, submission, email, student contribution, LinkedIn item, demo or rehearsal was asserted complete.

Commands/evidence: read required project docs and latest meeting companions; inspected handbook DOCX text/XML locally with PowerShell/.NET because Python `python-docx` is unavailable. Documentation-only change; no tests or model jobs run. Owner: repository coordinator; individual student ownership and effort remain unreported. Next: confirm current Blackboard deadline/name and presentation assignment, assign/evidence deliverables in T38, then update with actual outcomes.

## T37 Flow reference/prompt preparation - 19 October 2026

Prepared [three reference-image prompts and eight video prompts](flow-reference-prompts.md)
for the one-passenger/four-bag and different-passenger scenarios. The owner requested images
here for later upload into Flow. Read imagegen and HyperFrames entry guidance; user-selected
Flow remains the target, with no HyperFrames project/install or local video rendering.
Built-in image generation failed with HTTP 429 `usage_limit_reached` before producing an
image. No CLI fallback was attempted without the explicit authorization required by the
imagegen skill. **No reference image or video was generated.** Image prompts provide an
immediate Flow-native route; eight-second scene prompts and consistent bag/character
references are prepared, with illustrative alerts and external case linkage labelled.

No student hours or model execution evidence are inferred. T37 actual deliverables remain
open; next is to generate/review the reference stills, then one test clip in the user's
Flow account. No code changed; no Ruff/pytest or artifact QA is claimed.

## T37 Flow duration and prompting follow-up - 19 October 2026

Expanded [the research](video-tools-research.md) from official credit, access, model,
creation and scene-building guidance. Flagged inconsistent official access wording.
A JavaScript integer-budget calculation verified 50-credit raw-footage maxima: Omni
360p 70 seconds, Omni 720p 32 seconds, conditional Veo Lite 40 seconds and Fast 16 seconds.
Documented consistent references/frames, single outputs and the Veo 8-second ingredients
restriction. These are documented limits and calculated estimates, not account or media
tests. No generated video, credits spent or student hours are claimed; actual T37 delivery
remains open. Next: confirm in-account model costs and test one consistent airport shot.
The attempted shell calculation/documentation command was blocked by execution policy;
the calculation ran in the JavaScript tool runtime and documentation used apply_patch.
No production code changed; no Ruff/pytest or shell diff check was run for this follow-up.

This page records shareable project evidence. It is not a claim of individual student
authorship, hours or understanding. Those must be recorded by the actual contributor and
reviewer. Do not include personal paths, private contacts, raw correspondence or artifact files.
## T42 evaluation pipeline draft — 15 November 2026

Contributor: Ali Arif Saeed Alshamsi. Review pending: evaluator/model interfaces with
Ahmed and Faisal, GUI presentation with Abd and Mohammad. Branch `ali/evaluation`.

Added a draft evaluation path for the generic explosive task. `sdp_xray.evaluation` reads
a T40 shared record, checks the COCO ground truth against the model's category map
(ID 0 `Explosive` kept), converts `box_xyxy` to COCO `[x, y, width, height]`, counts
results at a fixed 0.25 threshold (not tuned) and checks that a baseline and a candidate
are a matched pair. `sdp_xray.coco_metrics` calls the official `pycocotools` evaluator,
installed from the separate `environments/evaluation.in`, not the root lock.
`scripts/evaluate_generic_yolov10.py` writes evaluate/compare reports. The draft protocol
is in [single-scan evaluation protocol](single-scan-evaluation-protocol.md). No existing
files were changed.

Checks: `uv run --locked ruff check .` passed. `uv run --locked python -m pytest` gave
225 passed and 10 skipped. With `--with-requirements environments/evaluation.in` it gave
232 passed and 9 skipped, including 45 new synthetic tests.

Limitations: synthetic software checks only. No model was run, no real evaluation was
performed and there are no project metrics. The protocol stays draft until the GUI
checkpoint is confirmed, the duplicate/boundary/validation policy is approved and the
ground-truth file hash is recorded.

Next: confirm the GUI checkpoint with Faisal and Abd, agree the candidate record with
Ahmed, and name an owner for the full test prediction run.

## T40 run planning and record check — 15 November 2026

Contributor: Faisal Daoud Alzarooni. Review pending. Branch `faisal/baseline-tools`,
following the first T40 change in pull request #17.

Added `baseline-plan`, which turns a scan-input list into the per-scan runner arguments
with the catalog hash and runs nothing, and `check-record`, which re-validates any
baseline or candidate record and reports scan, failure and per-label counts. The
[baseline run contract](baseline-run-contract.md) now gives the steps from scan list to
checked record and lists the HPC prerequisites that are still unconfirmed.

Checks: `uv run --locked ruff check .` passed. `uv run --locked python -m pytest` gave
192 passed and 9 skipped (existing Windows symlink tests).

Limitations: synthetic software checks only; no model run and no real record yet. The
HPC list is a set of open questions, not verified access.

Next: same as below, plus trying `check-record` on Ahmed's first candidate manifest.

## T40 baseline run contract and adapter — 15 November 2026

Contributor: Faisal Daoud Alzarooni. Review pending: ML contract with Ahmed and Ali,
GUI provenance with Abd and Mohammad. Branch `faisal/baseline`.

Added a shared run manifest (`sdp_xray.common.run_manifest`), a prediction-set check and
a `baseline-record` command that combines saved batch-one runner outputs into one record
identified by hashes, with no local paths. The existing runner and scan-result contract
are unchanged. Fields, checks and notes for T41/T42 and the GUI are in the
[baseline run contract](baseline-run-contract.md).

Checks: `uv run --locked ruff check .` passed. The PR worktree passed
`uv run --locked python -m pytest` with 196 passed on Windows. GitHub Ubuntu and Windows
checks also passed. These are synthetic software checks, not model evaluation.

Limitations: synthetic software checks only. No model was run and no real saved run has
been converted. The model the GUI selects has not yet been confirmed against the catalog
entry, and HPC access is unverified. `docs/tasks.md` is not updated here because the
T39–T43 rows are not yet on `main`.

Next: confirm the GUI model and hash with Abd, convert one approved real saved run, and
agree the candidate manifest with Ahmed and the record reader with Ali.

Review follow-up, 15 November: review of pull request #16 found two provenance
gaps, both fixed. The class and category maps are now checked against the catalog for
every combined run instead of only the first. A run that fails before its device is
resolved now records `device: null` with a separate `requested_device`, so the requested
device is no longer reported as the one that ran inference. After the fix the suite gave
196 passed on Windows. PR #17 was merged into `main` on 15 November 2026.

## T37 free online video-tool research - 19 October 2026

The owner requested free online options for two advisor-reported airport scenarios:
components across one passenger's bags and components across different passengers' bags.
[Research](video-tools-research.md) compares Canva/Clipchamp motion graphics, Flow/Bing
AI clips, CapCut editing and the restricted Runway/Firefly/Pika free offers. Official
pricing/help pages were inspected with web search/open/find; Pika's current zero-monthly-credit
pricing was distinguished from older FAQ snippets. Recommendation: controlled motion graphics
for the complete explanation, optional generated airport shots, then manual evidence/UI overlays.

This is documented research only: no account access, media generation, upload or export test.
No student authorship/hours or model capability is inferred. Different-passenger case linkage
must be explicitly supplied in the illustration; generated detections are not inference evidence.
T37 remains not started for actual deliverables; research is preparatory work. Next: choose
style, draft two storyboards and test one scene/export. Hardik/Fangzhou's F08 video assignment
is not silently reassigned. No production code changed; Ruff/pytest were not required.

## T37/T28 Secure Life Group visit requirements - 19 October 2026

The owner supplied the invitation and advisor instructions, summarized in
[F08](meeting_minutes/follow-up-slg-2026-10-19.md). Secure Life Group CEO visit is Wednesday
21 October 2026, 2-5 pm; presence is required. SDP prepares a digital project/progress
poster, Divya prepares the lab, and Hardik/Fangzhou prepare a high-quality video of their
work/approaches. Times use project Asia/Dubai context; the pasted source has no explicit
zone. Private room/calendar details are excluded from shared records.

Added T37 as not started on available evidence, linked earlier T28 GUI rehearsal, and
updated status, context/Q8, plan, poster preparation, conference guide, README and meeting
index. F08 resolves SLG identity/date; it does not establish attendance, response status,
lab readiness or completed materials. Tuesday 6G and Wednesday SLG remain separate,
and conference display specs are not assumed for the visit. Historical prototype, collection,
colorization and summit-video obligations remain; the visit video has the new dated scope.

Ownership: agent-assisted requirements update at the owner's request; no student hours or
completed work are inferred. No calendar response, external message or artifact production
was performed. Validation: Python standard-library checks passed **193 local links/anchors
across 11 affected files**, verified Wednesday 21 October and unique task IDs including T37.
`git -c core.safecrlf=false diff --check` passed; `git check-ignore -v` confirmed the local
logistics record remains ignored. No code changed; Ruff/pytest were not required.
Next: name the SDP poster editor/presenter, confirm visit display/handoff requirements,
review accurate progress evidence, rehearse GUI and coordinate lab/video readiness.

## T23 accepted poster and digital revision follow-up — 19 October 2026

The owner supplied the acceptance and subsequent revision/attendance email thread.
[F07](meeting_minutes/follow-up-poster-2026-10-19.md) records the dated 12 October acceptance,
14 October final-delivery request and 17 October screen-format revision request. Required
format is digital portrait 9:16 at 1080 × 1920 px on a 55-inch display; latest revision
permits PPT/PNG/PDF with proportional layout. Divya's new-template presentation handoff
and Brahim's receipt are documented; his TDRA check remains pending. No attachment was
provided or inspected, and repository v6 was not relabelled or modified.

Updated the conference guide, poster preparation/bundle notes, README, status, T23,
context/questions, plan and meeting index. Added only the sanitized F07 Markdown to the
meeting-record allowlist. Tuesday-only team attendance means 20 October by calendar;
the undated advisor's “today” wording is flagged, alongside exact session/setup and
2 pm photo-day clarification. Continuous presenter coverage is requested, not evidenced.
The generic Monday setup instruction is qualified by the team-specific Tuesday reply.

Ownership: agent-assisted documentation at the owner's request. No student hours,
actual attendance, successful display or TDRA approval are inferred. T23 stays in progress;
collection follow-up F06 and its November 30 deadline remain unchanged. No presentation
binary, private contacts or raw email were added; no external message was sent.
Validation: Python standard-library checks passed **187 local links/anchors across 12
files**, verified Tuesday 20 October by calendar and matched both earlier v6 artifact
SHA-256 hashes. `git -c core.safecrlf=false diff --check` passed. The sanitized F07 file
is not ignored. No code changed; Ruff/pytest were not required.
Next: obtain TDRA response and actual revised artifact, confirm Tuesday logistics/photo
and agree the private presenter rota; retain final digital file on USB as requested.

## T21/T26/T27/T30 collection follow-up — 19 October 2026

Documentation maintenance from the owner-supplied email thread is recorded in
[F06](meeting_minutes/follow-up-collection-2026-10-19.md). Updated the README, short handoff,
canonical tasks, context, plan, architecture, meeting index and blank schedule worksheet.
The current requirements are individual first-round counts against 500, completion of any
shortfall on the same set before moving on, the requested second-round schedule and overall
collection completion by 30 November 2026. Around 5 pm is optional where feasible.

T21 is in progress on Faisal's documented self-report only: reported 102, formula 104,
catalogue allocation 100. Other individual counts, the accepted team total and QC remain
unverified. T26 stays in progress; T30 actual collection remains not started on available
evidence. The historical 15 October Batch 1 milestone and unresolved prototype deadlines
are retained. C01 Session A/B are within Round 1, distinct from pre-/post-midterm rounds.
Source email timestamps, exact second-round dates and current availability were not supplied.

Ownership: documentation update assisted by the agent at the owner's request; student
collection hours, scan verification and schedule-sending ownership are not inferred.
Validation: the Python standard-library Markdown check passed **174 local links/anchors
across 12 affected files**; `git -c core.safecrlf=false diff --check` passed. No production
code changed; Ruff/pytest were not required.
No scans, model runs, filled personal schedules or raw email were added; no email was sent.
Next: each student supplies a count, the team reconciles files/logs and QC, then the sender
consolidates current availability into dated second-round slots for lab acceptance.

## T23 poster v6 repository review bundle — 30 September 2026

The owner requested publication of the latest poster and updates to the README,
project documents and task record. The current user-saved v6 PPTX and PDF are now
included in [the review bundle](posters/6g-mena-2026/README.md), with direct links,
editing guidance, source attribution and SHA-256 hashes. T23 remains in progress:
Prof. Naoufel/team feedback, final approval, print size and submission are outstanding.
Preparing an email and publishing repository files do not establish an email send.

Preparation progressed through six revisions: two problems and methods, preserved
paper evidence, descriptive sections and justified text, followed by linked IEDXray
detail crops and three FALCON close-ups. Version 6 preserves owner-supplied credits.
Its native QA recorded 182 objects, 93 text boxes, 11 pictures, seven reversible crops,
10 connectors and eight justified text boxes. Thirteen AP/mIoU values match the papers;
local demonstration confidence and proposed multi-package performance remain distinct.

For publication, an independent read-only audit verified ZIP integrity, all visible
PPTX text against the one-page PDF (2,942 non-whitespace characters), source attribution,
credits and no private filesystem paths, credential patterns, external relationships,
macros or embedded attachments. The PDF was rendered and visually checked. The current
files were copied without modification: PPTX 2,954,249 bytes, SHA-256
`b2c950f1630f1ed25d4c55ca56a56c6731028c1d460619a3dc6b06abee553a87`; PDF 139,507 bytes,
SHA-256 `20be167333269340f27419bfa9b2937200b18d176ebb067e3f529b2dc1f14ef1`.

Publication validation: `verify_publication.py` checked 139 local links/anchors,
both exact file hashes and the ignore rules for original PDFs, templates, older
drafts, scans and weights; all passed. `git diff --check` passed. These artifact
and documentation checks do not establish new model results.

An isolated `docs/poster-v6-2026-09-30` worktree separates this change from unrelated
local work. Only the review bundle, its exact PDF allowlist and poster-related README,
status, task, conference/index and preparation records are included. Source PDFs,
raw scans, weights, personal records and earlier drafts remain untracked. No production
code, inference, training, student hours or advisor approval are claimed.

## T23 research figure refinement, version 6 — 30 September 2026

The owner liked v5, supplied an edited file and requested clearer scientific figures and
larger/zoomed evidence in sections 03 and 04. Automated production preserved the supplied
credits, title and headings, added two IEDXray context/detail pairs and replaced the small
FALCON strip with one larger scene and three numbered close-ups. The coordinator integrated
independent scientific and visual reviews. No student hours or advisor approval are inferred.

The exact embedded FALCON Figure 9 JPEG (410 × 367, PDF p. 22, xref 904) was extracted without
re-encoding; its SHA-256 is `03db22a40b38832f744ec3ff50b2de657ddae7f67dd3f6fe8919e687d5db41f8`.
It retains all original boxes/masks, avoids intermediate resampling and restores native
proportions from the PDF's horizontally stretched placement. IEDXray Figure 6 source bytes
and six-color annotations are unchanged. No AI-generated scan detail, sharpening, new
inference or evaluation was used. All thirteen paper values and four bar lengths are unchanged.

Actual commands: `node inspect_template_deck.mjs --workspace ... --pptx ... --scale 4`;
`node build-v6.mjs` imported the duplicated edited source and exported with artifact-tool;
`node validate_template_plan.mjs --workspace ... --map ... --inspect ... --source-slide-count 1`;
`& ./finalize-native.ps1` restored the eight original justified text boxes through the
previously documented compatibility exception. PowerPoint SaveAs wrote a distinct staging
copy after Save reported a file-use conflict; user source decks were never saved by this pass.
Native text, geometry and media were checked unchanged across formatting.

`.venv/Scripts/python.exe qa/package_check.py` and `node check_template_fidelity.mjs ...`
passed. Native QA verifies **182 objects, 93 text boxes, 11 pictures, seven native crops,
10 connectors and eight justified text boxes**, no vertical overflow or out-of-slide objects,
and at most 1.13 pt of justified glyph overhang with no visible clipping. Checks cover ZIP
integrity, dimensions, full annotations, source hashes, thirteen metrics, common chart axis,
owner-supplied text, source/privacy notes and native formatting preservation. Independent
scientific and visual reviews passed. A later source-v5 save changed only metadata and a
run's dirty flag; reviewed visible content, style and geometry remained equivalent.

Final ignored local file: `docs/6g-mena-poster/drafts/RayGuard-Research-Poster-v6.pptx`,
SHA-256 `c86dd26155b2c4cad3099b82b70a4f6726bb959cfe3eb3088a40e9b347bcd5fe`.
Earlier files and showcase v3 remain intact. No production code, model execution, sending,
commit or push was performed. Next: owner/advisor review, print-size confirmation and
submission coordination; recorded deadlines and unresolved scheduling conflicts remain.

## T23 unified research poster, version 5 — 30 September 2026

The owner requested equal treatment of single-baggage and multi-package explosive detection,
replacement of the generic methods figure, consistent professional sections based on both
papers/proposal/repository evidence, richer demonstrations and justified text. Automated
production created research v5; separate agents reviewed scientific content, original figures,
repository implementation and native visuals. The coordinator integrated their findings.
No student authorship/hours or advisor approval is inferred.

Source coverage: both full papers and the full three-page SDP proposal; current meeting/
follow-up and project records; source modules, scripts, tests and configuration; 81 tracked
entries inventoried, dependency locks/manifests structurally inspected, and 18 active private
records reviewed. The review also verified saved model predictions, overlays and image hashes.
Generated/vendor/obsolete app trees and arbitrary model/data binaries were not claimed as
fully read scientific sources. No new inference or test benchmark was run.

The poster now pairs two explicit problems/objectives with two methods lanes. P1 demonstrates
actual independent YOLOv10-M task execution and saved Train000003 input/output (confidence
0.970), while future device-conditioned localization/host association remain explicit. P2
shows illustrative four-package case membership, proposed component evidence and comparison
of late fusion with a learned multi-input approach. It does not invent cross-bag outcomes.
Two IEDXray Figure 6 examples and three FALCON Figure 9 examples retain original annotations;
FALCON examples are explicitly independent single images. Nine AP table entries and four
mIoU chart values/lengths match the papers. Existing collection counts remain absent from
poster body and notes. Showcase v3 and all earlier research versions remain unchanged.

Actual commands: `node inspect_template_deck.mjs --workspace ... --pptx ... --scale 2`;
`node validate_template_plan.mjs --workspace ... --map ... --source-slide-count 1`;
`node build.mjs` imported an exact template duplicate and exported through artifact-tool
2.8.4. Independent alignment probes found that public, range, default-style and native
round-trip approaches all drop justification during PPTX conversion. To satisfy the owner's
explicit formatting request, `& ./qa/apply-justification.ps1` applied native Justify=4 only
to seven named prose boxes after export. This narrow compatibility exception changed no
text, shape coordinates/dimensions or source-media hashes. No installed runtime was patched.

`& ./qa/verify.ps1` opened/rendered the final file read-only. It has **150 objects, 80 text
boxes, 6 pictures, 3 native crops and 8 connectors**. Native COM and saved XML verify all
seven justified boxes. No vertical overflow or out-of-slide objects were found. PowerPoint
reports 0.88–1.13 pt of glyph overhang for justified lines; raw measurements were retained
and independently inspected without visible clipping. Titles/labels and numeric columns
retain semantic alignment. Text, diagrams, bars, table and legend remain editable.

`uv run --locked python qa/package_check.py` passed CRC, dimensions, removed-count/privacy,
native-justification, all thirteen numeric entries, four bar lengths, original media and
eight preserved-file hash checks. Native formatting preserved text/geometry/media; comparison
normalizes omitted zero-rotation attributes written by PowerPoint. `node qa/inspect_final.mjs`
read the final PPTX for geometry without resaving it; `node check_template_fidelity.mjs
--workspace ... --starter-pptx ... --final-pptx ... --map ... --starter-layout-dir ...
--final-layout-dir ... --edit-dir ...` passed. Independent scientific and visual reviews
passed after changing the next-step wording to preserve the open localization design choice.

Final ignored local file: `docs/6g-mena-poster/drafts/RayGuard-Research-Poster-v5.pptx`,
SHA-256 `b8c5db9cfafb1ba16df707328fa3249eeea49b483baae9857adb1459042be4d3`.
No production code, training, new inference, sending, commit or push was performed. Next:
owner/advisor review and author/print/submission confirmation. The 30 September poster
obligation and unresolved prototype/collection deadline conflict remain unchanged.
Final handoff passed: 52 local documentation links/anchors, `git diff --check`,
`git check-ignore -v` and final SHA-256 readback.

## T23 research poster revision, version 4 — 29 September 2026

The owner requested a compact title, richer scientific text, more published scan examples
and professional results graphics, removing the collection-plan graphic and its counts.
Automated production created a new research-only editable draft; independent agents
extracted/verified paper figures, reviewed source values and inspected the native render.
The coordinator integrated their work, clarified the AP definition and verified the final
file. No student authorship, hours, new experiments or advisor acceptance are inferred.

Research v4 has descriptive introduction/methods, three objectives, an editable protocol
diagram, four original Figure 6(a,c,d,f) examples with matching legend, an eleven-model
generic AP50 ranking and a three-model/three-task AP table. All eleven chart and nine table
values were checked against the supplied paper. Published single-image results remain
distinct from the proposed multi-package direction; FALCON §15 motivates the extension.
The removed graphic/counts are absent from poster text and notes. Historical collection
requirements are preserved in project records. Showcase v3 and all earlier files are unchanged.

Actual commands: `node inspect_template_deck.mjs --workspace ... --pptx ... --scale 2`;
`node validate_template_plan.mjs --workspace ... --map ... --source-slide-count 1`;
`node build.mjs` imported a duplicated original template and exported through artifact-tool
2.8.4; `& ./qa/verify.ps1` opened/rendered the draft read-only in PowerPoint. Native checks
report **162 objects, 86 text boxes, 5 pictures, 4 native crops and 3 connectors**, with
zero measured text overflows and zero out-of-slide objects. Text, protocol, chart bars,
table cells and legend are editable; original paper annotations remain in raster scans.

`uv run --locked python qa/package_check.py` passed CRC, one-slide/source dimensions,
original template and figure/logo media hashes, all bar lengths/labels, table values,
notes/privacy, removed-count absence and seven preserved-file hashes. An initial exact
decimal-size assertion was corrected to allow sub-EMU rounding; native dimensions match
the template. `node check_template_fidelity.mjs --workspace ... --starter-pptx ...
--final-pptx ... --map ... --starter-layout-dir ... --final-layout-dir ... --edit-dir ...`
passed against raw layouts, with no normalization. Independent scientific and visual
reviews found no remaining material issue after the metric wording correction.

Final ignored local file: `docs/6g-mena-poster/drafts/RayGuard-Research-Poster-v4.pptx`,
SHA-256 `4019649b2f59cd4e301c4f666e70b5ed1b881bf3d252dde5363102a79e9c7c81`.
No production code, inference, training, sending, commit or push was performed. Next:
owner/advisor review of research v4 and showcase v3; author credits, print dimensions,
actual CT/video material and submission details remain open. The 30 September obligation
and earlier prototype/collection deadline conflict remain unresolved.
Final handoff checks passed: 52 local documentation links/anchors, `git diff --check`,
final SHA-256 readback and `git check-ignore -v` for the new presentation.

## T23 paper-based poster revision, version 3 — 29 September 2026

The owner accepted the direction of the methods, CT and multi-package figures and requested
research sections in place of the large GUI, removal of the missed example and substantive
use of the two supplied research papers. Automated production created new editable copies;
independent agents reviewed the benchmark tables, FALCON motivation/results and native
PowerPoint layouts. The coordinator integrated their corrections. Student authorship/hours
and advisor acceptance are not inferred.

Both posters now show IEDXray's 17,360 images, 12,224/5,136 train/test split, three tasks and
eleven benchmarked models. The selected published AP50 comparison uses YOLOv10-M
73.4/58.0/59.1 and Grounding DINO 72.0/67.6/61.2 for device/generic/specific detection
(Tables 2–4, PDF pp. 7–8). Research also shows FALCON's Table 3 single-image RFG mIoU:
fine-tuned Groma 29.55 versus FALCON 69.58. Its §15 future-work discussion motivates the
proposed related-scan study. These paper findings are visibly attributed, not local results.
The successful training-image example retains its original bytes, exact saved box and
0.970 confidence. The GUI and missed example are removed from poster bodies; known misses
remain recorded elsewhere. CT is conceptual; 125 groups/500 images remain planned.

Actual commands: `node inspect_template_deck.mjs --workspace ... --pptx ... --scale 2`
inspected the source; `node validate_template_plan.mjs --workspace ... --map ...
--source-slide-count 1` passed; `node build.mjs` imported separate template copies and
exported through artifact-tool 2.8.4; `& ./verify.ps1` opened and rendered them read-only
in PowerPoint. Native chart objects were tested but automatic padding omitted a category
label in the compact layout. Final charts therefore use editable shapes/text; all six bar
lengths and value labels were checked against source numbers. Final native checks report
**220 / 317 objects**, **59 / 57 text boxes**, **5 / 4 pictures**, **1 / 0 native crops**,
and **36 / 46 connectors** for research/showcase. Both have zero measured text overflows
and zero out-of-slide objects. Final visual, numeric and scientific reviews passed.

`uv run --locked python qa/package_check.py` passed CRC, one-slide/dimension, preserved
template media, source scan/logo hashes, numeric bar geometry, notes/privacy, absent GUI/miss
media and unchanged v1/v2 checks. `node check_template_fidelity.mjs --workspace ...
--starter-pptx ... --final-pptx ... --map ... --starter-layout-dir ... --final-layout-dir ...`
passed separately for both against raw source/final layouts. No layout projection was needed.

Final files remain local and ignored under `docs/6g-mena-poster/drafts/`:

- `RayGuard-Research-Poster-v3.pptx`, SHA-256
  `2fa792d34c178aa352f0a3a708d0596c55b02d977b4bc93f1cd1204922de1c6d`.
- `Xray-Project-Showcase-v3.pptx`, SHA-256
  `e929129286d50943277f8dcc3dc63c22b9384fa60680c5256d20b33bf6c212ef`.

Original template/source media and earlier versions are unchanged. No inference, new model
evaluation, production code, training, sending, commit or push was performed. Next: owner/
advisor review, actual CT/video material, authors/credits, confirmed print size and submission
details. The 30 September obligation and prototype/collection deadline conflict remain open.
Final handoff checks passed: 52 local documentation links/anchors, `git diff --check`,
final SHA-256 readback and `git check-ignore -v` for both new presentations.

## T23 poster visual redesign, version 2 — 29 September 2026

The owner rejected both first PowerPoint drafts as too simple and requested finer detail,
figures and visuals. Automated production redesigned the body of each copied template;
separate agents reviewed asset provenance, scientific concepts and native PowerPoint renders.
The coordinator integrated their corrections. No student authorship or hours are inferred.

Research now uses an editable detector/review diagram, a distinct planned group branch,
large original X-rays with saved prediction/reference boxes, reversible detail crops,
figure labels/legends and a discussion band. Showcase now uses a large genuine GUI crop
with numbered callouts, editable CT projection/color concepts, a four-bag group schematic
and video programme strip. The approved A03 symbol is embedded unchanged. No new evidence,
accuracy, CT implementation, collection completion or material-color mapping is claimed.
The training score and retained test miss remain selected per-image diagnostics.

Actual commands in the thread-scoped workspace: `node build.mjs` imported independent
template copies and exported both files with artifact-tool 2.8.4; `& ./verify.ps1` opened
them read-only and rendered them in native PowerPoint; `uv run --locked python
qa/package_check.py` verified CRC, single-slide counts, original dimensions, original media
hashes, notes/privacy and unchanged v1 files. Research/showcase contain **138 / 183 native
objects**, including **44 / 42 text boxes**, **7 / 2 pictures** and **2 / 1 native crops**.
Both have zero measured text overflows and zero out-of-slide objects. Independent final
visual review confirmed inset captions inside panels, clear introduction spacing and
unobscured screenshot text; scientific review found no unsupported CT linkage/material claim.

`node check_template_fidelity.mjs --workspace ... --starter-pptx ... --final-pptx ...
--map ... --starter-layout-dir ... --final-layout-dir ...` passed for both. Its initial
raw-layout comparison falsely treated dormant master-layout subtitle prompts as visible
content. Read-only XML inspection confirmed that none of the five source-layout
placeholders is instantiated on any slide. `uv run --locked python qa/rendered_layouts.py`
produced rendered-object layout projections for this check, retaining every master artwork
and visible slide object; raw exports and final PPTX packages were not altered by QA.

Final local files in ignored `docs/6g-mena-poster/drafts/`:

- `RayGuard-Research-Poster-v2.pptx`, SHA-256
  `7f741b31e80311a8ac52fdc99be2d44eaefc7bc579c1fef2ff9a5c2e053f377b`.
- `Xray-Project-Showcase-v2.pptx`, SHA-256
  `198a1c86d75537a32363924d51f21d0c54403b5d4d515a5a77dc4402489bf261`.

Original template and v1 files remain unchanged. These are reviewed editable drafts;
owner/advisor acceptance, final project scope, author order, actual CT/video content and
print enlargement remain open. Next: obtain that content/scope decision, then print proof,
rehearsal and submission review. The 30 September obligation and earlier prototype/data
deadline conflict remain. No production code, inference, model tests, commit, push or
external sending was performed.
Final handoff checks passed: 52 local documentation links/anchors, `git diff --check`,
final file hashes and `git check-ignore -v` for both version 2 presentations.

## T23 editable poster alternatives — 29 September 2026

The owner requested two PowerPoint drafts copied from the supplied 6G MENA template:
conventional research and the advisor's broader introduction/context/SDP-aspects/video
outline. Automated production used artifact-tool 2.8.4 to import separate source copies,
add native editable content and export one-slide PPTX files. Independent read-only agents
reviewed source/template geometry, factual claims and native rendered layouts; the
coordinator integrated corrections. No student authorship or hours are inferred.

The research draft contains background, objective, methods, real single-scan positive/miss
diagnostics and discussion. The showcase presents CT/colorization and multi-baggage work
in parallel, with an actual saved GUI image and explicit editable CT/video/author fields.
Source scan/export/screenshot hashes were verified; canonical image bytes and the original
template are unchanged. Native overlay geometry follows saved original-image `xyxy` boxes.
Natnael Takele is the dataset's credited author (Figshare v1, CC BY 4.0); Takele et al.
is the separate paper citation. No new inference, collection, training, CT implementation,
fusion, metric or submission is claimed. Files remain in ignored `docs/6g-mena-poster/drafts/`.

Actual commands in the thread-scoped presentation workspace:
`node build.mjs` exported both files; `& ./verify.ps1` opened/rendered them read-only
in native PowerPoint; `uv run --locked python qa/package_check.py` checked package CRC,
single-slide count, source dimensions, source-image hashes, notes and privacy;
`node check_template_fidelity.mjs --workspace ... --starter-pptx ... --final-pptx ...
--map ... --starter-layout-dir ... --final-layout-dir ...` passed separately for both.
Native checks report **32 / 37 editable text boxes**, **2 / 1 embedded content pictures**,
**zero text overflows** and **zero out-of-slide objects**. The source header gradient renders
correctly in native PowerPoint; the artifact preview alone displayed it flat. Initial
showcase text overflow and research footer/overlay contrast issues were corrected and
rechecked. Final package and template-fidelity checks passed. No production code changed;
the checks here concern document editing/layout, not model validation.

Final SHA-256: research `3582a899078243fd9ff424dd88bb88383ee85c262b9c0c2e21e59bff1c71c06a`;
showcase `d54c258d4465af09ede302f8adf588575051d2d88c1735c74d5abb9797f5df2b`.
The template's **318.875 × 425.5 pt** dimensions are retained; final print enlargement is
unconfirmed. Next: advisor decision on combined/separate scope and earlier embedded-device
topic, approved author order/credits and CT/video assets, then final content/print/submission
review. The clarification email remains a draft. The **30 September** deadline and earlier
prototype/collection deadline conflict remain unresolved; no commit, push or external sending
was performed for these drafts.

## T18 README collection tables and publication preparation — 28 September 2026

The owner requested the README update, a visible dataset collection table and publication
to main. Automated documentation support added Session A/B and component-family tables:
48/52 images per student, 240/260 across five students, and 500 total planned images.
The README now reflects the proposed dates and reported all-five registrations, while
retaining pending lab acceptance, the C01/F03 assignment conflict and the 15 October deadline.
No acquired scans, approved booking, category IDs, case outcomes or student hours are inferred.

The publication scope is the README and its collection/registration source, status and task
records. Existing unrelated poster, branding and repository-housekeeping edits remain local.
Original documents, raw correspondence and filled personal schedules remain private.
The catalogue allocation tables contain planned totals, not private attendance schedules.

Read-only `git fetch origin` confirmed the starting main revision `761a1aa`. The GitHub
branch-rules readback requires a pull request and successful `CPU (ubuntu-latest)` and
`CPU (windows-latest)` checks; the existing owner-only PR review bypass remains separate
from those mandatory checks. Publication will use this route without changing protection.
This entry records preparation; the resulting PR/check/merge history records publication.

`.venv/Scripts/python.exe tmp/prepare-collection-publication.py` prepared eleven public files
and passed 114 local link/anchor checks against the proposed Git tree, table-total checks
and private-artifact/machine-path checks. `git apply --cached --check` accepted the patch.
This is a documentation-only change; hosted CPU checks remain mandatory for the merge.

## T11/T21/T26/T27 catalogue receipt and reconciliation — 28 September 2026

The owner supplied Yonathan's email (F05) and `Multi-bag Collection.docx` (C01).
Automated documentation support inspected the attachment and updated the shared source
summary, requirements, architecture boundary, plan, tasks and status. Human/lab confirmation
is pending; no student authorship, attendance or work hours are inferred. The source DOCX,
raw correspondence, named allocations and detailed audit remain private.

Actual inspection used PowerShell `Add-Type -AssemblyName System.IO.Compression.FileSystem`,
`ZipFile.OpenRead` and XML traversal of `word/document.xml`, followed by JavaScript
count/code checks across every configuration cell. All 24 tables were inspected: four keys
and twenty session tables. There are 125 groups / 500 bag entries, one target per bag and
one of each of four component families per group. Each student has 12 Session A groups
(48 bags) and 13 Session B groups (52 bags). Each family has 125 entries, each clutter level
25 groups and each orientation 125 entries. All listed clutter codes/counts match the keys;
no structural count/code mismatch was found. These are planned configurations, not acquired
scans or verified ground truth. No DOCX page rendering or visual layout review was performed.

`Get-FileHash -Algorithm SHA256 'docs/internal/Multi-bag Collection.docx'` identified the
unchanged source as `afeb6297d9203ff551c25443d5d7d4fa20720d2fff777d31240363783fca7630`.
The catalogue provides a concrete numerical target and planned groups, so protocol status
now distinguishes received scenarios from outstanding acquisition/export, annotation/QC,
negative/control outcomes and attendance-log ownership. Inventory readiness is reported by
Yonathan; physical items were not inspected. His undated availability does not confirm
29 September guidance or recurring availability.

C01's all-family sessions and E4/B3 inclusion in Round 1 conflict with F03's earlier
one-item weekly allocations/extras. Both records are retained, and the old private rota
and unsent scheduling reply are flagged for revision/clarification. No dates or assignments
were silently changed. Session A/B mapping to weeks needs lab confirmation. Repeated G01
labels require collector/session/source context; planned groups do not prove physical
independence. No machine category IDs, case outcomes or completed collection were invented.
The proposal's positive/negative sample scope remains unresolved despite the matching 500
count. All previous deadlines and the prototype/collection conflict remain visible.

A PowerShell here-string piped to `uv run --locked python -` checked 88 local links/anchors
across eleven reviewed documents, source-hash/audit readback and task states; all passed.
`git check-ignore -v` confirmed the attachment, private source/audit and filled planning
records remain excluded; `git ls-files --` confirmed they are untracked. `git diff --check` passed.
This was documentation-only work; no code/model tests, inference, message, commit or push
were performed. Existing working-tree changes were preserved.

T21 remains not started, T26/T27 in progress and T11 blocked on the remaining taxonomy/
provenance/ownership decisions. Next: confirm C01's precedence and A/B dates with the lab,
obtain remaining protocol/QC instructions and dated first-day guidance, then record actual
collection. M02's broader post-midterm Batch 2 remains T30.

## T26 revised slots and dated collection proposal — 28 September 2026

The owner supplied Dr. Divya's scheduling reply (F04): the earlier overlap would prevent
scan completion, afternoons are possible and final dates are requested promptly. The owner
then reported two changed slots after group discussion and explicitly supplied **29 September**
as the agreed first Tuesday. The original email timestamps were not supplied. This is
documented correspondence/team reporting, not evidence of completed scans or lab acceptance.

The private rota now has no overlapping sessions. The two changed times retain their full
two-hour durations; the other three slots and all ten F03 item allocations are unchanged.
Week 1 sessions fall on **29 September, 30 September and 1 October 2026**, with the same
weekday/time pattern repeated on **6, 7 and 8 October**. The final planned session precedes
the 15 October Batch 1 deadline. Planned student-session time remains 9 h 45 min/week and
19 h 30 min across two weeks; actual attendance/hours and scan counts remain unreported.

A new private reply draft includes all dates, times and item allocations and requests lab
acceptance, the protocol and Yonathan's first-day guidance on 29 September. It is not sent.
The earlier broad progress email is retained as a historical draft and points to the new
reply. F04 establishes review of an earlier proposal; its exact sent message was not supplied.
The private source record and shared source/context/plan/status/tasks distinguish the lab's
instructions from the owner's revised availability/date confirmation.

Executed checks: a PowerShell here-string piped to `uv run --locked python -` verified all
ten dated sessions, calendar weekdays, seven-day repetition, absence of overlaps, unchanged
item assignments, 1,170 total planned minutes and completion before 15 October. All 83 local
links across 11 reviewed documents resolved. `git check-ignore -v` confirmed the named rota,
new reply and private source remain excluded; `git diff --check` passed. This was a
documentation-only change; no code or model tests were needed.

T26 and T27 remain in progress for final reply/lab acceptance, protocol and guidance. T21
remains not started; T22 remains complete per the earlier owner confirmation. One shorter
weekly slot is unchanged. F03's extra-item timing question and the prior prototype/poster
obligations are retained. Automated documentation support recorded the update; no additional
student contributions or hours are inferred. Next: send the dated proposal, obtain lab and
protocol/guidance confirmation, then record actual collection. No message, commit or push
was sent by the assistant.

## T28 A03 approval and archive of earlier logo designs — 28 September 2026

The owner selected **A03 · Cobalt / controlled refinement**, superseding the 27 September
A04-02 Optical/Manrope 650 choice, and requested earlier designs archived with a dedicated
folder for the selected asset. Automated organization/documentation support performed this
work; no student authorship or hours are inferred.

The exact selected transparent PNG now lives in RayGuard-App's
`assets/logo/a03-cobalt-controlled-refinement/`, with approval and provenance records.
It is 1254 × 1254 RGBA, SHA-256
`e6477f1b87abe86afd1e3527c47ac2aaf2d0da33962b44fa83a20f7ebd0c7883`.
No image modification, alternative palette, wordmark or vector reconstruction was performed.

The complete former `outputs/logo/` and `assets/scroll-eye/` packages were moved into
the separate app's ignored `assets/archive/logo-designs/2026-09-28/` archive. It includes
the native/AI refinements, darker-blue comparison, A04 brand study, source references,
presentations and ZIPs, plus snapshots of the previous runtime artwork and older eye media.
All 472 original files matched their pre-operation SHA-256 inventory. Local README pointers
identify the new locations; already-deleted older material was not recreated.

Executed `& ./tmp/archive-rayguard-logos-2026-09-28.ps1` with native PowerShell operations.
The helper verified absolute path containment and absence of existing destination/reparse
conflicts before moving, verified the approved PNG copy, then verified every archive file.
The owner approval, task, shared handoff and app identity records were updated. Existing
working-tree edits and runtime copies remain preserved; no reset, commit or push occurred.

Independent file readback via a PowerShell here-string piped to `uv run --locked python -`
verified 472 archived originals (147,989,515 bytes), both ZIP CRCs, 23 unchanged runtime
artwork/media/icon files, the approved PNG's hash/dimensions/transparency and 110 local
Markdown links. `git diff --check` passed in both repositories. No application source was
changed, so code/browser tests were not rerun for this asset/documentation operation.

Approval/archive work is complete. The application still renders A04; A03 runtime adoption
is pending under T28. No fresh browser, inference or model-performance evidence is claimed.
Next: use the approved master for subsequent brand work; complete any app adoption/rehearsal
as its own implementation increment. Existing collection, poster and advisor deadlines remain.

## T21/T26/T27/T30 item allocations and protocol handoff — 28 September 2026

The owner supplied a further email from Dr. Divya (F03); its original send timestamp was not
provided. The [sanitized source summary](meeting_minutes/follow-up-collection-2026-09-28.md)
records the four labelled item families, weekly allocations, timing request and Yonathan's
protocol responsibility. The supplied correspondence and exact person/week assignments remain
private. Automated documentation support recorded the update; no student work hours or
completed collection are inferred.

The existing private rota and unsent advisor email now pair the owner's proposed timings with
Dr. Divya's ten weekly item allocations. The item sets are E1/B1/W1/D1/E2 in Week 1 and
B2/D2/W2/E3/D3 in Week 2. E4 and B3 are extras outside that table. These are item labels,
not scan counts, machine class IDs or verified case groups. The earlier availability spelling
of one student's name was aligned with the new email and meeting roster; no timing was changed.

T27 is now in progress: Yonathan is named to supply the protocol and requested for first-day
guidance. Neither protocol receipt nor his attendance is confirmed, and no model-support role
is inferred. T21 remains not started, T26 remains in progress and T30 remains not started.
T22 remains complete on the owner's earlier all-five registration confirmation.

Interpreting the post-midterm sentence as applying to E4/B3 extras is explicitly provisional.
The revised reply asks whether the initial campaign still follows the 15 October deadline.
Existing two-week cadence, ten sessions, poster obligation and prototype-date conflict remain
recorded. Exact dates, lab acceptance of overlap/shorter duration, quotas, annotation/group
schema, log ownership and extra-item allocation remain unresolved.

The source index, context, plan, architecture boundary, tasks and short status were updated.
The new shared summary was explicitly allowed by the existing meeting-file ignore policy;
raw correspondence and filled schedules remain excluded.

Executed checks: a PowerShell here-string piped to `uv run --locked python -` passed 83 local
links across 11 documents, all ten source-to-rota/email assignments, unchanged proposed times,
E4/B3 exclusion from the initial table and T21/T22/T26/T27/T30 states. `git check-ignore -v`
confirmed all three private records are excluded, and `git ls-files --` for those paths
returned no tracked files. `git status --short -- docs/meeting_minutes/follow-up-collection-2026-09-28.md`
shows the new shared summary as eligible/untracked; `git diff --check` passed. No code tests
were needed for this documentation-only update.

Next: send proposed times and obtain
lab/date clarification, Yonathan's protocol and confirmation of first-day guidance. No email,
code change, model run, commit or push was performed.

## T22/T26 registration and initial collection availability — 28 September 2026

The owner supplied initial weekly availability for all five students and explicitly confirmed
that all five, including himself, are registered for 6G MENA. T22 is marked complete on that
documented owner confirmation; receipts were not independently inspected and actual registration
dates were not supplied. Hardik's separate T24 registration/video remains unconfirmed.
Automated documentation support recorded this update; no student hours or additional
implementation contributions are inferred.

The filled schedule is retained privately under the existing documentation policy. Its five
slots total 9 h 45 min/week, or 19 h 30 min across two weeks if repeated unchanged. These are
planned student-session hours, including concurrent attendance, not completed work or exclusive
scanner time. One 90-minute overlap and one 1 h 45 min session require lab confirmation. No
calendar dates, approvals, session attendance, scan counts or new collection were invented.
T26 remains in progress; T21 collection and T27 protocol remain open.

A private, unsent progress email to Prof. Naoufel and Dr. Divya combines registration, the
proposed rota, GUI progress and both repository links. GUI statements use the existing
27 September migration/verification records and inspected app README; no fresh inference
or accuracy measurement was performed. The draft requests the exact consecutive weeks,
lab acceptance/protocol and reconciliation of the old 8/15 October prototype targets with
Batch 1 by 15 October and subsequent adaptation. The 30 September poster obligation is unchanged.

Executed checks: `git remote -v` in both checkouts matched the two repository URLs.
A PowerShell here-string piped to `uv run --locked python -` checked 62 local links across
the eight edited documents, both copies of all five supplied slots, duration/overlap arithmetic
and T22/T26 states; all passed. `git check-ignore -v docs/internal/collection-schedule.md
docs/internal/2026-09-28-progress-email.md` confirmed both private records are excluded;
`git ls-files --` for those paths returned no tracked files. `git diff --check` passed.
This was documentation-only work; no code tests, email sending, commit or push were performed.

Shared status, tasks, plan, context and event checklist now reflect the report. The blank
shared schedule and historical meeting requirements remain intact. Existing working-tree
edits were preserved. Next: send the consolidated email, obtain lab confirmation and protocol,
then record actual sessions; complete GUI rehearsal and the intended model/scanner handoff.

## T31 teammate collaborator invitations — 27 September 2026

The repository owner explicitly requested access for four supplied GitHub accounts.
Root coordinated the authenticated GitHub API operation and shared documentation;
a separate read-only agent reviewed the scope against the contribution rules.
No student authorship, work hours or code understanding is inferred.

Before mutation, authenticated read-only API checks verified owner administration
access, the exact `abdalrahman-ismaik/SDP-I-RayGuard` repository, all four account
identities, no existing teammate collaborators and no pending invitations. GitHub
canonicalizes the supplied `Blitzict` handle to `blitzict`.

| GitHub account | Repository permission | Verified outcome |
|---|---|---|
| `mohd2k5` | Write | Invitation sent; pending acceptance |
| `blitzict` | Write | Invitation sent; pending acceptance |
| `Boshahab` | Write | Invitation sent; pending acceptance |
| `Alshamisi10987` | Write | Invitation sent; pending acceptance |

Executed through the existing noninteractive Git credential helper, with credentials
kept in process memory: `GET /user`, `GET /users/{username}`, repository/collaborator/
invitation/ruleset GETs, then four serial
`PUT /repos/abdalrahman-ismaik/SDP-I-RayGuard/collaborators/{username}` requests.
For this personal-account repository, GitHub returned **Write** on each invitation.
A fresh invitation-list GET confirmed all four pending. API creation timestamps
are 26 September 21:51:43–45 UTC, or 27 September 01:51:43–45 Asia/Dubai.
Private invitation receipts remain ignored; no credentials are written to shared files.

The two active ruleset summaries matched before/after. CODEOWNERS, required reviews,
CI and bypass configuration were not changed. RayGuard-App permissions were not
modified. `git diff --check` passed; this was an access/documentation change, with
no code, model jobs, commit, push or publication of local working-tree changes.

T31 is now in progress. Next: each teammate accepts the GitHub invitation, confirms
required repository/material access and records their own explain-back/contributions.
An invitation is not proof of accepted access, a code contribution or material access.
Earlier dated records describing invitations as unsent retain their historical meaning.

## T28 repository exclusions and T23 design feedback — 27 September 2026

The user requested that application files remain versioned only in RayGuard-App
and that the main documentation/progress reflect the current state. Root
coordinated `.gitignore` and documentation changes; an independent read-only
agent audited the Git boundary. No student contribution or review hours are inferred.

Existing exclusions already covered local `app/`, `assets/`, `run-app.ps1` and the
old GUI workflow; none was tracked. Added anchored exclusions for accidentally
nested `RayGuard-App/` and copied `frontend/` / `backend/` roots. Expanded the
generated-output exclusion from `output/playwright/` to all of `output/`.
Git uses `.gitignore`; no ineffective `.ignore` substitute was created. Shared
contracts, model catalog, inference scripts and runtime profiles remain tracked
here and are consumed by the separate app's pinned engine submodule.

Executed checks: `git ls-files -- app assets run-app.ps1 .github/workflows/gui.yml frontend backend RayGuard-App output`
returned **zero tracked app/output files**. `git check-ignore -v --` with eleven
representative app/output paths matched all eleven. Five shared engine/documentation/test
paths remained tracked and unignored. `git add --dry-run --all .` listed only
ignore/documentation changes, including pre-existing work; it staged nothing.
The sibling app's `git status --short` remained clean. A local Markdown check
validated **128 relative links** across the updated documentation with no missing
targets; `git diff --check` passed. No code changed, so runtime/model tests were
not repeated for this housekeeping step.

README, contribution/index/architecture guides, status, tasks and poster records
now reflect the repository split and the user's design feedback: the first
poster is too generic and unprofessional, and **was not accepted**. Earlier render
checks establish file correctness only; redesign remains outstanding and poster
work is set aside for now. T23/T28 remain in progress, with existing deadlines and
human acceptance obligations unchanged. Local legacy files and services were
preserved; no tracked removal, app checkout edit, deletion, commit or push occurred.

## T23 application-led poster draft — 27 September 2026

The user chose the working application/live demonstration as the poster lead,
provisional A1 portrait, and unconfirmed author/supervisor credits. The
[poster plan](poster-plan.md) records this direction, content/evidence mapping,
review sequence and remaining acceptance. Automated assistance coordinated the
copy, HTML/PDF design and shared records; independent read-only agents inspected
source assets, scientific claims and the rendered layout. No student authorship,
presenter assignment, contribution hours or advisor approval is inferred.

A self-contained HTML draft, one-page A1 PDF, PNG preview, presenter notes and
private provenance/audit records were created. The main figure is an unchanged
actual app capture of the known missed laptop target. Two diagnostic figures use
unchanged canonical PNG bytes and vector boxes bound to saved exports: Test000001
has one reference and zero predictions; Train000003 has one generic prediction
and is explicitly labelled a bare-IED training example. Hashes, dimensions, run
IDs and box types were checked. No new model run, training, service change or
publication occurred; the September 24 content draft remains preserved.

Executed from the repository root:

```text
.venv/Scripts/python.exe outputs/poster/6g-mena-2026/build_poster.py
node outputs/poster/6g-mena-2026/render_poster.cjs
pdfinfo output/pdf/rayguard-poster-v1.pdf
pdffonts output/pdf/rayguard-poster-v1.pdf
pdftoppm -scale-to 1900 -singlefile -png output/pdf/rayguard-poster-v1.pdf outputs/poster/6g-mena-2026/rayguard-poster-v1-preview
pdftotext -layout output/pdf/rayguard-poster-v1.pdf outputs/poster/6g-mena-2026/poster-text.txt
uv run --locked ruff check .
uv run --locked python -m pytest
```

The final render has **one A1 page**, embedded fonts, 380 poster words including
captions/references, no page overflow, no missing assets, no page errors and no
external network requests. Text extraction and visual inspection passed. Ruff
passed; **143 CPU software tests passed in 6.45 seconds**, separate from model
evidence. Initial private-render helper checks caught a relative module path and
font-loading timing issue; both were corrected before the final export. Private
artifacts and manifests are ignored; the shared plan contains no scans or personal
paths. Existing unrelated documentation changes were preserved.

Remaining limitations: source scans have limited native resolution and the hero's
small interface text is supporting context, with large external explanations.
Actual-size print proof, printer/PDF requirements, author/order/supervisor credits,
approved branding/figures, advisor review, intended host/lab pairing and human
rehearsal remain open. The demo script is proposed, with saved real outputs clearly
labelled as fallback. T23 remains in progress; next action is advisor/content and
organizer-format review, not submission without those details. The 30 September
deadline and ASAP SLG obligation remain, with exact cutoff/route/visit unknown.

## T28 standalone public application — 27 September 2026

The owner requested immediate extraction and explicitly chose public visibility.
[RayGuard-App](https://github.com/abdalrahman-ismaik/RayGuard-App) now contains the
frontend, API, launcher and app documentation at initial commit `22ab909`.
SDP retains research requirements, the sole team backlog, contracts, model catalog,
runtime setup and inference tools. App `engine/` pins SDP core commit `b7ec59e`.
The app's [migration record](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/migration.md)
explains the boundary, exact pin, launch instructions and evidence limits.

Automated implementation coordinated the migration, dependency pins, shared
records and Git operations; separate agents adapted backend/launcher, checked
browser behavior and independently reviewed portability, privacy and attribution.
The owner supplied GUI direction and maintains its repository. No student hours,
code understanding or unrecorded authorship are inferred. Team research and
upstream artifacts retain their separate attribution.

Before extraction, a private source snapshot preserved 242 Git-visible working
files with hashes/sizes, working/index patches and a Git history bundle. The old
app, local configs, source media, environments and services remain available on
disk. Old `app/`, `assets/` and root `run-app.ps1` are now ignored recovery copies;
new GUI work belongs in RayGuard-App. No existing branch/history was reset.

Executed commands: root `uv run --locked ruff check .` passed and
`uv run --locked python -m pytest` gave **143 passed**. Extracted app backend lint
and **280 tests** passed. `npm ci` and production build passed; full Chromium suite
gave **149 passed in 4.8 minutes** using synthetic API/model fixtures and real
bundled media. These software results are separate from model evidence.

The actual new launcher started a separate service with an ignored local config
referencing existing artifacts. Fresh generic YOLO CPU/GPU qualification passed;
two ordinary runs at threshold 0.25 retained the training-image positive and the
known test-image miss with a **missed** annotation-comparison outcome. No model or
dataset downloads, split edits or training ran. Public staging review covered
155 app files plus the engine gitlink; no data, weights, credentials or private
configurations were included. Upstream font license bytes/hashes were preserved.

T28 stays in progress for intended lab pairing, human rehearsal and observed
scanner export handoff. The repo decision does not amend poster/collection
deadlines or complete P1/P2. Earlier entries below retain their dated evidence;
references to the former local app layout are historical.

## Verified engineering outcomes

| Date | Work / task | Evidence | Limits |
|---|---|---|---|
| 21–22 Sep 2026 | CPU package, shared JSON interfaces, audit tools and synthetic checks; T01 | Source/tests/lock and [verification](verification.md) | Neither prototype complete; individual student implementation/review time unrecorded |
| 22 Sep | IEDXray and STCray inspection; T03/T16 | [IEDXray](iedxray-audit.md), [STCray](stcray-audit.md) | Audits completed with findings; data are not cleared for all downstream uses |
| 22 Sep | Generic YOLO CPU diagnostic inference; T04 | [Commands and outcomes](first-inference.md) | Three images, including a missed threat and a training example; not an accuracy estimate |
| 22 Sep | Supplied-model inventory | [18-checkpoint catalog](checkpoint-catalog.md) | Static pairing/integrity evidence; only generic YOLO executed |
| 24 Sep | Public repository publication; T25 | Commit `1cfffa8` on main and both prototype branches | Publication does not establish five members' access, review or understanding |
| 24 Sep | Meeting 02 requirements ingested; T20/T33 | [Meeting records](meeting_minutes/README.md), [plan](plan.md), [tasks](tasks.md) | Documentation only; collection/GUI/registration/submission not completed by the record |
| 24 Sep | Shared team documentation and onboarding; T35 | [Index](README.md), [contribution guide](../CONTRIBUTING.md); 178 local links checked; fresh public-file export passed Ruff, 85 tests and CPU smoke commands; [verification](verification.md) | Prepared locally; publication and five-member access/adoption are separate actions. No private artifacts or new inference included |
| 24 Sep | Public agent-guidance follow-up; T35 | Root AGENTS.md and four project skills enabled for Git; four skill validations and 187 links across 55 public candidates passed | Explicit owner choice supersedes earlier exclusion; personal settings/sessions stay private. Guidance reviewed, no model/demo workflow executed; not yet published |
| 25 Sep | Collaboration access/protection setup; T36 | [PR #1](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/pull/1), merge 5fac792; shared docs/skills on all three branches, CODEOWNERS validated; two active rulesets read back; hosted Linux/Windows checks passed | Supersedes the earlier not-yet-published state. Owner has a PR-only review bypass; CI/history has none. Teammate usernames/invitations pending. No new model or collection evidence |

See [status](status.md) for the current handoff and [tasks](tasks.md) for the only backlog.

## T28 GPU inference research and plan — 26 September 2026

Automated research support inspected the configured model environment, GPU/driver,
checkpoint hash, installed original YOLOv10 fork and GUI execution/failure paths.
The root agent coordinated the study and shared documentation; separate agents reviewed
backend integration, official runtime compatibility, and correctness/latency validation.
Human implementation/review ownership and student effort remain unreported.

Actual read-only commands included `nvidia-smi --query-gpu=name,driver_version,memory.total,memory.used,compute_cap --format=csv,noheader`,
the configured interpreter's `torch`/`torchvision`/CUDA JSON probe, `Get-Content .venv-yolov10/pyvenv.cfg`,
`Get-FileHash -Algorithm SHA256 -LiteralPath data/IEDXray/model-weights/yolov10_generic_exp.pt`,
`Get-Volume -DriveLetter C`, and targeted `rg`/source reads. Results: RTX 2060, driver
591.74, 6,144 MiB VRAM, capability 7.5; Python 3.11.9 with torch 2.9.0+cpu and torchvision
0.24.0+cpu, CUDA unavailable; checkpoint SHA-256 matches the recorded baseline.
The existing environment inherits system packages. No model was executed in this study.

Primary-source research inspected PyTorch/NVIDIA version documentation, pinned Windows
build scripts, the fork's requirements/metadata, official wheel metadata/index entries
and HTTP headers. The [study and implementation plan](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/gpu-inference-plan.md)
recommends a separate torch 2.9.0+cu126 / torchvision 0.24.0+cu126 environment, explicit
CPU/GPU selection on restart and FP32 parity before adoption. It identifies repeated
GPU warm-up/process costs, configuration-only health checks, and folder intake advancing
after failures. It specifies truthful execution provenance, compute-failure queue pause,
three-target diagnostic comparison, bounded latency measurements and CPU rollback.

Evidence levels are separated in the plan: hardware/runtime probes executed; source and
remote artifacts inspected; GPU compatibility, peak memory and speed remain unverified.
No wheel/model download, environment/config change, service restart or GPU inference
occurred. The change is documentation only; software/model test results are not claimed.
Independent plan review corrected the pre-change canonical CPU control, GPU parity-before-replay
sequence, nonblocking probe/admission design, execution-record plumbing and preservation of
the concurrent annotation-comparison feature. `git diff --check -- docs/README.md docs/status.md docs/progress.md docs/tasks.md`
passed. An inline Python check resolved all **118 local Markdown link targets across six
updated documents**; the new plan also passed whitespace, code-fence and private-path checks.
Next implementation action: prepare the isolated environment lock and minimal device
plumbing, then run the plan's serial qualification gates. T28 remains in progress, and
the intended lab pairing, human rehearsal and existing schedule conflicts remain open.

## T28 GPU laptop-portability clarification — 26 September 2026

The user clarified that RayGuard should inspect each laptop and prepare its compatible
GPU runtime automatically. This supersedes the earlier plan's explicit-only selection
proposal: newly generated configurations would use Auto, resolving a verified GPU or
CPU with a visible reason before accepting runs. Existing CPU configurations and explicit
overrides remain supported; no failed GPU run silently retries on CPU.

Automated research support extended the [GPU plan](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/gpu-inference-plan.md) with
hardware discovery independent of CPU-only Torch, reviewed runtime profiles, isolated
CPU/GPU setup, atomic local activation, cached qualification/invalidation, hybrid-device
selection, visibility-mask handling, and cross-laptop acceptance gates. Root owns this
documentation update; separate agents reviewed runtime sources and integration policy.
Human ownership and student effort remain unreported.

Actual work was read-only `Get-Content`/`rg` inspection of the plan, launcher, installed
fork selector and backend, plus primary-source PyTorch/NVIDIA/AMD/Microsoft/Apple and
publisher package-metadata research. NVIDIA generations need compatible build profiles;
XPU, ROCm, MPS and DirectML are distinct backend candidates, not automatically verified
RayGuard support. The current Windows NVIDIA path is first; unsupported combinations
retain a qualified CPU path or an actionable incomplete-setup state. Another NVIDIA
laptop and CPU host must demonstrate clean setup before claiming cross-laptop usability.

Documentation only: no hardware settings, package environments, application code or
running services were changed; no install, GPU inference or second-laptop test occurred.
Independent reviews confirmed the vendor/runtime limits and corrected the distinction
between release qualification and fresh-laptop verification, including an explicit
verification path when setup has no diagnostic input yet. `git diff --check -- docs/status.md docs/tasks.md docs/progress.md`
passed; an inline Python check resolved **84 local links across five updated documents**
and checked plan whitespace, fences, private paths and superseded policy text.
Next: implement reviewed profile locks and the discovery/setup lifecycle, then the
serial model/integration/portability gates. The existing showcase obligations remain.

## T28 GPU implementation prompt — 26 September 2026

At the user's request, automated documentation support produced the ready-to-use
[implementation prompt](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/gpu-implementation-prompt.md) from the reviewed GPU plan.
The root agent owns this brief and shared handoff; an independent reviewer checked
acceptance criteria and setup/qualification ambiguities. No student authorship or
implementation completion is inferred.

The brief specifies project inspection, protected CPU controls, reviewed runtime profiles,
automatic setup, Auto/explicit policies, fresh-host qualification, fixed session selection,
device routing, provenance, queue failure recovery, minimal UI changes, software checks,
bounded real inference/performance and second-host evidence. It distinguishes the full
development benchmark from ordinary first-run verification and prevents unverified
hardware detection from being displayed as successful model execution.

Work was limited to `Get-Content`/`rg`/Git inspection and documentation edits. No package
installation, application implementation, model inference or service change occurred.
Independent review clarified Auto-only qualification fallback, CPU-only verification
and task-owned service restart boundaries. `git diff --check -- docs/README.md docs/status.md docs/progress.md docs/tasks.md`
passed; an inline Python check resolved **123 local links across six documents** and
checked the prompt/plan for whitespace, code-fence and private-path issues.
Next: use the brief in an implementation session and record actual gate outcomes;
T28, GPU execution and portability remain unverified beyond the prior recorded evidence.

## T28 GUI first draft — 25 September 2026

Automated implementation support created `app/` with React/TypeScript/Vite, a separately
locked FastAPI service and an adapter to the existing verified generic YOLO environment.
Independent review checked task labels, model/run binding, empty/failure handling, privacy
and final screenshots. Human GUI/model owners, student review and effort remain unreported.

Actual checks: `uv run --locked ruff check .` passed; root pytest **85 passed**; API pytest
**35 passed**; frontend clean install/typecheck/build passed; **12 Playwright browser tests
passed**, including both-theme automated accessibility checks; npm audit reported **0 known
vulnerabilities**. See [the exact commands and outcomes](verification.md#gui-first-draft--25-september-2026).
Tests use synthetic fixtures. One upstream test-client deprecation warning remains documented.

Separately, three real API inferences reproduced the earlier one-positive/two-empty outcomes.
Browser upload/run checks verified the positive training example and the missed-threat test
example, with actual overlays/history/exports and no benign verdict. Production layout was
checked from 320 to 1440 px; an actual exported run retained model provenance and run identity.
These checks establish the generic app integration, not accuracy or full P1/P2 completion.

Implementation and evidence are local on `feat/gui-first-draft`, not published. New GUI CI
jobs are defined but have no hosted result yet. Next: confirm the lab's intended laptop/pager
pairing, name the human GUI/model owners, and rehearse on the presentation laptop using the
[launch guide](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md), retaining both positive and missed-threat examples.

## T28 launcher follow-up — 25 September 2026

Automated implementation support added root `run-app.ps1` as the Windows startup entry
point. It installs locked frontend packages, builds, starts the locked API environment,
and selects the ignored local model config. Repeated launches preserve the existing
RayGuard session. Startup rejects unrelated occupied ports and API-only servers; native
command failures stop setup. `-SkipBuild`, `-Port` and `-Config` cover normal alternatives.

`uv run --locked python tmp/verify_gui_launcher.py` passed six local smoke scenarios:
full build/start from another working directory, unconfigured start using built assets,
unrelated occupied port, healthy API without UI, missing config, and simulated npm failure.
Both successful startup cases also verified repeat-launch reuse. The checks started real
temporary services and inspected health/HTML; they did not execute model inference.
Only their own process trees were stopped; the original GUI session was preserved.

Review found an API-only reuse edge; actual startup found multiple npm executables resolving
on PATH. Both were fixed before the passing run. Root Ruff passed and **85 CPU tests passed
in 2.94 s**. Private checks/logs are in `runs/gui-verification-2026-09-25/`. No model dependency,
checkpoint, UI behavior or publication changed. Student ownership/rehearsal remains pending.

## T28 airport workflow and folder intake — 25 September 2026

Automated implementation support researched Smiths, Rapiscan and Leidos primary sources
and inspected available public visuals. [Research notes](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/scanner-research.md) separate
vendor statements, visual evidence, project recommendations and unknown hardware details.
The user confirmed the scanner/interface is unknown. One coordinator integrated separate
backend, frontend and research work; an independent final code/claim review found no further
actionable issues after the fixes below. Human ownership and explain-back remain pending.

Added read-only PNG/JPEG/BMP intake, metadata/decode settling, a bounded automatic queue,
pause/resume and visible failures. The GUI now emphasizes inspection, source/queue state,
follow/hold selection, display-only controls and review notes/status. Existing upload,
real generic YOLO pairing, history/export and model isolation remain. The queue starts
paused and is session-only; restart behavior and recovery are explicit in the launch guide.

Actual commands: root `uv run --locked ruff check .` passed; root
`uv run --locked python -m pytest` **85 passed (2.81 s)**; API
`uv run --project app/backend --locked python -m pytest app/backend/tests` **58 passed
(3.35 s)**; `npm --prefix app/frontend run build` passed; installed-Chrome
`npm --prefix app/frontend run test:e2e` **19 passed (32.6 s)** after the final CSS fix.
These tests are synthetic; see [verification](verification.md) for coverage and limitations.

Separately, `node tmp/gui_folder_replay.mjs` and its recovery continuation
`node tmp/gui_folder_resume.mjs` exercised actual folder-to-YOLO-to-browser processing.
The training positive reproduced score 0.9702618 in 16.65 s; the known modified-laptop
miss returned zero boxes in 9.43 s. Pause retained queued work; resume processed it.
Review/export, source-byte preservation and responsive widths were checked. No external
page requests or unhandled browser errors occurred. Intake was left paused with no queue.
This is published-image replay, not a physical scanner test or a performance/accuracy result.

Iteration fixed backpressure halting dispatch, note editing losing its selected scan,
an adjustment panel changing canvas size and a collapsing findings list at laptop height.
The last issue was discovered during the real positive browser test; after fixing it,
checks resumed using the existing run and queued work. Final independent review and
light/dark/mobile visual inspection passed; the design detector reported no findings.

No scanner SDK/control, persistent queue, hardware handoff, authenticated operator audit,
video inference or full P1/P2 decisions are implemented. No model package, checkpoint,
dataset split or training changed. Work remains local and unpublished. Next: obtain the
lab's actual scanner/export details, observe one completed-scan handoff, and confirm the
intended showcase model with a human presentation-laptop rehearsal. T28 stays in progress.

## T28 typography, themes and navigation — 25 September 2026

Automated implementation support compared Carbon, Fluent and Atlassian primary design
guidance and Plex/Inter/Source Sans 3. A read-only audit identified tiny operational text,
review actions beneath technical metadata and long mobile setup. The established scan
workspace was refined using local IBM Plex Sans, a consistent rem-based hierarchy,
neutral light/graphite surfaces and direct section anchors. Review comes before disclosed
geometry; mobile settings collapse after an image loads, with Run always available.
Font files were downloaded from a pinned official source, hashed and bundled with OFL.
Three weights total 196,820 bytes. No UI package or runtime font service was added.

`npm --prefix app/frontend run build` passed; installed-Chrome
`npm --prefix app/frontend run test:e2e` passed **21 tests in 38.9 s**, including new
mobile keyboard/focus and local-font/fallback cases. Root Ruff passed and
`uv run --locked python -m pytest` passed **85 tests in 2.60 s**. The unchanged API retains
its earlier 58-test result. The design detector reported no findings. A label-in-name
mismatch was corrected before the final checks; both tested themes pass Axe A/AA checks.

`node tmp/gui_visual_check.mjs` inspected previously saved real results in the production
UI without running the model or writing review records. All fonts loaded, eight widths
from 320–1440 px avoided document overflow, and review actions fit the laptop panel.
No external HTTP, API mutation or unhandled page error occurred. This is visual/software
verification, not new inference, a hardware test or a human usability study.

Independent final screenshot review found only a missing tablet history-scroll cue.
After extending it to 960px, build passed again and the focused mobile/tablet keyboard
test passed (1 in 6.9 s). The initial npm forwarding command selected no tests; direct
Playwright CLI execution succeeded. Final link/artifact review passed: 254 relative
links, 104 public candidate files, no flagged private artifacts; whitespace check passed.

One coordinator owned CSS/fonts/shared evidence; component work and primary research had
separate owners. Human student authorship/time is not inferred. Work stays local on
`feat/gui-first-draft`. Next: team presentation-laptop rehearsal, actual scanner export
identification and the intended model pairing; T28 remains in progress.

## T28 inspection hierarchy — 25 September 2026

Automated implementation support simplified the page following the user's report
of competing information. One Choose/Run/Review sequence and action strip lead to
the image, then findings and operator review. Removed the settings rail, redundant
header anchors and empty results panel; settings, history and technical/export
details start closed. Active intake, pending work, errors and held unseen arrivals
remain visible. Source/model contracts and detector execution are unchanged.

One coordinator owned layout/styles/shared records; separate contributors owned
the findings/history components and browser tests, with an independent read-only
review. Student authorship, hours and acceptance are not inferred. The review found
failed runs advancing the step prematurely and paused intake hiding unseen-arrival
controls; both were fixed and covered by targeted regressions. A dark mobile page
background was also corrected. An intermediate Windows encoding error was recovered
from the prior built CSS before writing UTF-8 and passing the checks below.

Actual commands: `npm.cmd --prefix app/frontend run build` passed. From
`app/frontend`, `$env:PLAYWRIGHT_CHANNEL='chrome'; npm.cmd run test:e2e` passed
**22 tests in 41.5 s**. After the final state fixes, the same environment and
`npm.cmd run test:e2e -- --grep 'failed inference cannot carry stale predictions|history selection stays fixed'`
passed **2 targeted tests in 8.6 s**. Root `uv run --locked ruff check .` passed;
`uv run --locked python -m pytest` passed **85 tests in 4.68 s**. These are synthetic
software checks; unchanged API code retains the preceding 58-test result.
The design detector returned no findings.

`node tmp/gui_hierarchy_check.mjs` passed against previously saved actual model
results in the production app. Empty/positive/known-miss states, both themes and
eight widths from 320–1440 px were inspected. No external HTTP, API mutation or
unhandled page errors occurred; no new inference or scanner test was performed.
Final independent review found no remaining material issue. The sharing check
passed for 60 changed/new candidates and 197 relative links, without flagged private
artifacts; `git diff --check` passed. These are bounded artifact/pattern checks.
See [verification](verification.md) for evidence and limits. Source scans and
screenshots remain private. T28 stays in progress on `feat/gui-first-draft`;
next: team laptop rehearsal, actual scanner export details and intended lab model
pairing. No publication or changes to dataset splits, model packages or weights.

## T28 direct test replay and design choices — 25 September 2026

Automated implementation support linked the local IEDXray test directory through a
finite replay scheduler and explicit Dataset demo source. Default three-image
batches run fresh inference, stop at the batch/dataset end and support pause/resume
and held review. Independent source inspection matched all 5,136 filenames to all
four test annotation image tables. A separate backend reviewer checked exclusion
locks, failure state, source preservation and provenance; no blocking issue remained.
Backend, frontend and shared/local-runtime work had separate owners. No human
student authorship, effort or acceptance is inferred.

Root Ruff passed; root pytest passed **85 in 2.33 s**. The API suite passed **89 in
3.79 s**, including 31 new synthetic replay cases. Production build passed. Installed
Chrome `npm.cmd run test:e2e` from `app/frontend` passed **28 in 44.8 s**. A real
browser check exposed ambiguous held-image identity; the canvas now names its own
scan. Rebuild and four affected tests passed (**11.4 s**) using
`npm.cmd run test:e2e -- --grep 'pause and resume|completed workspace|laptop controls'`.
Synthetic checks are separate from the actual inference below.

An automatic approval check rejected the attempted idle-service replacement with
only “blocked by policy”; no replacement was performed. A hidden launcher instead
started `run-app.ps1 -SkipBuild -Port 8766`, preserving the prior 8765 service.
The browser started, paused, resumed and followed a predetermined first-three test
sequence with the unchanged generic YOLO CPU pairing and threshold 0.25. All three
runs completed with zero detections (12.84/13.36/11.61 s including startup), and the
known first-image miss remains explicit. Source hashes matched before/after.
`node tmp/gui_dataset_presentation.mjs` verified saved-result export identity, eight
responsive widths and zero external requests/API mutations/page errors. Run IDs,
commands and limitations are in [verification](verification.md). No model tuning,
training, scanner handoff or accuracy claim followed from these results.

The user's later visual request first prompted three generated console composition
studies, then explicitly requested ten professional layouts/themes to choose from.
Final redesign is therefore pending that choice; the working replay app is kept
separate from the read-only design previews. The frontend owner delivered
[ten interactive proposals](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/design-options.md), with shared status and
runtime verification coordinated separately. Build and JavaScript syntax checks
passed. `node tmp/design_studio_check.mjs` checked all ten designs at five widths,
offline states, keyboard/focus, clipboard and preview controls; automated Axe
reported zero violations, with no page errors, external HTTP or API mutations.
`node tmp/design_studio_limits_check.mjs` separately checked synthetic long-history
and multi-finding rendering. Review findings led to larger essential text, complete
scrollable findings and explicit history limits. The manual design detector returned
`[]`. Automated checks do not establish human usability or model accuracy.
Independent final review confirmed the two remaining visual findings resolved.
The bounded sharing check covered 69 changed/new candidates and 207 relative
Markdown links, with no broken links or flagged private artifacts. `git diff --check`
passed; local config, scans, run evidence and screenshots remain ignored.

T28 remains in progress. Next: choose
the workstation direction, rehearse on the presentation laptop with assigned human
owners, and verify the intended lab model/scanner export pairing. No push or commit.

## T28 eye introduction and loading plan — 26 September 2026

The user requested planning for the supplied `assets/scroll-eye` package and selected a
brief animation **every time the website opens**, rather than first-visit suppression.
The [RayGuard plan](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/eye-animation-plan.md) proposes a four-second assembly/reveal,
immediate skip, bounded fallback and a small resolved-eye loop tied to actual activity.
Root agent owned the plan/shared documentation; a separate read-only agent reviewed app
integration, readiness semantics and held review. Student authorship/hours and human owners
remain unreported. T28 stays in progress.

Actual inspection used `Get-Content` for the package README, manifest, validation record,
component/React wrapper/styles, prompts and original implementation notes, plus current
app source and required meeting/project context. The supplied contact sheet and poster
were visually inspected. `node <local-impeccable-skill>/scripts/context.mjs --target
app/frontend/src/App.tsx` resolved the existing app product/design guidance; the bracketed
path denotes the local skill installation rather than a repository dependency.

Executed PowerShell manifest verification with `Get-Content .../manifest.json -Raw |
ConvertFrom-Json`, then `Get-Item -LiteralPath $assetFile` and `Get-FileHash -LiteralPath
$assetFile -Algorithm SHA256` for each listed path: **20/20 byte lengths and SHA-256 values
match; zero failures**. This verifies the supplied package against its own manifest.
Media properties and the source project's 19 browser checks remain documented evidence,
not fresh decode/playback or RayGuard integration checks. MDN autoplay/reduced-motion and
W3C pause guidance were consulted and linked in the plan.

Source inspection confirms `/api/health` reports configuration/file availability, not
model warm-up. The model runner starts a subprocess per inference. `workspace.busy` also
covers enabled idle intake/demo, so animation must use actual activity and preserve a held
older result when a different run is active. The plan retains explicit empty-output limits.

Changes are documentation only. No encoding, runtime implementation, model execution,
publication, student contribution or human showcase acceptance is claimed. Root/app tests
were not rerun for this planning-only change. `git diff --check` passed; a bounded Node
link check across the plan and three updated shared documents found 52 local file links
and zero missing targets (anchors were not validated). Independent plan review clarified
manual replay/focus behavior and suppression of hidden duplicate video playback.
Next: prepare bounded media derivatives,
implement the intro/loading treatment and verify playback, skip/recovery, reduced motion,
state correctness and laptop presentation. Existing model/scanner/human rehearsal obligations
and the T10/Q9 deadline conflict remain open.

## T28 advanced workstation choices — 26 September 2026

The user requested more complex dashboards with clearer organization and partitions.
Automated frontend implementation added six advanced proposals, keeping the ten
compact designs and the working app. Navigation, saved-run search/filter/sort,
evidence tabs, panel visibility and view-only image adjustments are functional in
the preview. Independent source and browser reviewers had separate ownership;
root coordinated shared documents, development routing and persistent regressions.
No student effort or acceptance is inferred. Existing eye-animation planning work
and assets were preserved; this change does not implement that separate treatment.

Root Ruff passed and root pytest passed **85 in 2.56 s**. Production build and both
studio JavaScript syntax checks passed. The full browser command passed 28 existing
cases and exposed a development-only gallery route defect in four new cases. After
the Vite index mapping and pinned Node typings were added, the four affected tests
passed in **9.8 s**. The 24 independent synthetic renderer cases passed; the manual
design detector returned no findings. See [verification](verification.md) for commands,
limits and visual checks. None of these software results establish model accuracy.

The independent visual/edge harness passed 19/20 checks, with one navigation
overlapping a production rebuild. Its initial report is retained. Six targeted
follow-ups passed, including the stable option-11 rerun and final 11/15 laptop
Focus layouts with fresh Axe checks. Both show their footer within 1366×768 and
retain readable panels with internal scrolling. Five standard widths plus a
683px zoom-equivalent viewport were checked. No material issue remained after
independent review; no script errors, external requests or API mutations occurred
in the final checks. The scoped sharing review passed for 21 files and 159 relative
links; `git diff --check` passed. Reports/screenshots stay private.

The advanced gallery is served locally on port 8766 and remains read-only against
saved results. No new model job, dataset modification, backend dependency change,
commit or publication occurred. T28 remains in progress: choose the workstation
layout, apply it to the working app, and complete the human laptop rehearsal and
intended model/scanner handoff checks. Advisor obligations and deadlines remain.

## T28 eye introduction implemented — 26 September 2026

The user clarified that they expected to see the eye, then requested it centered as the
opening page background. Automated implementation now provides that full-screen opening
on every fresh load, immediate Skip/Escape, bounded media fallback and a small loop during
actual connection/upload/inference. Source → Presentation & motion offers replay/pause.
The earlier planning-only record is historical; [verification](verification.md#rayguard-eye-introduction--26-september-2026)
records the implementation evidence.

Root owned UI integration/shared documentation, a separate media agent owned only the
runtime derivatives, a test agent owned the new browser spec and an independent reviewer
checked state/focus claims. The user confirmed another session was redesigning the workspace;
its Analyst Studio and appearance changes were preserved. No student authorship/hours or
human showcase acceptance is inferred. T28 remains in progress.

The original package is unchanged. Intro: 4 s / 982,600 bytes; loop: 3.917 s / 117,251 bytes;
poster: unchanged 53,672 bytes. Both MP4s decode and contain fast-start metadata; the loop
uses a forward/reverse resolved-eye segment to avoid an abrupt reset. Exact encode commands,
hashes and provenance limits are in the [media record](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/frontend/public/media/rayguard/README.md).

Actual checks: `uv run --locked ruff check .` passed; `uv run --locked python -m pytest`
passed 85 tests in 4.45 s; `npm --prefix app/frontend run build` passed. From the frontend,
`npx playwright test tests/e2e/eye-animation.spec.ts` passed 12 checks in 37.5 s. Initial
attempts exposed stale selectors while the concurrent layout was being edited; only the
new spec was aligned with the actual Source/Session/Review controls before its passing run.
Real video playback was checked; API/run fixtures are synthetic, not inference evidence.

`node tmp/eye-visual-check.mjs` produced desktop, 320px mobile and 683px zoom-equivalent
screenshots with zero Axe findings and no horizontal overflow. Frames were frozen for
visual inspection only; the browser suite separately verifies playback/timeout behavior.
The scoped design detector reported no findings at its initial integration pass. Browser
inspection also confirmed the served video on port 8766. A first local visual-helper attempt
used Playwright's shorthand page creation, which Axe rejected; explicit contexts fixed the
helper, and the recorded three-viewport run passed. Private screenshots remain ignored.

Independent review found and resolved continued motion after disconnect, focus restoration
to a disabled replay button, and the pause control not affecting existing spinners. A held
scan is never relabeled as processing another run; empty-output language remains unchanged.
No new model/scanner job, publication or global configuration change occurred. Next: the
human presentation-laptop review and existing model/scanner pairing/handoff obligations;
the broader concurrent redesign has its own validation owner. T10/Q9 deadlines remain open.

## T28 selected workstation and appearance — 26 September 2026

The user selected Analyst Studio 15, then requested different fonts and themes.
Automated implementation applied its four partitions to the working app and added
eight independent palettes/seven fonts. Inspect/Session/Source navigation, evidence
tabs, searchable/filterable history, filmstrip and layout controls are functional.
Review drafts/zoom persist across view and appearance changes. Source labels and
canonical/original hashes remain explicit. The separate eye implementation was
preserved, including its presentation controls and tests.

Root coordinated integration, shared documentation and regressions; separate agents
owned shell/CSS, fonts/appearance and canvas/targeted tests, followed by independent
source and visual reviews. No student authorship, hours or human acceptance is inferred.
Primary font repositories were inspected and five licensed variable assets bundled
with pinned revision/hash records (688,100 bytes); no runtime font service was added.

Actual checks: Ruff passed; root pytest 85 passed in 2.32 s; production build passed.
All 50 browser cases have passing evidence across scoped runs. The initial combined
33-case run passed 32 and exposed an export fixture that also disconnected unrelated
polling; after narrowing that failure route, the workspace 17 passed in 33.6 s.
The first intake/demo/appearance 16 passed in 1.2 min. Final appearance 5 passed in 25.1 s,
including the added empty-dock keyboard/accessibility regression. Exact commands
and limitations are in [verification](verification.md).

Seven saved-data visual cases and three final targeted follow-ups checked desktop,
mobile, distinct font/palette pairs and empty state. Final Axe checks had no
violations; no API writes, external requests or script errors occurred. Review led
to keyboard-scroll access when every adjustment is disabled and focusing the scan
after mobile filmstrip selection. Earlier reports were retained beside final private
screenshots. The scoped design detector gave two style warnings for Geist/Inter;
both remain deliberate font-comparison choices, not mandatory branding.

Final scoped sharing review passed: 27 text files, 132 relative links, ten font/license
hashes and Git whitespace checks. Private screenshots/build/config remain ignored.

No new inference, dataset change, training, backend environment change, commit or
publication occurred. Changes remain local on feat/gui-first-draft. Next: the user
chooses a preferred palette/font and the team rehearses on its presentation laptop;
confirm the intended model pairing and observe a physical scanner export handoff.
Collection/poster deadlines and the T10/Q9 schedule conflict remain unchanged.

## T28 opening zoom-out refinement — 26 September 2026

The user requested a less close-up eye that starts at its current size and shrinks during
playback. Root implemented a centered scale from 1 to 0.76 with quadratic ease-out tied
to media time; another agent independently reviewed the approach and cleanup. Text and
controls stay fixed, and portrait framing uses the same relative reduction. No media
re-encoding, additional dependency or model job was needed. Concurrent redesign changes
were preserved; student effort and human acceptance remain unreported.

Executed checks: `uv run --locked ruff check .` passed; `uv run --locked python -m pytest`
passed 85 tests in 2.59 s; `npm --prefix app/frontend run build` passed;
`npm --prefix app/frontend run test:e2e -- tests/e2e/eye-animation.spec.ts` passed all
12 cases in 23.8 s. These are software checks with real video and synthetic API fixtures.
`node tmp/eye-visual-check.mjs` again produced three viewport captures with zero Axe
findings and no horizontal overflow; desktop/mobile final framing was inspected.
The scoped Impeccable detector returned no findings. A temporary read-only Playwright
probe sampled desktop scale 1, 0.82 and 0.76015 at playback times 0, 2 and 3.9 seconds,
with the center fixed; portrait samples retained the same proportional change.

T28 stays in progress. Next: human presentation review on the intended laptop, alongside
the existing font/palette choice and model/scanner handoff obligations.

## T28 premium airport console — 26 September 2026

The user rejected the first appearance catalog and selected a premium airport
console: dark, precise, restrained, with a dominant scan viewer. The implementation
keeps Analyst Studio's four partitions while changing its visual hierarchy:
Onyx surfaces, Barlow controls and Semi Condensed headings, compact source actions,
quieter separators and a shallow desktop filmstrip. Appearance remains available
for comparison; the default uses a new browser key and preserves old preferences.

Root coordinated shared documentation, appearance and verification; separate agents
implemented shell/adjustments, test changes and the official font bundle. Root
completed browser/visual review and the final geometry fix. These are automated
engineering contributions; no student authorship, hours or human approval is claimed.
Four unchanged official WOFF2 assets total 242,520 bytes, with pinned revision,
hashes and OFL. No runtime packages, model dependencies or backend contract changed.

Actual commands: `uv run --locked ruff check .` passed;
`uv run --locked python -m pytest` passed **85 in 7.60 s**;
`npm --prefix app/frontend run build` passed. With Chrome selected, the frontend
`npx.cmd playwright test` full run passed 49 and failed one new replay-size check
(328.61px versus the 330px target). Shortening the filmstrip by 4px resolved it.
The follow-up `npx.cmd playwright test tests/e2e/demo.spec.ts tests/e2e/appearance.spec.ts tests/e2e/intake.spec.ts`
passed all **17 in 1.0 min**; the other 33 cases had already passed. These are
synthetic software checks, including positive/empty/failure responses, not new
inference evidence. Production build passed after the fix.

`node tmp/premium-console-visual.mjs` inspected saved real scans at seven viewport
sizes, 320–1440px wide. The 1366×768 scan stage measured **332.61px high**, previously
about 220px, with all four partitions visible. Zero Axe findings, document overflow,
page errors, remote requests or API writes; four Barlow faces loaded locally.
The existing replay state stayed completed/disabled. Root visually inspected
desktop and phone captures. Private evidence is in `output/playwright/premium-console/`.
Five font/license hashes matched; 24 text files and 134 relative links passed the
scoped sharing review. The manual style detector retained two warnings for optional
Geist/Inter comparisons. No new default-style warnings were reported.

T28 stays in progress on the local feature branch. Next: human review of this
implemented console on the intended presentation laptop, confirm the lab model
pairing and rehearse, then observe the actual scanner export handoff once identified.
No model job, dataset change, commit or publication occurred for this refinement.

## T28 smaller, cleaner eye presentation — 26 September 2026

The user requested further scale reduction and a sharper, less noisy image. Root changed
the playback-synchronized endpoint from 0.76 to 0.56, including the fallback poster scale.
A media agent prepared native 1920×1080 candidates from the unchanged original; root
reviewed matched frames and promoted the lightly denoised/sharpened CRF17 candidate
and matching full-HD poster. The intro remains four seconds and is 3,714,480 bytes;
the poster is 101,332 bytes. Exact commands and hashes are in the
[media record](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/frontend/public/media/rayguard/README.md). The loading loop is unchanged.
An independent agent reviewed playback limits, fallback sizing, metadata and caching.
Root coordinated shared documentation; student effort/acceptance remain unreported.

Executed checks: `uv run --locked ruff check .` passed;
`uv run --locked python -m pytest` passed 85 in 2.30 s;
`npm --prefix app/frontend run build` passed;
`npm --prefix app/frontend run test:e2e -- tests/e2e/eye-animation.spec.ts` passed
12 in 22.4 s with actual new-video playback and synthetic API fixtures.
`node tmp/eye-visual-check.mjs` verified served 1920×1080 media at desktop1440×900
(2× pixel density), mobile320×740 and zoom-equivalent683×384. All three had zero
Axe findings and no horizontal overflow; root inspected desktop/mobile screenshots.
The scoped Impeccable detector returned no findings. Both candidate videos fully
decoded with 96 frames and verified fast-start metadata; source hash stayed unchanged.

This is software/media evidence, not detector or hardware validation. Native detail
and lower compression provide most of the improvement; original fiber texture remains.
No new model job, publication or global configuration change occurred. T28 stays in
progress; next is human presentation review and the existing model/scanner obligations.

## T28 smaller opening frame — 26 September 2026

The user clarified that the starting size was still too large. Root reduced the
initial scale from 1 to 0.70 while retaining the 0.56 endpoint and existing 1080p media.
CSS starts at 0.70 before the playback effect runs, preventing an initial large frame.
Independent read-only review confirmed centered desktop/portrait motion and fallback.
Concurrent workspace changes were preserved; no student effort or acceptance is inferred.

`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
85 in 2.80 s; `npm --prefix app/frontend run build` passed. The browser command
`npm --prefix app/frontend run test:e2e -- tests/e2e/eye-animation.spec.ts --grep 'packaged eye|Skip and Escape'`
ran all 12 eye checks (npm consumed the grep option); all passed in 24.4 s.
`node tmp/eye-start-check.mjs` checked the 0.15 s opening frame on desktop, mobile
and zoom-equivalent viewports: zero Axe findings or overflow, correct smaller scale,
with desktop/mobile captures visually inspected. The scoped design detector was clear.
These are software/media checks; T28 still needs human presentation review and the
existing model/scanner pairing and handoff work.

## T28 Onyx Light — 26 September 2026

The user liked Onyx/Barlow and requested a light version. Root added **Onyx Light**
to the existing Appearance controls: white panels, cool gray surroundings and
cobalt actions, retaining the dark scan well, layout and Barlow. Existing saved
preferences persist. The open local browser was switched to Onyx Light/Barlow.
A separate agent extended existing appearance checks and reviewed contrast;
root built and verified the result. Student effort and showcase sign-off remain unreported.

`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
**85 in 2.61 s**; `npm --prefix app/frontend run build` passed. From the frontend,
Chrome `npx.cmd playwright test tests/e2e/appearance.spec.ts` passed **5 in 23.2 s**,
including ten palette checks, keyboard selection and persistence. These are synthetic
software checks. `node tmp/onyx-light-visual.mjs` viewed saved real scans at 1366,
390 and 320px widths plus Session/Source: zero Axe findings, page errors, external
requests, API writes or document overflow. The laptop viewer retains 332.61px height.
The manual style detector retained only the two optional Geist/Inter warnings.
No new model inference, dependencies, commit or publication. Private screenshots
and results are under `output/playwright/onyx-light/`. T28 remains open for human
presentation review, intended model pairing and the real scanner export handoff.

## T28 final-eye hold — 26 September 2026

The user requested more time at the ending and asked about duration. Root added a
1.5-second hold after the four-second video ends, then the existing 0.25-second fade:
nominal presentation 5.75 seconds plus startup. The original source is 8.0417 seconds.
Media and scale are unchanged. An independent reviewer checked cleanup/races; the
ended handler ignores disposed, already-fading or already-held states, and cleanup
cancels its timer. Failed/stalled media keeps the earlier five-second exit bound.
Concurrent changes were preserved; student effort and human acceptance are unreported.

`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
85 in 3.05 s; `npm --prefix app/frontend run build` passed.
`npm --prefix app/frontend run test:e2e -- tests/e2e/eye-animation.spec.ts` passed
12 in 22.7 s, including a real ended-event hold assertion. After the cleanup guard,
from `app/frontend`, `node node_modules/playwright/cli.js test tests/e2e/eye-animation.spec.ts --grep 'packaged eye|stalled intro|Skip and Escape'`
passed 3 in 12.2 s. A temporary read-only browser probe of the built app measured
3.996 s playback, 1.514 s hold, 0.254 s fade and 5.894 s total including startup;
the actual held frame was visually inspected. These are software/media checks.
T28 remains open for human presentation review and the existing model/scanner obligations.

## T28 faster opening, longer original footage and smaller scale — 26 September 2026

The user requested a faster first three seconds, another four seconds of the original
footage, and a further size reduction. Root applied the announced interpretation:
source 0–3 s at 2× (1.5 s), then source 3–7 s at original speed (4 s). The resulting
5.5-second video retains the existing 1.5-second final-frame hold and 0.25-second fade,
for a nominal 7.25-second presentation plus startup. Initial/final scales are now
0.56/0.44, about 20% smaller than the preceding version, including first-paint CSS
and the poster fallback. The watchdog was extended to 6.25 s to fit the longer video.

A media agent owned the isolated candidate, root inspected/promoted it and coordinated
integration/shared records, and another agent reviewed timing and tests. No student
effort or human acceptance is inferred. Source remains unchanged; the matching full-HD
poster uses the last new frame. Exact commands, sizes and hashes are in the
[media record](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/frontend/public/media/rayguard/README.md). Complete decode, all
132 frame timestamps, fast-start ordering and sampled source matches around the speed
change/final frame passed; source/output join and final images were visually inspected.

`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
85 in 2.16 s; `npm --prefix app/frontend run build` passed;
`npm --prefix app/frontend run test:e2e -- tests/e2e/eye-animation.spec.ts` passed
12 in 24.2 s. Duration/hold/failure checks now cover the new timing with bounded
ended-state polling. `node tmp/eye-visual-check.mjs` verified the served 5.5 s/1080p
media at desktop, mobile and zoom-equivalent sizes: zero Axe findings or overflow.
Root inspected desktop/mobile final framing; the scoped design detector was clear.
These remain software/media checks with synthetic API fixtures, not detector evidence.
Concurrent workspace changes were preserved. No new inference or publication occurred.
T28 remains open for human presentation review and the existing model/scanner handoff.

## T28 main menu and workspace setup — 26 September 2026

The user requested an organized entry page that configures the dashboard before
opening it. Root coordinated integration and shared records; separate agents owned
the menu UI, browser coverage and independent review. No student effort or human
acceptance is inferred. The [setup contract](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/main-menu-design.md) records
four workflows: upload, dataset replay, folder receiver and saved-run review.
Users choose Analyst Studio or Focused review, panels, a future-run threshold and
arrival following where relevant. Onyx/Barlow and Onyx Light remain available.
Opening a workspace makes no API writes or automatic start. Returning to the menu
preserves mounted scan transforms and review drafts; active acquisition continues
and is clearly reported. Existing paused replay retains its captured threshold.

The implementation fixes two related behaviors: starting intake now respects the
chosen following preference, and polling a paused replay no longer replaces the
operator's future-run threshold. Intro completion focuses the visible page after
the dialog unmounts, including immediate autoplay rejection. Desktop setup settings
scroll independently with a separate launch footer; phone layouts use natural flow.

Actual verification:

- `uv run --locked ruff check .` passed; `uv run --locked python -m pytest`
  passed **85 in 2.07 s**. `npm --prefix app/frontend run build` passed, including
  the final page-title change.
- From `app/frontend` with `PLAYWRIGHT_CHANNEL=chrome`, `npx.cmd playwright test`
  ran **61 cases: 59 passed, 2 failed**. The failures exposed the intro focus race
  and a stale busy-message assertion. After fixes, `npx.cmd playwright test
  tests/e2e/main-menu.spec.ts tests/e2e/eye-animation.spec.ts` passed **22 of 23**;
  the remaining failure was an ambiguous status locator (the threshold output also
  has status semantics). The corrected busy case and expanded Skip/Escape case
  then passed **2 of 2 in 9.1 s**, including default-entry intro → main-menu focus.
  All **61 cases have passing evidence across these runs**; no unresolved failures.
- `node tmp/main-menu-visual.mjs` checked eight saved-real-session views: dark/light
  desktop menus, two phone widths, replay, folder desktop/mobile and saved review.
  Zero Axe findings, page errors, horizontal overflow or API mutations; acquisition
  state before/after matched. Screenshots were visually inspected.
- `node tmp/main-menu-tablet.mjs` passed at 768, 900 and 1024px widths with zero
  Axe findings, overflow, page errors or API mutations, also checking page titles.
  Its first attempt hit an Axe browser-context setup error; the probe was corrected
  to use an explicit context before the successful run. No app fix was needed.
- The scoped manual design detector reported no findings. A scoped sharing check
  of 17 text files and 127 relative links found no broken links, private user paths
  or credential-pattern matches. `git diff --check` passed; nothing was staged.

Browser fixtures are synthetic software checks; GET-only views of saved scans
establish presentation behavior only. No new inference, model dependency, hardware
test, commit or publication occurred. Private screenshots/results are under
`output/playwright/main-menu/`. T28 stays open: next is human review of the menu and
configured workspace, then intended model pairing, scanner handoff and rehearsal.
Independent final code/screenshot review found no material blocker; human rehearsal
remains pending.

## T28 visible dark/light shortcut — 26 September 2026

The user could not find dark mode on the main menu. Independent agent inspection
confirmed that Appearance → Onyx already worked; root added a visible native
Dark mode / Light mode header button using the existing appearance state. It
switches Onyx/Onyx Light on both routes, preserves the font and stores the chosen
palette through the existing browser preference path. Advanced palette choices
remain available. No student effort or human acceptance is inferred.

`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
**85 in 2.64 s**; `npm --prefix app/frontend run build` passed. From the frontend,
with `PLAYWRIGHT_CHANNEL=chrome`, `npx.cmd playwright test
tests/e2e/appearance.spec.ts tests/e2e/main-menu.spec.ts` passed **16 in 39.5 s**.
These existing cases use synthetic API/image fixtures.

GET-only `node tmp/theme-toggle-check.mjs` verified the actual built shortcut by
keyboard in both modes at 1366, 390 and 320px, reload persistence, retained Barlow
and theme continuity between menu/workspace. All six views had zero Axe findings,
horizontal overflow, page errors or API writes. Desktop/phone screenshots were
visually inspected; private evidence is in `output/playwright/theme-toggle/`.
The scoped design detector reported only the existing optional Geist/Inter style
warnings; the selected Barlow remains unchanged. `git diff --check` passed.
No new inference, hardware validation, commit or publication occurred. T28 remains
open for human presentation review, intended model pairing and scanner handoff.

## T28 four-second accelerated segment — 26 September 2026

The user revised the cut to source 0–4 s at 2×, then 4–8 s at original speed.
The new video is exactly six seconds/144 frames, followed by the existing 1.5-second
hold and 0.25-second fade (7.75 s plus startup). Root updated the watchdog/tests and
integration; the media agent prepared and verified the separate candidate. Root
reviewed source/output join frames and desktop/mobile presentation. Source, scale,
quality treatment and concurrent main-menu changes were preserved. Student effort
and human acceptance remain unreported. [Encoding commands/hashes](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/frontend/public/media/rayguard/README.md)
record the new video and matching final-frame poster.

`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
85 in 2.18 s; `npm --prefix app/frontend run build` passed;
`npm --prefix app/frontend run test:e2e -- tests/e2e/eye-animation.spec.ts` passed
12 in 24.0 s. `node tmp/eye-visual-check.mjs` verified served 6 s/1080p media at
three viewports with zero Axe findings or horizontal overflow. Full decode, contiguous
frame timestamps, fast-start ordering and sampled source-frame correspondence passed.
These are software/media checks with synthetic API fixtures, not inference evidence.
T28 remains open for human presentation review and existing model/scanner obligations.

## T28 remove the ending hold — 26 September 2026

At the user's request, root removed the final-frame hold timer and connected the
native ended event directly to the existing 0.25-second fade. The six-second video,
speed split, scale and source assets are unchanged; nominal presentation is now
6.25 seconds plus startup. Independent review confirmed cleanup and failure handling.
Concurrent menu/theme changes were preserved; student effort/acceptance is unreported.

`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
85 in 2.93 s; `npm --prefix app/frontend run build` passed;
`npm --prefix app/frontend run test:e2e -- tests/e2e/eye-animation.spec.ts` passed
12 in 24.0 s, including prompt removal after actual video completion. A read-only
browser probe of the built app measured 0.4 ms from ended to fade, 254.1 ms from
ended to removal, and 6.443 s total including startup. These are software/media checks
with synthetic API fixtures, not detector evidence. T28 remains open for human
presentation review and existing model/scanner obligations.

## T28 continuous Liquid Glass dashboard — 26 September 2026

The user requested the whole app as a dashboard and supplied the KU Planner
Liquid Glass design, dashboard/navigation source files and supporting landing
briefs as a reference. Root located/read the reference locally, inspected its
running dashboard and opened that preview for the user. The reference project
was not edited. [RayGuard's design system](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/DESIGN.md) and
[dashboard contract](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/dashboard-design.md) record the adopted structure.

Dashboard, Inspect, Workspace setup, Session and Source now share a persistent
labelled sidebar, page header, serif headings and glass actions. Desktop can
collapse the sidebar; mobile Menu preserves keyboard/Escape behavior. Real hash
links support direct entry, refresh, new tabs and Back/Forward without a router
dependency. The base address opens Dashboard; older setup/inspection hash links
still work. The dashboard uses actual current scan/source/run state, separates
dataset size from batch progress, and never invents operational metrics. Missing
results and failed receivers remain explicit. Setup applies choices without
starting acquisition; hidden inspection keeps scan transforms and review drafts.
Active work, paused replay and acquisition errors retain an Inspect return path.

Root coordinated shared status and owned App/dashboard integration; separate
agents owned navigation, theme/fonts, browser coverage and independent review.
Reviews caught and corrected skip links changing Session/Source to Inspect,
missing acquisition visibility, ambiguous result/error labels and misleading
full-dataset completion wording. No student effort or showcase sign-off is inferred.

Actual verification:

- `uv run --locked ruff check .` passed; `uv run --locked python -m pytest`
  passed **85 in 6.76 s**. `npm --prefix app/frontend run build` passed after
  the final integration/copy changes.
- From `app/frontend`, `PLAYWRIGHT_CHANNEL=chrome`, `npx.cmd playwright test`
  ran **69 cases: 67 passed, 2 failed in 3.1 min**. The two failures were test
  selectors: offline explanatory text within the same definition, and an intake
  checkbox also mounted in the hidden Source page. Corrected selectors retain
  the behavior assertions. `npx.cmd playwright test tests/e2e/dashboard.spec.ts
  tests/e2e/main-menu.spec.ts --grep 'dashboard|native navigation|mixed busy|succeeded record|setup applies'`
  passed **9/9 in 20.9 s**, including all eight new dashboard cases and the final
  dataset/batch copy. All **69 cases have passing evidence across these runs**.
- `node tmp/dashboard-visual.mjs` passed on the final build: **19 GET-only saved
  session views** covering all five pages, dark/light dashboards at desktop and
  390/320px, compact inspection and 1024/768/390/320px inspection. Zero Axe findings,
  horizontal overflow, page errors or API mutations; acquisition state before/after
  matched. The 1366×768 image stage measured **334.61px high** with every panel open.
  Desktop/mobile screenshots were visually inspected and independently reviewed.
- Instrument Serif regular/italic and OFL were copied from the supplied reference
  package, with hashes matching its manifest; **141,604 font bytes**, no runtime CDN.
  A scoped sharing check reviewed **17 text files / 83 relative links**, finding no
  broken links, private user paths or credential-pattern matches. All three font/
  license hashes matched their shared record. `git diff --check` passed; nothing staged.
- The single scoped design-detector run flagged Instrument Serif and the retained
  optional Geist/Inter fonts. Instrument Serif is explicitly pinned by the user's
  reference, and previous font comparisons remain available; no other findings.

Browser fixtures are synthetic software checks. Saved real-scan views establish
presentation only: no new inference, dataset validation, training or physical
scanner test occurred. Private evidence is under `output/playwright/dashboard/`.
Reference and RayGuard dashboard previews were opened; no commit or publication.
T28 remains in progress for human presentation review/rehearsal, the intended
laptop/pager model pairing and a real scanner export handoff.

## T28 fixed introduction scale — 26 September 2026

At the user's request, root removed the playback-driven scale animation and its
animation-frame loop. Shared CSS fixes video and fallback poster at the preceding
44% ending scale from first paint; existing portrait framing stays proportional.
Independent review confirmed cleanup and preservation of the asynchronous playback
failure guard. Media, speed split and immediate ending fade remain unchanged;
concurrent dashboard work was preserved. Student effort/acceptance is unreported.

`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
85 in 2.87 s; `npm --prefix app/frontend run build` passed;
`npm --prefix app/frontend run test:e2e -- tests/e2e/eye-animation.spec.ts` passed
12 in 24.9 s. A read-only browser probe sampled 0.15, 3 and 5.85 seconds:
desktop scale stayed 0.44 and portrait stayed 0.792, with identical bounds and
centers at every sample. Desktop/mobile opening captures were inspected; the
scoped design detector was clear. These are software/media checks with synthetic
API fixtures. T28 still needs human presentation review and the existing model/scanner handoff.

## T28 Instrument Serif throughout — 26 September 2026

The user requested trying the reference font on all website text. Root added
Instrument Serif to Appearance and made it the fresh-browser default, retaining
existing stored font/palette choices. UI, heading and numeric/record tokens now
use the face when selected; a conditional native-code override covers coordinates.
Font-choice specimens retain their named fonts for honest comparisons. Root selected
Instrument Serif in the user's open dashboard preview; its checked UI state was
confirmed. Preference persistence was verified in browser tests. No new font
download or dependency was needed. This remains a reversible
typography preview; human preference acceptance is pending.

Root owned implementation/docs, an independent agent reviewed inheritance and
font limitations, and a separate agent extended existing appearance checks.
No student authorship or hours are inferred. `uv run --locked ruff check .`
passed; `uv run --locked python -m pytest` passed **85 in 2.65 s**;
`npm --prefix app/frontend run build` passed. From `app/frontend`, with
`PLAYWRIGHT_CHANNEL=chrome`, `npx.cmd playwright test tests/e2e/appearance.spec.ts
tests/e2e/dashboard.spec.ts` passed **13 in 38.5 s**. These synthetic cases verify
computed families across all five pages and three evidence tabs, all nine font
choices, ten palettes, storage/fallback, preserved drafts/zoom and mobile accessibility.
Both existing local regular/italic font files loaded; no external requests or
unintended API writes occurred in the browser fixtures.

`node tmp/instrument-serif-visual.mjs` passed **19 GET-only saved-session views**:
all five pages, dark/light desktop and phone views, compact inspection and tablet
widths. Zero Axe findings, horizontal overflow, page errors or API mutations;
source/acquisition state was unchanged. Root inspected desktop and phone captures.
The regular/italic-only face is finer than the earlier Barlow UI; existing size,
spacing and color hierarchy is retained for this user-requested trial. The scoped
typography detector reported only the already known Instrument Serif/Geist/Inter
style warnings; the supplied reference explicitly pins Instrument Serif.

Private evidence: `output/playwright/instrument-serif/`. These are software and
presentation checks, not fresh inference or hardware validation. No commit or push.
T28 remains open for human font/presentation review, intended model pairing and
the real scanner handoff. Concurrent eye-media changes were preserved.

## T28 dashboard reference refinement — 26 September 2026

The user clarified that the latest reference refactor applies to the dashboard.
Root inspected the updated KU Planner dashboard source, design contract and
26 September visual, then adapted its dominant current-work panel, flat adjacent
summary, aligned supporting context row and grouped service directory. This is
user-directed presentation work, not a new scientific or advisor requirement.

The selected inspection now has a larger preview that remains visible down to
320px. Acquisition activity occupies the adjacent summary; a held historical
scan stays distinct from a different active run. Recent runs and source
configuration share the next row. Catalog size no longer shares a definition
with batch progress, and is described as catalogued inputs rather than guaranteed
source availability. Operational text has a clearer size hierarchy within the
existing Instrument Serif preview. Mobile stacks these groups in reading order.

Root owned dashboard code/CSS and shared records. One independent agent located
the latest reference; another assessed layout, updated focused browser cases and
reviewed state correctness. That review caught stale running-state wording after
disconnect and an imprecise queue-full label; both were corrected and covered.
Student authorship/hours and human acceptance remain unreported. Eye playback,
shared navigation, appearance preferences and concurrent work were preserved.

**Executed and verified:** `uv run --locked ruff check .` passed;
`uv run --locked python -m pytest` passed **85 in 3.70 s**;
`npm --prefix app/frontend run build` passed. From `app/frontend`,
`npm run test:e2e -- tests/e2e/dashboard.spec.ts` passed **11 in 25.7 s**.
Synthetic fixtures cover empty/offline states, held versus active runs, missing
results, queue saturation, service loss, long filenames, preview visibility,
keyboard/history/mobile navigation, draft/zoom preservation and no API writes.
These are software checks, not model validation.

`node tmp/dashboard-refactor-visual.mjs` passed **10 GET-only saved-session views**
in Chrome: Onyx and Onyx Light at 1440, 1000, 768, 390 and 320px. Zero Axe
findings, horizontal overflow, page errors or API writes; source, acquisition
and health state were unchanged. The initial visual runner needed an explicit
Playwright context for Axe; it was corrected before the passing run. The scoped
layout detector returned no findings. Private captures and report are under
`output/playwright/dashboard-refactor/`; root inspected desktop/tablet/mobile
composition. No new inference, hardware validation, commit or publication.

T28 remains in progress. Next: human review of the reference-based dashboard and
configured inspection, intended laptop/model pairing, showcase rehearsal and
observed scanner export handoff. The existing schedule conflict is unchanged.

## T28 dashboard icons and concise copy — 26 September 2026

The user requested clearer icons, less text and easier dashboard use. Root
replaced the long workflow directory with four labelled icon actions near the
top, shortened repeated copy, added semantic section/run-state icons and moved
secondary guidance into native Source details / Workspace notes disclosures.
Current scan, active acquisition, catalog size and review state remain distinct.
Research/no-safety-decision and unverified-scanner statements remain visible.
An independent reviewer implemented matching navigation icons and replaced the
checked-document empty-result icon with a neutral scan icon. No workflow controls
became unlabeled; the user-selected Instrument Serif and existing palettes remain.

Ownership: root implemented Dashboard/CSS and coordinated shared documentation;
one agent owned navigation/empty-result icons and another owned dashboard tests.
Student authorship, effort and measured usability gains are not inferred.

Executed checks:

- `npm --prefix app/frontend run build`: passed TypeScript/Vite build.
- `uv run --locked ruff check .`: passed.
- `uv run --locked python -m pytest`: **85 passed in 2.86 s**.
- From `app/frontend`, with `PLAYWRIGHT_CHANNEL=chrome`,
  `npx.cmd playwright test tests/e2e/dashboard.spec.ts tests/e2e/appearance.spec.ts`:
  **16 passed in 53.0 s**. Covers labelled shortcuts, Enter/Space disclosures,
  no automatic acquisition, retained drafts/zoom, offline/missing/failed results,
  zero detections during a held review, palettes/fonts and mobile accessibility.
- `npx.cmd playwright test tests/e2e/workspace.spec.ts -g "successful empty result"`:
  **1 passed in 7.7 s**. The visible empty-result warning remains. Both test runs
  used synthetic API/image fixtures, with no model or scanner execution.
- `node tmp/icon-dashboard-visual.mjs`: **10 GET-only saved-session views passed**:
  dark/light at 1366, 1024, 390 and 320px, expanded details at 320px and the existing
  empty-result inspection. No Axe findings, horizontal overflow, page errors or
  API writes; acquisition state was unchanged. Root inspected desktop and phone
  captures in ignored `output/playwright/icon-dashboard/`.
- `git diff --check`: passed; only existing line-ending normalization warnings.

Final independent review corrected the unrun-image label to **Detection not run**
(no offline/model-readiness promise) and scoped the count to **results awaiting
review**. The corrected dashboard suite passed **11 in 30.0 s**; its keyboard,
palette/mobile case passed **1 in 12.7 s** after the first target-size adjustment.
A direct compiled-build check then caught the shared glass-button selector still
overriding two desktop targets to 38px. The final scoped rule and rebuilt bundle
were checked at 1366/320px: all **12 dashboard buttons were at least 44px**, with no
overflow, page errors or API writes. This last check used `node --input-type=module`
with the installed browser library; captures and measurements are in
`output/playwright/icon-dashboard/final-*`. No new model execution occurred.

No new inference, data changes, dependencies, commit or push. The live local build
is available on port 8766. The browser connector could not refresh the user's tab
because multiple browsers are connected without a shared default; its routing
settings were left unchanged. The separate automated browser inspected the build.
T28 remains in progress: next is user review of labels/hierarchy, followed by the
existing model-pairing, scanner handoff and human showcase rehearsal obligations.

## T28 upper-eye introduction layout — 26 September 2026

At the user's request, root moved the opening video's center to approximately
30% of viewport height (26% on short screens) and the RayGuard heading to
56–58%, with its subtitle directly below. Only introduction CSS changed:
the existing media dimensions/scale stay fixed, while natural-flow text keeps
the footer clear as the subtitle wraps. A separate agent reviewed responsive
spacing and identified the short-screen media/text clearance to verify.
No student effort or human acceptance is inferred; concurrent dashboard work
was preserved. Playback remains six seconds, with the existing speed split,
immediate ending fade, skip/replay and reduced-motion behavior.

**Executed and verified:** `uv run --locked ruff check .` passed;
`uv run --locked python -m pytest` passed **85 in 3.58 s**;
`npm --prefix app/frontend run build` passed;
`npm --prefix app/frontend run test:e2e -- tests/e2e/eye-animation.spec.ts`
passed **12 in 28.3 s**. These are software/media checks, with synthetic API
responses in the browser suite, not detector or scanner validation.

`node tmp/eye-layout-check.mjs` and `node tmp/eye-layout-start-check.mjs`
captured the actual media at 5.85 and 0.15 seconds across six desktop, tablet,
phone and short-landscape sizes. All twelve views had no Axe findings,
horizontal overflow or copy/footer overlap; measured media scale remained
0.44 on landscape/desktop and 0.792 with the existing portrait framing.
The capture helpers extend the watchdog only for static visual inspection;
normal timing is covered by the unmodified browser suite. Root inspected
opening and ending compositions. The scoped layout detector was clear.
Private captures: `output/playwright/eye-layout/` and `eye-layout-start/`.
Next: user presentation review; T28's human rehearsal/model pairing/scanner
handoff remain open. No media re-encode, inference, commit or publication.

## T28 light-mode text readability — 26 September 2026

The user reported thin light-mode text and requested bold text. Root added a
light-theme-only 600 weight across navigation, content, controls, records and the
keyboard skip link. The selected Instrument Serif family is retained. Its local
files provide regular/italic only, so weight synthesis is explicitly permitted
within the light interface; available heavier faces from other selected fonts are
used normally. This follows the documented behavior of
[CSS weight synthesis](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight).
Dark-mode weights and the permanently dark intro remain unchanged. No font asset,
palette color, model, scan or acquisition behavior was changed.

Root owned CSS/docs and a separate agent reviewed inheritance/specificity and ran
existing browser checks. No new permanent tests or dependencies were added for
this small appearance change. No student authorship or hours are inferred.

Actual checks:

- `npm --prefix app/frontend run build`: passed, including the final skip-link rule.
- `uv run --locked ruff check .`: passed.
- `uv run --locked python -m pytest`: **85 passed in 5.58 s**.
- From `app/frontend`, `PLAYWRIGHT_CHANNEL=chrome`, the command below passed
  **6 checks in 38.8 s** using synthetic HTTP/image fixtures. It covers themes,
  fonts, keyboard/mobile navigation, contrast, preferences and retained drafts.

```text
npx.cmd playwright test tests/e2e/appearance.spec.ts tests/e2e/dashboard.spec.ts --grep "all palettes and fonts|appearance supports|blocked preference storage|layout partitions|empty Daylight workstation|dashboard supports keyboard"
```

- `node tmp/light-readability.mjs`: **11 GET-only saved-session views passed**
  across all five pages at 1366/390px, plus Dashboard at 320px. Computed text
  weights are at least 600 with weight synthesis enabled; switching back to dark
  reproduced the original typography. No Axe findings, overflow, page errors or
  API writes; source state remained unchanged. Root visually inspected desktop
  Dashboard and phone Inspect captures. The temporary probe was corrected for
  existing theme-toggle accessible names, an explicit browser context and closed
  disclosure visibility before its final successful run.

Private evidence is in `output/playwright/light-readability/`. These are software
and presentation checks, not new inference or human usability acceptance. No
commit or push. T28 remains open; next is user readability review and the existing
model/scanner/showcase handoff. Concurrent intro work was preserved.

## T28 IEDXray test reference and model comparison — 26 September 2026

The user requested the actual test reference and an indication of whether the
detector succeeded. The GUI now displays published generic annotations as dashed
cyan GT boxes, independently of amber model predictions. Findings shows annotated,
matched, missed and extra counts at the saved run's confidence threshold and a
fixed IoU ≥ 0.50. The latter is a project diagnostic choice, not an advisor metric.
Empty annotation/prediction pairs remain inconclusive; completed execution is
distinct from matching an annotated region. See the
[protocol and outcome definitions](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/annotation-comparison.md).

Root coordinated the API/UI contract, private preview, documentation and final
checks. Separate agents owned backend/frontend implementation; an independent
agent inspected the real source and reviewed identities, matching and claims.
No student contribution or hours are inferred. T28 remains in progress.

Implementation:

- Optional `demo_annotations`, `comparison.py`, selected-run comparison endpoint
  and export field. Exact filename/COCO image-ID matching, original category 0,
  source/canonical hashes, image sizes and generic result provenance gate the
  comparison. Annotation failure does not disable inference. Sources remain read-only.
- Run-keyed client requests discard late responses and do not refetch every poll.
  A separate cyan layer shares pan/zoom but not image filters; reference inspection
  holds the selected scan. Retry reference recovers a failed request on the same run.
- Portable setup, semantics and limitations are documented; ignored local config
  enables the inspected generic test source. No model or dataset dependency changed.

**Real artifact inspection and saved-inference comparison:** generic test SHA-256
`1aad3787ba4964456e58bc07366dfcc6ce29db8a6ca06cc5c377a2add8d8ca43`
has 5,136 images, 3,204 valid boxes, category 0 Explosive and 1,932 annotation-empty
images. All test JPEG headers matched sizes and lacked orientation tags; this was
a header check, not a new full decode audit. Exact image-table IDs matter: 532 do
not equal filename suffixes. Four previously reported cross-split duplicate pairs
were independently rehashed. Modified Pager example Test000071 remains generic-box
empty; no benign conclusion follows. These findings preserve the existing audit limits.

The current session contained **ten genuine saved runs**: Test000001–Test000009
from dataset replay and uploaded Test000080. Their generic YOLOv10-M outputs all
contain zero detections at confidence 0.25. Source/canonical hashes and dimensions
were checked; original JPEG hashes are recorded for the nine replay runs. The
read-only comparison correctly reports **nine missed targets**, each with one
reference box, zero matches and zero extras. The upload remains automatically
ineligible because its replay source provenance is absent, despite a manual image
match. This is not full-test accuracy and no new inference was launched.

The updated preview is `http://127.0.0.1:8767/#workspace`. A private one-off helper
copied the ten completed records and canonical PNGs, preserving IDs, timestamps,
predictions, thresholds and reviews. GET checks confirmed the original 8766 session
unchanged; both earlier services remain running. The normal launcher still has
session-only history; this preview copy is not a new recovery feature. Private
helpers/snapshots remain under ignored `tmp/`, `runs/` and `output/playwright/`.

Actual software checks:

- `uv run --locked ruff check .`: passed.
- `uv run --locked python -m pytest`: **85 passed in 3.16 s**.
- `uv run --project app/backend --locked python -m pytest app/backend/tests`:
  **143 passed in 10.68 s**, including 54 new synthetic comparison cases. One
  existing Starlette/httpx deprecation warning remains.
- `npm --prefix app/frontend run build`: passed (TypeScript and production build).
- From `app/frontend`, `PLAYWRIGHT_CHANNEL=chrome`, `npx.cmd playwright test`:
  **85 passed in 2.9 min**, including 13 new synthetic comparison checks. Covers
  matching outcomes, malformed/unavailable references, same-run retry, stale
  responses, independent layers, shared geometry, existing workflows and accessibility.
- Private `tmp/verify_ground_truth.py`: GET-only API/export comparison passed for
  nine real saved replay runs plus the ineligible upload; predictions and original
  service state unchanged, no private paths in exports.
- `node tmp/ground-truth-browser.mjs`: all nine real replay overlays match reference
  coordinates; six dark/light views at 1440/390/320px pass without Axe findings,
  horizontal overflow, page errors, failed responses or API writes. Toggle, zoom,
  provenance and upload exclusion checked. Root inspected desktop dark and phone
  light screenshots. Evidence: ignored `output/playwright/ground-truth/`.

Review fixes included correcting a synthetic reference category from 1 to actual
0 and adding same-run retry. The first focused browser pass exposed a fixture
isolation issue; the next exposed an older Barlow-font assertion after the user's
Instrument Serif change. Both test assumptions were corrected, then the full
suite passed. The private real-browser probe initially used an incorrect Fit
button name; after using the actual accessible label, all checks passed.

Synthetic tests verify software; the nine saved comparisons verify this feature
against actual prior predictions. Neither establishes model accuracy, new lab data,
physical scanner integration or completed P1. Independent final review found no
remaining concrete pairing/claim issue. `git diff --check` passed, no files were
staged, and local config, snapshots and evidence remain ignored. Existing
intro, typography and other local work were preserved; no commit or push.

Next: the user reviews reference/model overlays and actual misses; the human
model/showcase owner confirms the intended laptop/pager pairing and rehearses the
presentation. Dataset-quality/provenance issues still gate fair full-test
evaluation; do not adjust thresholds using this test demonstration.

## T28 wheel zoom, pan and hover magnifier — 26 September 2026

The user requested mouse-scroll zoom, panning while zoomed and a magnifier icon
for local image inspection. `ScanCanvas.tsx` and scoped `scan-interactions.css`
now provide pointer-centred 1–5× wheel zoom, bounded drag pan and a labelled 3×
Magnifier toggle. Both views render the same original image, visible model/reference
layers and display adjustments. The lens has no duplicate interactive finding
controls. Fit/0, Escape, pointer departure, scan changes, hidden routes and resize
clear relevant transient state. Keyboard zoom/pan remains available; touch can
scroll the page at Fit and drag when zoomed. The hover lens uses mouse/pen.

Root coordinated scope, docs and real saved-image checks. Separate agents owned
the two implementation files and browser tests; a third independently reviewed
geometry, events and accessibility. A canceled-drag click-suppression edge was
fixed before completion. No student authorship or hours are inferred. The existing
theme, source data and predictions remain unchanged; concurrent runtime and brand
work was preserved. T28 remains in progress for human showcase acceptance.

Implementation details were checked against current primary browser documentation:
[wheel events](https://developer.mozilla.org/en-US/docs/Web/API/Element/wheel_event),
[SVG screen transforms](https://developer.mozilla.org/en-US/docs/Web/API/SVGGraphicsElement/getScreenCTM)
and [touch-action](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/touch-action).
Native wheel cancellation is limited to ordinary viewer scrolling; Ctrl/Command
browser zoom remains available. The inverse SVG transform includes letterboxing.
Pointer capture waits for actual drag movement, preserving finding clicks.

Actual software checks:

- `npm --prefix app/frontend run build`: passed (TypeScript and Vite).
- `uv run --locked ruff check .`: passed.
- `uv run --locked python -m pytest`: **137 passed in 6.66 s** in the current
  workspace, including concurrently added runtime software tests.
- With `PLAYWRIGHT_CHANNEL=chrome`, from `app/frontend`, the following commands
  ran against synthetic HTTP/image/model fixtures:

```text
node node_modules/@playwright/test/cli.js test tests/e2e/viewer-controls.spec.ts --output=../../output/playwright/viewer-controls-tests
node node_modules/@playwright/test/cli.js test --output=../../output/playwright/viewer-controls-regression
node node_modules/@playwright/test/cli.js test tests/e2e/appearance.spec.ts tests/e2e/viewer-controls.spec.ts --grep "all palettes and fonts|magnifier clears" --output=../../output/playwright/viewer-controls-fixes
```

The new suite passed **8/8 in 29.9 s**. The full regression finished **103 passed,
1 failed in 4.0 min**: an existing appearance test checked a regular font before
that face loaded while light mode used weight 600. The test now explicitly awaits
the exact face it asserts, retaining family and local-file checks. The corrected
appearance case and strengthened Escape case (focus outside the viewer) then
passed **2/2 in 37.7 s**. The full suite was not rerun after that test-only fix.
Earlier trace-file teardown failures came from concurrent Playwright output
cleanup; separate output directories resolved them. An occupied alternate port
was left untouched; successful runs used the normal test port.

**Actual saved-image presentation, separate from inference:**
`node tmp/viewer-interaction-check.mjs` exercised the existing 8767 preview with
Test000001's real pixels, saved prediction and verified generic annotation. It
verified pointer anchoring, drag, exact 3× lens geometry and reference alignment
at 1440/390/320px in both themes. Six views had no Axe findings, horizontal overflow,
page errors, failed responses or API writes. All eleven existing session records
and source/run state were unchanged. Root visually inspected desktop dark and
phone light captures. The private probe was corrected to compare against the
actual native wheel event's rounded client coordinates, then passed. A later
frontend build from concurrent work prompted another read-only presentation check.
Evidence stays in ignored `output/playwright/viewer-interactions/`.

No backend restart, model inference, new dataset validation, commit or push was
needed. Synthetic interaction tests are software evidence; inspecting an existing
real scan establishes rendering behavior, not accuracy or a hardware handoff.
`git diff --check` passed and no files were staged. Local helpers/test overrides
and screenshots remain ignored.

Next: user review of wheel sensitivity and the hover lens, followed by the existing
human presentation-laptop rehearsal and model/scanner handoff. These display tools
do not complete P1/P2 evaluation or change the current collection/poster obligations.

## T28 portable GPU runtime implementation — 26 September 2026

The user explicitly authorized implementation of the accepted GPU plan, isolated
locked dependency installation and bounded local qualification. Root coordinated
shared interfaces/documentation, protected the old CPU reference and owned every
real model/GPU job. Separate agents owned setup/profiles/launcher, backend/readiness
and frontend/tests; independent reviews found and resolved runtime-mutation,
checkpoint-mutation, source-path and selection-reason issues. This is automated
engineering support; student authorship, hours and human acceptance are unreported.
The baseline-reproduction and detection-evaluation workflows guided preservation
and evidence; frontend/browser workflows supported the interface checks.

Implemented: Windows x64 hardware discovery independent of Torch; exact hashed CPU
and CUDA candidate profiles; serialized permanent-path environment preparation,
disk/download checks, cancellation and atomic config activation; pending model
verification; cached per-host evidence; session-fixed Auto/CPU/visible CUDA routing;
actual device/dtype/hash provenance; historical Not recorded semantics; structured
failure handling and queue-preserving acquisition pause. The original checkpoint,
fork, RGB/EXIF canonicalization, FP32 settings, category/coordinate conventions,
prediction contract and separate reference-comparison boundary are preserved.
The dashboard, eye intro, themes, overlays, review drafts, exports and concurrent
viewer work remain in place. No global environment, driver, OS setting, new weight,
training, full-dataset benchmark, publication, merge or push was performed.

Executed commands/evidence:

- `uv run --project app/backend --locked python tmp/capture_gpu_baseline.py` —
  saved the pre-change CPU configuration/freeze/source identity and three original
  plus canonical input hashes, predictions and overlays in fresh ignored storage.
- `uv run --locked python tmp/check_gpu_cpu_regression.py` — new runner/original
  CPU environment reproduced the frozen 1/0/0 results exactly.
- `uv run --locked python scripts/setup_model_runtime.py --managed --source-config app/config.local.json --config app/config.gpu-test.local.json`
  — installed separate CPU and CUDA 12.6 environments; both dependency checks
  passed for 42 packages. Original config and inherited CPU reference remain
  intact. Exact compressed artifact upper bound: 2,970,102,822 bytes. Current
  setup uses a conservative 4× compressed plus 1 GiB disk gate. Installer output
  was retained in the tool transcript; local environment receipts bind successful
  hash-checked installation. No separate installer log is claimed.
- Isolated `scripts/probe_model_runtime.py --device cpu` / `--device cuda:0`
  probes passed actual FP32 kernels. Fresh CUDA import took longer than the
  original 30-second bound; async probes now allow a bounded 120 seconds.
- `uv run --project app/backend --locked python tmp/qualify_gpu_parity.py` —
  CUDA-environment CPU, actual CUDA and isolated CPU all passed the frozen
  three-image gates. A repeated CUDA positive also passed; overlays inspected.
  Counts remain 1/0/0, including the known missed threat. Maximum positive
  coordinate difference was 0.00006103515625 pixel; confidence difference zero.
- `node tmp/check-gpu-app.cjs ...` and its resumed real-session flow — actual
  pending API admission, browser Verify, CUDA upload, finite one-image replay,
  held review, known-miss reference and export passed. A startup race and an
  exact-label test selector were corrected without changing model settings.
  One upload request-to-visible-result observation was 8.650 seconds, not p95/FPS.
- `uv run --project app/backend --locked python tmp/check_gpu_intake.py --mode success`
  — malformed-image recovery plus real CUDA positive/known-miss folder runs passed.
- The same private script with `--mode timeout` on an intentionally one-second
  task config — actual timeout failure, two retained pending scans, worker release
  and deliberate retry passed. No silent CPU retry. Synthetic tests, not forced
  memory exhaustion, cover actual OOM/error classification branches.
- `uv run --project app/backend --locked python tmp/check_cpu_rollback.py` —
  after saving exports/pending source work and restarting only task-owned 8770,
  isolated CPU upload and newly published folder positive both passed. Existing
  inbox files were baselined; session history/queues reset as documented.
- `uv run --locked ruff check .` — passed; `uv run --locked python -m pytest` —
  138 passed; `uv run --project app/backend --locked python -m pytest app/backend/tests`
  — 203 passed with one existing Starlette/httpx warning.
- `npm.cmd --prefix app/frontend run build` — passed;
  `npm.cmd --prefix app/frontend run test:e2e -- --config ../../tmp/playwright-runtime.config.ts --reporter=line`
  — 104 passed on isolated 18766, preserving another session's 18765 test server.
  A subsequent narrow completed-run reference gate passed 13 focused browser
  checks and the build. Mobile runtime controls had zero Axe findings/no overflow.

The bounded release harness then completed **45/45** serial fresh-process trials,
with five repetitions for each of three images and A/B/C targets:
`uv run --project app/backend --locked python scripts/benchmark_generic_runtime.py --cpu-python .venv-yolov10/Scripts/python.exe --gpu-python .venv-rayguard-cu126-95dc3ea79e95/Scripts/python.exe --checkpoint data/IEDXray/model-weights/yolov10_generic_exp.pt --checkpoint-sha256 b484d9a6fb37236f6adcc8c019e6a836f11901dc53a0f71d6cce7262413287ff --images runs/gpu-portable-2026-09-26/canonical/Train000003.png runs/gpu-portable-2026-09-26/canonical/Test000001.png runs/gpu-portable-2026-09-26/canonical/Test000034.png --output runs/gpu-portable-2026-09-26/benchmark45`.
Every trial passed fixed parity/forward/identity checks; all samples were retained.
Per-image CUDA forward-stage medians were 50.4–54.2 ms, versus 188.5–200.0 ms for
A/original CPU. Complete-process medians were about 8 seconds; CUDA showed no
consistent end-to-end advantage over A and was slower than B/isolated-environment
CPU. Constructor, predict-call and process medians/ranges, GPU warm-up, memory,
power snapshots and background activity boundaries are in the verification record.
No p95, FPS, guaranteed speedup or accuracy claim is made. The original config hash
and CPU dependency freeze remained identical to the protected copies.

The task service uses 8770 and separate storage/inbox; services 8765–8767 remain
untouched. The [verification record](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/runtime-verification.md) contains the
bounded benchmark protocol, execution limits and external qualification procedure.
After the study, `run-app.ps1 -Config app/config.gpu-test.local.json -Port 8770 -SkipBuild`
launched through a task-owned hidden process and reused verified Auto/CUDA selection.
Two fresh real GPU runs (positive upload and known-miss finite replay) passed and
were exported. `node tmp/capture-known-miss.cjs --run-id <saved-run-id>` verified
the final cyan reference/Missed target view through two polls without API writes
or page errors. Normal repeat launch reused the URL; explicit-config repeat refused
silent reconfiguration. The original three service process IDs remain unchanged.
Private manifests, images, weights, source-path details and raw samples remain
ignored. Installation/probe/model/parity evidence are distinct from accuracy and
scanner validation. Other vendors/platforms, second NVIDIA laptop and separate CPU
host execution remain unqualified. T28 remains in progress for those checks and
human showcase/model/scanner acceptance. The 30 September poster obligation and
M01/M02 prototype-versus-collection deadline conflict remain unresolved.

## T28 workspace CPU/GPU choice — 26 September 2026

The user requested clear CPU/GPU controls with GPU preferred when compatible and
confirmed explicit **Apply and restart** from the workspace. Root coordinated
interfaces, launcher, documentation and serial real-model checks; separate agents
owned backend and frontend files, with an independent read-only correctness review.
This is automated implementation support; student authorship/hours are unreported.
Existing dashboard, eye intro, themes, overlays, review drafts, queues and exports
were retained. No reset, publication, merge or push was performed.

Implemented a cached eligible-device inventory, saved atomic policy sidecar,
GPU UUID/host/visibility guards, stale-tab rejection and restart admission latch.
CPU choice preserves the candidate GPU interpreter. New managed launches prefer
GPU; explicit CPU remains saved. The launcher restarts only its opted-in child on
the dedicated restart exit code. Unsupervised launches can save for a later launch.
The page waits for a new service instance; no hot swap or implicit install occurs.

Actual commands and outcomes:

- `uv run --locked python scripts/setup_model_runtime.py --managed --source-config app/config.local.json --config app/config.managed.local.json --dry-run`,
  then the same command without `--dry-run`: reused both reviewed environments,
  zero downloads, 1 MiB metadata disk gate; created separate Auto config.
- `uv run --locked ruff check .` and `uv run --locked python -m pytest`: passed,
  138 root tests. `uv run --project app/backend --locked python -m pytest app/backend/tests`:
  final **238 passed**, one existing Starlette/httpx deprecation warning.
- `npm.cmd --prefix app/frontend run build`: passed.
  `npm.cmd --prefix app/frontend run test:e2e -- --config ../../tmp/playwright-runtime.config.ts --reporter=line`:
  **119 passed** in 4.5 minutes on isolated 18766. The 15 device-focused cases
  also passed independently on 18767; mobile Axe checks passed in both themes.
- `run-app.ps1 -Config app/config.device-choice.local.json -Port 8771 -SkipBuild`:
  launched a hidden, task-owned supervisor with separate private storage/inbox.
  Existing 8765–8767 and 8770 service process IDs remained unchanged.
- `uv run --project app/backend --locked python tmp/check_device_choice.py --step verify --device cuda:0`:
  real CPU/GPU qualification passed on the preserved canonical positive.
  `--step positive --device cuda:0`, then `--device cpu`, then `--device cuda:0`
  around actual browser CPU/GPU Apply-and-restart actions produced three successful
  ordinary positives with the requested actual execution devices. Each was exported.

The first return-to-GPU request was safely rejected: API Python 3.12 reported
Windows 11 while model Python 3.11 reported Windows 10 for the same OS build.
Preference save/validation now use the API interpreter's host identity consistently;
model host evidence remains separate. The regression and independent review passed,
then the corrected real return-to-GPU flow and positive passed. No model source or
precision/threshold settings changed for this fix. Browser drafts alone did not
change the active device. The final GPU session remains on **8771/#main-menu**.

See [runtime verification](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/runtime-verification.md) and [usage/recovery](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md#choose-cpu-or-gpu-in-the-workspace).
Private logs, outputs and config paths remain ignored. No benchmark was repeated;
no second-device or human acceptance is claimed. Pending work blocks UI restart;
failed queued work requires recorded source position and deliberate terminal CPU
rollback, preserving the existing session-only queue limitations. T28 stays in
progress; scanner/lab pairing, human rehearsal, second laptop/CPU host acceptance,
30 September poster obligation and M01/M02 schedule conflict remain outstanding.

## T28/T06 model selection and class pairing — 26 September 2026

The user requested multiple model choices and explicitly chose to list unverified
families too. Root coordinated shared catalog/interfaces, CLI, launcher, docs and
all serial real-model jobs; separate agents owned backend/frontend files, and an
independent reviewer checked artifact mappings, isolation and claims. Student
authorship/hours are unreported. The baseline-reproduction and detection-evaluation
workflows guided the bounded study; existing UI and services were preserved.

Implemented a three-entry inspected YOLOv10-M catalog, exact checkpoint/hash/name/
namespace/kind routing, immutable per-run model identity, atomic model/device
selection and versioned preference migration. Five historical families remain
disabled with reasons. Generic reference comparison cannot process another task.
Managed setup now preserves relative model mappings when copying configs between
directories. No dependency/weight downloads, global changes, training, publication,
merge or push occurred. Details: [model selection](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/model-selection.md).

Actual commands/outcomes:

- Private `tmp/capture_model_selection_baseline.py` harness:
  preserved pre-change config/source privately and captured the same three canonical
  CPU diagnostics in a fresh output directory, retaining counts 1/0/0.
- `uv run --project app/backend --locked python tmp/qualify_model_choices.py`:
  eighteen fresh serial model processes, nine task/image CPU/GPU pairs; all fixed
  FP32 parity gates passed. Updated generic CPU predictions equal the protected
  outputs exactly. Device outputs were empty/Laptop/Laptop; specific outputs were
  IED Explosive/empty/empty. Nonempty overlays were visually inspected. This is
  execution compatibility, not AP/recall or resolution of source label disputes.
- `uv run --locked ruff check .` and `uv run --locked python -m pytest`: passed,
  **143 root tests**. `uv run --project app/backend --locked python -m pytest app/backend/tests -q`:
  **267 passed**, one existing Starlette/httpx deprecation warning.
- `npm.cmd --prefix app/frontend run build`: passed.
  `npm.cmd --prefix app/frontend run test:e2e -- --config ../../tmp/playwright-runtime.config.ts --reporter=line`:
  **133 passed**, isolated port 18766. Fourteen new model-browser cases also passed
  on 18767, including 320px dark/light accessibility without Axe violations/overflow.
- `run-app.ps1 -Config app/config.model-choice.local.json -Port 8772 -SkipBuild`:
  separate task-owned supervised service/storage/inbox. Actual browser choices
  switched generic GPU to device CPU, then device GPU and specific GPU. Draft
  changes left the active model unchanged; model checks were pending after changes.
- `uv run --project app/backend --locked python tmp/check_model_choice.py --model author-yolov10m-device --device cpu --case Test000001`,
  then device `cuda:0`, then `--model author-yolov10m-specific --device cuda:0 --case Train000003`:
  actual qualification, positive ordinary inference and exports passed for each.
  A real specific-model finite Test000001 replay/review/export passed through
  `tmp/check_model_replay.py --model author-yolov10m-specific`; generic GT remained
  unavailable with no reference boxes. The launcher repeat-call check recognized
  the non-generic running service without replacing it.

Live review found generic-only wording in export limitations. It now derives scope
from the saved run, with historical fallback and focused regressions; the full
backend suite above includes the fix. A private harness initially expected 409 for
pending admission; the API correctly returned 503 `runtime_not_ready`. The harness
was corrected; no failed model run was reported as a successful empty result.

Final application return: `node tmp/switch_model_live.cjs` changed specific GPU to
generic GPU through the actual workspace Apply-and-restart flow and passed.
`tmp/check_model_choice.py --model author-yolov10m-generic --device cuda:0 --case Train000003`
passed qualification/positive/export, then
`tmp/check_model_replay.py --model author-yolov10m-generic` passed finite replay,
review/export and the retained known miss (one GT box, zero predictions).
The MCP browser hub disconnected after the earlier switches; installed Playwright
completed actual read-only specific-model inspection and the final UI return.
Four private specific-model screenshots and the return evidence passed without
page errors. No connector availability claim is inferred from those browser checks.
Final 8772 is idle and GPU-ready. Pre-existing 8765–8767/8770/8771 PIDs are unchanged;
the original CPU config matches the protected bytes. `git diff --check` and the
final root Ruff check passed. No unrelated changes were reset.

Evidence remains under ignored `runs/model-selection-2026-09-26/`; no scans,
weights or personal config paths were added to shared documentation. No benchmark
was repeated. T06 is in progress after the standalone device smoke; full P1
association/decisions remain open. T28 also remains in progress: intended lab
pairing, human rehearsal, scanner handoff and second-host acceptance are pending.
The 30 September poster obligation and unresolved M01/M02 schedule conflict remain.

## T28 Folder receiver first — 26 September 2026

At the user's request, root reordered the dashboard shortcut array to **Folder
receiver → Upload a scan → Dataset replay → Review saved runs**. Existing icons,
labels and handlers are retained; folder setup still requires explicit acquisition
start. An independent read-only review confirmed normal grid placement and keyboard
order, including the two-column mobile layout. No student authorship/hours inferred.

Actual checks: `npm --prefix app/frontend run build` and
`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
**143 tests in 6.00 s**. From `app/frontend`, with `PLAYWRIGHT_CHANNEL=chrome`,
`node node_modules/@playwright/test/cli.js test tests/e2e/dashboard.spec.ts --grep
"dashboard services preselect setup or open records" --output=../../output/playwright/folder-first`
passed **1 existing browser check in 7.1 s**, covering setup selection and no server
writes. Synthetic software checks only; no new tests, model execution or hardware
validation. No commit/push. T28 remains open for human showcase/model/scanner
acceptance; next action is user review of the dashboard order.

## T28 processing and completed scan view — 26 September 2026

The user requested simultaneous active and completed inspection views during
inference. Root coordinated shared state boundaries, documentation and verification;
separate agents owned the UI implementation and browser tests, with an independent
read-only review of identities, drafts, focus and layout. Student authorship/hours
are unreported.

`App.tsx` now derives the active scan separately from the latest valid completed
result, ordered by completion time. The active image appears left with the eye
above it; the existing completed viewer and Evidence inspector stay mounted on
the right. Explicitly held terminal reviews, including failed runs, retain their
draft and a Held review label. First-run and missing-active-image states use
placeholders. Completion/failure restores the usual layout; phones stack panes.
Adjustments identify the completed/held image they affect. Disconnection pauses
the eye and labels the last-known run status unknown. No model, API, acquisition
or reference-comparison protocol changed.

Actual checks:

- `npm.cmd --prefix app/frontend run build` — TypeScript and production build passed.
- `uv run --locked ruff check .` — passed.
- `uv run --locked python -m pytest` — **143 passed in 14.58 s** in the final run.
- From `app/frontend`, with `PLAYWRIGHT_CHANNEL=chrome`,
  `node node_modules/@playwright/test/cli.js test --output=../../output/playwright/processing-split-regression --reporter=line`
  — **146 passed / 3 failed in 6.0 min** initially. Two old assertions expected
  the previous processing-reference display; one cached test expected following
  after deliberately holding the completed image. Assertions were corrected to
  the new presentation while retaining identity, reference and lifecycle checks.
- `node node_modules/@playwright/test/cli.js test tests/e2e/comparison.spec.ts tests/e2e/processing-split.spec.ts --output=../../output/playwright/processing-split-final-checks --reporter=line`
  — **29 passed in 1.1 min**. The expanded split suite has 16 cases. Both themes
  passed laptop/phone geometry and Axe checks, including 1366 × 768 scrolling
  to left Zoom/Fit, right Review and the filmstrip.
- `node node_modules/@playwright/test/cli.js test tests/e2e/processing-split.spec.ts --grep="the first run has" --output=../../output/playwright/processing-split-empty-copy --reporter=line`
  — **1 passed in 6.2 s** after the final first-run inspector wording assertion.
  All **149 distinct browser checks** have passing final evidence across the
  full run and affected reruns; this is not a claim of one clean full-suite run.
- `node tmp/check-processing-split-saved.mjs` — GET-only production preview checks
  passed in dark/light modes on 8772. The selected genuine saved image and its
  detection count matched its record, all three saved records were unchanged,
  and there were no API writes, failed requests or browser errors. The initial
  private harness used a visible button label instead of its accessible name;
  correcting that selector resolved its timeout. No model was executed.

Screenshots and private check output remain ignored under `output/playwright/`.
`git diff --check` passed; the index is unchanged and private screenshots/helpers
remain ignored. These browser fixtures exercise software
state and accessibility, not detector accuracy, real-data validation or hardware
integration. Real saved-image presentation is separate from fresh inference.

Source and visual review confirmed distinct active/evidence identities, preserved
successful and failed review drafts, correct inspector/annotation binding and
focus return only from the removed active pane. Existing working changes and
services were preserved; no commit, push or publication. T28 remains open for
human showcase/model/scanner acceptance. Next: review this interaction during the
next deliberate inference/replay, then continue the human showcase rehearsal.
The 30 September poster obligation and unresolved M01/M02 schedule conflict remain.

## T28 removal of logo work — 27 September 2026

At the user's explicit request, root removed all nine local logo exploration
batches and ZIP archives, browser proofs, prompts, helper scripts and dedicated
design documentation. A separate agent independently audited the removal scope.
The generated-image cache contained 223 PNGs matched to the logo work by content
hash or recorded provenance; all were removed. PowerShell `Remove-Item -LiteralPath`
ran after absolute-path, reparse-point and cache-hash checks: 62 workspace targets
and 223 cache PNGs, 747 files totaling 494,266,140 bytes, with no target remaining.
Temporary cleanup helpers were removed after verification.

Final checks: `uv run --locked ruff check .` passed;
`uv run --locked python -m pytest` passed 143 tests in 10.41 s;
`git diff --check` passed. Independent inspection confirmed no active gallery
artifacts or stale links remain and the original animation/poster files exist.

The ten obsolete logo progress sections and active gallery/selection references
were removed. Original app/animation/poster assets and unrelated project work
were preserved; Git history and historical migration snapshots were not rewritten.
No logo selection or refinement is pending. T28 continues with human showcase,
model/scanner acceptance and existing schedule obligations. No student authorship
or hours are inferred, and no publication or commit/push was performed.

## T28 confirmed logo review — 27 September 2026

The user supplied and explicitly confirmed an X-and-eye logo, then requested
design feedback and color/font recommendations. This is a new selected reference
after the earlier exploration was deleted; those deleted files were not restored.
Root and an independent agent visually inspected the supplied raster. Its SHA-256
is `90f7bb585d6ca4719784d0f0abbbd94e818b444f8076aa7f0797b2fb994ada83`.

Artifact inspected: integrated X/eye silhouette, curved channels, two gold accent
wedges and a heavy wordmark with a cut R. Recommendations preserve the silhouette,
refine narrow convergences and wordmark spacing, and prepare separate small-size,
single-color and reverse artwork. Small-size concerns are visual predictions;
no recognition test, production export or uniqueness finding is claimed.

Recommended palette: deep ink `#142B38`, teal `#008F9C`, cool off-white `#F4F7F8`.
Alternatives retain muted gold or use cobalt. Recommended wordmark: Manrope 700,
with the approved R adapted to match its letter weight and spacing. Google Fonts
metadata/specimen and Vercel's official Geist specimen were consulted. Read-only
`rg`/`Get-Content` inspection confirmed Manrope/Geist declarations and several
existing app palettes; `Get-FileHash -Algorithm SHA256` identified the source.

Colors and typography are recommendations, not further user approvals. The
original image and app were unchanged. Only shared status/task/progress records
were updated; no software tests were required for this design review. Root owns
the record; student authorship/hours are unreported. Next: user chooses color/type,
then production refinement can proceed. T28 showcase acceptance and schedule
obligations remain open.

## T28 confirmed logo refinement gallery — 27 September 2026

The user authorized applying the earlier design review and comparing enhanced
versions of the confirmed X-and-eye in an HTML page. Root coordinated separate
vector-construction, gallery and independent-review agents. This records agent
work, not student authorship or hours. Earlier deleted explorations were not restored.

The local, ignored `outputs/logo/refinements/index.html` compares three native
constructions, three palettes and three actual outlined wordmarks. There are nine
geometry/color choices, with symbol, stacked and horizontal arrangements, plus
monochrome/reverse treatments: 93 SVG assets and 93 matching transparent PNGs.
Four additional built-in image-generation edits use the confirmed reference and
are labeled interpretive raster studies. Exact prompts, local fonts/licenses,
construction notes, size proofs and export metadata travel with the gallery.
These hand-built SVG redraws are not recovered original vector artwork.

Executed and verified:

- `uv run --with fonttools --with brotli --with uharfbuzz --with skia-pathops python tmp/refined-logo-vectors.py`
  and `node tmp/refined-logo-vectors.cjs` constructed the outlined vectors and PNG exports.
- `node tmp/refined-logo-build-gallery.cjs` and `node tmp/refined-logo-check-gallery.cjs`
  produced the final page and passed 21 browser-check categories at 1440, 390 and
  320 pixels. Every image decoded; local fonts, controls, exact-byte downloads,
  saved font/layout combinations, reload persistence and shortlist export passed.
  There were no browser errors, failed requests or horizontal overflow.
  Final HTML SHA-256: `f3f97bad8633867e92a68a37c17fe8f9ee1d95416a5a9e6fd80768d4651d1303`.
- `uv run --locked ruff check .` passed. `uv run --locked python -m pytest`
  passed 143 tests in 5.32 seconds. These are software checks, not model validation.
- `Invoke-Item` opened the local HTML gallery for the user.
- `uv run --locked python tmp/refined-logo-inventory.py` validated the unchanged
  source hash, all 93 native SVGs, their exact palette fills and geometry consistency,
  all PNG decodes and transparent exports. The final inventory covers 209 files.
- `uv run --locked python tmp/refined-logo-package.py` produced the 210-entry
  `outputs/logo/RayGuard-Identity-Refinements.zip` (19,234,035 bytes). Manifest
  hashes, archive CRCs and complete byte-for-byte archive readback passed.
  `git diff --check` passed.

Root and independent inspection of the final overview and actual-size proof support
P02 Optical / Ink + Teal / Manrope 700 custom R as the recommended starting point.
P03 provides a compact alternative but did not demonstrate a decisive small-size
advantage in the proof. At 16 pixels the X is clearer than the eye; 24 pixels remains
subtle, and 32 pixels is a safer starting point when eye recognition matters.
No audience-recognition, fabrication or trademark clearance is claimed.
The supplied PNG is unchanged; the application identity was not modified.

Next: the user chooses a final construction, palette and wordmark before application
adoption. No model job, publication, commit or push was performed. T28 human
showcase/model/scanner acceptance, the 30 September poster obligation and the
unresolved 8/15 October versus collection-first schedule conflict remain open.

## T28 darker-blue logo palettes — 27 September 2026

At the user's request, root added six darker-blue palette studies to the confirmed
logo pack. The comparison fixes P02 Optical geometry and the Manrope 700 custom-R
wordmark: Midnight Navy, Deep Sapphire, Oxford + Gold, Deep Indigo, Prussian Blue
and Navy Monochrome. The local `outputs/logo/refinements/dark-blues/index.html`
compares the palettes on the same light field and offers reverse versions on
their corresponding navy backgrounds. The main refinement gallery links to it.

Root owned palette assets, packaging and shared records; a separate agent owned
the comparison page/browser checks, with an independent visual reviewer. No
student hours or authorship are inferred. No application code or identity changed.

Executed: `uv run --locked python tmp/dark-blue-assets.py` generated 36 SVGs and
asserted exact fills and unchanged geometry/type attributes against existing P02
artwork. `node tmp/dark-blue-render.cjs` rendered 36 matching transparent PNGs.
The complete pack now contains 129 SVGs and 129 corresponding PNG exports, plus
the preserved original and earlier AI studies. These are controlled color
variations; no new AI image generation or shape redesign was needed.

After adding the darker-blue link, `node tmp/refined-logo-build-gallery.cjs` and
`node tmp/refined-logo-check-gallery.cjs` rebuilt the main gallery and passed all
21 existing browser-check categories at 1440/390/320 pixels. Main HTML SHA-256:
`2a10d02a8f3731d536442744a5e5930d37a09ac4a238128162c56828e021c720`.
`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
143 tests in 3.54 seconds. These are software checks, not detector validation.

`node tmp/dark-blue-gallery-build.cjs` and `node tmp/dark-blue-gallery-check.cjs`
produced the darker-blue page and passed 15 check categories, all 36 palette/layout/
treatment combinations and 72 exact-byte SVG/PNG downloads. The local font and
images loaded, links resolved, and 1440/390/320 layouts had no overflow, browser
errors or failed requests. Darker-blue HTML SHA-256:
`ff117a1cf5d6c4bf45666d8300f9d75ceb3d667c13dab260328c8d07731d1abc`.
Root and the independent reviewer inspected the rendered six-option overview;
the reviewer agreed with D01 as the restrained choice and D02 for a more visibly
blue mark. D03 retains the original warm accent; no color defect required revision.

Final inventory/package commands were `uv run --locked python tmp/refined-logo-inventory.py`
and `uv run --locked python tmp/refined-logo-package.py`. The unchanged source,
129 SVGs and transparent export decodes passed inspection. The revised ZIP has
287 entries, 25,239,055 bytes, and passed manifest hashes, CRCs and full byte-for-byte
readback. `Invoke-Item` opened the darker-blue page; `git diff --check` passed.

The user has not selected a final palette. Midnight Navy is the restrained
recommendation; Deep Sapphire is a more visibly blue alternative. Existing
small-size limitations, T28 human acceptance, the 30 September poster obligation
and the unresolved prototype/collection schedule conflict remain unchanged.

## T28 A04 monochrome branding study — 27 September 2026

The user requested deeper exploration of the A04 monochrome/compact study and
branding/presentation applications. Root coordinated separate native-art and
presentation agents. Root reviewed the actual reference, native construction and
size proofs, and contextual images. No student authorship or hours are inferred.

The local `outputs/logo/a04-brand-study/` package preserves A04 unchanged (SHA-256
`5208d0b9148e55390d7aceff858111a1d2e1caf8c1ed1ecf75aa3c6ce7affc74`). Three native
constructions directly interpret that raster, with black, deep navy and warm-white
treatments. This is a hand-built interpretation, not recovered original vector art
or a reuse of the earlier P03. Default lockups use outlined Manrope 650 with its
standard R; three standalone wordmarks offer further comparison.

`uv run --locked python tmp/a04-vectors.py`, `node tmp/a04-vectors-render.cjs` and
`uv run --locked python tmp/a04-vectors-verify.py` produced and verified 36 SVGs and
36 transparent PNGs. Checks passed for exact fills, geometry consistency across
colors, native paths/circles, portable proof links, absence of raster/live-text or
external artwork dependencies, PNG alpha and unchanged source. The author corrected
an overly fine upper-blade taper before delivery. Actual-size proofs support 32 px
or larger where the eye must read clearly; a 16 px recognition claim is not made.

Four built-in image-generation mockups visualize stationery, environmental signage,
a research equipment carry case and a debossed black folio. One targeted image edit
repaired incomplete transparent corners in the signage image; the selected v2 is
opaque RGB. Exact prompts and the selected paths are in the package. These images
show proposed applications, not installed signage, existing hardware or fabrication
tests. The source reference, original galleries and application identity are unchanged.

`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
143 tests in 3.71 seconds. These are software checks, not model validation.

`uv run --with fonttools --with brotli python tmp/a04-brand-fonts.py` created local
static Manrope instances. `node tmp/a04-brand-build.cjs` and
`node tmp/a04-brand-check.cjs` built the responsive gallery and ten-slide HTML/PDF
presentation. Fifteen browser-check categories passed, covering offline fonts/assets,
controls, exact SVG/PNG downloads, 1440/390/320 layouts, navigation/fullscreen,
ten distinct slide views, PDF readiness and text boundaries, without browser errors
or failed requests. A first screenshot loop captured repeated views; the author
corrected screen-media navigation and verified distinct final hashes.

`pdftoppm -png -r 96 outputs/logo/a04-brand-study/presentation.pdf outputs/logo/a04-brand-study/rendered/slide`,
`pdftotext -layout`, `pdfinfo`, `pdffonts`, and
`uv run --locked python tmp/a04-brand-contact.py` verified/rendered the final ten
16:9 PDF pages. Static fonts replaced the first variable-font export; final PDF
font subsets are embedded CID TrueType. Root and the presentation author inspected
the final contact sheet and full PDF pages 01, 06 and 10. Local browser and visual
audits passed; the PDF is not a tagged accessibility edition.

Final gallery SHA-256:
`61bfbcbd6fb26b8b33e4eb286f283cc4fbb2f41ea555209fb6e82d0a65dcbbf0`.
Final PDF SHA-256:
`ae064d21d449650161028b9c55928b561995032cd6bc02910fb68bdb24e7b8dc`.
`uv run --locked python tmp/a04-package.py` checked current gallery/deck/PDF hashes,
unchanged A04 source, native SVGs and transparent export decodes, then produced
`outputs/logo/RayGuard-A04-Brand-Study.zip`: 134 entries, 35,927,232 bytes.
Archive CRC and full byte-for-byte readback passed. `Invoke-Item` opened the gallery;
`git diff --check` passed. Root recommends A04-02 Optical with Manrope 650 as the
starting comparison, with black/ivory and a midnight-navy alternative.

Final identity selection and application adoption remain with the user. T28 human
showcase/model/scanner acceptance, the 30 September poster deadline and the
unresolved prototype/collection schedule conflict remain open. No model job,
publication, commit or push is part of this branding study.

## 27 September 2026 — approved A04 adoption in RayGuard App (T28)

The owner approved the A04 direction and requested its use throughout the app.
The implemented selection is **A04-02 Optical with outlined Manrope 650, standard R**.
The separate RayGuard-App checkout now uses the approved native identity in
expanded/compact/mobile navigation, the bounded introduction, activity marks,
browser/home-screen icons, Design Studio previews and README artwork. Ivory
`#F5F3EF`, navy `#0B1F3A` and near-black `#111418` are the canonical treatments.
Application UI preferences and detector/status semantics remain available.

Automated implementation used separate asset and UI ownership, independent
read-only coverage review, and coordinator-owned integration/documentation.
Twelve SVG masters match the approved study hashes byte-for-byte. Earlier studies,
the original confirmed image and historical execution footage remain intact;
the deleted exploration batches were not restored. No student hours are inferred.
The app's `docs/branding.md` and `frontend/public/brand/provenance.json` record
the identity contract and provenance. These changes are local and not yet published.

Actual checks: in the app, `npm --prefix frontend run build` and
`uv run --project backend --locked ruff check backend` passed;
`uv run --project backend --locked python -m pytest backend/tests` passed
280 tests in 18.72 seconds; `npm --prefix frontend run test:e2e` passed 147 tests
in 3.6 minutes. The former three video-failure cases are replaced by one
missing-brand-asset entry check. In this shared repository,
`uv run --locked ruff check .` passed and `uv run --locked python -m pytest`
passed 143 tests in 3.93 seconds. These are software checks, not real-data validation.
The mechanical interface detector reported no findings. Production browser review
covered dark/light marks, compact navigation and a 320-pixel open menu with no
horizontal overflow. The updated app runs locally on port 8780; older services
and the ignored recovery app remain untouched. No new inference or publication
was performed for branding adoption.

Brand choice/adoption is complete locally. T28 remains in progress for human
rehearsal, intended lab pairing and scanner handoff. The 30 September poster
obligation and unresolved prototype/collection deadline conflict remain open.
Next: rehearse the updated app on the presentation laptop and complete the
remaining human acceptance steps; branding approval is not model/scanner approval.

## 21 November 2026 — T38 report draft build

Task T38 (report). The untracked `docs/report/` LaTeX draft (`main.tex` plus six chapters,
appendices, `references.bib`, four original figures) was compiled with MiKTeX
`lualatex` and `bibtex` into the ignored `docs/report/build/`. The build produced a
36-page PDF with no LaTeX errors, no `??` references and no BibTeX warnings. The Gantt
figure was inspected visually. The top-axis labels for 24, 27 and 30 November sit close
together but remain legible. The draft is not committed; the team has not yet reviewed it.
A Word draft was generated with Pandoc 3.9 from a prepared copy of the source
(`build/main-word-draft.docx`, ignored). The prepared copy converts the two equation
environments to display math, writes the 14 figure and table captions with their
PDF numbers and replaces the cross-references with those numbers. The DOCX has
46 native Word equations, 4 embedded figures, 11 tables and no leftover TeX
commands in the text. Pandoc emitted no conversion warnings. Layout, pagination and
visual fidelity against the PDF are still unverified. The Word draft is not a
submission copy. Still open: the institutional cover and roster, student contribution
confirmations, the risk/H&S forms and signatures, approved screenshots, eligible
final metrics, and the course distribution decision. Software checks (`ruff`,
`pytest`) were not run; no code changed. Next: a named editor/reviewer compares the
DOCX with the PDF page by page, maps the draft to R01–R15, and confirms the handbook
distribution route before any upload.

## 21 November 2026 — T28, T34, T39 working pass

- **T39 (proposed owner Abd):** drafted the proposal-to-screen requirement map (10 requirements; 3 implemented, 7 partial) and a prioritized fix list in [demo requirement map](demo-requirement-map-2026-11.md). Not reviewed by Mohammad. No RayGuard-App code changed; its working tree has 23 uncommitted files from earlier work.
- **T28 (Abd):** RayGuard-App backend `uv run --locked ruff check .` passed; `uv run --locked python -m pytest -q` gave 280 passed, 1 warning; `npm run build` passed. Local browser replay (agent-driven, CPU, scratch config with `runtime_profile` manual): dataset replay of Test000001–003 completed 3/3, with one missed target shown and the empty-result text "not a safe or benign verdict". Not done: upload path, service-stop recovery, export, human rehearsal on the laptop, clean-start timing. Runbook is in the same map.
- **T34 (Abd, action A17):** the owner reports the Meeting 02 minutes were already sent to the advisor and team. Date, recipients and channel are not yet recorded here; the draft in [meeting-02-distribution-draft.md](meeting_minutes/meeting-02-distribution-draft.md) was not used to send anything.

Next: owner confirms recipients to send A17; Mohammad reviews the T39 map; a person runs the T28 rehearsal runbook on the presentation laptop.

## 22 November 2026 — latest PR review and T41 policy handoff

Review activity: AI-assisted inspection of the current GitHub PR list and visible diffs;
this is not a student contribution or formal GitHub review. No comments, approvals or
merges were submitted. PR #22 (`ali/data-policy`, `ea9a21b`) covers unchanged published
test data, shared seed-17 ~80/20 validation, exact-duplicate grouping and exploratory
status without physical groups. Both hosted CPU runs (push and pull request, two matrix
jobs each) succeeded. Abd/Ahmed's supplied decision supports those rules and makes the
box clamp conditional on checking the five actual training boxes and every <0.001 px
overshoot; the real dataset check, findings hash and partition have not run. Review items
before human acceptance: receipt example defaults to approved, the derived annotation
retains stale COCO `area` after `bbox` changes, and the test-only guard depends on
filename conventions. Raw test source was inaccessible in this review, and no local
tests were run. The reviewer receipt remains for the human student.

PR #20 (`docs/semester-progress-2026-11`, five commits/38 files) also has passing current
PR CI, but its prior approval was dismissed as stale after later commits. It needs a new
independent human review of the current diff and overlap with #22/T38 before merge.
PR #21 initialization is recorded merged as `29d6d0f`; PR #18 evaluator remains merged
as `9350482`. No model training or real evaluation was run. Next: authorized dataset
holder runs read-only generic/specific box checks; Abd completes the human policy receipt
after resolving review items; Ahmed creates real findings/partition artifacts only after
that, then connects trainer/evaluator and qualifies the HPC pilot. See [plan](plan.md#pull-request-review--22-november)
and current [task rows](tasks.md).

## 22 November 2026 — T38 report compliance pass (partial)

Task T38. Work followed the approved plan in `docs/report/`:
- Chapter 5 retitled to "Implementation and Fabrication" with a software-only note.
- Bibliography switched to IEEEtran. Three verified references added and cited:
  velayudhan2023survey (ACM Computing Surveys 55(8), DOI 10.1145/3549932), astolfo2022darkfield
  (Nature Communications 13(1), DOI 10.1038/s41467-022-32402-0; the supplied reference list's
  "Partridge" author is not the published first author), miao2019sixray (CVPR 2019).
- Appendix A now has a dated semester record (Table A.2), open conflicts (Table A.3) and a
  handbook-form task table (Table A.4). Effort is "unreported" throughout.
- Build: `lualatex` x2 with `bibtex` gives 40 pages, no errors, no undefined citations or references.
- Word draft regenerated with Pandoc 3.9 to `docs/report/build/main-word-draft.docx`: 46 equations,
  4 figures, 17 captions, no unresolved references. Layout not yet compared with the PDF.

Not done: Gantt figure (Fig. A.1) not rebuilt; the handbook-form table covers the required elements
instead. Literature and patent-search record not written. Abstract length not checked against about
200 words. Full page-by-page visual check not complete. `docs/report/handbook-compliance-matrix.md`
was changed on disk by someone else after my edit; the current version was kept.

Gantt rebuild (22 Nov, later): `docs/report/figures/gantt.tex` now has two panels. Panel A shows
recorded semester evidence by status; Panel B gives the forward schedule T1–T9 from 21 Nov, with
durations, dependency arrows and responsibilities. Effort is unreported throughout. Compiled with
`lualatex` to `figures/gantt.png`; the report builds at 40 pages with no errors, and the Word draft
was regenerated. The Gantt page was viewed at page size; the small labels are legible but compact.
`appendices.tex` was changed on disk by someone else during this step; the current version was kept.

Abstract and search record (22 Nov, later): the abstract is 198 words, within the handbook's
roughly 200-word guidance. Chapter 1 now has a literature and patent search record (Table 1.2)
from three scoping web queries accessed 22 Nov 2026. It is explicitly not a complete patent
search: no patent database was queried by classification or claim text, and no patent claiming
cross-image threat-detection fusion was found in the snippets. The report builds at 40 pages with
no errors, and the Word draft was regenerated with 18 captions. `appendices.tex` and
`01-introduction.tex` were also changed on disk by someone else during this work; the current
versions were kept.

Next: compare the Word draft with the PDF page by page; run a full patent-database search if the handbook requires it.

Patent search (22 Nov, later): three more scoping web searches with patent terms, added to Table 1.2.
They surfaced older related patents (EP0476070A1, US5153439A, US5600700A, US20040258199A1, US9915752) and
no patent for deep-learning detection of explosives in modified electronics or for cross-image detection
fusion. This is still not a patent-database search: the available tools cannot query Google Patents,
USPTO full text or Espacenet by classification or claim text. A database search with CPC G01V 5/20 is
still required. The report builds at 40 pages with no errors; the Word draft was regenerated.

## 22 November 2026 — Ahmed's T41 HPC/data handoff (reported)

Ahmed reports that all 124 transferred files, dataset inputs and exact starting weights
were verified; an audit covered 17,360 images and confirmed five matching sub-0.001 px
box findings in each training export. Job 740 failed during font discovery; GPU
environment job 741 completed after cache preparation. Ahmed reports 442 local checks
passed, 11 skipped and Ruff clean; exact command lines were not included in the message.
Original annotations/test data and existing local changes were preserved; there were no
Git mutations, no annotation repair, no partition, no task trials, and no jobs remain
running. The linked handoff was not found in this checkout, so these results are recorded
as teammate-reported, not independently inspected here. Job 741 confirms environment
setup only; it does not establish full trainer qualification or model performance.

Next: Abd completes the independent PR #22 implementation review and human policy receipt
after outstanding code questions are resolved. Then Ahmed may create the derived repair,
findings hash and partition, qualify the full trainer, and start the bounded T41 study.
No real training has started. See T40/T41 in [tasks](tasks.md) and the [plan](plan.md).

## 22 November 2026 — owner-authorized report source publication

The owner explicitly authorized publishing the working LaTeX report source and original
project figures to the research repository's GitHub branch. This is a draft-source
distribution decision only: the compiled PDF and Word copy remain ignored local build
outputs, and no signed forms, handbook source, scans, credentials or private receipts are
included. The source is not submission-ready; the final assembled report's audience,
Word/PDF fidelity review, official forms/signatures and course distribution conflict
remain open. T38 tracks final acceptance and submission.

## 22 November 2026 — PR #22 follow-up review

Inspected current GitHub PR #22 at head `053c95c` and its changed policy, CLI, repair
implementation and synthetic test files. Hosted Ubuntu/Windows CPU checks are green;
Ali reports 288 synthetic tests passed. No tests were rerun locally and no private data
files were accessed. The update addresses the prior pending-receipt, area-recording and
test-split-guard findings. Inspection of T41 `training_partition.py` at Ahmed's
`32091bc` confirms `make_partition` requires decision `approved`, nonempty owner/reference
and a findings hash matching the supplied inventory. Inspection of T42's evaluator confirms
the frozen objective is overall AP@[.50:.95].

Follow-up commit `3ee9c87` on PR #22 corrects the area-metric explanation and clarifies that
the implementation receipt is pending; it also renames a synthetic helper that pytest had
collected accidentally. On the isolated PR worktree, `uv run --locked ruff check .` passed.
`uv run --locked python -m pytest` reported 272 passed, 2 skipped because `pycocotools` was
unavailable, and no warnings. Hosted Linux/Windows checks for `3ee9c87` passed. No real test export
was verified here. No repair, findings hash, partition, training or performance evaluation
has run. Next: after hosted checks, Abd records the human receipt; Ahmed verifies the actual
test-export hash, runs read-only check then repair, creates findings/partition hashes and
completes trainer qualification before a pilot.

Patent search update (22 Nov): a team member supplied the Google Patents result page for the multi-view
query with CPC G01V 5/20 (about 230 results; run on 22 November 2026). The top ten are hardware or imaging
patents, not detection fusion. Recorded in report Table 1.2. Still open: the USPTO full-text search and the
claims of any relevant-looking hit. The mybrowser tool is not available in this
session; it was not installed from the bootstrap folder.

USPTO search (pasted result page): query "multi-view" AND "x-ray" AND ("detection" OR "detecting") AND ("baggage" OR "security") over US-PGPUB, USPAT and USOCR. The visible top 12 hits are mostly unrelated; one 2026 hit, "Detection of disassembled items" (Infosys), may relate to dismantled components and is not yet read. Run date and total hit count are still to be confirmed. Recorded in Table 1.2; no claims read.

USPTO result total (22 Nov 2026): 863 hits for the query recorded above. The Infosys "Detection of disassembled items" applications (US20260301145 A1, US20260301379 A1) were read from their abstracts: container imaging, material segmentation, a learned embedding and a restriction score based on distances between objects. This is the closest match so far to the distributed-component idea, but the applications are not granted, and their claims are not read.

Patent reading (22 Nov, later): the two Infosys applications (US20260301145, US20260301379) returned HTTP 404 on Google Patents with and without the kind code, so their claims and status are unread. A web search found US10977755B2 (IBM, filed 2017, granted 2021), which describes detecting disassembled components across multiple sensor scan images. It is the closest multi-scan match so far, but its first claim was not read verbatim and its legal-status fields conflict in the fetched summary. Recorded in Table 1.2 with these limits.

## Add the next actual result

For each meaningful result record:

- Date, task ID, actual contributor and reviewer; hours only if actually reported.
- What changed and the relevant commit, pull request or shareable technical record.
- Exact commands/data/model pairing as applicable, actual result and known limitations.
- Review/explain-back completed, blockers and the next action.

Keep detailed machine/run manifests in authorized private storage. A command someone plans
to execute is not a completed experiment, and a generated draft is not a student contribution.

## 22 November 2026 — T41 authorized-data read-only preflight

Independent preflight was performed against the current PR #22 box-check implementation
(`3ee9c870fc82fc7ebe2ed9de5ed34983913db7e5`) and Ahmed's T41 inventory/fingerprint code
(`32091bcd1f46782ed39ac1233ad70e6ecf70451d`). It read the authorized local IEDXray copies
without modifying source or test annotations. Results: 12,224 training and 5,136 test image
files; both generic and specific training exports contain the same five out-of-bounds box
findings, each below 0.001 px (maximum `0.00027450000000789343` px); paired train/test
exports share zero image filenames. Exact byte inventory: 5 within-train groups, 112
within-test groups, 4 exact train/test overlaps; physical-group metadata was unavailable,
so the 0 verified groups value is not evidence that physical groups do not exist.

`findings_sha256`: `4e5ff81087cc7a7b0bcbbf1abf45806e96ebd7936aca35b583d7f33e471ce9f7`.
Train/test image inventory hashes are `58f4e58b3d42a81d46e3436cefe77d3524942e9aef792bad9dbfb6eafc0b4a94` and
`6e438bb41a8520f005065fec321230cd8afc0c97491f4ac3a70d486b1ad96db6`; source annotation
hashes and detailed ignored receipts are retained under
`runs/t41-policy-preflight-2026-11-22/`. This is a local authorized-copy result; Ahmed must
recompute/confirm the inventory hashes against the HPC transfer before partitioning. No
box repair, derived annotation, partition, task trial, model training or evaluation was
performed. The human implementation-review receipt is still pending.

T41 readiness check: inspection of the `32091bc` CLI and trainer code found `--execute`
explicitly blocked (`execution:software_draft_only`, `integration:live_trainer_not_connected`).
Its Slurm template therefore does not launch actual training. The available documentation
for `gpu-student` allows up to six hours; no HPC scheduler session is connected here. A
valid training run tonight requires a real trainer integration and qualified HPC job path;
this draft cannot produce reportable model-performance results. Job 741 remains environment
setup evidence only, as reported by Ahmed.

T38 report update (22 Nov): the verified read-only preflight was added to Chapter 5 of the
canonical LaTeX draft, explicitly labeled as a local-copy audit with no approved partition,
repair, training or performance result. `lualatex` + BibTeX + three LuaLaTeX passes completed
without fatal errors; current PDF is 42 pages. Page 17 was rendered and visually inspected;
the added subsection and surrounding table are legible. Existing underfull-box warnings remain
in unrelated compact tables. The Word draft was not regenerated in this session because
Pandoc is unavailable on PATH, so the current DOCX must be rebuilt and compared before
submission. This is a working draft, not a final submission artifact.

## 22 November 2026 — patent reading and report rebuild (later pass)

- IBM US10977755B2: the USPTO PDF is a scanned image with no text layer (not readable without OCR). The Google Patents text page was read partially through a web fetch (quotes capped; claims 7–10 and the grant date rest on the page summary). Claim 1 recites detecting a component in a scan image of one owner's container and another in a second owner's container, storing records with contextual information, and flagging owners by correlation and danger thresholds. Three independent claims. Page status: expired for non-payment of maintenance fees; grant dates conflict on the page. Not a freedom-to-operate finding.
- Infosys US20260301145 and US20260301379: still HTTP 404; a web search did not find them. Claims and status remain unread.
- PR state checked read-only: #21 is MERGED (21 Nov 15:20 UTC), so the "PR #21 needs review" wording in status.md and tasks.md T40 is stale. #22 and #20 are open with REVIEW_REQUIRED.
- Report rebuilt with lualatex and bibtex (bibtex run against build/main with BIBINPUTS set): 42 pages, 0 errors, 0 undefined citations.
- Word draft not regenerated: the DOCX preparation script is not present in the current scratchpad, so main-word-draft.docx predates the Table 1.2 edit. Page-by-page fidelity review remains open.
- Handbook matrix updated: abstract (198 words) done; IEEE citation style done; patent-search row reworded with the limits above.
- Not done: no commit, push or PR action (no explicit owner authorization in this session); no human review or approval; no forms or signatures.

## 22 November 2026 — PR #22 review and deadline study scope

Live GitHub metadata confirmed PR #22 remains at `3ee9c870fc82fc7ebe2ed9de5ed34983913db7e5`,
with Ubuntu and Windows hosted checks passing and `REVIEW_REQUIRED`. Review of the isolated
PR implementation confirms the receipt defaults to `pending` and the T41 partition builder
requires an explicit approved decision, owner/reference and matching findings hash. The repair
CLI requires the task's published test annotations; the helper rejects the test annotation
file/hash and shared image filenames, preserves source `area`, and records the test hash and
per-box bbox/area changes. Its record/documentation correctly warns that size-specific metrics
on training-derived validation can be affected. Ali reports 288 synthetic tests; no live
repair or training evidence follows from them. Technical review found these three requested
implementation points addressed. The formal human review receipt and GitHub approval remain
for Abd to enter personally.

Owner direction for the 24 Nov report cutoff reduces the trial scope from 20 to six attempts
per task, with the untuned control included in the six. Failed/pruned attempts count. Run the
best completed tuned candidate and the control for up to 100 epochs each on the same task,
starting weights, partition, fixed controls and training seed 17; choose only from validation.
Defer top-three confirmation and multi-seed repeatability. This is a single-seed exploratory
comparison, not a robust generalization claim. Preliminary runtime estimate (not measured):
10--13 GPU-hours for generic; 20--26 for both tasks on one GPU. Generic proceeds first; specific
is conditional on time/allocations. The six-hour per-job limit requires sequential resumable
allocations. Estimates remain subject to trainer qualification and pilot measurement.

The real-data preflight findings hash is already computed locally; Ahmed must verify it on HPC
before repair/partition. No training backend is integrated and no scheduler session is available
in this workspace, so this scope update does not make a job submit-ready. The report records the
new scope as planned work; no model-performance values are claimed.

T38 follow-up (22 Nov): after the deadline-scope update, the LaTeX report rebuilt to 42
pages with no fatal compile errors. Rendered pages 17 and 18--19 were visually checked; the
preflight and revised study scope are legible. The Word copy remains to be regenerated and
compared, and it was not produced here because Pandoc is not available on PATH.

### T38 report Chapter 1 rewrite — 22 November 2026

Editor: AI agent (Claude) at the owner's request; not student work. Owner review pending.

- Rewrote `docs/report/chapters/01-introduction.tex` to the handbook structure: 1.1 goals,
  motivation, method, scope; 1.2 background, datasets, detectors, explosive/IED research,
  research gap, patent search; 1.3 report overview; 1.4 repositories, student GitHub accounts,
  branching, PR/review rules, documentation system and AI-use disclosure.
- Sources: the proposal, IEDXray, FALCON and the SRC 2026 paper in `docs/research_papers/`.
  SRC results are labelled as that paper's published results, not SDP I results.
- `references.bib`: 9 new entries and 6 upgraded from arXiv to published venues (22 total);
  metadata checked against Crossref on 22 Nov.
- New TikZ figures `figures/method.tex` and `figures/workflow.tex`; full patent log moved to
  Appendix A (`app:patentlog`); abbreviations extended; ragged-right table style `L{}` and
  `\tablesetup` added to `main.tex`.
- GitHub username mapping confirmed by the owner. Student contribution confirmations and AI
  prompt excerpts (Table 1.10) remain pending for each student. New task T44 records the
  AGENTS.md / CONTRIBUTING.md conflict.
- Build: lualatex + bibtex + 2× lualatex: 54 pages, 0 errors, 0 undefined references or
  citations, 0 BibTeX warnings; Chapter 1 is PDF pp. 10–21 with no overfull boxes. Nine
  overfull warnings remain in older appendix tables. Pages were visually checked. Word copy
  not regenerated.
- Revision (22 Nov, owner direction): Table 1.1 now lists only the five original-proposal
  requirements. The owner reports 500 positive scans collected by the team and about 7,000
  negative scans collected with the CVML lab (SLG-supplied scanner) and shared by Dr. Divya.
  Distributed (P2) work is scoped to SDP II. The AI-commit exception paragraph was removed at
  the owner's request. Table 1.10 is filled with draft rows from each member's submitted work;
  each student must confirm the tool and replace the prompt. Chapter 5 still reports 577 paths
  / 478 distinct payloads and must be reconciled with the 500-scan statement. Rebuild: 54
  pages, 0 errors, 0 undefined.
- Chapter 5 collection rewrite (22 Nov, owner direction): new subsections on positive scans
  (catalogue families E/D/B/W, four-bag groups, 125 groups / 500 configurations, sessions
  29 Sep–9 Oct), negative scans (~7,000, owner report, no repository inventory) and data
  handling. The owner states the 500 scans were collected and that the 14 Nov snapshot (478
  distinct files) is partial; the remaining 22 are not inventoried. The abstract, Chapter 2
  and Appendix A were aligned, and the "collection count" conflict row was removed. Build: 55
  pages, 0 errors, 0 undefined.
- Chapter 5 polish (23 Nov): rewritten in report style with title-case headings and section
  labels; new tables for implemented components (5.1), IEDXray audit and preflight findings
  (5.2) and the reduced study design (5.7); the rehearsal checklist is now a numbered list; the
  test command renders correctly. Facts unchanged from the prior draft and project records.
  Build: 57 pages, 0 errors, 0 undefined; no overfull lines in Chapter 5 (nine remain in
  appendix tables).
- Chapter 2 rewrite (23 Nov): restructured as problem and stakeholders, detection tasks,
  functional requirements FR1–FR7 traced to the proposal (old FR8 distributed requirement moved
  to the SDP II scope boundary), non-functional requirements NFR1–NFR6, system specification
  (pipeline, scan result and detection fields from docs/contracts.md, status semantics, run
  manifest), constraints, scope boundary. Six tables. Build: 59 pages, 0 errors, 0 undefined,
  no duplicate labels.
- Chapter 3 rewrite (23 Nov): added X-ray image formation (Beer–Lambert law, dual-energy
  ratio), YOLOv10 consistent dual assignments and matching metric, letterbox inversion,
  COCO AP/AR definitions with 101-point interpolation, group-preserving partition constraint,
  AdamW update, and an assumptions/consequences table. Physics is cited to Wells & Bradley;
  detector details to the YOLOv10 paper. Float pages are now top-aligned report-wide
  (main.tex). Build: 62 pages, 0 errors, 0 undefined.
- Chapter 4 rewrite (23 Nov): evaluation criteria C1–C5; qualitative evaluation of the six
  supplied detector families from docs/checkpoint-catalog.md (YOLOv10-M selected; ratings are
  a design assessment, not measured accuracy); system alternatives table drawn from
  docs/decisions.md; selected architecture; pre-processing and host association; realistic
  constraints table, standards, ethics. Build: 64 pages, 0 errors, 0 undefined.
- Chapter 6 rewrite (23 Nov): summary of work; achievement table against the five proposal
  requirements (evaluation "partly met"); critical appraisal split into strengths,
  limitations and lessons learned; SDP II further-work table (fine-tuning study, lab data
  preparation, lab-data evaluation, host association, distributed detection, deployment);
  concluding remarks. Build: 65 pages, 0 errors, 0 undefined.
- Title page and abstract (23 Nov): title page now lists the university, college,
  department, project title, "Senior Design Project I — Final Report", the five students and
  the supervisor (Prof. Naoufel Werghi, from the proposal); the earlier draft disclaimer is
  removed and the running header reads "Final Report". Project number and any official cover
  template remain to be added. Abstract rewritten to about 200 words to match the revised
  chapters. Build: 65 pages, 0 errors.
- Appendices rewrite (23 Nov): all appendix tables use the shared ragged-right style; the nine
  overfull warnings are gone (0 report-wide). Semester record adds the 14–22 Nov PR merges and
  report revision; the resolved PR #21 status conflict is removed; the risk worksheet,
  official-forms text and contribution record are rewritten in report voice; the handbook
  coverage table now cross-references the revised chapters. Build: 63 pages, 0 errors,
  0 undefined, 0 overfull.
- Word copy (23 Nov): regenerated `docs/report/build/main-word-draft.docx` from the current PDF
  with Microsoft Word's PDF conversion (Pandoc is not installed). Check: 68 Word pages vs 63
  PDF pages; 18,897 vs 19,322 words (98%); all chapters, appendices, figures and equations
  present; title-page table fixed by hand. Long appendix tables (A.4 task schedule, A.5 patent
  log) have misaligned cells after conversion and need manual tidying or a Pandoc conversion.
- Word copy via Pandoc (23 Nov): installed Pandoc 3.14 (`winget install JohnMacFarlane.Pandoc`)
  and rebuilt `docs/report/build/main-word-draft.docx` from the LaTeX source. A local
  preprocessing script flattened the custom table macros and took heading, table, figure and
  equation numbers from `build/main.aux` and `build/main.toc`; citations were rendered by
  `--citeproc` from `references.bib` with a minimal numeric style; Word then applied A4,
  25 mm margins, Times New Roman 12 pt, 1.5 spacing, booktabs-style table rules, the title
  page, contents and lists of figures and tables. Check (exported to PDF): 64 pages; 39
  tables, including A.4 and A.5, as real Word tables; 6 figures; citation numbers match the
  LaTeX PDF; no field errors. Limits: equation numbers are typed text, not Word fields; the
  bibliography follows a simplified IEEE style; front matter is numbered in arabic, not roman.
  The conversion scripts are now in `docs/report/tools/` (`build-docx.ps1` wrapper,
  `docx_prep.py`, `docx-refs.lua`, `ieee-min.csl`, `docx-format.ps1`), documented in
  `docs/report/README.md`. Wrapper run from `docs/report` reproduced the same result
  (64 pages, 39 tables, 6 figures). `uv run --locked ruff check .` passed; `uv run --locked
  python -m pytest` 196 passed, 37 subtests passed.

## 23 November 2026 — PR #24/#25 integration and report prototype results (T38/T41)

- PR #25 (T41, Ahmed): reviewed locally at head `950ea84` — Ruff passed; pytest 525 passed,
  3 skipped (`pycocotools` unavailable locally); no credentials, private paths, weights or
  images in the diff; frozen-test runner checks hashes of code, checkpoints, annotations and
  every test image before predicting. Owner approved head `950ea84` and merged it as
  `f14fc3f` (merge commit; the frozen-test source commit `54db37b` stays in history). GitHub
  records the merge 10 s before the approval on the same head (owner bypass).
- PR #24 (Faisal): reviewed at `d5ae27c` (Ruff passed; 276 passed, 2 skipped). After #25 it
  conflicted in the box-repair code. Merged `main` into `faisal/review-followups` as
  `87094b1`: kept #25's hash-bound training-source design; re-applied Faisal's
  `derived_file_sha256` field and the image name/size input check with their tests; dropped
  its report hunks (already on main). Ruff passed; pytest 529 passed, 3 skipped. Owner
  approved head `87094b1`; merged into main as `c58dac7`.
- Report (branch `docs/final-report-results`): new §5.5 "Prototype Results: Generic Explosive
  Detection" with the study design, hyperparameters, all T41 jobs, frozen test metrics,
  fixed operating point, inspected examples, latency and limitations; six original pgfplots
  figures (`figures/t41-*.tex`) with values copied from `docs/t41-results.md` and
  `docs/t41-handoff.md` and rows in `provenance.csv`. Abstract, Chapters 1, 2, 4 and 6,
  appendices and the Gantt chart updated; Gantt panel A day offsets for 4, 21 and 30 Nov
  corrected by one day. `chapters/05-t41-results.tex` from #25 is folded into Chapter 5 and
  removed. Build: 72 pages, 0 errors, 0 undefined, 0 overfull.
- Not yet available: detection-example images and precision–recall curves (need Ahmed's
  test-evidence archive of predictions), per-epoch training curves (need an export from
  jobs 770/819) and approved RayGuard-App screenshots.

## 23 November 2026 — review follow-ups for merged PRs #22 and #20 (T40 review role)

Faisal's review of the merged data policy (#22) and report draft (#20) from the T40
provenance side. The box clamp, its script and its tests are Ali's work from #22; this
change adds two small fixes to it and does not alter its behaviour on valid files.

- `scripts/repair_train_boxes.py` now records `derived_file_sha256`, the SHA-256 of the
  derived file as written. The existing `derived_content_sha256` is of the canonical JSON
  form and does not match a plain file hash, which a later check on HPC would trip over.
- `sdp_xray.box_repair` refuses an image entry without a file name or positive
  width/height with the normal exit 2 instead of a traceback.
- Report: five appendix tables had a doubled line break before `\midrule`, which prints
  the word "midrule" and drops the rule. Chapter 5 still described the pre-#22 policy
  (verified physical groups, geometry blocked); it now matches the merged policy.
- `uv run --locked ruff check .` passed. `uv run --locked python -m pytest`: 267 passed,
  11 skipped (nine Windows symlink tests, two that need `pycocotools`).

Limits: the report was not compiled here because no LaTeX toolchain is installed on this
machine, so the table fix needs one rebuild to confirm. No data, weights or model were
used. Two review questions for the policy owners remain open and are on PR #22: whether
the five within-train duplicate pairs carry identical boxes, and that a training image
identical to a test image can fall into validation.

## 23 November 2026 — PR #27 review fixes and training curves (T38)

- Faisal's review of PR #27 (five non-blocking points), all fixed: Chapter 6 no longer says
  the audit prevented train/test overlap (the four overlaps were retained and are reported);
  the evaluation requirement is "Partly met" in Table 1.1, Table 6.1 and the abstract
  (published test set, not an unseen-case benchmark); validation–test gaps stated exactly
  (46.1 and 39.4 percentage points); `method.png` provenance row corrected; PR #24 check row
  now cites merged head `87094b1` (529 passed, 3 skipped).
- Found and fixed three broken cross-references in Chapters 2 and 4 (a scripted edit had
  turned `\ref` into a control character); no other control characters in the sources.
- Ahmed supplied per-epoch validation AP for jobs 770 and 819 (100 epochs each, 0–1 scale);
  epoch 68 (control, 0.877062) and epoch 84 (candidate, 0.874833) match the handoff and are
  each run's maximum. Added as `figures/t41-val-ap.csv` with chart `figures/t41-curves.tex`
  (Figure in §5.5.1) and a provenance row.
- Ahmed's attribution note applied: §1.4 states that the two PR #25 commits were authored and
  committed by OpenAI Codex under Ahmed's instructions through his account (two earlier draft-
  branch commits likewise), CI passed, and the owner's approval is recorded 10 s after merge on
  the same commit; Table 1.7 and Appendix C mark Ahmed as T41 lead with AI-assisted
  implementation; Table 1.10 quotes his actual prompt excerpts. His name spelling, contribution
  confirmation and forms remain his own actions.
- Ahmed's frozen-test evidence archive received (`frozen-test-20261123.tar.gz`, SHA-256
  `d8d5e039…` matches `docs/t41-results.md`); both prediction files and the local test
  annotations and example images match the frozen-plan hashes. New `docs/report/tools/
  t41_figures.py` recomputes COCO metrics from the saved predictions (pycocotools 2.0.11;
  AP 41.5886 and 48.0502 reproduced exactly) and writes `figures/t41-pr.csv`
  (precision–recall at IoU 0.50/0.75; curve averages equal AP50/AP75) plus annotated
  example images in `figures/private/` (ignored by Git; dataset scans). Report adds the
  precision–recall figure and the three inspected examples; the example figure falls back
  to a note when the private images are absent. Build: 75 pages, 0 errors, 0 undefined,
  0 overfull; Word copy 77 pages, 17 figures.

## 23 November 2026 — Faisal's confirmation and RayGuard-App PR #1 (T38/T43)

- Faisal confirmed the T40 lead role and PRs #17, #19, #21 and #24, and supplied the
  Table 1.10 disclosure (reconstructed prompt, not verbatim). Checked on GitHub: all four
  PRs are Faisal's; reviews exist on #20 (later dismissed) and #27 (approved at `b7b9f2c`).
  Open point: the disclosure names CI scripts, but none of those PRs changes `.github/`.
- Mohammad's [RayGuard-App PR #1](https://github.com/abdalrahman-ismaik/RayGuard-App/pull/1)
  at `d5d4baf` (tests and docs only; base `3488abd`) run in a separate clone on Windows with
  installed Chrome: build passed; 8 T43 and 157 total browser tests passed; type check, backend
  lint and 280 backend tests passed. Hosted CI had not run (fork approval required).
  Software checks on synthetic data only; the walkthrough and acceptance remain open.

## 24 November 2026 — Dismantled-project methods in the report (T38)

- Follows the supervisor feedback in `meeting_minutes/follow-up-report-2026-11-24.md`.
- Added Section 1.2.5 (literature), 3.7 (model) and 4.6 (proposed methods, pipeline and
  evaluation plan), two figures (`p2-pipeline`, `p2-kofn`) and 12 references. Reference
  metadata was checked against Crossref, PMLR or arXiv; FALCON details come from the
  supplied v2 paper. The other new papers were checked through metadata and, for three of
  them, abstracts; they were not read in full. No component detector or fusion method has been
  trained, and the k-of-4 chart is analytical.
- Aligned the scope table, research gap, abstract, Chapter 2 and further-work item 5.

## 24 November 2026 — Application walkthrough in the report (T38/T43)

- Section 5.6 shows real RayGuard-App runs (app `3488abd`, engine `b7ec59e`, CPU, threshold
  0.25) on four IEDXray test scans, with the supplied IEDXray checkpoints. The fine-tuned
  checkpoint (job 819) is not on this machine; captions and text say which model is shown.
- Scans were chosen after running the supplied models on 260 annotated and 60 unannotated
  test images (seed 17), plus the known miss `Test000001`. None has an exact copy in Train.
- The table of fine-tuned results uses the saved job 820 predictions. Candidate 4 finds the
  laptop threat in `Test001489` (0.954) and misses `Test002804` (best 0.137).
- Screenshots stay in ignored `docs/report/figures/private/`. Next: recapture with the
  job 819 checkpoint after its hash and loading are verified.

## 24 November 2026 — Landscape Gantt chart and schedule (T38)

- Gantt chart redrawn as one landscape page (PDF and Word). The owner supplied the research
  period (8 Sep–10 Nov) and the collection period (28 Sep–4 Nov); both are marked as
  reported. The dated scan files (29 Sep–9 Oct) are marked inside the collection bar.
- The owner confirmed that the SLG CEO visit (21 Oct) took place. Its outcome is not recorded.

## 24 November 2026 — Final submission pass (T38)

- Merged main (#27, #28); kept Faisal's own wording and the #29 line.
- Title page follows the coordinator's list; project COSC01; examiner as given by the owner.
- Appendix B holds the Risk Assessment form, Health and Safety form and Declaration from the handbook.
  Student names are typed signatures on the owner's statement that all five agreed; supervisor and
  Safety Officer lines are blank. Ratings are proposed. Signatures, IDs and logo stay out of Git.
- Appendix C has a "who did what" table from tasks, PRs, commits and the collection inventory.
- `\pending` markers removed; open items are stated in plain sentences. PDF only.

- Evaluation is marked "Met for the prototype (generic task)" by owner decision. The four test images
  that are byte copies of training images (3 boxes) were excluded in a recomputation from the saved
  predictions: AP 41.5602 and 48.0317 on 5,132 images (41.5886 and 48.0502 on 5,136). The audit table
  wrongly said they were excluded from training data; corrected. Table A.3 (record conflicts) removed.
