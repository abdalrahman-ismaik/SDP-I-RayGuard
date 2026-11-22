# T39 requirement-to-screen map and T28 rehearsal runbook — 21 November 2026

Owner: Abd Alrahman Basim Ismaik (T39, proposed). Reviewer: Mohammad (per the demo plan).
Status: **draft for review**. Evidence below comes from reading the RayGuard-App source,
running its checks on 21 Nov and one local browser replay (below). No human walkthrough,
screen recording or real scanner run was performed.

## Local browser replay (21 Nov 2026, agent-driven)

Launched with `run-app.ps1 -Port 8770 -InferenceDevice cpu -SkipBuild` against a scratch
config (not the owner's `config.local.json`): `model_python` set to the existing
`.venv-yolov10` (torch 2.9.0+cpu, ultralytics), `runtime_profile` set to `manual` because the
managed cu126 profile is not installed here. Checkpoint `yolov10_generic_exp.pt`, hash as in config.

- Health: `status ok`, runtime `ready` on CPU, model YOLOv10-M Generic Explosive.
- Dataset replay of Test000001–Test000003 ran to **3 / 3 completed** with fresh inference.
- Test000001: 1 annotated, 0 matched, 1 missed, 0 extra (IoU ≥ 0.50, 25% threshold).
  Shown as "Missed target". This is the known miss the project already records.
- Test000002 and Test000003: "No detections reported" with the text
  "No regions met this run's 25% threshold. This is not a safe or benign verdict." (R6 evidence).
- Not tested here: Upload path, folder receiver, stopping the service mid-run, saved
  runs/export, and any on-screen check by a human. Not verified: GPU path, the other two models.

## Checks run (21 Nov 2026, RayGuard-App working tree)

| Command | Outcome |
|---|---|
| `uv run --locked ruff check .` (backend) | All checks passed |
| `uv run --locked python -m pytest -q` (backend) | 280 passed, 1 warning |
| `npm run build` (frontend) | Built in 1.53 s |

Not run: Playwright browser suite (`npm run test:e2e`). The working tree has 23 modified
files that are not committed by this check; no files were changed by it.

## Proposal requirement map

Source: the original proposal (`docs/SDP-2026- Naoufel Werghi-Project Explosive Detection.pdf`,
pp. 1–3). Status: **implemented** = present in the app and checked in code/tests;
**partial** = present with a stated gap; **missing** = not found in the app.

| # | Proposal requirement | App evidence (RayGuard-App) | Status | Gap / next action |
|---|---|---|---|---|
| R1 | Image acquisition: scan intake | Upload and folder receipt (`IntakeBar.tsx`, `InputPanel.tsx`), replay of finite IEDXray test images | partial | Physical scanner not connected; folder receipt only |
| R2 | Pre-processing: noise reduction / contrast | `ViewAdjustments.tsx`, `ScanCanvas.tsx` provide display-only contrast/brightness | partial | Display adjustments only; no pre-processing applied before detection; original pixels unchanged. State this on screen or in the runbook |
| R3 | Detection with a contemporary model | Three inspected YOLOv10-M task checkpoints, model/device selection (`RuntimeDeviceSelector.tsx`, `RuntimeStatus.tsx`) | implemented | Demo pairing with lab hardware not confirmed |
| R4 | Decision threshold / alert | Score threshold slider (`InputPanel.tsx`), "Threshold used" recorded in run details (`FindingsPanel.tsx`) | partial | Threshold is a confidence filter, not an operational alarm policy; screen text says scores are not calibrated |
| R5 | Operator view with bounding boxes | Boxes and scores on the scan (`ScanCanvas.tsx`), findings list (`FindingsPanel.tsx`) | implemented | — |
| R6 | Empty result is not a benign verdict | `FindingsPanel.tsx` shows "No detections reported"; `docs/usage.md` says empty detections do not mean safe | partial | Confirm the empty-state wording is visible in the demo, not only in docs |
| R7 | Evaluation on unseen test data | Replay of finite test images with reference comparison (`AnnotationPanel.tsx`: matched / missed / extra) | partial | Comparison is per image for the demo; no full benchmark metrics shown; precision is shown only as "Not recorded" when absent |
| R8 | GUI for system control and recording | Dashboard, sessions, notes, history and JSON export (`SessionHistory.tsx`, `ReviewPanel.tsx`) | implemented | Recording is review notes and exports, not live scanner capture |
| R9 | Explosive types (IED, laptop, phone) | Model task classes shown in `ModelClasses.tsx` | partial | Only generic explosive and the task checkpoints actually inspected; laptop/phone classes not established |
| R10 | Model/data provenance visible | "Selected scan & model record" in `App.tsx`; run record with model, threshold, device | implemented | Show checkpoint hash on the demo screen if time allows |

## Prioritized fix list (demo blockers first)

1. **Blocker — empty/error states on the demo path:** rehearse one run that returns no
   detections and one that fails (for example, service stopped). Confirm the screen says
   the result is not a benign verdict and the status is clear. Fix only wording or state
   bugs found this way.
2. **Blocker — threshold wording:** the slider must say it is a display/filter threshold
   and not a calibrated probability (already in `threshold-help`; confirm it is visible in
   the demo layout).
3. **Should — pre-processing claim:** do not present the contrast controls as pre-processing
   for detection. Adjust the label or the presentation script.
4. **Should — clean start:** run `run-app.ps1` from a fresh clone and record the exact steps
   and the engine revision. Record the app commit at the freeze.
5. **Later — scanner handoff, lab model pairing, full benchmark metrics:** out of scope for
   the 21–27 Nov window unless the supervisor changes the demo scope.

Do not edit another student's files in the RayGuard-App working tree. Coordinate with
Mohammad (T43) before changing any shared component.

## T28 showcase rehearsal runbook (human steps)

These steps need a person at the presentation laptop. An agent cannot complete them.

1. Start from a clean checkout of RayGuard-App at the frozen commit; record `git rev-parse HEAD`
   and the engine submodule revision.
2. Run `run-app.ps1`. Confirm the service starts and reports the checkpoint and device.
3. Upload or replay one test image with a known target; confirm boxes, scores and the
   reference comparison.
4. Run one image with no detections; confirm the empty-state text.
5. Stop the service mid-run; confirm the status shows unknown and recovers after restart.
6. Record review notes and export the JSON; open the saved run from history.
7. Time the whole path. Record the duration against the assigned slot.
8. Note which parts are live and which (if any) are a prerecorded fallback.

Record the outcome in `docs/progress.md` and `docs/status.md` with the actual commit and
the list of problems found. Do not record hours or ownership that were not reported.
