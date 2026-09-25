# Meeting records and current requirements

Shared, sanitized requirements summaries, updated 24 September 2026. These Markdown files
give all contributors the same record of agreed directions, open questions and source history.
They omit student IDs, contact information, private meeting logistics and raw correspondence.
Original PDFs and correspondence remain private and are not included in the repository.
Request an authorized source copy from the project team when original-source review is needed.

## Read in this order

1. [Meeting 02 companion](SDP_Meeting_02_Minutes_Fall_2026.md): current technical direction and action register.
2. [Dr. Divya's follow-up](follow-up-2026-09-24.md): explicit collection cadence, registration and showcase requirements.
3. [Meeting 01 companion](<SDP_Meeting_01_Minutes_KU_Styled (1).md>): original scope and obligations not explicitly amended.
4. [Current backlog](../tasks.md), [plan](../plan.md), [context/questions](../context.md) and [short handoff](../status.md).

Each source PDF has a Markdown companion with the same base filename. The companions are
structured summaries, not verbatim transcripts or evidence of action completion. PDF page
references include the cover; printed page 1 is PDF page 2. Prefix source IDs with M01 or M02
because both minutes reuse D/A/O numbering. The original filenames and hashes below identify
the private sources without creating links that fail after cloning the repository.

| Source | Meeting/date evidence | Role |
|---|---|---|
| M01 | 8 September 2026; individual attendance not established | Original P1/P2 scope, 8/15 October targets, governance and proposal alignment |
| M02 | 24 September 2026; all five students present according to the minutes | Collection-first multi-package priority, Batch 1/2, existing-model adaptation and laptop GUI |
| F02 | Dr. Divya's follow-up recorded alongside M02; actual send timestamp not supplied | Same weekly rota for two consecutive weeks, ten sessions, 15 October completion, all-five registration, exact poster topic/GUI/SLG and Hardik tasks |

## How to apply the sources

- Latest explicit agreed directions govern affected work. Preserve earlier obligations unless
  they are explicitly amended; do not treat silence as cancellation.
- Minutes/email establish **recorded requirements**. Paper summaries remain **paper findings**.
  Suggested implementation and scheduling choices are **project recommendations**. Missing
  owners, artifacts, dates and acceptance criteria remain **unresolved questions**.
- A model described as ready in M02 is **documented** availability. It is not proof of an
  inspected checkpoint, matching class map or locally executed GUI. Actual evidence is in
  [first inference](../first-inference.md) and the [checkpoint catalog](../checkpoint-catalog.md).
- Use M02's action register on PDF page 7 for A1–A17; its decision-table action references
  contain inconsistencies described in the companion.

## Amendments and remaining conflicts

| Topic | Current interpretation | Backlog |
|---|---|---|
| Team priority | Five SDP students handle distributed collection/model work; Hardik separately handles colorization. P1/P2 remain software boundaries, not confirmed new staffing assignments | T11, T26, T29, T32 |
| Batch 1 | Five weekly sessions, approximately two hours per student; repeat the same rota for two consecutive weeks, ten sessions total, completed by 15 October | T21, T26, T27 |
| Protocol and quota | Dr. Divya/CVMI supplies protocol and scenarios; quota not finalized. 20 items/20 scans/200 detonator references are not acceptance criteria | T27, Q7 |
| Proposal dataset target | The proposal's 500 total positive/negative samples has not been explicitly waived; reconcile its relationship to batch acceptance | T10, T27 |
| GUI and poster | Embedded Explosive Detection in Electronic Devices, with simple GUI, ready ASAP for SLG visit. Visit date and GUI owner remain unknown | T23, T28, Q8 |
| 6G | All five SDP students register; Hardik registers separately. Prior invitation gives 30 September poster deadline and official event is 19–20 October | T22–T24 |
| Old prototype dates | M01 records P1 8 October and P2 15 October. M02 places adaptation/training after Batch 1; no replacement prototype dates are supplied. Escalate the conflict | T10, T13, Q9 |
| Batch 2 | Another two weeks after midterms, followed by retraining/comparison; dates and metrics remain open | T30 |
| Hardik | Colorization data and phase 1 by 15 October; register and prepare summit video. Video deadline is not specified as 15 October | T24, T32 |

Meeting attendance is now documented; no completed lab collection, sent schedule, registration,
GUI, poster submission or model adaptation follows from that fact. Use the blank
[collection schedule template](../templates/collection-schedule.md) to gather actual availability.
Keep completed availability, attendance and sent-message records in the team's authorized
private workspace; the shared template is not a completed or agreed rota.

## Meeting 02 action coverage

| Source action | Current backlog |
|---|---|
| A1–A2, availability and one schedule email | T26 |
| A3/A5/A6, protocol, log and quota | T27; T21 records each actual session |
| A4, Batch 1 | T21 |
| A7, communicate workstream split | T34; current split recorded in context/plan |
| A8, colorization | T32 |
| A9, model adaptation | T29, supported by T11–T13 |
| A10, Batch 2/retraining | T30 |
| A11, repository access | T31; publication itself already T25 |
| A12/A15, GUI and live demonstration | T28 |
| A13, registration | T22 for five students; F02 separately adds Hardik in T24 |
| A14/A16, poster and event requirements | T23, T22, Q6/Q8 |
| A17, issue minutes | T34; T33 prepares structured reference documents, not evidence of distribution |

## Source integrity

| Source | Private PDF filename | SHA-256 |
|---|---|---|
| M01 | `SDP_Meeting_01_Minutes_KU_Styled (1).pdf` | `99792e279c3ab91a938585c8e338082d2ba45a21c5ae42dd601fc2a20f42b6a7` |
| M02 | `SDP_Meeting_02_Minutes_Fall_2026.pdf` | `12a14d16f0eb3fdf8faacc27a8acb0c9140082ea62940a03718c6bca9c9c010f` |

Source hashes were verified against the supplied PDFs; the original documents were not
rewritten. Reading a summary does not verify a dataset, model or completed action. Later
decisions should name their source and explicitly amend affected requirements rather than
silently rewriting the historical record.
