# Implementation and demo plan for November 2026

**Planning status: proposed, not yet accepted by the students or supervisor.** The immediate engineering outcome is a first integrated prototype draft that visibly follows the original proposal's acquisition/input, preprocessing, detection, evaluation-evidence and GUI/recording path. It is a prototype to defend with truthful evidence, not a claim that every requirement or operational capability is complete. The sole backlog remains [tasks.md](tasks.md); T39–T43 are proposed work packages for this plan.

## Dates and outcome

- **14–15 November:** confirm the assigned presentation time, demo scope, names/GitHub handles, owners/reviewers and access to the presentation machine. The report cutoff is **24 November 2026, 5:00 pm UTC+4** per the explicit Blackboard due-date field; another supplied announcement says 27 November, so retain that conflict and confirm it.
- **16–18 November:** parallel, small work packages on separate branches and owned files. No shared GPU run or shared output directory without one named owner.
- **19 November:** integrate accepted changes, freeze a demo candidate and rehearse clean startup. This makes the team ready if the supervisor chooses the optional **20 November** presentation.
- **20 November:** present only if the supervisor assigns/approves this early option; otherwise use it as a rehearsal checkpoint.
- **21–23 November:** complete the report, contribution table, slide deck, source/run references and a second full rehearsal. Freeze report content with time for review.
- **24 November by 5:00 pm UTC+4:** one group Blackboard submission; then email the same report to supervisors and examiner and commit the submitted copy to GitHub. Retain private receipts.
- **25–26 November:** individual explain-backs, Q&A practice and final presentation-machine rehearsal.
- **27 November, 8:00 am–12:00 pm:** stated final presentation window, 20 minutes plus 10 minutes Q&A, pending assigned slot/room confirmation.

## Scope gates

1. **Demonstration claim:** use only a model/checkpoint/task pairing already inspected and genuinely executed. Verify the presentation-machine setup, exact revision and selected input. Distinguish synthetic UI checks, real model runs, accuracy evaluation and lab scanner integration. A saved-run fallback must be labelled recorded; never present it as live inference.
2. **Model work:** T14 records that HPC credentials/manuals were issued, but login, password change, permissions, model pairing and job submission remain unverified. First inspect the attached manuals from the original email, change the initial password at first login, and verify the intended model/config/class map. Run one batch-one smoke test only after one owner, output directory and approved input are agreed. No broad training or large job is on the critical path.
3. **Evaluation claims:** do not tune thresholds on the published test split. Report accuracy metrics only with matching task-specific ground truth, class map, split provenance and a frozen protocol. The new collection count of 478 distinct byte payloads is not an evaluation set: labels, QC and physical/case grouping are unresolved. Do not turn empty detections into a benign outcome.
4. **Data handling:** raw scans stay on the lab computer. Do not use AI tools with raw scans, credentials, student IDs, private paths or filled manifests. Share sanitized aggregate evidence only.
5. **Scope control:** close only observed demo blockers. Do not add features to create a contribution, invent taxonomy/grouping, or claim full P1/P2 from the GUI. If a planned code lane finds no justified gap, submit a reviewed technical note or a meaningful test rather than speculative code.

## First-draft prototype acceptance map

The original proposal is the product brief. The prototype should show one coherent path from an authorized X-ray image to a model result, operator review and a traceable record, while the report names the gaps against the broader brief.

