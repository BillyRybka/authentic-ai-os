# vid-framing audit, 2026-08-04 (b)

Target: `.claude/skills/vid-framing/` at working-tree state (SKILL.md is modified and
uncommitted).

This is a re-audit. The first pass today (`vid-framing-audit-2026-08-04.md`) has no
Decisions section filled in, so nothing is on record as rejected and nothing below is
blocked from being re-proposed. Six of its nine findings are still live against the
same quoted evidence and are marked **repeat** where they are. What did land since
that report: the `3-5` count came out of the description, the Anti-Formulaic Guard and
Channel Positioning sections are gone, Step 6 went from nine validation criteria to
five, and the rationale lines under What This Creates are cut. SKILL.md is 352 lines
down to 260.

Routing: **repair, not rebuild.** Finding 1 is a ship blocker, not a design failure,
and it has a two-line fix. There is still no record of the current file failing on real
creator work, so every finding below except 1 and 3 is a hypothesis until a real run
tests it.

## Vitals

Judgement skill with a procedural tail (Lock and Save); the tail is a genuine split
candidate and the question is at the end of this report. 1,271 lines across SKILL.md
and everything it loads: SKILL.md 260, `finding-the-core.md` 191, `patterns.md` 353,
`examples.md` 221, `format-index.md` 42, `piece-additions.md` 83,
`knowledge/piece-contract.md` 121. 70 hard constraints total, 50 live at the generation
moment (Steps 2 to 6 plus the globals, with `patterns.md` and `examples.md` open). Six
reference files, zero loaded unconditionally, every one with a named step trigger.
Nothing loads three references deep: `format-index.md` names
`knowledge/format-planners/{format}.md` but hands that read to vid-structure.

## Findings

### 1. vid-framing hard-stops on two files nothing writes (check 11, and the broken-flow gotcha)

**Verdict.** Fail.

**Evidence.** SKILL.md line 12:

> No `content/pieces/{slug}/brain-dump.md`, point them at `vid-intake` and stop. No
> `foundation/avatar.md` or `foundation/iceberg.md`, point them at `/foundation` and
> stop.

Nothing writes those two files. The `/foundation` chain writes one file.
`skills/vid-positioning/SKILL.md` line 18 in the installed plugin: "**Outputs:**
Iceberg Statement section written to `foundation/creator-foundation.md`."
`skills/vid-avatar/SKILL.md` line 22: "**Outputs:** Offer, Avatar, and Top 3 perceived
problems sections written to `foundation/creator-foundation.md`." `commands/foundation.md`
line 31 checks that same single file for its seven sections. Checked against both
`plugins/marketplaces/peak-systems/plugins/authentic-ai-os/` and the installed
`plugins/cache/peak-systems/authentic-ai-os/0.2.1/`; they agree.

Grep across this repo for anything that writes `foundation/avatar.md` or
`foundation/iceberg.md` returns two consumers and no writer: this skill and
`vid-pipeline/SKILL.md` line 58, which carries the same hard check. Every other skill in
the fleet still reads `creator-foundation.md` (vid-intake line 12, vid-ideas line 30,
vid-title line 22, vid-intro line 16, vid-ending line 20, vid-pressure-test line 28,
vid-voice-capture line 40, post-write line 33).

The split was deliberate and premature. Commit 69e7a94: "New skill reads
foundation/avatar.md and foundation/iceberg.md (creator-foundation.md is now split into
iceberg/avatar/credibility/backstory/offer)." The parenthetical describes a migration
that was never made.

The observable: a creator with a fully completed foundation runs vid-framing, gets told
to run `/foundation`, runs it, comes back, and gets told to run `/foundation` again.
The skill cannot start. Same on vid-pipeline, one step earlier. If your own vault has
hand-made `avatar.md` and `iceberg.md`, the loop is invisible to you and fires for
every other creator.

`knowledge/piece-contract.md` line 121 is the other half of the same drift, and it is
read by this skill at Lock and Save: "**`foundation/creator-foundation.md` missing**:
hard stop. Tell the creator to run `/foundation` first." That fires the mirror-image
stop, at the save step, in a vault where the split *has* happened.

**Fix.** Two edits, and they hold whichever way the migration lands.

In SKILL.md, replace:

```
No `content/pieces/{slug}/brain-dump.md`, point them at `vid-intake` and stop. No `foundation/avatar.md` or `foundation/iceberg.md`, point them at `/foundation` and stop.
```

with:

```
No `content/pieces/{slug}/brain-dump.md`, point them at `vid-intake` and stop. No avatar and no Iceberg statement, point them at `/foundation` and stop. Both live in `foundation/creator-foundation.md`; a split vault carries them as `foundation/avatar.md` and `foundation/iceberg.md`. Read whichever exists.
```

Then apply the same substitution at the two read points. SKILL.md line 43, replace
"Read `foundation/avatar.md` when using the default audience." with "Read the avatar
when using the default audience." SKILL.md line 137, replace "Read
`foundation/iceberg.md`." with "Read the Iceberg statement." The two reference-table
rows at lines 252 to 253 get the same treatment:

```
| Default audience | avatar and Top 3 perceived problems, in `foundation/creator-foundation.md` or `foundation/avatar.md` | Step 1 |
| Channel positioning | Iceberg statement, machinery, content notes, 8 pillars, in `foundation/creator-foundation.md` or `foundation/iceberg.md` | Step 6 |
```

In `knowledge/piece-contract.md`, replace:

```
- **`foundation/creator-foundation.md` missing**: hard stop. Tell the creator to run `/foundation` first.
```

with:

```
- **Foundation missing**: hard stop. Tell the creator to run `/foundation` first. It writes `foundation/creator-foundation.md`; a split vault carries the same sections as separate files under `foundation/`. A skill needs whichever one holds the section it reads.
```

