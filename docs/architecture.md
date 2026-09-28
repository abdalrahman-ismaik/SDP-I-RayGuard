# Architecture and integration boundary

**27 September repository boundary:** application frontend, API, launcher and GUI
tests are now maintained in [RayGuard-App](https://github.com/abdalrahman-ismaik/RayGuard-App).
The app's `engine/` Git submodule pins this repository's contracts, model catalog,
inference scripts and environment locks. Research, dataset audits and P1/P2 remain
here. References below to the original `app/` describe its pre-extraction layout;
current paths and independent setup are in the application repository.

Status: CPU tools, JSON contracts, standalone generic-threat inference and a local GUI draft
implemented, including isolated Windows CPU/NVIDIA runtime preparation and session-fixed
execution. See [verified first inference](first-inference.md), [GPU verification](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/runtime-verification.md)
and [GUI setup](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md). Other-device portability acceptance is still open.
P1 pipeline and P2 fusion remain unimplemented.
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
[F03](meeting_minutes/follow-up-collection-2026-09-28.md) supplies explosive charge, detonator,
battery and wires item families with E/D/B/W labels, and names Yonathan as protocol provider.
The later [C01 catalogue](meeting_minutes/follow-up-collection-2026-09-28.md#catalogue-handoff-f05c01)
defines 125 planned four-bag groups, each containing one target per family, for 500 images.
These are documented collection groups, not verified scan associations, physical independence
or operational case outcomes. Set IDs restart per collector/session; retain source version,
collector, session, set and bag-slot provenance without inferring groups from filenames.
Exact model, annotation IDs, actual physical/case provenance, split and fusion architecture
remain open. C01 includes E4/B3 in Round 1, conflicting with F03's earlier assignments/extras;
confirm the amendment. Four slots apply to this catalogue, not a permanent P2 input limit.
The recorded Batch 1 deadline is retained. Existing IEDXray/FALCON class
maps cannot silently become the new component taxonomy; a reviewed contract extension is
needed before representing component predictions.

A **simple laptop GUI** for the reported-ready laptop/pager model is an immediate, separate
showcase requirement, alongside the poster on **Embedded Explosive Detection in Electronic
Devices**, ASAP for the SLG visit. The visit date and intended model pairing are unverified.
The GUI now selects among three inspected YOLOv10 task checkpoints before full P1 training or
distributed-model completion. Its implemented scope is image selection, actual localization/
score display, explicit task/model identity, zoom/pan, linked findings, themes, session history,
JSON export and visible errors/empty results. These are implementation decisions, not additional
quoted advisor requirements. Zero detections must never become a benign verdict.

The current generic runner is one executed baseline, not proof that the meeting's complete
laptop/pager demonstration already runs. Confirm that intended pairing and rehearse the UI
with its real saved/live evidence. Hardik's colorization is a separate workstream;
no colorization preprocessing or detector dependency is implemented or assumed.

Earlier P1/P2 target dates (8/15 October) need reconciliation with the new collection-first
sequence; no replacement dates or waiver of earlier prototype requirements were provided.

## Local GUI boundary

RayGuard-App's `frontend/` and `backend/` hold the React/TypeScript/Vite UI and small
FastAPI service. The legacy local `app/` copy in this repository is ignored and
is not an active application source. Shared inference tools remain tracked here.
The service binds to loopback, validates bounded PNG/JPEG uploads, and uses one canonical
oriented PNG for viewing and inference. Boxes remain `xyxy` in that image's original pixels.
One active subprocess invokes the catalog-selected task in its separate pinned model
environment; the root CPU tools do not gain model dependencies. Validate shared result schema,
scan/run identity, image dimensions, model/task/hash and threshold before displaying outputs.

Session history lives in memory; private images, predictions, logs and manifests remain under
ignored `runs/gui/`. JSON exports omit machine-specific paths. Restart clears the session list
without deleting evidence. Runtime frontend assets are local; no cloud inference is added.
See [app architecture and researched options](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/architecture.md) for module responsibilities,
limits and the extension path for another verified task. Network deployment, scanner control,
persistent history, device/benign decisions and P2 fusion are outside this draft.

[Verification](verification.md) separates synthetic software checks from real upload and
folder-replay inference. These diagnostic runs include a training image and a missed threat;
they establish integration behavior, not model accuracy or showcase acceptance.

The user-requested airport-interface extension adds read-only completed-image folder intake,
a bounded queue, follow/hold review, view-only adjustments and timestamped notes. The scanner
and its interface remain unconfirmed. Intake begins paused, skips old files on first Start,
then processes new PNG/JPEG/BMP exports sequentially. Pause preserves accepted work and lets
the active run finish. Queue/source state is session-only; restart requires deliberate
recovery of unfinished exports as documented in the [launch guide](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md).
Review does not clear an item; display filters do not change model inputs. A published-image
replay is not a hardware test. The [research record](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/scanner-research.md) explains
why export reception is the first adapter, pending one observed lab scan handoff.

The direct dataset-demo input reads the local IEDXray test directory without writing
to it. Finite, explicitly started batches use the same normalized-image/model path;
source hashes and test indices remain in saved/exported run records. A shared lock
excludes simultaneous manual, folder and demo dispatch. The published test split is
preserved, and test replay is neither training nor accuracy evaluation. See the
[replay guide](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md#replay-the-published-test-images). Design-studio
previews are a separate read-only surface and cannot dispatch model jobs.

An optional [annotation comparison](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/annotation-comparison.md) separately
verifies generic test references against the recorded replay source, canonical
image and completed model result. Cyan reference boxes and amber predictions
remain independent. A deterministic IoU ≥ 0.50 rule reports per-image matched,
missed and extra boxes; export records reference provenance without changing
`ScanResult`. Unverified inputs receive no verdict, and empty references are not
benign evidence. This is a diagnostic view, not full-test accuracy or a P1 decision.

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
bitwise reproducibility. The three inspected YOLOv10 task checkpoints now have
[bounded CPU/CUDA execution evidence](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/model-selection.md), selected through
one shared hash/class-map catalog and fixed per app session. Device localization
does not supply host-threat association. Their single-image outputs are not
accuracy evaluation. CPU data-audit evidence remains separate. Adopt heavier tracking
only for an observed need.

P2 needs group outcomes and component-level evidence. Compare independent scan decisions to
transparent group aggregation first; investigate learned fusion only with suitable data/time.
Measure benign-group false positives, group recall, scan-count/missing-scan effects and case
latency. Presence/checklists or language explanations do not establish connectivity or danger.
