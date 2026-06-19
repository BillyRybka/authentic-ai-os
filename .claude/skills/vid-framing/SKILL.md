---
name: vid-framing
description: Pick the angle for one specific video. Surfaces 3 outlier-anchored angle candidates plus 1 experimental angle from the creator's pattern banks and brain-dump. Runs one iceberg fit check (is the angle inside the lane the creator serves), predicts audience temperature (cold/warm/hot), confirms format from the creator's current packaging defaults, locks goal (sales/email/views). Output: framing decisions appended to `content/pieces/{slug}/piece.md` with the four locked fields downstream skills consume (selected_angle, core_payoff, format, goal, viewer_stage). Anti-fabrication, every anchored angle cites a real bank entry. Standalone OR invoked by vid-pipeline. Phrases like "frame the video", "pick the angle", "frame this piece", "what's the angle for this", "lock the framing", "what should this video be about", "re-frame this piece", "what angles do I have on [topic]", or any downstream pipeline that needs an angle locked before structure starts should fire this skill.
---

# Video Framing

Picks the angle for one specific video. Surfaces 3-4 candidates anchored to real pattern-bank outliers (with one experimental slot for the creator's gut pick), runs one iceberg fit check, locks the angle plus format plus goal plus predicted audience temperature, writes the framing decisions to `piece.md`. Downstream skills (vid-thumbnail, vid-title, vid-intro, vid-segment, vid-ending) read piece.md for their context.

**Scope boundary:** this skill produces the ANGLE only. It does not write titles (`vid-title`), thumbnail briefs (`vid-thumbnail`), scripts (`vid-structure` / `vid-intro` / `vid-segment` / `vid-ending`), or measurement (`vid-measurement`, future). It does not re-litigate iceberg or Top 3 problem alignment, those were locked upstream by `vid-intake`.

## What this produces

Framing decisions written into `content/pieces/{slug}/piece.md`. Fields appended to existing frontmatter, body sections appended after existing content. See `assets/piece-framing-additions.md` for the exact shape.

Locked fields after vid-framing completes:

- `selected_angle`, the picked angle, in the creator's voice, one sentence
- `core_payoff`, what the viewer gets from the video in one sentence
- `format`, one of case-study | short-process | deep-dive | listicle | roast | interview | news (from creator's current packaging defaults unless the creator knowingly overrides)
- `voice_context`, the delivery medium for voice. Default `youtube-script`. Set to tutorial | shorts | newsletter | linkedin | twitter | podcast | casual | talk only if this piece is genuinely that medium. Orthogonal to format. Drives which `foundation/reference-pieces/{voice_context}.md` the writing skills load
- `goal`, sales | email | views
- `viewer_stage`, cold | warm | hot (predicted audience temperature)
- `outlier_anchor`, the specific pattern-bank outlier this angle anchors to, or null for experimental
- `anchor_confidence`, high | medium | low | experimental (derived from the anchor's spread + own_channel_proven, not read from a stored label)
- `last_updated: {today}`

Body sections appended: Selected Angle, Why This Angle Lands, Considered + Dropped Angles.

## When to run this

- The creator has run vid-intake on a brain-dump and is ready to pick the angle
- The creator wants to re-frame an existing piece (the first angle wasn't right)
- vid-pipeline (future) invokes after vid-intake completes and before vid-title (framing precedes packaging)

## Prerequisites

Hard requirements:
- `content/pieces/{slug}/brain-dump.md` exists with the raw material AND `iceberg_aligned: true` (vid-intake locked this)
- `content/pieces/{slug}/piece.md` exists (created at piece-folder creation)
- `foundation/creator-foundation.md` exists with iceberg + audience profile
- `foundation/packaging-system.md` exists with the starting format rotation (3 core + 1 experimental) and current thumbnail test strategies
- `banks/pattern-bank.md` exists and is less than 120 days old (sticky-curated quarterly refresh)

Soft requirements:
- `foundation/voice-profile.md` for mirroring style during the conversation
- `foundation/reference-pieces/youtube-script/` for rhythm reference when mirroring style in conversation (default context; vid-framing does not write prose)

## Invocation modes

**Standalone:** creator invokes directly with a slug ("frame the ADHD planning piece"). Skill loads the piece's brain-dump, surfaces 3+1 angles, runs the iceberg fit check, locks the call, writes piece.md.

**Sub-skill:** vid-pipeline invokes after vid-intake completes. Skip the "which piece?" prompt, caller already passed the slug. Return a status packet on completion (`{selected_angle, outlier_anchor, last_updated}`).

**Re-frame mode:** detected when piece.md already has a `selected_angle`. Surface the previously selected angle and the previously dropped angles. Ask: "Re-frame from scratch, or refine the existing angle?" Don't re-surface dropped angles unless the creator says so.

## The 5 phases

### Phase 1: Silent context load

Silent loads (do NOT paste into chat):

1. `content/pieces/{slug}/brain-dump.md`, the raw material plus the locked `problem_addressed`, `iceberg_aligned`, `intake_mode` from vid-intake
2. `content/pieces/{slug}/piece.md`, existing frontmatter (slug, pillar, created, any prior framing if re-framing)
3. `foundation/creator-foundation.md`, iceberg statement, audience profile
4. `foundation/voice-profile.md`, preferred_hook_types, opener pattern, energy baseline (style only)
5. `foundation/packaging-system.md`, starting format rotation, current thumbnail test strategies
6. `banks/pattern-bank.md` (synthesis sections + topic clusters folded into synthesis + per-outlier full-package rows). This is the only research bank vid-framing loads. The sub-banks (`title-bank.md`, `power-words-bank.md`) are loaded by vid-title at write time, not by vid-framing for angle selection. Format comes from `foundation/packaging-system.md` rotation, not a bank.
7. `knowledge/outlier-identification-rules.md`, fluke filter logic
8. `knowledge/audience-temperature-model.md`, temperature definitions
9. `knowledge/three-circle-research.md`, own + niche + adjacent methodology (read once, don't re-explain)
10. `knowledge/format-planners/{format}.md`, loaded per candidate angle for format-fit reasoning

**Hard friction checks during load:**

- `brain-dump.md` missing → "No brain-dump for this piece. Run vid-intake first to capture the raw material."
- `pattern-bank.md` missing → "No pattern banks. Run vid-research first, first-build takes ~1.5 hours."
- `pattern-bank.md` older than 120 days → soft friction: "Your pattern banks are {N} days old. Want to refresh first (30-45 min) or proceed with stale data?"
- `creator-foundation.md` missing → "No foundation docs. Run /foundation first to lock the iceberg + audience profile."

### Phase 2: Angle generation

Generate 4 angle candidates total: 3 anchored + 1 experimental.

**For each of the 3 anchored angles:**

1. Pull a strong or moderate outlier from the pattern banks (strength derived from spread + own_channel_proven; see angle-anchor-rules.md). Prioritize the creator's OWN past winners (highest DPV signal). Then niche channel outliers. Then adjacent-niche structural patterns.
2. Match to brain-dump material, does the creator's raw material support this angle without stretching?
3. Run the fluke filter, confirm the anchor is on-niche for its source channel (`knowledge/outlier-identification-rules.md`).
4. Construct the angle. Use the creator's voice (from voice-profile). Specific, concrete, in one sentence.

**For the 1 experimental angle:**

- Use creator's brain-dump material that doesn't map cleanly to existing patterns (unique story, contrarian framing, adjacent-niche structural transfer)
- OR ask the creator: "Want a 4th angle from your gut? Drop the framing if you have one."
- Flag: `anchor_confidence: experimental`, `outlier_anchor: null`

**Each candidate surfaces with:**

- One-sentence angle in creator's voice
- Anchor citation (specific outlier title + channel + view count) OR "experimental, no anchor"
- One-line "why this could land" (tied to brain-dump material AND anchor strength)
- One-line risk

See `references/framing-conversation-examples.md` Example 1 for the worked surface format.

**Anti-fabrication rule:** every anchored angle MUST cite a real bank entry. Never invent an outlier. If the bank is thin, surface that as soft friction.

See `references/angle-anchor-rules.md` for the full anchor logic, fluke filter application, and the strong/moderate/weak/experimental strength definitions (derived from spread).

### Phase 3: Fit check + temperature

For each angle (or in bulk-keep mode, for the angle the creator pre-selects), run two checks:

- **Iceberg fit (the only fit gate):** is this angle inside the lane the creator serves (the iceberg)? Inside = keep. Outside = drop. That's the whole fit decision. Do NOT map the angle to a Top 3 problem, do NOT stamp it `outlier`. The angle plus the brain-dump already say what the video is about; the writing skills (vid-intro, vid-segment, vid-ending) pick which problem they poke at write time, from the foundation. Framing does not re-derive it.
- **Predicted temperature:** what audience temperature will this angle attract? (cold / warm / hot, see `references/audience-temperature-fit.md`). This drives the `viewer_stage` field downstream skills read.

Surface the two answers per angle. Creator confirms or pushes back.

**Bulk-keep mode:** if the creator says "this one's obvious, skip the check," the AI still runs the iceberg-fit + temperature check INTERNALLY before surfacing. Only skip the conversation, not the check.

**Soft friction during the check:**
- Angle sits outside the iceberg → "This angle is outside the lane you've built. Want to lock it anyway (a deliberate stretch), or pick one inside the iceberg?"

### Phase 4: Lock the call

The creator picks 1 of the 4 angles. Then:

1. **Confirm format.** If the anchored outlier has a clear format (e.g., Case Study anchor), default to that. Otherwise, show the creator's current packaging defaults (3 core + 1 experimental) and let them pick.
   - **Default, not a cage:** lead with the formats in the creator's packaging-system rotation (3 core + 1 experimental), not all 7, so the channel keeps a recognizable rhythm. But the creator can knowingly override and pick a different format for this video. If they want one off-rotation, let them and note it; don't block it.
2. **Pick goal.** Sales, email, or views? Tied to the offer ecosystem.
3. **Set voice_context.** Always write the field to piece.md, even when it stays `youtube-script`, so downstream skills read an explicit value and never guess. Do not ask the creator unless this piece is genuinely a different delivery medium (a screen-share tutorial, a short, a written newsletter cut). It is orthogonal to format: a listicle can be a youtube-script or a tutorial. Only override the default when the medium clearly differs.
4. **Confirm viewer_stage.** Default to the temperature predicted in Phase 3. If goal/temperature mismatch (e.g., sales goal + cold temperature), surface the conversion math, see `references/audience-temperature-fit.md`, and let the creator decide.
5. **Capture dropped angles' rationales.** One line each. Sticky for future runs on this piece.

**Soft friction at lock:**
- Goal × temperature mismatch → surface the math, creator decides
- Brain-dump material thin for the selected angle → "Heads up, your brain-dump is light on the specifics this angle needs. Want to lock and route back to vid-intake for more capture, or pick a less specific angle?"

### Phase 5: Update piece.md

Append framing fields to piece.md frontmatter. Append body sections. Set `last_updated: today`. Capture dropped angles in `## Considered + Dropped Angles`.

See `assets/piece-framing-additions.md` for the exact append protocol.

**Append rules:**
- Never overwrite fields owned by other skills (see piece.md schema in build-plan.md for ownership matrix)
- Never delete previous Considered + Dropped entries (append only, sticky)
- Set `last_updated` to today YYYY-MM-DD

After save, confirm with one-line summary plus next-skill prompt:

```
Framing locked. piece.md updated.
- Angle: {selected_angle}
- Format: {format}, Goal: {goal}, Audience: {viewer_stage}
- Anchor: {outlier_anchor or "experimental"}

Next: lock the title (vid-title), then the thumbnail (vid-thumbnail). Packaging comes before structure.
```

## Conversational discipline

- **Listen during dumps.** If the creator drops 3+ sentences about what they want, hear it all before responding.
- **Specificity in proposals.** Every anchored angle cites the bank entry by name (outlier title + channel + views). No "this pattern works in your niche" hand-waving. See the near-miss in `references/framing-conversation-examples.md` Example 1.
- **Fit check after candidates, not before.** Generate first, check fit second.
- **Risk surfacing is mandatory.** Every candidate has a risk line.
- **Bulk-keep mode for experienced creators.** Don't drag a 10-question dialogue through someone who pre-locked goal/format/temperature.
- **Save partial state.** If the session ends mid-flow before the angle locks, piece.md simply has no `selected_angle` yet. Re-running vid-framing (or vid-pipeline) resumes here. No separate in-progress flag.

See `references/framing-conversation-examples.md` for the worked dialogues.

## Hard friction (auto-flag, stop)

1. `brain-dump.md` missing → redirect to vid-intake
2. `pattern-bank.md` missing → redirect to vid-research
3. `creator-foundation.md` missing → redirect to /foundation
4. Em-dashes anywhere in the productized output (brand-level no)
5. Attribution leaks, no Ed/YGS/named-source language ever
6. Fabricated outliers, every anchored angle must cite a real bank entry
7. Cited outlier is weak-spread (1-2 channels, not own-channel-proven) being surfaced as one of the 3 anchored slots (must be strong or moderate)

## Soft friction (surface and explain, creator decides)

1. Pattern banks stale (>120 days), surface, offer refresh-first option
2. Goal × temperature mismatch, surface the conversion math (see `references/audience-temperature-fit.md`)
3. Selected format outside current packaging defaults, surface, creator knowingly overrides
4. Brain-dump thin for selected angle, flag what's missing, suggest vid-intake refresh
6. Low anchor diversity (e.g., all 3 anchored candidates come from one channel), surface, suggest broader research

## Reference index

| File | When to read it |
|---|---|
| `references/angle-anchor-rules.md` | Phase 2, the 3+1 split rule, anchor strength derived from spread, fluke filter application, what counts as a real anchor versus hand-waving, Repeat What Works affirmative surfacing, adjacent-niche structural transfer for experimental slot |
| `references/audience-temperature-fit.md` | Phase 3 + Phase 4, predicting temperature from angle + brain-dump, goal × temperature match matrix, specificity dial calibration, soft friction surfacing |
| `references/framing-conversation-examples.md` | All phases, worked dialogues for clean session, experimental pick, modified angle, bulk-keep, mismatch surface, stale banks |
| `knowledge/audience-temperature-model.md` | Phase 3. Audience Temperature Model definitions (shared with vid-ending, future vid-measurement) |
| `knowledge/outlier-identification-rules.md` | Phase 2, fluke filter (shared with vid-research) |
| `knowledge/three-circle-research.md` | Phase 2, own + niche + adjacent methodology (shared with vid-research, future vid-channel-audit) |
| `knowledge/format-planners/{format}.md` | Phase 2 + Phase 4, format shape reference (matched to candidate format) |
| `assets/piece-framing-additions.md` | Phase 5, exact frontmatter fields and body sections to append to piece.md |

## Principles (the why)

- **Anchored beats invented.** AI-generated angles without evidence sound confident but flop at scale. Anchoring to a real outlier turns guesses into hypotheses backed by data.
- **3 + 1 protects both discipline AND creativity.** Three anchored angles keep the creator from drift. One experimental slot protects intuition from being suppressed.
- **The creator's judgment is irreplaceable.** AI surfaces candidates with evidence. The creator picks. Does this fit MY audience? Only the creator can answer.
- **Repeat What Works is GOOD, not boring.** When the creator's own past winner anchors a new angle, surface that as a strong signal, not a "you already did this." Diminishing returns kick in around 3 repeats, until then, lean in.
- **Temperature is a controllable dial.** The same brain-dump can frame cold, warm, or hot depending on specificity choices. vid-framing surfaces the dial; the creator picks the temperature that matches the goal.
- **Drop nothing silently.** Every dropped angle gets a one-line rationale captured in piece.md. Sticky across runs. Prevents the AI from re-surfacing patterns the creator has already rejected.

## Related skills

- The `/foundation` chain produces creator-foundation.md (iceberg, audience, and the Top 3 problems the writing skills use later), vid-framing reads the iceberg + audience for fit
- `vid-voice-capture` produces voice-profile.md, vid-framing reads for mirroring style only
- `vid-research` produces the 3 research banks (pattern-bank, title-bank, power-words-bank) vid-framing consumes, primary upstream contract
- `vid-intake` produces brain-dump.md plus the locked `iceberg_aligned` + `problem_addressed` fields, vid-framing reads, does NOT re-derive
- `vid-thumbnail` reads piece.md `format` + `selected_angle` for thumbnail brief
- `vid-title` reads piece.md `selected_angle` + `outlier_anchor` plus `title-bank.md` and `power-words-bank.md` (uses anchor's title pattern if anchored, falls back to power-words-bank if experimental)
- `vid-structure` reads piece.md + brain-dump.md and builds the script.md skeleton (title + thumbnail already locked in packaging; structure does not invoke them)
- `vid-intro` reads piece.md `format`, `core_payoff`, `viewer_stage`, `selected_angle`
- `vid-segment` reads piece.md `selected_angle`, `format`, `goal`
- `vid-ending` reads piece.md `goal`, `viewer_stage` (CTA placement depends on temperature)
- `vid-pressure-test` reads piece.md + script.md for source-traceability audit
- `vid-pipeline` (future) orchestrates the full flow
