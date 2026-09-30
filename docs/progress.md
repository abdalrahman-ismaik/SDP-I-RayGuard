# Engineering progress and contribution records

This page records shareable project evidence. It is not a claim of individual student
authorship, hours or understanding. Those must be recorded by the actual contributor and
reviewer. Do not include personal paths, private contacts, raw correspondence or artifact files.

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

## T28 logo exploration — 26 September 2026

At the user's request, root inspected the completed-eye poster and generated
32 distinct numbered RayGuard concepts with the built-in `image_gen` tool.
Two first-pass images received cleanup edits, making 34 generation/edit calls.
The selected output is 32 opaque RGB PNGs, each 1254 × 1254, totaling 26,898,465
bytes. A local browser gallery, numbered overview, exact prompt record and
SHA-256 manifest accompany the images under ignored
`outputs/logo-exploration-2026-09-26/`. [Shared scope](logo-exploration.md)
explains the families and local-only delivery without depending on these files.

Root owns generation and shared records; a separate agent implemented the
gallery, checked its behavior and independently reviewed the art. No student
authorship/hours or user selection are inferred. Existing application, animation
and concurrent work were preserved; no model execution or publication occurred.

`uv run --locked ruff check .` passed; `uv run --locked python -m pytest` passed
85 in 4.50 s. `node tmp/check-logo-gallery.cjs` passed 12 Chromium checks with
all 32 images loaded and none pending: filtering, file-based shortlist persistence,
text download, full-image dialog/Escape/focus, print-media visibility and layouts
at 1440, 390 and 320 px. PIL inspection read dimensions/modes and generated a
relative-path SHA-256 manifest; it did not create or modify the artwork. Software
checks and visual inspection do not establish model performance. Next is user
evaluation by concept number; vector/production refinement follows a selection.
T28's human rehearsal, intended model pairing and scanner handoff remain open.
Final independent visual coverage included all 32 current images and both revised
files. The browser-captured overview is 3040 × 1930 with all numbers visible.
`Compress-Archive -LiteralPath outputs/logo-exploration-2026-09-26 -DestinationPath
outputs/RayGuard-32-logo-concepts.zip` created a 31,110,324-byte local package;
Python `zipfile.testzip()` passed and its inventory contains all 32 selected PNGs.

## T28 HTML logo showcase opened — 26 September 2026

The user explicitly requested an HTML page showing the complete logo set. Root
reused the existing standalone gallery, and an independent read-only check
confirmed all 32 embedded concepts and PNGs plus the filters, full-image viewer,
shortlist and export controls. The browser connector opened the local `index.html`
in a preserved tab. No duplicate page, application change or publication was needed;
user evaluation by logo number remains pending under T28.

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
the real scanner handoff. Concurrent logo and eye-media changes were preserved.

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

## T28 second logo batch — 26 September 2026

The user requested more professional, premium and distinctive logo exploration
around eyes, iris, X-ray, computer vision and protection, and authorized downloading
logo-design skills. Root coordinated 24 new raster symbol concepts B01–B24, six
color variations, exact prompts, provenance and a SHA-256 inventory in ignored
`outputs/logo-exploration-batch-02/`. A separate agent owns the offline HTML
gallery and browser verification; another independently inspected all 24 symbols.
No student contribution, hours or acceptance are inferred.

The reviewed MIT-licensed RampStack `logo-design` skill was installed with
`install-skill-from-github.py --repo rampstackco/claude-skills --path
skills/logo-design --ref 3d4510a94a76ead80122c691b5c480f92f3fbe40` through the
system skill installer. Imagegen, Impeccable and Playwright also informed the work.
The personal skill installation remains outside the repository.

Built-in image generation produced each symbol separately and six color edits.
B21 received a targeted edit to remove an unintended pupil notch; its initial
image was retained under `iterations/`. Metadata records generator deviations
separately from exact prompts. The gallery supplies six family filters, four local
licensed wordmark pairings, 32px/64px preview tiles, persistent favorites and text
shortlist export. File-URL PNG links open the original in a separate tab; hosted
links offer direct download. The earlier batch remains available alongside it.

**Executed and verified:**

- `uv run --locked ruff check .` passed.
- `uv run --locked python -m pytest` passed **85 in 2.36 s**. These remain
  software checks, not detector or real-data evaluation.
- `uv run --locked python tmp/inventory-logo-batch2.py` decoded all **30**
  selected PNGs, with 30 distinct hashes; 29 are 1254 × 1254 and B04 is 1402 × 1122.
