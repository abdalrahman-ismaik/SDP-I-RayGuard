# Baseline run contract (T40)

This is the shared format for a single-scan baseline run: which scans went in, which
predictions came out, and which model produced them. Training (T41) and evaluation (T42)
use the same format so a fine-tuned candidate can be compared with the original checkpoint
on equal terms.

**Evidence level:** code and synthetic software checks only. No model was run for this
change, and no real saved run has been converted yet. Nothing here is an accuracy result.

## What exists

| Piece | Where | Purpose |
|---|---|---|
| Scan input / scan result | `sdp_xray.common.contracts` ([contracts](contracts.md)) | Unchanged. One result per scan, `xyxy` boxes in original-image pixels |
| Run manifest | `sdp_xray.common.run_manifest` | One record per run: model identity, settings, stage status, input hashes |
| Prediction-set check | `validate_prediction_set(manifest, results)` | Confirms results belong to the manifest |
| Baseline adapter | `sdp_xray.baseline`, `sdp-xray baseline-record` | Combines saved batch-one runs into one shared record |

The existing runner `scripts/infer_generic_yolov10.py` is not changed. It still handles one
image per process and writes its own detailed `manifest.json`, which stays private because
it contains local paths. The adapter reads those saved outputs afterwards.

## Record layout

A shared record is a directory with two files:

- `run_manifest.json` — the run manifest below.
- `predictions.jsonl` — one scan result per line, in manifest input order.

Load both with `sdp_xray.baseline.read_record(directory)`. It validates the pair again
and returns `(manifest, results)`.

## Run manifest fields

All fields are required and unknown fields are rejected, as in the scan contracts.

| Field | Meaning |
|---|---|
| `schema_version` | `"1.0"` |
| `run_id` | Name of the record. Every scan result carries it in `run.id` |
| `role` | `baseline` for an original checkpoint, `candidate` for a fine-tuned one |
| `status` | `ok` only if every scan ran. `error` if any scan failed |
| `timestamp_utc` | When the record was written |
| `model.id`, `model.task`, `model.kind` | Catalog identity. `task` is also the category namespace of every detection |
| `model.checkpoint_sha256` | Hash of the weights used. Scan results repeat it as `model.provenance = "sha256:<hash>"` |
| `model.parent_checkpoint_sha256` | `null` for a baseline. For a candidate, the hash of the checkpoint it was initialized from |
| `model.class_map_sha256` | Hash of the class map as defined in `model_catalog.py` |
| `model.model_names` | Model output index → label, for example `{"0": "Explosive"}` |
| `model.source_category_map` | Dataset COCO category ID → label. Output indices and COCO IDs are different numbers |
| `code` | Team `git_commit`, `git_dirty`, and the `upstream_revision` of the YOLOv10 fork |
| `settings` | `imgsz`, `batch`, `conf`, `max_det`, `augment` |
| `stages` | `preprocessing`, `roi`, `features`, `postprocessing`, each with `status` and `detail` |
| `device`, `precision` | For example `cpu`, `float32` |
| `inputs` | Per scan: `scan_id`, image `sha256`, and the `source_run_id` it came from |
| `limitations` | Plain statements that travel with the record |

No path appears anywhere in the record. Images and weights are identified by hash.

### Stage status

Each stage is `implemented` (our code), `inherited` (done inside the upstream fork or the
checkpoint) or `absent`. For the current baseline:

| Stage | Status | Detail |
|---|---|---|
| Preprocessing | inherited | Upstream LetterBox, RGB / 255, as recorded by the runner |
| ROI / segmentation | absent | The full image is the detector input. Detector boxes are not a separate ROI stage |
| Features | inherited | The detector backbone inside the checkpoint. No separate feature step |
| Postprocessing | inherited | Upstream one-to-one head, top-k, no NMS |

## What is checked

`sdp_xray.baseline.shared_baseline` refuses to build a record unless:

- the run's model ID, checkpoint hash, class-map hash, task and category map all match
  the inspected pairing in `model_catalog.py`;
- every source run used the same model, settings, upstream revision, team commit, device
  and precision;
- each prediction file belongs to its run's input image.

`validate_prediction_set` then confirms that every result has the manifest's model, hash,
run ID and threshold, that every detection uses the task namespace and a label from the
class map, and that each input has exactly one result.

A failed source run stays in the record as a scan result with `status: "error"`. An empty
detection list on an `ok` result means the model reported nothing. It does not mean benign.

## Use

```text
uv run --locked python -m sdp_xray.cli baseline-record runs/<new-record-name> runs/<saved-run-1> runs/<saved-run-2>
```

The output directory must not exist and its name becomes the run ID. The command prints a
small JSON summary and exits with 2 without writing anything if a source run is unreadable
or fails a check. Records belong under ignored `runs/`, not in Git.

## Notes for the other tasks

**Fine-tuning (T41).** Write a manifest with `role: "candidate"`, the new weights' hash in
`checkpoint_sha256` and the starting checkpoint's hash in `parent_checkpoint_sha256`.
Keep `task`, `kind`, `model_names` and `source_category_map` identical to the baseline so
the two records are comparable. `validate_run_manifest` and `validate_prediction_set` do
not depend on the catalog, so they work for a checkpoint that is not listed there. The
baseline adapter itself only accepts catalog models.

**Evaluation (T42).** Start from `read_record`. For COCO output, convert `box_xyxy` to
`[x, y, width, height]` and look up `category_id` by label in `source_category_map`.
`confidence` is the raw model score and `inputs[].sha256` identifies the exact image.
Two records are a matched pair when `task`, both label maps, `settings`, all stage
entries and the input hashes agree. Results with `status: "error"` have no detections
and should be reported as failures, not counted as empty predictions. Conversion and
metrics are not implemented here.

**GUI (T39, T43).** Model name, task and checkpoint hash shown next to a result can come
from `model` in the manifest. `status`, `role` and `limitations` are meant to be shown
as they are, including the failed-scan and empty-result distinction.

## Open items

- Which model the GUI currently selects has not been confirmed against this catalog entry
  by its owner. The adapter proves the pairing of a saved run, not the GUI configuration.
- The adapter has only been exercised on synthetic manifests that copy the runner's field
  layout. Converting one real saved run needs an approved input and a named output owner.
- HPC access is not verified and no HPC job is part of this work.
- A candidate's training settings are outside this manifest and belong to T41.
