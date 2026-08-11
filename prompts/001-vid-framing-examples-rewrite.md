<!-- target: Opus 5 | effort: high | subagents: not needed -->

# Rewrite vid-framing's examples and the rule that contradicts them

The creator approved a new construction for the `frame` field in the `vid-framing` skill. Seven rewritten example options are pasted below, already approved word for word. Your job is to land them in the skill's example file and fix the three places elsewhere in the skill that still describe the old construction.

Everything is under `c:/Users/billr/projects/authentic-ai-content-engine/.claude/skills/vid-framing/`.

**Precondition:** the working tree must be clean for that directory before you start. If `git status --short .claude/skills/vid-framing/` returns anything, stop and say so. The scope check at the bottom depends on it.

## The approved text

Use this verbatim. Do not reword a frame or a core payoff. Must Deliver lines may be tightened for fit but must keep the same obligation.

### Batch 1: small creator, 57 subscribers after six months

**Option A. The advice that kept them stuck**
- Frame: I'm going to show creators sitting at 57 subscribers after six months of uploading which piece of the advice everybody gave them was the thing holding the channel down, and what I put in its place.
- Core payoff: You can drop the one habit that's costing you and know exactly what replaces it.
- Must deliver: The exact advice, why it fails at that size, and what replaced it. Without the swap it's clickbait.

**Option B. Testing what they already tried**
- Frame: I'm going to run every piece of advice small creators get handed for 30 days, so anyone still stuck under a few hundred subscribers can see which ones moved the numbers and which ones just ate their week.
- Core payoff: You can stop spending your week on the advice that failed the test and put those hours into what didn't.
- Must deliver: What was tested, what happened, and an honest line on what the test can't prove.

**Option C. What they can actually change**
- Frame: I'm going to show creators who know their video was good and watched it go nowhere anyway what YouTube is actually doing in the first few hours after you publish, and the one part of that you can reach.
- Core payoff: You can see where the video actually stalled and change the one piece that's yours before the next upload.
- Must deliver: What happens after upload, and one part of it the creator genuinely controls.

**Option D. The wrong conclusion**
- Frame: I'm going to show creators who have quietly started to think they are not talented enough what was actually wrong with their videos, and it has nothing to do with talent.
- Core payoff: You can stop reading your view count as a verdict on you and see the boring mechanical thing that was really in the way.
- Must deliver: What was really holding the videos back, why it got mistaken for a lack of ability, and what changed after.

### Batch 2: freelance designer, auditioning on every call

**Option A**
- Frame: I'm going to show designers who send a careful proposal and then wait three days for a reply how to get the yes, the no, or the real objection out of the client before the call ends.
- Core payoff: You can run your next call so it ends with a decision instead of a proposal.
- Must deliver: The old process, the one that replaced it, how the decision gets handled live, and what changed. Real numbers where they exist, and say plainly where they weren't tracked.

**Option B**
- Frame: I'm going to put two sales calls side by side so designers who feel like they are being interviewed can hear the exact sentence where one of them handed the decision over.
- Core payoff: You can catch yourself in the moment you start auditioning and say something else instead.
- Must deliver: Real recordings or accurate call examples, the specific moments the dynamic flips, and an alternative for each. Cannot reduce to advice about confidence.

**Option C**
- Frame: I'm going to show designers who keep rebuilding the portfolio and rewriting the pitch why every round of polish makes them easier to judge, and what actually decides who is doing the judging.
- Core payoff: You can stop proving you are good enough and start deciding whether the client is a fit.
- Must deliver: Why more proof doesn't change the dynamic, the behaviors that create the audition, and a practical way to lead without performing.

### The bad batch, rewritten

Replace the existing "What a bad batch looks like" quartet with these. The old ones were in the old phrasing, so a reader could conclude the lesson is about sentence shape. It isn't.

> I'm going to show small creators which advice is keeping them stuck, and what to do instead.
>
> I'm going to show small creators why the popular advice is why their channel isn't growing.
>
> I'm going to show beginner creators the common advice that keeps them invisible, and the fix.
>
> I'm going to show small creators what they were told to do that is quietly killing their growth.

Keep the existing "Why those are bad" explanation and extend it by one point: the who never gets more specific than "small creators," and not one names a thing the viewer physically does. The construction is correct and the batch is still worthless.

