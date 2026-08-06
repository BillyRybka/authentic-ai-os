---
type: reference
scope: skill-local
loaded_by: [post-write]
status: active
tags: [reference, post-write, template, post-note]
---

# Post Note Template

The shape of every saved post. One note per idea at `content/pieces/{slug}/posts/{idea-slug}.md`. Each note holds the platform-agnostic core piece plus an adaptation for every platform the creator asked for.

The split is the whole point: **frontmatter and the provenance block carry wikilinks for the graph; the `## Publishable` blocks are clean copy that leaves the vault.** Every publishable body has no wikilinks, no markdown internal links, and no em-dashes, so the creator can paste it straight to the platform.

## Frontmatter

```yaml
---
type: post
project: authentic-ai-os
piece: "[[{parent-slug}]]"        # the source: a video piece, a script, or the batch's own piece folder
post_type: mistake               # mistake | story | framework | checklist | contrarian | warning | comparison | do-this-not-that
platforms: [linkedin, instagram-carousel]   # which platforms the core was adapted to: any of linkedin, instagram-carousel, instagram-caption
pillar: {pillar-slug}            # from the creator's content pillars
problem_addressed: 1             # 1 | 2 | 3 | outlier_within_iceberg
iceberg_aligned: true
hook_type: contrarian            # the core's opening move: contrarian | observation | story | diagnostic | rule | tension | command | comparison | question
status: draft                    # draft | approved | published
captured: YYYY-MM-DD
published: null
source_unit: "the exact phrase or claim from the source this came from"
tags: [post, type-{post-type}, pillar-{pillar-slug}, problem-{n}]
---
```

## Body

```markdown
# {short internal label for this idea, not the hook}

## Core (platform-agnostic)

{The standalone core piece. The idea fully expressed in the post-type's shape, in the creator's voice. Clean copy: no wikilinks, no markdown links, no em-dashes. Every platform version below is adapted from this.}

## Publishable: LinkedIn

{The LinkedIn adaptation. Hook-first, short paragraphs, line breaks intact. Clean copy. Delete this block if LinkedIn was not requested.}

## Publishable: Instagram carousel

Slide 1 (title): {hook}
Slide 2: {one point}
Slide 3: {one point}
Slide 4: {one point}
Recap slide: {the takeaway compressed}
Caption: {the caption that expands the idea and holds the CTA}

### Visual brief

{One short line per slide: layout, what to emphasize, any imagery or icon idea, design notes. Text only, no rendering. Delete the carousel block and this brief if a carousel was not requested.}

## Publishable: Instagram caption

{The caption adaptation: warmer, single thread. Clean copy. Delete this block if a caption was not requested.}

## Provenance

- Source: [[{parent-slug}]]
- Post-type: {post_type} | Platforms: {platforms} | Hook: {hook_type}
- Fit: [[avatar#Top 3 perceived problems|problem {n}]], {clean fit | outlier within iceberg}
- Source unit: "{the exact phrase this was built from}"
- Drew on: {any bank entries used, in the vault convention: [[story-bank/slug]], [[metaphor-bank/slug]], [[proof-bank/slug]]. No "banks/" prefix. People as [[Full Name]], never [[people/Full Name]]. Cite only entries that exist; if a person is named, create the people stub.}
```

## Notes

- Provenance wikilinks are allowed here because this block stays in the vault. They never appear in any `## Publishable` block.
- Cite bank entries and people in the vault convention: `[[bank-dir/slug]]` (no "banks/" prefix) and `[[Full Name]]` (no "people/" prefix). A wrong-format link breaks the graph and reads as a fabricated link to anything checking it.
- Include only the platform blocks the creator asked for. Delete the rest. The `## Core` block is always present.
- Carousel slides are billboards: one idea each, 30 words max, two short sentences ceiling. Decompose the core into beats per `references/carousel.md`, never slice it at the paragraph breaks. If the idea is a single story or one belief, it is a caption, not a carousel.
- The note wikilinks its parent via `piece:`. Obsidian's backlink pane surfaces it on the parent, so the graph connects without leaking links into the copy.
- For a standalone batch with no parent video, the skill creates a lightweight piece folder for the batch, and `piece:` points at that batch's own `piece.md`.
- `hook_type` records the core's opening move so the batch-level hook-variety check (Phase 5) can scan for repeated openers.
