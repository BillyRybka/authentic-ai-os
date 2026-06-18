---
type: skill-reference
skill: vid-structure
phase: all
last_updated: 2026-05-13
---

# Structure Conversation Examples

Worked dialogues for how vid-structure runs in real sessions. Examples-first contrastive: what landing the conversation right looks like, plus near-misses that show common failures.

## Example 1: Clean session, Short Process format

A creator with a tight brain-dump on a clean angle. Outline proposal lands first time, minor adjustment, locks.

**Setup state:**
- piece.md: `selected_angle: "Why posting daily is killing your channel, and the retention-first fix"`, `format: short-process`, `goal: sales`, `viewer_stage: warm`
- brain-dump: 10 lessons (see brain-dump-mining.md worked example), mined to 3 cores

**The conversation:**

> **AI:** "Outline proposal. Short-process, 4 steps (added one between cores 2 and 3 to bridge the algorithm mechanism to the fix).
>
> **Title's central question:** "What's the daily-posting trap and how do I escape it?"
> **Title-promise payoff:** Step 3 (the named retention-first fix, 60% through body, holds)
> **Active thread:** the algorithm's logic, opened in Step 1 ("frequency over quality"), deepened in Step 2, named in Step 3
> **Handoffs:** each step forward-hooks via "but here's what changes when..." pattern
>
> ## Step 1: Why posting daily backfires
> **Material:** brain-dump on frequency-vs-quality + Linus example
> **Blocks:** [[story-linus-retention]] (story), [[proof-retention-curve]] (proof)
> **Bullets:** open on Linus's pattern → name the algorithm mechanism → payoff: the algorithm rewards retention over volume
> **Handoff:** "...but there's a specific window where this all breaks down."
>
> ## Step 2: The 12-minute window
> **Material:** brain-dump on minute-12 retention drops, 8-video analysis
> **Blocks:** [[proof-12min-curve]], framework candidate: 'algorithm-sampling-window' (no bank match)
> **Bullets:** name the window → show the curve → payoff: why minute 12 specifically
> **Handoff:** "...so if posting daily is wrong AND the 12-min window is the test, what's the actual fix?"
>
> ## Step 3: The retention-first restructure (TITLE-PROMISE PAYOFF)
> **Material:** brain-dump on shorter-videos-one-payoff + the 22% jump
> **Blocks:** [[proof-22-percent-jump]], [[framework-one-big-payoff]] if exists, else inline craft
> **Bullets:** name the principle → walk the restructure → payoff: 22% personal proof
> **Handoff:** "...and once retention jumps, the algorithm starts pushing your videos to cold viewers."
>
> ## Step 4: What happens after retention fixes
> **Material:** brain-dump on the compounding effect (light material, flag)
> **Blocks:** [[proof-cold-viewer-jump]] if available
> **Bullets:** the compounding effect → the new ceiling → payoff: where this leads
> **Handoff:** to ending. Pivots to "the next problem after retention fixes."
>
> **CUTS logged:** stock-B-roll comment, $200 mic recommendation, 2019 quit-job backstory (lives in vid-intro as credibility).
>
> Lock outline, swap a step, merge/split, re-order, or scrap?"

> **Creator:** "Step 4 is light. Cut it and let the ending carry the 'what comes after retention' frame."

> **AI:** "Cutting Step 4. Now 3 body steps. Title-promise still in Step 3 (now 75% through body, still holds). Thread closes at Step 3. Locked?"

> **Creator:** "Locked."

> **AI:** "Outline locked. Writing script.md skeleton + updating piece.md."

[script.md written with 3 body sections, intro+ending stubbed, piece.md gets status: drafting, tension_plan, segment_purposes, segments_completed: [], last_updated.]

**Why this worked:** AI surfaced the full outline with material anchors, block candidates, tension role, AND handoffs in one shot. Creator made one structural decision (cut Step 4), AI re-checked tension graph still holds, locked. No NPC-ticking through phases.

## Example 2: Re-structure mode

A creator runs vid-structure on a piece that already has `segment_purposes`. Wants to refine, not rebuild.

> **Creator:** "/vid-structure on the retention-mistakes piece."

> **AI:** "Heads up: this piece is already structured (locked 2026-05-08). Existing outline:
> - Item 1: Thumbnail mistake
> - Item 2: Pacing mistake  
> - Item 3: Hook mistake
> - Item 4: Promise mistake
> - Item 5: Retention mistake (title-promise payoff)
>
> Re-structure from scratch, refine the existing outline, or cancel?"

