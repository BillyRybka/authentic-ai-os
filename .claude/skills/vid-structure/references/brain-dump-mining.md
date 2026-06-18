---
type: skill-reference
skill: vid-structure
phase: 1.1
last_updated: 2026-05-13
---

# Brain-Dump Mining

How to filter brain-dump material against the locked angle. The output of this filter is what determines which lessons survive as segments, which collapse into one, which provide support inside a segment, and which get cut.

This is not a separate review the creator sees. It's the silent reasoning the skill applies during outline proposal. The creator sees the result (mined outline), not the worksheet.

## The four tags

Every lesson, story, framework, proof, anecdote, or aside in the brain-dump gets one of four tags.

### Core

Directly serves the locked angle. The viewer needs this to get the `core_payoff` named in piece.md. If this lesson were missing, the central question raised by the title would not get answered.

**Test:** "Does this lesson move the viewer toward the core_payoff? Without it, does the script still deliver the title's promise?"

If yes-needed: tag `core`. This becomes either its own segment OR a load-bearing piece inside a segment.

### Support

Provides context, proof, parable material, or examples that strengthen a core lesson. By itself it doesn't serve the angle, but it amplifies a core lesson that does.

**Test:** "Does this material strengthen a core lesson without being a lesson of its own?"

Examples of support material:
- A client story that illustrates a core lesson's impact
- A stat that proves a core claim
- A metaphor that makes a core concept land faster
- A counterexample that sharpens what the core lesson is NOT
- Background context (history, why this matters) for a core concept

Tag `support` and note which core lesson it backs. vid-structure will surface support material as block candidates in the segment that hosts the parent core lesson.

### Combine

Overlaps significantly with another lesson. Either lesson alone is weaker than both merged. Tag as `combine-with-{other}` and treat as one segment.

**Test:** "If I taught these two lessons separately, would the viewer feel like they were getting the same point twice? Is one a more specific version of the other?"

Examples:
- "Don't post daily" and "post less for retention" → same lesson, combine
- "Hook in 5 seconds" and "open with a question" → first is the principle, second is a tactic; combine with the principle as headline
- "Use real numbers" and "specificity beats generality" → combine, more specific phrasing wins

When combining, pick the version with the sharper phrasing or the stronger brain-dump material. Discard the weaker version's framing but preserve any unique material it contained (stories, proofs) as support inside the combined segment.

### Tangent

Interesting but doesn't serve the angle. Belongs in a different video, an aside, or a future piece. Cuts at outline time.

**Test:** "Could this lesson stand on its own as a separate video on a different angle? Does it lead the viewer somewhere besides the core_payoff?"

Common tangents in brain-dumps:
- Adjacent topics the creator got fired up about while dumping
- Pet theories that don't connect to the specific angle
- Tooling/setup details when the angle is about strategy (or vice versa)
- The creator's own backstory beyond what credibility-weaving needs

**Cut discipline.** When you tag a lesson `tangent`, log it. The creator may want to save it for a different piece. Surface during outline proposal as:

```
CUTS (logged for future pieces):
- "scheduling tools deep-dive" (tangent; could be its own short-process video on workflow)
- "studio lighting basics" (tangent; wrong angle for this piece)
```

Never silently drop a cut. The creator may know the cut lesson is the real gold for this piece, and the angle is wrong.

## Mining sequence

Walk the brain-dump in the order it was written. For each block of material:

