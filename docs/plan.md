# Current plan - Meeting 02 and follow-up

Updated **22 November 2026 (Asia/Dubai)**. Source precedence and exact action IDs are in the
[meeting index](meeting_minutes/README.md). [Tasks](tasks.md) holds status; this page sequences
the work without assigning availability or claiming completion.

## Pull request review — 22 November

**PR #22 — merged into main at `3ee9c87` (22 Nov) after a recorded approval.** The data-policy helper had
passed hosted Linux/Windows CPU checks; Ali reports 288 synthetic tests passed. The
policy direction is agreed: preserve the published test set, use the shared seed-17 ~80/20
partition, keep exact duplicate training images together, and mark validation exploratory
without verified physical groups. Ahmed reports an audit of 17,360 images; independent local
read-only checks confirmed 12,224 train/5,136 test images and the five matching sub-0.001 px
findings in each training export (maximum overshoot `0.00027450000000789343` px). There are
no shared train/test filenames, 5 within-train and 112 within-test exact-byte groups, 4 exact
train/test overlaps, and no verified physical-group records. Findings SHA-256 is
`4e5ff81087cc7a7b0bcbbf1abf45806e96ebd7936aca35b583d7f33e471ce9f7`; ignored receipts are
in `runs/t41-policy-preflight-2026-11-22/`. Ahmed must reproduce/confirm these hashes on HPC.
No repair or partition has run.

The latest code addresses the earlier findings: the receipt example is `pending`; T41's
`make_partition` requires approved decision plus owner/reference and a matching findings
hash; the repair record retains original COCO `area` and logs the bbox-implied change; and
the repair guard hashes the supplied test export and refuses shared image names. Independent
inspection confirms the T42 objective reports overall AP@[.50:.95]; COCOeval's area-specific
metrics can still be affected for a validation subset derived from the repaired training
copy. Commit `3ee9c87` corrects the policy wording and clarifies that Abd's policy message
was not the implementation receipt. The exact real test file/hash must still be verified
by Ahmed's run; a CLI argument alone does not establish provenance. In the isolated PR
worktree, Ruff passed and pytest reported 272 passed / 2 skipped because `pycocotools` was
unavailable, with no warnings. Hosted checks for `3ee9c87` passed. The findings hash is computed; the human receipt, approved partition, real trainer
connection/qualification and pilot remain outstanding.

Ahmed reports transferred inputs and starting weights verified, and GPU environment job 741
passed after job 740's font-discovery failure. This is environment evidence, not full
trainer qualification. After the human receipt is independently recorded, Ahmed should confirm the same findings
hash on HPC, run the approved check and training-only repair, create the hash-bound partition,
then connect and qualify the real trainer/evaluator.

**PR #20 — semester/progress/documentation update.** Merged at head `7fe234f` (70 files) by the
owner with no recorded approval. Its content, including the agent-merge rule in `AGENTS.md`
(`8723b0d`), still needs independent teammate review. Hosted Linux/Windows checks passed on
main at `6948559`. PR #21 is merged as `29d6d0f`; #18 is merged as `9350482`.

The open pilot gates remain human approval of the reviewed policy receipt; Ahmed's confirmation
that the HPC inventory matches the local findings hash; check/repair records and partition;
trainer/evaluator connection; transfer/head-handling receipt; and full trainer qualification.
No real training or model-performance evaluation is verified. The current Slurm template invokes
a planning CLI that refuses live execution, so submitting it now would not train. The documented
`gpu-student` allocation is capped at six hours; an all-night single job exceeds that limit.

## Latest team integration review — 21 November

**Completed re-review, 21 Nov 14:34 UTC:** PR #18 was updated with main to `6edcd68`,
tested and merged as `9350482`. Both review threads resolved; description updated.
Ruff passed, evaluation-enabled pytest passed **273 tests**, and required Linux/Windows
CI passed. This supersedes PR #18 re-review requirements in earlier snapshots below.
T42 evaluator software is integrated; real metrics and full task completion remain open.
Ahmed can consume it from current main. Small blocking adapter changes may be completed
by any available teammate, with assigned work first and collision coordination.

### Data policy handoff for the pilot

