# Supplied model catalog — 22 September 2026

**Artifact inspection completed, with pairing issues.** The local model folder now contains
18 completed checkpoints: three named tasks for each of six model families. Total size is
11,991,175,179 bytes (11.99 GB). File availability and archive integrity do not establish
task correctness or working inference. Only the [generic YOLO reference](first-inference.md)
has been executed in this project.

## Inventory and integrity

- All 18 files were SHA-256 hashed and stable in size/mtime during inspection.
- ZIP CRC checks passed across all 22,550 archive members, in 21.278 seconds including hashing.
- No two complete files are byte-identical; the five previously inspected files are unchanged.
- No unfinished download remains in the folder at this inspection. No sidecar configs were supplied.
- All 15 additional `.pth` files were inspected using symbolic pickle opcodes, without
  unpickling, importing checkpoint objects, executing config text or loading tensor storage.
  Twelve contain embedded MMDetection config text; three DETR files contain original-style args.

Source attribution remains the user-supplied author share; publisher checksums were not
provided. Original author paths/config text stay ignored locally. Evidence and repeatable
scripts are under `runs/iedxray-model-catalog-2026-09-22/`: `inventory.json`,
`inventory_checkpoints.py`, and `metadata/compact-summary.json` plus detailed metadata/configs.

| Model family | Named task files present | Static evidence / remaining work | Executed here |
|---|---|---|---|
| YOLOv10-M | Device, generic, specific | Embedded architectures and 4/1/5 class names previously inspected | Generic CPU smoke only |
| AO-DETR | Device, generic, specific | Config and classification heads have 4/1/5 classes; requires custom AO modules and specific-task mapping verification | No |
| Cascade R-CNN | Device, generic, specific | Config/head support 4/1/5 foreground classes; generic metadata type and specific ordering need attention | No |
| Faster R-CNN | Device, generic, specific | Device/generic heads support 4/1 classes; specific file has a concrete head/label inconsistency | No |
| DETR | Device, generic, specific | All store 92 classification outputs without class-name metadata; training mapping remains unknown | No |
| Grounding DINO | Device, generic, specific | Text-conditioned detector; generic config has a string/count issue, and specific ordering needs verification | No |

Counts in this table are in device/generic/specific order. All five non-YOLO families require
a separately verified backend. MMDetection/MMCV/MMEngine/transformers are absent from the
current inference environment; no installations were attempted for them.

## Concrete pairing issues

**Faster R-CNN specific:** `faster_rcnn_specific_explosive.pth` stores five class names but
sets `model.roi_head.bbox_head.num_classes=4`. Saved classifier weights have shape `[5,1024]`
and regressor weights `[16,1024]`. With its softmax, class-specific head this means four
foreground categories plus background, not five foreground categories. This interpretation
matches the [author's head implementation](https://github.com/Natnael-gh/IEDXray/blob/b4c32df0cd141d3d5f420dee9ff0ea135a036a85/mmdet/models/roi_heads/bbox_heads/bbox_head.py).
Hold this file for a corrected/matched artifact or an authoritative explanation; do not enlarge
the head and claim the added parameters are trained weights. Which semantic class is affected
cannot be established solely from its filename or metadata list.

**Grounding DINO generic:** `grounding_dino_generic_explosive.pth` stores `classes` as the
string `Explosive`, a configured count of 9 and denoising label embeddings of shape `[9,256]`.
The [published task config](https://github.com/Natnael-gh/IEDXray/blob/b4c32df0cd141d3d5f420dee9ff0ea135a036a85/mmdetection/configs/grounding_dino/bin_explosive_det_grounding_dino_swin-t_finetune_8xb2_20e_cat.py)
uses parentheses without a tuple comma and takes the string's length. This explains the
configuration's nine, but does not prove nine semantic prediction categories: Grounding DINO
classifies against text. Verify prompts, category handling and checkpoint loading together;
do not silently change dimensions and claim paper reproduction.

**Generic RCNN metadata:** Faster R-CNN and Cascade R-CNN also store `Explosive` as a string,
although their actual heads consistently support one foreground class. Their inference/evaluation
label metadata needs explicit normalization and verification before use; a list of characters
would be wrong. Original checkpoints remain unchanged.

**Specific-task ordering:** AO-DETR, Cascade R-CNN, Faster R-CNN and Grounding DINO metadata
place Pager before Mobile. The supplied COCO category array and YOLO names place Mobile before
Pager. A class-name order is not proof of the numeric mapping used during training: inspect the
dataset loader and actual author training annotations before assigning semantic output labels.
No label swap was applied. This is separate from the already recorded cross-export device-label
disagreement in the dataset.

**DETR:** all three files store `class_embed.weight=[92,256]`, ResNet-50/original-style DETR
arguments, 100 queries and epoch 79, with distinct recorded task paths and distinct file hashes.
No class names or model-index/category-ID map is stored. Sparse category IDs can retain a wide
head; these observations do not prove that the weights are generic COCO-only or untrained.
Their actual task mapping remains unverified.

## Backend/source readiness and next use

The author repository is now at [b4c32df](https://github.com/Natnael-gh/IEDXray/tree/b4c32df0cd141d3d5f420dee9ff0ea135a036a85),
which is an inspected source revision, not a verified training revision. Its
[MMDetection initializer](https://github.com/Natnael-gh/IEDXray/blob/b4c32df0cd141d3d5f420dee9ff0ea135a036a85/mmdet/__init__.py)
requires MMCV below 2.2.0, while its [bundled MMCV](https://github.com/Natnael-gh/IEDXray/blob/b4c32df0cd141d3d5f420dee9ff0ea135a036a85/mmcv/mmcv/version.py)
declares 2.2.0. These trees cannot simply be combined as-is. A compiled-operator pairing with
the existing Torch 2.9 CPU environment has not been established. See official
[MMDetection](https://mmdetection.readthedocs.io/en/latest/get_started.html) and
[MMCV installation documentation](https://mmcv.readthedocs.io/en/latest/get_started/installation.html).

AO-DETR embeds imports for `mmdet.models.detectors.dinov2_2`, `DINOv2` and `DINOHeadv2`.
The required detector module is absent from the inspected IEDXray tree, but exists in the
[original AO-DETR source](https://github.com/Limingyuan001/AO-DETR-test/blob/27628b5ee841e088fe452751354a66e284ec435b/mmdet/models/detectors/dinov2_2.py).
Exact custom-module/source pairing is still unverified. Grounding DINO additionally needs
local BERT/tokenizer assets; its [language implementation](https://github.com/Natnael-gh/IEDXray/blob/b4c32df0cd141d3d5f420dee9ff0ea135a036a85/mmdetection/mmdet/models/language_models/bert.py)
uses `from_pretrained`, which can initiate downloads when assets are absent.

**Project recommendation:** finish the working YOLO device/pipeline integration first. If a
second family is later selected, generic-explosive Faster R-CNN is a reasonable conventional
candidate after metadata/backend verification. This recommendation is not a performance result
or a commitment to run every model. Additional comparisons should use a fixed, documented
evaluation protocol after the data findings are addressed.
