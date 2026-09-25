# Working together on RayGuard

Start with the [documentation index](docs/README.md), [status](docs/status.md) and the active
[task](docs/tasks.md). Read the latest applicable meeting record and relevant architecture/
contracts before implementing. Everyone should be able to explain the code they submit.

## First clone and CPU setup

Install Git, Python 3.12 and uv. From a terminal:

```text
git clone https://github.com/abdalrahman-ismaik/SDP-I-RayGuard.git
cd SDP-I-RayGuard
uv sync --locked
uv run --locked python -m sdp_xray.cli doctor
uv run --locked ruff check .
uv run --locked python -m pytest
uv run --locked python -m sdp_xray.cli audit-coco tests/fixtures/synthetic_coco.json
```

The doctor may report missing artifact paths or GPU support on a new machine; that is not a
failed installation. The fixture audit is a **synthetic software check**, not baggage-data
validation. Neither command performs detector inference. See [verification](docs/verification.md).

Copy `configs/project.example.json` to ignored `configs/project.local.json` and enter your
own authorized artifact paths only when available. Do not copy another member's absolute paths.
Scans, weights, source PDFs and generated outputs are deliberately absent from Git.

The detector uses a separate environment. `uv sync` installs the CPU audit tools, not PyTorch
or YOLO. Follow [the recorded inference setup](docs/first-inference.md); its original backend
inherited local packages, so a fresh machine must independently verify compatible dependencies.
Do not assume that the lab's reported-ready demo/distributed model is the same artifact.

## Working with agents

The repository includes shared [agent instructions](AGENTS.md) and four focused project
skills. Read these from the current checkout so people and tools use the same requirements.
No personal settings or conversation history are needed. If a client does not discover them,
explicitly ask it to read `AGENTS.md` and the relevant skill file; do not assume every tool
loads repository guidance automatically.

| Task | Shared skill |
|---|---|
| Inspect IEDXray annotations, images and split findings | [iedxray-data-audit](.agents/skills/iedxray-data-audit/SKILL.md) |
| Verify a checkpoint/config pairing and execute a real detector baseline | [baseline-reproduction](.agents/skills/baseline-reproduction/SKILL.md) |
| Evaluate real predictions, thresholds, failures and timing | [detection-evaluation](.agents/skills/detection-evaluation/SKILL.md) |
| Rehearse the early GUI showcase or a full prototype demonstration | [prototype-demo](.agents/skills/prototype-demo/SKILL.md) |

A useful task handoff names the task ID, permitted files, existing work to preserve and
expected evidence. For example: "Read AGENTS.md and the applicable project skill, inspect
the current T28 state, then implement the agreed GUI scope. Preserve existing changes and
record actual checks and limitations." A skill is workflow guidance, not evidence that its
target capability is implemented. Dataset/model access and a compatible backend remain
separate prerequisites. New lab formats/taxonomy need inspection before using existing audits.

Only reviewed root guidance and the four skill files are shared. Keep personal client
configuration, session histories, overrides and credentials local. Review any guidance/skill
change like code; user instructions and agreed project requirements still govern the task.

## Claim one task and use a small branch

Agree a task ID, editor, reviewer, file scope and output directory before editing shared work.
Record the accepted assignment in `docs/tasks.md`; do not infer assignments from branch names.
Use a clean worktree and a short task branch, for example:

```text
git fetch origin
git switch -c task/T28-gui-demo origin/main
```

The branch name is an example, not an assignment or a claim that the GUI is implemented.
If you already have work, commit it appropriately or use a separate worktree before switching.
Do not reset or overwrite another contributor's branch to make it match your clone.

`main` is the integration branch. `prototype/p1-single-scan` and `prototype/p2-multiscan` are
shared workstream branches, not personal workspaces. Merge small reviewed increments into
main and bring shared fixes into both workstreams with normal merges, preserving their work.
Resolve conflicts with the affected owners; do not force-push over teammates' commits.

## Protected branches and review

The following policy is being configured under T36; activation is not yet verified.
It covers `main`, `prototype/p1-single-scan` and
`prototype/p2-multiscan`. Work on a task branch and open a PR against the agreed target.
Teammates can use branches in this repository after accepting a collaborator invitation,
or submit a PR from a fork without write access.

- Require the repository owner's code review through [CODEOWNERS](.github/CODEOWNERS).
  One generic approval from another collaborator does not replace the code-owner review.
- New reviewable commits dismiss stale approvals. Resolve review conversations before merging.
- Require both `CPU (ubuntu-latest)` and `CPU (windows-latest)` from GitHub Actions, with
  the branch tested against the latest target. These are software checks, not model evaluation.
- Block direct changes, force-pushes and deletion of the three shared branches; use PRs to
  bring shared fixes into each prototype branch as well.

Configure an owner-only **PR-only review bypass** because GitHub does not allow authors to approve
their own PRs. Use it deliberately for owner-authored or administrative changes, and seek
teammate review when available. Keep separate CI/history rules with **no bypass**, including
for the owner. A bypass is not a recorded approval or student sign-off. Collaborators may
click Merge once the required approvals and checks pass; ownership does not reserve that button.

Rules live in [GitHub repository settings](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/settings/rules),
not in the local Git configuration. See T36 and [verification](docs/verification.md) for the
actual setup result. Invitations and each member's access remain separately tracked in T31.

## Evidence and review rules

- Follow the latest explicit meeting/follow-up decisions. Keep earlier obligations unless
  amended; retain the unresolved old prototype-date conflict until an advisor clarifies it.
- Separate recorded requirements, paper findings, recommendations and unresolved questions.
  Label implementation claims documented, artifact inspected, or executed and verified.
- Preserve published test splits. Never invent category IDs, physical groups, predictions,
  metrics or student contributions. Empty detections do not mean benign.
- Keep coordinates/category namespaces explicit and code small enough to explain. Model
  dependencies stay outside the CPU audit environment.
- Use separate file ownership or worktrees for parallel work. One person owns each GPU job
  and output directory; agree resources before launching larger jobs.
- Treat generated suggestions as unverified until reviewed. A successful software test is
  separate from real-data validation, model inference and model-performance evaluation.

| Work type | Minimum evidence before claiming completion |
|---|---|
| Dataset audit | Actual source/hash/task/category inspection; image checks and split/group overlap findings; preserve originals |
| Baseline execution | Matching checkpoint/config/class order, pinned environment, genuine predictions/overlay and run manifest |
| Evaluation | Real saved predictions, justified split/metrics, operating threshold and explicit timing boundaries |
| GUI/demo | Verified model scope, runnable view, visible failure/empty states, clean-start rehearsal and limitations |

## Before sharing a change

1. Run `uv run --locked ruff check .` and `uv run --locked python -m pytest` for code changes,
   plus relevant real checks when artifacts are available. Record actual outcomes and limits.
2. Update the canonical task and add concise evidence to [progress](docs/progress.md) or the
   relevant technical record. Update status/decisions only when their information changes.
3. For documentation changes, check local links and source/date/ownership accuracy. A new
   clone must not need ignored files to understand a tracked page or follow its public links.
4. Review `git status --short` and `git diff --cached` after staging explicit intended paths.
   Keep credentials, data, weights, personal details and private journals out of the commit.
5. Push your task branch and open a pull request for the agreed reviewer. The repository owner
   must grant collaborator access or you must use a fork; a public clone does not grant push rights.

Repository access, student review and contributions remain unconfirmed until each person
records them. Do not credit tool-generated work as a student's understanding or invent hours.
