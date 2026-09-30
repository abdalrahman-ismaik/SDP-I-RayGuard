# RayGuard poster preparation

Updated 30 September 2026 for **T23**. This is the content/design and review record;
[tasks.md](tasks.md) remains the only backlog. No advisor approval or submission is recorded.

**Latest work:** research version 6 refines the owner's edited v5 with paired scan/detail
figures and a larger FALCON example with three numbered close-ups. The supplied credits,
title and headings are preserved. Showcase version 3 remains unchanged; earlier drafts
remain available. Advisor review and submission remain open.

## Repository review bundle — 30 September

At the owner's request, the current user-saved **v6 PPTX and matching PDF** are
versioned in [the poster review folder](posters/6g-mena-2026/README.md). The README
provides direct downloads, editing guidance, source attribution and file hashes.
Both files were copied byte-for-byte; original source PDFs, raw scans, earlier drafts,
templates and personal records remain outside this publication bundle.

This is the first poster draft developed through revision 6, shared for Prof. Naoufel
and the team to review and improve. It is not an approved final submission. No sent-email
record, advisor response or submission acknowledgement has been supplied. T23 remains
in progress. The owner-saved PPTX hash is
`b2c950f1630f1ed25d4c55ca56a56c6731028c1d460619a3dc6b06abee553a87`; its PDF hash is
`20be167333269340f27419bfa9b2937200b18d176ebb067e3f529b2dc1f14ef1`.

Independent publication review verified matching one-page PDF/PPTX text, intact
credits and annotations, source/metric provenance, package integrity and absence of
private paths, credentials, macros, external PowerPoint relationships and attachments.
The PDF was rendered and visually checked. The exact poster PDF has an explicit Git
allowlist; the general source-PDF exclusion remains in place.

## Version 6 figure refinement — 30 September

Current shared files: [PPTX](posters/6g-mena-2026/RayGuard-Research-Poster-v6.pptx) /
[PDF](posters/6g-mena-2026/RayGuard-Research-Poster-v6.pdf).
The owner liked v5, edited its credits/title/headings and requested clearer research
figures, especially larger examples and detected-region zooms in sections 03 and 04.

Section 03 pairs each original IEDXray Figure 6(a,f) scan with a corresponding enlarged
region. Thin neutral crop frames and attached connectors distinguish display crops from
the published model/ground-truth boxes. The six-color legend remains faithful to the paper.
Section 04 displays one larger Figure 9 scene with three numbered matching detail crops.
The original embedded 410 × 367 JPEG was extracted without re-encoding, avoiding an
intermediate rendering step and the PDF layout's horizontal stretch. Its original red
boxes and masks remain intact. Native aspect ratios are preserved in every new crop.
These are published single-image findings; multi-package performance remains proposed.

The original scan pixels were not enhanced with generative AI or synthetic sharpening.
Detail remains limited by the source images. Text, crop frames, labels, connectors,
table and chart bars remain editable; source annotations are embedded raster. The refined
poster contains **182 objects, 93 text boxes, 11 pictures, 7 reversible crops and 10
connectors**. All eight original justified text boxes, including the supplied author
credits, retain native justification. The previously documented artifact-tool alignment
exception required a bounded native PowerPoint pass; text/geometry/media were verified
unchanged across that pass.

Independent scientific and visual review passed. All thirteen AP/mIoU entries and four
bar lengths match the papers; original source hashes and complete annotations were checked.
PowerPoint reports no vertical overflow or out-of-slide objects. Justified text retains
at most 1.13 pt of measured glyph overhang without visible clipping. Package integrity,
source content, notes/privacy, native crops and template fidelity passed. A later save of
the source v5 changed only package metadata and a text-run dirty flag; visible source
content, style and geometry still match the reviewed copy. Earlier files remain intact.

Next: owner/advisor review of v6, print-size confirmation and submission coordination.
The 30 September obligation and unresolved prototype/collection deadline conflict remain.