1. **Test against the angle.** Does this serve `core_payoff`? Tag `core`, `support`, `combine`, or `tangent`.
2. **Pull material anchors.** For `core` and `support` tags, note the specific phrasings, numbers, names, moments from the brain-dump that anchor this material. These become the "Material" lines in the outline proposal.
3. **Group support material by parent core.** Each piece of `support` gets attached to a core lesson. If support has no parent core, re-tag (often it's actually a `tangent` or a `core` you missed).
4. **Resolve combines.** Merge `combine-with-X` pairs into one core lesson with combined material.

## Worked example

**Brain-dump (abbreviated):**
1. "Most channels stall because they post too often"
2. "I lost 30% of my viewers in the 12-15 minute window, this happened to Linus too"
3. "Daily posting trains the algorithm to expect frequency over quality"
4. "My retention curve dropped at exactly minute 12 across 8 videos"
5. "Backstory: I quit my job in 2019, lost everything, came back to YouTube"
6. "Stop using stock B-roll, it kills authenticity"
7. "The 12-minute mark matters because that's where the algorithm samples"
8. "Once I cut my schedule from daily to weekly, retention jumped 22%"
9. "Best mic under $200 is the Shure MV7"
10. "The fix: shorter videos with one big payoff instead of three medium ones"

**Locked angle (piece.md):** "Why posting daily is killing your channel, and the retention-first fix that works."
**Core payoff:** "Cut your schedule, restructure for one big payoff, and your retention jumps 20%+."

**Mining output:**

| # | Material | Tag | Notes |
|---|---|---|---|
| 1 | "Most channels stall because they post too often" | `core` | The thesis statement; this is segment 1 |
| 2 | "Lost 30% in 12-15 min window, like Linus" | `support` for #1 | Story block candidate, parent = #1 |
| 3 | "Daily posting trains algorithm to expect frequency over quality" | `combine-with-1` | Same lesson, sharper phrasing → merge into #1 |
| 4 | "Retention curve dropped at minute 12 across 8 videos" | `support` for #7 | Proof block candidate, parent = #7 |
| 5 | "Backstory: quit job 2019" | `tangent` | Credibility material for vid-intro, not a body segment |
| 6 | "Stop using stock B-roll" | `tangent` | Different angle (production, not retention) |
| 7 | "12-minute mark matters because algorithm samples there" | `core` | The named mechanism; likely segment 3 (title-promise payoff territory) |
| 8 | "Cut daily → weekly, retention jumped 22%" | `support` for #10 | Personal proof, parent = #10 |
| 9 | "Best mic under $200" | `tangent` | Pure tangent, different angle entirely |
| 10 | "Fix: shorter videos with one big payoff" | `core` | The solution; segment 4 (post-payoff application) |

**Surviving cores:** #1 (thesis), #7 (mechanism), #10 (solution). 3 core lessons.

**Format = Short Process** would map to 3-5 steps. Three cores feels light. Surface the option to add a step ("would you say there's a step between 'why daily fails' and 'how the algorithm samples'?") OR lock at 3 steps and proceed.

**Format = Listicle** would feel forced; 3 items reads as a deep-dive in disguise. Surface re-frame suggestion.

**Format = Case Study** would route the cores into the narrative beats (problem → action → outcome → lesson).

**Cuts logged:** #5, #6, #9 (3 tangents surfaced to creator for future pieces).

## Tag-disagreement protocol

The creator may push back on a cut or a tag. When this happens:

- **"That's not a tangent, it's the actual lesson."** Re-mine. The angle may be wrong. Route back to vid-framing if multiple "tangents" are the real story.
- **"Those two should be separate segments, not combined."** Accept and split. Combining is a default; not a hard rule.
- **"You missed that this supports lesson X."** Re-tag. Note for future runs (the creator's mental model often reveals threads the brain-dump didn't explicitly mark).

## Anti-patterns

- **Mining without an angle.** Don't mine before piece.md framing is locked. The angle determines what's core vs tangent. Without it, everything is "interesting."
- **Cutting silently.** Always log cuts. Creator may know the cut is the gold.
- **Combining destructively.** When combining two lessons, preserve both stories/proofs/material. Discard only the redundant framing.
- **Forcing every core into a segment.** Some core material lives as load-bearing support inside another segment's principle. Not every core is segment-worthy.
- **Counting cores against format target.** If mining yields 3 cores and format wants 6 segments, don't pad with tangents to hit the count. Surface the gap. Either the brain-dump is thin (route back to vid-intake) or the format is wrong (route back to vid-framing).
