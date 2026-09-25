# Meeting 01: First advisor meeting

## Source and reading convention

This Markdown is a structured companion to the source minutes, preserving the meeting's
decisions, proposed approaches, action register and unresolved questions. It is not a new
meeting record, an attendance confirmation or evidence that the actions were completed.
This shared summary omits student IDs and private meeting logistics. The original PDF is
not distributed in the repository; request an authorized copy from the project team if needed.

| Field | Source value |
|---|---|
| Project | AI-Powered Explosive Detection in X-ray Scans |
| Course / department | Senior Design Project 1 / Department of Computer Science, Khalifa University |
| Meeting | First advisor meeting, 8 September 2026 |
| Advisor / main speaker | Prof. Naoufel Werghi |
| Technical input | Dr. Divya Velayudhan, clarifications and responses |
| Minutes prepared by | Abd Alrahman Ismaik |
| Private source filename | `SDP_Meeting_01_Minutes_KU_Styled (1).pdf` |
| Source length | 10 PDF pages: cover plus 9 numbered content pages |
| Source SHA-256 | `99792e279c3ab91a938585c8e338082d2ba45a21c5ae42dd601fc2a20f42b6a7` |
| Attendance | Individual attendees and absentees are not confirmed in the source; the roster is not an attendance list |

**Page convention:** every reference below uses the physical PDF page, counting the cover as
PDF p. 1. Printed page 1 is PDF p. 2; printed page 9 is PDF p. 10. Thus `PDF p. 7` means the
action-register page headed with printed page 6. Section numbers refer to the source minutes.

**Evidence categories:** a *recorded decision/requirement* describes what the minutes establish;
a *proposed approach or recorded recommendation* remains a direction to investigate;
a *paper summary reported in the minutes* is not an independently verified dataset/model result;
an *unresolved question* stays open until a later source records its resolution. None of these
categories demonstrates implementation, training, data collection or student contribution.

**Later-update notice:** read the [meeting index](README.md) and
[24 September follow-up](follow-up-2026-09-24.md) for subsequent priorities and instructions.
This companion preserves the historical **8 October / 15 October 2026** targets. Later
Meeting 02 priority changes do not explicitly cancel those dates; do not silently replace
them or treat this historical record as the complete current plan. The
[project README](../../README.md) provides the current public overview.

## Executive summary

**Recorded direction, PDF pp. 2-3:** develop two complementary proofs of concept and integrate
them into a demonstrable end-to-end system. Workstream 1 addresses a single baggage scan,
including modified electronic devices. Workstream 2 correlates component evidence across
multiple scans or bags and is identified as the principal novel contribution.

- **Prototype 1:** conventional single-scan demonstration, **8 October 2026**.
- **Prototype 2:** distributed multi-scan demonstration, **15 October 2026**.
- Begin with the benchmark paper, IEDXray and available old-scanner data; use small local tests
  before larger training on HPC/CVMI Lab resources.
- Maintain formal minutes, a logbook, an action register, named responsibilities and individual
  contribution evidence. Every member must understand the submitted implementation.
- Review progress every two weeks, coordinate through Microsoft Teams and investigate
  publication/showcase opportunities. GITEX was a priority to verify, not confirmed participation.

The source does not establish completed data access, a selected detector, a working prototype,
approved collection protocol, assigned technical subteams or confirmed individual attendance.

## Decisions D1-D8

**Recorded decisions, source section 2, PDF p. 3.** The source labels this decision log its
authoritative summary. Action identifiers below are the original Meeting 01 identifiers.

| ID | Decision | Operational implication | Linked actions | Source |
|---|---|---|---|---|
| D1 | Formal meeting documentation | Issue minutes after each meeting; maintain a logbook, named owners and an action review | A1-A2 | PDF p. 3 |
| D2 | Two-week cadence and Teams | Review progress every two weeks and coordinate through Microsoft Teams between meetings | A2 | PDF p. 3 |
| D3 | Proof-of-concept delivery level | Prioritize a functioning end-to-end pipeline; control commercial-scale features and unnecessary data expansion | A10, A13 | PDF p. 3 |
| D4 | Two-workstream technical plan | Build the single-scan and distributed models separately, then integrate them | A5, A8-A9, A13 | PDF p. 3 |
| D5 | Immediate data starting point | Begin with the paper, IEDXray and available old-scanner data; add new-scanner data later | A6-A7, A12 | PDF p. 3 |
| D6 | Staged compute strategy | Run local smoke tests before scaling training to HPC/CVMI Lab resources | A11 | PDF p. 3 |
| D7 | Repository and assessment evidence | Track plans, code and contributions in GitHub; every member must understand the implementation | A3-A4 | PDF p. 3 |
| D8 | Publication and visibility | Investigate conferences and public events; prepare a showcase demo, with GITEX subject to verification | A14-A15 | PDF p. 3 |

