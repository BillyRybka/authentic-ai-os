---
type: reference
scope: skill-local
loaded_by: [vid-research]
status: active
tags: [reference, vid-research, vision, thumbnails]
---

# Thumbnail Vision Classification

Vision prompt template + the thumbnail strategies vid-research classifies outlier thumbnails into (five primary levers, with Social Hack as an enhancer layered on top). Used in Phase 1, 2, 3 when running vision analysis on confirmed-outlier thumbnails.

**Budget:** ~50 vision calls per full session (top 10 own + 25 across niche + 15 across adjacent). Mode 2 refresh ~15-25 calls. Mode 3 single-add: 1 call.

## The vision prompt

```
Classify this YouTube outlier thumbnail. Extract:

1. Primary lever (name ONE):
   - Cognitive Dissonance: contrarian framing, "wait what?" reaction
   - Result: prominent number, dollar figure, time period, or named outcome
   - Curiosity: implies a secret/mystery without spoiling
   - Before/After: split or paired transformation imagery
   - Minimal: clean composition, leans on title legibility and one strong visual

   A recognizable logo or a tool/brand mark is almost always an ENHANCER layered on top of a primary lever (Cognitive Dissonance, Result, or Curiosity), not a strategy by itself. Name the primary lever first.

   Enhancers (list any that apply, after the primary lever): logo or brand mark, a number, an expression. A well-known person or symbol borrowing authority is an enhancer, not the primary lever.

2. Hero element: face/expression, screenshot/UI, object/prop, text-only, infographic, comparison split, other

3. Color palette: 2-3 dominant colors

4. Text content: verbatim text on the thumbnail

5. Text positioning: top/middle/bottom + left/center/right

6. Expression (if face present): expression + gaze direction

7. Notes: distinctive details (props, lighting, post-production effects)

Channel context:
- Channel: {handle}
- Outlier title: {title}
- Views: {count}

Image: [thumbnail]

Title and thumbnail are one unit. Judge the thumbnail together with its title, never in isolation.

Output format:
Primary lever: {Cognitive Dissonance, Result, Curiosity, Before/After, or Minimal}
Enhancers: {logo or brand, a number, an expression; or none}
Hero element: {description}
Color palette: {colors}
Text content: "{verbatim}"
Text positioning: {position}
Expression: {if present}
Packaging read: {one line on how the title and thumbnail work together: reinforce the same promise, set up and pay off, or mismatch}
Notes: {distinctive details}
```

## The strategies (five primary levers + Social Hack as an enhancer)

### 1. Cognitive Dissonance

Thumbnail creates "wait, what?" reaction. Image or text contradicts conventional wisdom.

