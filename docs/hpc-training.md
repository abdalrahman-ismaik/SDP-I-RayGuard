# KU H100 training handoff

Updated 18 November 2026. **Documented policy and planning, not cluster execution.**
The owner confirms HPC access and availability of CVMI-provided model/resources.
The two supplied student DOCX guides in the local `docs/HPC/` folder were read.
They remain private/ignored; this sanitized summary is portable without them.

## Inspected scheduler and environment guidance

| Item | Guidance in supplied manuals |
|---|---|
| Server | Four NVIDIA H100 GPUs; availability and allocated memory still measured per job |
| Short checks | `gpu-debug` partition and matching QoS, one GPU, up to one hour |
| Project jobs | `gpu-student` partition and matching QoS, one or two GPUs, up to six hours |
| Excluded student partition | `gpu-long` |
| Execution | Use `sbatch`, or `srun` for short active checks; no training in login shell |
| Initial job proposal | One GPU, four CPUs, 32 GB host RAM, four hours; confirm current limits |
| Logs | Create log directory before submission: Slurm opens output before script runs |
| Device selection | Respect `CUDA_VISIBLE_DEVICES`; requesting two GPUs does not enable distributed training automatically |

One guide shows standalone venv/PyTorch installation; the shared-environment
manual explicitly directs students to the administrator-provided shared
Conda/PyTorch environment instead. Ahmed should qualify a project overlay using
that shared interpreter, without modifying shared packages. If the shared package
versions conflict with the pinned YOLOv10 fork, record the incompatibility and
coordinate a supported isolated alternative with the administrator; do not
silently replace shared Torch/torchvision or assume the GUI lock supports training.

## Implementation requirements for Ahmed and Faisal

1. Inside an allocation, capture Python, Torch, torchvision, CUDA/cuDNN and actual
   H100 identity, then test real kernels. Record the clean upstream revision
   `453c6e38a51e9d1d5a2aa5fb7f1014a711913397` and package provenance.
2. Keep training/Optuna dependencies in a separately qualified project overlay.
   Pin them after inspecting shared package versions and running dependency checks
   plus forward/backward/save/reload. Do not fabricate an executed training lock
   from the inference profiles. Root CPU dependencies remain separate.
3. Build one owned Slurm template with precreated logs, explicit resources, private
   config argument and unique trial/seed output directory. Record actual Slurm job
   ID, allocated GPU, wall time, package receipt, precision and effective batch.
4. Begin with one sequential Optuna worker on one GPU. Verify persistent journal
   locking on the actual storage; avoid SQLite on NFS. Preserve sampler RNG state,
   study definition and data/config fingerprints across clean resumptions.
5. Handle time limits/termination: stop starting trials before the scheduling
   budget expires, forward termination to the trainer, retain the last completed
   epoch and save study state. Hard kills may lose the current epoch. An incomplete
   trial remains interrupted/failed until explicitly resumed with the same identity;
   do not silently count a retry as an independent configuration or report it as zero AP.
6. Verify scheduler limits, storage permissions/capacity, checkpoint resume and
   study resume with a short pilot. Use measured epoch duration to propose GPU
   hours for the 20-trial study and full-budget confirmations. Submit continuations
   through the scheduler; manual approval of a study budget is not unlimited compute.

Use `squeue`, `scontrol show job JOBID` and
`sacct -j JOBID --format=JobID,State,ExitCode,Elapsed,AllocTRES,MaxRSS` for private
job evidence. Do not publish host addresses, usernames, credentials, personal
paths or filled manifests. No remote access or jobs were performed for this handoff.

The owner's previous football project was inspected for reusable practice. Its
current files describe fixed seeds, data provenance and validation-selection
limitations; no Slurm/Optuna scripts were found, and the current GRU code uses a
CPU setup. This does not dispute prior HPC training; it means those particular
submission scripts were not available in the inspected current tree.

See [fine-tuning protocol](finetuning.md) and [tasks](tasks.md) for ownership,
trial limits and evidence requirements. This document is guidance, not another backlog.
