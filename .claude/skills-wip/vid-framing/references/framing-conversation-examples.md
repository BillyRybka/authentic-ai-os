---
name: Framing Conversation Examples
type: skill-local-reference
loaded_by: vid-framing
when_to_read: All phases, examples to mirror conversational discipline
---

# Framing Conversation Examples

Worked dialogues showing how vid-framing should run a session. Each example shows the AI surfacing angles, the creator reacting, and the AI either adjusting or locking. Near-misses show the failure mode for each pattern. Every example assumes the silent loads from Phase 1 are already done.

## Convention markers used in these examples

- **Creator:** what the human says
- **AI:** what vid-framing says back
- *italic note*: design rationale for the skill builder (not part of runtime output)

## Example 1: Clean session, anchored angle picked

**Context:** brain-dump.md exists for the ADHD weekly planning piece. Pattern banks have T-7 (STOP pattern) HIGH confidence + Case Study format with creator's own past winner.

**Creator:** "Ready to frame the ADHD planning video."

**AI:**
> Loaded your brain-dump and pattern banks. Here are 4 angle candidates: 3 anchored, 1 experimental:
>
> **Angle 1 (HIGH-confidence anchor):** "Stop Using Time-Blocking If You Have ADHD"
> Anchor: T-7 STOP pattern. Outliers: "STOP Using These 5 Outdated Productivity Apps" (@CoachX, 1.4M), "STOP Planning Your Week Like This" (@CoachY, 800k).
> Why it could land: Brain-dump has your specific story about abandoning time-blocking after burnout. T-7 pattern lands consistently in this niche, audience expects contrarian framing of common advice.
> Risk: Needs a strong alternative in the body. Your "energy-blocking" needs to be specific in execution.
>
> **Angle 2 (HIGH-confidence anchor):** "How I Doubled My Client Load Using Energy-Blocking"
> Anchor: Case Study format. Outliers: your own "How I Went from 12 to 28 Clients in 90 Days" (320k, $4.20 DPV), @CoachZ's "How I 3x'd My Coaching Business" (500k).
> Why it could land: Personal result + named framework. Your past winner used this exact shape. Repeat What Works.
> Risk: Needs the specific 90-day timeline locked from your brain-dump.
>
> **Angle 3 (MEDIUM-confidence anchor):** "5 Weekly Planning Mistakes ADHD Brains Make"
> Anchor: Listicle pattern with counted hook. Outliers: 3 channels in your niche pulling this shape at 200-400k views.
> Why it could land: Listicles are warm-attracting in this niche. ADHD-specific narrows toward warm.
> Risk: Lower DPV signal than Angles 1 and 2. Better for views goal than sales.
>
> **Angle 4 (experimental, no anchor):** "I Threw Out My Calendar"
> No bank anchor. Gut framing using your personal-story material.
> Why it could land: Specific moment hook, unusual move, curiosity gap. Builds trust through transparency.
> Risk: No data behind this. Could flop or break out. Inherits more downside than the anchored options.
>
> Which one feels right? Or want to mix elements?

*Note: the AI surfaced 4 candidates, each with anchor + worked outliers + why + risk. No hand-waving. Creator can pick or modify.*

**Creator:** "Angle 2. I want to anchor on the past winner."

**AI:**
> Locked. Quick fit check:
>
> - Iceberg fit: ADHD coaches scaling past $10k/mo. Inside your lane, this is exactly what they came back for.
> - Predicted temperature: hot (specific result + named framework + your past winner already pulled hot DPV)
>
> Goal: sales, email, or views?

**Creator:** "Sales."

**AI:**
> Sales + hot temperature match. Strong fit. Now: format. Your packaging-system has Case Study as your locked primary, plus Listicle as a test slot. The anchor uses Case Study. Lock Case Study?

**Creator:** "Yep."

**AI:**
> Locked. Writing to piece.md now.
>
> - selected_angle: "How I Doubled My Client Load Using Energy-Blocking"
> - core_payoff: a 90-day Energy-Blocking method ADHD coaches can implement to double client capacity
> - format: case-study
> - goal: sales
> - viewer_stage: hot
> - outlier_anchor: "How I Went from 12 to 28 Clients in 90 Days" (your own channel, 320k views, $4.20 DPV)
> - anchor_confidence: high
>
> Dropped angles captured. Ready for vid-structure.

