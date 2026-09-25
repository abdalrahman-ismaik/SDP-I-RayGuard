# Context and source register

Updated 24 September 2026 after Meeting 02 and Dr. Divya's follow-up. Start with the
[meeting index](meeting_minutes/README.md); each source PDF has a structured Markdown companion.
Evidence categories: **recorded requirement**, **paper finding**, **project recommendation**,
**unresolved question**. Implementation evidence remains **documented**, **artifact inspected**
or **executed and verified**. Source claims do not prove that a model or GUI runs locally.

## Latest agreed direction

Meeting 02 occurred **24 September 2026**. Its record confirms all
five students, Prof. Werghi, Dr. Divya and Hardik present. M01 attendance remains unconfirmed.
The new follow-up email's send timestamp was not supplied; its filename records this update.

| Recorded requirement | Source and effect |
|---|---|
| Prioritize distributed/multi-package IED detection and new collection | M02 D1, PDF pp. 2–4; all five students focus on collection and model work; Hardik's colorization is separate |
| One consolidated schedule email to Dr. Divya; same weekly pattern for two consecutive weeks, ten sessions | F02-1/2; M02 A1–A5, PDF p. 7, adds five weekly sessions and approximately two hours per student/week |
| Complete initial distributed dismantled collection by **15 October 2026** | F02-2; M02 calls this Batch 1, with QC/count review and no final image quota |
| Obtain lab protocol/scenarios and record attendance/scans each session | M02 A3/A5; Dr. Divya/CVMI supplies protocol, student log owner remains TBD |
| Adapt/train/evaluate the available model after usable Batch 1; inspect access early | M02 §3.2, A9, risk controls; base-model identity and support contact not established |
| Second two-week collection after midterms, then retraining/comparison | M02 D5/A10; exact window and metrics TBD |
| Simple laptop GUI for the reported-ready laptop/pager model | M02 D7, §3.4, A12/A15; early showcase path, not evidence P1/P2 complete |
| Poster on **Embedded Explosive Detection in Electronic Devices**, with GUI, ASAP for SLG visit | F02-4; visit date, SLG identity and exact demonstration scope unknown |
| All five SDP students register for 6G; Hardik registers and prepares a video separately | F02-3/6; actual confirmations and video deadline unreported |
| Hardik collects colorization data and completes phase 1 by **15 October** | F02-5; M02 reports collection begun, without verified outputs or formal phase-1 acceptance |

