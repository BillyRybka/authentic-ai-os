---
name: vid-thumbnail
description: Write thumbnail TEXT that completes a locked title, never restates it. Mines the video's real numbers, paradoxes, and named systems from its own material, never invented, and locks 1-2 picks into piece.md. Text only; visual design is parked. Standalone or pipeline-invoked after vid-title, before vid-structure. Triggers on "thumbnail text", "thumbnail options for [video]", "thumbnail copy", "what should the thumbnail say", "pair a thumbnail with this title", "let's do the thumbnail".
---

# Video Thumbnail Text

The title is locked. This skill writes the other half of the package: thumbnail TEXT that completes it. Read the title, mine what the title does not already say, shape options, lock 1-2 picks with the creator.

**Scope: text only.** No layout, hero, expression, color, or image prompts. Text is the testable half of the package, so it gets its own pass; the visual comes later, and designing it is drift. **This is a conversation, not a document.** Short messages; references feed your thinking and never get pasted at the creator.

## What makes thumbnail text win

**The text completes the title; it never restates it.** The viewer reads title and thumbnail in one glance, as one unit; both carrying the same beat wastes half the package. The pair must raise more curiosity than either half alone, and one repeated word means rewrite one side. The four winning pairings:

- **Title states it, text proves it.** "Why Hiring a VA Tanked My Revenue (Fix Inside)" + "-30% IN 6 WEEKS". Cause in the title, receipt in the text.
- **Title asks it, text flips it.** "Should You Buy a House?" + "DO NOT BUY A HOUSE". The text is the unexpected answer.
- **Title teases it, text names it.** "The One Rule That Killed My Procrastination" + "THE 15-SECOND RULE".
- **Title shows the result, text shows the data.** "How I Got 481% Faster at Mile Times" + "23:07 → 19:42". Abstraction above, raw proof below.

**One hero idea.** A thumbnail never summarizes the video. One contrarian point, one dramatic number, one name, carried hard. Two ideas fused into one text is a cut, not a rewrite.

**The glance test.** Readable at feed size, in one breath. 1-4 words is the winning band, 5 is the ceiling. One high-curiosity word ("LIAR", "BACKWARDS") is valid. A pure number or arc ("275 → 175") counts as one unit.

**Specificity earns the click the title promised.** "$712,921.88" beats "$700K". "29 DAYS" beats "quickly". Real numbers, verbatim from the material, read as true; round paraphrase reads as marketing. A named system works only when the name carries its own mystery: "THE 90 MINUTE RULE" makes you ask "of what?", while "THE 12-SOP RULE" answers before you ask. A label is not a hook.

Worked calls, one title: "Why Hiring a VA Tanked My Revenue (Fix Inside)". Script numbers available: -30%, 6 weeks, +40%, 9 weeks, 12 SOPs.

- Weak: "VA TANKED MY REVENUE" restates the title; the viewer already read that. Strong: "-30% IN 6 WEEKS" adds the receipt instead, shares no words with the title, and matches the failure tone.
- Weak: "+40% IN 9 WEEKS" is a real number in the wrong register; a positive result against a failure title reads as contradiction, not curiosity. Strong: "STOP DELEGATING" keeps the dark register from a different angle, and the video pays it off.
- Weak: "BOTTLENECK" fits a hundred founder videos. Strong: "BACKWARDS" only makes sense for THIS video's wrong-order insight. If the word fits any other video in the niche, it is not a hero.

## What loads, and when

| Step | Load | For |
|---|---|---|
| 1 | `content/pieces/{slug}/piece.md` | the locked title (the anchor), format, goal |
| 1 | `content/pieces/{slug}/script.md` if complete, else `brain-dump.md` | the material and its numbers; a finished script supersedes the dump |
| 2 | `knowledge/thumbnail-text-patterns.md` | the 5 patterns, anti-patterns, pairing rules, examples library. The pattern reference |
| 2 | `foundation/packaging-system.md` and `banks/packaging-bank/*.md`, when present | packaging settings and receipts. **These override every default on this page** |

