# T41 training environment proposal

Status on 19 November 2026: **software proposal; no environment installed or
qualified for training**. The coordinator's [pinned HPC handoff](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/blob/6d57e5cb362164d12cb9338cf60bd72d3f9bdc6a/docs/hpc-training.md)
supersedes the earlier Windows-first proposal. Access is confirmed; an allocated
backend, shared-package inventory, safe batch and measured compute budget are not.
Keep model dependencies outside root `pyproject.toml` / `uv.lock`.

Use the administrator's shared Conda/PyTorch interpreter with a separately owned
project overlay. An overlay may inherit shared packages read-only; do not install
into or replace the shared environment. Qualify the exact THU-MIG fork
`453c6e38a51e9d1d5a2aa5fb7f1014a711913397`, initially FP32, and proposed Optuna
4.5.0 against the actual allocated H100. If versions conflict, coordinate an
administrator-supported isolated alternative. Do not silently replace Torch or
install stock PyPI ultralytics as a substitute for the fork. Package pins/lock
remain unresolved until dependency and full train/save/reload qualification.

The 17 November Windows x64 / CPython 3.11.9 proposal followed an inference profile;
it remains historical comparison context, not an HPC training qualification.

## Scheduler template and activation assumptions

`train.slurm` proposes `gpu-student` partition/QoS, one GPU, four CPUs, 32 GB RAM
and four hours. It requires exactly three absolute arguments: private config,
private evidence JSON, and a new owned output directory whose parent exists.
It requires an allocation and preserves `CUDA_VISIBLE_DEVICES`; CUDA device 0
would be relative to the allocation. It creates the output exclusively, uses a
separate child process group, forwards TERM/INT, and requests a TERM warning
120 seconds before the scheduler limit. No job has been submitted.

**The present CLI still returns blocked even with `--execute`. This template is
not yet a usable training job.** A future approved integration must validate that
the config's output ownership agrees with the allocated job directory, record
actual Slurm ID/GPU/wall time/effective batch/precision/package evidence, stop
starting work with a measured time margin, and qualify full checkpoint resume.

Set `T41_PROJECT_ROOT` and `T41_OVERLAY` explicitly. Proposed activation defaults
are `/etc/profile.d/conda.sh` and `/data/shared_envs/gpu_pytorch`; confirm them with
the administrator or override `T41_CONDA_SH` and `T41_SHARED_ENV`. The overlay
must have been created using that shared interpreter and independently qualified.
`setsid`, signal behavior, writable storage, filesystem locking and current
scheduler limits also need confirmation. No environment creation/install command
is executed by the template. Do not use global loading or package-install overrides.

Before any separately authorized human submission, create the log directory in
the submission working directory (normally the project root):

```bash
mkdir -p logs
```

Slurm opens `logs/%x-%j.out` and `.err` before executing the script, so creating
logs inside the script would be too late. Scheduler directives do not expand
shell variables; use explicit human-supplied scheduler overrides when necessary.
The template's Bash parser check is unavailable on the current Windows sandbox
because its runtime cannot initialize named objects; static checks are separate.

## Optuna persistence proposal

Use one sequential worker, Optuna 4.5.0 JournalStorage/JournalFileBackend, and
verify locking on the real shared storage. Do not use SQLite on NFS. The optional
adapter is source-based scaffolding, not executed Optuna evidence. It stores both
TPE and random-sampler NumPy RNG states as JSON, along with a journal signature
and config fingerprint. Access to those private RNG fields is version-specific
and must be qualified. No pickle is loaded for sampler restoration. The CPU fake
sampler exercises the state-preservation contract without importing Optuna/NumPy.
Torn snapshots, stale writer locks and journal/ledger divergence block automatic
resume. Do not remove/replay them without reviewed recovery. Interrupted attempts
retain the same configuration identity; failed jobs never become zero AP.

## What the pinned source actually does

All fork links below are pinned to that revision. These are code-inspection
findings, not executed training evidence.

