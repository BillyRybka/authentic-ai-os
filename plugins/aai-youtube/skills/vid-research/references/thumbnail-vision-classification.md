---
type: reference
scope: skill-local
loaded_by: [vid-research]
status: active
tags: [reference, vid-research, vision, thumbnails]
---

# Thumbnail Vision Classification

Vision prompt template plus the two tag layers vid-research reads off every outlier thumbnail: the strategy (one primary lever, five to choose from, Social Hack as an enhancer on top) and the visual facts (fixed vocabularies, one value per axis). Used in Phase 1, 2, 3 when running vision analysis on confirmed-outlier thumbnails. The third layer, emotional promise, is judged from title plus thumbnail together and lives in `pattern-extraction-prompts.md` as Prompt 6.

**Scope:** every confirmed outlier gets classified; a channel clearing more than ~10 outliers is a prompt to revisit its floor with the creator, not a reason to skip thumbnails. Mode 2 refresh classifies only the new outliers. Mode 3 single-add: 1 call.

**The one rule for tags:** every value must be something two people would label the same way from the image alone. A whiteboard is a whiteboard. "Confident energy" is not a tag and never will be. If a value is not in the vocabulary below, it does not exist; pick the closest listed value or leave a list empty.

## The vision prompt

```
Classify this YouTube outlier thumbnail. Every field takes a value from its fixed vocabulary; never invent a value.

1. Strategy (name ONE primary lever):
   - Cognitive Dissonance: contrarian framing, "wait what?" reaction
   - Result: prominent number, dollar figure, time period, or named outcome
   - Curiosity: implies a secret/mystery without spoiling
   - Before/After: split or paired transformation imagery
   - Minimal: clean composition, leans on title legibility and one strong visual

   A recognizable logo or a tool/brand mark is almost always an enhancer layered on top of a primary lever, not a strategy by itself. Name the primary lever. If none fits, use "Generic / no clear strategy". If several pile up with no leader, use "Stacked / unclear primary".

2. Visual facts (one value each unless marked list; tests in the vocabulary section):
   - hero: face | screenshot | object | whiteboard | logo | text
   - face: none | small | medium | big
   - expression (omit when face is none): neutral | shocked | smile | smirk | excited | defeated
   - gesture (omit when face is none): none | pointing | presenting | shushing | open-hands | thumbs
   - layout: single | split | collage | text-dominant
   - text_amount: none | few | phrase
   - text_style (list, zero or more): caps | handwritten | highlighted | boxed | outlined
   - background: solid | gradient | real | screenshot
   - bg_tone: dark | light
   - devices (list, zero or more): arrow | circle | check-x | number | logo | mockup | money | glow

3. Text content: verbatim text on the thumbnail, or "" if none

4. Hero detail: one line of prose describing the primary visual element (this is the description behind the hero tag)

Channel context:
- Channel: {handle}
- Outlier title: {title}
- Views: {count}

Image: [thumbnail]

Title and thumbnail are one unit. Judge the strategy and the packaging read together with the title. Judge the visual facts from the image alone.

Output format:
strategy: {Cognitive Dissonance | Result | Curiosity | Before/After | Minimal | Generic / no clear strategy | Stacked / unclear primary}
hero: {value}
face: {value}
expression: {value, or omit}
gesture: {value, or omit}
layout: {value}
text_amount: {value}
text_style: [{values}]
background: {value}
bg_tone: {value}
devices: [{values}]
thumbnail_text: "{verbatim}"
hero_detail: {one line}
packaging_read: {one line on how the title and thumbnail work together: reinforce the same promise, set up and pay off, or mismatch}
```

## Layer 1 vocabulary and tests

What is physically in the frame. Fixed vocabularies, no free text. When a value is a judgment call, the test decides.

### hero (single value)

The main thing in the frame. If two compete, the larger one.

| Value | Test |
|---|---|
| `face` | A person is the largest element |
| `screenshot` | A UI, app, browser, terminal, or device screen is the largest element |
| `object` | A physical prop or product is the largest element (a logo held in a hand counts here) |
| `whiteboard` | A diagram, list, or drawing on a board or board-like surface |
| `logo` | A brand mark with no face and no scene around it |
| `text` | Words are the largest element |