## Scope and prototype interpretation

**Recorded requirements, section 2.1, PDF p. 3:**

1. Support human decisions in X-ray baggage screening by detecting and localizing concealed
   explosive threats, including modified consumer electronics.
2. Add a capability or measurable improvement beyond the scanner's existing AI functions.
3. Demonstrate the full flow from data access/preparation through inference, evaluation and
   operator-facing output.
4. Start with a simple functioning system while validating technical assumptions and controlling scope.

**Deadline clarification, section 2.2, PDF p. 3:** the source says the recording briefly repeats
8 October for Prototype 2, then corrects it to 15 October. The written team note confirms the
final sequence: **P1 on 8 October, P2 on 15 October**.

### Technical workstreams

**Source section 3.1, PDF p. 4.** The goals and targets are recorded directions. The architecture
rows retain the source's wording as *proposed approaches*, not implemented or selected designs.

| Attribute | Workstream 1: single scan | Workstream 2: distributed multi-scan |
|---|---|---|
| Goal | Detect modified or explosive electronic devices in one baggage scan | Correlate suspicious components distributed across multiple scans or bags |
| Input | One X-ray image | Multiple X-ray images |
| Proposed approach | Stage 1 detects/classifies the device; stage 2 localizes the modified or explosive region | Compare late fusion of per-image detections with an end-to-end multi-input model |
| Initial output | Device class, suspicious-region localization and benign/modified distinction | Binary explosive/non-explosive was discussed as a possible first output |
| Rationale | Device context can support detection of small, cluttered or occluded modifications | Components that appear benign individually may collectively form a threat |
| Illustrative evidence | Laptop, mobile phone, pager or walkie-talkie with wires, filled cavities or other modifications | Battery, wire, circuit and organic or chemical material distributed across scans |
| Target | 8 October 2026 | 15 October 2026 |
| Unresolved in this meeting | Baseline model, operating threshold and performance target | Fusion architecture, number of scans, traveler association and lane/channel linkage |

The term **"classical"** in the team notes means the conventional single-scan problem; it
does not require classical machine-learning algorithms. The examples of **three bags** and a
dismantled pistol were illustrative: they set neither an input-scan count nor a change of scope
from explosive threats to weapon detection. No same-bag multiview or traveler-group protocol
was fixed by these examples. (PDF p. 4.)

### Detection rationale and error analysis

**Discussion and recorded requirement, section 3.2, PDF p. 4:** the discussion described an IED
in broad terms as explosive material, a trigger/detonator and a power source. It discussed
abnormal material, wiring and filled cavities as possible indicators in modified electronics.
These are contextual examples, not an acquisition protocol or verified detector capability.

The team must examine **false positives and false negatives**. Relevant difficulties include
clutter, overlapping metal, occlusion, small components and benign materials with similar X-ray
appearance. Toiletries were given as an ambiguity example. No operating threshold or required
numerical performance level was agreed in this meeting.

## Research starting point and reported benchmark facts

**Recorded instruction, section 3.3, PDF pp. 4-5:** Dr. Divya directed the team to study the
benchmark's experiments, model comparisons, numerical results and linked dataset before
choosing a baseline.

**Paper summary reported in the minutes, PDF p. 5; not project execution evidence:**

| Item | Recorded information |
|---|---|
| Paper | Takele et al. (2026), *A Benchmark Dataset for Concealed Improvised Explosive Device Detection in X-ray Security Imaging* |
| Publication | Scientific Data, volume 13, Article 962; 28 April 2026 |
| Dataset size | 17,360 X-ray images |
| Published split | 12,224 training images and 5,136 test images |
| Annotations | COCO format, with task-specific annotations |
| Benchmark tasks | Electronic-device detection; generic explosive detection; specific explosive detection |
| Reported metrics | mAP@[0.5:0.95], AP50 and AR@[0.5:0.95] |
| Model families listed | YOLOv10, Faster R-CNN, Cascade R-CNN, RetinaNet, FCOS, RTMDet, TOOD, DETR, Grounding DINO, SDANet and AO-DETR |

