# T41 reduced generic results — 23 November 2026

**Executed and independently verified.** The owner-authorized deadline scope is
complete: six generic attempts (one failed, five completed), control/candidate
100-epoch confirmations, and one frozen published-test comparison. The original
20-attempt-per-task study, specific task and repeatability stages were explicitly
deferred. These results do not complete those stages or the full application.

## Protocol and identities

Both confirmations started independently from the exact same general YOLOv10-M
initializer, not from a search checkpoint. Seed 17, task category 0 = Explosive,
the shared 9,779 fit / 2,445 validation partition, batch 32, FP32 and two loader
workers were fixed. Search candidate 4 was selected from validation only; the
control and candidate checkpoints were selected at epochs 68 and 84 respectively.
[The handoff](t41-handoff.md) records all jobs, search values and parameters.

The final test plan was frozen before submission of Slurm **820**, which completed
at **08:45:31 UAE** on 23 November, exit 0:0, elapsed **1m27s**. It binds both
checkpoint hashes, all test image bytes, original annotations, inference code,
training receipts and settings. All **5,136 test images / 3,204 boxes** were retained.
No checkpoint, model, threshold, seed or hyperparameter was selected or changed
using these test results. This is the final comparison of the already selected pair.

| Artifact | SHA-256 |
|---|---|
| General initializer, 66,924,323 bytes | `ff2c559f11d13701abc4e0345f82851d146ecfe7035efaafcc08475cfd8b5f2d` |
| Shared partition identity | `3a1f364ff80e6e9f6db9cd5fbfc8783270fa42e2968aa136043611d09b1f9e85` |
| Original generic test annotations | `1aad3787ba4964456e58bc07366dfcc6ce29db8a6ca06cc5c377a2add8d8ca43` |
| Control checkpoint, job 770 epoch 68 | `8ebadfcf6c91f29c0a235559161f9e4414083d717449c046f0a68c6e82475c91` |
| Candidate checkpoint, job 819 epoch 84 | `097ff71eb741ce51ba053bc77512ba0916772c69ae8b4d7d50c0ef497e3f65f8` |
| Frozen test plan | `bd62be3c99f0e47c4bad375a3bc295ab71a77c474243b6353e7d606352c67188` |
| Control test predictions | `8160c3635f985b225b491be0694e11d252d84ed634cd4bc01d03c7e3c83a5431` |
| Candidate test predictions | `186474c38d6ea56a56dd7130c76c5917dd19b3e82023682ece20760a3f167ea3` |
| Final comparison record | `ee5559b7c68870ebb14bc2bd2d804526cb063062144b2b7823434f4ac2b3222f` |

Executable inference source is commit `54db37baeb1a0ebdb74281b9b9f25536d96f8a93`;
its transferred source archive is
`7692b9906b9c395ef304445d4c826af4669e993a2a13a732c37e833c11df1055`.
All 31 bound source files were verified before execution and afterward.
The runner is [`scripts/evaluate_t41_frozen.py`](../scripts/evaluate_t41_frozen.py).

## Results

All AP/AR/precision/recall entries below are **percentages**, not fractions.
One generic class means these are also the class-0 metrics; no device or
specific-component class result is implied.

| Metric | Untuned control | Search candidate |
|---|---:|---:|
| Training-only validation AP@[.50:.95] | 87.7062 | 87.4833 |
| Published-test AP@[.50:.95] | 41.5886 | 48.0502 |
| Published-test AP50 | 63.4039 | 66.5397 |
| Published-test AP75 | 42.2905 | 52.3537 |
| Published-test AR@1 | 47.3346 | 51.9070 |
| Published-test AR@10 / AR@100 | 49.2603 | 53.2709 |
| Test AP small | 33.4914 | 27.0458 |
| Test AP medium | 35.8683 | 43.5687 |
| Test AP large | 47.4741 | 53.5703 |
| Test AR small | 50.7018 | 37.8947 |
| Test AR medium | 46.9843 | 51.4295 |
| Test AR large | 51.2404 | 56.6816 |
| Precision at confidence 0.25 / IoU 0.50 | 89.0028 | 95.0830 |
| Recall at confidence 0.25 / IoU 0.50 | 48.7516 | 48.2834 |
| True positives | 1,562 | 1,547 |
| False positives | 193 | 80 |
| Missed annotated boxes | 1,642 | 1,657 |
| False positives on annotation-empty images | 55 | 25 |
| Saved detections at score floor 0.001 | 4,351 | 3,212 |

