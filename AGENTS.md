# SDP-I-RayGuard

**Owner amendment, 21 November — shared execution:** named task leads are contacts,
not exclusive owners. Prioritize assigned work. A student may complete a small blocking item in another lane's unfinished
work without waiting for its lead. Record task/scope and actual editor, notify affected
teammates and proceed on an isolated branch/worktree; notification is not permission.
Coordinate overlapping active edits and shared GPU/output use. Preserve existing work,
independent technical review, protected-branch rules and actual contributor credit.
This supersedes older person-specific file exclusions and named-person handoff gates;
scientific/data/environment gates and human-only GitHub actions remain in force.

For all report-related work, read `docs/final-report-requirements.md` first. The
Fall 2026 handbook is the primary course authority; specific notices amend logistics.
The owner requires canonical LaTeX source, a professional PDF and a checked Word
submission copy unless PDF acceptance is confirmed. Preserve handbook coverage,
verified paper/project/meeting sources, visual provenance, Gantt chart, applicable
forms and both SDP I rubrics. T38 in `docs/tasks.md` owns delivery state. Target
24 November 2026, 17:00 UTC+4; do not infer results, signatures or publication permission.

The GUI now lives in https://github.com/abdalrahman-ismaik/RayGuard-App.
Its pinned `engine/` submodule consumes this repository's shared model/contracts
code. Make GUI edits in that separate checkout. A remaining local `app/` is an
ignored pre-migration copy kept for running sessions, not an active source tree.

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
- AI agents may inspect, draft and edit agreed project files, but they are never GitHub
  contributors: no agent account, bot identity, author/committer/co-author metadata,
  agent-authored commit, push, PR, review comment or collaborator invitation. Each human
  student reviews their diff and personally runs their own Git identity, commit and push
  commands. An agent may suggest commands but must not execute them. Keep agent sessions,
  transcripts, generated client settings and local state out of Git. The reviewed project
  guidance in `AGENTS.md` and `.agents/skills/` remains team-owned documentation.
- Use the four focused workflows in `.agents/skills/` when their task applies. No custom
  orchestration or global configuration changes are required. These reviewed project files
  are shared; personal client settings, credentials and session histories remain ignored.

Keep `main` integrable. Merge small workstream increments and bring shared fixes into both
`prototype/p1-single-scan` and `prototype/p2-multiscan`. Do not reset existing work.