## What the construction is

Add this to `references/examples.md` as a short section above Batch 1. It is the part the creator most wants captured, because the sentence shape is the least of it. Four things, in plain prose, no more than a dozen lines:

1. **The who is a thing they physically do.** "Business owners who rewrite every AI draft line by line." An action you could film, specific enough to sting. Not a demographic, not a feeling. Batch 1 Option D is the licensed exception: its who is a private thought, and that is exactly what makes it a different video from A, B and C.
2. **The what has a handle they already own.** "An autocorrect." A noun from the viewer's real life, not an invented label. Never "a system for catching AI language."
3. **The clause after the verb carries the insight.** "Before the draft ever reaches them" is where the video's actual idea lives.
4. **The verb is physical.** Install, drop, run, put side by side. Not understand, not learn about.

Core payoff is second person, present tense, and states what they walk out able to do. Not what they will know, and never opening with "by the end of this video."

State plainly that the "I'm going to show X how to Y" spine is not a mould. The seven approved options run seven different spines, and the file should say so rather than let a reader copy one shape.

## The other three files

**`assets/piece-additions.md` line 17.** The `frame` field rule currently reads "third person, one direction only. Never a spoken line, never a headline, never a description of the contents." First person and spoken is now correct. Rewrite that parenthetical to describe the approved construction. Leave the `core_payoff` rule on line 18 alone: it already says second person and the approved payoffs match it. Leave line 31's third-person display flip alone unless it now contradicts itself, in which case fix it and say what you changed.

**`templates/output-format.md` line 8.** "[One concise paragraph describing the video direction.]" describes the old form. Replace with a placeholder that matches the approved construction.

**`SKILL.md`.** Two dangling references, fix only:
- Line 128 reads ``Read `references/output-format.md` ``. The file is at `templates/output-format.md`.
- Line 79 reads "Write like the Fixed versions in `references/examples.md`." There are no Fixed versions in that file. Point it at the approved options instead.

Also in `references/examples.md`: line 3 says to read the file "after the viewer is approved," but Step 2 of SKILL.md is now internal and nothing gets approved. Fix that line. Delete the stray triple-backtick fences at the end of the file. Drop the `finding-the-viewer.md` pointer on line 103, since SKILL.md no longer cites that file and each batch carries its own audience paragraph.

## Out of scope

Do not touch `references/patterns.md`, `references/finding-the-viewer.md`, `references/format-index.md`, or anything under `tests/`. The eval rubric at `tests/skills/vid-framing/rubric.md` still says a frame "is not a spoken line" and will now fail every approved option. That is known and deliberately deferred. Do not fix it, and do not mention it as a recommendation.

Do not invent an eighth option, a third batch, or an audience. The two audiences stay as written.

## Done

Run all five from the repo root and paste the raw output.

```bash
# 1. old construction gone from the skill
grep -rniE "\ba video (about|showing|that shows)" .claude/skills/vid-framing/     # expect: no matches

# 2. every approved frame landed
grep -c "I'm going to" .claude/skills/vid-framing/references/examples.md          # expect: >= 11

# 3. no em-dashes anywhere (hard rule, see CLAUDE.md)
grep -rc $'\u2014' .claude/skills/vid-framing/                                     # expect: 0 on every file

# 4. every path SKILL.md cites resolves
grep -oE '`(references|templates|assets)/[a-z-]+\.md`' .claude/skills/vid-framing/SKILL.md \
  | tr -d '`' | sort -u | while read f; do
      test -f ".claude/skills/vid-framing/$f" && echo "OK   $f" || echo "MISS $f"; done

# 5. scope: exactly four files, nothing else
git status --short .claude/skills/vid-framing/ tests/
```

Check 5 is the one that matters most. It must list exactly these four and nothing under `tests/`:

```
 M .claude/skills/vid-framing/SKILL.md
 M .claude/skills/vid-framing/assets/piece-additions.md
 M .claude/skills/vid-framing/references/examples.md
 M .claude/skills/vid-framing/templates/output-format.md
```

## Report back with

The five command outputs verbatim, the four files changed, and any line you rewrote whose meaning you had to decide rather than copy.
