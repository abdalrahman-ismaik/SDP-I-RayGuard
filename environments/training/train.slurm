#!/usr/bin/env bash
# T41 template only: live CLI remains blocked. Human submission requires qualification.
#SBATCH --job-name=t41-research
#SBATCH --partition=gpu-student
#SBATCH --qos=gpu-student
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=04:00:00
#SBATCH --signal=B:TERM@120
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err

set -euo pipefail
umask 077

# Slurm opens logs before this script starts. Create logs BEFORE human submission.
# Arguments: absolute config.json, evidence.json, new owned output directory.
[[ $# -eq 3 ]] || { echo 'Expected CONFIG EVIDENCE NEW_OUTPUT' >&2; exit 2; }
config=$1
evidence=$2
output=$3
[[ "$config" = /* && "$evidence" = /* && "$output" = /* ]] || exit 2
[[ -f "$config" && -f "$evidence" && ! -e "$output" && ! -L "$output" ]] || exit 2
: "${SLURM_JOB_ID:?Run only in a separately approved allocation}"
: "${CUDA_VISIBLE_DEVICES:?Allocated GPU mask is required}"
: "${T41_PROJECT_ROOT:?Set the project checkout explicitly}"
: "${T41_OVERLAY:?Set the qualified overlay created with the shared interpreter}"

# Proposed KU activation paths; confirm these on the cluster or override them.
source "${T41_CONDA_SH:-/etc/profile.d/conda.sh}"
conda activate "${T41_SHARED_ENV:-/data/shared_envs/gpu_pytorch}"
source "$T41_OVERLAY/bin/activate"
[[ "$VIRTUAL_ENV" = "$T41_OVERLAY" ]] || exit 2
export PYTHONDONTWRITEBYTECODE=1
export PYTHONNOUSERSITE=1
export PIP_NO_INDEX=1
export HF_HUB_OFFLINE=1
# Preserve CUDA_VISIBLE_DEVICES exactly; device 0 is allocation-relative.

cd "$T41_PROJECT_ROOT"
mkdir -- "$output"  # Atomic collision check; never reuse a prior job directory.
child=''
forward_term() {
    if [[ -n "$child" ]]; then
        kill -TERM -- "-$child" 2>/dev/null || true
    fi
}
trap forward_term TERM INT

# setsid gives this child tree a process group for termination forwarding.
# This produces only a BLOCKED planning manifest with the present software.
# A future qualified runner must also stop new trials before its wall-time margin.
setsid "$T41_OVERLAY/bin/python" scripts/tune_yolov10.py \
    --config "$config" --evidence "$evidence" \
    --output "$output/training-plan.json" --execute &
child=$!
set +e
wait "$child"
result=$?
if kill -0 "$child" 2>/dev/null; then
    wait "$child"
    result=$?
fi
exit "$result"