## Version 5 unified research poster — 30 September

Earlier research file: `docs/6g-mena-poster/drafts/RayGuard-Research-Poster-v5.pptx`.
The owner rejected the generic methods figure and requested a coherent introduction,
objectives, methods and results for both problems, fuller source review, meaningful
visual demonstrations, efficient space use and justified text.

The review covered both full papers, the complete SDP proposal, meeting/follow-up
records, active project documentation, repository source/configuration/tests and saved
inference evidence. Dependency locks/manifests were structurally inspected; active private
records were reviewed without copying personal information into the poster. Generated
outputs, vendor packages, obsolete app copies and arbitrary binary/data contents were
not represented as a line-by-line source review.

The figure has two explicit lanes. P1 shows the working selected-task YOLOv10-M baseline
from real scan to saved overlay, class/score and review/export. Device-conditioned
localization and host association remain future work; crop versus full-image association
is not silently decided. P2 shows four illustrative package slots with supplied case
membership, component grounding, alternative late-fusion/multi-input approaches and joint
review. P2 remains proposed; no group result or acquired-case outcome is invented.

The two evidence panels reproduce IEDXray Figure 6(a,f) and the three independent
single-image FALCON Figure 9 examples, with original annotations retained. The IEDXray
three-model/three-task AP table is separate from FALCON's four-model functional-grounding
mIoU chart. All thirteen numeric entries and four bar lengths were verified. The local
0.970 demonstration is a saved training-image confidence, clearly distinct from accuracy.
The removed collection graphic/counts remain absent from the poster and notes.

The poster has **150 native objects, 80 text boxes, 6 pictures, 3 reversible crops and
8 connectors**. Seven prose boxes have native PowerPoint **Justify = 4**, confirmed in
the saved XML and PowerPoint. Artifact-tool 2.8.4 drops justified alignment on import and
export; independent API/round-trip probes confirmed this limitation. To meet the owner's
explicit formatting requirement, a bounded native formatting pass changed only those
seven paragraph alignments after artifact-tool production. Text, geometry and source-media
hashes were checked unchanged across the pass. This compatibility exception is recorded
in notes; future regeneration must preserve native justification.

Native rendering, independent scientific/visual review, package/numeric/privacy checks
and template fidelity passed. Justified text has at most 1.13 pt of reported glyph
overhang, independently inspected without visible clipping; no vertical overflow or
out-of-slide objects were found. The original template, research v1–v4 and showcase
v1–v3 were verified unchanged. Author order, final print size and advisor acceptance
remain open. Next: review research v5 and confirm credits/submission details; the
30 September obligation and unresolved prototype/collection date conflict remain.

## Version 4 research poster — 29 September

Earlier research file: `docs/6g-mena-poster/drafts/RayGuard-Research-Poster-v4.pptx`.
The owner requested less title space, fuller introduction/objectives/methods/results,
more paper figures and professional quantitative graphics. The collection-plan figure
and its counts are absent from both the new poster body and speaker notes.

The new layout contains a compact one-line title, descriptive introduction, three
objectives, native editable protocol diagram and detailed methods. Four selected
published detection examples reproduce IEDXray Figure 6(a,c,d,f), with every original
in-panel model/ground-truth box and the matching six-color legend. Full source JPEG
bytes are retained with reversible native PowerPoint crops. Figure attribution and
CC BY 4.0 credit appear on the poster and in notes.

An eleven-model horizontal chart transcribes generic AP50 from Table 3, using a common
0–100 axis and direct values. A separate table compares AP@[0.50:0.95] across the three
tasks for Grounding DINO, YOLOv10-M and RTMDet. Results text explains the leading scores,
the 9.6-point generic AP50 difference and the recall/localization distinction. The paper's
single-image evidence is explicitly separated from the proposed multi-package extension;
FALCON remains its motivation. These are published findings, not new RayGuard evaluation.

