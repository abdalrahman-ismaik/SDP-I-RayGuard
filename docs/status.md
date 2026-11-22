# Current project status

**Collaboration update, 21 November:** the owner prioritizes assigned work and authorizes a teammate blocked by a small dependency to
finish another lane's work without waiting for its lead. Record scope/actual editor,
notify affected teammates and proceed in isolation; coordinate active collisions and
shared GPU/output use. Names in task handoffs are contacts, not exclusive implementers.
Retain independent review, scientific gates, protected branches and accurate credit.

Updated 21 November 2026. Read [tasks](tasks.md), [meeting records](meeting_minutes/README.md)
and [the plan](plan.md) for the authoritative backlog and requirements.

## Pull request review — 22 November

The current GitHub PR list has two open requests. **PR #22** (`ali/data-policy`, head
`3ee9c87`) proposes the frozen test split, shared seed-17 ~80/20 training partition,
exact-byte duplicate grouping and an exploratory label; hosted Linux/Windows CPU checks
pass, and Ali reports 288 synthetic tests passed. Ahmed reports an audit of 17,360 images
confirmed five matching sub-0.001 px boxes in each training export; per-box evidence was
not inspected in this checkout. No repair, findings hash or partition has run. The update
addresses the pending-receipt default, source-area recording and split guard; T41's
partition builder requires approved owner/reference and matching findings hash. Review
identified one wording correction: unchanged COCO `area` may affect size-specific validation
metrics on a repaired training-derived validation split, even though T42's frozen objective
uses overall AP@[.50:.95]. Commit `3ee9c87` corrects that rationale and clarifies the receipt
attribution. Isolated-worktree checks: Ruff clean; pytest 272 passed / 2 skipped because
`pycocotools` was unavailable, with no warnings. Hosted checks passed. The human
receipt remains unfilled; Ahmed must verify the actual published test export/hash during the
data run.

