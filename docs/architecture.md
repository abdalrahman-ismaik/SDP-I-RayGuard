# Architecture and integration boundary

Status: CPU tools, JSON contracts and standalone generic-threat inference implemented.
See [verified first inference](first-inference.md). P1 pipeline and P2 fusion remain unimplemented.
One repository, separate `sdp_xray.p1` and `sdp_xray.p2`, shared `common` and `data` modules.
The exact contract is documented in [contracts.md](contracts.md) and enforced by
`src/sdp_xray/common/contracts.py`; contract examples/tests are synthetic software evidence.

The shared scan result uses a version, scan ID, execution status, original image dimensions,
model/task identity and provenance, run provenance, threshold and detections. Each detection
has an ID, original-coordinate `xyxy` box, category namespace/label, confidence and explicit
device association. COCO audit input instead uses `xywh`; conversion is not implemented.
Unmatched regions retain a null association. Scores are not automatically calibrated.
An empty successful result differs from missing input and execution failure and implies no
benign classification. The future benign/modified decision policy remains an explicit dependency.

P2 takes scan results plus externally supplied case identity and grouping provenance. No
traveler/group inference from filenames. Complete-device threat classes cannot substitute for
component labels; component evidence is explicitly not supplied by this initial interface.
Failure/missing-scan cases stay visible. Fusion and case outcomes are not implemented.

## Direction after the 24 September meeting

The five-student team's primary technical work is now distributed component evidence across
separate packages. Complete the initial lab dataset by **15 October**, then adapt/train/evaluate
the available model. A second two-week collection period follows midterms, then retraining.
Exact model, lab taxonomy, physical/case grouping, data split and fusion architecture remain
open. The discussed three packages do not fix input cardinality. Existing IEDXray/FALCON class
maps cannot silently become the new component taxonomy; a reviewed contract extension is
needed before representing component predictions.

A **simple laptop GUI** for the reported-ready laptop/pager model is an immediate, separate
showcase requirement, alongside the poster on **Embedded Explosive Detection in Electronic
Devices**, ASAP for the SLG visit. The visit date and intended model pairing are unverified.
The GUI is not implemented. It can be developed against a verified existing model before full
P1 training or distributed-model completion. Recommended minimum behavior is image selection,
real localization/score display, explicit task/model identity and visible errors/empty results;
these details are design recommendations. No detection must never become a benign verdict.

The current generic runner is one executed baseline, not proof that the meeting's complete
laptop/pager demonstration already runs. Confirm the matching artifacts, then implement and
rehearse the UI with real saved/live evidence. Hardik's colorization is a separate workstream;
no colorization preprocessing or detector dependency is implemented or assumed.

Earlier P1/P2 target dates (8/15 October) need reconciliation with the new collection-first
sequence; no replacement dates or waiver of earlier prototype requirements were provided.

## P1 implementation gates

1. Inspect real task-specific COCO/category map, published split, original RGB images and
   checkpoint/config pairing. Record provenance/hashes, license and exact upstream revision.
2. Run a real standalone full-image threat detector; add device inference as required. Save
   actual predictions, overlay and run manifest. Do not pass generic COCO classes off as threats.
3. Resolve the proposed device-crop cascade versus full-image association with the advisor.
   Crop cascade requires padding, multiple/overlapping hosts, out-of-crop/unmatched regions,
   crop labels, coordinate remapping and deduplication. Missed hosts gate later detections.
   No host-region ground-truth link may be invented.
4. After forward-pass and training smoke tests, run bounded training/fine-tuning with valid
   validation data; optionally evaluate a focused adaptation. Only then evaluate/freeze/demo.
   Preprocessing alone does not satisfy P1 A8; checkpoint-only fallback needs advisor agreement.

## Evaluation and run evidence (protocol, not implemented evaluator)

Preserve the published test split. Derive validation from training using verified physical groups.
If groups are missing, log the uncertainty; random filenames do not prove independence. Author
weights trained on all published training data have already seen a carved-out validation subset.
Use generic pretraining excluding validation or independent validation for tuning. Keep FALCON
original/counterfactual variants and P2 cases together.

Match task, class order, preprocessing, evaluator and split. Report device/threat metrics separately:
mAP@[.50:.95], AP50, AR, per-class results, precision/recall at the chosen threshold, benign false
positives and missed threats. Freeze model/threshold choices before final test reporting. Compare
model latency with total application latency separately (hardware, backend, precision, batch,
warm-up, synchronization, preprocessing/postprocessing boundaries; median/tail when supported).

For each real run save an ignored `runs/<run_id>/manifest.json` with UTC timestamp/run ID,
team commit and dirty state, upstream revision, exact command/config, dataset/split hashes,
checkpoint source/SHA-256, class map, seed, dependency/CUDA/hardware details, output paths,
actual metrics and errors. Keep detailed execution journals locally; seed alone does not establish
bitwise reproducibility. Generic YOLOv10 CPU smoke runs now exist; their single-image outputs
are not accuracy evaluation. CPU data-audit evidence remains separate. Adopt heavier tracking
only for an observed need.

P2 needs group outcomes and component-level evidence. Compare independent scan decisions to
transparent group aggregation first; investigate learned fusion only with suitable data/time.
Measure benign-group false positives, group recall, scan-count/missing-scan effects and case
latency. Presence/checklists or language explanations do not establish connectivity or danger.
