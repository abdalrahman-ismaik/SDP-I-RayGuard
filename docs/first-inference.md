# First genuine IEDXray inference — 22 September 2026

**Executed and verified:** the supplied generic-explosive YOLOv10-M checkpoint runs on CPU
and produces model predictions, an overlay and a run manifest. This is a standalone reference;
the sequential P1 pipeline, benign/modified decision, training and model evaluation remain
unimplemented. No dataset annotation is used to generate predictions.

## Supplied artifacts

This section records the initial five-file inspection. The later
[expanded catalog](checkpoint-catalog.md) covers all 18 supplied checkpoints and their findings.

The user supplied `data/IEDXray/model-weights/` following Natnael's renewed link. Five
completed checkpoint files were hashed without changes; one `.crdownload` was unfinished
and was left alone. Their publisher checksums were not supplied. Source attribution is based
on the user's provision and author correspondence, not a remote byte-for-byte comparison.

| File | Bytes | Inspection |
|---|---:|---|
| `yolov10_generic_exp.pt` | 33,482,415 | Static metadata, all archive CRCs, hash and real CPU inference verified |
| `yolov10_device_detection.pt` | 33,482,479 | Static metadata, all archive CRCs and hash verified; inference not run |
| `yolov10_specific_exp.pt` | 33,496,111 | Static metadata, all archive CRCs and hash verified; inference not run |
| `ao_detr_generic_exp_detection.pth` | 750,415,778 | Hash/archive inventory only; configuration and inference unverified |
| `ao_detr_specific_exp_detection.pth` | 752,569,058 | Hash/archive inventory only; configuration and inference unverified |

Generic checkpoint SHA-256:
`b484d9a6fb37236f6adcc8c019e6a836f11901dc53a0f71d6cce7262413287ff`.
Full inventory and static inspection scripts/results are under ignored
`runs/iedxray-model-inspection-2026-09-22/`. Static inspection used ZIP/pickle opcodes without
unpickling. All YOLO checkpoints embed the model architecture, saved names and training arguments:
`YOLOv10DetectionModel`, `yolov10m.yaml`, scale m, version 8.1.34, saved training image size 640.

| Task | Stored model indices → names | Local COCO IDs |
|---|---|---|
| Generic | 0 Explosive | 0 |
| Device | 0 Laptop, 1 Mobile, 2 Pager, 3 Walkie-Talkie | 1–4 in that order |
| Specific | 0 IED Explosive, 1 Laptop Explosive, 2 Mobile Phone Explosive, 3 Pager Explosive, 4 Walkie-Talkie Explosive | 1–5 in that order |

Exact names match the corresponding local category maps. This does **not** settle the
Mobile/Pager disagreements with the complete annotations. Separate YAML/class sidecars are
not needed for this smoke inference because the architecture/names are embedded. Exact author
source revision and training data YAML are still unavailable. The generic checkpoint stores
author mAP50–95 0.34517 versus the paper's 35.1%; neither is a result measured by this project.

## Tested environment and command

Used a separate `.venv-yolov10` with Python 3.11.9 and read-only access to the existing Python
installation's packages through `--system-site-packages`. It inherits PyTorch **2.9.0+cpu** and
torchvision **0.24.0+cpu**; CUDA is unavailable in this backend. No Torch/CUDA download occurred.
The CPU audit `.venv` and global packages were not changed. Full installed versions are in
`runs/iedxray-model-inspection-2026-09-22/backend-freeze.txt`.
The CPU `doctor` checks path presence only; its validation/inference flags describe that command,
which neither runs a model nor reads earlier manifests. Verified model evidence is in the runs below.

The installed model code is the [original THU-MIG fork at 453c6e3](https://github.com/THU-MIG/yolov10/tree/453c6e38a51e9d1d5a2aa5fb7f1014a711913397),
not identified merely by its package version. Small missing dependencies were added locally.
To recreate this setup **on a machine already containing the same Python/Torch dependencies**:

```powershell
py -3.11 -m venv --system-site-packages .venv-yolov10
uv pip install --python .venv-yolov10/Scripts/python.exe --no-deps "https://github.com/THU-MIG/yolov10/archive/453c6e38a51e9d1d5a2aa5fb7f1014a711913397.zip" "seaborn==0.13.2" "py-cpuinfo==9.0.0" "thop==0.1.1.post2209072238" "huggingface-hub==0.23.2" "safetensors==0.4.3"
uv pip install --python .venv-yolov10/Scripts/python.exe --no-deps -e .
.venv-yolov10/Scripts/python.exe scripts/infer_generic_yolov10.py data/IEDXray/model-weights/yolov10_generic_exp.pt data/IEDXray/Train/Train000003.jpg runs/my-new-generic-run --checkpoint-sha256 b484d9a6fb37236f6adcc8c019e6a836f11901dc53a0f71d6cce7262413287ff
```

This environment depends on the existing installation; it is not a self-contained locked
GPU environment or an exact reconstruction of the author's training environment. The runner
requires a fresh output directory and the inspected checkpoint hash. PyTorch's full-object load
is enabled only for that resolved file during construction, then the original loader is restored.
No global loader setting is changed. Automatic package installation and hub synchronization are
disabled; settings stay under the ignored run directory.

The reference uses CPU FP32, batch one, confidence 0.25 (untuned), maximum 300 detections,
no augmentation, original one-to-one head/top-k postprocessing without NMS. Original automatic
stride-aligned letterboxing is retained; `imgsz=640` does not mean every tensor is 640×640.
Actual tensor shapes are captured in the manifest. Coordinates are transformed back to the
original image and validated against the shared scan-result contract.

## Actual outcomes

These three images were previously selected for the annotation audit. The first inspected test
image returned no detections; the training/benign examples were then used to exercise the
nonempty/empty output paths. No threshold was adjusted and the miss is retained.

| Input | Annotation context | Predicted boxes at 0.25 | Actual input tensor H×W |
|---|---|---:|---|
| `Test000001.jpg` | Modified laptop; one generic threat box | 0 — a miss on this annotated example | 288×640 |
| `Train000003.jpg` | Bare IED; one generic threat box | 1, confidence 0.9702618 | 320×640 |
| `Test000034.jpg` | Ordinary laptop; no generic threat box | 0 | 320×640 |

The training example may have been seen during model training; it is a software/inference
diagnostic, not generalization evidence. No detections do not establish a benign scan.
The detected original-pixel box is approximately `[229.23, 71.40, 320.75, 227.06]` (`xyxy`).
All overlays were visually inspected. Manifests and predictions are saved in
`runs/iedxray-yolov10-generic-{test1,train3,test34}-2026-09-22/`.
A repeated training-image run is under `...-repeat-2026-09-22/`; an earlier first test attempt
is retained under `...-smoke-2026-09-22/`. The initial attempt's requested `rect=false` was
not honored by the upstream predictor; later runs explicitly record actual preprocessing shapes.
The repeat reproduced the positive box/score exactly. Per-run `annotation-context.json` records
the source split and annotation hash separately from prediction; these annotations were not model inputs.

The three recorded prediction calls took about 1.79–1.95 seconds including backend setup/warm-up.
These single cold calls are **not latency benchmarks**; upstream substage timers have limited
resolution here. No dataset AP/recall, training or GPU performance was measured.

Next: run standalone device inference while resolving concrete device-label and split-evaluation
findings in parallel. Agree P1 association and benign/modified semantics before pipeline integration.
A bounded fine-tuning experiment remains an advisor requirement, separate from this run.