| Source | Finding and consequence |
|---|---|
| [YOLOv10 model](https://github.com/THU-MIG/yolov10/blob/453c6e38a51e9d1d5a2aa5fb7f1014a711913397/ultralytics/models/yolov10/model.py), [trainer](https://github.com/THU-MIG/yolov10/blob/453c6e38a51e9d1d5a2aa5fb7f1014a711913397/ultralytics/models/yolov10/train.py) | `YOLOv10` binds detection training to `YOLOv10DetectionTrainer`. It constructs the detection model with the dataset class count and loads starting weights. Match the selected catalog task and class order before construction. |
| [Model.train](https://github.com/THU-MIG/yolov10/blob/453c6e38a51e9d1d5a2aa5fb7f1014a711913397/ultralytics/engine/model.py) | The API is `YOLOv10(checkpoint).train(data=..., **approved_settings)`. It passes loaded weights into the trainer and reloads best/last afterwards. This is a future integration outline, not a command enabled by this draft. |
| [Base trainer](https://github.com/THU-MIG/yolov10/blob/453c6e38a51e9d1d5a2aa5fb7f1014a711913397/ultralytics/engine/trainer.py) | `get_dataset` falls back from a missing/empty `val` to `test`. Explicit, nonempty validation is mandatory. A future training YAML must omit `test` entirely. `save_model` writes full model/EMA objects, optimizer and metrics to last/best; final evaluation strips checkpoints and validates best. |
| [Checkpoint loader](https://github.com/THU-MIG/yolov10/blob/453c6e38a51e9d1d5a2aa5fb7f1014a711913397/ultralytics/nn/tasks.py), [optimizer stripping](https://github.com/THU-MIG/yolov10/blob/453c6e38a51e9d1d5a2aa5fb7f1014a711913397/ultralytics/utils/torch_utils.py) | Both call `torch.load` without `weights_only`. The initial loader can download missing weights and try installing missing modules. Training needs reviewed controls for every load/reload and finalization path, not just initial inference construction. |
| [COCO converter](https://github.com/THU-MIG/yolov10/blob/453c6e38a51e9d1d5a2aa5fb7f1014a711913397/ultralytics/data/converter.py), [label verifier](https://github.com/THU-MIG/yolov10/blob/453c6e38a51e9d1d5a2aa5fb7f1014a711913397/ultralytics/data/utils.py) | Converter subtracts one from category IDs, skips crowd/invalid boxes and deduplicates labels. Loader also removes duplicate float32 rows. T41 checks these losses before any eventual trainer use; ID 0 is mapped explicitly. |
| [Fork requirements](https://github.com/THU-MIG/yolov10/blob/453c6e38a51e9d1d5a2aa5fb7f1014a711913397/requirements.txt) | Pins Torch 2.0.1 / torchvision 0.15.2 and includes training/export extras. This differs from RayGuard's inference profiles and is not proof the supplied checkpoints were trained with these exact versions. |

The existing inference candidate uses Torch 2.9.0 / torchvision 0.24.0. In
[PyTorch 2.9 serialization](https://github.com/pytorch/pytorch/blob/v2.9.0/torch/serialization.py),
the default load uses `weights_only=True` when no pickle module is supplied.
These full-object fork checkpoints require a reviewed loading strategy. The
existing inference runner's scoped initial-load handling does not cover trainer
finalization/reload. Do not globally disable loading safeguards.

**Current dependency decision:** inventory the administrator's shared versions
first, then qualify a compatible project overlay. The earlier 2.9.0 / 0.24.0 and
upstream 2.0.1 / 0.15.2 alternatives are historical candidates, not instructions
to replace shared packages. No pair is an approved training lock; CUDA backend,
hardware budget and full dependency closure remain unset. The recorded source archive hash is
`ac5262ab1c7f2ad916496cdf6a00cad62cc5d92c2c6254833d9282d26d4e728f`;
it was not downloaded or rehashed during this draft.

## Qualification required in a separately authorized task

1. Approve the exact model/source, public-data policy, validation design, bounded
   scope, hardware budget, human owner and new output directory. Resolve the
   reviewed annotation/group/duplicate findings and live interface handoffs first.
   The November protocol was read at its pinned commit; the local backlog is not
   edited by this work and retains older content.
2. Produce and review a project-overlay dependency lock with artifact hashes, license
   obligations, Python, Torch/vision and CUDA/driver identity. Confirm disk/memory
   capacity. Do not reuse or alter the GUI inference environment.
3. Review source for network/package downloads, HUB callbacks, AMP checks,
   distributed-launch behavior, cache writes, hidden defaults and data repair.
   Disable automatic downloads/installs; inputs must already exist and be hashed.
4. Under separate explicit authorization, verify a bounded forward/backward and
   optimizer update, actual checkpoint save, optimizer stripping, final validation
   and fresh-process reload. Verify class names, output head, device and finite
   losses survive the whole cycle. A successful initial forward pass is inadequate.
5. Record exact commands, effective settings (including upstream defaults), source
   and lock hashes, hardware, actual outputs/errors and reviewer evidence. Hash
   produced weights only after the run. No performance or ancestry claim follows
   from merely saving a file.

No such qualification, model import, smoke training or HPC submission was performed
here. The planning CLI always blocks `--execute`, including with supplied approvals.
