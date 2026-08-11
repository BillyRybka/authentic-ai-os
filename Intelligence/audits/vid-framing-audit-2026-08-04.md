# vid-framing audit, 2026-08-04

Target: `.claude/skills/vid-framing/` (the shipped skill, not the WIP rewrite at
`.claude/skills/skills-wip/vid-framing/`).

Routing: **repair, not rebuild.** The scar-tissue signal is present (two files
carry a note about the same past double-validation bug, and the git history shows
two prior full rewrites), but there is no record of the current file failing on
real creator work. `tests/skills/vid-framing/judge-scores.json` scores four
dimensions (`psychology_depth`, `angle_quality`, ...) that no longer exist in
`tests/skills/vid-framing/rubric.md`, which scores five different ones. Those
scores predate both the current rubric and the current file, so they are not
evidence about this skill. Every finding below is a hypothesis until a real run
tests it, except where a downstream skill already carries a workaround.

Worth knowing before you read further: the WIP rewrite at
`.claude/skills/skills-wip/vid-framing/SKILL.md` already answers findings 1, 3,
6 and 9 by deleting the sections they name. If that rewrite is where this is
headed, findings 2, 4, 5, 7 and 8 are the ones that still need doing there.

## Vitals

Judgement skill with a procedural tail (Lock and Save). 1,364 lines across
SKILL.md and everything it loads: SKILL.md 352, `finding-the-core.md` 191,
`patterns.md` 353, `examples.md` 221, `format-index.md` 42,
`piece-additions.md` 83, `knowledge/piece-contract.md` 122. 46 hard constraints
live at the generation moment from SKILL.md alone, 55 once `patterns.md` and
`examples.md` are open at Step 3. Five skill-owned reference files, zero loaded
unconditionally.

## Findings

### 1. Rule budget (check 4)

**Verdict.** Fail, 46 constraints live at one moment in SKILL.md, 55 with the
Step 3 references open.

**Evidence.** Counted at Step 3 to Step 6, which is one moment because the batch
is written and validated before anything is shown. Global: "Never Invent" (39),
"Never repeat a reference file's teaching inside the output" (45), "Read nothing
outside it" (347), "No target number" and "Say how many survived, in a clause"
(20). Step 3: 11 more (82, 84-90, 92, 94, 96-103, 105-112, 114 three times, 116,
118-124, 126). Step 4 and 5: 4 more (132-139, 141, 149, 162). Step 6: 12 more
(the 9 validation criteria, plus 204, 206, 208). Channel Positioning: 4 bullets
(214-217). Anti-Formulaic Guard: 7 bullets (221-227). Output Format: 6 required
fields plus the recommendation block (231-262). `patterns.md` adds 9 more once
open (line 7, Blending Rules 1-6, 326, 328).

Three of those clusters are one rule wearing many hats. The Anti-Formulaic Guard
(7 bullets), validation criterion 8 "Distinctiveness", Step 3's "Good batch
variety may include" list, and line 116 "Each option must change the substance of
the video, not just the wording" all enforce the same thing. The sentence that
replaces them is already written, in `examples.md` line 138: "The tell: read the
Must Deliver for each. If they are the same sentence, you wrote one option four
times."

**Fix.** Four edits.

Replace lines 18-35 ("## What This Creates" through "ready for `vid-title`")
with:

```
## What This Creates

As many genuinely different framing options as the material supports, then one
locked Frame, Core Payoff, format, and goal on disk for `vid-title`. No target
number: a count makes you pad to reach it, and three real angles beat five where
two are filler. Say how many survived, in a clause.
```