Day one, no packaging-system yet: ALL CAPS, no strategy constraint. No locked `title` in piece.md yet: run `vid-title` first.

## Step 1: Read the title, then mine for its partner

Name the title's hook (the question it plants) and its tone: failure, success, mystery, contrarian, instructive, news. Open with one line to the creator: the title, and that you are pairing it with the strongest material. Then mine the script (or brain dump) for what the title does NOT already say:

- verbatim numbers, dollar figures, percentages, timeframes. Also the **lock list**: the only numbers a candidate may use. Nothing invented, ever.
- belief-clashes and paradoxes the video argues, named systems and rules, the single most dramatic moment or claim

## Step 2: Shape candidates against the title

Load the patterns file and generate wide, privately. Write the title at the top of your working space and draft every candidate beneath it, each read as "title + this text, one glance." Same beat twice, dead on arrival. Know why each candidate makes someone click before it earns a spot.

Spread across the 5 patterns (cognitive dissonance, number-hero, named system, single-word curiosity, imperative command); they are lenses, not cages, so a text the material begs for that fits none still earns a spot, with the why said out loud. Honor the vault when it speaks: a strategy test in packaging-system biases part of the set, and packaging-bank winners outrank generic best practice.

## Step 3: Filter hard, then show the package

Only the strongest 3-5 survive, ranked, strongest first. Two strong means show two. Never pad, never caveat a flaw; a known flaw is a cut. Cut before the creator sees:

1. **Fabrication.** Any number off the lock list.
2. **Pre-delivered payoff.** "SOPs BEFORE PEOPLE" does not tease the lesson, it removes the reason to watch. The bar is click-pull plus deliverability, not spoiler-avoidance: "STOP DELEGATING" names the lesson and still pulls the click because the how stays inside the video.
3. **Package break.** Repeats a title word (parentheticals count), or its tone fights the title instead of matching or productively contrasting.
4. **Generic.** Would fit 100 other videos in the niche. The text must signal THIS story.
5. **Anti-pattern.** Per the patterns file: visual-metaphor words, vague paradoxes, hedges, stock hype, open-mouth language.

Then three tests on every survivor, through the ideal buyer's eyes, answered silently; a fail cuts:

1. **Context.** Does title + text together carry what the video is about? If not, the image has to, allowed only for a standout candidate, and noted at lock.
2. **Curiosity.** Does the pair make the buyer think what, why, or how?
3. **Clarity.** One idea, one glance?

Show the package, not a list in a vacuum: title on the first line, numbered candidates beneath, each line the text in quotes plus its pattern name and nothing else. No rationale paragraphs, no self-grading. They scan and pick. **Kill criteria:** after one full regeneration the options are still weak, the problem is upstream (vague title, or material with no number or moment worth a thumbnail); say so and stop.

## Step 4: Pick

Ask which 1-2 they would actually test, by number. Two picks should be meaningfully different (different tension, different pattern) so a test teaches something; two variants of one idea as a copy test is fine, note it. Before locking, one last package check per pick, and confirm the video delivers what the text implies. Clickbait is fine only when delivered; otherwise kick it back.

## Step 5: Save, then hand off

Append to `content/pieces/{slug}/piece.md`, never overwriting another skill's fields:

```yaml
thumbnail_text: ["{pick verbatim}"]   # 1-2 locked picks
thumbnail_shape: [{pattern name}]     # same count, same order
```

Bump `last_updated:`. Same write in standalone and pipeline mode; `thumbnail_text` present is the pipeline's done signal. Candidates and rationale stay in chat. Close: picks saved, then point to `vid-structure`, which builds the outline that has to pay the package off.

## Related skills

- `vid-title` runs right before and locks the title this skill pairs against; a strong title candidate that lost there often lives again here
- `vid-structure` runs next and reads the locked package plus the framing fields from piece.md
- `vid-research` produces `packaging-system.md` and the packaging-bank; `vid-pipeline` orchestrates and invokes this skill after `vid-title`
