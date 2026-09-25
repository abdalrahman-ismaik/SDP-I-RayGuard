# Project decisions

Updated **24 September 2026**. Entries distinguish repository choices from recorded advisor
requirements. Decisions describe the intended approach; they do not establish completed work.
Current tasks and ownership are in the [backlog](tasks.md), with evidence in
[verification](verification.md). Original decision IDs are retained from the project record.

## Repository and baseline choices

| ID | Decision and current status | Rationale and limits |
|---|---|---|
| D01 | Use the existing project folder and name, `SDP-I-RayGuard` | Preserve the chosen project identity; no nested repository |
| D02 | One repository with `main` and P1/P2 workstream branches | Share contracts, audit tools and evidence. Merge small verified changes and propagate shared fixes; branch names do not assign students |
| D03 | Small Python CPU package, uv lock, Pillow, pytest and Ruff; separate model environment | Annotation/image checks should not require model or GPU imports. Backend compatibility needs its own verification |
| D04 | YOLOv10-M is the working IEDXray generic-threat reference | Published size/speed motivated the initial choice; genuine CPU smoke inference now exists. This does not select the new distributed model or commit to a broad detector comparison |
| D05 | Establish full-image threat inference before pipeline adaptation | Verify task-compatible execution before introducing coordinate transforms and stage errors. The completed reference does not satisfy full P1 acceptance |
| D06 | Versioned JSON with explicit statuses, original-coordinate boxes and nullable associations | Keep empty detections, missing inputs and errors distinct. Association and benign/modified policies remain explicit dependencies |
| D07 | Keep portable example configuration unassigned; identify synthetic fixtures clearly | Real IEDXray category IDs have now been inspected. Their task namespaces and known disagreements must be handled explicitly; verified physical groups remain unavailable. Unset templates do not imply missing local annotations |
| D08 | Keep source PDFs, scans, weights, private configuration and generated runs outside Git | Share source titles, permitted links and evidence summaries without redistributing sensitive originals or large artifacts |
| D09 | Historical: P1-first allocation, with P2 interface defined before implementation | **Priority superseded by D12.** The shared interface remains useful, but it does not supply component labels, case data or a current staffing assignment |
| D10 | Small root AGENTS.md and four project skills, now shared publicly by explicit repository-owner choice on 24 September | Reusable project guidance in the checkout; no custom orchestration or global configuration changes. Earlier exclusion of these reviewed files is superseded; personal settings, histories, private records and artifacts remain excluded |
| D11 | IEDXray-only working scope for P1; STCray optional and deferred | IEDXray matches the recorded device/modified-region task. STCray adds unresolved geometry/version work without a current P1 requirement. Preserve its audit evidence; revisit only for a justified experiment. This is not the dataset strategy for the whole project |

Full P1 training/evaluation requirements remain distinct from the immediate GUI showcase.
The three diagnostic inference examples are not an accuracy benchmark. Exact model pairing,
data clearance and evaluation policy remain documented dependencies.

## Meeting 02 and follow-up

Source: [meeting records and follow-up](meeting_minutes/README.md). These entries amend
priorities and delivery planning, not measured software or model capabilities.

| ID | Decision / source category | Consequence |
|---|---|---|
| D12 | **Recorded requirement:** all five students prioritize distributed collection/model work; Hardik handles colorization separately | Supersedes D09's P1-first allocation. D11 still limits optional P1 dataset work; new distributed collection is required. Technical/GUI leads remain to be named |
| D13 | **Recorded requirement:** repeat five weekly sessions for two consecutive weeks, ten sessions total; Batch 1 due 15 October; adaptation afterwards; two-week Batch 2 after midterms | Confirm actual slots, lab protocol, taxonomy/grouping and quota. Retain old 8/15 October prototype obligations as historical dates awaiting explicit reconciliation; no replacement dates are assumed |
| D14 | **Recorded requirement:** poster on Embedded Explosive Detection in Electronic Devices, with simple GUI, ASAP for SLG visit | Prepare an early existing-model showcase separately from full P1/P2 acceptance. Exact model pairing, owner and visit date remain open; prior 30 September poster deadline remains |
| D15 | **Documentation choice:** share sanitized Markdown meeting companions, source index and separate follow-up record; keep original PDFs private | Retain source IDs/page references and distinguish later amendments. Omit student IDs and private contact information. Documented model readiness does not imply executed inference or a working GUI |
| D16 | **Documentation choice:** version the canonical team requirements, plan, backlog, progress, research, decisions and verification records | Keep a common reviewable project record. Sensitive originals, detailed private logs and personal scheduling information remain local. Record actual evidence without attributing unverified work to students |

D12–D14 do not waive the proposal's sample target or broader GUI obligations. Hardik's
15 October colorization phase-1 deadline does not establish a video or GUI deadline.
See [context and open questions](context.md) and the [plan](plan.md).
