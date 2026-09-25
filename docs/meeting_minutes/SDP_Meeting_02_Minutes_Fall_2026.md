# Meeting 02 — Second advisor meeting, 24 September 2026

Shared, sanitized companion to the private source `SDP_Meeting_02_Minutes_Fall_2026.pdf`.
Read alongside the [meeting-record index](README.md) and the separately attributed
[follow-up action record](follow-up-2026-09-24.md).

This companion records what the minutes say; it does not establish that collection, model
adaptation, registration, GUI delivery or action completion occurred. Later follow-up instructions
are distinguished below. The original PDF remains the source record and is not distributed
in the repository. Request an authorized copy from the project team when needed. Student IDs,
contact information and private meeting logistics are omitted from this summary.

| Record field | Value |
|---|---|
| Project / course | AI-Powered Explosive Detection in X-ray Scans / Senior Design Project 1 |
| Meeting | Second advisor meeting |
| Date | 24 September 2026 |
| Advisor / main speaker | Prof. Naoufel Werghi |
| Technical input | Dr. Divya Velayudhan |
| Additional attendee | Hardik; surname and formal role not supplied |
| Prepared by | Abd Alrahman Ismaik |
| Attendance status | All five student members present, according to the record; attendance confirmed by Abd Alrahman Ismaik |
| Source length | Nine PDF pages: cover is PDF p. 1; printed pp. 1–8 are PDF pp. 2–9 |
| Source SHA-256 | `12a14d16f0eb3fdf8faacc27a8acb0c9140082ea62940a03718c6bca9c9c010f` |
| Evidence level | Documented meeting directions; source PDF inspected and hash verified |

## Outcome and agreed direction

Source: PDF p. 2 / printed p. 1.

Prioritize a new lab-collected dataset for multi-package IED detection: correlate component
evidence across separate bags or packages. Coordinate five scanning sessions per week,
approximately one two-hour session per student each week, for an initial two-week campaign.
The recorded first-batch target is **15 October 2026**. Adapt the existing model once sufficient
data are available, then undertake a broader two-week collection batch after midterms and retrain.

The team should send one consolidated rota to the advisor/lab team, follow the CVMI scanning
protocol and maintain a shared attendance list. Available PhD/lab support should assist model
adaptation and training. Hardik continues recolorization while the five students concentrate
on their assigned scanning and model work. Use the shared GitHub repository for code and
relevant project materials.

In parallel, prepare an IED-detection poster and a simple laptop GUI/live demonstration using
the laptop/pager IED model described as ready in the meeting. Register for the 6G event as
soon as possible. **The meeting's readiness statement is a reported claim, not local execution
verification or evidence that the multi-package system is complete.**

## Decisions D1–D8

Source: PDF p. 3 / printed p. 2. The last column reproduces the PDF's printed cross-references;
some do not match its later Action Register.

| ID | Recorded decision and implication | Actions printed in decision table |
|---|---|---|
| D1 | Primary technical priority: multi-package IED detection and data needed to correlate components across separate packages. | A1–A8 |
| D2 | Five-session weekly rota: approximately one scanning session per student per week; coordinate before emailing it. | A1–A2 |
| D3 | Two-hour commitment: approximately two hours per student per week during initial collection. | A4–A5 |
| D4 | First dataset milestone: target completion of the first batch by 15 October 2026. | A4–A8 |
| D5 | Second collection batch: two more weeks after midterms, with broader scenarios, followed by retraining for generalization. | A10 |
| D6 | Existing-model path: adapt and retrain the available model rather than build the multi-package model entirely from zero. | A7–A8 |
| D7 | Live demonstration: simple laptop GUI for the laptop/pager IED model described as ready; prioritize a working demonstration. | A9, A14 |
| D8 | 6G event participation: register promptly, start with an IED-detection poster and add a laptop demonstration if ready. | A12–A15 |

