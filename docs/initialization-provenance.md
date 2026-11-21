# General starting weights for the controlled study (T40)

Checked 21 November 2026. This page answers the T41 request for the general pretrained
YOLOv10-M starting weights: which file, where it comes from, its SHA-256, the evidence
that it has not seen IEDXray, and how its identity is recorded in a run.

**Evidence level:** the file was downloaded and hashed, and its contents were inspected
without loading it. The loading behaviour below was read from the pinned upstream code.
No model was loaded, no training or inference was run, and nothing here is an accuracy result.

**Credit.** The receipt fields and the validator that consumes them are Ahmed's work in
`training_research.py` on [`ahmed/t41-software-draft`](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/tree/ahmed/t41-software-draft)
(commit `32091bc`). The requirement for a fresh general initialization, the untuned/tuned
design and the seeds come from the coordinator's protocol in `docs/finetuning.md`, prepared
by Abd. The matched-comparison code this page refers to is Ali's, on `ali/evaluation`.
This page and `sdp_xray.initialization` only supply the identity those pieces need.

## The file

| Field | Value |
|---|---|
| Model | YOLOv10-M, 80-class COCO detector, official release |
| Source | <https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10m.pt> |
| Release | [THU-MIG/yolov10 `v1.1`](https://github.com/THU-MIG/yolov10/releases/tag/v1.1), published 26 May 2024 |
| File name | `yolov10m.pt` |
| Size | 66,924,323 bytes |
| SHA-256 | `ff2c559f11d13701abc4e0345f82851d146ecfe7035efaafcc08475cfd8b5f2d` |
| License | AGPL-3.0, as for the upstream repository |

Why this file: the README at our pinned upstream revision
[`453c6e3`](https://github.com/THU-MIG/yolov10/blob/453c6e38a51e9d1d5a2aa5fb7f1014a711913397/README.md)
names exactly this `v1.1` download for fine-tuning from pretrained weights. It is the same
architecture as the three supplied task checkpoints, and it is a different file from all of
them: the task checkpoints are about 33.5 MB each and their hashes are in `model_catalog.py`.

Do not use the older `v1.0` asset of the same name. It is a different file
(66,924,131 bytes, SHA-256 `36a0daa37ed8bdc7698d38e56a071dde503ae1d9333c50c212e8240b637bed7e`)
and its embedded metadata has no dataset name and numeric class names. The Hugging Face
copy `jameslahm/yolov10m` is a different serialization and was not checked.

The weights stay out of Git, like every other checkpoint.

## What was checked

1. **Downloaded and hashed.** Both release assets were downloaded from the URLs above on
   21 November 2026 and hashed with SHA-256. Sizes match what the GitHub API lists.
2. **Upload date.** The GitHub API lists the `v1.1` asset as created 2024-05-26T15:53:52Z
   and the download response carries `Last-Modified: Sun, 26 May 2024 15:54:07 GMT`.
3. **Contents, without loading.** The file is a ZIP with 802 members and all CRC checks
   pass. Its pickle was read as opcodes only: nothing was unpickled or imported. It stores
   `data: coco.yaml`, `epochs: 500`, `pretrained: False`, `nc: 80`, the 80 COCO class names
   starting `person, bicycle, car`, and model classes from `ultralytics.nn` only. No string
   in it mentions x-ray, IED or explosive.
4. **Not a task checkpoint.** Its hash differs from the generic, device and specific
   hashes in `model_catalog.py`. A test checks this.

GitHub publishes no checksum for this asset, so there is no publisher hash to compare
with. The hash above is of the bytes served by the official release on the check date.

## Evidence that the weights exclude IEDXray

| Event | Date | Source |
|---|---|---|
| YOLOv10 `v1.1` weights uploaded | 26 May 2024 | GitHub release asset metadata |
| IEDXray paper received by the journal | 25 November 2025 | [Article history](https://doi.org/10.1038/s41597-026-07263-7) |
| IEDXray dataset first public | 23 February 2026 | [Figshare record](https://figshare.com/articles/dataset/IEDXray_Dataset/30784328), `posted` date |
| IEDXray paper online | 28 April 2026 | Article history |

- The file has not changed since it was uploaded, 21 months before the dataset became
  public and 18 months before the paper was submitted.
- The file's own training arguments name `coco.yaml`, with `pretrained: False`, and its
  class list is the 80 COCO classes. COCO is a natural-image dataset without x-ray scans.
- The [YOLOv10 paper](https://arxiv.org/abs/2405.14458) and the upstream README report
  these weights as trained on COCO.
- The publisher, THU-MIG, is not among the IEDXray authors or their institutions.

**Limit of this evidence.** Weights cannot be inspected for what they were trained on, so
this is documentary and timing evidence, not a proof. It is enough to say that no public
route existed for IEDXray images to reach this file. The supplied task checkpoints are the
opposite case: they were trained on IEDXray and must not be used as the starting point of
the controlled study.

## How the file becomes a task model

Read from the pinned upstream code at `453c6e3`. This is code inspection, not an executed
training run.

- The trainer builds the task model with the class count from the data file, then
  `BaseModel.load` copies every tensor whose name and shape match the file
  (`intersect_dicts`). No layer is frozen unless the training config asks for it.
- In `v10Detect`, the hidden class-branch width is `max(ch[0], min(nc, 100))`. For
  YOLOv10-M `ch[0]` is 192, so the width is 192 for 80, 1 and 5 classes alike. Only the
  last 1x1 class convolution of `cv3` and `one2one_cv3` at each of the three scales changes
  shape. Those 12 tensors (weight and bias) are not copied. They start from the framework's
  default initialization under the training seed, with upstream `bias_init`.
- Everything else, including the box branches, is expected to transfer. The trainer logs
  `Transferred N/M items from pretrained weights`. **Keep that line from the pilot**: it is
  the executed evidence for this section, and N is expected to be M minus 12.

The generic and specific studies therefore start from the same file but not from
byte-identical models: their new class layers have different shapes. Within one task, the
untuned and tuned runs start identically when they use the same seed.

Four upstream behaviours to control when the trainer is connected:

- A weights name that is not found locally is searched for online
  (`attempt_download_asset`). Always pass the full path of the verified local file.
- With `amp: True`, which is the upstream default, `check_amp` loads `yolov8n.pt` and
  downloads it if missing. The protocol starts in FP32, so set `amp: False` explicitly.
- If unpickling hits a missing module, `torch_safe_load` tries to install packages. The
  qualified environment should make that impossible, for example by running offline.
- The upstream default seed is 0. The seed must be passed explicitly.

## Recording initialization provenance

Proposed for agreement with Ahmed and Ali. It needs no change to the shared run manifest.

1. **One file, hashed where it is used.** Copy `yolov10m.pt` to the machine that trains and
   run the command below there, before the first job. A hash checked on another machine
   does not count for that copy.
2. **The receipt goes into the training config.** The command prints the receipt in the
   format Ahmed's `validate_initialization` accepts. It was checked against that function
   at `32091bc` for both tasks. The receipt carries the hash, source, the two review
   entries, the loading procedure, the head handling, the seed and the task identity.
3. **The prediction record carries only the hash.** For both the untuned control U and the
   tuned output T, the shared run manifest has `role: "candidate"`, the output's own hash
   in `model.checkpoint_sha256`, and the hash above in `model.parent_checkpoint_sha256`.
   Training settings stay out of the run manifest, as Ahmed's draft already does.
4. **Model IDs.** Proposed: `research-yolov10m-<task>-<untuned|tuned>-seed<N>`, for example
   `research-yolov10m-generic-tuned-seed17`. The catalog IDs starting `author-` stay
   reserved for the supplied checkpoints.
5. **Comparing U and T.** Ali's current `matched_pair_differences` expects a baseline and a
   candidate whose parent is that baseline. U and T are both candidates with the same
   parent, so that check needs a second, explicit mode: both `candidate`, equal
   `parent_checkpoint_sha256`, and the same task, label maps, settings, stages and inputs.
   T's parent must not be rewritten to U's hash to fit the existing mode. This is Ali's
   file and decision; the manifest already holds what the new mode needs.
6. **Kept with the training record:** the receipt, the `Transferred N/M` log line, and the
   upstream revision.

## Use

```text
uv run --locked python -m sdp_xray.cli init-receipt <path-to>/yolov10m.pt --task generic --owner "<your name>" --output runs/<new-file>.json
```

It reads and hashes the file, and exits with 2 without writing if the bytes differ from
the table above, if the file is one of the supplied task checkpoints, or if the output
file already exists. `--task specific` gives the receipt for the specific study and
`--seed` defaults to 17. The owner is the person running the check: the two `approved`
entries in the receipt are that person's statement, not something the tool can know.
Receipts belong under ignored `runs/`.

## Open items

- The loading and head description is from code inspection. The pilot's transfer log line
  has to confirm it.
- The file has not been copied to or hashed on the HPC system.
- The model ID convention and the common-parent comparison mode are proposals until Ahmed
  and Ali agree.
- `sdp_xray.initialization.task_identity` repeats the small task lookup in Ahmed's
  `training_research.py`. Once both are on one branch, one should import the other.