> **Creator:** "Refine. Item 4 isn't landing in the brain-dump. I don't have material that actually fits."

> **AI:** "Pulling Item 4 material: brain-dump entry on viewer-betrayal patterns. Thin (2 short lines without specifics). Options:
> 1. Cut Item 4, re-route to 4 items with Item 5 becoming Item 4 (title-promise still holds at 75%, fine)
> 2. Merge Item 4's intent into Item 3 (the hook mistake; promise mismatch is a hook problem)
> 3. Pause to capture more material on viewer-betrayal via vid-intake
>
> Which?"

> **Creator:** "Merge with Item 3. The hook IS the promise."

> **AI:** "Merging. New outline:
> - Item 1: Thumbnail mistake
> - Item 2: Pacing mistake
> - Item 3: The hook-promise mistake (combined: hook is the contract, broken hook = broken trust)
> - Item 4: Retention mistake (was Item 5, now the title-promise payoff)
>
> Item 3's material now combines hook-gap brain-dump + viewer-betrayal patterns. Blocks: [[story-tom-startup]], [[metaphor-broken-contract]]. Tension: still climbs toward Item 4. Locked?"

> **Creator:** "Locked."

[piece.md segment_purposes updated, script.md merges Item 3 + 4, renumbers Item 5 → Item 4, comment logged for the merge decision so re-structure runs preserve it.]

**Why this worked:** AI surfaced the existing outline, accepted the creator's diagnosis without re-mining from scratch, proposed three concrete routes with tension-graph check, locked on the chosen one. No "let me start over from the brain-dump."

## Example 3: Narrative format (Case Study), outline shape differs

A case-study piece. The outline isn't N segments. It's a narrative arc.

**Setup state:**
- piece.md: `selected_angle: "How Steve went from $0 to $80k/mo in 9 weeks after his wife got pregnant"`, `format: case-study`, `goal: sales`, `viewer_stage: warm`
- brain-dump: Steve's story in full, plus the methodology Billy used

> **AI:** "Outline proposal. Case-study (narrative arc, not segmented).
>
> **Title's central question:** "How did Steve do it in 9 weeks?"
> **Title-promise payoff:** the Outcome moment (where $80k lands) at ~70% through body
> **Active thread:** Steve's transformation, opens in Setup with stakes, closes in Outcome
>
> ## Setup: Where Steve started
> **Material:** brain-dump on Steve's state (wife pregnant, lost job, runway gone, $0 MRR)
> **Blocks:** [[story-steve-week-zero]] (the stakes-laden open)
> **Bullets:** name the stakes → name the goal → name what was at stake if it didn't work
> **Role:** raises tension to maximum at the open (stakes drive emotional weight)
>
> ## Problem: Why nothing was working
> **Material:** brain-dump on the 3 things Steve tried that didn't move the needle
> **Blocks:** [[proof-failed-attempts]] if exists; otherwise narrate from brain-dump
> **Bullets:** the 3 dead-ends → why each failed → the moment of realizing he was stuck
> **Role:** deepens stakes. Viewer feels the trap.
>
> ## Action: What we actually did
> **Material:** brain-dump on the 4-week methodology rollout (week-by-week)
> **Blocks:** [[framework-9-week-arc]], [[proof-week-3-traction]]
> **Bullets:** the named system → the first week's pivot → the moment retention started climbing → the breakthrough week
> **Role:** rising action. Tension climbs toward Outcome.
>
> ## Outcome: $80k/mo (TITLE-PROMISE PAYOFF)
> **Material:** brain-dump on the final number + the week it landed
> **Blocks:** [[proof-80k-mrr-screenshot]], client video clip if available
> **Bullets:** name the number → name the timeframe → land the moment
> **Role:** the climax. The title's promise lands, full payoff.
>
> ## Lesson + Steps: What this proves and what you can do
> **Material:** brain-dump on the one big takeaway + 1-3 replicable steps
> **Blocks:** [[framework-9-week-arc]] (named again, this time as the takeaway)
> **Bullets:** the ONE big lesson → 1-3 specific steps for the viewer → tie to offer (sales goal)
> **Role:** falling action / application. Viewer converts from 'wow' to 'I could do this'.
>
> No body 'segments' in the listicle sense. This is one continuous narrative arc. Lock outline, sharpen a beat, or scrap?"