### face (single value)

| Value | Test |
|---|---|
| `none` | No person in frame |
| `small` | The face takes under a quarter of the frame |
| `medium` | A quarter to a half |
| `big` | Over half |

### expression (single value, only when face is not none)

| Value | Test |
|---|---|
| `neutral` | Closed or relaxed mouth, level eyes |
| `shocked` | Wide eyes, open mouth, or raised brows |
| `smile` | Teeth or a clear upturn |
| `smirk` | One-sided, knowing |
| `excited` | Big open-mouth grin, often with a gesture |
| `defeated` | Head down, hand on face, eyes closed |

### gesture (single value, only when face is not none)

| Value | Test |
|---|---|
| `none` | Hands not in frame or at rest |
| `pointing` | A finger aimed at something, including up or at the viewer |
| `presenting` | An open palm holding or showing an object |
| `shushing` | Finger to lips |
| `open-hands` | Both hands open, palms up or out |
| `thumbs` | Thumbs up or down |

### layout (single value)

| Value | Test |
|---|---|
| `single` | One subject, one zone |
| `split` | Two zones side by side or stacked, each with its own subject |
| `collage` | Three or more panels or a grid |
| `text-dominant` | The text block takes more area than any image element |

### text_amount (single value)

| Value | Test |
|---|---|
| `none` | No words on the image |
| `few` | One to three words |
| `phrase` | Four or more |

### text_style (list, zero or more)

| Value | Test |
|---|---|
| `caps` | All capitals |
| `handwritten` | A script or marker style face |
| `highlighted` | A colored box behind a word |
| `boxed` | A border around the text |
| `outlined` | A stroke around the letters |

### background (single value)

| Value | Test |
|---|---|
| `solid` | One flat color |
| `gradient` | A blend between colors |
| `real` | A room, outdoors, any photographed environment |
| `screenshot` | A UI or screen fills the back |

### bg_tone (single value)

`dark` | `light`. Judge the majority of the frame.

### devices (list, zero or more)

| Value | Test |
|---|---|
| `arrow` | Any arrow |
| `circle` | A ring or highlight circle drawn on |
| `check-x` | A check mark or an X, including green check beside red X |
| `number` | A standalone figure: a count, a dollar amount, a percentage, a multiplier |
| `logo` | A recognizable brand mark anywhere in frame |
| `mockup` | A phone, browser, or device frame around content |
| `money` | Cash, bills, coins |
| `glow` | A deliberate glow or light effect on an element |

### Not tags

Color palette (nobody filters for "the orange ones"; `bg_tone` covers the decision). Motifs like "OLD vs NEW split" (that is `layout: split` plus two labels; keep tags atomic and let combinations emerge). Anything interpretive about the image: confident, premium, authentic.

## Layer 2: the strategies (five primary levers + Social Hack as an enhancer)

### 1. Cognitive Dissonance

Thumbnail creates "wait, what?" reaction. Image or text contradicts conventional wisdom.

