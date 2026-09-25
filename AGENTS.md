# SDP-I-RayGuard

Read `docs/status.md`, the active item in `docs/tasks.md`, and `docs/meeting_minutes/README.md`.
Read the latest applicable meeting companion/follow-up, then the relevant `docs/context.md`,
`docs/research.md`, and `docs/architecture.md`. Preserve older obligations unless explicitly
amended; flag unresolved deadline conflicts. Shared summaries are in Git; original PDFs,
filled schedules and personal/session records stay local. Read `docs/README.md` and
`CONTRIBUTING.md` for the portable team workflow; `docs/tasks.md` is the only backlog.

- Meeting minutes establish agreed direction; the proposal retains broader requirements.
  Papers report experiments, inspected releases establish implementation details.
  Separate recorded requirement, paper finding, project recommendation, unresolved question.
  Label implementation evidence documented, artifact inspected, or executed and verified.
- Preserve the published test split. Never invent category IDs, physical groups, predictions,
  metrics, student contributions, or inferred benign outcomes from empty detections.
- Keep code small enough for each contributor to explain. Name coordinate conventions and
  category namespaces explicitly. Model dependencies belong in a separately verified environment.
- Keep scans, weights, credentials, private paths and source PDFs out of commits.
  Work with authorized external artifacts; no publication or large jobs as part of scaffolding.
- Run `uv run --locked ruff check .` and `uv run --locked python -m pytest` for code changes.
  Synthetic tests are software checks, not real-data validation or inference evidence.
- Update the active task and shared `docs/progress.md` with actual commands, outcomes,
  ownership, limitations and next action. Detailed session/private evidence may be kept in
  ignored `docs/logbook.md`; that file is not required to start from a fresh clone.
  Do not invent student authorship or hours. Status is the short handoff.
- Use one coordinator for dependencies/shared status and separate file ownership or worktrees
  for parallel edits. Review label correctness, leakage and unsupported claims independently.
  One owner per GPU job/output directory; agent output still requires verification.
- Use the four focused workflows in `.agents/skills/` when their task applies. No custom
  orchestration or global configuration changes are required. These reviewed project files
  are shared; personal client settings, credentials and session histories remain ignored.

Keep `main` integrable. Merge small workstream increments and bring shared fixes into both
`prototype/p1-single-scan` and `prototype/p2-multiscan`. Do not reset existing work.