Not a fix to this file, and the reason this is a re-audit finding rather than a fleet
one: `vid-pipeline/SKILL.md` line 58 carries the identical check and needs the identical
edit, or the pipeline blocks one step before vid-framing ever runs.

### 2. Two output fields nothing reads, and they are specified twice (checks 8 and 14) [repeat of 2026-08-04 finding 3]

**Verdict.** Fail, 2 of 6 fields.

**Evidence.** SKILL.md lines 167 to 171 require them on every option:

> **Psychological Hook:**
> [The audience belief, pain point, fear, desire, or internal tension being targeted.]
>
> **Why They Will Stop Scrolling:**
> [Why this specific viewer needs this video now.]

SKILL.md line 74 fixes the audience tension across the whole batch: "Hold the approved
context still. Every option below is a different video made from the same context, not
a different context." The audience tension is the approved context, so Psychological
Hook is the same sentence on every option by construction. Why They Will Stop Scrolling
restates the Core Payoff against that same tension a third time.

Neither field survives the session. `knowledge/piece-contract.md` line 70 lists
vid-framing's writes as `frame`, `core_payoff`, `format`, `voice_context`, `goal`, plus
the `## The Read` body section. `assets/piece-additions.md` writes the same set.

And `references/examples.md`, which line 5 calls "the standard," shows neither field on
any of its seven worked options. Batch 1 Option A (lines 56 to 69) gives Frame, Core
Payoff, Framing DNA, Must Deliver, and stops. The file that defines what good looks like
disagrees with the file that defines the required shape, at the same step, in the same
context window.

The six fields are also listed twice: lines 20 to 27 under What This Creates with a
one-line gloss each, and lines 156 to 174 under Output Format with the fill-in text that
actually governs. The first copy changes no action the second does not already govern,
and it sits in the placement budget at the top of the file.

**Fix.** Two deletions.

Delete from What This Creates:

```
Each option includes:

- **Frame:** The specific direction the video will take for this audience
- **Core Payoff:** What the viewer receives by staying to the end
- **Framing DNA:** The patterns used
- **Psychological Hook:** The audience tension being targeted
- **Why They Will Stop Scrolling:** Why this viewer needs this video now
- **Must Deliver:** What the video must prove or reveal
```

In Output Format, replace:

```
**Framing DNA:**  
[Primary pattern] + [Supporting pattern] + [Optional supporting pattern]

**Psychological Hook:**  
[The audience belief, pain point, fear, desire, or internal tension being targeted.]

**Why They Will Stop Scrolling:**  
[Why this specific viewer needs this video now.]

**Must Deliver:**  
[What the video must prove, reveal, or demonstrate.]
```

with:

```
**Framing DNA:**  
[Primary pattern] + [Supporting pattern] + [Optional supporting pattern]

**Must Deliver:**  
[What the video must prove, reveal, or demonstrate.]
```

That is the shape all seven options in `examples.md` already demonstrate.

### 3. "Never a headline" still arrives after the frames are written (check 1) [repeat of 2026-08-04 finding 2]

**Verdict.** Fail.

**Evidence.** The rule exists twice in this skill's context and both copies load at Lock
and Save. `assets/piece-additions.md` line 17: "Never a spoken line, never a headline,
never a description of the contents." `knowledge/piece-contract.md` line 23: the same
sentence.

The frames are written at Step 3, SKILL.md lines 72 to 92, which never states it. The
closest it comes is line 86: "A frame should sound like a creator clearly explaining the
video they want to make, not a strategist writing a report."

The downstream skill carries a workaround for this. `.claude/skills/vid-title/SKILL.md`
line 14: "The frame arrives as a description of the video, never as a headline, so it
competes with nothing you write; if it reads like a title, framing broke its own rule
and the wording is still yours to beat." A downstream skill writing a contingency for an
upstream skill breaking its own rule is the cheapest evidence available that it happens.

`assets/piece-additions.md` line 55 confirms it from the other side: "their working
labels are title shaped."

**Fix.** In Step 3, replace:

```
A frame should sound like a creator clearly explaining the video they want to make, not a strategist writing a report. Keep it to 1-2 sentences. The list above is what the frame has to make clear, not five clauses to cram into one sentence.
```

with:

```
A frame should sound like a creator clearly explaining the video they want to make, not a strategist writing a report. Never a headline. `vid-title` writes those. Keep it to 1-2 sentences. The list above is what the frame has to make clear, not five clauses to cram into one sentence.
```

### 4. Rule budget (check 4)

**Verdict.** Fail, 70 constraints, 50 live at the generation moment.

**Evidence.** Counting rule: one per bulleted or numbered instruction, one per
independent imperative sentence, and menus that feed a single decision count once (the
six internal questions at Step 2, the five gap types, the six Core Payoff shapes, the six
Must Deliver examples). The prior audit used a coarser rule and reported 46, so the two
numbers are not comparable and 70 is not a regression.

By section: Before You Start 3, What This Creates 3, Never Invent 3, the read-timing line
at 37 is 1, Step 1 is 2, Step 2 is 4, Step 3 is 10, Step 4 is 2, Step 5 is 2, Step 6 is 8,
the two difference tests are 3, Output Format 3, When a Batch Is Rejected 3, Lock and Save
22, the reference-table rule at 258 is 1. `patterns.md` adds 9 once open (line 7, Blending
Rules 1 to 6, lines 326 and 328) and `examples.md` adds 1 (line 221).

Six of the 70 are a rule stated twice inside the same moment's context. The pre-save list
at lines 233 to 241 is read alongside `assets/piece-additions.md`, which line 225 opens at
that exact step:

- "Target is a causal chain, not a profile. If "their goal is" or "their pain point is"
  appears, rewrite it." is `piece-additions.md` line 42: "No "their goal is / their
  challenge is" scaffold."
- "Transformation reaches the same ending as `core_payoff`." is `piece-additions.md`
  line 44: "Names the same ending as core_payoff."
- "Every claim, number, and duration traces to the brain dump, the foundation, or
  something the creator said in this session. Every gap is a `> [!todo]`." is
  `piece-additions.md` line 78 and lines 59 to 63, and SKILL.md line 31 already said it
  globally.
- "`format` is one of the seven and `goal` is set." is SKILL.md line 219 ("Lock one of
  the seven") and `format-index.md` line 26.

Two of the five validation criteria do the same thing across steps. Step 6 criterion 2,
"**Payoff.** Is the end result specific, worth staying for, and something the viewer
cannot get without watching?" re-asks all of Step 4, which already gives the vague/specific
contrast at lines 107 to 113. Step 6 criterion 3, "**Credibility.** Can the creator
support every claim in it from the brain dump?" re-asks Step 5 line 128, "Reject any frame
the creator cannot honestly support," and Never Invent at line 31.

**Fix.** Delete these four bullets from the pre-save list:

```
- Target is a causal chain, not a profile. If "their goal is" or "their pain point is" appears, rewrite it.
- Transformation reaches the same ending as `core_payoff`.
- Every claim, number, and duration traces to the brain dump, the foundation, or something the creator said in this session. Every gap is a `> [!todo]`.
- `format` is one of the seven and `goal` is set.
```

The three that survive are the ones nothing else states: the word-for-word check, the
would-actually-get-made check, and the Stakes swap test. The lead-in at line 233 already
routes the rest correctly: "Field-level rules are in `assets/piece-additions.md`."

Then replace the five validation criteria:

```
1. **Substance.** Is there enough here for a whole video, or is it one good line?
2. **Payoff.** Is the end result specific, worth staying for, and something the viewer cannot get without watching?
3. **Credibility.** Can the creator support every claim in it from the brain dump?
4. **Channel fit.** Read `foundation/iceberg.md`. Does it serve the Iceberg statement and sit inside the pillars, rather than drifting into generic advice outside the creator's lane? Internal brand language stays out of the Frame unless the audience already knows it.
5. **Distinctiveness.** Apply both tests below.
```

with:

```
1. **Substance.** Is there enough here for a whole video, or is it one good line?
2. **Channel fit.** Read the Iceberg statement. Does it serve that statement and sit inside the pillars, rather than drifting into generic advice outside the creator's lane? Internal brand language stays out of the Frame unless the audience already knows it.
3. **Distinctiveness.** Apply both tests below.
```

That takes 70 to 64 and the generation-moment set to 46. It does not reach five and a
skill of this ambition will not. The point is that the six cuts were re-asking questions
an earlier step in the same run already answered.

### 5. The description carries no negative coverage, and a same-machine skill collides on nearly every trigger (check 3) [repeat of 2026-08-04 finding 7]

**Verdict.** Fail. Description is 748 characters, well under the 1,536 truncation, so
there is room.

**Evidence.** Line 3 has no "not for" clause. The body's boundary line was deleted in
commit d46341b ("stop narrating the pipeline"), which removed:

> **Scope: the angle, never the words.** It does not capture raw material
> (`vid-intake`), pick the topic (`vid-ideas`), write the title (`vid-title`) or
> thumbnail (`vid-thumbnail`), build the outline (`vid-structure`), or draft a line of
> script.

Deleting it from the body was right; that was narration nobody acts on. But the boundary
now exists nowhere, and the router never read the body copy anyway.

The confusions are real and adjacent by trigger phrase. `vid-ideas` fires on "what should
I make", this skill fires on "what should this video be about". `vid-intake` fires on "I
want to make a video about X". The key use case, "Use whenever a piece needs its direction
decided", currently lands at character 324 of 748, behind a summary of what the skill
contains.

**Fix.** Replace line 3 with:

```
description: Use whenever a piece needs its direction decided, including when the creator never says the word "frame". Turns a video idea into a decided video: reads the brain dump and the creator foundation, writes several genuinely different framings of the same idea each with a Core Payoff, and recommends one. Once the creator picks, writes the read, sets the format and the goal, and saves it all to piece.md before handing to vid-title. Triggers include "frame this video", "pick the angle", "what should this video be about", "what's the angle here", "what part of this do people actually care about", "re-frame this piece", "I don't know how to position this one", and any point where a creator has an idea but has not decided why anyone would watch it. Not for capturing raw material (vid-intake), not for choosing which video to make next (vid-ideas), and not for writing the title or thumbnail (vid-title, vid-thumbnail).
```

965 characters, still clear of the truncation.

Separate, and not a fix to this file: your machine has a second installed skill,
`content-creation-studio:video-framing`, described as "Transform video ideas into
must-watch concepts by finding unique angles. Use when brainstorming video angles,
positioning content, or finding the psychological hook for a video idea." That collides
on nearly every trigger. Naming it in the shipped description would be wrong, since
creators will not have that plugin. Resolve it locally by retiring or renaming it.

### 6. `examples.md` contradicts Step 3 at the same step (check 5) [repeat of 2026-08-04 finding 4]

**Verdict.** Fail.

**Evidence.** SKILL.md line 74: "Hold the approved context still. Every option below is a
different video made from the same context, not a different context."

`references/examples.md` lines 199 to 201, opened at that same step: "Batches 1 and 2 hold
the context still and vary the video. The other axis holds the raw idea still and varies
who it is for. Both matter." It then spends fifteen lines working that second axis with
two frames aimed at two different audiences (lines 203 to 215).

The instruction says one axis. The standard says two and demonstrates the second. This
resolves arbitrarily, which is worse than either rule alone.

**Fix.** Delete `referencesBut you're saying things like, you know, for number five, you're like, it doesn't do, you could say it doesn't do this if you want. That's actually helpful according to your documentation or according to like the skill or the audit skill. But the thing is, is adding in vid ideas, vid title, vid thumbnail, vid structure, all that kind of crap is like we have a router for a reason. And I don't know. It should know what this skill does. And if it only does that, Cloud's probably not like, hey, it does a bunch of other, it's probably not like, hey, it also does a bunch of other things. No. You know what I don't want a bunch of other references necessarily for like, you can improve the description, but I just don't want a bunch of freaking references about thumbnails, titles, ideas, things like that you Okay. OK, go ahead and for number six, go ahead and do that fix. Make sure you do one at a time, and you validate that it works. But yeah. Okay. you you /examples.md` lines 199 to 217, from "# The second axis: same
idea, different audience" through "one video retitled." and the `---` under it. If the
material is worth keeping, its home is `references/finding-the-core.md`, read at Step 2
while the audience is still open, not at Step 3 after it is approved and fixed.

### 7. Two taxonomies both called format, one term in both (check 12) [repeat of 2026-08-04 finding 5]

**Verdict.** Fail.

**Evidence.** `references/patterns.md` line 206: "# Video Format Patterns", holding System
or Framework, Comparison, Review or Ranking, Expert Breakdown. Line 155 of the same file:
"## Case Study", a proof pattern.

`references/format-index.md` line 12 onward: the seven values of the `format` field,
including `case-study` at line 15, which becomes `format: case-study` in frontmatter and
selects `knowledge/format-planners/case-study.md` for vid-structure.

A frame carrying "Framing DNA: Case Study + Specific Result" from Step 3 is one run away
from `format: case-study` getting locked by association at Lock and Save instead of by
`format-index.md` line 24. The failure is a wrong planner handed to vid-structure, and it
is silent.

**Fix.** In `references/patterns.md`, replace:

```
# Video Format Patterns

These patterns shape how the idea is organized and delivered.
```

with:

```
# Delivery Patterns

These patterns shape how the idea is organized and delivered inside the video. They are not the `format` field, which is one of the seven in `references/format-index.md` and gets set at Lock and Save.
```

And insert after "Uses a real person, channel, project, or result as evidence.":

```
Not `format: case-study`. This is a proof pattern used inside a frame; the format field is set separately at Lock and Save.
```

### 8. The reference table forbids a read the skill instructs (check 5) [repeat of 2026-08-04 finding 8]

**Verdict.** Fail.

**Evidence.** SKILL.md line 258: "This table is exhaustive for reading. Read nothing
outside it."

SKILL.md line 225: "Read `assets/piece-additions.md` for the exact shape, then write to
`content/pieces/{slug}/piece.md`." Line 233 names the file again. It is not in the table
at lines 247 to 256.

**Fix.** Insert into the table, above the `piece-contract.md` row:

```
| Exact piece.md shape, when saving | `assets/piece-additions.md` | Lock and Save |
```

### 9. Emphasis caps and a typo in the read-timing line (check 6)

**Verdict.** Fail, 1 instance worth editing of 2 found.

**Evidence.** SKILL.md line 37: "Read the referenced files ONLY when you move to the
appropriate step where its referenced." Caps emphasis plus "its" for "it's". The other
instance, "What do they REALLY want from this topic?" at line 53, sits inside an internal
question rather than an instruction and reads as spoken emphasis; leave it.

**Fix.** Replace:

```
Read the referenced files ONLY when you move to the appropriate step where its referenced.
```

with:

```
Read each reference file at the step that names it.
```

### 10. The standard demonstrates the failure a live rule names (check 14)

**Verdict.** Fail, 6 of 10 worked frames.

**Evidence.** SKILL.md Step 3: "Vary how they open: two options starting the same way
read as one idea reworded."

`references/examples.md` is read at that same step and line 5 calls it "the standard."
Its ten worked frames open:

> A story about how the advice every creator repeats...
> A video that takes the twelve pieces of advice...
> A video about why a channel this size gets shown...
> A video about the six months a creator spent...
> A video about the last proposal this designer ever sent...
> A video putting two recordings of the same kind of sales call...
> A video about why polishing the portfolio...

plus the three Fixed versions in the stiff pairs: "A video showing how...", "A video
about what actually happens...", "A video about the moment...".

Six of ten open "A video about". Batch 1 breaks the rule inside a single batch (Options
C and D), and so does Batch 2 (Options A and C). The instruction says two options
starting the same way read as one idea reworded, and the file held up as the standard
does it twice.

The mechanism: the model reads a rule, then reads ten demonstrations, six of which
break it. Demonstrations win, which is the entire reason examples exist in a skill. The
observable is a batch where most options open "A video about" and the variety rule
reads as decoration.

**Fix.** Rewrite the openings so the standard demonstrates the rule. In
`references/examples.md`, Batch 1 Option D, replace:

```
A video about the six months a creator spent quietly deciding they were not talented enough, and the boring mechanical reason their videos were not being seen that had nothing to do with talent at all.
```

with:

```
Six months of a creator quietly deciding they were not talented enough, and the boring mechanical reason their videos were not being seen that had nothing to do with talent at all.
```

Batch 2 Option C, replace:

```
A video about why polishing the portfolio and tightening the pitch make the audition worse instead of better, and what actually decides which side of the table is being evaluated.
```

with:

```
The case that polishing the portfolio and tightening the pitch make the audition worse instead of better, and what actually decides which side of the table is being evaluated.
```

That leaves no batch with two options sharing an opening, and it leaves "A video about"
as the plain default it should be rather than the only move on the page.

### 11. Nine rules describing a shape the examples already demonstrate (check 7)

**Verdict.** Fail, 7 of 9 rules convert.

**Evidence.** Step 3 carries nine rules about how a frame should read:

> **Write it in plain language.**
>
> A frame should sound like a creator clearly explaining the video they want to make,
> not a strategist writing a report. Never a headline. Keep it to 1-2 sentences. The
> list above is what the frame has to make clear, not five clauses to cram into one
> sentence.
>
> `references/examples.md` opens with three stiff frames rewritten. Read the register
> off those pairs. Vary how they open: two options starting the same way read as one
> idea reworded.
>
> Be specific rather than vague. The hidden thing, the part that is not obvious to
> everyone else, is what creates intrigue, so keep the answer withheld. Just make the
> setup around it concrete enough to picture. Do not over-explain.

`references/examples.md` lines 9 to 45 already demonstrate every one of those except
two: three stiff frames next to their fixed versions, each with a "What changed" line
naming the move, closing on "keep every piece of framing information, change only the
language."

This is the "Voice and style" conversion in `Resources/rules-to-judgement.md`, almost
line for line: "The rules were a bad proxy for the examples. Point at the shape, not at
a list of things the shape isn't."

Two rules do not convert, and both survive for a reason the method itself predicts.
"Never a headline" survives because no example shows a headline being rejected, so the
demonstration does not carry it. "Vary how they open" survives only once finding 10 is
fixed, because right now the examples demonstrate against it.

**Fix.** Apply finding 10 first. A sentence that points at the standard is only as good
as the standard. Then replace the block above with:

```
**Write it in plain language.**

Write frames that read like the Fixed versions in `references/examples.md`. Never a headline. The list above is what the frame has to make clear, not five clauses to cram into one sentence.

Vary how they open: two options starting the same way read as one idea reworded.
```

Nine rules to three. Plain language, register, sentence count, specificity, the withheld
answer, the concrete setup and the do-not-over-explain rule are all carried by the three
pairs, which show them rather than assert them.

The same pattern repeats three more times in this file and is worth naming as one
observation rather than three findings: Step 2's six internal questions sit on
`finding-the-core.md`, whose three traces demonstrate the dig; Step 4's six Core Payoff
shapes sit on its own avoid/prefer pair two lines below them; Step 5's six Must Deliver
examples sit on the Must Deliver line every worked option in `examples.md` already
carries. Each is a bullet menu layered on a demonstration of the same thing. Step 2's
menus are already deletion candidate 3; the other two are the same test.

Where check 7 does not apply, so it is not tried: Step 6's validation criteria, the two
difference tests, and "When a Batch Is Rejected" look like one cluster and are three
(a per-option gate, a per-batch gate, and a recovery path). Case 1 in
`rules-to-judgement.md`: genuinely different cases, keep them, count them individually.
The pre-save bullets are a deduplication against `piece-additions.md`, not a judgement
conversion; converting them would be the wrong repair.

## Passes

Check 2 (description is a trigger, third person, 748 characters, clear of the 1,536
truncation; ordering is finding 5). Check 9 (nothing stated that the model would read off
the filesystem or know from being Claude). Check 10 (six reference files, zero
unconditional, every one with a named step trigger: `finding-the-core.md` Step 2,
`patterns.md` Step 3, `examples.md` Step 3, `format-index.md` Lock and Save,
`piece-additions.md` Lock and Save, `piece-contract.md` Lock and Save; the table gap is
finding 8, not a trigger gap). Check 11 (`format-index.md` line 30 dates its scores to
2026-07-28; the undated-claim failure is finding 1). Check 15 (no heading named Gotchas,
but "When a Batch Is Rejected" at lines 189 to 202 holds four real upstream causes plus
the two-question recovery, and "Never Invent" lines 31 to 33 hold the creator's-own-history
trap, which is a real one; a missing heading is not a finding when the content exists).
Check 16 (no absolute rule here has a cost a hook could enforce that a sentence cannot;
the nearest candidate, "never lock one with no planner in `knowledge/format-planners/`",
is checkable on disk and worth enforcing only if this ever runs unattended).

Check 13 fails by the letter and gets no fix. This is a judgement skill and it opens 574
lines of patterns and examples at Step 3, the exact moment a judgement skill's search
space should be widest. The honest test is deletion, not a rewrite. See candidates 1 and 2.

## Deletion candidates

**1. `references/patterns.md` entirely (353 lines, opened at Step 3).** Prediction: batch
variety holds, because Step 3's "vary what kind of video it is" plus the Must Deliver test
carry it, and a frontier model already knows this taxonomy. What changes is the Framing DNA
labels, which get vaguer or stop appearing, and Framing DNA is not saved to piece.md by
anything. How you tell: run one real brain dump twice, with the file and without, and
compare whether the options still differ in genre and in Must Deliver. If the batch
collapses to two genres without it, put it back. This is the largest single file the skill
opens at its highest-pressure moment, which is why it is first.

**2. `references/examples.md` Batch 2 (lines 142 to 196).** Prediction: nothing changes.
Batch 1 already demonstrates the shape, the four-videos-not-one argument, and the fake-batch
contrast. Batch 2 teaches the same lesson in a different world. How you tell: check whether
the batch still produces options with genuinely different production requirements. If Batch
1 alone makes every option story-led, Batch 2 was doing work and only finding 6's second-axis
block should go.

**3. Step 2's two menus (the six internal questions at lines 53 to 58, the five gaps at
lines 62 to 66).** Prediction: entry points get less formulaic, because `finding-the-core.md`
already teaches the dig through three worked traces and the menus give a checklist to fill
instead of a nerve to find. How you tell: read the entry point out loud. With the menus gone
it should stop reading as six answers in a row and start reading like the one sentence the
reference file's closing test asks for ("If it sounds like a description of an audience
segment, it is the surface"). If entry points get shallower rather than plainer, the menus
were load-bearing.

