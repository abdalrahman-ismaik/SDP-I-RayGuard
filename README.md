# SDP-I-RayGuard

**AI-Powered Explosive Detection in X-ray Scans** — a Khalifa University Senior Design Project.
Advisor: **Prof. Naoufel Werghi**. Technical guidance: **Dr. Divya Velayudhan**.

RayGuard investigates how X-ray evidence of suspicious components can be combined across
separate bags or packages. Following the **24 September meeting**, the main priority is the
distributed dismantled dataset and model adaptation. An early single-scan laptop GUI supports
the **Embedded Explosive Detection in Electronic Devices** showcase. The executed detector
baseline is **IEDXray + YOLOv10-M**; STCray and extra detectors remain optional.

**Overall collection deadline: 30 November 2026.** The
[latest follow-up](docs/meeting_minutes/follow-up-collection-2026-10-19.md) requests individual
first-round counts against **500** and the **second-round schedule**. Finish any first-round
shortfall on the same set before moving on. Around **5 pm** is preferred where feasible,
not mandatory; exact second-round dates await current availability and lab acceptance.
The earlier **15 October Batch 1** milestone remains historical and completion unverified.
Yonathan's catalogue plans **500 images across 125 four-bag groups**; see the
[collection table](#dataset-collection--round-1).

The owner reports that the project team attended **6G MENA on 20 October 2026**. This is
retained as historical project evidence in the [6G MENA record](docs/6g-mena-2026.md);
individual attendance, the actual presentation, and TDRA approval have not been independently
verified. The separate Secure Life Group visit record and 6G poster artifacts remain available
for the final report.

## RayGuard application

The GUI is maintained separately in **[RayGuard-App](https://github.com/abdalrahman-ismaik/RayGuard-App)**,
with its own launcher, frontend/API, tests and documentation. Abd Alrahman Basim Ismaik
directs and maintains the application; its [credits](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/CREDITS.md)
distinguish app development assistance, team research and published models/data.
This repository remains the SDP research and shared inference source. The app pins a
specific revision of those tools; teammates should use its documented release/setup.

The legacy local `app/`, `assets/` and `run-app.ps1` are excluded by
[.gitignore](.gitignore); app source is versioned only in RayGuard-App. Nested
`RayGuard-App/` copies and copied `frontend/` / `backend/` roots are also excluded.
Shared `src/sdp_xray/`, `scripts/` and `environments/` remain versioned here and
are consumed by the app through its pinned `engine/` submodule.

## Current progress

As of **14 November 2026**, the shared repository contains a dated inventory of the
dismantled-scan collection: **577 JPEG paths, 478 distinct byte payloads, and 99
exact-copy paths**. All files decoded, but catalogue mapping, QC, physical-case
provenance and lab acceptance are not established. The scans remain on the lab
computer. This collection supports the dismantled multi-scan work and is not the
single-scan training, evaluation or demo dataset. See the
[inventory and date breakdown](docs/collection-progress-2026-11-14.md).

For the single-scan prototype, the intended public source is IEDXray. A limited
YOLOv10-M inference baseline exists, but it is not a full benchmark evaluation or
fine-tuned result. The exact checkpoint configured by the GUI and its source/hash
still need reconciliation. The GUI supports upload/folder intake, finite IEDXray
test replay, actual boxes and reference comparison, operator review, export and
CPU/GPU selection. See the [app guide](https://github.com/abdalrahman-ismaik/RayGuard-App)
and [single-scan ML plan](docs/single-scan-ml-pipeline-plan-2026-11.md).

The team received CS-HPC access details by email on **4 November 2026, 12:52 pm**.
Credentials are private. Login, first-login password change, permissions, manual
review and job submission have not been verified; see the shared
[status](docs/status.md) and [progress record](docs/progress.md).

The proposed November work split is: Faisal, reproducible baseline; Ahmed,
fine-tuning pipeline draft; Ali, evaluation design and implementation; Abd and
Mohammad, GUI refinement and acceptance, with both also reviewing the ML integration.
These are proposed task owners until each person accepts and records actual work in
the [shared progress file](docs/progress.md) and [task backlog](docs/tasks.md).

Bounded real CPU/GPU runs establish execution compatibility, including known
misses; they do not establish accuracy. Synthetic software checks and real
inference evidence are recorded separately in [verification](docs/verification.md),
[baseline evidence](docs/first-inference.md) and [data audits](docs/iedxray-audit.md).
The scanner connection, intended lab model pairing and human showcase rehearsal
remain unverified. Full P1 association/decisions, P2 fusion, fine-tuning and model
evaluation remain unfinished. Empty detections never establish a benign scan.

The **[poster review draft, version 6](docs/posters/6g-mena-2026/README.md)** is now
available as a [PDF](docs/posters/6g-mena-2026/RayGuard-Research-Poster-v6.pdf) and an
[editable PowerPoint](docs/posters/6g-mena-2026/RayGuard-Research-Poster-v6.pptx).
It covers both detection problems, with enlarged source figures, linked detail views,
published benchmark results and a saved RayGuard demonstration. Prof. Naoufel and the
team can comment and improve the PPTX directly. This is the earlier review artifact;
F07's received new-template revision was not inspected or identified with v6. TDRA approval
and actual presentation remain open under [T23](docs/tasks.md); the proposed multi-package study
is clearly distinguished from measured single-image results.

## Dataset collection — Round 1

The received [collection catalogue (F05/C01)](docs/meeting_minutes/follow-up-collection-2026-09-28.md#catalogue-handoff-f05c01)
assigns **at least 100 images to each of five students across two sessions**. Its listed
configurations total exactly 100 per student. Each group contains four distinct bags,
with one registered target per bag: explosive simulant, battery, detonator simulant or
standalone wire, plus the catalogue's specified clutter.

| Catalogue session | Groups per student | Images per student | Team groups | Team images |
|---|---:|---:|---:|---:|
| Session A · G01–G12 | 12 | 48 | 60 | 240 |
| Session B · G01–G13 | 13 | 52 | 65 | 260 |
| **Round 1 total** | **25** | **100** | **125** | **500** |

| Target family | Catalogue item codes | Planned images |
|---|---|---:|
| Explosive simulant | E1–E4 | 125 |
| Battery | B1–B3 | 125 |
| Detonator simulant | D1–D3 | 125 |
| Standalone wire | W1–W2 | 125 |
| **Total** | **12 item variants** | **500** |

**Collection status: in progress on self-report; team total and QC unverified.** Faisal
reports 102 first-round scans, but his formula gives 104 while the catalogue plans 100 per
student. Other students' counts are not supplied. Reconcile files/logs before accepting totals.
These tables show catalogue targets; their Session A/B both belong to Round 1 and differ from
the pre-/post-midterm collection rounds. The five clutter levels each cover 100 planned images. Set numbers
restart for each student/session, so a set label alone does not uniquely identify a group.

Lab confirmation is still needed for the proposed dates, Session A/B mapping to weeks,
and replacement of the earlier one-item weekly assignments: the catalogue covers all four
families per student and includes E4/B3 in Round 1. Scanner/export instructions, annotation
rules, QC and negative/control examples remain open. F06 sets **30 November** for overall
collection; the earlier **15 October** first-round milestone remains historical and unverified.
See [current tasks T21/T26/T27](docs/tasks.md) and [requirements](docs/context.md) for the
acceptance details. Original lab documents and filled personal schedules remain private.

## Joining the project

Start with the [team documentation index](docs/README.md) and [contribution/setup guide](CONTRIBUTING.md).
Read [current status](docs/status.md), choose an agreed task from the [shared backlog](docs/tasks.md),
then consult the [requirements](docs/context.md), [plan](docs/plan.md) and
[latest meeting summaries](docs/meeting_minutes/README.md). Everyone uses these same records;
cloning the repository does not grant access to datasets, weights or private lab documents.
For agent-assisted work, use the shared [AGENTS.md](AGENTS.md) and
[four project skills](CONTRIBUTING.md#working-with-agents). Personal client settings stay local.

## Workstreams and their next tasks

**Immediate priorities:** reconcile individual first-round counts against 500, finish any
shortfall on the same set and prepare the second-round schedule for lab acceptance. Resolve
catalogue/protocol/QC questions and reconcile the 577-path inventory with the approved
catalogue. Keep collection evidence separate from the IEDXray single-scan benchmark. Confirm
the proposed workstream owners and record accepted assignments and actual results in the
shared progress file. The inventory does not certify the accepted collection total.

| Workstream | Goal and immediate tasks | Start here |
|---|---|---|
| **Collection and dismantled multi-scan** | Reconcile the 577 paths/478 distinct payloads with the approved catalogue, QC and physical-case records; confirm accepted counts and next collection actions with the lab. Do not use this collection as single-scan training/evaluation evidence. | [Collection inventory](docs/collection-progress-2026-11-14.md), [P2 interface](src/sdp_xray/p2/__init__.py), [shared contracts](docs/contracts.md) |
| **Faisal — single-scan baseline (proposed)** | Reproduce and document the public IEDXray baseline, confirm the GUI checkpoint provenance, and record an approved split-preserving evaluation protocol. | [ML pipeline plan](docs/single-scan-ml-pipeline-plan-2026-11.md), [model catalog](docs/checkpoint-catalog.md), [baseline evidence](docs/first-inference.md) |
| **Ahmed — fine-tuning pipeline (proposed)** | Draft a reproducible fine-tuning path and data/config checks; report decisions and limitations. Do not launch a large training job until data/split and HPC access are verified. | [ML pipeline plan](docs/single-scan-ml-pipeline-plan-2026-11.md), [tasks](docs/tasks.md) |
| **Ali — evaluation (proposed)** | Implement/review a fair evaluation workflow, metrics and error analysis that preserve the published test split and distinguish software checks from detector evidence. | [ML pipeline plan](docs/single-scan-ml-pipeline-plan-2026-11.md), [evaluation records](docs/verification.md) |
| **Abd and Mohammad — GUI and ML integration review (proposed)** | Polish the existing GUI, align its outcomes with requirements, and review the detector/pipeline interface and evidence. GUI source changes belong in RayGuard-App. | [GUI setup](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md), [app architecture](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/architecture.md), [demo plan](docs/implementation-plan-demo-2026-11.md) |
| **Hardik — colorization** | Historical phase-1 target was 15 October. The separate summit-video action is past; completion is not established. F08 separately assigned Hardik/Fangzhou a video for the 21 October Secure Life Group visit. | Coordinate with the lab; no colorization implementation in this repository |

The P1/P2 interfaces are explicit stubs. The proposed workstream owners must accept tasks and
record actual contributions; a proposed assignment is not evidence of completed work. Both
modules share `common/` and `data/`; merge small changes into `main` from
`prototype/p1-single-scan` and `prototype/p2-multiscan`.

## Repository structure

```text
SDP-I-RayGuard/
├── src/sdp_xray/
│   ├── p1/                 # Single-scan pipeline interface
│   ├── p2/                 # Multi-scan fusion interface
│   ├── common/             # Shared JSON validation
│   ├── data/               # COCO and STCray audit tools
│   └── cli.py              # Environment checks and dataset audits
├── scripts/                # Catalog-bound YOLO inference and runtime setup
├── environments/           # Reviewed model environment profiles and locks
├── configs/                # Portable configuration example
├── tests/                  # Synthetic software tests
├── docs/                   # Shared status, tasks, requirements, plan and evidence
│   ├── README.md           # Documentation index and reading order
│   ├── posters/            # Current review poster: editable PPTX and matching PDF
│   ├── meeting_minutes/    # Reviewed Markdown summaries; original PDFs excluded
│   └── templates/          # Blank collection schedule and sample manifest
├── data/ & models/         # Usage notes; actual artifacts stay local
├── .github/workflows/      # Automated software checks
├── AGENTS.md               # Shared instructions for project agents
├── .agents/skills/         # Four focused audit, baseline, evaluation and demo workflows
├── CONTRIBUTING.md         # Setup, branches, reviews and evidence standards
└── pyproject.toml, uv.lock  # Package and pinned CPU dependencies
```

## Deadlines and milestones

Dates are in **2026**. The latest collection and showcase requirements take planning priority.
Earlier prototype targets need explicit reconciliation with the new collection-first sequence.
For the course report and presentation, follow the [end-of-semester checklist](docs/course-endgame-2026-11.md).
The Blackboard due-date field and one announcement specify **24 November, 5:00 pm UTC+4**;
a later notice says **27 November**. Use the earlier Blackboard cutoff until the coordinator
confirms otherwise. Prepare for presentations on **27 November, 8:00 am–12:00 pm**, with
20 minutes plus 10 minutes of Q&A, unless your supervisor assigns another slot.

| Date | Deliverable |
|---|---|
| Before proposed **29 September** start | Confirm the consolidated schedule, catalogue assignments and first-day guidance; obtain remaining protocol/QC instructions |
| **29 September–1 October / 6–8 October**, proposed | Two collection weeks; ten sessions, pending lab acceptance and Session A/B mapping |
| **Wednesday 21 October, 14:00-17:00** | Secure Life Group CEO visit: required presence, SDP digital progress poster; Divya lab preparation, Hardik/Fangzhou video; earlier GUI obligation retained |
| **30 Sep / 14 Oct / 17 Oct** | Poster invitation / accepted-poster final / screen-format revision delivery stages; acceptance and revised-file receipt documented, TDRA pending |
| **Tuesday 20 October** | Team poster day confirmed; continuous coverage requested, exact session/setup and 2 pm photo day to confirm |
| Historical **15 October** | Batch 1 collection milestone; completion unverified. Hardik's separate colorization phase 1 retains this deadline |
| **30 November** | Latest overall collection deadline (F06); second-round schedule requested, first-round shortfalls completed before next set |
| After usable Batch 1 | Adapt, train and evaluate the available distributed model; exact dates TBD |
| After midterms; dates TBD | Second two-week collection batch, then retraining and comparison |
| Historical **8 / 15 October** | Original P1/P2 targets: retain as recorded obligations, but reconcile with the new sequence; no replacement dates supplied |

Open dependencies: conflicting Mobile/Pager labels, four duplicate image pairs across the supplied
train/test split, physical-group provenance and P2 case labels. Preserve the published test split.
The catalogue supplies a **500-image Round 1 target**. Annotation taxonomy, QC and negative/control
coverage still need confirmation; the matching count alone does not satisfy the proposal's
**500 positive/negative samples** requirement. Remaining full-GUI scope and departmental dates
also need confirmation. The simple showcase GUI is required now.
See the [paper/annotation review](docs/iedxray-paper-review.md).

## Run the GUI

Clone **[RayGuard-App](https://github.com/abdalrahman-ismaik/RayGuard-App)** with
`--recurse-submodules` and follow its README. Its Windows entry point is
`run-app.ps1`. GUI source and launcher changes belong in that repository;
research/model changes belong here. Authorized datasets and checkpoints stay local.

## Run the CPU tools

Install Git, Python and [uv](https://docs.astral.sh/uv/). Python **3.12** was tested locally.
From the repository root:

```text
uv sync --locked
uv run --locked python -m sdp_xray.cli doctor
uv run --locked python -m sdp_xray.cli audit-coco tests/fixtures/synthetic_coco.json
uv run --locked ruff check .
uv run --locked python -m pytest
```

Copy [the example config](configs/project.example.json) to `configs/project.local.json` for
local artifact paths; paths are relative to the config file. The CPU environment does not install
the detector backend. Follow the separate [inference setup](docs/first-inference.md) for YOLO.
Keep datasets, weights, credentials, source PDFs, local configuration and generated runs outside Git.

## Research sources

- **IEDXray:** [benchmark paper](https://doi.org/10.1038/s41597-026-07263-7), [dataset](https://doi.org/10.6084/m9.figshare.30784328), [author code](https://github.com/Natnael-gh/IEDXray).
- **YOLOv10:** [original implementation](https://github.com/THU-MIG/yolov10); supplied task checkpoints are documented in the [model catalog](docs/checkpoint-catalog.md).
- **FALCON:** [component-reasoning paper](https://arxiv.org/abs/2606.25701v2), relevant to P2 research; it does not provide cross-bag grouping by itself.

## Upcoming publication opportunities

The completed 6G MENA participation and expired calls have been removed from this active list.
See the [conference opportunity register](docs/conferences-2026-2027.md) for current UAE
paper calls, deadlines, fit, publication caveats and the two invitations shared with the team.
The strongest later local student route identified is Zayed University's SRC 2027; its paper
window is **15 December 2026–18 January 2027**. ISDIA and ICISAS deadlines fall on
**15 November 2026** and should be considered only if a complete, defensible paper is already
ready and the team confirms the relevant publication and AI-use rules.