Native PowerPoint verified **162 objects**, **86 text boxes**, **5 pictures**, **4 native
crops** and **3 connectors**, with zero measured text overflows or out-of-slide objects.
Independent scientific/numeric and visual reviews passed after the AP definition was
clarified. Package integrity, all eleven bar lengths/labels, nine table values, source
media, privacy and template fidelity passed. The original template, earlier research
versions and showcase version 3 were verified unchanged.

Text, method diagram, chart bars, table cells and legend remain editable; source paper
images retain their published raster annotations. Authors/order and actual print size
remain unconfirmed. Next: owner/advisor review of research v4 and showcase v3, then
confirmed credits, materials and submission details. The earlier deadline obligations
and unresolved project-scope questions are unchanged.

## Version 3 paper-based research and showcase — 29 September

Earlier version 3 files; showcase remains current:

- `docs/6g-mena-poster/drafts/RayGuard-Research-Poster-v3.pptx`: background/objective,
  methods, IEDXray dataset/split statistics, published AP50 comparison, smaller successful
  local illustration and discussion with a FALCON grounding chart and proposed group study.
- `docs/6g-mena-poster/drafts/Xray-Project-Showcase-v3.pptx`: the research sections replace
  the GUI, followed by CT projection/colorization and multi-baggage concept figures,
  discussion and the advisor's video programme.

The supplied PDFs were inspected, including rendered benchmark tables and FALCON's
results/future-work pages. These **paper findings** drive the public-facing narrative:

| Source | Displayed evidence | Boundary |
|---|---|---|
| IEDXray, PDF p. 6 and Tables 2–4, pp. 7–8 | 17,360 images; 12,224 train / 5,136 test; three tasks; eleven models. Selected YOLOv10-M AP50: 73.4 / 58.0 / 59.1; Grounding DINO: 72.0 / 67.6 / 61.2 for device / generic / specific detection | Published fine-tuned benchmarks, not local RayGuard evaluation. AP50 is average precision at IoU 0.50, percentage scale |
| FALCON, Table 3, PDF p. 13 | Referring Functional Grounding mIoU: 29.55 for fine-tuned Groma; 69.58 for FALCON | Separate single-image grounding task/metric; no cross-bag performance claim |
| FALCON, §15, PDF p. 27 | Cross-image evidence aggregation across related scans is future work | Motivates the proposed multi-package study; does not establish an implemented system |
| Saved RayGuard run | Train000003 with its exact prediction overlay and confidence 0.970 | Selected qualitative training-image illustration, not accuracy or unseen validation |

Both quantitative graphics use editable native shapes/text, explicit 0–100 axes and
direct values. Native chart objects were tried, but PowerPoint's automatic plot spacing
omitted a category label in the compact layout; the final shape charts keep every label
legible. The source data, paper/table attribution and metric definitions remain in notes.
Native PowerPoint verified **59 / 57 text boxes**, **5 / 4 pictures** and **1 / 0 native
crops** in research/showcase, with zero text overflows and zero out-of-slide objects.
Package, chart-value/geometry, source-media, privacy and template-fidelity checks passed.
Independent numeric, scientific and visual reviews passed.

The GUI and missed example are absent from the poster bodies. Known local failure evidence
remains in project records; removing the front-facing panel does not change the evaluation
record. CT remains conceptual, and 125 groups / 500 images remain planned. Existing scope,
credit, actual CT/video, print-size, rehearsal and submission questions remain open, with
the 30 September obligation unchanged. Next: owner/advisor review of version 3 and confirmed
material/credits before final production.

## Version 2 visual redesign — 29 September

Earlier version 2 files, retained for comparison:

- `docs/6g-mena-poster/drafts/RayGuard-Research-Poster-v2.pptx`: research question,
  editable detector/review workflow, separate planned group branch, large positive/miss
  comparison, reversible picture detail crops, figure legends and discussion.
- `docs/6g-mena-poster/drafts/Xray-Project-Showcase-v2.pptx`: larger genuine GUI image
  with numbered callouts, editable CT projection geometry and illustrative color display,
  a separate four-bag group diagram, planned collection counts and video programme strip.