## The split question

Lock and Save is a procedure inside a judgement skill: read the format index, state format
and goal, read the shape file, append to piece.md, run seven pre-save checks, report. It is
22 of the 70 constraints and it runs at a moment when none of the framing craft is live any
more. Splitting it out would take the generation-moment budget down without touching the
craft. Against that: the format call genuinely reads off the locked Frame, so a split skill
would have to re-read what framing just decided. Your call, and nothing else in this report
depends on it.

## Coverage correction

The first version of this report ran the sixteen checks against SKILL.md and used the
six reference files only as evidence about it. Two gaps, both found by Billy on review:

**Check 7 was not run.** It appeared in neither the findings nor the Passes list, which
means the report implied coverage it did not have. Now run: finding 11.

**The include test was never applied section by section to the reference files.** Run
now, and it produces no new findings, which is worth stating rather than leaving silent.
`finding-the-core.md` earns its 191 lines: its three traces demonstrate a dig method no
instruction in the skill describes, which is case 3 in `rules-to-judgement.md`.
`format-index.md` is a decision table with dated scores. `piece-additions.md` is the
write shape, with the four-bullet overlap already in finding 4. `examples.md` is the
standard, with findings 6 and 10 against it. `patterns.md` is the one file the test
argues against, and it is already deletion candidate 1: its fifteen pattern entries are
largely knowledge the model has from training (check 9), and with `Framing DNA` cut it
now has no consumer that reaches the creator. That is a deletion to test, not a finding
to write, which is where the first version left it and where it stays.

