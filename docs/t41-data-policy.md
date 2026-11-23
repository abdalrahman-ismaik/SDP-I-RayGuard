# T41 data and validation decision record

## Prediction geometry amendment - 22 November 2026

Actual failed search job 755 and read-only diagnostic 756 established that the
pinned predictor can produce positive boxes wholly outside the original image;
its normal boundary clipping turns these into zero-area boxes. Across the 2,445
validation images, epoch 6 produced 5,880 detections, of which 293 on 124 images
had this failure. These are model predictions, not annotation findings.

The bridge now retains the original-image pixel `xyxy` coordinates only when a
finite, positive, wholly outside box collapses under clipping. Other detections
retain the fork's existing behavior. Scores, classes, detection count and image
coverage are unchanged; original and clipped coordinates are recorded. Outside
boxes remain unmatched predictions, never silently removed or expanded with an
epsilon. Raw invalid geometry still fails. Ali's COCO objective is unchanged.
This explicitly qualifies the earlier frozen-postprocessing statement below;
it is a project correction, not a claim of stock-fork equivalence. Actual GPU
qualification 757 passed: all earlier valid predictions and their AP matched
exactly, while all 5,880 epoch-6 detections including the 293 outside boxes were
retained. That diagnostic score is excluded from search selection. No successful study configurations have been pooled
across implementations, and failed configuration 0 stays in the attempt budget.

The user's current scope is generic only, six attempted configurations including
that failure, then control/best confirmation at 100 epochs and seed 17. Specific
and repeatability are deferred. Source annotations, repaired training copies,
shared partition and published test preservation are unaffected.

## Authorized execution update - 22 November 2026

The user's later explicit instruction to proceed without further human approval
supersedes the wait recorded below. The private receipt identifies user
authorization; it does not fabricate Abd's implementation review. The example
receipt remains pending. Both actual training exports were repaired as separate
derived copies, changing the five verified boxes and their areas only. Shared
seed-17 membership has 9,779 fit and 2,445 validation images, all task classes
represented on both sides, and membership SHA-256
`3a1f364ff80e6e9f6db9cd5fbfc8783270fa42e2968aa136043611d09b1f9e85`.
Both isolated bundles completed; all four original annotation hashes remained
unchanged. Published test membership is preserved and excluded from trainer YAML.
Exact-duplicate grouping and the exploratory physical-group caveat still apply.

## Historical implementation review response - 22 November 2026

The three supplied review requests are now addressed in local proposed changes
to Ali's PR22 implementation. The example approval is explicitly **pending**.
For the inspected box-only training exports, source area equals source bbox area;
the chosen derived treatment is to recompute area from the clamped bbox for
changed annotations only and record both source/derived values. This explicitly
replaces the earlier proposal to retain area in changed derived annotations.

Repair also requires both verified file-byte and canonical full-document hashes
for the two published training exports. The full image table, annotations and
categories are bound, independently of filename conventions. HPC read-only
checks accepted both real train exports and rejected both test exports, including
test documents paired with claimed train hashes. Details are in the updated
[policy](single-scan-data-policy.md); approval and actual repair remain pending.

## Executed read-only follow-up - 22 November 2026

The public archive is now present and verified on HPC. Ali's PR22 policy and
repair implementation were incorporated **unchanged** from `ea9a21b`. The user's
policy agreement is already recorded in that proposal. Abd's implementation
review and the human-filled policy receipt are still pending; the supplied
approval of PR18 concerns the evaluator only. No repair or partition was made.

Both actual training exports passed the explicit paired check: exactly five
findings with identical annotation/image IDs, filenames and original geometry.
Every overshoot is strictly less than 0.001 px:

| Annotation ID | Image ID | Original image | Overshoot (pixels, rounded for display) |
|---|---|---|---|
| 860 | 862 | Train000862.jpg | 0.000274500000008 |
| 1435 | 1437 | Train001437.jpg | 0.000272500000051 |
| 2452 | 2454 | Train002454.jpg | 0.000198499999995 |
| 3118 | 3120 | Train003120.jpg | 0.000274500000008 |
| 3209 | 3211 | Train003211.jpg | 0.000269500000008 |

The unrounded values and original boxes are retained in the private paired-check
record. Both CLI checks returned zero, but the count, threshold and correspondence
assertions establish this finding independently of their exit status. All five
specific-task findings belong to IED Explosive. No claim about their cause follows
from the small numerical size.

Original annotation byte hashes, unchanged after audit:

| Export | SHA-256 |
|---|---|
| Generic train | `95db51070c08927241cc1a0241ff9878dfdf5a9d5bc1d7af75b9f360290836dc` |
| Generic test | `1aad3787ba4964456e58bc07366dfcc6ce29db8a6ca06cc5c377a2add8d8ca43` |
| Specific train | `3398e2366c4f07d98ea3bd3e83ca2519ead0c7bb2303d045afcd9e4b37c73500` |
| Specific test | `2ae2d86bf23404c1e298e0ff684c31806760f82f210ae290af560dfa6fbecc21` |

