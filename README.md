# SDP-I-RayGuard

**AI-Powered Explosive Detection in X-ray Scans** — a Khalifa University Senior Design Project.
Advisor: **Prof. Naoufel Werghi**. Technical guidance: **Dr. Divya Velayudhan**.

RayGuard investigates how X-ray evidence of suspicious components can be combined across
separate bags or packages. Following the **24 September meeting**, the main priority is the
distributed dismantled dataset and model adaptation. An early single-scan laptop GUI supports
the **Embedded Explosive Detection in Electronic Devices** showcase. The executed detector
baseline is **IEDXray + YOLOv10-M**; STCray and extra detectors remain optional.

**Collection deadline: 15 October 2026.** All five students must coordinate one schedule for
Dr. Divya: five sessions per week, repeated unchanged for two consecutive weeks, **ten sessions
total**, approximately two hours per student each week. The team proposes **29 September–1 October**
and **6–8 October**, pending lab acceptance. Yonathan's received catalogue specifies
**500 planned images across 125 four-bag groups**; see the [collection table](#dataset-collection--round-1).

> [!IMPORTANT]
> **6G MENA 2026: SDP project poster due 30 September 2026.**
> The advisor requires participation as a project KPI. The summit takes place **19–20 October**
> at **Conrad Abu Dhabi Etihad Towers**. The poster deadline comes from the project invitation;
> attendee registration is a separate action with no confirmed cutoff.
> **All five students are registered**, confirmed by the owner on 28 September; receipts remain private.
> The poster and simple GUI are also needed **ASAP for
> the SLG visit**; the visit date is awaiting confirmation.
>
> **[Conference & agenda](https://6g-mena.com/#agenda)** · **[Official event details](https://eu-ems.com/summary.asp?event_id=4979&page_id=16881)** · **[Register](https://eu-ems.com/register.asp?event_id=4979)** · **[Poster requirements & team checklist](docs/6g-mena-2026.md)**

## RayGuard application

The GUI is maintained separately in **[RayGuard-App](https://github.com/abdalrahman-ismaik/RayGuard-App)**,
with its own launcher, frontend/API, tests and documentation. Abd Alrahman Basim Ismaik
directs and maintains the application; its [credits](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/CREDITS.md)
distinguish app development assistance, team research and published models/data.
This repository remains the SDP research and shared inference source. The app pins a
specific revision of those tools; teammates should use its documented release/setup.

## Current progress

As of **28 September 2026**, CPU dataset audits, shared JSON interfaces and three
inspected YOLOv10 task runners are implemented. The separate application supports
upload/folder intake, finite IEDXray test replay, actual boxes and reference
comparison, operator review, export and CPU/GPU selection. See the
[app guide](https://github.com/abdalrahman-ismaik/RayGuard-App).

Bounded real CPU/GPU runs establish execution compatibility, including known
misses; they do not establish accuracy. Synthetic software checks and real
inference evidence are recorded separately in [verification](docs/verification.md),
[baseline evidence](docs/first-inference.md) and [data audits](docs/iedxray-audit.md).
The scanner connection, intended lab model pairing and human showcase rehearsal
remain unverified. Full P1 association/decisions, P2 fusion, fine-tuning and model
evaluation remain unfinished. Empty detections never establish a benign scan.

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

**Collection status: not started; no acquired scans reported.** These are catalogue targets,
not completed images. The five clutter levels each cover 100 planned images. Set numbers
restart for each student/session, so a set label alone does not uniquely identify a group.

Lab confirmation is still needed for the proposed dates, Session A/B mapping to weeks,
and replacement of the earlier one-item weekly assignments: the catalogue covers all four
families per student and includes E4/B3 in Round 1. Scanner/export instructions, annotation
rules, QC and negative/control examples remain open. The **15 October** deadline is unchanged.
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

**Immediate priorities:** confirm the proposed collection schedule, reconcile the received
catalogue with earlier assignments, obtain the remaining lab protocol and assign GUI/poster owners.
All five student registrations are reported complete. Published-dataset inspection
does not complete the new collection requirement; no new SDP lab scans have been reported.

| Workstream | Goal and immediate tasks | Start here |
|---|---|---|
| **Five-student team — collection and distributed model** | Complete Batch 1 by 15 October with real case/component labels. Inspect the lab's available model early, then adapt/train/evaluate after Batch 1. Collect a broader two-week batch after midterms and retrain. | [P2 interface](src/sdp_xray/p2/__init__.py), [shared contracts](docs/contracts.md), [architecture](docs/architecture.md) |
| **Single-scan / GUI showcase** | Review the working generic-detector GUI, confirm the intended lab laptop/pager pairing, assign a human owner and rehearse alongside the poster. Full P1 device/region/decision work remains separate. | [GUI setup](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md), [app architecture](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/architecture.md), [model notes](models/README.md), [poster checklist](docs/6g-mena-2026.md) |
| **Hardik — colorization** | Collect colorization data and complete phase 1 by 15 October; separately register for 6G and prepare its video. Interface to detection and video deadline need confirmation. | Coordinate with the lab; no colorization implementation in this repository |

The P1/P2 interfaces are explicit stubs. Model, GUI and integration leads still need naming;
module names do not assign students. Both modules share `common/` and `data/`; merge small changes into `main` from
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

| Date | Deliverable |
|---|---|
| Before proposed **29 September** start | Confirm the consolidated schedule, catalogue assignments and first-day guidance; obtain remaining protocol/QC instructions |
| **29 September–1 October / 6–8 October**, proposed | Two collection weeks; ten sessions, pending lab acceptance and Session A/B mapping |
| ASAP; SLG visit date TBD | Poster on **Embedded Explosive Detection in Electronic Devices**, with simple GUI/laptop demonstration |
| **30 September** | **[6G MENA poster submission](docs/6g-mena-2026.md)** (deadline supplied in the project invitation) |
| **15 October** | **Batch 1 distributed dataset collection complete:** ten sessions over two consecutive weeks; Hardik's separate colorization phase 1 also due |
| After usable Batch 1 | Adapt, train and evaluate the available distributed model; exact dates TBD |
| **19–20 October** | **6G MENA Summit, Abu Dhabi**; attendance/presentation confirmation pending |
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

## UAE conferences and events

**Required project priority:** [6G MENA poster and registration](docs/6g-mena-2026.md), checked
24 September 2026. The other entries are optional opportunities checked on 23 September.

| Conference / event | When and where | Possible route |
|---|---|---|
| [6G MENA 2026](https://eu-ems.com/summary.asp?event_id=4979&page_id=16881) | **19–20 October 2026**, Conrad Abu Dhabi Etihad Towers | SDP poster requested; submission **30 September** per invitation. [Attendee registration](https://eu-ems.com/register.asp?event_id=4979) is separate from poster submission. |
| [CAISAIS 2026](https://caisais26.ajman.ac.ae/en/home) | **25–27 November 2026**, Ajman University | Research paper in AI/computer vision/security; extended submission deadline **30 September 2026**. |
| [MoSICom 2026](https://mosicom2026.com/) | **7–9 December 2026**, BITS Pilani Dubai Campus | Research paper in intelligent computing/image processing; [extended submission deadline](https://mosicom2026.com/important-dates) **15 October 2026**. |
| [GITEX GLOBAL 2026](https://www.gitex.com/conference-overview) | Expo **8–11 December 2026**, Expo City Dubai; summit **7 December**, DWTC | Technology exhibition/networking; investigate a university demo route. No research-paper submission route identified. |
| [Intersec Global 2027](https://intersecglobal.ae.messefrankfurt.com/dubai/en/planning-preparation.html) | **12–14 January 2027**, Dubai World Trade Centre | Security exhibition/networking; visitor or exhibitor route. No research-paper submission route identified. |

Prioritize collection and the GUI/poster. Additional papers remain optional; MoSICom's deadline
coincides with the required first collection batch. Submit research only with suitable results and capacity.