The source reconciles the transcript's **"about 13K"** baseline with the 12,224-image training
split. It says the **approximately 70K old-scanner images appear to be a separate internal
collection**, whose relationship to IEDXray must be verified. It does not confirm that the
team possesses that collection or that these figures identify distinct, nonoverlapping releases.

Reference as recorded in the source, PDF p. 10: Takele, N. A., Velayudhan, D., Mahapatra, D.,
AlMarzouqi, H., and Werghi, N. (2026).
[DOI: 10.1038/s41597-026-07263-7](https://doi.org/10.1038/s41597-026-07263-7).
No independent release verification is implied by reproducing this citation.

## Data, compute and integration

**Recorded directions, section 3.4, PDF p. 5:**

1. Start immediately with the paper baseline and available old-scanner data rather than waiting
   for new acquisition.
2. Confirm full-team access to the article, dataset, annotations, baseline code/weights and any
   internal explosive dataset.
3. Collect representative new-scanner images later **under an approved lab protocol**, varying
   devices, placements and viewing angles while controlling collection scope.
4. Use public X-ray datasets for comparison where appropriate; prioritize lab data because many
   public datasets lack representative explosive examples.
5. Run small local tests first, then use HPC/CVMI Lab GPU resources. Assign an owner for project
   registration and access.
6. Plan for old/new-scanner differences in resolution, image quality and embedded processing.
7. Combine the two functional prototypes into a scanner-oriented demonstration of the complete pipeline.

These directions do not establish an approved sample list, initial batch size, completed
collection, annotation assignment, granted HPC access or split protocol. A12 and O5/O7 below
retain those dependencies. Starting with published data does not itself amend the proposal's
collection requirement.

## Governance, assessment and visibility

**Recorded practices, section 4, PDF p. 6:**

- Assign a note-taker; record decisions, action items, owners and dates.
- Start each advisor meeting by reviewing the previous action register and completion status.
- Maintain dated minutes and logbook evidence of progress and individual contribution.
- Audio recording/transcription may help but does not replace the formal written record.
- Use Microsoft Teams between the two-week advisor reviews.
- Ask **Dr. Jamal** to confirm current delivery, grading, evaluation and GitHub requirements.
- Maintain developed code, plans, results and contribution evidence in GitHub.
- Every member must understand the implementation; examiners may inspect and ask about any part.
- Demonstrate a functioning system and technical understanding, not only a written description.
- Divide the five students into two technical subteams; membership and interfaces were still unassigned.

**Visibility direction, section 4.1, PDF p. 6:** identify suitable conferences in the current and
next semester, verify deadlines and prepare a showcase-ready demonstration before final
integration. NYU Abu Dhabi and Zayed University were examples only; exact event names were
not reliably captured. GITEX was the highest-priority showcase target in the team note.
November was mentioned, but the timing references conflicted and participation was unconfirmed.

### Milestones recorded at Meeting 01

**Source section 4.2, PDF p. 6.** These are targets and expected acceptance evidence, not claims
that the evidence existed at the meeting.

| Target | Milestone | Expected evidence | Certainty in source |
|---|---|---|---|
| Immediate | Mobilization | Paper/data access, assigned subteams, selected baseline, dated internal checkpoints | Agreed |
| 8 October 2026 | Prototype 1 | Working conventional single-scan demonstration | Recorded |
| 15 October 2026 | Prototype 2 | Working distributed multi-scan demonstration | Recorded |
| After prototypes | Integration | One end-to-end system combining both workstreams | Sequence agreed |
| Every two weeks | Progress review | Updated actions, risks, contribution evidence and milestone status | Agreed |
| November 2026, mentioned only | GITEX target | Showcase-ready demonstration | Date and participation unconfirmed |

## Action register A1-A15

**Source section 5, PDF p. 7.** Preserve `TBA` where no person was assigned. Target wording
such as "now" is relative to the 8 September meeting. The source provides no completion
status for these actions; later evidence must be recorded separately.

| ID | Action / expected deliverable | Responsible in source | Target in source | Source |
|---|---|---|---|---|
| A1 | Issue Meeting 01 minutes; designate a note-taker and update the logbook after every future meeting | Abd (M01); future owner TBA | Every meeting | PDF p. 7 |
| A2 | Begin each advisor meeting by reviewing the previous action register and completion status | Whole team | Every 2 weeks | PDF p. 7 |
| A3 | Ask Dr. Jamal to confirm delivery, grading, evaluation and GitHub requirements | Team representative - TBA | Before next meeting | PDF p. 7 |
| A4 | Create and maintain the GitHub repository, plan, contribution evidence and shared code understanding | Whole team | Start now; ongoing | PDF p. 7 |
| A5 | Finalize members, roles and interfaces for the two technical subteams | Whole team | Immediate | PDF p. 7 |
| A6 | Share the Nature paper, IEDXray link, baseline materials and internal explosive-dataset access; confirm full-team access | Dr. Divya / advisor team and liaison | As soon as possible | PDF p. 7 |
| A7 | Review the paper, experiments, metrics, annotations and split; select suitable baseline models | Both subteams | Before training | PDF p. 7 |
| A8 | Develop, train or fine-tune, test and document the two-stage single-scan prototype | Workstream 1 - members TBA | 8 October 2026 | PDF p. 7 |
| A9 | Select and implement the distributed architecture, evidence-fusion method and initial output definition | Workstream 2 - members TBA | 15 October 2026 | PDF p. 7 |
| A10 | Date internal checkpoints for data access, model selection, training, evaluation and demo readiness | Whole team | Immediate; ongoing | PDF p. 7 |
| A11 | Confirm HPC project access; run local smoke tests before scaling training | HPC liaison - TBA; advisor support | Before full training | PDF p. 7 |
| A12 | Confirm the new-scanner protocol, then collect and incorporate representative scans | Team with CVMI Lab | When protocol is ready | PDF p. 7 |
| A13 | Design the end-to-end pipeline: preprocessing, model stages, evaluation, alerts and GUI integration points | Whole team | Begin now | PDF p. 7 |
| A14 | Compile relevant conferences and submission deadlines for this and next semester | Owner TBA | As soon as possible | PDF p. 7 |
| A15 | Compile KU/external event requirements; verify GITEX timing/participation; prepare a showcase demo | Owner TBA / whole team | Start now; before event | PDF p. 7 |

**Requirement interpretation:** A8 explicitly includes training or fine-tuning. Running supplied
weights alone cannot be described as completion of that entire action. The meeting did not
select an operating threshold or define a validated benign/modified decision policy.

## Open questions O1-O9

**Source section 6, PDF p. 8.** These were unresolved in Meeting 01. This table preserves that
historical state; consult later records before treating any item as still open today.

| ID | Area | Confirmation required | Impact in source | Source |
|---|---|---|---|---|
| O1 | Meeting record | Confirmed individual attendees and absentees | Formal completeness | PDF p. 8 |
| O2 | Ownership | Named workstream members, subgroup leads and integration owner | Accountability | PDF p. 8 |
| O3 | Distributed scope | Same traveler versus multiple travelers; number of bags/scans; association across lanes/channels | Architecture and data design | PDF p. 8 |
| O4 | Baseline | Selected models, supplied code/weight status and relationship between IEDXray and internal collection | Training start | PDF p. 8 |
| O5 | Data protocol | Final quantity, access terms, annotation responsibilities and train/validation/test protocol | Reproducibility | PDF p. 8 |
| O6 | Evaluation | Metrics, performance targets, operational threshold and false-positive/false-negative trade-off | Acceptance criteria | PDF p. 8 |
| O7 | Infrastructure | New-scanner protocol, HPC account/project owner and compute schedule | Delivery risk | PDF p. 8 |
| O8 | Visibility | Conference/event names and deadlines, exact GITEX date and confirmed participation | Showcase planning | PDF p. 8 |
| O9 | Interface | Detailed GUI scope, recording/control requirements and delivery timing | Integration scope | PDF p. 8 |

### Recorded risk controls

**Recommendations documented in section 6.1, PDF p. 8; not completed mitigations:**

| Risk | Recommended control in the minutes |
|---|---|
| Scope expansion | Freeze a minimum demonstrable pipeline before adding datasets, GUI features or harder multi-traveler scenarios |
| Data-access delay | Confirm access immediately; begin with published training data and available old-scanner data |
| Scanner domain shift | Keep scanner metadata, compare performance by domain and plan targeted fine-tuning |
| Unclear ownership | Assign subteams, leads, HPC liaison and integration owner; track contribution evidence |
| Unbalanced model performance | Report false positives and false negatives alongside aggregate accuracy/mAP |
| Compressed integration time | Define workstream interfaces early and test a thin end-to-end path before both models are complete |

## Proposal alignment and retained requirements

**Source section 7, PDF p. 9.** These are inherited proposal requirements as summarized by the
minutes. A proposal item is not automatically a separate decision taken in Meeting 01.

| Area | Proposal baseline reported in the minutes | Meeting 01 direction | Status recorded |
|---|---|---|---|
| Objective | Detect explosives and IEDs in baggage/electronic devices | Retained through single-scan and distributed workstreams | Aligned |
| Dataset | Construct 500 samples including positive and negative X-rays | Start with IEDXray/old-scanner data; add new-scanner images later | Amendment not recorded |
| Processing and models | Preprocess, apply object detection and evaluate on unseen data | Study benchmark, use two-stage detection and investigate multi-scan fusion | Baselines pending |
| System/HMI | GUI for control/recording, threat scoring, alerts, localization and operator display | Deliver an end-to-end proof of concept; detailed GUI scope unassigned | Partially defined |
| Pipeline | Acquisition, preprocessing, AI detection, decision logic and operator review | Retain as the framework for both workstreams | To design |
| Resources | CVMI scanner/GPUs, a laptop/PC and indicative AED 1,000 budget | Local testing, then HPC/CVMI resources | Access to confirm |

The **500 samples are a combined positive-and-negative requirement**, not 500 per class. No
initial batch size, class ratio, completion count, delivery date or waiver is established here.
The original proposal p. 1 states the 500-sample requirement; the minutes preserve it with
"amendment not recorded." Likewise, the proof-of-concept direction does not itself cancel the
proposal's control/recording GUI requirement.

### Next meeting as anticipated by Meeting 01

**Source section 7.1, PDF p. 9:** reviews occur every two weeks, with exact date, time and venue
to be confirmed through Teams. The next review should confirm subteam membership and access
to paper/data/HPC, approve internal checkpoints and assess P1 progress. It should assign owners
and close the most consequential open items, particularly O2-O7. No specific next meeting slot
was confirmed in this source.

## Roster and privacy

**Source appendix A.1, PDF p. 10:** the selection form establishes the five-person roster below,
all in Computer Science. It does not prove individual attendance at Meeting 01 or technical
workstream membership. Student identifiers present in the PDF are intentionally omitted here.

| Name | Program |
|---|---|
| Abd Alrahman Ismaik | Computer Science |
| Faisal Daoud Alzarooni | Computer Science |
| Ali Arif Saeed Alshamsi | Computer Science |
| Mohammad Arwani | Computer Science |
| Ahmed Almansoori | Computer Science |

## Ambiguities future readers must preserve

- **Date correction:** P2's repeated 8 October reference was corrected to 15 October; retain
  the final historical 8/15 October sequence (PDF p. 3).
- **Attendance and roles:** the cover identifies speakers/preparer and the appendix lists a
  roster; neither supplies a confirmed attendance list or assigned subteams (PDF pp. 1, 8, 10).
- **Data identity:** about 13K and about 70K must not be silently substituted for the published
  dataset/split; the internal collection relationship remains unverified in M01 (PDF p. 5).
- **Acquisition:** new-scanner collection depends on the approved protocol; final quantity,
  ownership, labels and split policy were not fixed (PDF pp. 5, 7-8).
- **Proposal scope:** starting with existing data is not a recorded waiver of collection or
  the GUI's control/recording requirement (PDF p. 9).
- **Technical design:** a two-stage proposal does not establish crop transforms, association
  rules, calibrated decisions, a specific detector or a performance threshold (PDF pp. 4, 8).
- **Distributed scope:** illustrative bags/components do not establish real grouping labels,
  a fixed scan count or approved traveler/lane linkage (PDF pp. 4, 8).
- **Events:** the NYU Abu Dhabi/Zayed examples lack reliably captured event names; GITEX's
  November reference and participation require verification (PDF pp. 6, 8).
- **Execution:** this source records plans and reported paper facts, not completed training,
  evaluated models, collected samples or individual student work. Consult dated later evidence
  through the [meeting index](README.md) and [September follow-up](follow-up-2026-09-24.md).