| Proposal requirement | First-draft prototype evidence | Current limit / decision gate |
|---|---|---|
| Acquire 500 positive and negative baggage scans | Use the public IEDXray release as the single-scan dataset source; document source, labels, sample selection and split. If proposing a 500-image subset, get approval and verify both positive and negative composition. Track dismantled scans separately as collection progress. | The 478 distinct dismantled images count toward the dismantled-threat collection, but are not the single-scan training/demo/evaluation set. Their detector labels, QC and groups are unreviewed. |
| Preprocess scans | Put a named, versioned preprocessing step in the shared image-to-model path and record its settings; compare against identity preprocessing only if time and valid data support it | Do not add enhancement by assumption. Document whether the supplied model expects a specific transform and whether the scanner exports match it. |
| Detect and localize explosives | Use the exact CVMI-provided, task-matched checkpoint already configured for the GUI, after recording its file hash/source/task; show real class, score and box overlay. Compare a fine-tuned candidate only if it remains the same task. | Existing records verify a generic YOLOv10-M checkpoint and real smoke inference; the exact identity of the current GUI-configured artifact must be confirmed. Keep known miss/error examples visible. |
| Evaluate on unseen data with metrics | Produce a reproducible evaluation protocol and, only when labels/splits qualify, matching metrics and failure examples | Existing annotation/split findings and checkpoint training provenance block an unqualified “unseen” or “strong” result. Never tune on the published test split. |
| GUI for control and recording | Demonstrate image intake, run/clear or review controls supported by the app, result visualization and a run-linked record/export | Describe what is session-only and what the current interface cannot do; do not claim scanner control unless tested with the lab hardware. |

The presentation should walk through the actual vertical slice, then map each proposal requirement to **demonstrated**, **partially demonstrated**, or **not yet verified** evidence. The report should include the same map, model/data provenance, decisions, measured results (if eligible), limitations and each student's evidenced contribution. Synthetic fixtures can demonstrate interface behavior but must be identified as synthetic.

### GUI polish acceptance checklist

Abd and Mohammad should inspect the current app before editing and keep its active visual direction. Turn findings into a prioritized, owner-per-file fix list; do not redesign the GUI just to create activity. Verify the interface supports the proposal's operator outcomes:

- Image upload/replay/receipt paths clearly show source and status. The real scanner is unverified; never label folder receipt or replay as scanner control.
- Inference starts only by explicit user action. The selected model/task and run identity remain visible and match the actual backend run.
- Detections and any eligible published reference boxes remain separate, in original-image coordinates, with class/score and provenance. Empty predictions never display “safe”, “benign” or clearance.
- Controls, progress, errors, unavailable model, no detections, completed result and held human review each have distinct truthful states. A failure must not look like a successful empty result.
- The operator can inspect the scan, record a review note and export/retrieve the run evidence supported by the app; display adjustments must not silently change model inputs or saved coordinates.
- Review route transitions, refresh/back behavior, narrow screens, keyboard focus, contrast in light/dark palettes, reduced motion and preservation of selected scan/draft state.
- Record each mismatch, evidence/reproduction, owner, agreed fix and check. Separate cosmetic polish from requirement blockers, and validate the final end-to-end path on the intended presentation machine.

The acceptance checklist is a review plan, not evidence that these behaviors have been re-tested in this turn.

## Proposed student work packages

Names below follow the supplied HPC email and collection folder labels. These are **proposed owners**, not evidence of acceptance, skill level or prior contribution. Confirm spelling and GitHub handles, including Mohammad/Mohammed, and each person's availability. Every student owns a distinct deliverable, personally commits/pushes under their own GitHub identity, updates the shared [team progress file](progress.md) with their own evidence, and explains the work. Abd and Mohammad also review the ML pipeline against the GUI/report outcomes.

