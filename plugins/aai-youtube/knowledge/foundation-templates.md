# Foundation file templates

The creator's foundation lives in five focused files under `foundation/`, one concern per file, so skills load only the slice they need. Each file below has one owning skill. A skill creates its file from the matching template the first time it saves; sections not yet built keep their `[pending {skill-name}]` marker.

| File | Built by |
|---|---|
| `foundation/offer.md` | `vid-avatar` (Phase 1) |
| `foundation/avatar.md` | `vid-avatar` (Phases 2 and 3) |
| `foundation/iceberg.md` | `vid-positioning` (statement + machinery), `vid-pillars` (content pillars) |
| `foundation/credibility.md` | `vid-credibility` |
| `foundation/backstory.md` | `vid-backstory` |

Vaults that still hold a single `foundation/creator-foundation.md` migrate via `knowledge/foundation-migration.md`.

Set `date` when the file is created and bump `last_refreshed` on every save. One exception: a migration carve (see `knowledge/foundation-migration.md`) carries the old file's `last_refreshed` forward, since the content moved without changing.

---

## `foundation/offer.md`

```markdown
---
type: foundation
doc: offer
project: authentic-ai-os
status: active
date: YYYY-MM-DD
last_refreshed: YYYY-MM-DD
tags: [foundation, offer]
---

# Offer

*What the creator currently sells or plans to sell. One paragraph. The result the buyer walks away with.*

> [pending vid-avatar]
```

---

## `foundation/avatar.md`

```markdown
---
type: foundation
doc: avatar
project: authentic-ai-os
status: active
date: YYYY-MM-DD
last_refreshed: YYYY-MM-DD
tags: [foundation, avatar]
---

# Avatar

*Who this is for. A description, not a structured field list. A few sentences. Enough that the packaging and writing skills can write to a recognizable person.*

> [pending vid-avatar]

## Top 3 perceived problems

*What the avatar says when they complain. In their language, not the expert's. Three distinct domains.*

1. [pending vid-avatar]
2. [pending vid-avatar]
3. [pending vid-avatar]
```

---

## `foundation/iceberg.md`

```markdown
---
type: foundation
doc: iceberg
project: authentic-ai-os
status: active
date: YYYY-MM-DD
last_refreshed: YYYY-MM-DD
tags: [foundation, iceberg, positioning, pillars]
---

# Iceberg Statement

*One sentence. The channel's promise. Contains WHO + WHAT + HOW + TENSION.*

> [pending vid-positioning]

## Optional longer version

*Use only if it surfaced naturally during the interview. Leave this section empty otherwise.*

## Machinery

*The four components broken out, in the creator's words.*

- **Who:** [pending vid-positioning]
- **How:** [pending vid-positioning]
- **What:** [pending vid-positioning]
- **Tension:** [pending vid-positioning]

## Content notes

*Optional, creator-grown. Standing notes on how the promise should show up in content. Empty until the creator adds them.*

## Content pillars (bottom of the iceberg)

*8 to 12 subtopics the creator can teach that deliver on the Iceberg Statement. Categories of teaching, not video titles. This list grows with experience.*

1. [pending vid-pillars]
2. [pending vid-pillars]
3. [pending vid-pillars]
4. [pending vid-pillars]
5. [pending vid-pillars]
6. [pending vid-pillars]
7. [pending vid-pillars]
8. [pending vid-pillars]

*Add more (target 8-12 minimum). Refine as published videos surface what real viewers respond to.*
```

---

## `foundation/credibility.md`

```markdown
---
type: foundation
doc: credibility
project: authentic-ai-os
status: active
date: YYYY-MM-DD
last_refreshed: YYYY-MM-DD
tags: [foundation, credibility]
---

# Credibility brags

*3 viewer-relevant wins. One sentence each. Specific numbers where possible. Never anti-proof.*

1. [pending vid-credibility]
2. [pending vid-credibility]
3. [pending vid-credibility]
```

---

## `foundation/backstory.md`

```markdown
---
type: foundation
doc: backstory
project: authentic-ai-os
status: active
date: YYYY-MM-DD
last_refreshed: YYYY-MM-DD
tags: [foundation, backstory]
---

# Backstory

*Problem, Action, Outcome. 1-2 short paragraphs. Conversational tone. If the creator never had the viewer's problem, use a real client's backstory with clear attribution.*

> [pending vid-backstory]

## 3-sentence compressed version

*For quick intros.*

> [pending vid-backstory]
```

---

## Notes

- This is a minimum viable foundation. Expect to refine after 3-4 videos of data.
- Any major Iceberg Statement shift means re-running `vid-positioning`.
- The content pillars list grows continuously. Add as the channel evolves.
