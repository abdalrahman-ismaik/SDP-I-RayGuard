# Current project status

Updated 25 September 2026. Start with [tasks](tasks.md), [latest meeting records](meeting_minutes/README.md)
and [the plan](plan.md). This is a short handoff; task state and ownership belong in the backlog.

## Immediate priorities

- **T26/T27/T21:** all five students agree one repeated two-week rota, obtain the lab protocol,
  then complete ten distributed collection sessions by **15 October**. Slots/quota remain
  unassigned; use the blank [schedule template](templates/collection-schedule.md).
- **T28/T23:** simple laptop GUI plus **Embedded Explosive Detection in Electronic Devices**
  poster ASAP for SLG. Visit date, GUI owner and intended model pairing remain unknown.
  The earlier **30 September poster submission** deadline still applies.
- **T22:** register all five students for 6G; actual confirmations are unreported.
- **T29/T30:** inspect the lab's existing distributed model early, adapt/train/evaluate after
  usable Batch 1, then collect a broader two-week batch after midterms and retrain.
- **T32/T24:** Hardik's separate colorization phase 1 is due **15 October**; his registration/
  video are separate actions with no exact video deadline supplied.

**Schedule conflict:** M01's P1/P2 targets were **8/15 October**. M02 puts adaptation after
Batch 1 collection. T10/Q9 must reconcile these obligations; no new prototype dates were supplied.

## What actually works

Repository collaboration setup is in progress under T36: shared documentation/agent guidance,
owner-reviewed PRs and required CPU checks. Teammate usernames and invitations remain pending
under T31; public visibility is not confirmation of individual access or understanding.

CPU audits, strict JSON contracts and the standalone generic YOLOv10-M runner exist.
[Real diagnostic inference](first-inference.md) ran on three images, including a missed threat
and a training example; it does not establish accuracy or benignness. [Data audits](verification.md)
completed with unresolved label, geometry, duplicate and physical-group findings.

P1/P2 interfaces are stubs. Device-model execution, full P1 decisions, distributed fusion,
training/evaluation and GUI are unfinished. The meeting's ready-model statement is not proof
that its exact model or GUI runs here. Source data/weights are acquired separately.

The last SDP collection report covered published datasets only. New lab sessions, registrations,
poster submission and new model adaptation remain unverified. Model/GUI/collection leads must
be accepted explicitly; branch names do not assign students.

See [verification](verification.md) for dated commands/results and [progress](progress.md) for
engineering evidence. Software tests, real-data audits, model inference and individual student
contributions are separate claims.