## Verification note

Nine findings survived the skeptic pass. Three did not and were cut: a check-5 finding on
"State both, do not ask" at line 217 sitting eight lines above "Ask the cost question first,
every time" at line 227 (different subjects, no contradiction); a check-8 finding on the
read-timing rule at line 37 being stated three times (it is stated once, and line 258 is a
different rule about scope); and a check-15 finding on the missing Gotchas heading (the
content exists under "When a Batch Is Rejected").

No behavioral verification was run. Finding 1 is confirmed by file inspection rather than
hypothesis: the writer does not exist. Finding 3 has independent evidence in the form of a
workaround written into vid-title. Everything else is a hypothesis until a real run tests
it, and the deletion candidates are the only items with a test attached.

## Decisions

Reviewed 2026-08-04. Applied items landed the same day.

- **1. Foundation migration.** Deferred. Billy fixes the migration separately. `vid-pipeline` line 58 needs the same edit whenever that happens.
- **2. Psychological Hook and Why They Will Stop Scrolling.** Approved, applied. Both fields cut from Output Format, and the duplicate field list cut from What This Creates.
- **3. Never a headline.** Approved with a correction, applied. The fix landed as "Never a headline." with no mention of `vid-title`: naming the downstream skill hands the model a skill it has no business thinking about at Step 3, and the justification clause was arguing for the instruction. Billy asked whether `examples.md` already covers this. It does not: the stiff/fixed pairs contrast report language against plain language, and both sides of all three pairs are descriptions. No example shows a headline being rejected, so nothing at Step 3 ruled one out.
- **3a. Resolved by finding 11.** "Keep it to 1-2 sentences" is one of the seven rules the examples already demonstrate. It gets absorbed by the conversion rather than dropped, which is the answer to whether the examples are enough: for that rule, yes. For "never a headline," no.
- **10. Opening variety.** Approved with corrections, applied. Batch 2 Option C landed as Billy's version, dropping "A video about" and starting on "Why polishing the portfolio," rather than the proposed "The case that." Batch 1 Option D also lost "mechanical" in the same edit: nobody says "the boring mechanical reason," and "the boring reason" carries the contrast because "had nothing to do with talent at all" is already doing that work. Verified afterward that no batch has two options sharing an opening.
- **11. Nine rules to three.** Approved, applied after 10. Step 3 now points at the Fixed versions as the shape and keeps only the two rules the examples cannot carry.
- **11a. Approved, applied.** The three sibling clusters from finding 11 are cut. Step 2 loses eleven bullets (the six internal questions and the five gap types) and now runs on "It should feel like you're reading their minds" plus the three traces in `finding-the-core.md`, whose own closing test carries the standard. Step 4's six payoff shapes fold into one sentence, with the avoid/prefer pair left to demonstrate. Step 5's six Must Deliver examples are replaced by a pointer to the seven worked options in `examples.md`, which state theirs better than the bullets did.
- **4a. Substance.** Approved, cut. Step 6 renumbered to four criteria.
- **4b. Pre-save bullets.** Approved, cut. Three of seven survive: the word-for-word check, the would-actually-get-made check, and the Stakes swap test. Those are the three nothing else states.
- **7b. `patterns.md` heading.** Approved, applied. "Video Format Patterns" is now "Delivery Patterns" with the `format` field named as a separate thing, and the Case Study proof pattern carries a line saying it is not `format: case-study`.

