---
type: story
project: youtube-content-os
story_type: client
problem_illustrated: general
client: "[[Client Name]]"
captured: YYYY-MM-DD
status: captured
tags: [story, problem-general]
used_in: []
---

# {Story title, short and descriptive}

## Problem

{1 to 3 sentences in creator's voice. Specific. Emotional. Drop the viewer into the worst moment, not the beginning of the journey.}

## Action

{Concrete moves. Verbs. 1 to 3 sentences max. The one thing that started solving the problem, not everything.}

## Outcome

{Specific result. Numbers where possible. Connect back to the problem. Twist endings are gold.}

> [!tip] Why this story lands
> {1 to 2 sentences on the specific detail, the unexpected turn, or the emotional beat that makes it work.}

## Notes

- Captured: {date}
- Source: {how it was captured, e.g., conversation, past video, client email, voice memo}
- Related: {optional wikilinks to related stories, metaphors, or proofs}

---

## Filling instructions (delete this section before save)

**Frontmatter fields:**

- `story_type`: one of `client`, `own`, `viewer`
- `problem_illustrated`: one of `1`, `2`, `3`, `general` (maps to top 3 problems in creator-foundation.md)
- `client`: wikilink to `People/{Full Name}.md`. Only present for client stories. Remove the line entirely for own stories or viewer stories.
- `captured`: ISO date YYYY-MM-DD
- `status`: starts `captured`. Writing skills change to `used` when first consumed.
- `tags`: at minimum `story` and `problem-{n}` or `problem-general`. Add theme slugs as applicable (e.g., `pricing`, `positioning`, `delegation`).
- `used_in`: starts `[]`. Writing skills populate with `[[piece-slug]]` wikilinks.

**Body rules:**

- Preserve the creator's exact phrasing. Do NOT polish.
- 20 to 30 seconds when read aloud. Trim if longer.
- Problem: specific, vivid, 1 to 2 sentences.
- Action: one key move. Three max.
- Outcome: specific numbers, timeline, or transformation.
- `> [!tip] Why this story lands` is a required callout.
- Notes section captures meta: when, how, what it connects to.

**Client mention rule:** if the creator names a client by full name, check `People/{Full Name}.md`. If missing, create it using `people-stub-template.md`. Then write `client: "[[Full Name]]"` in frontmatter and `[[Full Name]]` at first body mention.