- `node tmp/check-logo-batch2.cjs --http` passed gallery checks for final labels,
  all images/fonts, filters, favorites/persistence, export, preview arrows/Escape,
  offline original opening, empty-state recovery and 320px/390px layouts without
  horizontal overflow. No page/console errors, failed requests or external
  requests were recorded for the offline gallery. A hosted PNG download matched
  source bytes. Temporary browser/server resources were closed.
- Root visually reviewed the white-backed artwork, final four-column/six-row
  overview, color sheet and mobile layout. Evidence is under
  `output/playwright/logo-batch2/`; overview/color sheets and browser results
  are included in the local pack.
- `Compress-Archive -LiteralPath outputs/logo-exploration-batch-02
  -DestinationPath outputs/RayGuard-Batch-02-24-logo-concepts.zip` produced a
  **24,743,760-byte** archive. Python `zipfile` checked all CRCs and confirmed
  **51 entries**, including the 30 selected artwork files and HTML page.

These are raster identity studies, not final vectors or finished favicon exports;
small previews retain source margins. Related shape explorations remain in the
collection for comparison. B01/B10/B08 were the independent review's strongest
starting shortlist, with B15/B24 as technical/fluid eye alternatives. User selection
is pending. No app branding was replaced, inference run, commit or publication
performed. T28 remains in progress for human presentation review, model pairing
and scanner handoff; the 30 September poster and unresolved 8/15 October versus
collection-first schedule conflict remain unchanged.

Next: the user evaluates B-number, palette and wordmark combinations; refine the
selected identity into precise production artwork. See [shared scope](logo-exploration.md).

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
model/scanner/showcase handoff. Concurrent logo and intro work was preserved.

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
staged, and local config, snapshots and evidence remain ignored. Existing logo,
intro, typography and other local work were preserved; no commit or push.

Next: the user reviews reference/model overlays and actual misses; the human
model/showcase owner confirms the intended laptop/pager pairing and rehearses the
presentation. Dataset-quality/provenance issues still gate fair full-test
evaluation; do not adjust thresholds using this test demonstration.

## T28 B20-focused logo variations — 26 September 2026

The user preferred B20 Dual Energy because it reads as an X, with 09 Iris Crest
and 07 Ribbon Sight as secondary references. Root coordinated 24 focused raster
variations C01–C24 and four separate palette studies of the original B20 using
built-in image generation. The three originals were inspected and copied unchanged
as references. Exact prompts, intended geometry and actual-art review notes are
preserved in the ignored local pack. The installed logo-design skill informed
silhouette and typography review; Imagegen, Impeccable and Playwright supported
generation and gallery checks.

Separate agents owned `outputs/logo-exploration-batch-03/index.html` and independent
art inspection, with root owning generation, packaging and shared records. The
gallery provides four families, four offline wordmark pairings, persistent
favorites, shortlist export, enlarged previews, 32px/64px comparison tiles and
original PNG links. Root inspected the final 24-concept overview, color sheet
and cleaned C21 white-backed preview. Image-generation edits removed artifacts
from C21, C22 and the B20 reverse study; their earlier iterations were retained.
C10's description now reflects the rendered layered cuts. No student authorship,
effort or acceptance is inferred.

Executed and verified:

- `uv run --locked ruff check .` — passed.
- `uv run --locked python -m pytest` — 85 passed in 2.95 seconds.
- `uv run --locked python tmp/inventory-logo-batch3.py` — all 28 selected PNGs
  decoded at 1254 × 1254, with 28 distinct SHA-256 hashes; only C21 retains alpha.
- `node tmp/check-logo-batch3.cjs` — gallery agent's final Chromium check passed
  for metadata agreement, all 31 selected/reference images, four fonts, family
  filters, persistence, saved-only comparisons, focus after removal, export,
  preview navigation, local PNG opening and 320px/390px layouts. No page/console
  errors, failed requests or external requests. Evidence is local under
  `output/playwright/logo-batch3/`; checks and overview/color sheets are also
  copied into the deliverable. This batch was checked as an offline file gallery.
- `Compress-Archive -LiteralPath 'outputs/logo-exploration-batch-03' -DestinationPath
  'outputs/RayGuard-Batch-03-X-variations.zip'` — completed. Python `zipfile`
  CRC/read-back verification passed: 53 entries, 28 selected artwork files,
  29,943,183 bytes, and the HTML entry point present.