Use these conservative implementation defaults; they do not certify real artifacts:
preserve published test files and annotations exactly, report all known test/train
byte overlaps, and make no independent-test claim for them. Fit/validation come only
from published training images, share one hashed ID assignment across both tasks,
and keep connected exact-byte duplicates plus verified physical groups together.
Never infer groups from names. If physical groups remain unavailable, label any
reviewed byte-group-only experiment exploratory with unverified physical independence.
Keep annotation-empty images; never label them benign from absent annotations.
Invalid/nonpositive/nonfinite/out-of-bounds training geometry blocks the live pilot
under the present software; no silent clipping, removal or relabeling. Ahmed/Ali
or an available teammate must bind the actual findings, dispositions and partition
hash in the existing policy receipt; any derived repair needs explicit review and
separate provenance. Report reproduction with original test annotations separately
from controlled-study validation. These decisions permit software integration now;
actual data clearance, authentic reviewer receipts and HPC qualification remain gates.

**Owner amendment — shared execution:** focus on assigned work first; an available student may complete a small
unfinished dependency, including another lane's evaluator, receipt, trainer or report.
Names here identify contacts/current contributions, not exclusive rights or mandatory
approvers. Record scope/editor, notify affected teammates and proceed in isolation;
no reply is required to start non-overlapping work. Coordinate active edit/compute
collisions. Use an available qualified reviewer while preserving independent review
and protected-branch permissions. Credit actual work. This supersedes older personal
file exclusions and named-person handoff gates; data/qualification gates still apply.

This review supersedes stale "not started" software descriptions below. Evidence:
GitHub branch/PR metadata and selected source inspected; teammate execution reports
are attributed reports, not locally repeated checks. No new real training/evaluation
or HPC qualification was executed. Backlog state and ownership stay in [tasks](tasks.md).