**Visual cues:** contrarian command text (STOP/DON'T/NEVER), reversal text (Why I Quit, I Was Wrong), image showing opposite-of-expected action, surprising contrast.

**Worked example:** "Why I Cut My Squat 20%"
- Hero: face with disappointed/resolute expression
- Palette: navy, yellow, white
- Text: "I CUT MY SQUAT 20%"
- The contrarian move (strength coach REDUCING a lift) creates dissonance.

**Anti-pattern:** "STOP" text with no visual or contextual contradiction, that's a Result thumbnail with a warning label, not Dissonance.

### 2. Result

Prominent number, dollar amount, time period, or named outcome.

**Visual cues:** large numerical text ($500K, 10X, 90 DAYS), clear before/after stat, named achievement, authority figure pointing at result.

**Worked example:** "How I Hit $40k in 3 Months"
- Hero: face + revenue dashboard screenshot
- Palette: green, white, dark gray
- Text: "$40K IN 3 MONTHS"
- Dashboard screenshot lends visual proof; dollar figure dominates composition.

### 3. Social Hack (enhancer, not a primary lever)

Leverages well-known person, brand, or recognizable symbol for borrowed authority. A recognizable logo or a tool/brand mark is almost always an enhancer layered on top of a primary lever (Cognitive Dissonance, Result, or Curiosity), not a strategy on its own. Name the primary lever first, then note this as an enhancer.

**Visual cues:** recognizable face/logo/symbol, side-by-side with known figure, brand juxtaposition.

**Worked example:** split image of well-known fitness creator + creator's own face, text "[Celebrity name]'s WORKOUT (Tested)"
- Borrows audience-recognition from celebrity. Pulls click from both audiences.

**Caution:** overuse triggers audience fatigue. Track frequency, once a month at most.

### 4. Curiosity

Implies a secret or unanswered question. Withholds enough to require the click.

**Visual cues:** vague but evocative text ("THE TRUTH ABOUT", "WHAT NOBODY TELLS YOU"), partially obscured object, pointing gesture toward unseen subject, dramatic expression with no caption explaining why.

**Worked example:** "What Nobody Tells You About Strength Programming"
- Hero: face looking off-camera
- Palette: muted gray, single accent
- Text: "NOBODY TELLS YOU"
- Off-camera gaze + vague text creates "what is he looking at? what is the secret?" pull.

**Anti-pattern:** Curiosity text with visual that gives the answer away. Once the visual answers the question, the click impulse dies.

### 5. Before/After

Explicit transformation imagery showing change between two states.

**Visual cues:** split-screen comparison, BEFORE/AFTER labels, time-bound progression (Day 1 vs Day 90), visual evidence of change.

**Worked example:** "30 Days of This Workout"
- Hero: split-screen body shot, lighting deliberately matched
- Text: "DAY 1 vs DAY 30" above each side
- Matched lighting makes the transformation legible; no filters or angle tricks; reads as honest.

### 6. Minimal

Clean, simple composition. Leans on title legibility + one strong visual element.

**Visual cues:** lots of negative space, single dominant visual element, title is the dominant text (no overlay caption), limited palette (often 2 colors + black/white), no clutter.

**Worked example:** "5x5 vs 3x5"
- Hero: large bold "5x5" and "3x5" with vs between
- Palette: black, white, single red accent
- Extreme minimalism. Title's clarity carries the click.

**Caution:** works for sophisticated audiences who skim by title. Fails for general audiences who need visual stimulation to click.

## Anti-pattern flags (classify but don't bank)

When vision surfaces these, flag rather than auto-classify:

- **Polished but generic**, face + smile + bold text saying "MY BEST TIPS." No specific hook. Classify as `Strategy: Generic / no clear strategy` and flag. Shows up in flop analysis, not pattern extraction.
- **Strategy stack**, multiple levers piled with no clear primary (celebrity + dollar figure + before/after + curiosity text). Levers dilute the click. If one lever clearly leads, name it as the primary and list the rest as enhancers. If none leads, classify as `Primary lever: Stacked / unclear primary` and flag.
- **Mismatch with title's promise**, title is Curiosity ("What Nobody Tells You") but thumbnail is Result ($500K). Title and thumbnail should reinforce, not compete. Flag misalignment.

## Signal weighting

- **High signal:** strategy convergent across 3+ channels in the niche set
- **Medium signal:** strategy appears in 2 niche channels + 1+ adjacent channel
- **Low signal:** strategy appears on one channel only, could be creator quirk
- **No signal:** anti-pattern flag, surface but don't recommend

## Common mistakes

- **Classifying every thumbnail.** Respect the prioritization (top 10 own / top 5 niche / top 3 adjacent). Lower-tier outliers get URL-saved without vision analysis.
- **Forcing one of the levers when none fit.** Generic thumbnails happen. Classify as Generic and flag.
- **Confusing Curiosity with Cognitive Dissonance.** Curiosity withholds. Dissonance contradicts. "What nobody tells you" is Curiosity. "Stop doing this" is Dissonance.
- **Hallucinating thumbnail content from the title alone.** If vision is unavailable (download failed, file corrupted), mark `vision: unavailable`, don't invent.
