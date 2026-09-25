# Verification record

Updated **25 September 2026**. This record separates software checks, real-data inspection,
static checkpoint inspection and actual model inference. The team-sharing update reran CPU
software checks in a fresh copy of the public candidates; data audits and model inference
below are earlier recorded outcomes. Student review remains pending; no student contribution
or sign-off is inferred.

## CPU software checks

Latest local check: **25 September 2026**, during collaboration setup. `uv run --locked ruff
check .` passed and `uv run --locked python -m pytest` passed **85 tests in 5.54 seconds**.
The CI workflow now names its two jobs explicitly for required-check configuration. Both
hosted jobs subsequently passed in the setup PR, as recorded below; local and hosted results
remain separate evidence.

Earlier software check: **24 September 2026**, in a fresh directory containing the **50 public
files prepared before the agent-guidance follow-up**, without private instructions,
configuration, data, checkpoints or environments.
This was a local export of pending changes, not a clone of a newly published commit.

| Check | Recorded outcome |
|---|---|
| `uv sync --locked --offline --python 3.12` | Passed; new environment built using the local package cache, Python 3.12.12 |
| `uv run --locked ruff check .` | Passed |
| `uv run --locked python -m pytest` | **85 tests passed in 4.78 seconds** |
| `uv run --locked python -m sdp_xray.cli doctor` | Exit 0; artifact paths unconfigured and PyTorch absent, as expected for CPU setup |
| `uv run --locked python -m sdp_xray.cli audit-coco tests/fixtures/synthetic_coco.json` | Exit 0; synthetic annotation fixture accepted. Image files, physical groups and split overlap were not checked |

The export checks establish local CPU setup from the intended shared files. They do not
verify a new machine's network/package access, model dependencies or hosted CI. No model,
dataset download or training was launched. Only documentation/result records changed after
this run; production code and dependency files were unchanged throughout the sharing update.

An earlier **24 September** normal-workspace pre-publication check passed Ruff and **85 tests
in 3.07 seconds**.

An earlier **23 September** check in an isolated copy of the reviewed public files passed
Ruff and **85 tests in 3.43 seconds**. That separate check supports local installation from
the shared files; it is not a remote CI result.

The suite checks annotation references, category maps, box geometry, image decoding,
path containment, duplicate/split findings, JSON contracts, configuration and CLI behavior.
Tests use synthetic fixtures. Their success does not establish real-data quality or detector
performance. The historical 22 September implementation checks also recorded 37 subtests;
that is a separate recorded run, not an additional count asserted for the 24 September result.

Standard repository checks:

```text
uv run --locked ruff check .
uv run --locked python -m pytest
```

The CPU package was tested with Python 3.12 and a locked uv environment. A clean installation
also verified imports from the installed package rather than relying on source-path injection.
These local records do not establish hosted success; the separate 25 September run below does.

## GitHub collaboration verification — 25 September 2026