*Note: the lock step writes piece.md, captures dropped angles for stickiness, names next skill.*

## Example 1 near-miss, angle without an anchor

**The mistake:**

> **Angle 1:** "Stop Using Time-Blocking If You Have ADHD"
> Why this could land: STOP titles work well in your niche. Curiosity-gap framing. Your ADHD audience would relate.

**Why it fails:** no specific outlier cited. "STOP titles work well in your niche" is hand-waving. The creator can't evaluate the strength of the claim without seeing the actual outliers behind it.

**The fix:** every anchored angle must cite the specific bank entry (pattern + outlier titles + view counts + channel handles).

## Example 2: Creator picks the experimental angle

**Context:** same brain-dump, same banks.

**Creator:** "I want Angle 4."

**AI:**
> Experimental slot picked. Want to keep the angle as stated ("I Threw Out My Calendar") or rewrite it?

**Creator:** "Keep it. But I want to add, it'll be about how I switched to energy-blocking."

**AI:**
> Got it. Keeping the curiosity-gap hook, payoff is your energy-blocking framework. Quick fit check:
>
> - Iceberg fit: ADHD coaches scaling. Inside your lane.
> - Predicted temperature: warm-hot (personal-story hook + specific framework body)
> - Risk: no anchor means we're guessing on the title pattern's reach. Vid-title will need to use power-words-bank instead of a known title pattern.
>
> Goal?

**Creator:** "Email signups."

**AI:**
> Email goal + warm-hot temperature is a strong fit. Lead magnet aligned with energy-blocking would convert well from this. Format: short process, case study, or deep dive?

**Creator:** "Short process. Quick + practical."

**AI:**
> Locked. Writing piece.md.
>
> - selected_angle: "I Threw Out My Calendar"
> - core_payoff: switching from time-blocking to energy-blocking for ADHD brains
> - format: short-process
> - goal: email
> - viewer_stage: warm
> - outlier_anchor: null
> - anchor_confidence: experimental
>
> Dropped angles captured. Note: vid-title will run without a title-pattern anchor. It'll use your power-words-bank as the source. Heads up if you re-frame later.

*Note: experimental angle is first-class. The "no anchor" flag is communicated, the downstream impact is named.*

## Example 3: Creator modifies an anchored angle

**Context:** same brain-dump. Creator wants to rewrite Angle 1's exact wording.

**Creator:** "I like Angle 1 but I'd write it as 'I Stopped Time-Blocking, Here's What I Use Now.' More personal."

**AI:**
> Good rewrite. Same T-7 STOP pattern, but framed first-person. Anchor stays, that's just a different surface expression of the same pattern. Quick check on the predicted temperature:
>
> Original: "Stop Using Time-Blocking If You Have ADHD", predicted warm (imperative, audience-narrow)
> Your rewrite: "I Stopped Time-Blocking, Here's What I Use Now", predicted warm-hot (personal story + curiosity gap)
>
> The rewrite shifts slightly hotter. Still anchored. Confirm goal: sales?

**Creator:** "Yeah sales."

**AI:**
> Sales + warm-hot temperature. Good fit. Format: case study or short process?

**Creator:** "Case study."

**AI:**
> Locked. piece.md fields:
>
> - selected_angle: "I Stopped Time-Blocking, Here's What I Use Now"
> - outlier_anchor: T-7 STOP pattern, anchored to "STOP Using These 5 Outdated Productivity Apps" (@CoachX, 1.4M)
> - anchor_confidence: high
> - (other fields as expected)
>
> Note: the rewrite is sharper than the original. I'll capture that in dropped angles as "Original framing of Angle 1, replaced with creator's personal-story variation."

*Note: AI captures the original anchor + the creator's rewrite. Anchor confidence stays HIGH because the underlying pattern is unchanged.*

## Example 4: Bulk-keep / power-user mode

**Context:** experienced creator who knows what they want. Brain-dump is already tight.

**Creator:** "Frame it. Going for sales. Case study format. Hot audience."

