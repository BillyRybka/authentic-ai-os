---
type: testimonial
project: authentic-ai-os
source: dm
illustrates: the system kept running after the client stepped back
themes: [delegation, systems]
client: "[[Client Name]]"
anonymized: false
captured: YYYY-MM-DD
status: captured
tags: [testimonial, source-dm, delegation, systems]
used_in: []
---

# {Testimonial slug, client + topic}

> [!quote] {Client name or "Anonymous"}, {source} {date}
> {Verbatim quote, preserved exactly, including typos or casual phrasing.}

## Context

{What the client was responding to. Which video, offer, or moment triggered this testimonial. Link to the piece with a wikilink if it exists in `content/pieces/`.}

## Anonymization

{Applied / Not applied / Permission granted for full name / Permission granted for first name only}

## Notes

- Captured: {date}
- Source: {wikilink to Client's People profile if named, plus platform: comment, dm, email, or video}
- Related: {optional wikilinks to related stories or proof}

---

## Filling instructions (delete this section before save)

**Frontmatter fields:**

- `source`: one of `comment`, `dm`, `email`, `video`
- `illustrates`: one short line for the point this quote backs, plain cause and effect, in the creator's voice. Unquoted unless a colon forces quotes.
- `themes`: open list of the angles this quote backs (e.g., `delegation`, `systems`). Multi-value.
- `client`: wikilink to `people/{Full Name}.md` if named with permission. Otherwise "Anonymous".
- `anonymized`: `true` if identifying details were removed, `false` if using real name with permission
- `captured`: ISO date
- `status`: starts `captured`
- `tags`: at minimum `testimonial` and `source-{slug}` (e.g., `source-dm`, `source-comment`), plus the theme slugs.
- `used_in`: starts `[]`

**Body rules:**

- The `> [!quote]` callout is the headline. Verbatim text only. No paraphrasing, no grammar cleanup, no emoji removal unless the creator specifically needs it.
- Preserve typos, casual phrasing, and profanity exactly as written.
- Context section: what was the client responding to? Link to the triggering piece if available.
- Anonymization section: state the permission status clearly. Default to "Applied" when in doubt.

**Client mention rule:** if the client is named with permission, check `people/{Full Name}.md`. If missing, create via `people-stub-template.md`. Then write `client: "[[Full Name]]"` in frontmatter.

**Scope note:** vid-bank saves testimonials that already exist (comments, DMs, emails, videos the creator already received). Soliciting new testimonials is out of scope for this skill.
