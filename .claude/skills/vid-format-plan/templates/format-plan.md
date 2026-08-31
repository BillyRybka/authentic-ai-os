---
type: format-plan
project: authentic-ai-os
slug: {kebab-case-slug}
format: {format-slug}
goal: {sales | emails | views}
status: planning
created: {YYYY-MM-DD}
last_updated: {YYYY-MM-DD}
tags: [format-plan, format-{format-slug}]
---

# {The working title, or the creator's one line when there is no title yet}

## The video

{The creator's one line, in their words.}

## {N}. {Blank name, from the card, in card order}

> [!todo] Empty
> {The short form of the ask, so the file reads on its own.}

## {N}. {A blank that has been filled}

{Their answer. Their nouns, their numbers, their phrasing.}

## {N}. {A blank that came back thin twice, or got skipped}

> [!warning] Gap: {what is missing, in four words}
> {Why the video needs it. One sentence, from the planner.}

## Body {N}: {segment name, from the card}

### {N}. {Blank name}

> [!todo] Empty
> {The ask.}

---

## Notes for whoever writes this file. Do not copy anything below this line.

**Three states, one per section.** A `> [!todo] Empty` callout, the creator's answer as plain prose, or a `> [!warning] Gap:` callout. The callout is the status marker. Nothing else records state and nothing else needs to.

**The empty markers are the resume handle.** One left means the session was cut short and can be walked back into. None left means the plan closed. That holds because the file is written after every single answer rather than at an exit, and the sessions that need resuming are the ones that never got an exit.

**Section order comes from the card, not from here.** The card is per format and its order is the order the video plays: package, intro, body, close, upload. A body segment heading carries its blanks as H3s and no marker of its own.

**Repeating blanks get numbered sub-sections.** A card blank marked `Repeats` becomes `### 9.1`, `### 9.2`, one per point, step, review, or question, written the moment the counting blank fills. Before that it is one container section holding an empty marker that says what is coming. The plan file never shows a repeating section for an item that does not exist yet.

**Numbers on the headings are the count the creator hears** in the progress line. They come from the card and do not get renumbered mid-session.

**`goal` in frontmatter is the goal blank.** It sits in two places on purpose, once where a skill can read it and once where the creator does.

**Names are plain text.** A wikilink goes in only when its target is already on disk.

**No summary section, ever.** No "what I'm hearing", no themes, no recap block. The blanks are the plan. A summary above them becomes the thing that gets read instead of the plan.