> **Creator:** "Lock. Move."

[script.md written with `## Setup`, `## Problem`, `## Action`, `## Outcome`, `## Lesson + Steps`: narrative beats, not segment numbers. piece.md segment_purposes lists the 5 beats; tension_plan names Outcome as title-promise location.]

**Why this worked:** AI used the format-native shape (narrative arc) instead of forcing 5 generic segments. The piece.md `segment_purposes` array still works; it's just labeled narratively.

## Example 4 (near-miss): Format-shape mismatch surfaced

A creator with 11 brain-dump lessons frames the piece as Case Study. Misalignment.

> **AI:** "Outline proposal. But flagging a structural mismatch first.
>
> Brain-dump has 11 distinct lessons. Format is case-study (narrative arc, one story, one transformation). Case Study works with ONE Problem-Action-Outcome story, not 11 lessons.
>
> Two routes:
> 1. **Re-frame to Deep Dive or Listicle.** Your 11 lessons map cleanly to a deep-dive (3-5 big ideas grouping the 11) or a listicle (each lesson its own item). Route back to vid-framing.
> 2. **Pick the ONE transformation story.** Which client/personal-result is the case study really about? The other 10 lessons either support that story or get cut.
>
> Which?"

> **Creator:** "Pick the one. The Steve story is the case study. The other lessons aren't case-study material."

> **AI:** "Pulling Steve story material. Tagging the other 10 lessons as either support-for-Steve or tangent (logged for future pieces). Proceeding with narrative arc outline..."

[Outline proposal continues with Case Study shape on the Steve story only.]

**Why this worked:** AI surfaced the mismatch BEFORE proposing an outline that would force-fit. Gave two concrete routes. Creator picked, work continued cleanly.

## Example 5 (near-miss): Early-payoff flagged

A creator wants the title's promise paid off in segment 2. AI flags the retention risk.

> **AI:** "Outline proposal (Listicle, 5 items)...
>
> [outline body...]
>
> ## Item 2: The retention-first fix (TITLE-PROMISE PAYOFF)
> **Material:** ..."

> **Wait, flag.** "I drafted this with the title-promise in Item 2 because your brain-dump leads with the fix. But that's early-payoff territory. Most viewers will get the named answer in 90 seconds and leave. Items 3-5 will lose 30-50% of the audience.
>
> Two routes:
> 1. **Push the named answer to Item 4.** Items 1-3 deliver pieces (context, mechanism, what doesn't work). Item 4 names the fix. Item 5 is the application/what-happens-after.
> 2. **Lock as-is.** You may have a reason for early payoff (e.g., this is for warm-hot audience already nodding along; the value is in the application layers).
>
> Which?"

> **Creator:** "Push to Item 4. I want this to retain."

> **AI:** "Restructuring..."

[New proposal with title-promise at Item 4. Material redistributed.]

**Why this worked:** AI didn't silently let the early-payoff outline ship. Surfaced the risk with the retention math, gave concrete routes, creator made the structural call.

## Anti-pattern: NPC ticking

> **AI:** "Phase 1.1 complete. Brain-dump mined. Moving to Phase 1.2."
> **AI:** "Phase 1.2 complete. Title's central question identified. Moving to Phase 1.3."
> **AI:** "Phase 1.3 complete. Format shape mapped. Moving to Phase 1.4."

Don't do this. The phases are for the SKILL's internal sequencing, not for the chat. The creator sees ONE outline proposal that contains all the mining work. Bulk-keep mode: if the creator confirms, lock. If they push back, surface what they want to adjust, re-propose. No tick-tock.

## Anti-pattern: abstract segment purposes

> **AI:** "## Segment 1: {opening hook}"
> **AI:** "## Segment 2: {first main point}"
> **AI:** "## Segment 3: {second main point}"

Don't do this. Segment purposes are MATERIAL-ANCHORED. Every header references actual brain-dump content. vid-segment can't write Segment 1 if the purpose is just "opening hook"; it needs to know WHICH lesson lands there.

## Anti-pattern: silent cuts

> **AI:** "Outline proposal: 5 items..." [proceeds without mentioning which brain-dump lessons got cut]

Don't do this. Always log cuts at the bottom of the proposal:

```
CUTS (logged for future pieces or audit):
- {brain-dump entry slug or short label}: {reason for cut}
```

The creator may know a cut entry is the actual gold.