**Cross-reference discrepancy:** use the **Action Register on PDF p. 7 / printed p. 6** below
as authoritative for action IDs, owners and targets. In that register A7–A8 concern the
recolorization workstream, while model adaptation is A9; GUI development is A12, registration
A13, poster A14, live demonstration A15 and event verification A16. Thus D6's and D7's printed
links do not identify their corresponding implementation actions, and the broader ranges
should not replace the register. The printed references are preserved here rather than silently
renumbered.

## Technical scope and limits

Sources: PDF pp. 3–4 / printed pp. 2–3.

The core scenario is an IED whose component evidence is distributed across separate packages.
Individual components may appear ordinary in isolation, motivating cross-package correlation.
The discussed starting components are **detonator, explosive material, and wires/connectors**.
This is a proposed starting set **subject to a standardized lab taxonomy**, not approved class
IDs or a completed annotation specification.

| Element | Recorded system implication |
|---|---|
| Detonator | Retain potentially weak component evidence for later cross-package fusion. |
| Explosive material | Associate evidence with other scans before deciding. |
| Wires / connectors | Consider component combinations rather than a single-object rule. |
| Multiple packages | Define case grouping and evidence fusion explicitly. |

Three packages were an example, **not a permanent input limit**. The number of scans per case,
fusion architecture and association method remain open. Dismantled or 3D-printed firearms
were discussed as an analogy or optional future variant, not a committed deliverable.

The recorded workflow is: lab protocol and packing scenarios → five-student collection →
quality review of counts, labels, diversity and usable images → adaptation of the available
PhD-developed model → Batch 1 training/evaluation with recorded errors → repeat after Batch 2.
No model version, grouping schema, evaluation metrics or implementation results are established
by this workflow description.

Recolorization is a separate workstream. The meeting reports that Hardik had begun its data
collection and would continue through 15 October. Its objective, protocol, outputs and interface
with multi-package detection still need documentation. Reported activity is not independently
verified collection evidence.

## Collection plan and milestones

Sources: PDF pp. 3, 5–6 / printed pp. 2, 4–5.

| Item | Recorded plan / limit |
|---|---|
| Participants | All five student members; record attendance and completed sessions. |
| Cadence | Five sessions each week, approximately one session per student. |
| Effort | Approximately two hours per student per week; additional time welcome, not required. |
| Initial campaign | Two active collection weeks; exact dates and possible session overlap unresolved. |
| Planned session total | Five sessions × two weeks implies ten planned sessions; the later email explicitly confirms ten and repetition of the same weekly rota. This is not a count of completed sessions. |
| Batch 1 target | **15 October 2026**; retain the written date pending rota confirmation. |
| Protocol | Advisor/lab team to provide scanning protocol and packing scenarios before scanning. |
| Quota | **No final image quota fixed.** Review throughput and quality; obtain an agreed acceptance rule. |
| Batch 1 review | Record completed collection, counts and quality review before adaptation/training acceptance. |
| After Batch 1 | Adapt, train, test and document the existing model for the new task. |
| Batch 2 | Two weeks of broader, more diverse collection after midterms, then retrain and compare with Batch 1; exact dates and metrics unresolved. |

The source mentions **20 threat items, 20 scans per student and at least 200 detonator examples**,
but expressly says no final image count was set. These are discussion figures requiring
clarification, **not fixed quotas or acceptance criteria**.

The source also flags a scheduling inconsistency: 15 October is three weeks after the
24 September meeting, while the campaign is described as two weeks. Do not invent a start date
or stretch the active campaign to three weeks; confirm the two active weeks in the rota.

### Rota as recorded at the meeting

PDF p. 6 / printed p. 5 says no individual day/time was assigned. The worksheet lists:

| Student | Lab day/time in meeting record | Planned duration | Status in record |
|---|---|---|---|
| Abd Alrahman Ismaik | TBC | Approx. 2 hours/week | To schedule |
| Faisal Daoud Alzarooni | TBC | Approx. 2 hours/week | To schedule |
| Ali Arif Saeed Alshamsi | TBC | Approx. 2 hours/week | To schedule |
| Mohammad Arwani | TBC | Approx. 2 hours/week | To schedule |
| Ahmed Almansoori | TBC | Approx. 2 hours/week | To schedule |

