---
type: reference
skill: vid-pressure-test
reviewer: retention-logic
tags: [reviewer-rubric, retention, tension-architecture]
---

# Retention-Logic Reviewer Rubric

Phase 2 reviewer 4. Fresh-context spawn. Single job: check the spine of the script. Does the script keep tension live across all sections? Does the title-promise pay off late, not early? Do opened threads close? Does each segment serve the locked frame? Does the ending pivot correctly?

This is the ONLY reviewer that reads the whole script in one go to catch emergent cross-section problems.

## Sources of truth

1. `knowledge/script-tension-architecture.md`: the three load-bearing tactics: title-promise lock, setup-payoff threading, segment handoffs
2. `knowledge/format-planners/{format}.md`: format-native tension arc for this piece (Case Study, Listicle, Short Process, Deep Dive, News, Roast, Interview)
3. `content/pieces/{slug}/piece.md`: locked title, frame, format, goal (audience temperature is judged from the script itself, not read from a field)
4. `content/pieces/{slug}/script.md`: the full script being audited

## What to check (the 5 retention gates + 3 anti-patterns)

The 5 gates cover the spine. The 3 anti-patterns are specific failure modes from `knowledge/script-tension-architecture.md` Section "Anti-patterns": **promise drift** (title promises X, body delivers adjacent-X), **stacked lessons** (no thread connects segments, each a complete lesson), **cliffhanger-as-content** (script opens loops it never closes, treating the open question as a substitute for substance). Walk all 5 gates AND scan for the 3 anti-patterns. Either failure type can land in the top 3.

### Gate 1: Top 3 viewer questions delivered

The intro's Setup section names "in this video I'm going to show you X, Y, Z" (or the format's equivalent). Walk the body. Are X, Y, Z each delivered? If the Setup promises three things and the body delivers two, the third is an orphaned promise. Retention dies in the segment after the missed delivery.

### Gate 2: Title-promise location

The title makes an implicit promise (the question the viewer clicked to answer). When does the full answer land in the body? Per script-tension-architecture.md, it should land LATE (past midpoint) for most formats. Case Study lands at the Outcome beat. Listicle lands at the final item. Short Process at step-end. News compresses the wait.

Read `tension_plan` from piece.md: the full answer landing before `title_promise_segment` is early-payoff. When the plan is absent, the fallback signal is the full answer landing in segment 1 or 2 of a 5-segment piece. Viewers who got the answer leave.

### Gate 3: Open loops close

Walk the script and find every open loop. "We'll come back to this." "More on that later." Implicit setups that promise something later. For each, check: does the loop close? Same scene returns, question gets answered, character pays off. If a loop opens and never closes, viewers feel cheated.

### Gate 4: Each segment serves the locked frame

Read piece.md `frame`. Walk each segment. Does the segment material serve THAT angle, or did it drift to a related but different angle? Off-angle segments fragment the piece. They feel like tangents the creator could not resist.

### Gate 5: Ending pivots correctly per goal × audience temperature

Read piece.md `goal`. Judge audience temperature (cold/warm/hot) from the script itself, then cross-check against `knowledge/audience-temperature-model.md` and the format planner's ending guidance.

- `goal: sales` → ending CTA should reference offer / sales link. Clear ask.
- `goal: emails` → ending CTA should reference lead magnet / list signup. Specific to the piece's challenge.
- `goal: views` → ending should pivot to next video. No external links that kill recommendations.
- Cold temperature → CTA tighter, less ask. Hot temperature → ask harder.

If the ending CTA mismatches goal or temperature, retention of intent dies even when retention of attention held.

## Severity tiers

**Hard issue (retention killer):**

- Top 3 question not delivered (orphaned setup)
- Title-promise fully resolved before the `tension_plan` payoff segment (early-payoff)
- Open loop never closes
- Off-angle segment that breaks the through-line
- Ending CTA wrong for the goal (e.g., sales goal with no offer reference, views goal with external link)

**Soft issue (retention risk):**

- Title-promise resolves slightly earlier than format ideal (still in body but not optimally late)
- Open loop closes but loosely (creator references it but does not pay off cleanly)
- Segment drifts adjacent to angle (related but slightly off)
- Ending CTA matches goal but is weak (mentions offer but no specificity)
- Cold handoff between segments (no forward-hook into next segment)

## Returning the top 3

Rank by severity. Killers first. Then risks. The 4 retention gates that failed get priority over soft retention risks.

Each issue:

```
Reviewer: retention-logic
Location: {section spans, e.g. "Intro Setup vs Segment 3" or "Segment 4 line 8"}
Quote: "{exact relevant text from script.md, may span 2 lines for orphan checks}"
Issue: {which gate failed and how}
Suggested fix: {specific restructure recommendation, sometimes spanning multiple sections}
```

