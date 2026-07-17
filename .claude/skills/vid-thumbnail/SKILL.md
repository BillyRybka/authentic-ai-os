---
name: vid-thumbnail
description: Generate thumbnail TEXT options for one video and lock 1-2 picks with the creator. TEXT planner only, it does NOT design the visual (no layouts, hero choices, expressions, color, or AI prompts). Writes the locked picks into the video's piece.md. Use when the title is locked and you are packaging the video, or when the creator says "let's do the thumbnail text", "thumbnail options for [video]", "thumbnail copy", or a pipeline invokes it right after vid-title.
---

# Video Thumbnail Text Planner

Title and thumbnail are ONE package. Typically the title comes first, and this skill writes the other half. Three moves: read the title, mine the video's most compelling material for what complements it, shape that into text options. The creator picks 1-2, the picks save to piece.md.

**Scope: text only.** Layout, hero element, expression, color, and AI image prompts are out of scope. Do not drift into designing the visual.

**This is a conversation, not a document.** Short messages. References are for your thinking; never paste them at the creator. They scan options and pick.

## What loads, and when

Load each file at the step that needs it. Do not front-load.

| Step | Load | For |
|---|---|---|
| 1. Title + mine | `content/pieces/{slug}/piece.md` | the title (the anchor), format, goal |
| 1. Title + mine | `content/pieces/{slug}/script.md` IF it exists and is complete, ELSE `brain-dump.md` | the material. The script wins when it exists; don't read the brain dump if a finished script supersedes it |
| 2. Shape | `knowledge/thumbnail-text-patterns.md` | the 5 text patterns, anti-patterns, title-pairing rules, examples library, BENS lens. The one craft reference |
| 2. Shape | `foundation/packaging-system.md` IF it exists | the channel's packaging SETTINGS (written by vid-research): the thumbnail strategy currently being tested, casing preference |
| 2. Shape | `banks/packaging-bank/*.md` IF entries exist | packaging RECEIPTS: title+thumbnail combos that already won. Holds the creator's own winners AND studied outliers from other channels; each entry's `source` field says which |
| 3-5 | nothing | filter, pick, and save load no files |

No hard dependency on `packaging-system.md`. A fresh creator makes a thumbnail on day one: defaults are ALL CAPS and no strategy constraint. When the file exists, honor it.

Prerequisite: a `title` in piece.md. Text can't pair against a title that doesn't exist, so if there is none yet, run `vid-title` first.

## Step 1: Read the title, then mine for its partner

Read the title FIRST. Name to yourself what hook it carries (the question it plants) and its tone: failure, success, mystery, contrarian, instructive, news. Everything generated next must work WITH this title as one package: the thumbnail adds a second, different hook, it never repeats the title's.

Open with one short line to the creator: name the title, say you're pulling the strongest material to pair with it.

Then mine the script (or brain dump) for the most compelling assets the video actually contains, looking specifically for what the title does NOT already say:

- verbatim numbers, dollar figures, percentages, timeframes (these are also the **lock list**: candidates may use ONLY numbers that appear here, nothing invented)
- belief-clashes and paradoxes the video argues
- named systems, rules, methods
- the single most dramatic moment or claim

## Step 2: Shape into candidates

Load `knowledge/thumbnail-text-patterns.md` and shape the mined assets into candidates. **Generate against the title, never in a vacuum:** write the title at the top of your working space and draft every candidate directly beneath it, reading each one as "title + this text, seen together in one glance." If the pair reads as the same beat twice, the candidate is dead on arrival.

Generate wide privately; count doesn't matter, strength does. The creator only ever sees the survivors of Step 3. For each candidate, know WHY it makes someone click before it earns a spot.

**One point is enough.** A candidate doesn't summarize the video or carry the whole format's stakes. In a listicle, one contrarian point or one dramatic claim can be the entire thumbnail, IF it hits emotionally on its own. Strength beats coverage, always. Generate from THIS video's material, calibrated by the patterns file, not by inventing generic thumbnail lines.

The patterns are lenses, not cages. If the material begs for a text that fits none of the 5, keep it, show it, and say why it works. Never kill a compelling option because it lacks a label.

If packaging-system names a current strategy test, bias part of the set toward it and mark which candidates serve the test. If the packaging-bank has winners, echo what already worked for this creator over generic best practice.

## Step 3: Filter hard, then show

Only the strongest 3-5 survive, ranked, strongest first. If only two are strong, show two. Never pad the list with a candidate you already know is weak, and never show one while flagging its own weakness; a candidate with a known flaw gets cut, not caveated.

Reject before the creator ever sees:

1. **Fabrication.** Any number not on the lock list.
2. **Spoiler.** If the text alone gives away the video's central insight, it kills the click. The thumbnail makes them want to know; it doesn't tell them.
3. **Package break.** Repeats the title's key words (parentheticals count), or its tone fights the title instead of matching or productively contrasting. One package, two hooks.
4. **Generic.** Text that would fit 100 other videos in the niche. It must signal THIS story.
5. **Anti-pattern.** Per the patterns file: visual-metaphor words, vague paradoxes, hedges, stock phrases.

**Length:** 2-4 words preferred, 5 is the ceiling, 6+ auto-rejects. One high-curiosity word is valid. A pure number or arc counts as one unit, never rejected on word count. **Casing:** ALL CAPS unless the creator's guardrails say otherwise.

Show the package, not a list in a vacuum: the title on the first line, then the numbered candidates beneath it, so the creator reads each one the way a viewer would, next to the title. Each line is the text in quotes plus its pattern name, nothing else. No rationale paragraphs, no self-grading (no "serves the strategy test" tags). They scan and pick.

**Kill criteria.** If after one full regeneration the options are still weak, the problem is upstream: the title is too vague or the material lacks the specific number or moment thumbnails need. Say so and stop. Don't grind weak text from a thin source.

## Step 4: Pick

Ask which 1-2 the creator would actually test, by number. If they pick two, push for meaningfully different ones (different tension, different pattern) so a test teaches something. If they want two variants of one idea as a copy test, fine, note it.

Before locking, check each pick one last time as a package against the pairing rules in the patterns file, and confirm the video actually delivers what the text implies. Clickbait is fine only if delivered; if it isn't, kick it back.

## Step 5: Save

Append to `content/pieces/{slug}/piece.md` (never overwrite another skill's fields):

```yaml
thumbnail_text: ["{pick verbatim}"]   # 1-2 locked picks
thumbnail_shape: [{pattern name}]     # same order as the picks
```

Bump `last_updated:`. This write happens in BOTH standalone and pipeline mode; `thumbnail_text` present is how the pipeline knows this step is done. Candidates and rationale stay in chat; piece.md holds only the locked picks.

Close with one line: picks saved.
