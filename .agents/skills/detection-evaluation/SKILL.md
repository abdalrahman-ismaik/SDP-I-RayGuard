---
name: detection-evaluation
description: Define and run fair device and threat evaluation, operating-point analysis, pipeline error analysis and reproducible latency for real saved model predictions.
---

Use when selecting thresholds, comparing detector runs or preparing final test results. Inputs:
real predictions/manifests, matching ground truth/task/category map, split provenance and frozen
protocol. Paths below are relative to the repository root. Read `AGENTS.md`, the active task,
`docs/research.md` and `docs/architecture.md`. Evaluation is not implemented. For applicable
bounding-box tasks, select/verify the backend's official COCO evaluator; distributed-case
evaluation requires agreed case ground truth and a task-specific protocol.

1. Audit split/groups. Preserve published test data for final reporting. Author weights trained
   on all training images invalidate unseen claims for a subset carved from that training set.
2. Match class order, labels, transforms and evaluator; freeze model/threshold before final test.
   For device/threat box tasks, report AP@[.50:.95], AP50, AR and per-class results separately,
   plus precision/recall at the operating point, benign false positives and missed threats.
3. Inspect real failures: clutter, small/occluded regions and stage error propagation. If crops
   exist, test remapping and account for missed hosts, outside-crop and unmatched regions.
4. Measure model and total latency separately, recording warm-up, synchronization, hardware,
   backend, batch, precision and processing boundaries. Use median/tail only with sufficient samples.

Output: frozen protocol, run-linked metrics/failure examples, threshold rationale and timing.
Verify counts/category mappings, genuine predictions and split hashes before interpreting scores.
Stop performance claims on missing ground truth, leakage or task mismatch; resolve or label the
experiment's limits. Synthetic fixtures test software only. For P2, evaluate cases and missing/
varying scan counts; component presence never proves connectivity. Update `docs/tasks.md`
and `docs/progress.md`; retain raw outputs and detailed journals privately.
