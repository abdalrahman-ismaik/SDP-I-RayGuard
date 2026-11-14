# Team documentation

This is the shared starting point for everyone working on RayGuard. Requirements, task status
and technical evidence live in this repository so a new clone has the same project context.

The GUI source and app-specific guides are in [RayGuard-App](https://github.com/abdalrahman-ismaik/RayGuard-App).
Clone it with `--recurse-submodules`; its `engine/` pins this research repository.
GUI contributions go there, while the research backlog and meeting requirements
stay here. See the [migration evidence](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/migration.md).

The root [.gitignore](../.gitignore) excludes legacy app/media/launcher files and
accidental copies of the separate app. Shared inference tools remain tracked in
this repository. App implementation documentation belongs in RayGuard-App; this
index links there while team status, progress and the sole backlog stay here.

## Start here

For the November report, GitHub evidence, individual assessment, demo and presentation, use the [end-of-semester course checklist](course-endgame-2026-11.md).

1. Read [current status](status.md) and the active item in [tasks](tasks.md).
2. Read [requirements and open decisions](context.md), the [latest meeting records](meeting_minutes/README.md)
   and the relevant part of the [plan](plan.md).
3. Follow [contribution/setup instructions](../CONTRIBUTING.md); when using an agent, also
   read [shared agent instructions](../AGENTS.md) and the relevant
   [project skill](../CONTRIBUTING.md#working-with-agents).
4. Read the [architecture](architecture.md), [shared contracts](contracts.md) and the evidence
   relevant to your task before changing behavior.

Use the same reading order when handing a task to another contributor or development tool.
Do not rely on a previous conversation as the only record of a requirement or completed action.

## Which document owns which information?

| Document | Purpose; update when |
|---|---|
| [status.md](status.md) | Short handoff: what works, current priorities and blockers; update after a material result |
| [tasks.md](tasks.md) | **The only backlog**: stable task IDs, owner/reviewer, dependencies, state and acceptance evidence |
| [plan.md](plan.md) | Sequencing and capacity assumptions; update when dates or dependencies change |
| [implementation/demo sprint plan](implementation-plan-demo-2026-11.md) | Proposed individual work packages, demo gates, AI workflow and November schedule |
| [context.md](context.md) | Agreed requirements, source precedence and questions; update when an authoritative answer arrives |
| [decisions.md](decisions.md) | Dated design/scope choices and explicitly superseded choices |
| [meeting_minutes/](meeting_minutes/README.md) | Reviewed Markdown records and source references; originals are retained privately |
| [progress.md](progress.md) | Shareable engineering results and future verified contributions; no invented authorship/hours |
| [verification.md](verification.md) | Recorded software, data-audit and inference checks with their limits |

Keep one current record per purpose. A personal note is not a second backlog or an amendment
to the agreed requirements. Name unresolved owners as TBD until someone accepts responsibility.

## Technical references

| Task area | Read |
|---|---|
| Model execution / GUI baseline | [First inference](first-inference.md), [single-scan training/evaluation plan](single-scan-ml-pipeline-plan-2026-11.md), [model catalog](checkpoint-catalog.md), [model selection/classes and execution](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/model-selection.md), [model storage/setup](../models/README.md), [GPU inference study and plan](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/gpu-inference-plan.md), [GPU implementation prompt](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/gpu-implementation-prompt.md) |
| GUI implementation and rehearsal | [App launch/development](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md), [app architecture/options](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/architecture.md), [airport UI/scanner research](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/scanner-research.md), [design/font comparison](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/visual-research.md), [workspace choices](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/design-options.md), [actual checks](verification.md) |
| IEDXray reference in the GUI | [Annotation pairing, overlay and matching protocol](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/annotation-comparison.md); per-image agreement is separate from accuracy |
| Data collection and audits | [Data handling](../data/README.md), [distributed collection inventory](collection-progress-2026-11-14.md), [member contribution guide](collection-contribution-guide.md), [IEDXray audit](iedxray-audit.md), [paper/annotation review](iedxray-paper-review.md) |
| Model research and selection | [Research findings](research.md), [dataset catalog](datasets.md); optional [STCray audit](stcray-audit.md) |
| Interfaces and integration | [Architecture](architecture.md), [contracts](contracts.md), [baseline run contract](baseline-run-contract.md) |
| Conference, poster and GUI showcase | [Secure Life Group visit requirements](meeting_minutes/follow-up-slg-2026-10-19.md); [Acceptance/digital revision and Tuesday participation](meeting_minutes/follow-up-poster-2026-10-19.md); [Current v6 PPTX/PDF review bundle](posters/6g-mena-2026/README.md), [6G MENA requirements/checklist](6g-mena-2026.md), [poster preparation and evidence](poster-plan.md) |
| New collection paperwork | [Latest count/schedule requirements](meeting_minutes/follow-up-collection-2026-10-19.md); blank [schedule](templates/collection-schedule.md) and [sample manifest](templates/collection-manifest.csv) |

## What belongs in Git?

| Keep in the shared repository | Keep private / ignored |
|---|---|
| Current plan, backlog, requirements, decisions, technical evidence and owner-authorized poster review bundle | Raw correspondence, personal notes, detailed session/recovery journals |
| Reviewed meeting Markdown without student IDs or contact details | Original minutes/proposal/selection PDFs and documents |
| Code, meaningful synthetic tests, lock file and portable example config | Scans, annotation releases, checkpoints, environments and generated run outputs |
| Blank reusable templates and concise reviewed results | Filled availability schedules, attendance/contact details and registration confirmations |
| Commands, relative paths, model/source hashes and explicit limitations | Credentials, expiring access links, personal absolute paths and local configuration |
| Reviewed root agent guidance and four project skills | Personal client settings, sessions, local overrides and unrelated skills |

Copy templates to an ignored private location before filling personal details. Share restricted
artifacts through an authorized team/lab channel, not through commits. The repository's public
visibility means every tracked document can be read beyond the five-student team.

The shared Markdown is sufficient for planning, CPU development and understanding the evidence.
Original source documents or lab instructions must still be obtained through the team when
source review or acquisition requires them; model/data access is not granted by cloning code.
