# SDP-I-RayGuard

**AI-Powered Explosive Detection in X-ray Scans** — a Khalifa University Senior Design Project.
Advisor: **Prof. Naoufel Werghi**. Technical guidance: **Dr. Divya Velayudhan**.

RayGuard aims to identify electronic devices and suspicious modifications in baggage X-rays,
then investigate how component evidence can be combined across related scans or bags.
The current detector baseline is **IEDXray + YOLOv10-M**. Initial lab dataset collection is a
separate priority. STCray and additional detectors are optional later work.

> [!IMPORTANT]
> **6G MENA 2026: SDP project poster due 30 September 2026.**
> The advisor requires participation as a project KPI. The summit takes place **19–20 October**
> at **Conrad Abu Dhabi Etihad Towers**. The poster deadline comes from the project invitation;
> attendee registration is a separate action with no confirmed cutoff.
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

## Two teams and their next tasks

**Immediate shared priorities:** agree and carry out the initial dataset collection, report
progress to the advisor, register for 6G MENA and prepare the SDP poster for **30 September**.
Published-dataset inspection does not establish completion of the collection requirement.

| Workstream | Goal and immediate tasks | Start here |
|---|---|---|
| **Team 1 — Prototype 1** | One scan: classify devices, locate suspicious regions and distinguish benign/modified devices. Next: run the device checkpoint, agree region association and decision rules, integrate, fine-tune and evaluate. | [P1 interface](src/sdp_xray/p1/__init__.py), [working generic runner](scripts/infer_generic_yolov10.py), [model notes](models/README.md) |
| **Team 2 — Prototype 2** | Combine component evidence across related scans/bags and compare late fusion with an end-to-end approach. Next: confirm ownership, obtain genuine case/group labels and component evidence, then implement and evaluate fusion. | [P2 interface](src/sdp_xray/p2/__init__.py), [shared contracts](docs/contracts.md), [architecture](docs/architecture.md) |

The P1/P2 interfaces are currently explicit stubs. Team membership and P2 leadership still need
confirmation. Both teams share `common/` and `data/`; merge small changes into `main` from
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
├── docs/                   # Architecture, contracts and technical evidence
├── data/ & models/         # Usage notes; actual artifacts stay local
├── .github/workflows/      # CPU CI definition
└── pyproject.toml, uv.lock  # Package and pinned CPU dependencies
```

## Deadlines and milestones

Dates are in **2026**. Prototype deadlines are recorded advisor requirements; intermediate
dates are working targets, dependent on data clarification and compute availability.

| Date | Deliverable |
|---|---|
| Earliest availability | Advisor follow-up: initial collection scope, named lead, lab session and first deliverable |
| 25 September | P1 decision rules and data/evaluation policy; P2 owner and grouping feasibility |
| 24–29 September | Device inference and P1 integration alongside collection; poster draft and advisor review |
| **30 September** | **[6G MENA poster submission](docs/6g-mena-2026.md)** (deadline supplied in the project invitation) |
| 3–7 October | Bounded fine-tuning, evaluation, failure analysis and demo rehearsal |
| **8 October** | **Prototype 1 demonstration** |
| 9–14 October | P2 evaluation, integration and rehearsal |
| **15 October** | **Prototype 2 demonstration** |
| **19–20 October** | **6G MENA Summit, Abu Dhabi**; attendance/presentation confirmation pending |

Open dependencies: conflicting Mobile/Pager labels, four duplicate image pairs across the supplied
train/test split, physical-group provenance and P2 case labels. Preserve the published test split.
The timing of the proposal's **500-sample** requirement and full GUI, plus any earlier departmental
submission, still needs confirmation. See the [paper/annotation review](docs/iedxray-paper-review.md).

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

Prioritize initial collection, the 6G poster and the prototype deadlines. CAISAIS closes before
P1, and MoSICom closes on the P2 deadline; consider additional papers only when results and capacity allow.