- [Setup PR #1](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/pull/1) merged as
  `5fac792`. Reviewed documentation, agent guidance and CODEOWNERS were then synchronized
  to both prototype branches by ordinary fast-forward updates before protection activation.
- [Hosted run 36129256939](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/actions/runs/36129256939)
  completed successfully with `CPU (ubuntu-latest)` and `CPU (windows-latest)`. These run
  the locked CPU software checks; no datasets/checkpoints or model inference are involved.
- [CI/history ruleset](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/rules/23994219)
  requires both observed check names from GitHub Actions (integration 15368), requires testing
  against the current base, blocks force-pushes/deletion and has no bypass actors.
- [PR/review ruleset](https://github.com/abdalrahman-ismaik/SDP-I-RayGuard/rules/23994221)
  requires one approval, code-owner approval, stale-approval dismissal and resolved review
  threads. Only the repository owner has a PR-only bypass; this is distinct from an approval.
- Both active rulesets were read back, and their effective rules were checked for `main`,
  `prototype/p1-single-scan` and `prototype/p2-multiscan`. GitHub returned no CODEOWNERS errors
  for each branch. Verification inspected configuration; no destructive push/delete probe ran.
- No collaborator invitations were sent: teammate usernames are pending. Repository visibility
  and passing checks do not prove individual student access, review or contribution.

## Shared documentation checks — 24 September 2026

- After adding shared agent guidance, all **187 relative Markdown links** resolve within
  the **55 intended public files**. The earlier 50-file review checked 178 links.
- Both original meeting PDF hashes are unchanged. Companions retain **16 decisions,
  32 actions and 19 open questions**; all five source student IDs are absent from shared files.
- All **35 task rows** have unique ordered IDs and valid states. The collection manifest
  has 15 fields and no sample records; the schedule has no actual availability or agreed slots.
- Private-record ignore checks and independent content reviews passed. Source PDFs, raw
  correspondence, filled schedules, detailed journals and machine-specific material remain
  outside Git. No production code, model artifacts or dependencies changed.
- Root `AGENTS.md` and four project `SKILL.md` files are included by explicit owner choice.
  All four passed the skill-creator `quick_validate.py` format/frontmatter check; their scope
  and references were separately reviewed against the latest meeting requirements. Validation
  is not evidence that a skill's model/evaluation/demo workflow has been executed.
- Eighteen ignore probes passed, including personal agent settings, sessions, nested local
  guidance and unreviewed skill files. This follow-up changed guidance/ignore rules only, so
  CPU tests were not rerun; the 85-test software result above remains the latest execution.
- These checks establish documentation consistency and sharing boundaries, not student
  access, completed collection, submitted materials or reviewed individual contributions.

## Real-data audits — 22 September 2026

| Supplied dataset | Executed checks and actual outcome | Limits |
|---|---|---|
| IEDXray | All 17,360 images decoded and matched declared dimensions; eight COCO files inspected. All four task-pair audits returned **exit 1 with findings**: four cross-split exact-byte pairs and 13 distinct boundary violations; cross-export joins additionally found 4,955 Mobile/Pager name disagreements. | Source images/annotations and published splits unchanged. Physical groups, original archive identity and authoritative label corrections remain unresolved. [Full audit](iedxray-audit.md) |
| STCray | All 46,642 images decoded/hashed and 45,693 rectangle JSON files parsed. Full audit returned **exit 1 with findings**, in 470.186 s: 10,949 dimension mismatches, 55 out-of-bounds boxes, 644 within-split duplicate pairs and no cross-split byte duplicates. | Geometry/version and physical provenance remain unresolved; optional for P1. [Full audit](stcray-audit.md) |

These are actual data findings, not synthetic test failures or model metrics. Representative
ground-truth overlays were visually inspected: six IEDXray examples and seven STCray examples.
No annotation repairs, split changes or automatic Mobile/Pager remapping were applied.
The [paper/annotation review](iedxray-paper-review.md) distinguishes published claims from
discrepancies in the supplied files.

## Checkpoint inspection — 22 September 2026

**Artifact inspected:** 18 supplied checkpoints across six model families, totaling
11,991,175,179 bytes, were hashed. All 22,550 archive members passed CRC checks; no two
completed files shared a hash. Static inspection examined embedded configurations, class
metadata and head shapes without executing the 15 non-YOLO checkpoints.

The [catalog](checkpoint-catalog.md) records concrete pairing issues, including specific
Faster R-CNN head/class inconsistency, Grounding DINO configuration metadata, Mobile/Pager
ordering and unmapped DETR outputs. Integrity checks do not establish task correctness.
Publisher checksums and exact training-source provenance remain unavailable.

## Genuine inference — 22 September 2026

**Executed and verified:** supplied generic-explosive YOLOv10-M checkpoint, original THU-MIG
source revision `453c6e38a51e9d1d5a2aa5fb7f1014a711913397`, Python 3.11.9,
PyTorch 2.9.0+cpu and torchvision 0.24.0+cpu. CPU FP32, batch one, confidence 0.25.

| Diagnostic input | Recorded model output |
|---|---|
| Modified-laptop test example | No detections: a miss on the annotated threat |
| Bare-IED training example | One detection, confidence 0.9702618 |
| Ordinary-laptop test example | No detections; this does not establish benignness |

Predictions, original-coordinate overlays and run manifests were saved and checked against
the shared scan-result contract. The positive box/score repeated exactly. Annotations were
read separately for context and did not generate predictions. A wrong-checkpoint-hash check
returned exit 2 before model load and created no output directory.

See [reproduction commands and limitations](first-inference.md). The training image may have
been seen during model training; the sample selection was diagnostic. No AP/recall estimate,
calibration result, application latency benchmark or generalization claim follows from these runs.

## Remaining verification

- Device-checkpoint execution and intended laptop/pager demo pairing.
- GUI implementation and a clean-start laptop demonstration.
- Full P1 integration, association/benign-decision policy, fine-tuning and fair evaluation.
- Distributed component taxonomy, real case/group labels, P2 fusion and model adaptation.
- GPU/HPC model execution, other checkpoint backends and FALCON.
- Real collection-session evidence, registration/submission confirmations and student explain-back.

Meeting-reported model readiness is documented availability only. Check [status](status.md)
and [tasks](tasks.md) for current ownership and dependencies. Source artifacts and detailed
run outputs remain outside Git; shareable summaries do not replace those underlying records.