## Mechanical verification of the applied cuts

Every instruction removed was checked against the context live at the same moment.

- Four pre-save bullets: "no their-goal-is scaffold" is `piece-additions.md` line 42, "names the same ending as core_payoff" is line 44, "everything traces, a gap is named" is line 78 with the `> [!todo]` shape at line 62, and format/goal are set eleven lines above the cut in Lock and Save. One thing genuinely lost: SKILL.md named "their pain point is" as a scaffold variant and `piece-additions.md` names "their challenge is". The variant list is now shorter by one.
- Step 2's eleven bullets: "what have they already tried" survives where it does the most work, in the recovery path at "When a Batch Is Rejected."
- Step 5's six examples: verified all seven worked options in `examples.md` still carry a Must Deliver line, since the replacement text points at them.
- Step 4's six shapes: folded into a sentence, not dropped.
- Substance: nothing else stated it, and that is the finding. It is a deliberate deletion, so it is the one item here with no safety net. If options start arriving that are one good line with nothing behind them, this is the first thing to put back.

SKILL.md 260 lines to 185. Total loaded context 1,271 lines to 1,151.

- **Deletion candidate 1, `patterns.md`.** Not deleted. Cut to 182 lines from 355, after Billy corrected the reasoning behind it. My claim that the Blending sections were "dead since Framing DNA came out" conflated the field with the practice. The field is gone; fusing one main pattern with one or two supporting ones is still exactly what a good frame does. Batch 1 Option A is a personal story that is also a myth-bust and a transformation, and Option B is an experiment carrying a ranking. Both verified against the current `examples.md` text before the claim went into the file.

  Cut: the Example Frame and Why It Works blocks under all fifteen patterns, and the three worked Blending examples. The Example Frames were the real cost, not just bulk: generic YouTube-growth lines sitting in context next to `examples.md`, which is the actual register model, and two of the three Blending examples were weaker duplicates of Batch 1 Options A and B.

  Kept, deliberately: all fifteen pattern names, their one-line definitions, every Best for, and every Must Deliver. The Must Delivers are the reason the file survives at all, because `examples.md` works only seven frames and never touches eight of these patterns, so nothing else in the skill says what a Hypothetical Restart or a Mistake or Warning owes. Kept the full Pattern Selection Guide. Kept "Choosing Between Two That Fit," which the earlier version of this report wrongly called duplicated: SKILL.md says do not force a pattern the evidence cannot carry, and this section is the only place that says how, by checking the Must Deliver against the dump. It also carries the anti-double-validation guard pointing at Step 6.

  Converted rather than deleted: six Blending Rules became three sentences. Rules 1, 2 and 5 collapse into "one pattern controls the direction and the rest serve it," which is the judgement sentence that was already sitting two lines under them. Rule 3 survives on its own. Rules 4 and 6 were the only genuine duplicates, of SKILL.md line 64 and Step 5.