**Visual cues:** contrarian command text (STOP/DON'T/NEVER), reversal text (Why I Quit, I Was Wrong), image showing opposite-of-expected action, surprising contrast.

**Worked example:** "Why I Cut My Squat 20%"
- hero: face, expression: neutral (disappointed, resolute)
- text: "I CUT MY SQUAT 20%"
- The contrarian move (strength coach REDUCING a lift) creates dissonance.

**Anti-pattern:** "STOP" text with no visual or contextual contradiction, that's a Result thumbnail with a warning label, not Dissonance.

### 2. Result

Prominent number, dollar amount, time period, or named outcome.

**Visual cues:** large numerical text ($500K, 10X, 90 DAYS), clear before/after stat, named achievement, authority figure pointing at result.

**Worked example:** "How I Hit $40k in 3 Months"
- hero: face, background: screenshot (revenue dashboard), devices: [number]
- text: "$40K IN 3 MONTHS"
- Dashboard screenshot lends visual proof; dollar figure dominates composition.

### 3. Social Hack (enhancer, not a primary lever)

Leverages well-known person, brand, or recognizable symbol for borrowed authority. A recognizable logo or a tool/brand mark is almost always an enhancer layered on top of a primary lever (Cognitive Dissonance, Result, or Curiosity), not a strategy on its own. Name the primary lever; the borrowed mark shows up as `devices: [logo]`.

**Visual cues:** recognizable face/logo/symbol, side-by-side with known figure, brand juxtaposition.

**Worked example:** split image of well-known fitness creator + creator's own face, text "[Celebrity name]'s WORKOUT (Tested)"
- Borrows audience-recognition from celebrity. Pulls click from both audiences.

**Caution:** overuse triggers audience fatigue. Track frequency, once a month at most.

### 4. Curiosity

Implies a secret or unanswered question. Withholds enough to require the click.

**Visual cues:** vague but evocative text ("THE TRUTH ABOUT", "WHAT NOBODY TELLS YOU"), partially obscured object, pointing gesture toward unseen subject, dramatic expression with no caption explaining why.

**Worked example:** "What Nobody Tells You About Strength Programming"
- hero: face, gesture: none, gaze off-camera
- text: "NOBODY TELLS YOU"
- Off-camera gaze + vague text creates "what is he looking at? what is the secret?" pull.

**Anti-pattern:** Curiosity text with visual that gives the answer away. Once the visual answers the question, the click impulse dies.

### 5. Before/After

Explicit transformation imagery showing change between two states.

**Visual cues:** split-screen comparison, BEFORE/AFTER labels, time-bound progression (Day 1 vs Day 90), visual evidence of change.

**Worked example:** "30 Days of This Workout"
- hero: face, layout: split, lighting deliberately matched
- text: "DAY 1 vs DAY 30" above each side
- Matched lighting makes the transformation legible; no filters or angle tricks; reads as honest.

### 6. Minimal

Clean, simple composition. Leans on title legibility + one strong visual element.

**Visual cues:** lots of negative space, single dominant visual element, title is the dominant text (no overlay caption), limited palette, no clutter.

**Worked example:** "5x5 vs 3x5"
- hero: text, layout: text-dominant, background: solid
- text: "5x5 vs 3x5"
- Extreme minimalism. Title's clarity carries the click.

**Caution:** works for sophisticated audiences who skim by title. Fails for general audiences who need visual stimulation to click.

## Anti-pattern flags (classify but don't bank)

When vision surfaces these, flag rather than auto-classify:

- **Polished but generic**, face + smile + bold text saying "MY BEST TIPS." No specific hook. Classify as `strategy: Generic / no clear strategy` and flag. Shows up in flop analysis, not pattern extraction. Layer 1 tags still get filled; the facts are still facts.
- **Strategy stack**, multiple levers piled with no clear primary (celebrity + dollar figure + before/after + curiosity text). Levers dilute the click. If one lever clearly leads, name it. If none leads, classify as `strategy: Stacked / unclear primary` and flag.
- **Mismatch with title's promise**, title is Curiosity ("What Nobody Tells You") but thumbnail is Result ($500K). Title and thumbnail should reinforce, not compete. Flag misalignment in the packaging read.

## Signal weighting

- **High signal:** strategy convergent across 3+ channels in the niche set
- **Medium signal:** strategy appears in 2 niche channels + 1+ adjacent channel
- **Low signal:** strategy appears on one channel only, could be creator quirk
- **No signal:** anti-pattern flag, surface but don't recommend

## Common mistakes

- **Forcing one of the levers when none fit.** Generic thumbnails happen. Classify as Generic and flag.
- **Confusing Curiosity with Cognitive Dissonance.** Curiosity withholds. Dissonance contradicts. "What nobody tells you" is Curiosity. "Stop doing this" is Dissonance.
- **Inventing a tag value.** If the image has a prop that is not in the `devices` list, it is not a device. Describe it in `hero_detail` prose instead.
- **Tagging from the title.** Layer 1 is the image alone. A title that says "$10K" does not put `number` in `devices` unless the figure is on the thumbnail.
- **Hallucinating thumbnail content from the title alone.** If vision is unavailable (download failed, file corrupted), mark `vision: unavailable`, don't invent.
