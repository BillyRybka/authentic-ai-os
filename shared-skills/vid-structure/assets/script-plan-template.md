---
type: skill-asset
skill: vid-structure
purpose: exact shape of script.md on first write
---

# Script Plan Template

The exact shape vid-structure writes to `content/pieces/{slug}/script.md` once the built plan locks. `vid-intro` fills `## Intro`, `vid-segment` writes each body section, `vid-ending` fills `## Ending`. Use this only for a first write. A re-structure with existing prose follows `references/restructure-safety.md`. Do not paste this file into chat.

```markdown
---
type: script
piece: "[[content/pieces/{slug}/piece|{slug}]]"
status: outlined
tier: 1
last_refreshed: {YYYY-MM-DD}
---

# {locked title}

> Tier 1 outline. vid-intro fills ## Intro. vid-segment writes each body section.
> vid-ending fills ## Ending.

## Intro
*vid-intro fills this.*

## {Section heading, material-anchored, in the shape the body plan names}
**Parable:** {type}, [[bank/slug]] or the dump anchor, or to build
- {what happens first}
- {then}
- {the turn, the moment it lands}
**Principle:**
- {the lesson, as the viewer would repeat it}
- {why it is true, or what it costs to ignore}
- {the move}. Proof: [[proof-bank/slug]] or to build

## {next section}
{the fields the body plan names for this section, each with its beats}

## Ending
*vid-ending fills this. CTA per piece.md goal.*

## To build
- [ ] {section} / {block type}: {what is needed} (no bank match)

<!--
CUTS (sticky across re-structure runs):
- {dump anchor}: {reason} [tangent / off-angle / off-format / repeated / merged]
-->
```

## Fields by format

The heading shape and the fields under it come from `references/format-plans/{format}.md`. Parable and Principle are the common pair. Where a format locks different fields, that file shows them and its example is the bar.

| Format | Headings | Fields per section |
|---|---|---|
| step-by-step | `## The parable: {what it shows}`, then `## Step N: {action}` | the parable section carries Parable; each step carries Principle, and Parable only on a hard or doubted step |
| list-video | `## {N}: {point}` | Parable and Principle at every point |
| deep-dive | `## Proof`, `## The parable: {old way, new way}`, then `## Step N: {step}` | the proof block carries Proof; the parable section carries Parable; each step carries Principle with Proof, and Parable where the step earns one |
| success-story | `## The story: {transformation}`, `## The lesson: {one line}` | the story carries Problem, Stakes, Actions, Outcome, Proof; the lesson carries Principle and Steps |
| review | `## Review N: {subject}` | Asset, Problems, Fix, Result |
| interview | `## Q{N}: {question}` | Question, Target story, Target insight, Serves |
| news | `## What happened`, `## Why it matters`, `## What to do` | Facts with sources, then Stakes and POV, then Actions |

## Conventions

- **Headings are material-anchored.** They name the actual step, point, subject, or question in the creator's words.
- **Every field is a label line, then its beats as bullets.** As many as the section needs. A single-line field, like an exact question or an outcome number, stays a line. Never a placeholder bullet, never a field with nothing under it.
- **A field the format does not use in a section is left out.** No `none` lines.
- **Beats are notes to the writer, not script.** The creator's nouns and numbers, in the creator's phrasing, without the throat-clearing.
- **Every `to build` flag gets a row in `## To build`.** An empty list means the script is fully sourced.
- **Cuts live in the HTML comment**, sticky so re-structure runs do not re-propose them.
- **Tension lives once, in piece.md.** No inline setup or payoff notes per section.
- The `piece` link targets the validated piece file, never a bare slug the vault might not resolve.
