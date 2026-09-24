# External models

The supplied generic-explosive YOLOv10-M checkpoint, embedded config/class map and CPU backend
are verified for smoke inference; see [commands and results](../docs/first-inference.md). Keep files
outside Git or in this ignored directory. Doctor checks only presence/type through
`SDP_CHECKPOINT`, `SDP_MODEL_CONFIG`, `SDP_CLASS_MAP` or the matching local config fields.

The user supplied `data/IEDXray/model-weights/` after Natnael's renewed link. All three YOLO
task checkpoints embed their architectures/class names; separate sidecars are not required for
basic inference. The expanded folder now has 18 completed checkpoints across six families;
see the [checkpoint catalog](../docs/checkpoint-catalog.md). All archive checks pass, but several
additional task/config mappings need resolution. Only generic YOLO inference has been executed.
For each additional model, pair its
checkpoint with exact upstream commit, model config, task-specific class order, preprocessing,
source/license and SHA-256. A filename is not pairing evidence. Do not load untrusted pickle
weights without reviewing their source and selected backend guidance.

Initial reference: YOLOv10-M generic-explosive detection. `.venv-yolov10` uses pinned original
fork revision `453c6e38a51e9d1d5a2aa5fb7f1014a711913397` and reuses existing Python 3.11.9 /
Torch 2.9.0+cpu / torchvision 0.24.0+cpu. System packages are inherited read-only, not independently
locked; full versions are recorded locally. Other task inference and CUDA execution are unverified.

The author's suggestion to explore current Ultralytics models is optional future work. A
newer stock checkpoint needs IEDXray fine-tuning/evaluation to establish a dataset-specific
baseline. Current-package compatibility with the author's actual weights remains untested.

The [baseline runner](../scripts/infer_generic_yolov10.py) verifies source/hash/task and saves
actual predictions, overlays and manifests. Device-label correctness and pipeline decisions
remain separate from this working reference. The RTX 2060 has 6 GB; no CUDA capacity claim
is made from the CPU runs. Empty predictions do not mean benign.

The agreed training/fine-tuning work follows forward-pass and training smoke tests, with a reviewed
validation protocol. No training or large model download was launched. FALCON/full VLM
retraining is outside the initial critical path; see the [dataset catalog](../docs/datasets.md)
for related releases and their limitations.