Replace lines 92-114 (from "**Write it in plain language.**" through "one a
creator could picture filming.") with:

```
**Write it in plain language.** A frame should sound like a creator clearly
explaining the video they want to make, not a strategist writing a report. Keep
it to 1-2 sentences, keep the answer withheld, and keep the setup concrete
enough to picture. The list above is what the frame has to make clear, not five
clauses to cram into one sentence. Never write it as a headline: that is
`vid-title`'s job and a title here gets rejected downstream. No internal brand
language unless the audience already understands it.
`references/examples.md` shows three stiff frames next to their fixed versions.
```

Replace line 116 with:

```
Each option must change the substance of the video, not just the wording. The
test is Must Deliver: read the Must Deliver line for every option in the batch,
and if two are the same sentence, you wrote one option twice.
```

Delete lines 210-227 entirely (the "## Channel Positioning" and "##
Anti-Formulaic Guard" sections). Channel positioning survives as validation
criterion 2 below; the brand-language rule moved into the plain-language block
above.

Replace lines 164-208 ("### 6. Validate" through "Do not display scores unless
requested.") with:

```
### 6. Validate

Steps 2 to 5 already enforced the audience read, the payoff, and the
deliverable. Four things they did not check. Run these once, here, before
presenting.

1. **Credibility.** Can the creator support this from the brain dump?
2. **Channel fit.** Does it sit inside a pillar and support the transformation
   the Iceberg statement promises? Read `foundation/iceberg.md`.
3. **Distinctiveness.** Do any two options share a Must Deliver line?
4. **Frame accuracy.** Does the Frame describe the video that would actually get
   made?

Revise or remove any option that fails. This is the only validation pass. Do not
display scores unless requested.
```

That takes 46 to roughly 20. It does not reach five, and a skill of this ambition
will not: the point is that 26 of the 46 were re-asking questions an earlier step
already answered.

### 2. Placement (check 1)

**Verdict.** Fail.

**Evidence.** The rule "`frame` is never a headline" exists twice in this skill's
context and both copies arrive after the frames are written.
`assets/piece-additions.md` line 17: "Never a spoken line, never a headline,
never a description of the contents." `knowledge/piece-contract.md` line 23: the
same. Both files are read at Lock and Save. The frames are written at Step 3
(SKILL.md lines 78-126), which never states the rule; the closest it gets is the
"Prefer clear language such as: A video about..." list at 105-112.

The downstream skill already carries a workaround for this.
`.claude/skills/vid-title/SKILL.md` line 14: "The frame arrives as a description
of the video, never as a headline, so it competes with nothing you write; if it
reads like a title, framing broke its own rule and the wording is still yours to
beat." A downstream skill writing a contingency for an upstream skill breaking
its own rule is the cheapest evidence available that it happens.

**Fix.** The replacement block in finding 1 for lines 92-114 already contains the
sentence: "Never write it as a headline: that is `vid-title`'s job and a title
here gets rejected downstream." Landing that one edit closes this finding.

### 3. Examples restate rather than demonstrate (check 14)

**Verdict.** Fail, 2 of 6 output fields.

**Evidence.** SKILL.md lines 242-246 require two fields per option:

> **Psychological Hook:**
> [The audience belief, pain point, fear, desire, or internal tension being targeted.]
>
> **Why They Will Stop Scrolling:**
> [Why this specific viewer needs this video now.]

Line 82 fixes the context across the whole batch: "Hold the approved context
still. Every option below is a different video made from the same context, not a
different context." The audience tension is the approved context, so
"Psychological Hook" is the same sentence on every option in the batch by
construction. "Why They Will Stop Scrolling" restates the Core Payoff and the
same tension a third time.

Neither field is saved. `assets/piece-additions.md` writes `frame` and
`core_payoff` only, and `knowledge/piece-contract.md` line 70 lists vid-framing's
writes as `frame`, `core_payoff`, `format`, `voice_context`, `goal`, plus the
body section. And `references/examples.md`, which line 5 calls "the standard,"
does not show either field on any of its seven worked options: Batch 1 Option A
(lines 56-69) shows Frame, Core Payoff, Framing DNA, Must Deliver, and stops.
The file that defines what good looks like disagrees with the file that defines
the required shape.

**Fix.** Replace lines 231-249 with:

```
### Option [Number]: [Short Working Label]

**Frame:**  
[One concise paragraph describing the video direction.]

**Core Payoff:**  
[The answer, result, realization, verdict, or transformation delivered by the end.]

**Framing DNA:**  
[Primary pattern] + [Supporting pattern] + [Optional supporting pattern]

**Must Deliver:**  
[What the video must prove, reveal, or demonstrate.]
```

That is exactly the shape every option in `examples.md` already demonstrates.

### 4. Contradiction (check 5)

**Verdict.** Fail.

**Evidence.** SKILL.md line 82: "Hold the approved context still. Every option
below is a different video made from the same context, not a different context."

`references/examples.md` lines 199-201, read at the same step: "Batches 1 and 2
hold the context still and vary the video. The other axis holds the raw idea
still and varies who it is for. Both matter." It then spends 15 lines
demonstrating that second axis with two frames aimed at two different audiences
(lines 203-215).

The instruction says one axis. The standard says two and shows the second one
worked. This resolves arbitrarily.

**Fix.** Delete `references/examples.md` lines 199-217 (from "# The second axis:
same idea, different audience" through "one video retitled."). If the material is
worth keeping, its correct home is `references/finding-the-core.md`, which is
read at Step 2 while the audience is still open, not at Step 3 after it is
approved and fixed.

### 5. Near-miss context (check 12)

**Verdict.** Fail.

**Evidence.** Two taxonomies in this skill's context are both called format, and
one term appears in both meaning different things.

`references/patterns.md` line 206: "# Video Format Patterns", containing System
or Framework, Comparison, Review or Ranking, Expert Breakdown. Line 155: "##
Case Study", a proof pattern.

`references/format-index.md` line 12: the seven values of the `format` field,
including `case-study` (line 15), which becomes `format: case-study` in
frontmatter and selects `knowledge/format-planners/case-study.md` for
vid-structure.

A frame labelled "Framing DNA: Case Study + Specific Result" at Step 3 is one
run away from `format: case-study` being locked by association at Lock and Save
rather than by the rule at `format-index.md` line 24. That is a wrong planner
handed to vid-structure, which is expensive and silent.

**Fix.** In `references/patterns.md`, replace line 206 and the line under it
with:

```
# Delivery Patterns

These patterns shape how the idea is organized and delivered inside the video.
They are not the `format` field. That is one of the seven video formats in
`references/format-index.md`, set at Lock and Save, and nothing on this page
decides it.
```

And insert after line 157 ("Uses a real person, channel, project, or result as
evidence."):

```
Not the same thing as `format: case-study`. This is a proof pattern used inside
a frame; the format field is set separately at Lock and Save.
```

### 6. Contradiction (check 5)

**Verdict.** Fail.

**Evidence.** The description (line 3): "writes 3-5 genuinely different framings
of the same idea each with a Core Payoff."

SKILL.md line 20: "No target number: a count makes you pad to reach it, and three
real angles beat five where two are filler."

`tests/skills/vid-framing/rubric.md` line 60 agrees with the body, not the
description: "The count is not scored." The description is the only place a
number appears, and it is the first thing loaded.

**Fix.** In line 3, replace "writes 3-5 genuinely different framings of the same
idea each with a Core Payoff" with "writes as many genuinely different framings
of the same idea as the material supports, each with a Core Payoff".

### 7. Negative coverage (check 3)

**Verdict.** Fail.

**Evidence.** The description (line 3) has no "not for" clause. SKILL.md line 10
has a good one, but that is body text, not what the router reads:

> **Scope: the angle, never the words.** It does not capture raw material
> (`vid-intake`), pick the topic (`vid-ideas`), write the title (`vid-title`) or
> thumbnail (`vid-thumbnail`), build the outline (`vid-structure`), or draft a
> line of script.

The named confusions are real and adjacent by trigger phrase: `vid-ideas`
("what should I make"), `vid-intake` ("I want to make a video about X"), and
`vid-title`. The key use case, "Use whenever a piece needs its direction
decided", currently lands at character 324 of 748, behind a summary of what the
skill contains.

**Fix.** Replace line 3's description with:

```
description: Use whenever a piece needs its direction decided, including when the creator never says the word "frame". Turns a video idea into a decided video: reads the brain dump and the creator foundation, writes as many genuinely different framings of the same idea as the material supports, each with a Core Payoff, and recommends one. Once the creator picks, writes the read, sets the format and the goal, and saves it all to piece.md before handing to vid-title. Triggers include "frame this video", "pick the angle", "what should this video be about", "what's the angle here", "what part of this do people actually care about", "re-frame this piece", "I don't know how to position this one", and any point where a creator has an idea but has not decided why anyone would watch it. Not for capturing raw material (vid-intake), not for choosing which video to make next (vid-ideas), and not for writing the title or thumbnail (vid-title, vid-thumbnail): this decides the angle and stops.
```

Separate, and not a fix to this file: in your own environment there is a second
installed skill named `content-creation-studio:video-framing`, described as
"Transform video ideas into must-watch concepts by finding unique angles. Use
when brainstorming video angles, positioning content, or finding the
psychological hook for a video idea." That collides with this skill on almost
every trigger phrase. Adding a negative naming it would be wrong in the shipped
description, since creators will not have that plugin. Resolve it on your machine
by retiring or renaming that skill.

### 8. Contradiction (check 5)

**Verdict.** Fail.

**Evidence.** SKILL.md line 347: "This table is exhaustive for reading. Read
nothing outside it."

SKILL.md line 305: "Read `assets/piece-additions.md` for the exact shape, then
write to `content/pieces/{slug}/piece.md`." Line 328 names it again.
`assets/piece-additions.md` is not in the table at lines 336-345.

The skill instructs a read that its own exhaustive list forbids.

**Fix.** Insert into the table at line 344, above the `piece-contract.md` row:

```
| Exact piece.md shape, when saving | `assets/piece-additions.md` | Lock and Save |
```

### 9. The include test (check 8)

**Verdict.** Fail.

**Evidence.** Lines 18-35 ("## What This Creates") list the six per-option fields
with a one-line gloss each. Lines 229-249 ("## Output Format") specify the same
six fields with the instruction text that actually governs. The first copy
changes no action; it is a preview of the second. Lines 31-33 are rationale on
their own:

> The Core Payoff rewards the viewer for staying.
>
> The Frame determines the video.

With finding 3 applied, the duplication also becomes a drift risk: the field list
would have to be cut in two places or the two copies disagree.

**Fix.** The replacement for lines 18-35 in finding 1 deletes this. No separate
edit.

## Passes

Check 2 (description is a trigger in third person, 748 characters, under the
1,536 truncation, though see finding 7 on ordering). Check 6 (one instance,
"REALLY" in caps at line 62; not worth an edit). Check 9 (nothing stated that the
model would read off the filesystem). Check 10 (every reference has a named step
trigger, nothing loads unconditionally; the table gap is finding 8, not a
trigger gap). Check 11 (`format-index.md` line 30 dates its scores to
2026-07-28). Check 15 (no section named gotchas, but "When a Batch Is Rejected"
at lines 264-280 holds nine real failure causes and "Never Invent" at 37-41 is a
real one; a missing heading is not a finding when the content exists). Check 16
(no absolute rule here has a cost a hook could enforce that a sentence cannot).

Check 13 fails by the letter: this is a judgement skill and it opens 574 lines of
examples and patterns at the generation moment, which is exactly where a
judgement skill's search space should be widest. No fix proposed, because the
honest test is deletion rather than a rewrite. See candidates 1 and 2.

## Deletion candidates

**1. `references/patterns.md` entirely (353 lines, loaded at Step 3).**
Prediction: batch variety holds, because Step 3's five variety categories and the
Must Deliver test carry it, and a frontier model already knows this taxonomy.
What changes is the Framing DNA labels, which get vaguer or stop appearing, and
Framing DNA is not saved to piece.md by anything. How you tell: run one real
brain dump twice, with the file and without, and compare whether the options
still differ in genre and in Must Deliver. If the batch collapses to two genres
without it, put it back. This is the largest single file the skill opens at its
highest-pressure moment, which is why it is first.

**2. `references/examples.md` lines 142-217 (Batch 2 and the second axis).**
Prediction: nothing changes. Batch 1 already demonstrates the shape, the
four-videos-not-one argument, and the fake-batch contrast; Batch 2 teaches the
same lesson in a different world, and the second axis contradicts Step 3
(finding 4). How you tell: check whether the batch still produces options with
genuinely different production requirements. If Batch 1 alone makes every option
story-led, Batch 2 was doing work and only the second axis should go.

**3. Step 6 "Validate" entirely (lines 164-208), rather than the trim in finding
1.** Prediction: credibility and channel fit slip first, because those are the
only two of the nine criteria that nothing upstream checks. The other seven
re-ask what Steps 2 to 5 already enforced. How you tell: an option appears that
the brain dump cannot support, or one drifts outside the pillars. If neither
happens across three real pieces, the whole 45 lines were re-asking answered
questions and the trim in finding 1 is too conservative.

## Verification note

The findings above are ordered by what they cost. Nine survived the verification
pass; two did not and were cut (a "gotchas section is missing" finding, because
the content exists under a different heading, and a "patterns.md restates
training knowledge" finding, because the Must Deliver lines and the selection
table are genuinely non-obvious and the honest test is deletion, not argument).

No behavioral verification was run. There is no real failing input on record for
this version of the file: the eval outputs in `tests/skills/vid-framing/` were
produced by an earlier skill against an earlier rubric. Finding 2 is the only one
with independent evidence behind it, and that evidence is a workaround written
into `vid-title`, not a captured failure. Test the rest on real work.
