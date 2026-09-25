---
name: baseline-reproduction
description: Establish or reproduce a real RayGuard detector baseline from a matching checkpoint, configuration, class map and pinned backend; verify existing-model pairings for GUI or distributed-model preparation.
---

Use for a new task-specific forward pass or reproducing a selected baseline. Inputs: verified
artifact inventory, actual RGB scan, task labels, compute limits and run owner/output directory.
Paths below are relative to the repository root. Read `AGENTS.md`, the active task,
`models/README.md`, `docs/first-inference.md`, `docs/research.md` and `docs/architecture.md`.
Generic YOLO diagnostic inference already exists; it does not identify the meeting's intended
demo/distributed model. Confirm that pairing instead of assuming the catalog selects it.

1. Pair checkpoint source/hash with exact config, task class order, transforms and upstream commit.
   Check current primary installation docs and licenses. Prefer a verified lab pairing over a
   new comparison project; generic COCO weights are not task-trained threat evidence.
2. Build a separate compatible backend environment; do not contaminate the CPU audit lock.
   Record dependencies/CUDA/hardware and verify capacity with a single-image, batch-one run.
3. Add the smallest real adapter and save model-produced predictions/overlay. Do not substitute
   annotation boxes or realistic mock detections. Keep missing input/error distinct from no detections.
4. Save the full run manifest specified in architecture and record a shareable result in
   `docs/tasks.md` and `docs/progress.md`. Keep artifact paths and raw outputs private. Compare
   transforms/task/hardware/precision with the paper. Export timings differ from framework timings.

Output: pinned source/environment, artifact pairing, exact tested command, real output and
deviation record. Verify output labels/coordinates manually on the input image and rerun from
recorded config. Paper values and public listings are not team metrics. Stop if checkpoint/task
pairing or resource access is unresolved; continue independent inspection. No automatic
large downloads/training from setup authority. M01-A8 fine-tuning remains separate from
baseline execution and the immediate GUI; use the current backlog for sequencing.