Agree one consolidated schedule, resolve lab conflicts and send it before the first session.
The [later email](follow-up-2026-09-24.md) adds the requirement to repeat the same weekly rota.

## GUI, poster, event and supplier visit

Sources: PDF pp. 4, 6 / printed pp. 3, 5.

- Assign an owner and build an early runnable GUI for the laptop/pager IED model described as
  ready. This is a near-term showcase path separate from the unfinished multi-package system.
- Package the model, GUI, sample inputs and run procedure for a reliable laptop demonstration.
  A live working result is preferred over a poster-only or prerecorded result.
- Start with an IED-detection poster; verify its format and submission deadline. The exact
  poster title supplied later belongs to the follow-up email, not these minutes.
- Register for the 6G event as soon as possible. The record requests names and student IDs for
  registration; personal identifiers are intentionally omitted from this companion.
- Verify official event title/date, registration and submission routes, equipment/monitor
  availability and demonstration rules. The minutes do not establish completed registration,
  poster acceptance or a confirmed event setup.
- A scanner-supplier visit was discussed as possible in the following week. Visitor identity,
  company, exact date and expected demonstration remain unconfirmed; the advisor is to confirm.

## Action Register A1–A17

Source: **PDF p. 7 / printed p. 6, §6**. This register controls action numbering. TBA means
the meeting did not name the person. Targets are recorded requirements, not completion claims.

| ID | Action / expected deliverable | Responsible as recorded | Target as recorded |
|---|---|---|---|
| A1 | Collect all five students' available lab slots and agree one scanning rota. | Whole team; coordinator TBA | ASAP |
| A2 | Email the consolidated schedule to the advisor/lab team and keep a shared attendance list. | Team liaison TBA | ASAP |
| A3 | Provide scanning protocol and packing scenarios for collection sessions. | Dr. Divya / CVMI Lab team | Before first session |
| A4 | Complete the two-week Batch 1 campaign; confirm exact active dates in the rota. | All five students | By 15 Oct 2026 |
| A5 | Update attendance and record scans completed during each session. | Each student; log owner TBA | Every session |
| A6 | Confirm the final quota and clarify the 20-scan and 200-detonator references. | Advisor/lab team and team liaison | Before acceptance |
| A7 | Document and communicate the split: Hardik continues recolorization; five-student team focuses on multi-package scanning and model work. | Team liaison TBA | Immediate |
| A8 | Continue recolorization collection and document its objective, protocol and output. | Hardik; technical owner TBA | 15 Oct 2026 |
| A9 | Adapt, train, test and document the existing model on Batch 1 multi-package data. | Model subteam TBA; PhD/lab support | After Batch 1 |
| A10 | Complete two-week Batch 2, retrain and compare with Batch 1. | Whole team; model subteam TBA | Collection after midterm; retraining follows |
| A11 | Confirm repository access for everyone and use the existing GitHub repository for shared materials. | Repository creator / whole team | Immediate; ongoing |
| A12 | Assign and build a simple laptop GUI for the laptop/pager IED model described as ready. | GUI owner TBA | As early as possible |
| A13 | Collect team names/IDs and complete 6G event registration. | Registration liaison TBA | ASAP |
| A14 | Prepare the IED-detection poster and verify submission format/deadline. | Whole team; design owner TBA | Before event |
| A15 | Prepare a reliable laptop-based live demonstration for the event or supplier visit. | GUI/model owners and whole team | Before first showcase |
| A16 | Verify official event title, dates, submission route, monitor availability and demonstration rules. | Advisor/event liaison | Immediate |
| A17 | Issue Meeting 02 minutes and actions to advisor and team. | Abd Alrahman Ismaik | Immediately after meeting |

Creating this companion does not establish that A2 or A17 was sent, or that any other action
was completed. Review the register at the next advisor meeting.

