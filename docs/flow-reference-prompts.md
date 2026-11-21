# Flow reference images and short-video prompts

Prepared 19 October 2026 for the two owner-requested airport scenarios. These are concept
storyboards, not generated model evidence. Built-in image generation was attempted but
returned HTTP 429 `usage_limit_reached`; **no reference images were generated**. The user
can create the references in Flow with the image prompts below. Flow execution/export and
actual account entitlements remain untested. Related research: [tools](video-tools-research.md).

## Create three reference images

Use 16:9 landscape. Save each successful image before generating video. Reference 2 should
use Reference 1 as its visual reference; Reference 3 should also use Reference 1. These
prompts specify fictional adult characters and illustrative security screening only.

**Reference 1 — one passenger / checkpoint**

> Professional 3D animated airport explainer, believable adult proportions, soft daylight,
> navy/teal palette, single wide shot. One adult man with short dark hair, navy jacket,
> white shirt and charcoal trousers stands beside exactly four small matching upright
> suitcases: blue, green, yellow and red. All four bags fully visible and clearly his.
> A female security officer with tied-back dark hair, pale teal uniform and navy trousers
> stands beside a baggage X-ray scanner with black conveyor and blank dark monitor.
> Uncluttered modern checkpoint. No other passengers, bags, text, logos or weapons.

**Reference 2 — different passengers**

> Match the checkpoint, officer, lighting, 3D style and suitcase designs in Reference 1.
> Replace the lone passenger with exactly four distinct adults, standing apart, each with
> exactly one suitcase: original navy-jacket man with blue bag; curly-haired woman in
> green cardigan with green bag; older grey-haired man in mustard sweater with yellow
> bag; short-haired woman in red overshirt with red bag. Clearly separate ownership.
> Wide view, all people and bags fully visible. No extra bags, text or logos.

**Reference 3 — officer / monitor**

> Match Reference 1's female officer, scanner, daylight and professional 3D style.
> Over-the-shoulder view of the officer at a large dark monitor. Four evenly spaced,
> empty scan-card placeholders with blue, green, yellow and red borders. Blank central
> panel. Simple flat UI shapes, generous spacing, screen clearly visible. No readable
> text, scores, faces, actual X-rays, weapons or completed device.

## Video settings and shared instructions

Suggested: 16:9 landscape, one output, 8 seconds. Select a model/mode actually available
in the account; confirm its displayed cost. Use references as ingredients, or as start
frames where appropriate. Eight seconds fits the documented Veo ingredients restriction.
Render each scene separately; do not request four shots inside one generation.

Append to every video prompt:

> Preserve reference appearance and bag colors. Calm professional 3D animation, one
> continuous shot, no dialogue, captions, logos, panic, explosion or device assembly.

## Film A — one passenger, four bags

**A1 — Reference 1**

> Wide shot: navy-jacket passenger stands with his four colored suitcases. Officer
> gestures toward the conveyor; passenger rolls the blue suitcase forward. Slow push-in.

**A2 — Reference 1**

> Side view: blue suitcase travels alone on the conveyor into the X-ray tunnel. Passenger
> waits with green, yellow and red suitcases clearly beside him. Locked camera.

**A3 — Reference 3**

> Over-the-shoulder monitor close-up: four colored scan cards appear sequentially,
> one abstract highlighted shape per card. Cards collect beneath one generic passenger
> icon in the central case panel; a small amber review symbol appears. Slow push-in.

**A4 — References 1 and 3**

> Medium view: officer studies the monitor, then calmly gestures for secondary baggage
> inspection. Navy-jacket passenger waits beside his four suitcases. Locked camera.

Suggested manually added captions: One passenger, multiple bags / Separate scans /
Proposed case-level evidence review / Officer reviews the combined evidence.

## Film B — four passengers, separate bags

**B1 — Reference 2**

> Wide shot: four distinct passengers queue separately with their own matching-colored
> suitcases. Preserve the four owner-bag pairs. Queue advances slightly. Slow tracking shot.

**B2 — Reference 2**

> Side view: navy-jacket man places only his blue suitcase on the conveyor. Other three
> passengers wait separately with green, yellow and red bags. Locked camera.

**B3 — Reference 3**

> Over-the-shoulder close-up: officer manually selects four colored evidence cards,
> each retaining a distinct generic passenger icon, into one illustrative case panel.
> Only after selection, an amber review symbol appears. Locked camera. No identity matching.

**B4 — References 2 and 3**

> Medium view: officer examines the combined monitor view and gestures for secondary
> review. Four passengers remain visibly separate with their own colored bags. Calm scene,
> locked camera, no arrest or implication that identity alone proves a threat.

Suggested manually added captions: Different passengers, separate bags / Separate scans /
Illustrative case linkage supplied externally / Proposed joint review of component evidence.

Keep **Illustrative scenario - proposed multi-package capability** visible in the edited
films. Add readable captions, deterministic evidence graphics and any genuine GUI footage
after generation. If generated ownership, cards or monitor graphics drift, use controlled
graphics in the editor rather than treating the output as evidence. Generating a single
bag entering the scanner avoids asking the model to execute four timed scans in one clip;
the later evidence panel represents those separately supplied scans conceptually.