Total loaded context now 978 lines, from 1,271 at the start of the audit.

- **12. Four names for one artifact (check 5), raised by Billy.** Not in the original findings and it should have been. `finding-the-core.md` called the thing it produces "the core" in its title, "the nerve" in its body, "the context" in nine section headings, and "the entry point" in lines 3, 21, 77 and 187. One file, four names, for the one artifact Step 2 hands to Step 3. SKILL.md and `examples.md` split the same way: SKILL.md titled the step "Find the Audience Entry Point" and then said "Hold the approved context still," and `examples.md` labelled both batch headers "Context (approved at Step 2)."

  "Context" was the worst of the four, because in a skill file it also means the context window.

  Fixed to one name, "entry point," everywhere: 24 verified replacements in the reference file, three in SKILL.md, six in `examples.md`. The file is renamed `references/finding-the-entry-point.md`, with both pointers updated. Verified afterward that the only surviving uses of the word "context" in the skill are the `voice_context` field and "honest context around the number" in a Must Deliver line.

  Section headings went from labels you have to decode to labels that say what they are: "Trace 1: The long accretive dump" is "Example 1: A brain dump built up over several sessions," "The dump" is "The brain dump," "The surface read" over "*What a shallow pass returns:*" is "The obvious answer" over "*What you get from reading it once:*," "The dig" is "What is actually going on," and "The context" is "The entry point."

  Left alone deliberately: "Follow the heat, not the headings" and "heat in the wrong place." Those are metaphors defined by the sentence immediately after them, which is writing rather than jargon. The test applied here was whether a reader has to decode a label to navigate the file, not whether a figure of speech appears.

  **Correction, same day.** The first pass at this renamed everything to "entry point," which is another invented label that says nothing. Billy caught it. The artifact is a paragraph describing one person and what is actually going on with them, so the name is **the viewer**. Renamed again across all three files, file now `references/finding-the-viewer.md`.

  The second name is better than a tidy-up. Step 3's rule went from "Hold the approved context still. Every option below is a different video made from the same context, not a different context" to "Hold the viewer still. Every option below is a different video for the same viewer, not a different viewer." That is the sharpest statement of that rule the skill has had, and the batch headers in `examples.md` now read "Four videos for one viewer," which says the whole lesson in the heading.

### 14. The skill invites the narration it produces (check 8), found in a real run

**Verdict.** Fail, 3 causes. This is the first finding in this audit backed by observed output rather than by reading.

**Evidence.** A live run opened with:

> Read the dump, the avatar, and the iceberg. Holding one viewer still across all four: a business owner writing with AI who already told it not to sound like AI, watched it drift back anyway, and is now spending more time rewording the output than writing would have taken.
>
> Four survived.

Three lines, three separate causes, none of them the model freelancing.

"Four survived" is the skill obeying an instruction. SKILL.md said "Say how many survived, in a clause." The culling is real (Step 6 drops failures and "Anything that fails does not get offered"), so the count was honest. Asking for it out loud is what exposed machinery the creator has no use for.

"Holding one viewer still across all four" plus the restated viewer came from `examples.md`. Every batch there is laid out as a heading, then "**The viewer (approved at Step 2):**", then the paragraph, then the options. Line 5 calls that file "the standard," so the model reproduced its presentation shape and not only its frame register. It turned a teaching scaffold into a preamble, and re-showed the creator a paragraph they had already approved one step earlier.

