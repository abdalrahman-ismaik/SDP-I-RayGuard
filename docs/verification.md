# Verification record

Updated **27 September 2026**. This record separates software checks, real-data inspection,
static checkpoint inspection and actual model inference. The GUI draft adds the dated checks
below; earlier data audits and baseline records retain their original dates. Student review
remains pending; no student contribution or sign-off is inferred.

## Standalone application extraction — 27 September 2026

Application source and future GUI checks now live in
[RayGuard-App](https://github.com/abdalrahman-ismaik/RayGuard-App). Its
[migration record](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/migration.md)
records exact commands, the SDP engine pin and portability boundaries. Root Ruff
and **143 CPU tests** passed; extracted backend Ruff and **280 tests** passed;
frontend install/build and **149 Chromium checks** passed. These are software
checks with synthetic inputs where described.

Separately, the new launcher ran with existing authorized artifacts. Fresh real
generic CPU/GPU qualification passed, followed by a one-detection training-image
upload and a zero-detection test replay whose annotation comparison correctly
reported the known miss. No accuracy estimate, benign verdict, training or
physical scanner connection is established. Local source/history backups and
private run evidence remain ignored; publication excluded scans and checkpoints.
Older sections below describe their original checkout and dated evidence.

## Continuous Liquid Glass dashboard — 26 September 2026 follow-up

**Executed locally, T28:** the user's planner reference informed a persistent
five-page shell: Dashboard, Inspect, Workspace setup, Session and Source. Native
hash navigation, compact desktop sidebar and mobile Menu preserve mounted review
and scan state. Dashboard shows real loaded records and source availability;
dataset catalog size and finite-batch progress are separate. Glass controls and
local Instrument Serif headlines extend the existing dark/light modes.

| Check | Actual outcome |
|---|---|
| `uv run --locked ruff check .` | Passed |
| `uv run --locked python -m pytest` | **85 passed in 6.76 s**, synthetic core checks |
| `npm --prefix app/frontend run build` | Final TypeScript and production build passed |
| Chrome `npx.cmd playwright test`, from `app/frontend` | **67/69 passed in 3.1 min**; two test-selector failures |
| Dashboard suite plus affected setup case, exact command in [progress](progress.md#t28-continuous-liquid-glass-dashboard--26-september-2026) | **9/9 passed in 20.9 s** after locator corrections; final dataset/batch copy covered |
| `node tmp/dashboard-visual.mjs` | **19 GET-only saved-session views passed**; zero Axe findings, overflow, page errors or API mutations; acquisition state unchanged |
| Laptop inspection geometry | At 1366×768, image stage **334.61px high** with all four partitions open; collapse navigation preserves state |
| Local font/license verification | Two Instrument Serif files, **141,604 font bytes**, and OFL hashes matched the supplied manifest and shared record |
| Scoped public-file check | 17 text files / 83 relative links; no missing targets, private user paths or credential-pattern matches |
| Scoped design detector | Three font-style warnings: user-pinned Instrument Serif and retained optional Geist/Inter; no other findings |

All **69 browser cases have passing evidence across the full and targeted runs**;
no fresh all-pass full run is claimed. Eight new cases cover real links/history,
direct routes, skip-link focus without route changes, no automatic start, mixed
and missing-result states, held drafts/zoom, compact navigation, dark/light modes
and mobile keyboard/accessibility. Browser fixtures remain synthetic. Saved scans
were inspected separately, with screenshots independently reviewed. No new model
inference, scanner validation or human rehearsal occurred. Private evidence lives
under `output/playwright/dashboard/`; required model/scanner handoffs remain open.

## Main menu and workspace setup — 26 September 2026 follow-up

**Executed locally, T28:** the default entry now configures upload, dataset replay,
folder receipt or saved-run review before opening the dashboard. Layout/panels,
future-run threshold and following are applied without starting acquisition.
Returning preserves the existing view and draft. Availability comes from the
service; configuration is not evidence of working hardware or accurate inference.

| Check | Actual outcome |
|---|---|
| `uv run --locked ruff check .` | Passed |
| `uv run --locked python -m pytest` | **85 passed in 2.07 s**; synthetic core checks |
| `npm --prefix app/frontend run build` | Final TypeScript and production build passed |
| Chrome `npx.cmd playwright test`, from `app/frontend` | **59/61 passed**; intro focus race and stale busy-message assertion found |
| After fixes: `npx.cmd playwright test tests/e2e/main-menu.spec.ts tests/e2e/eye-animation.spec.ts` | **22/23 passed**; one ambiguous busy-status test locator remained |
| Corrected busy case and expanded Skip/Escape case rerun | **2/2 passed in 9.1 s**, including default intro → menu focus |
| `node tmp/main-menu-visual.mjs` | Eight GET-only saved-session views passed; zero Axe findings, overflow, page errors or API mutations; acquisition state unchanged |
| `node tmp/main-menu-tablet.mjs` | Corrected probe passed at 768, 900 and 1024px; zero Axe findings, overflow, page errors or API mutations; menu/workspace titles verified |
| Scoped design detector | No findings |
| Scoped sharing review | 17 text files / 127 relative links; no broken links, private user paths or credential-pattern findings |

All **61 browser cases have passed across the full run and targeted reruns**,
including eleven new menu cases. They cover all four entry paths, no automatic
start, changed readiness, preserved drafts/zoom, paused replay thresholds, intake
following, keyboard controls and dark/light phone accessibility. The tablet probe's
first attempt failed due to its Axe context setup, corrected before the passing run.
Screenshots were visually inspected; private evidence is under
`output/playwright/main-menu/`. Existing local saved scans were viewed separately
from synthetic browser fixtures. No new model inference or scanner validation was
performed. Human presentation review and model/scanner handoff remain open.

## Onyx Light — 26 September 2026 follow-up

The user liked Onyx/Barlow and requested its light counterpart. Onyx Light is
selectable in Appearance, preserves Barlow/layout and persists across reloads.
Root Ruff passed; root pytest **85 passed in 2.61 s**; production build passed.
Chrome `npx.cmd playwright test tests/e2e/appearance.spec.ts` passed **5 in 23.2 s**.
These existing synthetic cases cover all ten palettes, local assets, keyboard
selection, storage/fallback and retained inspection state.

GET-only `node tmp/onyx-light-visual.mjs` passed at 1366×768, 390×844 and 320×740,
also checking Session and Source. Zero Axe findings, document overflow, page
errors, external requests or API mutations; laptop scan stage stayed 332.61px high.
The live light workspace was visually inspected. Contrast review found minimum
text 5.37:1 and control boundaries 3.02:1 across relevant surfaces. The scoped style
detector still reports only optional Geist/Inter font warnings. No new inference
or hardware validation occurred. Private evidence: `output/playwright/onyx-light/`.

## Premium airport console — 26 September 2026 follow-up

**Executed locally, T28:** after rejecting the initial appearance choices, the
user chose a dark, precise and restrained console with a dominant scan viewer.
Analyst Studio's four partitions remain. Onyx/Barlow now defaults, with compact
source actions, quieter panel dividers, stronger filename/heading hierarchy and
an 86px desktop filmstrip. Earlier comparisons remain optional in Appearance.
The new preference key preserves the old saved choice without applying it.

| Check | Actual outcome |
|---|---|
| `uv run --locked ruff check .` | Passed |
| `uv run --locked python -m pytest` | **85 passed in 7.60 s**; synthetic core software checks |
| `npm --prefix app/frontend run build` | Passed TypeScript and production build |
| `npx.cmd playwright test`, from `app/frontend`, Chrome channel | Initial full run: **49 passed, 1 failed**. The new replay viewer-size check measured 328.61px against a 330px minimum |
| After shortening desktop filmstrip by 4px: `npx.cmd playwright test tests/e2e/demo.spec.ts tests/e2e/appearance.spec.ts tests/e2e/intake.spec.ts` | **17 passed in 1.0 min**. The failed case and all changed appearance/replay/intake cases passed; the other 33 full-run cases had already passed |
| `node tmp/premium-console-visual.mjs` | GET-only saved-real-scan probe passed at 1366×768, 1440×900, 1100×768, 1024×768, 768×1024, 390×844 and 320×740; zero Axe findings, horizontal overflow, page errors, external requests or API mutations |
| Font artifact review | Four unchanged upstream WOFF2 hashes/lengths and the OFL hash matched; **242,520 bytes**. All four faces loaded from the local app |
| Scoped public-file review | 24 text files and 134 relative links checked; no broken links, private user paths or credential-pattern findings |
| Scoped Impeccable detector | Two style warnings for the retained optional Geist/Inter comparisons; new default is Barlow. No other findings |

At 1366×768 in completed replay, the actual scan stage is **772×332.61px**,
up from approximately 220px high in the preceding treatment. All four partitions
and the footer fit. The source band measures 77px and the filmstrip 86px. Desktop
and phone screenshots were visually inspected; larger stage geometry is measured,
not a claim of faster or better human inspection. Private screenshots and JSON
are under `output/playwright/premium-console/`.

Browser regressions use synthetic HTTP/image fixtures and test display filters,
shared image/box transforms, selection hold, draft retention, replay, failure
recovery, local assets, keyboard controls and accessibility. Saved real scans
were viewed separately; this change ran **no new model inference**, dataset audit,
training or hardware test. Existing replay remained completed and disabled.
Human presentation review, intended laptop/pager model pairing and a real scanner
export handoff remain open. Nothing was committed or published for this refinement.

## Analyst Studio and appearance — 26 September 2026

**Executed locally, T28:** the user selected layout 15 and then requested different
fonts/colors. The working app now implements its adjustment dock, central viewer,
tabbed inspector and filmstrip, plus Inspect / Session / Source navigation.
Eight palettes and seven independent font choices give 56 combinations. Appearance
preferences are local to the browser; no model inputs or saved predictions change.

| Actual command / check | Outcome |
|---|---|
| uv run --locked ruff check . | Passed |
| uv run --locked python -m pytest | **85 passed in 2.32 s** |
| npm --prefix app/frontend run build | TypeScript and final production build passed |
| PLAYWRIGHT_CHANNEL=chrome; npm --prefix app/frontend run test:e2e -- intake.spec.ts demo.spec.ts appearance.spec.ts | **16 passed in 1.2 min** |
| Same environment, npm --prefix app/frontend run test:e2e -- workspace.spec.ts design-studio.spec.ts eye-animation.spec.ts | **32 passed, 1 failed**: the export-only test fixture accidentally disabled the entire polled service |
| Workspace-spec rerun after isolating the export failure fixture | **17 passed in 33.6 s** |
| From app/frontend, PLAYWRIGHT_CHANNEL=chrome; npx.cmd playwright test tests/e2e/appearance.spec.ts | Final **5 passed in 25.1 s**, including the added empty-dock regression |
| Font artifact verification | Five new font binaries and five license hashes/lengths matched the pinned provenance record; 688,100 new WOFF2 bytes |
| Palette token contrast analysis | 128 checks passed: minimum regular-text pair 4.81:1; control border/surface 3.04:1 |
| Scoped manual design detector against the changed UI sources | Two stylistic warnings for widely used Geist/Inter; deliberately retained as selectable comparison choices, with five alternatives |

**All 50 browser cases have passing evidence across these scoped runs**: 17 workspace,
6 intake, 6 dataset replay, 5 appearance, 4 design gallery and 12 eye treatment.
The workspace rerun was requested with the additional npm arguments
-g 'export failure'; npm forwarded the text as a positional pattern and actually
ran all 17 cases, as reported above. No broader test rerun was claimed.

The export fixture now fails only the export route; full service disconnection
and recovery retain their separate tests. Independent review also corrected:
missing origin shown as Upload, original-source/canonical-image hash ambiguity,
empty inspector tabs prematurely holding replay, keyboard access to a disabled
scrolling dock, and mobile filmstrip selection leaving the viewer offscreen.

Browser checks cover eight palettes with Axe, all seven font choices with local
asset loads, persisted and blocked storage, keyboard/Escape, font fallback,
review drafts and scan transforms across tabs/sections/layout controls, original
image/box alignment, review/export failures, source/replay and history behavior.
The existing eye treatment was preserved and its 12 tests passed. API responses
and image fixtures in these tests are **synthetic software evidence**, not model
predictions. The unchanged backend's earlier 89-test result was not rerun here.

Read-only visual inspection used six already-saved real IEDXray runs on port 8766;
it dispatched **no new inference**. Seven combinations/viewport cases covered
1440/1366 desktop and 390/320 mobile. Desktop footer fits within 768px; the scan
stage is about 220px high with all docks shown, with zoom and panel hiding available.
A synthetic empty-run visual check exposed the dock focus issue; after the fix,
three targeted follow-ups (empty Daylight and both mobile sizes) had zero Axe
violations. Actual saved-data checks had no API writes, external requests or page
errors. Reports/screenshots remain ignored under output/playwright/analyst-studio.

Final sharing review checked 27 source/documentation files for credential/private
path patterns and 132 relative documentation links: no matches or missing targets.
All ten bundled font/license hashes were independently rechecked. Git diff whitespace
check passed; screenshots, build output and local configuration remain ignored.
No files were staged or committed for this interface refinement.

Fonts, licenses and source revisions are documented in the
[font catalog](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/frontend/public/fonts/choices/README.md). New appearance
assets are code dependencies, not dataset images. Shared documentation records
layout 15 as selected and font/palette choice as open. Human laptop rehearsal,
intended lab model pairing and physical scanner handoff remain outstanding.

## Advanced workstation proposals — 26 September 2026

**Executed locally, T28:** the user's request for richer dashboards added six
advanced proposals (11–16) while preserving the ten compact designs. The studio
now partitions section navigation, saved-run selection, image tools, evidence and
context. Search, filters, sorting, keyboard evidence tabs, applicable panel toggles
and Analyst Studio's display adjustments work locally. Final user selection is open.

| Actual command / check | Outcome |
|---|---|
| `uv run --locked ruff check .` | Passed |
| `uv run --locked python -m pytest` | **85 passed in 2.56 s** |
| `npm.cmd --prefix app/frontend run build` | TypeScript and production build passed |
| `node --check` for `studio.js` and `advanced.js` | Passed |
| In `app/frontend`, `$env:PLAYWRIGHT_CHANNEL='chrome'; npm.cmd run test:e2e` | **28 existing cases passed**; four new gallery cases exposed a Vite development-route fallback defect |
| Same environment, `npm.cmd run test:e2e -- design-studio.spec.ts` after the route fix | **4 passed in 9.8 s**; all 32 browser cases have passing evidence across these runs |
| Inline Node ES-module assertions, PowerShell here-string piped to `node --input-type=module -` | **24 synthetic renderer cases passed**: six layouts × succeeded, failed with stale result, running with stale result, empty |
| Impeccable detector once against `app/frontend/public/design-studio` | Returned `[]`; no findings |

The route fix maps `/design-studio/` to its public directory index before Vite's
React fallback, preserving query parameters. It follows Vite's
[documented development middleware hook](https://vite.dev/guide/api-plugin.html#configureserver).
The Node HTTP request typings were absent; adding pinned `@types/node` **22.20.4**
resolved the build error. This is a development-only dependency; the detector and
API environments did not change. Installation reported zero npm audit findings.

Independent source review verified GET-only saved-run access, local image URLs,
escaped text, explicit loaded-record counts, distinct scores/thresholds and no
stale predictions displayed for failed/running records. Saved-image identity stays
fixed when search/filtering excludes it. The successful browser regressions are
synthetic software checks. The visual walkthrough renders existing saved results;
this implementation/verification work dispatched **no new inference**, training
or scanner test. Concurrent user work and saved records are preserved.

`node tmp/advanced_design_studio_check.mjs` recorded **19 of 20 checks passing**:
five standard widths (1440/1366/1024/390/320), a 683×384 viewport equivalent to a
1366×768 display at 200% browser zoom, automated Axe, and heterogeneous synthetic
records. The one failure was option 11 navigating while the production assets were
being rebuilt. `node tmp/advanced_design_studio_check.mjs --final-focus` passed
**all six targeted checks** on a stable build,
including option 11 at all six widths and fresh Axe checks for focused 11/15.
The initial failure record was retained. These are viewport-equivalent checks,
not a claim to have changed Chrome's native zoom setting.

Focused 11/15 now fit at 1366×768: footer ends at y=746, lower docks at y=704,
with image areas 265/226 px high. Long lists, notes and findings scroll within
their partitions; hide/show/reset preserves the selected image. All six layouts'
accessibility/edge checks passed, with no reported Axe violations, external
requests, API mutations, unhandled script errors or failed assets in final checks.
Synthetic cases cover the 50-of-53 cap, unsafe image URL exclusion, six findings,
failed/running/empty states, escaped text, long names and display-only adjustments.
This is not accessibility certification or human showcase acceptance.

Private reports: `runs/advanced-design-studio-verification-2026-09-26.json` and
`runs/advanced-design-studio-final-focus-2026-09-26.json`; screenshots remain under
`output/playwright/advanced-design-studio/`. A scoped sharing review of 21 changed
design/source/document files checked 159 relative links without broken targets or
flagged private patterns. Unrelated eye-animation assets were outside that scope.
`git diff --check` passed; nothing was staged, committed or published.

## Ten interactive design choices — 25 September 2026

**Executed and verified locally, T28:** the separate `/design-studio/` gallery
offers ten layouts/themes with full-size previews, Focus/Escape, saved-image
selection, zoom, overlays, details, local favorites and explicit copy-choice.
The [comparison guide](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/design-options.md) records each option and its
tradeoff. These are proposals for user selection; a final redesign is not approved.

| Actual command / check | Outcome |
|---|---|
| `npm.cmd --prefix app/frontend run build` | Passed after the final gallery fixes |
| `node --check app/frontend/public/design-studio/studio.js` | Passed |
| `node tmp/design_studio_check.mjs` | All ten previews checked at 1440, 1366, 1024, 390 and 320 px; no document overflow; Focus view includes the footer at laptop size |
| Same browser check | Navigation, zoom/Fit, overlays, Details, saved-image selection, favorites, keyboard focus, Focus/Escape and clipboard passed; all ten offline states checked |
| Automated Axe WCAG 2 A/AA and 2.1 AA checks | Zero reported violations across all ten designs; not accessibility certification or human usability acceptance |
| `node tmp/design_studio_limits_check.mjs` | Synthetic rendering probe: 53 fixture runs reported as 50 displayed of 53, all six findings retained, eighth run selectable, overlay toggle passed |
| Impeccable detector, once against `app/frontend/src` and `app/frontend/public/design-studio` | Returned `[]`; no findings |

Initial visual/accessibility review prompted contrast, essential text size,
keyboard-focus and disclosure fixes. Full previews now show the complete scrollable
findings list and every loaded run; the session limit is explicitly labeled.
Presentation Studio uses larger operational text. The limits probe used synthetic
fixtures only; ordinary visual checks used the three saved genuine replay results
below without dispatching any further inference.

There were no unhandled page errors, external HTTP requests, API mutations or
unexpected HTTP errors. Ten injected 503 responses deliberately exercised offline
previews. The gallery uses local assets and read-only saved results; it does not
control a scanner, run models, save reviews or publish a choice. Private evidence:
`runs/design-studio-verification-2026-09-25.json`,
`runs/design-studio-synthetic-limits-2026-09-25.json` and
`output/playwright/design-studio/`. These artifacts and scans remain ignored.
Independent targeted review confirmed the final findings/history and text-size
fixes. A bounded sharing review checked **69 changed/new candidate files and 207
relative Markdown links**, with no broken links or flagged private artifacts;
`git diff --check` passed. Nothing was staged, committed or published in this step.

## Direct test-dataset replay — 25 September 2026

**Executed and verified locally, T28:** Dataset demo links the authorized local
IEDXray test directory to finite fresh-inference batches. Independent read-only
inspection found 5,136 direct JPEGs, `Test000001.jpg` through `Test005136.jpg`,
matching the image filenames in all four test annotation tables. This does not
resolve existing label/split findings or prove publisher byte identity.

| Actual command / check | Outcome |
|---|---|
| `uv run --locked ruff check .` | Passed |
| `uv run --locked python -m pytest` | **85 passed in 2.33 s** |
| `uv run --project app/backend --locked python -m pytest app/backend/tests` | **89 passed in 3.79 s**, including 31 new synthetic replay checks |
| `npm.cmd --prefix app/frontend run build` | Passed, including the final visible-image-identity fix |
| In `app/frontend`, `$env:PLAYWRIGHT_CHANNEL='chrome'; npm.cmd run test:e2e` | **28 passed in 44.8 s**; synthetic browser fixtures |
| Same environment, `npm.cmd run test:e2e -- --grep 'pause and resume\|completed workspace\|laptop controls'` | **4 passed in 11.4 s** after the image-name fix |
| `node tmp/gui_dataset_presentation.mjs` | Passed against saved genuine demo results; no additional inference or API mutations |

Replay checks cover finite order/end behavior, pause/resume, failure stopping with
the unfinished position retained, source changes/links, byte/catalog/session limits,
mode exclusion, raw-source hashes, export provenance, held review and reconnection.
Actual browser inspection found that the currently processing filename could differ
from the held image; the canvas now displays its own filename explicitly. Both tested
themes pass automated Axe checks; this is not formal accessibility certification.

### Genuine bounded demonstration

The updated service was started with `run-app.ps1 -SkipBuild -Port 8766`, after an
automatic approval check blocked restarting the existing 8765 service. The old
service was preserved. The ignored local config links `data/IEDXray/Test` and uses
the unchanged generic checkpoint/backend pairing from the earlier records: CPU
FP32, confidence **0.25**, three-second delay after completed inference.

The first three filenames were recorded and hashed **before** running the model.
The connected browser started the default three-image batch, paused during the
first run, verified one completed run with no active job, and resumed the remaining
two. Holding the first image retained it while two newer results arrived; Follow
latest then selected the third image. The batch stopped automatically.

| Published test source | Run ID | Actual result | Total run duration |
|---|---|---|---|
| `Test000001.jpg` | `ee22d43ee2b5438b9e2837bb850ebdbb` | Zero detections; previously documented missed threat retained | **12.84 s** |
| `Test000002.jpg` | `626153475b9f4c93a59892bb9cc0044d` | Zero detections | **13.36 s** |
| `Test000003.jpg` | `a5d921a7951344809f99bf9b4cb1fdbf` | Zero detections | **11.61 s** |

Each has one generic source annotation, inspected separately; annotations were not
model inputs. Empty outputs do not establish benignness. These three cases are a
diagnostic integration demonstration, not AP/recall evaluation or representative
performance. No threshold tuning or training used the published test images.
Durations include process/model startup and application overhead, not model FPS.

Before/after hashes confirm all three source files unchanged. Each saved run/export
has `origin=dataset_demo`, dataset/split and zero-based index, raw source SHA-256 and
normalized image hash. Browser JSON export retained that identity. Saved-result
presentation passed at eight widths from 320–1440 px, with no document overflow,
external HTTP, unhandled page errors or API mutations. The service remains idle,
batch completed; folder intake is paused with no queued work.

Private evidence is in `runs/gui-dataset-demo-verification-2026-09-25/` and
`output/playwright/dataset-demo-*.png`. Source files, local config and run evidence
remain ignored. Human showcase acceptance, intended lab laptop/pager model pairing
and real scanner acquisition remain unverified.

## Inspection hierarchy — 25 September 2026

**Executed locally, T28:** the user's difficulty following the page led to a single
Choose/Run/Review sequence, one action strip and a dominant scan workspace. The
settings rail and empty findings panel are removed. Source/detector settings,
history and run metadata/export start closed; findings and review remain direct.
Active intake, pending work, errors and unseen arrivals while holding an older
scan stay visible. Failed inference retains the Run step and prominent retry.

| Actual command / check | Outcome |
|---|---|
| `npm.cmd --prefix app/frontend run build` | TypeScript and production build passed after final fixes |
| In `app/frontend`: `$env:PLAYWRIGHT_CHANNEL='chrome'; npm.cmd run test:e2e` | **22 passed in 41.5 s**; synthetic cases, including both theme Axe checks |
| In `app/frontend`: `npm.cmd run test:e2e -- --grep 'failed inference cannot carry stale predictions\|history selection stays fixed'` with the same Chrome environment | **2 passed in 8.6 s** after final state fixes |
| `uv run --locked ruff check .` | Passed |
| `uv run --locked python -m pytest` | **85 passed in 4.68 s** |
| Impeccable design detector, once against `app/frontend/src` | Returned `[]`; no findings |
| `node tmp/gui_hierarchy_check.mjs` | Passed against saved actual results; read-only, **no new inference** |

The browser suite adapts existing coverage to closed disclosures, checks keyboard
access and adds actual workflow-step progression. The final two regressions check
failed-run retry emphasis and visible Follow latest controls when intake is paused
with newer arrivals and an uploaded historical scan held. Root checks are synthetic;
API/model code is unchanged and retains the preceding **58-test API** evidence.
Automated accessibility checks are not certification or a human usability study.

Production screenshots cover empty, saved positive and known missed-threat results
in light/dark desktop, tablet and phone layouts. At widths 320, 390, 640, 768, 960,
1024, 1366 and 1440 px there was no document overflow. Run and both review actions
remain reachable in the 1366×768 layout. No external HTTP requests, API mutations
or unhandled browser errors occurred. The dark page background was corrected after
visual review. Existing intake remains paused; no scanner or model job was launched.

Private evidence: `runs/gui-hierarchy-verification-2026-09-25/presentation.json` and
`output/playwright/hierarchy-*.png`. A Windows text-encoding error interrupted an
intermediate stylesheet rewrite; the prior built stylesheet restored its existing
rules, edits were written as UTF-8 and subsequent build/browser checks passed.
Independent review prompted the two state fixes above; final read-only review found
no remaining material issue. Sharing review checked **60 changed/new candidate files
and 197 relative links**, with no broken links or flagged private artifacts. The
path/key-pattern and large-file checks are bounded checks, not a credential audit.
`git diff --check` passed. Human operator rehearsal,
the intended lab laptop/pager pairing and a real scanner handoff remain outstanding.

## Visual refinement — 25 September 2026

**Executed locally, T28:** locally served IBM Plex Sans, a rem-based type hierarchy,
light/graphite theme refinements, real Inspect/Review/History anchors, review before
collapsed detection details, and mobile input-settings disclosure. The user's design
request drives these changes; [primary-source research](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/visual-research.md)
supports the recommendation, not an objective best-font or usability-performance claim.

| Actual command / check | Outcome |
|---|---|
| `npm --prefix app/frontend run build` | TypeScript and production build passed |
| `$env:PLAYWRIGHT_CHANNEL='chrome'; npm --prefix app/frontend run test:e2e` | **21 passed in 38.9 s**; synthetic software cases |
| `uv run --locked ruff check .` | Passed |
| `uv run --locked python -m pytest` | **85 passed in 2.60 s** |
| Design detector | No findings; rendered review remains a separate check |
| `node tmp/gui_visual_check.mjs` | Passed against the production UI and previously saved real runs; read-only, **no new inference** |

The two added browser cases check keyboard anchor focus, mobile settings collapse/
expand and desktop restoration, local font loading, and usable fallback when font
requests fail. Existing result identity, overlay alignment, review/export, intake,
failure/retry and theme tests pass. Both tested completed-workspace themes have zero
Axe WCAG A/AA findings; this is not accessibility certification. API/model code and
dependencies were unchanged, so the preceding **58-test API** result remains applicable.

Production screenshots cover empty, positive and known missed-threat saved results.
Light/dark, laptop/mobile/tablet layouts were inspected. All three font weights loaded;
their embedded family metadata and hashes were inspected. Widths 320, 390, 640, 768,
960, 1024, 1366 and 1440 px had no document overflow. At 1366×768, Run remains in the
viewport and both review actions fit within the findings panel. There were no external
HTTP requests, API mutations or unhandled page errors. Existing intake remains paused.

Private evidence: `runs/gui-design-verification-2026-09-25/visual-check.json` and
`output/playwright/design-*.png`. The source fonts/license and [asset provenance](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/frontend/public/fonts/README.md)
are intended repository assets; source scans and screenshots remain ignored. No
training, downloads of models, changes to scientific results or publication occurred.
Human operator rehearsal, scanner handoff and intended laptop/pager pairing remain open.

Independent screenshot review found one tablet history-scroll cue missing; the cue now
appears through 960px. After that CSS change, production build passed again and the
expanded mobile/tablet keyboard test passed (**1 test in 6.9 s**) using
`node node_modules/@playwright/test/cli.js test --grep 'mobile settings and section navigation'`
from `app/frontend`. An earlier npm argument-forwarding attempt selected no tests;
the direct CLI invocation above is the successful check. Final sharing review found
**254 working relative links across 104 public candidate files**, with no flagged
scan/checkpoint/private-path/key material or file above 2 MB. `git diff --check` passed.

## Folder intake and operator workflow — 25 September 2026

**Executed and verified locally, T28:** read-only completed-image reception, bounded
queue, automatic generic YOLO execution, pause/resume, follow/hold selection, display-only
adjustments, and saved review notes/status. **Physical scanner: unverified.** The user
confirmed that the scanner/interface is not yet known. Vendor research is recorded in
[the app research notes](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/scanner-research.md); it is not hardware compatibility evidence.

### Latest software checks

| Actual command / check | Outcome |
|---|---|
| `uv run --locked ruff check .` | Passed |
| `uv run --locked python -m pytest` | **85 passed in 2.81 s** |
| `uv run --project app/backend --locked python -m pytest app/backend/tests` | **58 passed in 3.35 s**, including 23 intake/review tests |
| `npm --prefix app/frontend run build` | TypeScript and production build passed |
| `$env:PLAYWRIGHT_CHANNEL='chrome'; npm --prefix app/frontend run test:e2e` | **19 passed in 32.6 s**, after the final layout fix; installed Chrome |
| Design detector and actual browser screenshots | Detector returned no findings; light/dark, positive/missed-threat, queue and responsive views inspected |

These are synthetic software checks except the separately described real replay below.
New tests cover existing-file baselining, partial/stable files, BMP decoding, source
preservation and escapes, source/storage/model errors, retry, backpressure, pause/resume,
queued thresholds, review persistence/failure, selection holds and late saves, and
display-only transforms. Existing upload/export/reconnection/keyboard tests still pass.
Both tested completed-workspace themes have zero Axe WCAG A/AA findings; this is not
accessibility certification. One upstream Starlette TestClient deprecation warning remains.
No dependency lock or model environment changed for this extension.

Review/testing found and fixed: full-queue dispatch stopping, arrivals replacing a scan
while a note was being typed, an adjustment panel resizing the canvas, and a short-laptop
findings list collapsing beneath the review panel. The real replay initially stopped at
that last UI interaction; after the CSS fix, verification resumed against the same saved
positive run and queued second scan, without re-running the positive model job.

### Real folder replay, not a physical scanner test

The existing generic checkpoint and original source pairing from the section below were
used unchanged on CPU FP32 at confidence **0.25**, through the production server on port
8765. Two authorized published images were copied into an ignored local inbox. A preexisting
file was skipped, then the new images were accepted and inferred automatically. Pause
allowed the active job to finish while retaining the second scan; resume dispatched it.

| Published diagnostic source | Run ID | Actual result | Total run duration |
|---|---|---|---|
| `Train000003.jpg` | `e52fb431fadd48209c4b5007416fc869` | One generic `Explosive` region, score **0.9702618** | **16.65 s** |
| `Test000001.jpg` | `431cc71ddbd64ad6a210f7973dd81c1a` | Zero detections; known annotated modified-laptop miss, no benign verdict | **9.43 s** |

Browser checks selected the real box/finding, saved an explicitly automated verification
note with follow-up status, and downloaded the actual JSON export without machine paths.
Original inbox bytes remained unchanged. The final receiver state was paused, two received,
zero queued and no intake issues. The page made no external HTTP requests and raised no
unhandled page errors; no document overflow at 1440, 1366, 768, 390 or 320 px.

Private commands: `node tmp/gui_folder_replay.mjs`, then
`node tmp/gui_folder_resume.mjs` after the layout fix. Evidence is retained under
`runs/gui-operator-verification-2026-09-25/` and `output/playwright/`; run artifacts stay
under `runs/gui/`. The first script's initial locator ambiguity was corrected before
new images were accepted. These private scripts use the local model setup; shared
synthetic tests remain runnable without artifacts.

The positive source belongs to training, and the other example is a known miss. Durations
include process/model startup; they are not scanner throughput, FPS, or a latency benchmark.
No accuracy estimate, new-data collection, physical scanner test or human review is claimed.
Intake starts paused and its queue/index are in memory; automatic restart recovery is
unimplemented. Lab export details, intended laptop/pager pairing and human rehearsal remain
open. Changes stay local on `feat/gui-first-draft`; no publication or hosted GUI CI result.

Final sharing checks: `git diff --check` passed; **239 relative Markdown links**
resolved across **98 public candidate files**. No source scan/checkpoint/PDF/archive,
file over 2 MB, private user-path or tested private-key/token pattern was found in
that candidate set. Eight ignore probes passed for local configuration, source/model
artifacts, dependencies/builds, environment, screenshots and private verification scripts.

## GUI first draft — 25 September 2026

**Executed and verified locally, T28:** [React/TypeScript workspace and FastAPI service](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/usage.md)
integrated with the existing separately pinned generic YOLOv10-M backend. Automated
implementation and independent code/visual review were performed; human team ownership,
explain-back and presentation-laptop rehearsal remain pending. Changes are on local
`feat/gui-first-draft`; the new GUI CI definition has not been published or run on GitHub.

### Software checks

| Actual command / check | Outcome |
|---|---|
| `uv run --locked ruff check .` | Passed, including the new Python API and tests |
| `uv run --locked python -m pytest` | **85 passed in 2.28 s**; existing CPU suite |
| `uv run --project app/backend --locked python -m pytest app/backend/tests` | **35 passed in 1.73 s**; synthetic API/adapter tests |
| `npm --prefix app/frontend ci` then `npm --prefix app/frontend run build` | Clean dependency installation and TypeScript/production build passed; Node 22.14.0, npm 11.6.2 |
| `$env:PLAYWRIGHT_CHANNEL='chrome'; npm --prefix app/frontend run test:e2e` | **12 passed in 20.4 s** using installed Chrome; synthetic image/API fixtures |
| `npm --prefix app/frontend audit` | **0 known vulnerabilities** reported for the locked frontend dependency tree at execution time |
| Design detector and independent visual review | Detector reported no findings; final light/dark, laptop/mobile and missed-threat screenshots reviewed |

API tests cover invalid/oversized images, EXIF normalization, upload/run limits, concurrent
run rejection, origin/host checks, subprocess failures/timeouts, job/result identity, invalid
numbers, storage failure and sanitized exports. Browser tests cover upload/selection, zoom
alignment, keyboard pan/reset, history/settings retention, successful empty output, failed
inference, disconnection/restart recovery, export contents and retry. Both completed themes
have zero detected Axe WCAG A/AA violations in the tested states; this is automated coverage,
not accessibility certification. All browser cases check for unhandled page errors.

Iteration fixed connection state recovery, mobile history overflow, muted-text contrast,
export error feedback and short-laptop action placement. The initial native-download mock
could not intercept a browser download reliably; actual production download worked, and
the improved fetch/error/export flow now has a passing content/retry regression check.

One upstream Starlette TestClient deprecation warning recommends replacing its httpx-based
test client dependency. No test failed; no runtime warning was inferred from that test message.
No changes were required to the root dependency lock or the model environment.

Final sharing review: `git diff --check` passed; **220 relative Markdown links across
90 public candidate files** resolved. No scan/checkpoint/PDF/archive/private-key file or
file above 2 MB appeared in that candidate list. Ignore probes covered the local config,
environments, dependencies, built assets, screenshots, run exports and private test scripts.
The changes remain uncommitted locally; no new artifact or GUI source was pushed.

### Genuine model and production-browser checks

Actual CPU FP32 inference used the author generic checkpoint SHA-256
`b484d9a6fb37236f6adcc8c019e6a836f11901dc53a0f71d6cce7262413287ff`, original
THU-MIG revision `453c6e38a51e9d1d5a2aa5fb7f1014a711913397`, confidence **0.25**.
The app normalizes each upload into the exact PNG used for both viewing and inference.
This preserves the inspected pixels here; its hash identifies canonical input bytes.

| Path through the app | Diagnostic image | Actual output | Total run duration |
|---|---|---|---|
| Live API | `Test000001.jpg` | Zero boxes: known annotated modified-laptop miss | 16.33 s |
| Live API | `Train000003.jpg` | One `Explosive` region, score 0.9702618 | 9.78 s |
| Live API | `Test000034.jpg` | Zero boxes; no benign verdict | 9.48 s |
| Browser upload/run | `Train000003.jpg` | Same positive region/score; linked overlay and JSON checked | 11.29 s |
| Browser upload/run | `Test000001.jpg` | Zero boxes; explicit no-safe/benign-verdict message checked | 9.60 s |

The production build was served by the loopback API, not Vite. Browser run IDs were
`85b1fe45f485454ea7d10f344d7e846b` (positive) and
`91ed7d5068914216a504034a8eb8ceaf` (miss). The final export button downloaded the actual
positive run with the matching score, ID and model provenance and no machine-specific paths.
The observed production page made no external HTTP requests and raised no unhandled page
errors. Document widths matched viewports at **1440, 1366, 768, 390 and 320 px**; the loaded
scan's Run button fits within a **1366×768** viewport. Final screenshots were reviewed.

Private execution evidence is under `runs/gui-verification-2026-09-25/`; model manifests/logs
remain under `runs/gui/`. Screenshots stay ignored under `output/playwright/`. The three-API
smoke used the private command `uv run --locked python tmp/gui_smoke.py`; final live browser
inspection used Playwright CLI and `node tmp/gui_final_browser.mjs`. These machine-specific
scripts/records are not required for a fresh clone; the committed synthetic suite is portable.

These are diagnostic integration checks, **not accuracy, generalization, calibration or
latency benchmarks**. The positive image belongs to training. Total duration includes model/
process startup and is not model-only latency. No training, large artifact download, split
change or new dataset audit was performed. The lab's intended laptop/pager model is still
unconfirmed; this GUI does not implement device association, benign decisions or P2 fusion.

## CPU software checks

Earlier local check: **25 September 2026**, during collaboration setup. `uv run --locked ruff
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

## RayGuard eye introduction — 26 September 2026

**Executed and verified, software/media evidence:** the local four-second eye introduction
plays on fresh loads, with bounded skip/failure behavior. Its final composition follows
the user's amendment: centered video background with RayGuard text below. The small
resolved-eye loop follows real UI activity signals; it does not represent detector evidence.

| Check | Actual outcome |
|---|---|
| `uv run --locked ruff check .` | Passed. |
| `uv run --locked python -m pytest` | 85 passed in 4.45 s. |
| `npm --prefix app/frontend run build` | Passed, including the concurrent Analyst Studio changes. |
| `npx playwright test tests/e2e/eye-animation.spec.ts` from `app/frontend` | 12 passed in 37.5 s. Real MP4 playback; API/scan fixtures are synthetic. |
| `node tmp/eye-visual-check.mjs` | Desktop 1440×900, mobile 320×740 and 683×384 zoom-equivalent opening views: no horizontal overflow, zero Axe WCAG2A/AA/2.1AA findings; screenshots inspected. The script is ignored local evidence. |
| Scoped Impeccable detector | No findings for the eye components/styles, including the final centered-background amendment. |
| Media decode/metadata | Both MP4 files fully decode; silent 24 fps H.264/yuv420p with fast-start metadata. [Commands/hashes](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/frontend/public/media/rayguard/README.md). |

The browser checks cover reload, Skip/Escape, native modal focus, no initial video request
under reduced motion, autoplay rejection, absent/stalled media, offline/unconfigured service,
replay preserving notes/focus, loading pause/resume, disconnection uncertainty and held review
while another scan runs. Independent review led to explicit disconnected-run text, focus
fallback when replay becomes disabled, and pausing the existing decorative spinners too.

The visual helper freezes a late media frame and extends its watchdog only in the screenshot
browser; those images do not prove timing. The separate browser tests check the actual
four-second playback and production timeout. Zoom-equivalent viewport checks are not physical
device certification. Prior 19 source-package checks remain separately documented evidence.
No detector job, scanner handoff or human rehearsal was performed during this change.

The subsequent user-requested zoom-out starts at the previous size and eases to 76%
over actual playback time. The build and Ruff passed again, root pytest passed 85 in
2.59 s, and `npm --prefix app/frontend run test:e2e -- tests/e2e/eye-animation.spec.ts`
passed 12 in 23.8 s. The three-viewport visual/Axe check was repeated with zero findings
and no horizontal overflow; desktop/mobile framing was inspected. A read-only browser
probe confirmed fixed centering at media times 0, 2 and 3.9 s, with desktop scales
1, 0.82 and 0.76015 and the same proportional portrait change. Independent review covered
playback synchronization, finite/clamped progress and animation-frame cleanup.

The later quality refinement supersedes that scale endpoint with 56%. Native 1080p,
CRF17, mild denoising/sharpening and a matching full-HD poster replace the earlier
720p intro. [Media commands and hashes](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/frontend/public/media/rayguard/README.md)
record the exact output; source footage and the compact loop are unchanged. The build
and Ruff passed, root pytest passed 85 in 2.30 s, and the same targeted browser command
passed 12 in 22.4 s. The three-viewport visual/Axe helper confirmed the served media's
1920×1080 dimensions, zero findings and no overflow, with desktop at 2× pixel density.
Matched source/current/native/cleaned frame crops and final desktop/mobile screenshots
were inspected. These support the visual improvement, not a universal noise-free claim.

## GUI test-reference comparison — 26 September 2026

Implemented [per-image annotation agreement](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/annotation-comparison.md) for
verified IEDXray generic test replay. The source has 5,136 images / 3,204 boxes;
exact COCO ID/category, source/canonical hashes, dimensions and model/run pairing
are checked before comparing. The fixed IoU ≥ 0.50 rule is a project diagnostic,
not full COCO AP or a safety decision.

Current software checks: root Ruff passed; root pytest **85 passed**; backend
pytest **143 passed** (54 new synthetic cases, one existing dependency warning);
production build passed; full Chrome Playwright suite **85 passed** (13 new
comparison cases). Same-run retry and a stale font assertion were corrected before
the successful full run. See [commands and review](progress.md#t28-iedxray-test-reference-and-model-comparison--26-september-2026).

Separately, GET-only checks compared **nine genuine saved replay predictions**
(Test000001–Test000009) with their actual generic references. All nine correctly
report one missed target at saved confidence 0.25: zero predictions, one reference.
The ordinary upload is ineligible for automatic reference pairing. JSON exports
include comparison evidence without changing predictions or disclosing paths.
Real-browser checks verified each overlay's coordinates, independent visibility,
zoom and six dark/light desktop/mobile views with no Axe violations, overflow,
page errors or API writes. The updated 8767 preview preserves copies of the ten
saved records; the previous services and originals are unchanged. No new model
inference, full-dataset metric or scanner validation occurred.

## Viewer wheel zoom and magnifier — 26 September 2026

The viewer now supports pointer-centred wheel zoom, bounded drag and an optional
3× hover lens with the same visible reference/model layers. Build and Ruff passed;
root pytest passed **137**. Eight new synthetic browser cases passed, covering
actual SVG coordinate transforms, wheel limits, drag/click selection, lens alignment,
layer visibility, Escape/reset, mobile bounds, keyboard/Axe and native touch gestures.
The full browser regression passed **103/104**; its remaining pre-existing font
loading race was corrected and verified in a **2/2** focused rerun. Exact commands,
test-only fixes and concurrent test-isolation issues are in
[progress](progress.md#t28-wheel-zoom-pan-and-hover-magnifier--26-september-2026).

Separately, GET-only browser checks on an actual saved IEDXray scan confirmed wheel
anchoring, panning and exact 3× rendering across six dark/light desktop/mobile views,
with no Axe findings, overflow, page errors or API writes. Eleven saved records and
service state remained unchanged. This is presentation evidence; no new inference,
dataset audit or physical scanner test was run for these controls.

## Portable CPU/CUDA runtime — 26 September 2026

[Detailed execution record](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/runtime-verification.md): reviewed isolated
Windows x64 CPU/CUDA profiles, hardware discovery, managed preparation and explicit
per-host model qualification are implemented. Protected original CPU results and
all three isolated CPU/CUDA diagnostics passed fixed FP32 parity gates; the positive
was repeated and overlays inspected. The known missed threat remains a miss.
Actual upload/replay/held review/reference/export, folder malformed-image recovery,
timeout queue preservation/retry and CPU rollback passed on task-owned 8770.
Existing CPU environment and 8765–8767 services remain intact.

Software checks passed separately: Ruff, 138 root tests, 203 backend tests, frontend
build and 104 browser tests; a later narrow reference-transition correction passed
13 focused browser checks and build. Tests use synthetic hardware/failures where
stated and require no CUDA packages in CPU CI. No accuracy or universal portability
claim follows. The 45/45 bounded A/B/C benchmark trials passed parity. CUDA's
forward-stage medians were 50.4–54.2 ms, but fresh-process medians stayed near
8 seconds without a consistent end-to-end speedup. The execution record retains
all per-image median/range summaries, timing boundaries, memory/power observations
and explicit second-device acceptance steps.

## Workspace CPU/GPU choice — 26 September 2026

The [runtime follow-up](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/runtime-verification.md#workspace-cpugpu-selection-follow-up--26-september-2026)
records clear device controls, saved preferences, GPU-first managed defaults and
explicit launcher-supervised restart. Ruff, 138 root tests, 238 backend tests,
the production build and 119 browser tests passed. The real 8771 service completed
initial CPU/GPU qualification, a GPU positive, a browser switch/CPU positive and
a browser switch/GPU positive. Execution evidence belongs to each run. The real
test exposed and corrected differing Python Windows-release labels in preference
identity; a regression preserves rejection of actual host/visibility/device changes.
This is local execution evidence, not cross-laptop or human showcase acceptance.

## Model selection — 26 September 2026

[Model selection evidence](https://github.com/abdalrahman-ismaik/RayGuard-App/blob/main/docs/model-selection.md) records the inspected
generic/device/specific YOLOv10-M pairings and a protected pre-change generic CPU
capture. The updated generic CPU JSONs match exactly. Eighteen serial processes
produced nine CPU/GPU pairs that passed fixed FP32 count/class/namespace/box/score
gates. Device/specific nonempty overlays were inspected; empty matches are only
execution compatibility. The actual app verified device CPU/GPU and specific GPU
execution, model-aware exports and specific-test replay reference isolation.
Actual browser return to generic GPU also passed qualification, positive inference
and the known-miss replay: one reference box, zero predictions, missed outcome.
Existing service PIDs and the original CPU config were preserved.

`uv run --locked ruff check .`, `uv run --locked python -m pytest` (**143 passed**),
`uv run --project app/backend --locked python -m pytest app/backend/tests -q`
(**267 passed**, one existing Starlette/httpx warning),
`npm.cmd --prefix app/frontend run build`, and
`npm.cmd --prefix app/frontend run test:e2e -- --config ../../tmp/playwright-runtime.config.ts --reporter=line`
(**133 passed** on isolated 18766) passed. Fourteen focused model-browser tests
also passed, including both 320px themes with no Axe violations or overflow.
These software checks do not require CUDA in CPU CI and are distinct from the
local RTX 2060 model executions. No new performance claim or second-host acceptance
follows. Generic-only export wording found during live review was corrected to
derive scope from the saved run, including a safe historical-unknown fallback.

## Remaining verification

- Scanner/export identification, completion/retention guarantees and one observed physical handoff.
- Intended laptop/pager demo pairing and authoritative device-label clarification.
- Human clean-start presentation-laptop rehearsal and acceptance of the GUI draft.
- Full P1 integration, association/benign-decision policy, fine-tuning and fair evaluation.
- Distributed component taxonomy, real case/group labels, P2 fusion and model adaptation.
- Second supported NVIDIA laptop and separate CPU-host managed setup/actual-model acceptance;
  additional GPU vendors/platforms, HPC execution, other checkpoint backends and FALCON.
- Real collection-session evidence, registration/submission confirmations and student explain-back.

Meeting-reported model readiness is documented availability only. Check [status](status.md)
and [tasks](tasks.md) for current ownership and dependencies. Source artifacts and detailed
run outputs remain outside Git; shareable summaries do not replace those underlying records.