**AI:**
> Power-user mode. Pulling 4 anchored candidates from banks and surfacing the strongest based on your stated goal/format/temperature. One second.
>
> ...
>
> Top match: Angle 2 from the standard set, "How I Doubled My Client Load Using Energy-Blocking", anchored to your past winner, HIGH confidence, hot-temperature fit, case-study format. Lock that one, or want the other 3 surfaced?

**Creator:** "Lock it."

**AI:**
> Locked. piece.md written. Ready for vid-structure.

*Note: power-user mode skips the fit-check conversation because the creator pre-locked goal/format/temperature. AI still ran the iceberg-fit + temperature check internally before surfacing.*

## Example 5: Mismatch surface (creator decides)

**Context:** brain-dump has lots of personal-story material + named framework. Creator says they want "views" goal.

**Creator:** "Frame it for views."

**AI:**
> Loaded banks. Heads up before surfacing, your brain-dump has heavy personal-story + named-framework material. That tends to attract hot-temperature audience. For views goal, you typically want broader, cold-attracting angles.
>
> Two paths:
> 1. Surface anchored angles tuned for cold-warm temperature (matches views goal). Less use of your personal-story material.
> 2. Surface anchored angles tuned for warm-hot. Better use of your material, but might underperform on raw views.
>
> Which way?

**Creator:** "Path 2. I'd rather build hot audience than chase views."

**AI:**
> Smart. Locking goal as views with the understanding it'll likely build temperature instead. Surfacing 3+1 angles now...

*Note: AI surfaces the mismatch transparently, doesn't block, follows creator's call. Source teaches no pre-prod kill, soft friction only.*

## Example 5 near-miss, silent mismatch

**The mistake:** AI surfaces 4 angles tuned for hot temperature without flagging that the creator said "views." Creator picks Angle 2, publishes, gets fewer views than expected, blames the framing skill.

**Why it fails:** the math was knowable in advance. AI should have surfaced the choice instead of guessing the creator's preference.

**The fix:** when goal × temperature mismatch detected, ALWAYS surface as soft friction before generating candidates.

## Example 6: Pattern banks stale or missing

**Context:** creator runs vid-framing but pattern-bank.md hasn't been refreshed in 6 months (or doesn't exist).

**AI:**
> Loading your banks... pattern-bank.md is 187 days old. The last full rebuild was [date]. Your niche has likely shifted in 6 months. Before framing, run vid-research to refresh, quarterly refresh takes 30-45 minutes.
>
> Want to refresh first, or proceed with stale banks?

**Creator:** "Proceed with stale. I'll refresh after this one."

**AI:**
> Got it. I'll surface candidates with the stale data, flag any HIGH-confidence anchors with `last_validated: stale`. Pick angles knowing the underlying patterns may have shifted.
>
> Surfacing 3+1 angles now...

*Note: surface staleness, let creator decide. Don't silently use stale data without flagging.*

## Conversational discipline rules embedded in these examples

1. **Listen during dumps.** When the creator drops 3+ sentences about what they want, hear the whole thing before responding.
2. **Specificity in proposals.** Every anchored angle cites the bank entry, outlier titles, view counts. No "this pattern works in your niche."
3. **Fit check runs after candidates surfaced.** Not before. Generate first, check fit second.
4. **Risk surfacing is mandatory.** Every angle has a risk line. No risk = not enough thought put in.
5. **Bulk-keep mode for experienced creators.** Don't drag a 10-question dialogue through someone who already knows what they want.
6. **Soft friction surfaces math, doesn't block.** Goal/temperature mismatch is surfaced, explained, creator decides.
7. **Save partial state.** If session ends mid-flow, frontmatter captures `piece_status: angle-in-progress` so resume works.
8. **Capture dropped angles with one-line rationale.** Sticky for future runs on this piece, don't re-surface dropped angles unless asked.

## What NOT to do

- Don't generate 7 angles "to give options." 3-4 is the rule.
- Don't surface angles without anchors as if they're anchored. The 4th slot is the only no-anchor slot.
- Don't water down a hot angle to make it views-friendly. Pick a different angle.
- Don't lock an angle that the brain-dump can't support. Flag thin material and route back to vid-intake.
- Don't fabricate outliers, view counts, or pattern bank entries. If the bank is thin, surface that.