**PR #20** (`docs/semester-progress-2026-11`) remains open at seven commits / 70 files,
including report draft sources and event materials. CI passes at `56b8a4c`, but the
approving review was dismissed as stale after later commits. It needs a
fresh independent human review of the current diff and reconciliation with the 22 Nov
policy handoff. No GitHub review or merge was submitted in this review. See [T38/T40–T42](tasks.md)
and [the current plan](plan.md#pull-request-review--22-november).

**HPC handoff — 22 November:** Ahmed reports all 124 transferred files, the dataset and
exact starting weights verified; image audit of 17,360 images completed; GPU environment
job 740 failed at font discovery and job 741 passed after cache preparation; local checks
reported 442 passed/11 skipped and Ruff clean. No annotation repair, partition or T41
trials ran, and no jobs remain active. This evidence is in Ahmed's referenced handoff,
which is not present in this checkout. Job 741 validates environment setup; full trainer
qualification remains after PR #22 review and the human-filled policy receipt.

## Report priority — 21 November

Owner confirms the 24 Nov report deadline; target **17:00 UTC+4**. The primary handbook
requirements and owner-approved **LaTeX/PDF plus checked Word** workflow are recorded in
the [report specification](final-report-requirements.md), including six SDP I chapters,
paper/project/meeting sources, figures/tables, Gantt chart, applicable forms and both
assessment rubrics. T38 and the [delivery sequence](plan.md#report-delivery-sequence-agreed-21-november)
track remaining work. A 40-page LaTeX draft PDF and a generated Word draft now exist
locally; DOCX pagination/fidelity review against the PDF and requirement-by-requirement
review remain open. Official form review/signatures, student ownership/contribution
confirmations, full patent-database search, final PDF/Word distribution clearance and
submission are not verified complete. The owner authorized the working LaTeX source and
original figures for GitHub publication on 22 Nov; this does not clear the assembled
report or signed/private materials. Next: compare the Word copy page by page, map actual evidence to
the handbook/rubrics, complete the required patent search and close official forms and
submission route. The older 27 Nov notice remains a
recorded conflict; plan around 24 Nov.

## Latest software and PR handoff — 21 November

**Latest outcome:** PR #18 merged into main as `9350482` after update-head `6edcd68`
passed Ruff, **273 evaluation-enabled tests**, and required Linux/Windows CI. Both
review threads resolved and description updated. Earlier pending-review statements
below are historical snapshots. Ahmed can integrate from main; T42 remains in progress
for real metrics. Next: bind real data-policy findings/partition receipts and qualify
the trainer/evaluator pilot. No real training/evaluation was executed by this review.

Selected remote artifacts and current PR metadata inspected: T40 PRs #17/#19 are
merged; initialization PR #21 (`b325c28`) has passing hosted CPU checks and requires
human review. Ahmed's T41 branch `32091bc` implements blocked planning/synthetic
study software and a Slurm template, not live training; no open T41 PR found. Ali's
T42 PR #18 now at `6dfa7d6` contains both safeguards, the validation objective and
common-parent comparison; hosted CPU checks pass, earlier changes-requested review
needs human re-review. Trainer integration and data policy remain open; no real metrics.
T41/T42 now in progress. Mohammad's branch records
an app acceptance slice; actual shared app commit and human walkthrough need review.
No open RayGuard-App PR found at inspection. No real training, full evaluation or HPC
qualification verified by this review. [Current dependency order and handoffs](plan.md#latest-team-integration-review--21-november).
Next: Abd reviews #21/#20 and Ahmed's software PR to main; Ali fixes #18 and agrees
validation/data policy with Ahmed. Prioritize report evidence by 23 Nov, submission
24 Nov 17:00; preserve unfinished studies as limitations. Older 19 Nov draft targets
and proposed-owner wording below are historical; current task rows supersede them.

## ML planning update — 18 November

HPC access and CVMI Lab provision of the models/resources are owner-confirmed.
The new [research protocol](finetuning.md) targets checkpoint evaluation reproduction,
author-training reproduction where possible, and controlled Optuna improvement:
generic then specific explosives, 20 attempted configurations per task. Ahmed
owns training/search/Slurm, Faisal baseline/shared contracts, Ali independent
metrics; assignments need student acceptance. The [HPC handoff](hpc-training.md)
summarizes inspected manuals. No trainer, environment, new run or improvement is
verified by this documentation update. Next: owners agree split/data policy,
initialization and metric handoffs, then qualify a GPU pilot. The 19 Nov milestone
is a draft/review target; study completion depends on pilot timing.

## Immediate priorities

- **T14 — CS-HPC access handoff:** email received **4 November 2026 at 12:52 pm** says credentials and job-submission manuals were issued to the named SDP1 recipients; change the initial password at first login. Credentials are intentionally not recorded here or in Git. The owner now confirms HPC access; individual password-change/permissions and new RayGuard job/backend qualification are not inferred. Supplied manuals were inspected for the current training plan. Next advisor appointment is still TBD.

- **T39–T43 — proposed first-draft prototype sprint:** Abd and Mohammad/Mohammed (name/handle to confirm) own GUI requirement fit and polish, preserving the extensive in-progress app work; both also review ML integration. Faisal (T40) owns baseline/run integration, Ahmed (T41) fine-tuning, and Ali (T42) evaluation. Use the exact CVMI model configured in the GUI and public IEDXray data after verifying artifact/task identity. Dismantled scans count toward their collection-progress workstream only, not this single-scan dataset. Contributions must remain accurately attributed. Since 22 Nov, explicitly owner-authorized agents may commit/push with clear agent metadata; human review and protected-branch integration remain required. Owners remain proposed. Target an integrated draft by **19 Nov**; preserve all existing uncommitted work. No new code, training run or full-data evaluation is claimed by this plan.

- **T38 — end-of-semester submissions and assessment:** use **24 November 2026, 5:00 pm UTC+4** as the working Blackboard report deadline (one attempt; no late submission); another pasted notice says 27 Nov, so confirm the active course link/deadline. Email the same report to supervisors and examiner and put it in GitHub. Include the repository link and per-student contribution table. Each student should prepare a GitHub contribution explain-back with the supervisor. Prepare for **Friday 27 November, 8 am–12 pm** presentations, 20 minutes plus 10 minutes Q&A; assigned slot/room and demo timing remain to confirm. See the [course checklist](course-endgame-2026-11.md). No report, submission, rehearsal or individual contribution evidence has been verified.

- **T37 / T28 — Secure Life Group visit:** [F08 visit requirements](meeting_minutes/follow-up-slg-2026-10-19.md) confirms **Wednesday
  21 October, 2–5 pm** (project time context: Asia/Dubai). Presence is required. The
  **SDP team prepares a digital poster on the project and progress**; Divya prepares
  the lab; Hardik/Fangzhou prepare a high-quality video of their work/approaches.
  Name the SDP editor/presenter, confirm display requirements and rehearse the earlier
  GUI obligation. Readiness and attendance remain unverified. This follows the Tuesday
  6G session; its 9:16 poster specification does not automatically apply to SLG.

- **T21/T26/T30 — collection inventory and remaining checks:** the lab-computer snapshots were inspected. The latest has **577 JPEG paths and 478 distinct image byte payloads**, with 99 exact duplicate copies in Ahmed's `total` folder; all 577 decode, but QC/case provenance is unverified. Filename dates are 29 Sep–9 Oct, with per-student counts in the [dated inventory](collection-progress-2026-11-14.md). The provisional 478-versus-500 difference is not yet an accepted shortfall: students must confirm their counts and the lab must confirm round/catalogue mapping and accepted/usable criteria. Scans remain on the lab computer; use the [member contribution guide](collection-contribution-guide.md) to verify personal counts and commit sanitized GitHub evidence. F06's second-round schedule and **30 Nov 2026** overall deadline remain. Optional ~5 pm slots are not mandatory. The 15 Oct Batch 1 milestone is historical and completion remains unverified; T10/Q9 and the earlier prototype-date conflict remain open.
- **T27 / earlier rota:** the September proposal covered 29 Sep–1 Oct and 6–8 Oct;
  lab acceptance, shorter-slot acceptance and guidance attendance remain unverified.
  [C01](meeting_minutes/follow-up-collection-2026-09-28.md#catalogue-handoff-f05c01)
  plans 125 four-bag groups / 500 images, 100/student across A/B (48/52). Its all-family
  allocation and E4/B3 inclusion conflict with F03. Reconcile assignments and actual logs;
  annotation/export instructions, physical provenance, QC/negative controls and log owner
  remain open. The old proposal does not establish second-round availability.
- **T23 — accepted poster / digital revision:** [F07 poster follow-up](meeting_minutes/follow-up-poster-2026-10-19.md) records acceptance
  (12 Oct), a 17 Oct revision request for **1080 × 1920 px, portrait 9:16**, and Divya's
  new-template presentation handoff acknowledged by Brahim. The owner reports the team attended
  on 20 Oct. Individual attendance and presentation evidence remain unreviewed. **TDRA approval
  and the revised artifact remain unverified**; retain T23 only for these unresolved historical
  deliverables.
- **T28 / earlier showcase:** rehearse the laptop GUI and poster on **Embedded Explosive Detection
  in Electronic Devices** for the now-dated SLG visit (21 Oct, F08). Intended lab pairing
  remains unconfirmed; the earlier 30 September poster stage is followed by F07's
  14/17 October delivery/revision requests. The
  [research poster v6 review bundle](posters/6g-mena-2026/README.md) now includes the
  editable PowerPoint and matching PDF in Git. It covers both problems with enlarged
  source figures and preserves the supplied credits. Prof. Naoufel/team review,
  print size and submission remain open. The separate showcase v3 stays local;
  confirm the advisor's combined-versus-separate CT/colorization scope and obtain
  any required CT/video material. The earlier topic/deadline is not silently replaced.
- **T22 complete:** on **28 September**, the owner explicitly confirmed that all five
  students are registered for 6G. This is documented confirmation; receipts were not inspected.
  Hardik's separate registration remains T24.
- **T29/T30:** inspect the distributed base model early, adapt/evaluate after usable
  Batch 1, then collect a broader two-week batch after midterms and retrain. F03 names
  E4/B3 as extras, but C01 includes both in Round 1. Reconcile that conflict and retain M02's
  broader post-midterm Batch 2; F06 requests its schedule and sets 30 November overall completion; exact batch dates remain open.
- **T32/T24:** Hardik's separate colorization phase 1 is due **15 October**;
  his summit registration/video remain separate actions with no exact summit-video deadline
  supplied. F08 separately requires Hardik/Fangzhou's visit video ready for 21 October.

**Schedule conflict:** M01's P1/P2 targets were **8/15 October**. M02 places adaptation
after Batch 1 collection. T10/Q9 must reconcile these obligations; no replacement
prototype dates or cancellation have been supplied.

## Application and research repositories

The GUI now lives in [RayGuard-App](https://github.com/abdalrahman-ismaik/RayGuard-App). Make app changes there; use its
[single launcher and setup guide](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/README.md). Its `engine/` submodule
pins this repository's shared contracts, model catalog, detector tooling and
runtime profiles at `b7ec59e`. Research, CPU audits, P1/P2 and the sole team backlog
remain here. Original local app files and services were preserved as an ignored
recovery copy, not an active second GUI source tree. Attribution distinguishes the
owner's GUI direction/maintenance, assisted implementation and team/upstream work.

The Git boundary was rechecked: no legacy app/media/launcher or GUI-workflow
files are tracked here. `.gitignore` also excludes nested `RayGuard-App/` and
copied `frontend/` / `backend/` roots. Shared engine source remains tracked here;
the boundary audit did not modify the independent application checkout.

The [extraction checks](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/migration.md) passed: root lint/143 CPU
tests, app lint/280 API tests, production build and 149 browser checks. Fresh real
CPU/GPU qualification and two ordinary generic YOLO runs passed in the new folder:
a training-image positive and the retained test-image miss. These diagnostics are
separate from synthetic software checks and do not establish accuracy or benignness.

The app implements upload, automatic folder receipt, finite test replay, actual
boxes/scores, verified generic reference comparisons, zoom/pan/magnifier, viewing
adjustments, themes, processing/completed split view, model/device choice, notes,
session history and JSON export. Three inspected YOLOv10 tasks have bounded execution
evidence; other families remain unavailable. Empty detections are never a safe verdict.
Queues/history are session-only. The scanner/interface is unconfirmed; published-image
replay is not a real scanner connection. Other-host GPU/CPU qualification and human
rehearsal remain open. Details and prior diagnostics are in the app documentation.

## Research evidence and open work

The [poster plan](poster-plan.md) records the preparation of research v6 and the
local showcase alternative. The [v6 PPTX and PDF](posters/6g-mena-2026/README.md) are
versioned for team review. Original paper annotations, all thirteen reported metrics,
source attribution and the supplied credits are retained. Native PowerPoint and
independent scientific/visual checks passed; the current user-saved PDF/PPTX also
passed text, package and publication checks. F07 separately documents poster acceptance
and receipt of a new-template revision; TDRA approval, final artifact inspection and actual
presentation remain open. Repository v6 is not established as that revision.

CPU audits, strict JSON contracts and genuine generic/device/specific YOLO execution
exist. [Data audits](verification.md) retain unresolved label disagreements, geometry,
cross-split duplicates and physical-group provenance. Published splits are unchanged.
Full P1 association/decisions, distributed P2 fusion, new model training/evaluation and
lab collection are unfinished. Human model/GUI ownership must be accepted explicitly.

Collaboration rules and owner-reviewed PRs with required Linux/Windows CPU checks are
active on the shared SDP branches. Write-access invitations were sent on 27 September
to `mohd2k5`, `blitzict`, `Boshahab` and `Alshamisi10987` for SDP-I-RayGuard; all four
were pending acceptance at verification. T31 is in progress for acceptance, needed
material access and explain-back. Invitations do not establish contributions or
understanding. The registration report above is separate from GitHub access; poster acceptance/revision receipt is separately documented in F07; collection completion
and presentation/TDRA approval remain unverified. The owner reports team attendance at 6G MENA on 20 October; individual attendance records and presentation evidence were not independently reviewed.

The owner approved **A03 · Cobalt / controlled refinement** on **28 September**,
superseding A04-02 Optical/Manrope 650. The exact transparent PNG now has its own
`assets/logo/a03-cobalt-controlled-refinement/` folder in the separate RayGuard-App
checkout, with approval and provenance records. Earlier logo studies, source packages
and runtime snapshots are in that app's ignored dated archive; 472 file hashes matched.
The approved master is unchanged. The app still renders the previous A04 artwork;
A03 runtime replacement remains pending. Historical A04 build/lint/280 API/147 browser
and shared lint/143 CPU checks remain historical evidence, not A03 adoption checks.
See [progress](progress.md) and [verification](verification.md) for the evidence boundaries.
No branding publication or student hours are inferred.