## Open questions O1–O10

Source: PDF p. 8 / printed p. 7, §7.1. These describe the open state in the minutes; subsequent
answers should be attributed to their later source.

| ID | Area | Confirmation required | Impact |
|---|---|---|---|
| O1 | Schedule | Exact two-week Batch 1 window; whether sessions may overlap. | Rota and lab capacity |
| O2 | Quota | Meaning of 20 threat items, 20 scans/student and 200 detonator examples. | Acceptance criteria |
| O3 | Workstream handoff | Interface, deliverables and handoff between recolorization and multi-package work. | Integration |
| O4 | Recolorization | Formal objective, inputs/outputs, protocol, labels and success measures. | Workstream definition |
| O5 | Model | Base-model version, support contact, fusion architecture and scan grouping. | Implementation start |
| O6 | Evaluation | Metrics, split, baseline, threshold and error-analysis procedure. | Technical acceptance |
| O7 | GUI | Named owner and minimum interface/demo requirements. | Showcase readiness |
| O8 | 6G event | Official title/date, registration route, poster template and equipment. | External deadline |
| O9 | Supplier visit | Visitor identity, company, date and expected demonstration. | Near-term planning |
| O10 | Batch 2 | Midterm end date and exact collection/retraining window. | Schedule risk |

### Risks and next meeting

Source: PDF p. 8 / printed p. 7, §§7.2–7.3.

| Risk | Recorded practical control |
|---|---|
| Unclear quota | Approve written protocol and acceptance rule before judging completion. |
| Schedule collisions | Use one rota/attendance log and resolve conflicts before sessions. |
| Scope split | Document the boundary between multi-package detection, recolorization and the ready-model GUI demonstration. |
| Data quality | Track scenario, labels, source and usability per scan; review before training. |
| Model delay | Test the existing model and access path before Batch 1 is complete. |
| Event uncertainty | Verify dates/requirements promptly and retain a laptop demonstration fallback. |

Next meeting date, time and venue are TBC. Review A1–A17, approve protocol and rota, check
Batch 1 progress and assign GUI/event owners. The record calls for closing O1–O10 before
dataset acceptance or public presentation; it does not show those questions already resolved.

## Attendance

Source: cover and PDF p. 9 / printed p. 8. All below are marked present. All five students are
listed as Computer Science; their student identifiers are deliberately not reproduced.

| Attendee | Recorded role |
|---|---|
| Prof. Naoufel Werghi | Advisor and main speaker |
| Dr. Divya Velayudhan | Technical input and lab guidance |
| Hardik | Additional technical participant; surname/formal role not supplied |
| Abd Alrahman Ismaik | Student team; minutes preparer |
| Faisal Daoud Alzarooni | Student team |
| Ali Arif Saeed Alshamsi | Student team |
| Mohammad Arwani | Student team |
| Ahmed Almansoori | Student team |

## Follow-up actions and relationship to earlier deadlines

**Separate source:** [Dr. Divya's follow-up action record](follow-up-2026-09-24.md), not a
retroactive addition to the Meeting 02 transcript. It explicitly calls for the same weekly rota
over two weeks, ten sessions in total; registration of all five students; the poster title
**Embedded Explosive Detection in Electronic Devices**; GUI preparation ASAP for SLG; and
Hardik's phase-one deadline of **15 October**. Follow the linked summary for the recorded
requirements and source attribution. These instructions do not establish that the rota, registrations, GUI or
Hardik's work are completed. Do not infer that his phase-one deadline resolves the separate
video deadline or all recolorization deliverables.

Meeting 02 makes multi-package collection the immediate technical priority and records
15 October for Batch 1. It does **not explicitly cancel or reschedule** Meeting 01's
8 October P1 and 15 October P2 prototype dates. Their relationship to this collection/model
sequence needs explicit clarification; retain both sets of recorded milestones. Event/poster
deadlines from other correspondence remain separately sourced in the [record index](README.md).