"Read the dump, the avatar, and the iceberg" came from a hole. `## Output Format` began at `### Option [Number]` and never showed what the message opens with, so the model invented an opener, and the most available thing to say was what it had just done.

**Fix.** Applied, three edits, no new rule layer.

In `## What This Creates`, replace "Say how many survived, in a clause." with "The ones that failed are not mentioned; the creator counts what is in front of them."

Under `## Output Format`, insert above the option block: "The message opens on Option 1. Nothing above it."

In `references/examples.md`, extend the line above the batches with: "The viewer paragraph heading each batch is what went into it, not something the creator gets shown a second time."

Checked and left alone: `patterns.md` and `finding-the-viewer.md` invite nothing. The only hits are prose about the worked examples, and "Say it out loud" in `finding-the-viewer.md` closes on an internal judgement rather than a thing to say to the creator.

Also left alone on Billy's call: the `## Recommendation` block, which worked in the same run.

### 13. The test that governs the file is the last line in it (check 1)

**Verdict.** Fail. Raised but not applied.

**Evidence.** `references/finding-the-viewer.md` closes on the sentence that decides whether the whole exercise worked:

> Say it out loud. If it sounds like a description of an audience segment, it is the surface and you have not dug yet. If it sounds like something you would say to one specific person to make them go quiet, you found it.

It is at line 189 of a 191-line file, after three long worked examples. A reader gets the test only after doing the thing the test judges.

**Fix.** Move that paragraph directly under "## Saying it back," before Example 1 begins, and leave a one-line pointer back to it in the closing section. Not applied, awaiting a call.

### On whether `finding-the-viewer.md` earns its length

Billy asked. It is the best-built file in the skill and no finding is manufactured against it.

Each of the three examples runs the full chain: raw material, the shallow answer, the reasoning, the real answer. The three cover genuinely different shapes rather than three of one kind (accreted over four sessions, one spoken sitting, the creator arguing about whether to make the video at all), which is what "cover the range" means in check 13. And the shallow-answer sections are the rarest thing in the skill: most examples anywhere show only good output, which teaches what good looks like but not how to tell it from the plausible thing beside it.

Check 7 was run against it and produces no conversion. The five-place list ("look in the asides, the self-corrections...") looks like a cluster that "Follow the heat, not the headings" would replace, and it does not: two of the five are not heat. Something said twice without noticing is repetition, and getting something wrong about your own work is self-correction. Case 1 in `rules-to-judgement.md`, genuinely different cases. Kept and counted rather than collapsed.
- **4. Rule budget.** Split decision.
  - Validation criteria 2 (Payoff) and 3 (Credibility): **rejected.** Billy keeps both. The finding was that each is stated at an earlier step in the same run, not that either is unimportant; he reaffirmed, so they stay.
  - The four duplicated pre-save bullets: **open, not applied.** Awaiting a call.
  - Criterion 1 (Substance): **recommend cutting, not sharpening.** Reasoning revised after Billy pushed on what it means. Substance is the only one of the five that fails an option for being small rather than for being wrong, and the skill has no action attached to that failure: Before You Start routes on a missing `brain-dump.md`, never on a thin one, so nothing defines where a Substance failure goes. Billy's own read is that a three-sentence idea should still get framed the most interesting way it can be, which makes a gate that rejects it a gate that fires wrong. The honest version of the test already exists at Step 5, "Reject any frame the creator cannot honestly support," which catches the frame promising more than the material can pay. That is the real failure. Thin is not.
- **5. Description.** Negative coverage **rejected**: naming vid-ideas, vid-intake, vid-title and vid-thumbnail in the description spends the router's attention on four skills this one never does, and the router already separates them. Reordering **approved, applied**: the key use case now leads at character 0 instead of 324. 748 characters, unchanged in length.
- **6. `examples.md` second axis.** Approved, applied. Lines 199 to 217 deleted.
- **7. Format taxonomy collision.** Superseded. Billy cut the `Framing DNA` field instead, which removes the path the collision travelled. See 7a. The `patterns.md` heading rename is **open** and now low priority.
- **7a. Framing DNA cut.** Approved, applied. Confirmed first that nothing saves it: `piece-contract.md` line 70 and `piece-additions.md` both list vid-framing's writes without it. Removed from Output Format, from all seven worked options in `examples.md`, and the "On Framing DNA labels" section at the end of `examples.md` deleted with it. Consequence: `patterns.md` now has no output-visible consumer at all, which makes deletion candidate 1 the next thing worth testing.
- **8. Reference table.** Approved with a bigger cut, applied. The whole `## Reference Files` section is gone. Verified afterward that every reference is named inline at its step: `brain-dump.md` and `avatar.md` at Step 1, `finding-the-core.md` at Step 2, `patterns.md` and `examples.md` at Step 3, `foundation/iceberg.md` at Step 6, `format-index.md` and `piece-additions.md` at Lock and Save. The avatar row's "(avatar, Top 3 perceived problems)" detail was folded into the Step 1 line rather than lost.
- **8a. Two things the table cut dropped, flagged rather than restored.** "This table is exhaustive for reading. Read nothing outside it." is gone, so nothing now bounds what the skill may open. And `knowledge/piece-contract.md` lost its only direct pointer; it is still reachable through `piece-additions.md` line 77, which is read at the same step, so the ownership map is one hop away instead of loaded. Both are defensible as cuts. Neither was the stated intent of the edit.
- **9. Emphasis caps and typo.** Approved, applied. Line 37 is now "Read each reference file at the step that names it."

SKILL.md 260 lines to 225. `examples.md` 221 to 174.
