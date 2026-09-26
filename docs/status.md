# Current project status

Updated 27 September 2026. Read [tasks](tasks.md), [meeting records](meeting_minutes/README.md)
and [the plan](plan.md) for the authoritative backlog and requirements.

## Immediate priorities

- **T26/T27/T21:** agree the five-student repeated rota, obtain the lab protocol and
  complete ten collection sessions by **15 October**. Slots, quota and human leads
  remain unassigned. Only published-dataset acquisition has been reported.
- **T28/T23:** rehearse the laptop GUI and poster on **Embedded Explosive Detection
  in Electronic Devices**, ASAP for SLG. The visit date and intended lab pairing
  remain unknown; **30 September poster submission** still applies.
- **T22:** register all five students for 6G; confirmations remain unreported.
- **T29/T30:** inspect the distributed base model early, adapt/evaluate after usable
  Batch 1, then collect a broader two-week batch after midterms and retrain.
- **T32/T24:** Hardik's separate colorization phase 1 is due **15 October**;
  his registration/video are separate actions with no exact video deadline supplied.

**Schedule conflict:** M01's P1/P2 targets were **8/15 October**. M02 places adaptation
after Batch 1 collection. T10/Q9 must reconcile these obligations; no replacement
prototype dates or cancellation have been supplied.

## Application and research repositories

The GUI now lives in [RayGuard-App](https://github.com/abdalrahman-ismaik/RayGuard-App). Make app changes there; use its
[single launcher and setup guide](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/README.md). Its `engine/` submodule
pins this repository's shared contracts, model catalog, detector tooling and
runtime profiles at `b7ec59e`. Research, CPU audits, P1/P2 and the sole team backlog
remain here. Original local app files and services were preserved as an ignored
recovery copy, not an active second GUI source tree. Attribution distinguishes the
owner's GUI direction/maintenance, assisted implementation and team/upstream work.

The [extraction checks](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/migration.md) passed: root lint/143 CPU
tests, app lint/280 API tests, production build and 149 browser checks. Fresh real
CPU/GPU qualification and two ordinary generic YOLO runs passed in the new folder:
a training-image positive and the retained test-image miss. These diagnostics are
separate from synthetic software checks and do not establish accuracy or benignness.

The app implements upload, automatic folder receipt, finite test replay, actual
boxes/scores, verified generic reference comparisons, zoom/pan/magnifier, viewing
adjustments, themes, processing/completed split view, model/device choice, notes,
session history and JSON export. Three inspected YOLOv10 tasks have bounded execution
evidence; other families remain unavailable. Empty detections are never a safe verdict.
Queues/history are session-only. The scanner/interface is unconfirmed; published-image
replay is not a real scanner connection. Other-host GPU/CPU qualification and human
rehearsal remain open. Details and prior diagnostics are in the app documentation.

## Research evidence and open work

CPU audits, strict JSON contracts and genuine generic/device/specific YOLO execution
exist. [Data audits](verification.md) retain unresolved label disagreements, geometry,
cross-split duplicates and physical-group provenance. Published splits are unchanged.
Full P1 association/decisions, distributed P2 fusion, new model training/evaluation and
lab collection are unfinished. Human model/GUI ownership must be accepted explicitly.

Collaboration rules and owner-reviewed PRs with required Linux/Windows CPU checks are
active on the shared SDP branches. Teammate usernames/invitations remain pending under
T31; repository visibility is not proof of access or understanding. No completion of
registration, poster submission or collection is inferred from this technical work.

See [progress](progress.md) for dated engineering records, [verification](verification.md)
for evidence boundaries and [logo exploration](logo-exploration.md) for the private,
unselected identity studies. Student contributions and hours remain separately evidenced.
