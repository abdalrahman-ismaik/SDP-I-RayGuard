# Architecture and integration boundary

Status: CPU tools and JSON contracts implemented; model paths intentionally unimplemented.
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
actual metrics and errors. Register it in `experiments/registry.csv`; seed alone does not establish
bitwise reproducibility. No real runs exist yet. Adopt heavier tracking only for an observed need.

P2 needs group outcomes and component-level evidence. Compare independent scan decisions to
transparent group aggregation first; investigate learned fusion only with suitable data/time.
Measure benign-group false positives, group recall, scan-count/missing-scan effects and case
latency. Presence/checklists or language explanations do not establish connectivity or danger.