| Proposed owner | Work package and owned area | AI/agent assignment | Review and completion evidence |
|---|---|---|---|
| **Abd Alrahman Basim Ismaik** | **T39 — GUI requirement fit, polish and demo integration.** Own the proposal-to-GUI checklist, visual/interaction issue triage, targeted polish/refactors in agreed files, integrated demo path and runbook. Continue from the existing in-progress RayGuard-App work after recording its status; coordinate file ownership with Mohammad. Review ML contracts and the final result/provenance display with the ML owners. | Ask an agent to map routes/states to proposal/app requirements, identify reproducible mismatches and propose a prioritized fix list before edits. It may draft agreed files but cannot commit, push, create a PR or modify another student's owned files. | Review by Mohammad. Evidence: requirement-to-screen checklist, reviewed changes, required app checks, truthful empty/error states, real-run provenance if executed and timed rehearsal. Keep private scan/run evidence local. |
| **Faisal Daoud Alzarooni** | **T40 — ML baseline adapter and reproducible run path.** Own the baseline side of the shared single-scan interface: verify checkpoint/task pairing, connect batch-one inference to the shared prediction/run-manifest contract, and document preprocessing/environment. Coordinate HPC access and manuals; run a bounded diagnostic only after prerequisites and input/job approval. | Ask an agent to inspect the existing inference/catalog/API and propose the smallest adapter and contract first. No credential, raw scan or private path in prompts; no agent Git operations. | Review by Abd and Mohammad for prototype/result-display fit; Ahmed/Ali confirm interfaces. Evidence: code and required checks, plus a real run manifest only if authorized and executed. |
| **Ahmed Fadhel Salem Rashed Almansoori** *(folder label: Ahmed Almansoori; confirm identity)* | **T41 — fine-tuning candidate.** Own fail-closed COCO preflight, training/config/manifest draft and separate training-environment proposal. Do not train on dismantled data or change the published split. | Use the [single-scan ML plan](single-scan-ml-pipeline-plan-2026-11.md) as the project brief. An agent may map requirements and propose the smallest candidate design before implementation. Use synthetic fixtures only; no agent Git operations. | Review by Ali and Faisal for ML correctness; Abd and Mohammad review proposal fit and result/provenance integration. Real training remains gated by approved data/validation policy, compatible environment, HPC and named job/output owner. |
| **Ali Arif Saeed Alshamsi** | **T42 — independent evaluation candidate.** Own prediction export/evaluator, frozen protocol, metrics and failure-analysis code. Preserve the source split and keep threshold selection off test. | Ask an agent to audit the runner/evaluator and data blockers, then propose a protocol and code boundary. No raw scans, credentials, private paths or test-tuned thresholds in prompts; no agent Git operations. | Review by Ahmed and Faisal for evaluation correctness; Abd and Mohammad validate GUI interpretation/provenance. Synthetic checks are software evidence only; real metrics require approved labels/split policy. |
| **Mohammad Arwani** *(called Mohammed by the owner; confirm roster spelling/GitHub handle)* | **T43 — GUI flow polish and acceptance.** Pair with Abd on route/state review, responsive layout, accessibility and visual consistency. Own a separate component/test/docs slice and fix observed requirement mismatches; validate truthful live, error, empty and held-review states. Review ML outputs where they appear in the GUI. | Ask an agent to map current E2E coverage and proposal/UI requirements, then suggest owned files and targeted checks. It may draft agreed files but must not commit, push or create GitHub activity. | Review by Abd; Mohammed personally commits under his GitHub account, completes app checks and a human walkthrough, and explains the changes. Synthetic fixtures remain distinct from real inference. |

The three ML lanes are complementary parts of one prototype, not three competing end-to-end stacks. Before coding, Faisal, Ahmed and Ali should agree on one image/input contract, one prediction schema (original-image `xyxy` boxes, confidence, explicit category namespace), one run-manifest format and one evaluation input format. Each may submit a short alternative design or an isolated candidate component; implement alternatives only where a real uncertainty exists and each can be compared fairly. Merge the smallest compatible pieces that have evidence. The existing three YOLO checkpoints represent different tasks/classes, so they are not interchangeable model candidates for a generic-explosive comparison.

If any proposed owner cannot take the lane, the coordinator should agree a replacement with that student and update T39–T43 before work starts. Keep one editor per file set. The report/presentation coordinator must not claim another student's work; individual authorship comes from the actual PR, commits, review and explain-back.

Use [prototype-demo](../.agents/skills/prototype-demo/SKILL.md) for T39/T43 and the final vertical slice; T40 uses [baseline-reproduction](../.agents/skills/baseline-reproduction/SKILL.md); T41 also reads [iedxray-data-audit](../.agents/skills/iedxray-data-audit/SKILL.md); T42 uses [detection-evaluation](../.agents/skills/detection-evaluation/SKILL.md). The detailed single-scan design brief is in [the ML pipeline plan](single-scan-ml-pipeline-plan-2026-11.md).