These are related raster concepts for evaluation; final production work needs
vector construction and optical adjustment. Small tiles retain artboard margins;
palette edits may contain minor geometric/color differences. Suggested comparison
points C01/C02, C08/C14, C15/C19 and C23 are design judgments, not user approval.
The previous two packs remain available. This work changed no app branding,
detector behavior or model evidence, and performed no publication or commit.
Next: user chooses C-numbers, palette and wordmark for refinement. T28 remains
in progress for human showcase review and its existing model/scanner handoff;
the 30 September poster deadline and unresolved prototype/collection schedule
conflict remain unchanged.

## T28 simpler logo directions — 26 September 2026

The user did not find a final identity in batch 03 and asked for a simple,
creative mark that is clear and easy to understand. Root generated eight
distinct directions D01–D08 with built-in image generation, continuing B20
through two X concepts and exploring simpler eye, iris, guard and R constructions.
An image edit smoothed D05's lower contour. Exact prompts, original D05,
metadata and hashes are in ignored `outputs/logo-exploration-batch-04/`.

Root coordinated art, packaging and shared records; a separate agent owned the
offline HTML gallery and browser checks; another independently inspected all
eight images and a limited set of category precedents. A separate UI review
found no material fixes. No student authorship, hours or final approval is inferred.
The logo-design, Imagegen, Impeccable and Playwright skills supported this work.
Review favored D02 Cross Eye, D07 Sight R and D05 Shelter Eye; these are design
recommendations, not user selections or measured audience recognition.

Executed and verified:

- `uv run --locked ruff check .` — passed at the time of this logo work's check.
- `uv run --locked python -m pytest` — 85 passed in 2.45 seconds at that check;
  concurrent model-runtime development is separate from this result.
- `uv run --locked python tmp/inventory-logo-batch4.py` — eight selected PNGs
  decoded at 1254 × 1254 RGBA, all with alpha 0–255 and distinct SHA-256 hashes.
- Gallery agent ran `node tmp/sync-logo-batch4.cjs` and
  `node tmp/check-logo-batch4.cjs` after the D05 replacement. Passed: metadata,
  eight images on white, two fonts, favorites/persistence/export, keyboard focus,
  modal navigation, original PNG opening and 320px/390px layouts. No browser
  errors or external requests. Root inspected the final overview and all-eight
  16/32/64/128px proof. Evidence is under `output/playwright/logo-batch4/`;
  overview, small-size proof and check JSON are also in the review pack.
- `Compress-Archive -LiteralPath 'outputs/logo-exploration-batch-04'
  -DestinationPath 'outputs/RayGuard-Batch-04-Simple-Directions.zip'` — completed.
  Python `zipfile` CRC/read-back verification passed: 24 entries, eight selected
  artworks, 4,247,336 bytes, and the HTML entry point present.

All marks remain raster concepts. At 16px, D02/D07 retain X/R silhouettes but
their secondary eye details weaken; the tiles retain original artboard margins.
No final favicon, print or embroidery suitability is claimed. App branding and
detector behavior were not changed by this work; no publication or commit was
performed. Next: user selects a simpler structure for vector and optical refinement.
T28's human showcase review and model/scanner handoff remain open. The 30 September
poster obligation and unresolved prototype/collection deadline conflict are unchanged.

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

## T28 iris-focused logo studies — 26 September 2026

After rejecting batch 04 as too basic, the user clarified that the logo should
look like an iris. Root inspected the completed animation frame and 09 Iris Crest,
then generated six initial studies, two refinements and two replacements with
built-in image generation. Four studies are selected in the local batch-05 HTML
gallery. Wheel/scoop/rosette outcomes were excluded and retained only as local
iteration history. Exact prompts and selected-image provenance are bundled.

Root owned generation, curation, packaging and shared records. A gallery agent
owned the offline HTML and browser verification; another independently inspected
all selected images and rejected attempts. A separate ideation agent contributed
iris construction proposals. No student authorship, hours or approval is inferred.
Review favors E01 for a controlled logo and E04 for a more natural iris; E04's
illustrative detail needs further reduction for small production use. Earlier
X/R/eye recommendations do not establish a selected identity.

Executed and verified:

- `uv run --locked ruff check .` — passed.
- `uv run --locked python -m pytest` — 129 passed in 11.65 seconds at this check;
  concurrent runtime implementation is separate from the logo work.
- `uv run --locked python tmp/inventory-logo-batch5.py` — four selected
  1254 × 1254 RGBA PNGs decoded, each with alpha 0–255 and a distinct SHA-256 hash.
- Gallery agent ran `node tmp/build-logo-batch5.cjs` and
  `node tmp/check-logo-batch5.cjs` against the final four studies. Offline image/
  reference/font loading, favorites, persistence, export, preview navigation,
  original PNG links and focus passed; 320px/390px layouts had no overflow.
  No page/console errors, failed requests or external requests. Root inspected
  the final white-backed overview and 16/32/64/128px sheet. Evidence is under
  `output/playwright/logo-batch5/`, with final proofs/check JSON in the pack.
