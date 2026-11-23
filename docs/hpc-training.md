# T41 HPC execution status - 22 November 2026

## Final generic evaluation — 23 November 2026

Job 820 completed the frozen 5,136-image published-test comparison, exit 0:0.
Test AP is 41.5886% control / 48.0502% candidate; all metrics independently
recomputed from saved predictions. No test-based model or parameter selection.
See [final results and limitations](t41-results.md). Earlier unused-test statements
below describe the training stage before this final evaluation. No additional
training is scheduled under the completed reduced scope.

## Verified completion - 23 November 2026

The user-authorized reduced generic protocol completed at 05:13 UAE: six attempts
(five complete, one failed), then two complete 100-epoch confirmations. Ali's
validation AP was 87.7062% for the untuned control and 87.4833% for the best search
candidate, independently recomputed exactly. All 350 successful epoch prediction
records were verified. The published test set was unused; physical independence
remains exploratory. Specific/repeatability are deferred; the original 20-attempt
protocol is not complete. See [the current handoff](t41-handoff.md) for actual jobs,
checkpoint hashes, timings, scope and limitations. No further GPU job was started.

## Historical launch and implementation record

Authenticated access, assigned-storage isolation and verified source transfer
are now executed. Public IEDXray and the exact general initializer are present
and hashed on HPC. The shared Python 3.10.22 environment is unsuitable and was
left unchanged; a new isolated Python 3.12.16 candidate was installed from the
account's separate interpreter, with no shared packages inherited. The user's
explicit instruction authorizes this isolated alternative.

Logs preceded submission. Environment job **740 failed** on blocked Matplotlib
font discovery; **741 completed**, exit 0:0, in 14 seconds after local cache
preparation. Both used `gpu-student` partition/QoS, one GPU/node/task, four CPUs,
32 GB and a four-hour allocation, with a 20-minute probe process limit.
H100 NVL kernels, the pinned fork's general initializer forward/save/fresh reload,
and synthetic Optuna persistence were verified. These are not the T41 training
pilot. No unrelated job was cancelled and no GPU work ran in the login shell.

The user's subsequent explicit instruction to proceed without further human
approval is recorded as execution authorization; no Abd review is claimed.
Derived repairs, the shared 9,779/2,445 partition and both training bundles are
complete. Scoped trainer loading/finalization, local font provisioning and
in-memory label caches passed software and actual training checks. Generic pilots
750 and 754 completed train/save/reload, class mapping and Ali validation. Pilot
754 qualified batch 32 FP32 with two loader workers, full compressed predictions
and best/latest retention; steady epochs took about 99.4 seconds. Generic search
control job 755 failed during epoch-6 validation after five completed reports.
Diagnostic 756 completed; GPU qualification 757 passed the bridge fix retaining
all wholly outside detections and exactly preserving earlier valid predictions/AP.
Configuration 1 was submitted as job 758; no completion is claimed. The user's revised
scope is six generic attempts, then 100-epoch control/best confirmation at seed 17;
specific and repeatability are deferred. The finite sequence uses one whole
attempt/run per allocation, checks quota and duration, and stops at unresolved
gates. Checkpoint continuation is unsupported. No search completion is claimed.
See [the detailed handoff](t41-handoff.md) and
[environment evidence](../environments/training/README.md).

## Historical local template status - 21 November 2026

The coordinator-prepared 18 November handoff from commit `6d57e5cb362164d12cb9338cf60bd72d3f9bdc6a` is retained below with its original attribution and evidence boundaries. The local `environments/training/train.slurm` template now exists for review; no cluster access, environment qualification or job submission was performed. See [current software usage](finetuning.md) and [activation/qualification details](../environments/training/README.md). The private source guides mentioned below were inspected for the coordinator's handoff, not reopened for this implementation.

The coordinator's 21 November commit `1b911128e034c38f0087227f375f0f4d99856419`
retains the brief below. Faisal's initialization receipt identifies the official
v1.1 general pretrained file; its documented SHA-256 is
`ff2c559f11d13701abc4e0345f82851d146ecfe7035efaafcc08475cfd8b5f2d`.
No actual weights were read or transferred for this T41 update. Faisal's
HPC transfer/rehash, the allocated environment qualification and the pilot's
`Transferred N/M` log remain outstanding.

Local code now connects the upstream saved-epoch API, isolated converted datasets,
and Ali's PR18 validation interface through a conditionally gated workflow.
It has been exercised only with fake trainers/predictors, not an executed pilot.
Ali's common-parent matcher and two safeguards were inspected at `6dfa7d6`;
their code still needs integration into the execution checkout. The Slurm template
takes four private paths: config, evidence, execution authorization and runtime.
It blocks without the complete receipts described in [the handoff](t41-handoff.md).
Real checkpoint resume, download/install hooks and train/save/reload behavior
still need qualification. No job submission is authorized by these local checks.
Keep data-policy review and invalid-geometry blocks
explicit. The report freeze on 23 November does not justify bypassing these checks.

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
