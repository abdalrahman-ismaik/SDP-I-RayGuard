# SDP-I-RayGuard

Khalifa University senior design: **AI-Powered Explosive Detection in X-ray Scans**.
Advisor: Prof. Naoufel Werghi; technical guidance: Dr. Divya Velayudhan.

This is a CPU repository bootstrap. **Real model inference has not been verified.**
Implemented: environment/access reporting, COCO annotation and optional image/split audits,
validated JSON interfaces, synthetic tests, and project records. P1 prediction, P2 fusion,
training, COCO model evaluation, overlays and GUI are not implemented; prediction interfaces
raise `NotImplementedError`.

| Milestone | Scope | Deadline |
|---|---|---|
| Prototype 1 | One scan: device class, suspicious-region localization, benign/modified distinction | 8 October 2026 |
| Prototype 2 | Correlate component evidence across scans/bags | 15 October 2026 |

One repository retains its chosen name. Python imports use `sdp_xray`; the installable package
is `sdp-rayguard`. Shared code lives on `main`, with temporary workstreams
`prototype/p1-single-scan` and `prototype/p2-multiscan`. Team 1 jointly owns P1; P2 ownership
is unconfirmed. YOLOv10-M is a provisional investigation choice, contingent on a matching
task checkpoint/config/class map and compatible environment.

## CPU setup

Prerequisites: Git, Python 3.11–3.14, and uv. Bootstrap verification uses Windows/Python 3.12
and uv 0.11.15; other Python versions are allowed by package metadata but not locally tested.
The resolved `uv.lock` pins runtime and development dependencies. Pillow is the only runtime
dependency; GPU packages are intentionally separate.

From the repository root:

```text
uv sync --locked
uv run --locked python -m sdp_xray.cli doctor
uv run --locked python -m sdp_xray.cli doctor --config configs/project.example.json
uv run --locked python -m sdp_xray.cli audit-coco tests/fixtures/synthetic_coco.json
uv run --locked ruff check .
uv run --locked python -m pytest
```

See [actual verification results](docs/verification.md). A successful synthetic audit only
checks the software and fixture; without image roots and verified physical-group metadata
it does not establish image integrity or absence of physical leakage.

Copy `configs/project.example.json` to ignored `configs/project.local.json` and fill only
verified paths/settings. `null` means unresolved. `doctor --config configs/project.local.json`
checks path presence/type, not file compatibility. Paths in the config are relative to that
config's directory; shell `SDP_*` paths are relative to the current directory. Environment
variables override config paths. `.env.example` is documentation; `.env` is not auto-loaded.
`task`, `upstream_revision`, and `physical_group_key` record future integration settings;
doctor does not claim to validate them. No category IDs have been assigned for real data.

The audit accepts `--image-root`, `--other`, `--other-image-root`, and `--group-key`; use
`audit-coco --help` for syntax. It never downloads or modifies inputs. Exit 0 means the
implemented checks found no errors (inspect warnings); 1 means audit findings; 2 means
invalid CLI/config input. Doctor returns 0 even when optional resources are missing.

## Next task and navigation

Start **T02**: obtain authorized dataset/annotation paths and a paired checkpoint/config/class
map from the lab. Inspect one real annotation file before choosing a backend or conversion.
The local RTX 2060 has 6 GB VRAM; framework compatibility and inference capacity remain untested.

- [Context and open advisor questions](docs/context.md), [research evidence](docs/research.md)
- [Architecture](docs/architecture.md), [JSON field contract](docs/contracts.md), [decisions](docs/decisions.md)
- [Plan](docs/plan.md), [task source of truth](docs/tasks.md), [current handoff](docs/status.md)
- [Contribution logbook](docs/logbook.md), [data](data/README.md), [models](models/README.md)

Source PDFs remain local and ignored, including the selection form's student identifiers.
No data, weights, secrets, or remote publication belongs to this bootstrap.