Both preserve the original conference template and use the approved A03 RayGuard symbol.
Research/showcase contain **44 / 42 editable text boxes**, **7 / 2 embedded pictures**
and **2 / 1 native picture crops** respectively. Repeated scan thumbnails and detail crops
remain the same source images, not new experimental cases. Text, diagrams, annotations,
legends and callouts are native objects; raster evidence remains replaceable and unchanged.
All pictures retain their aspect ratios. Native PowerPoint reports zero text overflows
and zero out-of-slide objects. Package, source-media, notes/privacy and template-fidelity
checks passed; independent scientific and visual reviews found no remaining blockers.

CT geometry and color display are explicitly generic concepts, awaiting the team's actual
method/results. They do not imply a material classifier or connection to the baggage
detector. The large 0.970 value is one training-image prediction confidence; the 0 / 1
counter is predictions / annotated regions for a retained test miss. Neither is accuracy.
The planned 125 groups / 500 images are not acquired data. Author order and video links
remain editable draft fields. Source details and interpretation limits are in speaker notes.

The original small-scale canvas, unresolved scope/credits/print requirements and 30 September
obligation are unchanged. Next: owner visual review and advisor scope clarification, then
approved CT/video material and credits, print proof, rehearsal and submission review.

## 29 September template-based alternatives

The advisor's email, supplied by the owner on 29 September (send timestamp not
established), requests introduction/context/problematics, CT projection and
colorization, multiple baggage screening, and Secure-X / CT projection/augmentation
video with Divya mentioned. It does not settle whether these belong in one poster,
whether Hardik needs a separate poster, or how CT relates technically to detection.
The earlier embedded-device poster/GUI requirement and 30 September deadline remain
recorded obligations pending clarification. A clarification email was drafted, not sent.

The supplied single-slide template was inspected and copied independently for these
first drafts, now superseded by research version 6 and showcase version 3 above:

- `docs/6g-mena-poster/drafts/RayGuard-Research-Poster-Draft.pptx`: background,
  objective, methods, real single-scan diagnostic examples, discussion and next steps.
- `docs/6g-mena-poster/drafts/Xray-Project-Showcase-Draft.pptx`: introduction,
  context/problematics, parallel CT and multi-baggage workstreams, GUI and video areas.

These older local drafts and their source template remain ignored; the current v6
review copies are shared in the bundle above. Both first drafts preserve the
conference logo, master artwork, event/footer and
318.875 × 425.5 pt canvas (approximately 112.49 × 150.11 mm). This is a small-scale
template, not confirmation of final print dimensions. Text, diagrams and overlay
boxes are native editable PowerPoint objects; images are embedded, replaceable
picture objects. Source template and source raster hashes are unchanged.

The first research draft has 32 editable text boxes and two diagnostic images. The first showcase
has 37 editable text boxes and one actual GUI screenshot. CT figures/method/results,
video links and authors/order remain explicit editable fields. The four-bag diagram
is conceptual; 125 groups / 500 images are planned catalogue counts. No CT pipeline,
group fusion, acquired data, new model evaluation or accuracy claim is implied.
Speaker notes preserve source attribution, evidence limits and editing guidance.

Both first-draft files opened and rendered in native PowerPoint with zero text overflows
and zero out-of-slide objects. Package integrity, embedded source-image hashes,
notes/privacy and template-fidelity checks passed. Independent content and visual
reviews prompted spacing and annotation-contrast improvements. See [progress](progress.md)
for commands/outcomes. Next: choose scope with the advisor, fill approved credits/CT/video
content, confirm print/submission requirements, and review before submission.

## Earlier working direction (before the supplied template)

The user selected **working application and live demonstration** as the lead,
**A1 portrait (594 × 841 mm)** as a provisional draft, and confirmed that author
names/order and supervisor credits are not yet agreed. A1 is a working choice,
not an organizer specification. The assigned title remains:

**Embedded Explosive Detection in Electronic Devices**

Use **RayGuard** as the project name, with a neutral Khalifa University / Senior
Design Project affiliation for now. Do not infer authorship from repository ownership
or select an exploratory logo as the approved identity. The audience is provisionally
academic and industry visitors at the poster/GUI showcase; their exact demo expectations
remain unconfirmed.

The message is: **a working local application makes detector outputs, reference
comparisons and review evidence inspectable.** The poster invites a demonstration;
it does not claim completed embedded-threat research or distributed detection.

## First visual draft

The private, editable, self-contained HTML is
`outputs/poster/6g-mena-2026/rayguard-poster-v1.html`. Its print export is
`output/pdf/rayguard-poster-v1.pdf`; the rendered preview, build helpers, presenter
notes, layout audit and asset provenance are in the private poster directory.
These artifacts contain authorized scan imagery and remain ignored rather than
being committed. The older 24 September content draft is preserved as history.

| Area | Purpose and content |
|---|---|
| Title | RayGuard wordmark, assigned title, neutral affiliation and one sentence on the working application |
| Main figure | Actual application screenshot showing the modified-laptop miss, reference overlay and evidence inspector |
| Demo steps | Choose a scan → inspect selected model output → record/export evidence |
| Diagnostic pair | Missed test target beside a detected bare-IED training example, each explicitly labelled |
| Model scope | Three separate supplied YOLOv10-M task checkpoints, chosen one at a time |
| Local verification and next research | Bounded CPU/GPU execution; planned lab collection, adaptation and component evidence across packages |
| Footer | Diagnostic/safety limits, dataset/model attribution, public application link and printable working-draft marker |

The style uses a white background, dark navy text and restrained teal. Predictions
are solid amber; references are dashed teal and labelled in words. The full screenshot
is unchanged; standalone scans preserve the canonical input bytes and aspect ratios,
with vector boxes copied from saved exports in original-image pixel `xyxy` coordinates.
No generated scan art, invented predictions or AI enhancement is used.

Typography uses locally licensed Barlow: 70 pt main title, 31 pt main headings,
24 pt demo text, 23 pt figure captions and 15 pt references. Original scan resolution
is limited; enlargement creates no new detail. Interface text is supporting context;
large external labels carry the explanation. The private HTML embeds its images/fonts
and renders without network requests. It is the editable draft, not a new app surface.

## Copy and evidence boundaries

Opening copy: “A working X-ray inspection prototype for running detectors,
reviewing their output and recording evidence.”