The candidate-minus-control test AP difference is **+6.4616 percentage points**.
Confirmation validation differed by **-0.2228 percentage points**. The candidate
has lower small-object AP and slightly lower fixed-threshold recall. These are
descriptive results for one preselected pair, not evidence of repeatability,
statistical significance, TPE convergence or a post-test deployment selection.
The large validation-to-test gap and roughly half the boxes missed at the fixed
operating point must remain visible in any report or presentation.

## Evaluator, failures and latency

The isolated HPC environment used Python 3.12.16, PyTorch 2.9 with CUDA 12.6,
the THU-MIG fork at `453c6e38a51e9d1d5a2aa5fb7f1014a711913397` and official
pycocotools 2.0.11. Inference was batch one, FP32, image size 640, score floor
0.001 and max_det 300. The confidence-0.25 operating point is a fixed illustrative
threshold recorded before test, not an optimized or safety-qualified threshold.
The evaluator uses original-pixel COCO `[x, y, width, height]` predictions. The
qualified preserve-wholly-outside-v1 geometry policy is retained; neither final
model produced an outside-box event. These native records are not a claim of
compatibility with every GUI/export contract.

Three original test images and their saved predictions were inspected privately
after the frozen evaluation. Selection was descriptive: the first ordered miss,
the candidate's highest-scoring false positive, and the previously flagged image 71.

- `Test000001.jpg`: the annotation lies over the densely structured electronic
  region. Both models miss it at 0.25; the candidate has no detection even at
  0.001, while the control's highest score is 0.032816 and its box is below the
  annotated region. No new label or causal explanation is inferred.
- `Test004918.jpg`: the candidate predicts the right-side region with score
  0.945477, but the generic annotation export has no box for this image. It is
  counted as a false positive against that export, not certified as a benign scan.
- `Test000071.jpg`: the known modified-host label question remains. Both outputs
  are below 0.25 (control 0.016566, candidate 0.001137). Empty operating-point
  detections and empty annotations do not establish a safe or benign outcome.

Five validation-image warmups preceded each test pass; 5,136 images per model
were timed on one Slurm-allocated H100 NVL. CUDA was synchronized around each
predictor call. The first test image's actual latency remains in the sample;
warmup on one validation shape does not prewarm every possible test shape.

| Timing boundary | Control median / p95 | Candidate median / p95 |
|---|---:|---:|
| Predictor call: loading + preprocessing + inference + postprocessing | 7.395 / 8.086 ms | 7.387 / 7.886 ms |
| Fork model-only inference Profile | 5.589 / 5.713 ms | 5.583 / 5.691 ms |

Predictor timings exclude input hashing and record writing. They are not complete
GUI, scanner, network or operator-workflow latency. Slurm MaxRSS was 1,728,716 KiB.
Process CUDA allocated/reserved peaks were 232,977,920 / 289,406,976 bytes for the
control pass and 301,198,336 / 358,612,992 bytes for the candidate pass; these are
observed process allocator peaks, not full-device capacity requirements. Raw
two-second GPU utilization/memory samples are preserved with the Slurm logs.

## Integrity, limitations and handoff

At 08:48 UAE a separate CPU process verified all saved prediction hashes,
5,136-image coverage per model, category/geometry, frozen source/checkpoints,
common initializer, prior training receipts and original annotation bytes. It
recomputed **all COCO metrics and operating-point counts exactly**, checked each
individual report against the comparison and recomputed predictor median/p95.
Earlier training verification separately checked all 350 successful epoch
prediction records and 237 bound runtime files. These are real-data checks;
the repository's synthetic tests remain software evidence only.

The final test archive is 1,496,736 bytes, SHA-256
`d8d5e039038e72066f46571cbb175fd47bfc9f17dac725534cfe1ed5c94e1a76`.
It contains 47 members; all 46 manifest-listed files were rehashed locally after
safe extraction. Selected weights were already backed up with the training
archive recorded in the handoff. Private originals, scans, weights, session
helpers and full receipts remain excluded from Git.

Four train/test exact-byte overlaps and 112 within-test duplicate pairs remain
in the original published test protocol. Physical grouping is unverified.
This is not an independent unseen-case benchmark. No re-splitting, annotation
repair, silent box clipping, sample removal or new model selection was performed
on the published test set. Single-seed generic results do not validate specific
classes, host/threat pipeline decisions, distributed fusion or operational safety.

T41's reduced execution and report-evidence handoff are complete. Review and
protected-branch integration remain human/team workflow; the broader T38 report
still requires its own forms, contribution confirmations, Word/PDF acceptance
and submission. No colleague approval, student hours or personal authorship is
inferred from this agent-assisted execution.