- `Compress-Archive -LiteralPath 'outputs/logo-exploration-batch-05'
  -DestinationPath 'outputs/RayGuard-Batch-05-Iris-Studies.zip'` — completed.
  Python `zipfile` CRC/read-back verification passed: 27 entries, four selected
  artworks, 9,632,229 bytes, HTML entry point present.

These remain raster review concepts. Internal features merge at very small sizes;
the preview tiles retain artboard margins and are not final favicon exports.
App branding, detector behavior and inference evidence were unchanged by this
work; no commit or publication was performed. Next: user selects the iris structure
and detail level for vector/optical refinement. T28 human showcase/model/scanner
handoffs, the 30 September poster obligation and the unresolved prototype versus
collection-first schedule conflict remain open.

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

## T28 iris-inside-shield variations — 26 September 2026

The user requested an iris contained inside a shield, in multiple variations
from simple to complex. Codex root coordinated the artwork and shared summary;
separate gallery and review agents owned the offline page/checks and independent
visual review. No student authorship or hours are inferred. Earlier work and
concurrent app/runtime edits were preserved.

The local `outputs/logo-exploration-batch-06/` contains twelve selected concepts
F01–F12, four each at Simple/Balanced/Detailed levels. Built-in image generation
used the existing Iris Crest, iris studies and animation references. Four
targeted edits removed gray inner shadows; the initial files and exact prompts
are retained. Every selected shield is closed and fully contains its iris/pupil.
Review suggests F02/F05/F10 for an initial cross-level comparison, with F07/F11
as useful alternatives; these are recommendations rather than user selections.

Executed and verified:

- `uv run --locked ruff check .` — passed.
- `uv run --locked python -m pytest` — 138 passed in 3.68 seconds; software
  checks, not real-model or data evidence for this logo work.
- `uv run --locked python tmp/inventory-logo-batch6.py` — twelve distinct
  1254 × 1254 RGBA PNGs, four per level; dimensions/alpha/hashes recorded.
- `node tmp/build-logo-batch6.cjs` and `node tmp/check-logo-batch6.cjs` — offline
  desktop/320px/390px checks passed for artwork, fonts, filters, cross-level
  favorites, empty states, export, preview navigation and keyboard focus.
  No browser errors, failed requests or external requests were recorded.
- Root and the independent reviewer inspected all final marks, four cleanup
  edits, the overview and the 16/32/64/128px proof. Detailed fibers are intended
  for larger display; the proof retains original artwork margins.
- `Compress-Archive -LiteralPath 'outputs/logo-exploration-batch-06'
  -DestinationPath 'outputs/RayGuard-Batch-06-Iris-Shields.zip'` and Python
  `zipfile` read-back — CRC passed, 35 entries, all twelve selected images,
  17,173,358 bytes. The gallery, fonts/licenses, originals, prompts, metadata,
  review, proofs and browser evidence are bundled.

These remain raster concept studies. F05/F08 need optical clearance refinement;
generated pixel colors are not final vector specifications. No identity was
adopted, and no model job, commit or publication was performed for this work.
Artifacts are local/ignored and need separate transfer. Next: user selects an
F-number/detail level for vector refinement. T28 remains in progress for human
showcase/model/scanner acceptance; the 30 September poster obligation and
unresolved M01/M02 schedule conflict remain unchanged.

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

## T28 C19/C21 logo variations — 26 September 2026

The user asked to revisit C19 Eye Weave and C21 Guarded Cross and create many
creative variations. Codex root coordinated artwork and shared documentation;
separate agents proposed construction ideas, built/checked the gallery and
independently reviewed actual artwork. No student authorship or hours are inferred.
Earlier artifacts and concurrent app/runtime work were preserved.

`outputs/logo-exploration-batch-07/` presents sixteen G-series concepts across
Eye Weaves, Guarded Forms, Iris Hybrids and New Constructions. Both requested
references remain unchanged and visible. Sixteen initial built-in image calls
and one G13 fill-cleanup edit produced the selected artwork; exact prompts and
the superseded G13 are retained. G08's generated counter was closed rather than
open, so its name/caption were corrected to Tapered Crest. G04/G05/G16 are review
suggestions, not user selections. Near-duplicates and alternate visual readings
are documented rather than claiming sixteen unrelated or globally unique marks.

Executed and verified:

- `uv run --locked ruff check .` — passed.
- `uv run --locked python -m pytest` — 143 passed in 3.74 seconds.
- `uv run --locked python tmp/inventory-logo-batch7.py` — sixteen distinct
  1254 × 1254 PNGs, four per family; four RGBA and twelve RGB files. Inventory
  was refreshed after the G13 replacement.
- `node tmp/build-logo-batch7.cjs` and `node tmp/check-logo-batch7.cjs` — offline
  desktop/320px/390px checks passed for images, two local fonts, family filters,
  cross-family favorites, export, preview navigation, PNG access and focus.
  Full checks passed again after G13 cleanup; no browser errors, failed requests
  or external requests were recorded.
- Root and the independent reviewer inspected all selected marks, the overview,
  original-margin 16/32/64/128px proof and G13 cleanup on white. Both fill blemishes
  were removed while retaining its contours and pupil.
- `Compress-Archive -LiteralPath 'outputs/logo-exploration-batch-07'
  -DestinationPath 'outputs/RayGuard-Batch-07-Weave-and-Guard.zip'` and Python
  `zipfile` CRC/read-back verification — passed, 33 entries, sixteen selected
  images, 15,088,134 bytes.

The pack includes the offline gallery, originals, references, exact prompts,
metadata/hash inventory, review, proofs, browser evidence and font licenses.
These are raster selection studies; several fine distinctions disappear at
16/32px and need optical/vector refinement. No identity was applied to the app,
and no model job, commit or publication was performed for this work. Generated
artifacts remain local/ignored. Next: the user selects G-numbers for refinement.
T28 human showcase/model/scanner acceptance stays open; the 30 September poster
obligation and unresolved M01/M02 schedule conflict remain unchanged.

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

## T28 fresh sharp-eye logo direction — 26 September 2026

The user explicitly rejected earlier designs and requested thirty new AI logo
ideas: a sharp, serious eye that watches the viewer, integrated with X-ray and
project-related inspection ideas. Root coordinated concept generation, selection,
prompt/provenance records and shared documentation. Separate agents prepared the
offline gallery and independently reviewed every selected image and proof.
No student authorship or hours are inferred.

The local batch-08 pack contains thirty H-series PNGs across six families,
an offline HTML gallery, two licensed local wordmark pairings, family filters,
favorites/shortlist export, enlarged previews, overview and small-size proof.
Fifty generation/edit calls produced thirty selected results; eighteen were
revised for sharper gaze, cleaner details or framing. All fresh generations had
no image references, and edits used only this batch's new artwork. Earlier
artwork remains historical and is not referenced by this gallery.

Actual commands and outcomes:

- `uv run --locked ruff check .` passed; `uv run --locked python -m pytest`
  passed **143 tests in 4.43 s**. These are software checks, not detector evidence.
- `uv run --locked python tmp/inventory-logo-batch8.py` decoded thirty PNGs,
  verified distinct hashes and six groups of five, and wrote `manifest.json`.
- `node tmp/build-logo-batch8.cjs` and `node tmp/check-logo-batch8.cjs` passed
  **22 browser check categories**, including all images, offline controls,
  local fonts, saved choices, export and desktop/320px/390px layouts. No browser
  errors, failed requests or external requests. Proofs and checks are bundled.
- `uv run --locked python tmp/package-logo-batch8.py` checked source/browser/
  manifest hash agreement and created `outputs/RayGuard-Batch-08-Sharp-Eyes.zip`:
  **44 files, 30 selected PNGs, 10,465,121 bytes**. CRC and full read-back passed.

Root and independent review favor comparing H01/H11/H13/H21 first, with H26 as
a heavier alternative. The local review describes all thirty actual renders,
related variants, H27's retained pupil highlight, H28's mascot reading and tiny-
size limitations. These remain raster concepts, not approved vector masters;
no uniqueness or model-performance claim is made. No app identity change,
model job, publication or commit/push was part of this work.

Next: user chooses H-numbers for vector/optical refinement. T28 remains open for
human showcase/model/scanner acceptance. The 30 September poster obligation and
unresolved M01 8/15 October versus collection-first schedule conflict remain.

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

## Add the next actual result

For each meaningful result record:

- Date, task ID, actual contributor and reviewer; hours only if actually reported.
- What changed and the relevant commit, pull request or shareable technical record.
- Exact commands/data/model pairing as applicable, actual result and known limitations.
- Review/explain-back completed, blockers and the next action.

Keep detailed machine/run manifests in authorized private storage. A command someone plans
to execute is not a completed experiment, and a generated draft is not a student contribution.