All 17,360 images decoded and matched their recorded dimensions. Current findings
confirm five within-train, 112 within-test and four cross-split exact-byte duplicate
groups. Physical groups are absent; no filename-derived group was invented.
Canonical findings fingerprint:
`4e5ff81087cc7a7b0bcbbf1abf45806e96ebd7936aca35b583d7f33e471ce9f7`.
The private policy template binds that fingerprint and leaves `review: null`.
Original generic/specific audits still fail on the five invalid training boxes
and preserved cross-split overlap, as expected. No sample or box was silently
removed, clipped or relabelled. Empty annotations remain annotation-empty.

Next, after the required human review: apply the proposed derived repair into
distinct new task directories, verify source/test preservation and the exact
intended changes, and record both the repair record's canonical-content hash and
its actual file-byte SHA-256. Then create the shared training-only seed-17 partition
and inspect its class coverage. This follow-up provides evidence for review; it
does not fill the human approval fields in the unchanged
[PR22 policy](single-scan-data-policy.md).

## Historical decision record - 21 November 2026

21 November 2026. Review of the documented audit and merged T42 protocol, not a
new real-data audit or a completed joint approval. Dataset and execution approval
receipts remain unset. Generic first, specific second; public IEDXray only.

## Decisions implemented in the software

| Topic | Disposition | Limit |
|---|---|---|
| Published test | Preserve images, annotations and membership; never use for model/threshold selection | Four documented cross-split exact-byte pairs remain a reported test limitation |
| Training duplicates | Retain every sample; union exact-byte duplicates and verified physical groups before partitioning | Duplicate annotations that the upstream loader would silently discard still block conversion |
| Unknown physical groups | Use the protocol's explicit exploratory exact-byte fallback only after its review receipt | This is not proof of physical independence or absence of near duplicates |
| Fit/validation | One seed-17 approximately 80/20 partition of published training images; same membership for both tasks | Actual fractions/class coverage and the partition hash must be recorded from the real inventory |
| Invalid boxes | Block conversion and training; preserve originals | Five documented train threat-boundary findings remain unresolved; no epsilon, clipping, sample removal or relabelling is applied |
| Empty annotations | Retain the image as annotation-empty | Do not call it verified benign; validation AP requires at least one valid ground-truth box overall |
| Starting weights | General pretrained receipt for controlled U/T; supplied checkpoints remain a separate reproduction track | A supplied-checkpoint train carve-out is not unseen validation |

Sources: [recorded IEDXray audit](iedxray-audit.md), coordinator protocol at
`6d57e5c`, and merged [T42 evaluation protocol](single-scan-evaluation-protocol.md)
at `9350482`. Counts and findings above are recorded historical evidence; no
current scan or annotation file was opened for this decision record.

## Frozen prediction settings

The example now uses `validation_prediction = {"conf": 0.001, "max_det": 300}`.
The confidence follows Ali's documented AP score-floor requirement. The
300-prediction ceiling is an explicit project control consistent with the
existing shared-record examples, not an author-reported optimum. The official
COCO evaluator retains its own `maxDets=100` convention. Predictions use the
pinned YOLOv10 postprocessing, 640 resolution, batch one, FP32 and no test-time
augmentation. Do not add a separate NMS or change these settings during a study.

The objective is obtained directly from
`sdp_xray.validation_objective.objective()`. Its exact evaluator/settings block
and the separate prediction controls both enter the study fingerprint. Changing
either creates a different experiment. The values are now explicit and fixed
in the draft; they do not create an approval receipt or authorize execution.

## Boundary decision that cannot be cleared by a software test

The September audit reports small train-box overruns consistent with rounding,
but the cause was not established. Merely calling them rounding is not permission
to alter annotations. Current conversion and training therefore remain blocked
on those findings. Ahmed/Ali/Abd need an authoritative correction or an explicitly
reviewed derived transformation, including affected IDs, source/output hashes,
the exact transformation and its impact on paper comparability. A documented
choice to leave them blocked is valid; it does not make a real pilot runnable.

Approval must bind the actual current audit findings and partition, not the
historical counts in this document. No policy receipt was filled automatically.

## Message Ahmed can send for the joint review

The evaluator from merged PR18 is integrated locally and the config uses its
objective. I fixed validation confidence at 0.001 and max detections at 300 in
the draft. The partition code preserves every sample, groups exact duplicates
and verified physical groups, and supports the documented exploratory fallback
when physical groups are unknown. Published test membership stays unchanged.
Invalid train boxes still block the pilot: we need to review the five recorded
boundary findings and agree an authoritative correction or derived-transform
policy before preparing real training inputs. Please review these choices and
the actual findings-bound receipts together; no real training has run.