| Work | Inspected state | Next handoff |
|---|---|---|
| Faisal T40 | Baseline/contracts/tools merged in PRs #17/#19. [PR #21](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/pull/21), head `b325c28`, supplies initialization provenance and receipt helper; both hosted CPU platforms pass, review required. | Ahmed reviews receipt; Ali reviews common-parent semantics; Abd performs human PR review. Rehash the permitted file on HPC before use. |
| Ahmed T41 | [Draft `32091bc`](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/tree/32091bcd1f46782ed39ac1233ad70e6ecf70451d) on `ahmed/t41-software-draft`: partition/provenance/preflight, synthetic study orchestration and Slurm template. CLIs explicitly block live execution. No open PR found at inspection. | Ahmed opens PR **to `main`** for software review; reconcile overlapping planning docs with PR #20. Implement real trainer/validation connections only after interface/data/environment gates. |
| Ali T42 | [PR #18](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/pull/18), head `6dfa7d6`: both safeguards, validation objective and common-parent comparison implemented; hosted CPU checks pass, earlier review still changes-requested. | Human re-review; connect trainer using objective() and actual file-hash provenance; agree data policy and qualify pilot. Specific-task end-to-end behavior still needs verification. |
| Mohammad T43 | Research branch `mohammad/guiflow`, `164d6cf`, records an assisted GUI acceptance slice and reported checks in the separate app. The branch changes only research task/progress docs. | Supply app commit/diff and human walkthrough evidence for Abd's review; verify app work is actually shared. No open app PR found; that does not establish whether local work is complete. |
| Abd T38/T39 | Report specification and guidance are local reviewed-work candidates; PR #20 remains behind/review required despite passing hosted CPU checks. Current app implementation was not requalified here. | Review integration, reconcile docs, preserve existing edits, coordinate report and demo evidence. All GitHub reviews/merges remain human actions. |

### Dependency order and decisions to close

**Ali update, later 21 November:** source inspected at PR #18 head `6dfa7d6`.
The safeguards and common-parent comparison requested below are now implemented;
retain the requirements as acceptance criteria, not outstanding implementation tasks.
Use `from sdp_xray.validation_objective import objective, evaluate_validation` and
set the training configuration's `objective` to `objective()`. The function accepts
request, validation-only COCO ground truth, supplied ground-truth/checkpoint hashes
and original-pixel COCO xywh detections; returns matching identities, evaluated IDs
and AP on 0–1 scale. Failures raise `ValueError`, never zero AP. It pins pycocotools
2.0.11. Ahmed's adapter must hash actual files and bind predictions to the checkpoint;
the evaluator compares caller-provided hashes and echoes the partition hash, not
independently verifying weights or partition membership. Validation image coverage
and source partition remain trainer/preflight responsibilities. Reported compatibility
with Ahmed's validator is synthetic, not locally repeated here. Next dependencies:
human PR re-review, config/adapter integration, reviewed data policy and qualified pilot.
The PR description still describes the original scope and should be updated by its
human author to include the interface and candidate/candidate mode.

1. **Review targets:** student PRs for shared ML/software/documentation target `main`;
   GUI implementation targets RayGuard-App. Review #21 and updated #18 independently;
   Ahmed's PR may be reviewed as a blocked software draft before live dependencies are
   merged. Do not silently overwrite coordinator protocol with branch-local drafts.
   Human reviewer reconciles #20/T41 `docs/finetuning.md` and `docs/hpc-training.md`,
   preserving both the agreed protocol and Ahmed's actual implementation history.
   After accepted increments, humans sync shared fixes into both prototype branches;
   app engine pin advances only with app integration checks.
2. **Initialization:** PR #21 documents official THU-MIG/yolov10 `v1.1` `yolov10m.pt`,
   66,924,323 bytes, SHA-256
   `ff2c559f11d13701abc4e0345f82851d146ecfe7035efaafcc08475cfd8b5f2d`.
   Its documentary/timing/embedded-COCO evidence supports exclusion of IEDXray but is
   not proof of training contents. This review inspected Faisal's record/code, not
   the weight bytes or upstream sources independently. Faisal/Ahmed transfer through
   an approved channel and rehash on HPC. Agree receipt fields, task identity and
   model IDs; both U/T records use role `candidate` with the same initialization
   parent hash, never one another's output as parent. Keep actual output hashes distinct.
3. **Ali's immediate interface:** review Ahmed's existing `validation_request` and
   `validate_objective_result` in `src/sdp_xray/tuning.py` at `32091bc`. Request binds
   checkpoint hash, completed epoch, task, partition hash, annotation hash, validation
   IDs and objective. Result supplies status, matching identities/objective, exact
   evaluated image IDs and finite AP@[.50:.95] in **0–1**. Freeze evaluator version,
   settings and ID inside the objective metadata. Use training-derived validation
   only; keep final test evaluation separate. Agree failure, callback and checkpoint
   selection behavior; test wrong hash/task/IDs, nonfinite values and evaluator failure.
4. **Matched comparison:** Ali keeps supplied-checkpoint reproduction separate from
   controlled U/T comparison. Add a mode accepting two candidate records with equal
   parent/task/class maps, split and inference settings, and clean identical inference
   code identity. Link separate training receipts to the same partition, initialization
   procedure and paired seeds/budget; shared parent hash alone is insufficient. Preserve
   the existing baseline/candidate mode. Ahmed's current initialization validator fixes
   seed 17; agree how head initialization and repeat seeds 17/29/43 are represented
   before repeat runs, rather than assuming all seed receipts already interoperate.
5. **Data policy — Ali and Ahmed draft, Abd coordinates review:** retain published test
   files/annotations unchanged; group exact training duplicates transitively with any
   verified physical groups in one training-derived partition shared by both tasks.
   Record published-test overlap and limit independence claims. Missing physical groups
   requires an explicitly reviewed exploratory fallback, never filename inference.
   Invalid geometry stays blocked in the current draft; any repair needs separate
   reviewed derived-data implementation, source/affected-ID hashes and rationale.
   These are recommendations to approve and bind to findings hashes, not new approvals.
6. **Live integration and pilot:** Ahmed connects the qualified real trainer to Ali's
   evaluator; Faisal checks provenance/run handoff. One owner/job/output directory,
   pinned isolated environment, full verified local weights path, explicit seed and
   `amp: False` for initial FP32 qualification. Prevent runtime package/weight downloads.
   Keep the upstream transfer log to verify task-head handling. Forward/backward/save/
   reload and a bounded pilot must pass; record hardware, actual device, dependency
   inventory, hashes, command, errors and measured runtime before estimating search cost.
7. **Research/report cutoff:** retain generic-first then specific 20-attempt studies as
   the agreed research scope, not a guarantee before 24 Nov. Schedule only after measured
   pilot/quotas and accepted compute budget. On 23 Nov freeze report content for review;
   include only verified results available then. If blocked, document implemented
   software, synthetic checks, precise blockers and the unfinished experiments. Missing
   new metrics must not delay the 24 Nov 17:00 submission. The 30 Nov collection deadline
   and full P1/P2 obligations remain separately tracked.

Each student supplies a concise report-ready method/evidence/limitations paragraph,
real commit/PR links, actual checks and personal contribution statement. Follow the
[handbook report specification](final-report-requirements.md), including sources,
figures, Gantt plan-versus-actuals and applicable forms. No invented dates/hours or
metric values. These instructions allocate next handoffs; new availability is unconfirmed.

## Report delivery sequence agreed 21 November

Follow the [report specification](final-report-requirements.md) and T38 as the immediate
delivery priority. **21 Nov:** coordinator/report editor and students confirm ownership,
map handbook requirements to evidence, inspect official templates/forms, verify source
metadata and establish the LaTeX-to-Word conversion path. **22 Nov:** assemble the six
SDP I chapters, bibliography, purposeful visuals, Gantt chart and applicable forms;
distinguish actual work from planned experiments. **23 Nov:** complete group/supervisor
review as available, contribution verification, reference/visual provenance checks and
page-by-page PDF/Word inspection. **24 Nov:** resolve submission gates and submit before
**17:00 UTC+4**, preserving the same content for permitted distribution and private
receipts. These are planned milestones, not accepted student assignments or completion.
Required human signatures, format acceptance and confidentiality/publication decisions
remain explicit dependencies. Report from verified evidence; retain unfinished ML/P2
work and the 30 Nov collection obligation without promising new results before submission.

## Current end-of-semester implementation phase — 14 November

The proposed, not-yet-accepted work packages T39–T43 and the 14–27 November schedule are in
the [implementation/demo plan](implementation-plan-demo-2026-11.md). Abd and Mohammad lead
GUI polish; they also review ML integration. Faisal owns the baseline/run contract, Ahmed
fine-tuning, and Ali evaluation. The [ML pipeline plan](single-scan-ml-pipeline-plan-2026-11.md)
prioritizes the GUI-selected CVMI model and public IEDXray data after exact artifact verification.
Dismantled collection scans count toward collection progress, not this single-scan data path.
Every student personally commits and pushes under their own identity; agents only advise or
draft. Confirm each student, reviewer, model/demo pairing and presentation slot before code work starts.
The earlier sections below preserve historical meeting/planning context; their October dates are not silently reset.

## Latest collection sequence — F06

The [19 October source update](meeting_minutes/follow-up-collection-2026-10-19.md) sets
**30 November 2026** as overall collection completion and requests the second-round schedule.
Gather each student's first-round count against 500; reconcile Faisal's reported 102 with
his formula's 104 and C01's planned 100. Complete any shortfall using the same set before
moving to the next round. No accepted team total or QC evidence is available.

Gather current availability and exact post-midterm dates, retain M02's two-week round pending
amendment, and propose around **5 pm** where feasible; late attendance is optional. Obtain
lab acceptance and record sending of the schedule. No new dates or availability are supplied.
The earlier rota and 15 October Batch 1 milestone below are historical, with acceptance and
completion unverified. F06 does not expressly replace that milestone or other deadlines.
C01 Session A/B both belong to Round 1, distinct from the pre-/post-midterm rounds.

## Historical conference and showcase records

6G MENA participation is complete as an event; the owner reports that the project team
attended on 20 October 2026. Individual attendance, actual presentation, final revised poster
and TDRA approval remain unverified. Preserve the requirements and artifacts in the
[historical dossier](6g-mena-2026.md). Current paper calls are tracked separately in the
[conference register](conferences-2026-2027.md).

## Secure Life Group visit - F08

[F08](meeting_minutes/follow-up-slg-2026-10-19.md) confirms **Wednesday 21 October, 2-5 pm**,
with required presence. T37 covers the SDP digital poster on project/progress and coordination
of Divya's lab preparation and Hardik/Fangzhou's high-quality work/approaches video. Name
the SDP poster editor/presenter and review an accurate progress summary before the visit;
confirm display/file requirements and any earlier handoff cutoff. Rehearse the existing GUI
under T28, retaining its verified scope and failure/empty states. No new artifact or readiness
is established by the invitation. Tuesday's 6G session and Wednesday's visit are consecutive
events; prepare for both and do not automatically transfer 6G's display specification to SLG.
The separate summit-video deadline remains unknown; the visit video must be ready for 21 Oct.

## Earlier workstreams and capacity

**Primary technical work:** all five SDP students collect the distributed dismantled dataset,
then adapt the available model for multi-package evidence. Hardik owns a separate colorization
workstream. P1/P2 modules and branches remain useful implementation boundaries; student model,
GUI and integration assignments need confirmation.

**Near-term showcase:** simple laptop GUI and poster on **Embedded Explosive Detection in
Electronic Devices**, required for the SLG visit now dated 21 Oct (F08). This is separate from completed P1
requirements and a trained multi-package system. The [local GUI draft](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md)
integrates the verified IEDXray generic YOLOv10-M baseline. Confirm the intended lab
laptop/pager pairing before presenting this draft as that specific showcase model.

Collection commitment is approximately **2 hours/student/week for two consecutive weeks**:
5 weekly sessions, 10 sessions total, about 20 student-session hours over the campaign.
These are planned collection hours, not completed contributions or capacity for model/GUI work.
Initial weekly slots for all five were supplied on 28 September and recorded privately.
They total 9 h 45 min/week, or 19 h 30 min over two weeks if unchanged. Following the lab's
rejection of overlap, the owner supplied two revised slots and a 29 Sep start. The proposal
now has no overlaps: Week 1 is 29 Sep–1 Oct and Week 2 is 6–8 Oct. Lab acceptance of these
dates/times and one shorter session remains open. Other capacity is unconfirmed. Previous individual
implementation allowances are not a commitment under the expanded priorities. STCray corrections, extra detector comparisons and optional
conference papers remain deferred.

[F05/C01](meeting_minutes/follow-up-collection-2026-09-28.md#catalogue-handoff-f05c01) supplies
the scenario catalogue: 125 four-bag groups / 500 planned images, 100 per student across
Session A/B (48/52). This conflicts with F03's earlier one-item weekly allocations and
E4/B3 extras: the catalogue includes both in Round 1. Confirm the lab's intended amendment
and map Session A/B to the proposed weeks before using the old rota's item columns.
Yonathan reports inventory readiness; first-day guidance and rota acceptance remain
unconfirmed. His email's undated availability is not a recurring booking. Keep the
15 October deadline while resolving assignment and post-midterm timing questions.

## Application ownership and delivery

The owner requested immediate public separation of the GUI on 27 September.
[RayGuard-App](https://github.com/abdalrahman-ismaik/RayGuard-App) now owns frontend/API/launcher development and consumes the
versioned SDP core through a pinned submodule. The team backlog, research and
collection obligations remain here. Local extraction, software checks and real
diagnostics are complete; human presentation rehearsal and lab pairing stay open.
This repository decision does not amend advisor requirements. F07 separately records
the later 14/17 October poster delivery/revision stages after the earlier 30 September stage. Use the application checkout for GUI contributions and
review core dependency changes here before advancing its pin.

## Earlier sequence (collection actions updated by F06 above)

| Order / timing | Required action | Evidence / dependency |
|---|---|---|
| Promptly, before proposed 29 Sep start | T26: send the final team proposal for 29 Sep–1 Oct and 6–8 Oct and obtain lab acceptance | F04 rejects previous overlap; revised private rota has none. Dated reply drafted, not sent; one shorter session unchanged. [Blank worksheet](templates/collection-schedule.md) |
| Before proposed 29 Sep start / first day | T27: confirm C01's assignment/session mapping, remaining acquisition/annotation/QC instructions and guidance on 29 Sep | Catalogue and 500-image target received; actual group/scan provenance, negative controls and log/review owners remain open |
| In parallel, ASAP | T23/T28: assign poster/GUI owners, confirm SLG date/model and rehearse the GUI draft; T22 complete per owner's all-five confirmation on 28 Sep | Registration receipts not independently inspected. Intended lab artifact pairing; reviewed real predictions, known miss and failure/empty states |
| 25–29 Sep, internal planning targets only | Content/layout review and GUI rehearsal as capacity permits; earlier SLG date takes priority if confirmed | Organizer format, advisor review and named submitter; no promised completion before visit date is known |
| **30 Sep, earlier invitation deadline** | Submit reviewed poster through confirmed route | Submission acknowledgement; registration is separate |
| Proposed Week 1: 29 Sep–1 Oct; Week 2: 6–8 Oct | T21: carry out 10 sessions against the lab-confirmed catalogue/assignment mapping; record attendance and usable samples | C01 plans 100 images/student in two sessions; resolve F03 conflict, A/B dates, lab acceptance and remaining protocol before collection |
| **By 15 Oct, current required milestone** | Complete Batch 1 distributed collection and review inventory/quality | Actual session records, counts, hashes, labels/groups and lab acceptance; review target to agree before deadline |
| Before/after Batch 1 as applicable | T29: inspect available base model early; adapt, train and evaluate once usable data and protocol exist | Lab model identity/support, justified split/metrics and real run manifests |
| After midterms, dates TBD | T30: second two-week broader collection campaign, then retrain and compare against Batch 1 | C01 includes E4/B3 in Round 1 despite F03 extras wording; clarify the amendment and broader Batch 2 scope/dates; no assumed improvement |

Hardik separately collects colorization data; phase 1 had a **15 October** target (T32). T24 records the separate summit registration/video as historical and unverified. F08 separately assigned Hardik/Fangzhou a visit video for 21 Oct (T37); the colorization phase-1 date does not become a video deadline.

## Prototype timetable conflict to resolve

M01's **8 October P1 / 15 October P2** targets are still recorded requirements. M02 does not
explicitly replace them, but its adaptation-after-Batch-1 sequence conflicts with the prior
P2 completion plan. T10/Q9 must reconcile deliverables/dates with the advisor. Do not keep the
old 9–14 October P2 evaluation/rehearsal blocks as active promises or invent replacement dates.

The ASAP GUI can expose a verified existing model without waiting for full P1 training.
That demonstration must accurately state its scope and limitations; it is not evidence that
the distributed detector or the full earlier P1 brief is finished.

## Technical preparation that can proceed now

1. T06/T28: run the already inspected device checkpoint on a declared diagnostic sample and
   establish the exact lab demo model. Save real outputs, class namespace, input hashes and
   latency boundaries; use a separately verified backend. No test-set tuning.
2. T28: review and rehearse the implemented GUI on the presentation laptop using the
   [launch instructions](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md). Upload, model/task identity, localization/score,
   zoom/pan, history/export and failure/empty states are implemented design choices, not newly
   quoted advisor specifications. Review the real positive and missed-threat examples; retain
   exact run evidence. Never turn zero detections into a benign verdict. Human rehearsal and
   confirmation of the intended lab model remain separate from automated browser checks.
   The user's airport-interface request now has a working folder receiver, queue, display
   tools and review notes. Identify the scanner/export interface, then observe one actual
   scan handoff; published-image replay is software integration evidence only. Rehearse
   pause/resume and the documented session-only queue/restart recovery before a demonstration.
3. T03/T05: resolve existing label/split contradictions and P1 decision semantics in parallel.
   These constrain accuracy claims; they do not block planning a GUI or checking execution.
4. T11/T27/T29: agree lab component taxonomy, genuine case/physical grouping and model
   handoff. The current schema has no component namespace; propose a reviewed extension
   before adding it. Do not synthesize groups from filenames.
5. T31: verify each member can access the repository/materials and explain shared code.
   Public visibility alone does not establish team access, write permission or understanding.

## Collection quality and remaining requirements

Use lab-provided scenarios and protocol; this plan does not prescribe acquisition or device
preparation. Record actual scanner/session/physical-instance/configuration/case/view provenance,
hashes, annotation review and usability. Preserve published IEDXray splits; new case-level
splits require lab-supported grouping. Check shared samples/physical groups before evaluation.

M02 did not fix the discussed **20 items / 20 scans per student / 200 detonator examples**
as acceptance criteria. C01 now supplies a **500-image Round 1 target**, but usable-image/QC
acceptance remains open. All listed bags contain a target and all groups contain four families;
negative/control outcomes are not supplied. The proposal's **500 total positive/negative samples**
therefore remains a separate scope question, not satisfied by matching the number alone. The simple GUI is
required now; remaining full control/recording GUI features need explicit scope/timing.

Three packages and firearms were examples, not a fixed scan-count limit or expanded project
deliverable. Meeting-reported model readiness is not executed evidence. The GUI draft has
[recorded checks](verification.md); this plan does not establish showcase acceptance, completed
collection, model adaptation, external email, registration or submission.