The earlier Lina invitation gives **30 September poster submission**; this date is not cancelled
by the ASAP SLG requirement. Official event details were checked on 24 September:
[19–20 October, Conrad Abu Dhabi Etihad Towers](https://eu-ems.com/summary.asp?event_id=4979&page_id=16881);
[attendee registration](https://eu-ems.com/register.asp?event_id=4979). No exact registration cutoff,
poster template/route or SLG date is confirmed. Do not infer a video deadline from either October
15 or September 30. Do not expand the SLG acronym or equate it with the possible supplier visit.

## Source precedence and unresolved schedule conflict

M02/F02 govern current priorities. M01's **8 October P1 / 15 October P2** dates remain historical
recorded obligations because no explicit replacement was provided. Adaptation after Batch 1
conflicts with the old P2-complete-by-15-October plan. T10/Q9 must reconcile the scope and dates;
neither declare the old target fulfilled nor invent a new deadline. Proposed short-term GUI work
is independent of full P1 training and multi-package model readiness.

M02 PDF p. 3's decision-table action references contain mistakes. Use its actual action register
on PDF p. 7 (adaptation A9, GUI A12, live demo A15), as explained in the companion.

## Source register

| Source | Local reference | Relevant evidence |
|---|---|---|
| M01, First Advisor Meeting, 8 September | [Companion](<meeting_minutes/SDP_Meeting_01_Minutes_KU_Styled (1).md>) | PDF pp. 2–7 scope/governance/actions, p. 8 open questions, p. 9 proposal, p. 10 roster |
| M02, Second Advisor Meeting, 24 September | [Companion](meeting_minutes/SDP_Meeting_02_Minutes_Fall_2026.md) | PDF p. 1 logistics, pp. 2–6 decisions/technical/collection/demo, p. 7 A1–A17, p. 8 O1–O10, p. 9 attendance |
| F02, Dr. Divya's Meeting Follow-Up and Action Items | [Email requirements record](meeting_minutes/follow-up-2026-09-24.md) | Team-supplied follow-up; exact cadence, poster/GUI topic and Hardik phase 1 |
| Proposing Senior Design Project Idea Form | SDP-2026- Naoufel Werghi-Project Explosive Detection.pdf | p. 1 broad requirements, p. 2 system, p. 3 resources |
| A Benchmark Dataset for Concealed Improvised Explosive Device Detection in X-ray Security Imaging | Same title PDF under docs | pp. 5–8 tasks/benchmarks, p. 9 limits, p. 10 availability |
| FALCON: Functional Assembly and Language for Compositional Reasoning in X-ray | Falcon - Functional Assembly and Language for Compositional Reasoning in X-ray.pdf | arXiv:2606.25701v2; single-image reasoning, PDF p. 27 limitations; [research](research.md) |
| Senior Design Project Selection | SDP Selection Form - Updated.pdf | p. 1 roster/preferences and departmental obligations |

Original source PDFs are retained privately; obtain them through the authorized team/lab
channel when needed. The shared meeting companions record source filenames, hashes and pages
and are sufficient for the agreed-action overview. Two distinct meetings are represented.
Page citations include the cover (printed page 1 = PDF page 2); Markdown omits student IDs.

## Earlier requirements retained

- M01 single-scan scope: device class, suspicious/modified-region localization and benign/
  modified distinction, proposed two-stage approach. Its A8 includes development, training/
  fine-tuning, testing and documentation; a GUI around a baseline is not full completion.
- M01 distributed scope: correlate components across separate scans/bags and compare late
  fusion with an end-to-end approach. Scan count, association and traveler/lane grouping are
  not fixed. Three bags and firearms were illustrative, not new acceptance criteria.
- M01 local smoke before HPC, scanner-novelty comparison, integration, biweekly review,
  explainable student ownership and actual contribution records remain applicable.
- Proposal: **500 total positive/negative samples**, preprocessing, unseen-test evaluation and
  broader GUI/control/recording requirements. M02 leaves the new-batch quota open; it does not
  explicitly waive 500 samples. Its 20-item/20-scan/200-detonator discussion is not a quota.
- Proposed minimum GUI features are implementation recommendations pending owner/reviewer
  agreement. The basic GUI itself is now a recorded immediate requirement.

## Data and implementation boundaries

Last student report: published datasets only, no new SDP lab scans. No later acquisition or
completed session evidence was supplied. This says nothing about existing lab data or Hardik's
separate collection. IEDXray generic YOLO has real CPU evidence, but the specific ready lab demo/
multi-package base-model pairing is not established. See [first inference](first-inference.md),
[model catalog](checkpoint-catalog.md) and [audit findings](iedxray-audit.md).

The lab must confirm the initial component taxonomy (detonator, explosive material, wires/
connectors discussed), labels and physical grouping. Do not invent category IDs or map these
directly to IEDXray/FALCON categories. Preserve the published test split; no empty-detection
benign decision. Paper counts/performance remain published findings, not local validation.

The proposal's illustrative 92% score and 85% threshold are not adopted targets or calibration
evidence. IEDXray contains processed RGB, not raw dual-energy channels. The approximately
70K internal scans are not proven equivalent to IEDXray. Optional STCray work remains deferred.

## People and capacity

Five named SDP students: Abd Alrahman Ismaik, Faisal Daoud Alzarooni, Ali Arif Saeed Alshamsi,
Mohammad Arwani and Ahmed Almansoori. M02 confirms their attendance and F02 assigns all five
collection/registration; there is no new model/GUI subteam allocation. The proposal's four-person
resource description remains a departmental paperwork question, not a reason to omit a student.

The earlier two-student P1 arrangement predates the new priority; confirm the current model,
GUI and P2 leads. Each student's approximately two weekly collection hours are separate from
other implementation work. Actual availability, contributions and completed hours are unreported.

## Advisor/lab question log

| ID | Remaining decision | Suggested liaison | Needed by |
|---|---|---|---|
| Q1 | Full P1 decision semantics/cascade versus association; minimum GUI can proceed with verified model scope | GUI/model leads TBD with advisor | Before claiming full P1 output |
| Q2 | Department rubric/date, proposal 500-sample and full GUI obligations, any roster paperwork | Team representative TBD | Before batch/demo acceptance |
| Q3 | IEDXray Mobile/Pager and duplicate-policy questions, physical groups/internal data; identify demo and distributed base-model artifacts separately | Model liaison with lab/author | Before semantic evaluation/training |
| Q4 | Model/GUI/integration owners, lab taxonomy, case grouping, architecture and retained fusion-comparison scope | Whole team with advisor | Before adaptation/schema extension |
| Q5 | Existing scanner AI comparison and measurable novelty | Team with CVMI | Before evaluation claims |
| Q6 | Poster template/route/cutoff, monitor/demo rules, registrations, Hardik video deadline/handoff | Event liaison TBD | ASAP; poster deadline 30 Sep retained |
| Q7 | Exact two consecutive collection weeks/slots, one email sender, protocol/scenarios, overlaps, final quota and link to 500 samples | Five students with Dr. Divya/CVMI | Before first session; finish by 15 Oct |
| Q8 | SLG identity/date and expected GUI/model demonstration | GUI/event liaison with advisor | ASAP |
| Q9 | Reconcile original 8/15 Oct prototypes with Batch 1 by 15 Oct and adaptation afterwards | Whole team with advisor | Immediate planning decision |
| Q10 | Midterm end/date window for Batch 2, retraining protocol and metrics | Collection/model leads TBD | Before Batch 2 scheduling |
| Q11 | Hardik phase-1 deliverables, technical owner and interface to detection, if any | Hardik with lab/advisor | Phase 1 due 15 Oct |
