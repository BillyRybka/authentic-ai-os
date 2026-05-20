---
name: Audience Temperature Fit
type: skill-local-reference
loaded_by: vid-framing
when_to_read: Phase 3 (Theory of One filter) and Phase 4 (lock the call)
---

# Audience Temperature Fit

This reference is the vid-framing-specific application of the Audience Temperature Model. The model itself lives in `knowledge/audience-temperature-model.md` (shared). This file is HOW vid-framing uses it: predicting the temperature an angle will attract, surfacing mismatches with the goal, locking the viewer_stage field.

## What this file is FOR

- Deciding which `viewer_stage` value (cold/warm/hot) to write into piece.md for the selected angle
- Surfacing goal/temperature mismatches as soft friction during Phase 3
- Calibrating specificity during Phase 4 if the creator wants to shift the temperature an angle attracts

## What this file is NOT for

- Re-explaining the Audience Temperature Model, load `knowledge/audience-temperature-model.md` for that
- Decisions made AFTER framing (CTA placement = vid-ending; retention math = vid-pressure-test)

## Predicting temperature from angle + brain-dump

vid-framing can't measure temperature pre-publish. It predicts based on FOUR observable choices:

1. **Topic breadth**, how narrow is the angle? Broad = cold-attracting. Specific = warm/hot-attracting.
2. **Problem framing language**, generic problem ("how to grow") = cold. Specific problem ("how to fix retention on a 7-min deep dive") = hot.
3. **Stories in the brain-dump**, generic illustrative stories = cold. The creator's own client wins or personal results = warm/hot.
4. **Frameworks referenced**, borrowed external frameworks = cold. The creator's named systems = hot.

For each candidate angle, score the four choices. Map to a viewer_stage:

| Choices scored | viewer_stage |
|---|---|
| 3-4 cold-attracting | cold |
| Mixed (2 cold, 2 hot-leaning) | warm |
| 3-4 hot-attracting | hot |

This is predictive, not exact. The creator can override if their reading of the brain-dump differs.

## The goal × temperature mismatch surface

After predicting viewer_stage for each angle, vid-framing checks it against the goal the creator picks in Phase 4.

| Goal | Compatible viewer_stage | What happens if mismatched |
|---|---|---|
| sales | hot (ideal), warm (acceptable for low-ticket) | Surface as soft friction. Cold-temperature sales video math: 250k views → 10 sales. Hot-temperature: 50k views → 40 sales. Creator can override if they're building a hot-audience flywheel. |
| email | warm (minimum), hot (better) | Surface if cold. Lead magnets need clearly aligned audience to convert. |
| views | cold OR warm acceptable. Hot is fine but underutilizes the offer. | Surface if hot and the creator hasn't named a reason. Hot-temperature views videos often signal a goal mismatch, the angle is too narrow for views, should be re-framed broader OR the goal should change to sales/email. |

**Hard rule for vid-framing:** don't BLOCK on mismatch. Surface, explain the math, creator decides. Source teaches no pre-production kill criteria, kill happens at measurement.

## Worked example, mismatch surface

Brain-dump topic: ADHD weekly planning method. Creator's stated goal: `views`.

vid-framing surfaces 4 angles, predicts temperature on each:

- **Angle 1 (anchored T-7 STOP pattern):** "Stop Using Time-Blocking If You Have ADHD", predicted **warm** (narrow problem framing, creator's own story)
- **Angle 2 (anchored Listicle):** "5 Weekly Planning Mistakes ADHD Brains Make", predicted **cold-warm** (counted listicle attracts cold, but ADHD-specific narrows toward warm)
- **Angle 3 (anchored Case Study):** "How I Doubled My Client Load Using Energy-Blocking", predicted **hot** (specific result, creator's own framework)
- **Angle 4 (experimental):** "I Threw Out My Calendar", predicted **warm-hot** (personal-story framing creates trust + curiosity)

Goal is `views`. The predictions show that 2 of 4 candidates are warm-hot, which would attract a hotter audience than the goal targets.

**Soft friction surface:**

> Your goal is views, but Angles 3 and 4 are likely to attract a hot audience (specific results, personal-story framing). Hot-temperature views videos often underutilize the audience, you'd convert more if you used these for a sales goal instead.
>
> Two options:
> 1. Pick Angle 1 or 2, broader framing, more views-attracting
> 2. Change the goal to sales. Angle 3 or 4 will likely sell better than they'll view

Creator decides. vid-framing doesn't block.

## Calibrating temperature via specificity

If the creator wants to shift an angle's predicted temperature, they shift the specificity dial. Both directions:

**Hotter (more specific):**
- Add the creator's specific result ("doubled my client load" → "doubled my client load in 90 days")
- Name the creator's framework ("a planning method" → "energy-blocking")
- Add audience-specific qualifier ("for ADHD" → "for ADHD coaches scaling past $10k/mo")

**Colder (less specific):**
- Remove proper nouns / named systems
- Replace results with generic outcomes ("doubled my client load" → "got more clients")
- Broaden audience reference ("for ADHD coaches" → "if you have ADHD")

vid-framing's job is to surface the dial, not to make the call. The creator picks.

## The "specificity creep" warning

When trying to make an angle "more interesting," AI tends to ADD specificity automatically. This is usually wrong, it shifts the temperature without the creator deciding.

If during the framing conversation an angle's specificity changes during refinement, ASK before locking: "I added [specific detail]. This shifts the predicted temperature from [X] to [Y]. Still good?"

## The "broaden it for views" trap

When goal is views and predicted temperature is hot, the obvious move is "broaden the angle." Sometimes this works. Sometimes it kills the angle's appeal entirely.

The trap: broadening can strip the specific edge that made the angle interesting. "How I doubled my client load using energy-blocking" → "Productivity tips for ADHD" loses everything that made the first version pull.

Better than broadening: pick a DIFFERENT angle from the brain-dump that's natively broader. Don't take a hot-temperature angle and water it down. Take a cold-temperature angle and run that one.

## Temperature signals from the pattern bank

When an anchor outlier comes from the creator's own channel and has high DPV, that's a hot-temperature signal. When the same outlier has high views but low DPV, that's a cold-temperature signal.

For anchored angles, the anchor's temperature is the strongest predictor of the new video's temperature. If the anchor pulled hot for the creator, the new angle copying that anchor's pattern will probably pull hot too.

Anchor temperature signals (when available from vid-measurement):
- High DPV (>$1/view) → hot anchor
- Medium DPV ($0.10-$1/view) → warm anchor
- Low DPV (<$0.10/view) → cold anchor or low conversion regardless of temperature

Without DPV data (first build, no measurement history), default to "warm" prediction for own-channel anchors and "cold" for niche-channel anchors. Adjust as measurement data fills in.

## Edge cases

### Mixed-temperature angle

Sometimes an angle has cold-attracting hooks but hot-payoff body. Example: "5 Productivity Mistakes ADHD Brains Make" (cold hook) → body delivers the creator's specific Energy-Blocking framework (hot payoff).

Predicted viewer_stage: take the BODY-level temperature. The hook brings them in; the body determines what audience they leave as. Lock as `warm` for this kind of mixed-temperature angle.

### Cold-anchor angle with hot brain-dump material

When the anchor pattern is cold (e.g., a generic listicle outlier) but the creator's brain-dump material is hot (specific results, named frameworks), the predicted temperature is warm-hot. The angle inherits the brain-dump's specificity even when the anchor pattern is generic.

### Hot-anchor angle with thin brain-dump material

When the anchor pattern is hot but the creator's brain-dump doesn't have the specific stories/frameworks/results to support that level of specificity, FLAG it. The angle will under-deliver because the body can't match the hook's promise.

Surface as soft friction: "This angle would attract a hot audience based on the anchor, but your brain-dump is thin on the specifics that would land. Consider returning to vid-intake to capture more, or pick a less specific angle that matches the material you have."

## Quick-reference matrix

| Angle attribute | Cold-attracting | Warm-attracting | Hot-attracting |
|---|---|---|---|
| Topic specificity | Generic ("productivity") | Topic-narrow ("ADHD productivity") | Audience-narrow ("ADHD coaches scaling past $10k") |
| Problem framing | Universal | Niche-specific | Stage-specific within niche |
| Stories | Illustrative / external | Creator's experience | Creator's client wins with numbers |
| Frameworks | Borrowed / common | Adapted to creator's context | Creator's named system |
| Title pattern | Listicle, counted, news-jack | Case study, specific result | Deep dive, named-system, edge case |

Use this matrix during Phase 2 (angle generation) to predict each candidate's temperature. Use it during Phase 4 (lock the call) to confirm or adjust the viewer_stage field before writing piece.md.
