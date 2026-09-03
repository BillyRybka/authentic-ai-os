---
type: skill-reference
skill: vid-structure
step: 1
---

# Brain-Dump Mining

How to filter brain-dump material against the locked frame when roughing the spine. The result decides which lessons become main points, which become subpoints under a point, which merge, and which get cut.

This is silent reasoning, not a review the creator sees. They see the rough spine (main points and subpoints, plus the cuts), never the worksheet.

## The four tags

Every lesson, story, proof, or aside in the brain-dump gets one tag.

### Main point

Serves the locked frame on its own. The viewer needs it to reach the `core_payoff`. If it were missing, the video would not deliver the title's promise. Becomes its own body section.

**Test:** "Does this move the viewer toward the payoff? Without it, does the video still deliver the title's promise?" Yes-needed means main point.

Where piece.md carries framing's `## The Read`, its **Transformation** is the sharper version of the same test: the field names the from and the to, so a main point is anything the viewer needs in order to make that move. Material that fits the topic but does not move them along that line is a subpoint or a tangent, however good it is.

### Subpoint

Backs a main point without being a point of its own. It strengthens something that already serves the frame.

**Test:** "Does this strengthen a main point without standing alone?"

Examples: a client story that shows a main point's impact, a stat that proves a claim, a metaphor that makes a concept land, a counterexample that sharpens what the point is not, background context for a concept.

Tag it a subpoint and note which main point it sits under. It shows up in the spine as a line under that point.

### Combine

Overlaps another lesson enough that both are weaker apart than merged.

**Test:** "Taught separately, would the viewer feel they got the same point twice? Is one a sharper version of the other?"

Examples: "don't post daily" and "post less for retention" are the same point, combine. "Hook in 5 seconds" and "open with a question" are a principle plus a tactic, combine under the principle. When merging, keep the sharper phrasing and preserve any unique material (a story, a proof) as a subpoint of the combined point.

### Tangent

Interesting but does not serve this angle. Belongs in a different video. Cut at outline time.

**Test:** "Could this stand as its own video on a different angle? Does it lead the viewer somewhere other than the payoff?"

Common tangents: adjacent topics the creator got fired up about mid-dump, pet theories that don't connect, tooling or setup detail when the frame is strategy, backstory beyond what the intro needs.

**Cut discipline.** Log every tangent, never drop it silent. The creator may know a cut is the real gold, which means the frame is wrong. Surface cuts in the spine like this:

```
CUTS (logged for future pieces):
- "scheduling tools deep-dive" (tangent, could be its own step-by-step video)
- "studio lighting basics" (tangent, wrong angle for this piece)
```

## Mining sequence

Walk the brain-dump in the order it was written. For each block:

1. **Test against the frame.** Main point, subpoint, combine, or tangent.
2. **Pull the material anchor.** For main points and subpoints, note the specific phrasings, numbers, names, and moments from the dump. These become the spine's lines.
3. **Attach subpoints to their main point.** A subpoint with no parent is usually a tangent or a main point you missed.
4. **Resolve combines.** Merge the pair into one main point with the sharper phrasing.

## Worked example

**Brain-dump (abbreviated):**
1. "Most channels stall because they post too often"
2. "Lost 30% of viewers in the 12-15 minute window, this happened to Linus too"
3. "Daily posting trains the algorithm to expect frequency over quality"
4. "My retention curve dropped at exactly minute 12 across 8 videos"
5. "Backstory: I quit my job in 2019, lost everything, came back to YouTube"
6. "Stop using stock B-roll, it kills authenticity"
7. "The 12-minute mark matters because that's where the algorithm samples"
8. "Once I cut daily to weekly, retention jumped 22%"
9. "Best mic under $200 is the Shure MV7"
10. "The fix: shorter videos with one big payoff instead of three medium ones"

**Locked frame:** "Why posting daily is killing your channel, and the retention-first fix."
**Core payoff:** "Cut your schedule, restructure for one big payoff, retention jumps 20%+."

| # | Material | Tag | Notes |
|---|---|---|---|
| 1 | "channels stall because they post too often" | main point | the thesis |
| 2 | "lost 30% in the 12-15 min window, like Linus" | subpoint of #1 | story anchor |
| 3 | "daily posting trains the algorithm for frequency" | combine with #1 | sharper phrasing, merge |
| 4 | "retention dropped at minute 12 across 8 videos" | subpoint of #7 | proof anchor |
| 5 | "quit my job in 2019" | tangent | credibility for the intro, not a body point |
| 6 | "stop using stock B-roll" | tangent | different angle (production) |
| 7 | "minute 12 matters, the algorithm samples there" | main point | the mechanism |
| 8 | "cut daily to weekly, retention jumped 22%" | subpoint of #10 | personal proof |
| 9 | "best mic under $200" | tangent | different angle entirely |
| 10 | "shorter videos, one big payoff" | main point | the solution |

**Surviving main points:** #1 (thesis), #7 (mechanism), #10 (solution). Three main points.
**Cuts logged:** #5, #6, #9.

If the format is step-by-step, three points maps to three lean steps. If it wants more, surface the gap (add a step, or the dump is thin, route to vid-braindump), do not pad with tangents to hit a count.

## Tag-disagreement protocol

The creator may push back on a cut or a tag.

- **"That's not a tangent, it's the actual lesson."** Re-mine. The angle may be wrong. If several "tangents" are the real story, route back to vid-framing.
- **"Those two should be separate points, not combined."** Accept and split. Combining is a default, not a rule.
- **"You missed that this supports point X."** Re-tag. The creator's mental model often reveals a connection the dump didn't spell out.

## Anti-patterns

- **Mining without a frame.** Don't mine before framing is locked. Without the frame, everything looks interesting.
- **Cutting silently.** Always log cuts. The creator may know the cut is the gold.
- **Combining destructively.** Keep both stories and proofs when merging, discard only the redundant framing.
- **Forcing every main point into its own section.** Some serving material lives as a subpoint inside another point, not as a section of its own.
- **Counting points against a format target.** If mining yields three and the format wants six, surface the gap. Either the dump is thin (vid-braindump) or the format is wrong (vid-framing). Never pad.
