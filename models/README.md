# External models

No checkpoint, model config, class map or backend environment has been verified. Keep files
outside Git or in this ignored directory. Doctor checks only presence/type through
`SDP_CHECKPOINT`, `SDP_MODEL_CONFIG`, `SDP_CLASS_MAP` or the matching local config fields.

First seek a working lab copy of an IEDXray task checkpoint; the public author weights link was
rechecked on 21 September and reports expiration (see [research](../docs/research.md)). Pair
checkpoint with exact upstream commit, model config, task-specific class order, preprocessing,
source/license and SHA-256. A filename is not pairing evidence. Do not load untrusted pickle
weights without reviewing their source and selected backend guidance.

Provisional primary: YOLOv10-M, unless another paper model already has a verified runnable lab
pairing. Create a separate backend environment after checking the exact upstream Python,
Torch/CUDA and supporting package requirements. The CPU project's Python version is not a
GPU environment prescription. Record upstream revision; do not vendor whole frameworks.

Next real run (not yet an executable command): one authorized held-out-for-inspection RGB scan,
batch 1, a task-compatible threat checkpoint, reviewed config/class map, recorded preprocessing
and explicit output directory. GPU discovered locally: RTX 2060, 6 GB; capacity/compatibility
untested. Use a CPU forward pass if supported or assigned lab compute if it does not fit; record
actual resources. Save predictions/overlay/run manifest before training. No invented upstream
inference command is supplied while the exact checkpoint/config pairing is unknown.

Training/fine-tuning under A8 follows forward-pass and training smoke tests, with a reviewed
validation protocol. No training or large model download was launched. FALCON/full VLM
retraining is outside the initial critical path; see release limitations in research.