Retention issues often span sections. The quote may need to include both the setup AND the missing payoff to make the issue clear.

## Worked examples

### Example 1: orphaned promise (HARD)

Intro Setup: "In this video I'm going to show you three things: the mistake, the system I use instead, and the three-step rollout."

Walk body. Segment 1 covers the mistake. Segment 2 covers the system. Segments 3-4 cover something else (lead magnet positioning). Ending wraps. Three-step rollout never appears.

```
Location: Intro Setup vs Body coverage
Quote: "In this video I'm going to show you three things: the mistake, the system I use instead, and the three-step rollout." (Intro Setup) vs the body does not contain a three-step rollout.
Issue: Setup promises 3 deliverables. Body delivers 2. The three-step rollout is orphaned.
Suggested fix: Either add a segment that delivers the three-step rollout, OR tighten the Setup to only promise what the body actually delivers ("two things: the mistake, and the system I use instead").
```

### Example 2: early payoff (HARD)

Title: "Why I Quit Posting Daily And Grew My Channel 10x"

Implicit promise: viewer wants to know the reason and the alternative.

Script: Segment 1 (of 5) reveals: "The reason is that daily posting destroyed my quality, and the alternative is to post twice a week with 5x the production effort per video."

Segments 2-5 elaborate examples.

```
Location: Title-promise resolves in Segment 1 of 5
Quote: "The reason is that daily posting destroyed my quality, and the alternative is to post twice a week..." (Segment 1 line 4)
Issue: Title promised the why and the alternative. Both land in segment 1. Segments 2-5 have nothing to hold the viewer who just got their answer.
Suggested fix: Restructure. Segment 1 reveals the failure (no alternative yet). Segments 2-3 deliver pieces of the alternative. Segment 4 reveals the full system. Segment 5 shows the result. Title-promise lands at segment 4, past midpoint.
```

### Example 3: open loop never closes (HARD)

Segment 2 line 6: "And there is a third reason I don't share publicly. I'll come back to it."

Walk script. Segments 3, 4, 5 do not mention the third reason. Ending does not mention it.

```
Location: Segment 2 line 6 (open) vs Segments 3-Ending (no close)
Quote: "And there is a third reason I don't share publicly. I'll come back to it."
Issue: Explicit open loop. Never closes. Viewer who tracked the promise feels cheated.
Suggested fix: Either close the loop in segment 4 or 5 (add the third reason), OR remove the open-loop sentence entirely (do not promise what you will not deliver).
```

### Example 4: ending CTA mismatch (HARD)

piece.md: `goal: sales`. The script reads warm: it assumes the viewer knows the creator and names the offer's problem as familiar ground.

Ending CTA: "Subscribe and hit the bell for more content like this."

```
Location: Ending CTA
Quote: "Subscribe and hit the bell for more content like this."
Issue: Goal is sales and the script reads warm. CTA should reference the offer, not request a subscribe. Warm viewers are ready for the ask.
Suggested fix: "If you want this exact system done for you, the link to {offer} is in the description. Warm viewers convert there. Anyone else, the next video walks through {related topic}."
```

### Example 5: cold handoff (SOFT)

Segment 3 ends: "And that is the second principle."

Segment 4 opens: "The third principle is about consistency."

```
Location: Segment 3 close vs Segment 4 open
Quote: "And that is the second principle." / "The third principle is about consistency."
Issue: Cold handoff. Segment 3 closes cleanly, segment 4 opens cold. No forward-hook to pull the viewer across the boundary. Retention dips at segment boundaries when handoffs are cold.
Suggested fix: Add a forward-hook to the segment 3 close: "And that is the second principle. The third is the one that surprised me." Now segment 4's opener pays it off naturally.
```

## What this reviewer does NOT catch

- Fabricated claims (source-traceability)
- Voice violations (voice-authenticity)
- AI-slop phrases (AI-slop reviewer)

Focus on the structural spine.

## Format-specific weighting

The format planner adjusts the gates:

- **Case Study:** Gate 2 (title-promise) is the strongest gate. Outcome lands at narrative peak.
- **Listicle:** Gate 1 (Setup delivery) and progression (each item N+1 > N).
- **Short Process:** Gate 4 (each step serves the system) and step-end full-system payoff.
- **Deep Dive:** Gate 3 (cross-segment threads layered) most critical.
- **News:** Gate 2 with compression (named answer lands earlier than other formats).
- **Roast:** Gate 4 (each call-out serves the central premise).
- **Interview:** Gate 1 (questions promised get answered).

## Meta-check

After surfacing the top 3 retention issues, ask: "If the creator fixes only these 3, does the script's spine hold?" If yes, the ranking is correct. If the spine still has obvious holes after these 3, the cap is hiding too much; surface a note: "Additional retention risks detected. Consider second pass after these resolve."
