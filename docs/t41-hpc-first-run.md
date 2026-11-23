# T41 first HPC connection and qualification

21 November 2026. These are preparation steps, not evidence that an HPC session,
file transfer, environment qualification or job has occurred.

**Superseded setup assumption:** the shared interpreter was later verified as
Python 3.10.22 and is incompatible with this project's requirement. The authorized
isolated Python 3.12.16 environment and completed 23 November training are recorded
in [the current HPC handoff](t41-handoff.md). The shared-interpreter requirement
in this historical guide is not the environment used for the completed runs.

## First establish access

The supplied KU shared-environment manual, page 1, specifies **PuTTY, SSH port
22**, and **FortiClient / KU-VPN when off campus**. Connect to KU-VPN first,
then use the server address printed in the manual in PuTTY. The private host
address is intentionally not copied into this repository. Obtain missing
account/VPN details from Faisal, Abd or HPC support. Enter credentials yourself
in the official login flow; do not put them in chat, scripts or Git. The manual
does not establish that a particular user's account/session is already working.

Suggested message: "Please send me the approved HPC login website/SSH hostname
and VPN instructions, and help me confirm my first terminal session. I also need
our project directory and the existing public IEDXray/starting-weights locations.
Please do not send passwords in the group."

Once connected, `pwd` shows the current directory. Keep personal paths private.
Ask the project owner which shared directory contains the approved project,
weights and data; do not scan unrelated users' directories. Code, data and
weights must be transferred or located through the approved team process.

## Collect inventory without loading a model

The documented shared activation is:

```bash
. /etc/profile.d/conda.sh
conda activate /data/shared_envs/gpu_pytorch
```

Confirm these paths on the cluster. The project overlay must use that interpreter
and must not replace shared packages. Before the qualified overlay exists,
inventory can also run from the project root using the shared Python and an
explicit source path; it requires no Torch import or model installation:

```bash
PYTHONPATH=src python -m sdp_xray.training_qualification
```

Run inside the intended overlay later to inventory the environment actually used.
It reports Python/package versions and allocation/mask presence, without personal
paths, tokens, hostnames or environment-variable dumps. Exit 0 means inventory
completed, **not qualified for training**. It never automatically approves anything.

To hash the already transferred starting file, use its actual absolute path and
a new private JSON output whose parent exists:

```bash
PYTHONPATH=src python -m sdp_xray.training_qualification --weights /ABSOLUTE/EXISTING/yolov10m.pt --output /ABSOLUTE/PRIVATE/new-inventory.json
```

Replace the placeholders only after confirming the directories. The expected
file is 66,924,323 bytes and SHA-256
`ff2c559f11d13701abc4e0345f82851d146ecfe7035efaafcc08475cfd8b5f2d`.
The helper uses Faisal's byte hashing, never unpickles a checkpoint, rejects a
mismatch and refuses to overwrite an output. A local-PC hash does not verify
the HPC copy. Faisal's full receipt API is integrated, but his shared CLI change
remains outside this local integration; do not assume `sdp-xray init-receipt`
exists until his CLI change has been incorporated through the team workflow.

## Before the bounded pilot

Prepare the audited fit/validation bundle after the data reviews and before the
training qualification. Bundle preparation does not require completed GPU
qualification or manufacture it; the pilot still checks its own execution inputs.

Use [the data-policy record](t41-data-policy.md). Actual annotation/partition
receipts, reviewed source provenance, fixed safe batch, environment source/lock
identity, owned outputs and bounded compute must be supplied. A package inventory
alone does not qualify CUDA kernels, checkpoint loading, training or saving.

Inside a separately approved GPU allocation, verify:

1. Exact interpreter, fork/source hashes, packages, CUDA/driver and GPU identity.
2. One visible GPU, preserved scheduler mask, real forward/backward/optimizer step.
3. Correct class map and actual `Transferred N/M` log; account for the fork's
   inherited `.dfl` freezing despite the older provenance note's wording.
4. Save, finalization, Ali's validation call and fresh-process checkpoint reload.
5. Finite losses/metrics, full validation coverage, memory, checkpoint disk usage,
   timing, storage locks and failure behavior. Start with the explicit FP32 policy.

Use the existing four-input Slurm template only when those prerequisites and the
pilot authorization are concrete. Create `logs` before submission. The initial
resource proposal remains one GPU, four CPUs, 32 GB RAM and four hours on
`gpu-student` partition/QoS. No submission command was executed for this document.

## Real continuation qualification

Native checkpoint continuation is still blocked. The inspected upstream saves
half-precision checkpoint tensors, may strip optimizer state during finalization,
and restores earlier output arguments. Saving `last.pt` alone does not preserve
the full training trajectory, RNG state or an interrupted optimizer accumulation.

Before enabling it, implement/review a complete resumable state contract: model
and EMA precision, optimizer/scheduler/scaler, Python/NumPy/Torch/CUDA RNG states,
epoch/step and accumulation position, sampler state and owned output paths. Do
not advertise exact continuation using the current native adapter.

Then compare a short uninterrupted run with an explicitly interrupted/restarted
run under the same frozen inputs and seed. Check state restoration, epoch order,
predictions/objective identities, no duplicated Optuna reports, sampler state,
separate retry accounting, and no writes into an earlier run's output. A clean
boundary resume and a partial-epoch recovery are separate cases. Define equality
or numerical-tolerance criteria before running; record differences and failures.
Only reviewed execution evidence can clear this gate. Until then, use bounded
allocations that can finish trials and retain explicit interrupted status on
timeouts; do not silently replay or call a retry a new configuration.