## Kickoff and AI workflow

Run a 30–45 minute team session on 14 or 15 November. Decide: (1) supervisor's actual presentation slot; (2) one honest demo scope and two representative states (successful output and a known miss/error or empty state); (3) model/input approval and machine; (4) role acceptance, GitHub handles and reviewers; (5) report section/slides per person; and (6) one current limitation to explain clearly. Capture decisions/actions and unresolved points in meeting minutes.

An agent may receive a bounded work request naming the task ID, public docs and approved files. The student must request a proposed plan/diff explanation and personally inspect the actual edits. Agents may not use GitHub accounts or perform Git mutations. If asked, they can suggest commit/push commands only; the student reviews and executes the chosen commands. Do not place prompts, sessions, transcripts, client state, or credentials in Git.

Student responsibilities: accept a bounded task, inspect and verify the changes and evidence, personally perform all GitHub activity under their own identity, and explain the result. AI-generated code is not evidence until the student understands and verifies it. Record AI assistance according to the course handbook without publishing private prompts.

At each meaningful checkpoint, the student owner adds a dated update to the shared `docs/progress.md` using its template: task/status, work completed, files and PR/commit, exact checks/results, blockers/decision owner, and next action/owner. Update `docs/tasks.md` when task state, owner, due date or next action changes. For app work, also keep `RayGuard-App/docs/progress.md` current and link its reviewed PR/commit from the team-wide log. Coordinate one editor per progress file at a time.

## Integration and acceptance gates

### Gate 1 — work is reviewable

- Each owner has a task ID, isolated branch/worktree, bounded file list, one reviewer and one stated acceptance result.
- Before code, the owner reads `git status` in that checkout. The RayGuard-App working tree already has uncommitted changes; do not reset, stash over, or edit another owner's files.
- Engine changes are made in SDP-I-RayGuard first, reviewed and tested; only then may RayGuard-App update its pinned engine commit and run its own integration checks.
- Code changes in this repository run `uv run --locked ruff check .` and `uv run --locked python -m pytest`. App backend changes run its documented locked Ruff/pytest; frontend changes run build and the targeted Playwright checks. Do not run model jobs during general CI.

### Gate 2 — demo candidate by 19 November

- Record the app commit, pinned engine revision, model/task/checkpoint hash, runtime/device and exact clean-start steps.
- Rehearse the complete user path with an authorized input; show actual output/provenance and at least one known limitation or failure state. Explain that an empty result is not a benign verdict.
- Confirm demo duration and handoffs fit the assigned slot. Mark any fallback as prerecorded/recorded evidence.
- Collect reviewer notes and fix only demo-blocking issues. Freeze a candidate revision; any later fix gets a focused regression check and a short re-rehearsal.

### Gate 3 — submission and assessment evidence

- **GitHub record (15%):** each student's PR/commits, documentation, review and explain-back are traceable. No activity padding or AI-only attribution.
- **Final report (20%):** include objectives/scope, method/architecture, implementation, verified results, limitations/references, GitHub URL and an honest per-student contribution table. Include signatures/forms required by the handbook/current Blackboard instructions.
- **Presentation (20%):** prepare a 20-minute story with readable visuals, technical explanation, ownership transitions and timing; separately rehearse the live demo. A possible division is 2 min problem/scope, 4 min architecture/data, 6 min implementation by owners, 6 min results/demo, 2 min limitations/next step. Adjust to the actual presenters and slot.
- **Live demo (25%):** demonstrate the integrated workflow on the agreed setup, representative real execution, output review/export and failure handling. Do not pass browser mocks or a recorded fallback off as live inference.
- **Q&A (20%):** every member prepares a 60–90 second explanation of their own contribution and can discuss one design choice, one failure/limitation and what they personally verified.

Keep private submission receipts, filled per-image manifests, scan identities and credentials off Git. Record completion in `docs/progress.md` only after the named owner/reviewer has supplied evidence. This plan itself is a proposed workflow, not completed student contribution.
