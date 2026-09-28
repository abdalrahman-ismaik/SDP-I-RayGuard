# Current project status

Updated 28 September 2026. Read [tasks](tasks.md), [meeting records](meeting_minutes/README.md)
and [the plan](plan.md) for the authoritative backlog and requirements.

## Immediate priorities

- **T26/T27/T21:** Dr. Divya rejected the earlier overlap and requested final dates.
  The team revised two slots; the private rota now has no overlaps. The owner supplied
  **29 September** as the first Tuesday: Week 1 is **29 Sep–1 Oct**, Week 2 **6–8 Oct**.
  Send the dated proposal and obtain lab acceptance, including the shorter session.
  [Yonathan's catalogue F05/C01](meeting_minutes/follow-up-collection-2026-09-28.md#catalogue-handoff-f05c01)
  is received and inspected: **125 four-bag groups / 500 images planned**, 100 per student
  across Session A/B (48/52). It includes all four families and E4/B3 in Round 1, conflicting
  with F03's one-item weekly allocations/extras; confirm which assignments apply and map A/B
  to the proposed weeks. Confirm **29 September** guidance; the email's undated availability
  does not establish that booking. Annotation/export instructions, QC/negative controls and
  log owner remain open. Ten sessions precede **15 October**; no collection is reported.
  The earlier dated reply remains unsent and needs the catalogue clarification before use.
- **T28/T23:** rehearse the laptop GUI and poster on **Embedded Explosive Detection
  in Electronic Devices**, ASAP for SLG. The visit date and intended lab pairing
  remain unknown; **30 September poster submission** still applies.
- **T22 complete:** on **28 September**, the owner explicitly confirmed that all five
  students are registered for 6G. This is documented confirmation; receipts were not inspected.
  Hardik's separate registration remains T24.
- **T29/T30:** inspect the distributed base model early, adapt/evaluate after usable
  Batch 1, then collect a broader two-week batch after midterms and retrain. F03 names
  E4/B3 as extras, but C01 includes both in Round 1. Reconcile that conflict and retain M02's
  broader post-midterm Batch 2; no new batch dates are supplied.
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
T31; repository visibility is not proof of access or understanding. All-five registration is documented above from the owner's report;
no poster submission or collection is inferred from this technical work.

See [progress](progress.md) for dated engineering records, [verification](verification.md)
for evidence boundaries and [logo exploration](logo-exploration.md) for the private,
unselected identity studies. Student contributions and hours remain separately evidenced.
