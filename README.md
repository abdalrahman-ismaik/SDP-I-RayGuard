# SDP-I-RayGuard

**AI-Powered Explosive Detection in X-ray Scans** — a Khalifa University Senior Design Project.
Advisor: **Prof. Naoufel Werghi**. Technical guidance: **Dr. Divya Velayudhan**.

RayGuard investigates how X-ray evidence of suspicious components can be combined across
separate bags or packages. Following the **24 September meeting**, the main priority is the
distributed dismantled dataset and model adaptation. An early single-scan laptop GUI will
showcase **Embedded Explosive Detection in Electronic Devices**. The executed detector
baseline is **IEDXray + YOLOv10-M**; STCray and extra detectors remain optional.

**Collection deadline: 15 October 2026.** All five students must coordinate one schedule for
Dr. Divya: five sessions per week, repeated unchanged for two consecutive weeks, **ten sessions
total**, approximately two hours per student each week. Actual dates and lab slots are pending.

> [!IMPORTANT]
> **6G MENA 2026: SDP project poster due 30 September 2026.**
> The advisor requires participation as a project KPI. The summit takes place **19–20 October**
> at **Conrad Abu Dhabi Etihad Towers**. The poster deadline comes from the project invitation;
> attendee registration is a separate action with no confirmed cutoff.
> **All five students must register.** The poster and simple GUI are also needed **ASAP for
> the SLG visit**; the visit date is awaiting confirmation.
>
> **[Conference & agenda](https://6g-mena.com/#agenda)** · **[Official event details](https://eu-ems.com/summary.asp?event_id=4979&page_id=16881)** · **[Register](https://eu-ems.com/register.asp?event_id=4979)** · **[Poster requirements & team checklist](docs/6g-mena-2026.md)**

## Current progress

As of **24 September 2026**, CPU dataset-audit tools, shared JSON interfaces and a standalone
generic-threat detector are implemented. The detector has produced real predictions on three
diagnostic images, including a missed threat; these runs do not establish accuracy.
Device inference, the complete P1 pipeline, P2 fusion, fine-tuning, model evaluation and GUI
remain unfinished. Empty detections do not establish that a scan is benign.

See [baseline commands/results](docs/first-inference.md) and [IEDXray audit findings](docs/iedxray-audit.md).
The latest software checks passed **85 tests** in a copy containing only public project files;
these are separate from real-data inspection and model inference.

## Joining the project

Start with the [team documentation index](docs/README.md) and [contribution/setup guide](CONTRIBUTING.md).
Read [current status](docs/status.md), choose an agreed task from the [shared backlog](docs/tasks.md),
then consult the [requirements](docs/context.md), [plan](docs/plan.md) and
[latest meeting summaries](docs/meeting_minutes/README.md). Everyone uses these same records;
cloning the repository does not grant access to datasets, weights or private lab documents.
For agent-assisted work, use the shared [AGENTS.md](AGENTS.md) and
[four project skills](CONTRIBUTING.md#working-with-agents). Personal client settings stay local.

## Workstreams and their next tasks

**Immediate priorities:** send the complete repeated collection schedule, confirm the lab
protocol, assign GUI/poster owners and register all five students. Published-dataset inspection
does not complete the new collection requirement; no new SDP lab scans have been reported.

| Workstream | Goal and immediate tasks | Start here |
|---|---|---|
| **Five-student team — collection and distributed model** | Complete Batch 1 by 15 October with real case/component labels. Inspect the lab's available model early, then adapt/train/evaluate after Batch 1. Collect a broader two-week batch after midterms and retrain. | [P2 interface](src/sdp_xray/p2/__init__.py), [shared contracts](docs/contracts.md), [architecture](docs/architecture.md) |
| **Single-scan / GUI showcase** | Confirm the intended ready laptop/pager model, assign a GUI owner and prepare a runnable laptop demonstration alongside the poster. Full P1 device/region/decision work remains separate and unfinished. | [P1 interface](src/sdp_xray/p1/__init__.py), [generic runner](scripts/infer_generic_yolov10.py), [model notes](models/README.md), [poster checklist](docs/6g-mena-2026.md) |
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
├── scripts/                # Standalone generic YOLO inference
├── configs/                # Portable configuration example
├── tests/                  # Synthetic software tests
├── docs/                   # Shared status, tasks, requirements, plan and evidence
│   ├── README.md           # Documentation index and reading order
│   ├── meeting_minutes/    # Reviewed Markdown summaries; original PDFs excluded
│   └── templates/          # Blank collection schedule and sample manifest
├── data/ & models/         # Usage notes; actual artifacts stay local
├── .github/workflows/      # CPU CI definition
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
| Earliest opportunity | One consolidated schedule for all five students; lab protocol, owners and registrations |
| ASAP; SLG visit date TBD | Poster on **Embedded Explosive Detection in Electronic Devices**, with simple GUI/laptop demonstration |
| **30 September** | **[6G MENA poster submission](docs/6g-mena-2026.md)** (deadline supplied in the project invitation) |
| **15 October** | **Batch 1 distributed dataset collection complete:** ten sessions over two consecutive weeks; Hardik's separate colorization phase 1 also due |
| After usable Batch 1 | Adapt, train and evaluate the available distributed model; exact dates TBD |
| **19–20 October** | **6G MENA Summit, Abu Dhabi**; attendance/presentation confirmation pending |
| After midterms; dates TBD | Second two-week collection batch, then retraining and comparison |
| Historical **8 / 15 October** | Original P1/P2 targets: retain as recorded obligations, but reconcile with the new sequence; no replacement dates supplied |

Open dependencies: conflicting Mobile/Pager labels, four duplicate image pairs across the supplied
train/test split, physical-group provenance and P2 case labels. Preserve the published test split.
The lab collection quota/taxonomy, proposal's **500-sample** obligation, remaining full-GUI
scope and departmental dates need confirmation. The simple showcase GUI is required now.
See the [paper/annotation review](docs/iedxray-paper-review.md).

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