| Poster statement | Evidence type and source | Interpretation limit |
|---|---|---|
| Upload, folder receipt, published-image replay, viewing, notes and export work | Executed and verified in the [app migration record](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/migration.md); saved screenshot inspected for this draft | Human rehearsal and physical scanner handoff are unexecuted |
| Three task models are selectable | Inspected class maps and bounded execution in [model selection](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/model-selection.md) | Separate checkpoints; no automatic device-to-threat association or multi-model cascade |
| CPU/NVIDIA execution works locally | Prior saved real-model verification; [runtime record](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/runtime-verification.md) | Another GPU computer and CPU host remain unqualified; no universal GPU claim |
| Train000003 gives one generic prediction, score 0.970 | Actual saved app export and canonical-image hash inspected | Bare-IED **training** image, possibly seen by the model; score is not accuracy or safety probability |
| Test000001 gives zero predictions and one missed reference | Same-run saved export with reference annotation and `missed` comparison outcome | Selected modified-laptop **test** image, not an accuracy estimate or benign result |
| Clutter and overlap complicate localization | Paper finding: [Takele et al., Scientific Data 13, 962 (2026)](https://doi.org/10.1038/s41597-026-07263-7) | Upstream research, not a new RayGuard experiment |
| Collection, adaptation and evidence across packages are next | Recorded direction in [M02 follow-up](meeting_minutes/follow-up-2026-09-24.md) and [architecture](architecture.md) | Planned work; neither new collection/training nor P2 fusion is complete |

Both plotted cases use the generic explosive namespace
`iedxray.generic_explosive_detection`, confidence 0.25, FP32, batch one,
image-size setting 640, no augmentation and original one-to-one/top-k YOLOv10
postprocessing without NMS. Checkpoint identity and original fork are retained
in the private figure manifest. No inference or benchmark ran during poster preparation.

Reference boxes are annotations, not detector outputs. The screenshot's “GT1” means
the first ground-truth/reference box; the external caption spells out its role.
Dataset images and models are upstream contributions. Caption attribution is
“Images: Natnael Takele, IEDXray Dataset v1, CC BY 4.0. RayGuard overlays added.”
The [dataset record](https://doi.org/10.6084/m9.figshare.30784328.v1) and paper remain
linked. Final figure review is still required.

Do not add paper AP/FPS as application results, new training claims, universal
portability, operational clearance, successful unseen embedded localization,
automatic scanner connectivity or 6G network features. The published splits remain
unchanged; known label/overlap/provenance audit findings constrain interpretation.

## Demonstration companion

The proposed short demonstration is: introduce the research scope; show model/compute
identity; run an authorized scan; explain its boxes or empty output; show the retained
miss/reference comparison; add a review note and export. Model switches use the app's
deliberate restart flow and should be rehearsed in advance, since queues/history are
session-only. Do not promise a switch or fresh qualification during a short presentation.

Private `presenter-notes.md` contains the proposed sequence, actual saved run IDs and
a **recorded real-run fallback**, clearly distinguished from live inference. No presenter,
clean-start rehearsal, event laptop or demonstration acceptance is implied by preparing
those notes. Use the [prototype-demo workflow](../.agents/skills/prototype-demo/SKILL.md)
and [current app launch guide](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/README.md)
when executing rehearsal. Do not manufacture a benign example to complete a script.

## Review and finish sequence

These are preparation recommendations under T23, not new deadlines or a second backlog.

| When | Reviewable outcome |
|---|---|
| 27 September | Application-led A1 draft, figure evidence mapping and presenter notes prepared locally |
| 28 September | Advisor scientific review; confirm authors/order, supervisor credits, logo/figure approval, official template and submission instructions |
| 29 September | Apply approved corrections; rehearse on intended computer; proof the exported PDF and inspect critical regions at actual print size |
| 30 September | Submit through the confirmed route, after approval, and retain acknowledgement; exact cutoff/time zone and required submission stage remain unknown |

The ASAP SLG obligation also remains; visit timing is unconfirmed. Earlier internal
25/26 September preparation targets are not recorded as achieved. M01's 8/15 October
prototype targets still conflict with M02 adaptation after Batch 1; poster work does
not amend that conflict or the 15 October collection obligation.

Before final production, confirm: organizer dimensions/orientation/file requirements;
author and supervisor credits; approved logos; final figure use; submission stage,
route and cutoff; printing/presenter responsibility; intended model/lab pairing and
event computer. PDF/X, CMYK, bleed or printer-specific requirements have not been
supplied or validated. The earlier HTML-derived RGB PDF was an internal review
draft; the current v6 native PowerPoint export also awaits print specifications.

## Historical HTML-draft checks

The following checks apply to the earlier A1 HTML-derived draft, not the current
v6 native PowerPoint PDF, which retains the supplied template scale.

Executed locally for that earlier draft: exact source image/export hashes checked; saved boxes bound to
their run IDs; headless Chromium PDF export; one A1 page confirmed by `pdfinfo`;
fonts embedded confirmed by `pdffonts`; text extracted with `pdftotext`; PDF rendered
with `pdftoppm` and visually inspected. Browser audit found no missing assets,
page errors, external network requests or page overflow. Independent automated
review checked scientific claims, evidence identity and privacy. These checks do
not replace advisor approval, actual-size print proof or presenter rehearsal.
