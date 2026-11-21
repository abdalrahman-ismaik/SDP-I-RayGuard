# Single-scan evaluation protocol (T42, draft)

**Status: draft.** This describes how a saved baseline or fine-tuned run will be scored on
the public IEDXray test split. **No real evaluation has been run.** The code has passed
synthetic software checks only. No number produced under this draft is a project metric.

Owner (proposed): Ali Arif Saeed Alshamsi. Reviewers: Ahmed and Faisal for the
evaluator/model interfaces; Abd and Mohammad for how results appear in the GUI.

## What is evaluated

| Item | Decision | Evidence level |
|---|---|---|
| Task | `iedxray.generic_explosive_detection`, one class, COCO category **0** `Explosive` | Documented in [model catalog](../src/sdp_xray/model_catalog.py) and [IEDXray audit](iedxray-audit.md) |
| Baseline model | `author-yolov10m-generic`, SHA-256 `b484d9a6…287ff` | Artifact inspected ([first inference](first-inference.md)). **Whether the GUI selects this exact file is not yet confirmed** |
| Ground truth | Published `binary_explosive_det_test.json`: 5,136 images, 3,204 boxes, 1,932 annotation-empty images | Counts documented by the audit. File hash to be recorded in the protocol config before approval |
| Split | Published test split, unchanged. No image is removed, moved, relabelled or clipped | Project rule |
| Input | A T40 shared record ([run contract](baseline-run-contract.md)): `run_manifest.json` + `predictions.jsonl` | Code |
| Evaluator | `pycocotools` 2.0.11 `COCOeval`, `iouType="bbox"`, default parameters | Synthetic checks executed |

The frozen settings are in [configs/evaluation/generic-explosive-test.json](../configs/evaluation/generic-explosive-test.json).
The evaluator refuses a record whose task, ground-truth counts or (once recorded) file hash
differ from that file.

## Conventions

- **Coordinates.** Records hold original-image pixel `box_xyxy`. COCO uses original-image
  pixel `[x, y, width, height]`. Conversion is `[x1, y1, x2 - x1, y2 - y1]`; no rescaling.
- **Categories.** A detection label maps to a COCO category ID only through the manifest's
  `source_category_map`. Model output indices are never used as dataset IDs.
- **Scan to image.** A scan ID (the runner's image file stem) is matched to a ground-truth
  `file_name` stem, and the image size must agree. Image hashes are not used for matching
  because 112 test image pairs share identical bytes.

## Metrics

1. **COCO box metrics:** AP@[.50:.95], AP50, AP75, AP small/medium/large, AR@1/10/100 and AR
   by size. An undefined value (COCOeval's −1) is reported as `null`, not zero.
2. **Fixed operating point:** true positives, false positives and missed boxes at confidence
   **0.25**, IoU 0.5, with greedy one-to-one matching. 0.25 is the existing GUI/runner default,
   declared before any test result. **It is not tuned**, because no approved validation split
   exists. Choosing a threshold from test results is not allowed.
3. **Failure examples:** every missed box and false positive at that operating point, by file
   name. A false positive on an annotation-empty image is reported under that name, never as a
   "benign false positive"; annotation-empty is not verified benign.

## Rules the code enforces

- **Score floor.** AP needs low-score predictions. The record must have been run at
  `conf ≤ 0.001`. A GUI-style record at 0.25 is refused. This is a separate evaluation record,
  for example the existing runner with `--confidence 0.001`.
- **Full coverage.** Every test image must have an `ok` result. A failed scan is a failure,
  not an empty prediction. A partial run needs `--allow-subset`, and the report then says `subset: true`.
- **Matched comparison.** Two separate modes, never mixed:
  - `compare` (supplied-checkpoint reproduction vs fine-tuned): baseline `role: baseline`,
    candidate `role: candidate` whose parent is the baseline checkpoint.
  - `compare-candidates` (T41 untuned control vs tuned): both `role: candidate`, different
    checkpoints, the **same** parent hash (the general starting weights from
    [initialization provenance](initialization-provenance.md), on `faisal/init-provenance`).

  Both modes also require task, kind, both label maps, settings, stages, precision, every
  input image hash, and **clean, identical inference code** (`git_dirty: false`, same
  `git_commit` and upstream revision). The output lists second-minus-first differences
  only, with no "better" verdict.
- **Approved protocol.** `status: approved` is refused unless the ground-truth SHA-256 is pinned.
- **Reports.** File names and hashes only, never local paths. A report is marked
  `draft-protocol` until this protocol's status is changed to `approved`. Reports are never overwritten.

## Validation objective for T41 tuning

`sdp_xray.validation_objective.evaluate_validation(request, ground_truth, ground_truth_sha256,
checkpoint_sha256, detections)` is the evaluator T41 calls for each completed epoch. It uses
only the validation partition, never the test split.

- **Request:** exactly the fields built by `tuning.validation_request`, namely
  `checkpoint_sha256`, `completed_epoch`, `task` (catalog task identity), `partition_sha256`,
  `validation_ids`, `annotation_sha256` and `objective`.
- **Objective:** must equal `validation_objective.objective()`: name `coco_bbox_AP_50_95`,
  scale `fraction`, evaluator ID `sdp_xray.validation_objective/pycocotools-bbox-1` and the
  frozen settings. T41 copies this block into its config.
- **Checks:**
  - the detections' checkpoint hash equals the request
  - the validation annotation file hash equals the request
  - the ground truth holds exactly the requested image IDs
  - the task identity is an inspected catalog pairing
  - every detection uses a valid image, category, box and score
- **Result:** `status: ok`, the same identities, `evaluated_image_ids`, and
  `value` = AP@[.50:.95] on a 0–1 scale.
- **Failure:** any failure raises an error. It is never returned as zero AP. A checkpoint with
  no detections does score 0, because that is a real result.

Checked against T41 commit `32091bc`: `tuning.validate_objective_result` accepted a result from
this function on synthetic fixtures. That proves the interfaces fit, not that any model is accurate.

## Known data issues (listed, not fixed)

- Four test images have the same bytes as training images: `Test001859`, `Test002780`,
  `Test002859` and `Test004750`. They stay in the primary result and are listed in the report.
- Test image ID 71 has a modified host in the complete annotations but no generic threat box.
- The generic checkpoint's full training provenance is not established.

## Timing (not measured in this task)

Model latency and total pipeline latency must be reported separately, recording hardware,
backend, precision, batch size, warm-up and synchronization. Reuse
`scripts/benchmark_generic_runtime.py`. Do not report p50/p95 from a handful of images.

## How to run

```text
uv run --locked --with-requirements environments/evaluation.in python -m pytest tests/test_evaluation.py tests/test_coco_metrics.py

uv run --locked --with-requirements environments/evaluation.in python scripts/evaluate_generic_yolov10.py evaluate --record runs/<record> --ground-truth <binary_explosive_det_test.json> --protocol configs/evaluation/generic-explosive-test.json --output runs/<report>.json
```

`compare --baseline runs/<a> --candidate runs/<b>` takes the same other options.
Reports belong in ignored `runs/`.

## Before a real evaluation

1. The GUI owner confirms the selected checkpoint hash (Faisal/Abd).
2. The team approves the duplicate, boundary and validation policy.
3. The ground-truth file SHA-256 is recorded in the protocol config, and its status is set to `approved`.
4. One named person owns the full test prediction run (5,136 images at `conf 0.001`) and its output directory.
5. For a comparison, Ahmed's candidate record uses `role: candidate` with the baseline hash as its parent.
