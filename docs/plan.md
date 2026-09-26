# Current plan - Meeting 02 and follow-up

Updated **27 September 2026 (Asia/Dubai)**. Source precedence and exact action IDs are in the
[meeting index](meeting_minutes/README.md). [Tasks](tasks.md) holds status; this page sequences
the work without assigning availability or claiming completion.

## Workstreams and capacity

**Primary technical work:** all five SDP students collect the distributed dismantled dataset,
then adapt the available model for multi-package evidence. Hardik owns a separate colorization
workstream. P1/P2 modules and branches remain useful implementation boundaries; student model,
GUI and integration assignments need confirmation.

**Near-term showcase:** simple laptop GUI and poster on **Embedded Explosive Detection in
Electronic Devices**, ready ASAP for the SLG visit. This is separate from completed P1
requirements and a trained multi-package system. The [local GUI draft](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md)
integrates the verified IEDXray generic YOLOv10-M baseline. Confirm the intended lab
laptop/pager pairing before presenting this draft as that specific showcase model.

Collection commitment is approximately **2 hours/student/week for two consecutive weeks**:
5 weekly sessions, 10 sessions total, about 20 student-session hours over the campaign.
These are planned collection hours, not completed contributions or capacity for model/GUI work.
Collect everyone's actual slots and remaining capacity privately. Previous individual
implementation allowances are not a commitment under the expanded priorities. STCray corrections, extra detector comparisons and optional
conference papers remain deferred.

## Application ownership and delivery

The owner requested immediate public separation of the GUI on 27 September.
[RayGuard-App](https://github.com/abdalrahman-ismaik/RayGuard-App) now owns frontend/API/launcher development and consumes the
versioned SDP core through a pinned submodule. The team backlog, research and
collection obligations remain here. Local extraction, software checks and real
diagnostics are complete; human presentation rehearsal and lab pairing stay open.
This repository decision changes neither the 30 September poster deadline nor
advisor requirements. Use the application checkout for GUI contributions and
review core dependency changes here before advancing its pin.

## Immediate sequence

| Order / timing | Required action | Evidence / dependency |
|---|---|---|
| Earliest opportunity | T26: collect five availability responses, name a coordinator, agree two consecutive active weeks and email one complete schedule to Dr. Divya | [Blank worksheet](templates/collection-schedule.md); five weekly slots repeated unchanged; request lab approval if pending; no fabricated times |
| Before first session | T27: obtain Dr. Divya/CVMI protocol/scenarios, annotation taxonomy, genuine group provenance and acceptance rule | Versioned lab instructions, named log/review owners; resolve overlap/conflicts |
| In parallel, ASAP | T22: all five students register; T23/T28: assign poster/GUI owners, confirm SLG date/model and rehearse the GUI draft | Actual registrations; intended lab artifact pairing; reviewed real predictions, known miss and failure/empty states |
| 25–29 Sep, internal planning targets only | Content/layout review and GUI rehearsal as capacity permits; earlier SLG date takes priority if confirmed | Organizer format, advisor review and named submitter; no promised completion before visit date is known |
| **30 Sep, earlier invitation deadline** | Submit reviewed poster through confirmed route | Submission acknowledgement; registration is separate |
| Two consecutive weeks, exact window TBD | T21: carry out 10 sessions, record attendance and usable samples after each | Approximately 2 h per student/week; same rota repeated, no invented scan quota |
| **By 15 Oct, current required milestone** | Complete Batch 1 distributed collection and review inventory/quality | Actual session records, counts, hashes, labels/groups and lab acceptance; review target to agree before deadline |
| Before/after Batch 1 as applicable | T29: inspect available base model early; adapt, train and evaluate once usable data and protocol exist | Lab model identity/support, justified split/metrics and real run manifests |
| **19–20 Oct** | 6G MENA participation as arranged | Confirmed attendance, presentation/demo logistics |
| After midterms, dates TBD | T30: second two-week broader collection campaign, then retrain and compare against Batch 1 | Exact window and greater diversity agreed; defensible evaluation, no assumed improvement |

Hardik separately collects colorization data and completes **phase 1 by 15 October** (T32),
registers for the summit and prepares the video (T24). Its deadline/scope/handoff needs
confirmation; the colorization date does not become a video deadline.

## Prototype timetable conflict to resolve

M01's **8 October P1 / 15 October P2** targets are still recorded requirements. M02 does not
explicitly replace them, but its adaptation-after-Batch-1 sequence conflicts with the prior
P2 completion plan. T10/Q9 must reconcile deliverables/dates with the advisor. Do not keep the
old 9–14 October P2 evaluation/rehearsal blocks as active promises or invent replacement dates.

The ASAP GUI can expose a verified existing model without waiting for full P1 training.
That demonstration must accurately state its scope and limitations; it is not evidence that
the distributed detector or the full earlier P1 brief is finished.

## Technical preparation that can proceed now

1. T06/T28: run the already inspected device checkpoint on a declared diagnostic sample and
   establish the exact lab demo model. Save real outputs, class namespace, input hashes and
   latency boundaries; use a separately verified backend. No test-set tuning.
2. T28: review and rehearse the implemented GUI on the presentation laptop using the
   [launch instructions](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md). Upload, model/task identity, localization/score,
   zoom/pan, history/export and failure/empty states are implemented design choices, not newly
   quoted advisor specifications. Review the real positive and missed-threat examples; retain
   exact run evidence. Never turn zero detections into a benign verdict. Human rehearsal and
   confirmation of the intended lab model remain separate from automated browser checks.
   The user's airport-interface request now has a working folder receiver, queue, display
   tools and review notes. Identify the scanner/export interface, then observe one actual
   scan handoff; published-image replay is software integration evidence only. Rehearse
   pause/resume and the documented session-only queue/restart recovery before a demonstration.
3. T03/T05: resolve existing label/split contradictions and P1 decision semantics in parallel.
   These constrain accuracy claims; they do not block planning a GUI or checking execution.
4. T11/T27/T29: agree lab component taxonomy, genuine case/physical grouping and model
   handoff. The current schema has no component namespace; propose a reviewed extension
   before adding it. Do not synthesize groups from filenames.
5. T31: verify each member can access the repository/materials and explain shared code.
   Public visibility alone does not establish team access, write permission or understanding.

## Collection quality and remaining requirements

Use lab-provided scenarios and protocol; this plan does not prescribe acquisition or device
preparation. Record actual scanner/session/physical-instance/configuration/case/view provenance,
hashes, annotation review and usability. Preserve published IEDXray splits; new case-level
splits require lab-supported grouping. Check shared samples/physical groups before evaluation.

M02 did not fix the discussed **20 items / 20 scans per student / 200 detonator examples**
as acceptance criteria. The proposal's **500 total positive/negative samples** remains a
separate obligation whose relationship to the batches must be confirmed. The simple GUI is
required now; remaining full control/recording GUI features need explicit scope/timing.

Three packages and firearms were examples, not a fixed scan-count limit or expanded project
deliverable. Meeting-reported model readiness is not executed evidence. The GUI draft has
[recorded checks](verification.md); this plan does not establish showcase acceptance, completed
collection, model adaptation, external email, registration or submission.
