## Output: piece.md

The per-piece identity ledger. vid-intake creates it the moment the topic is known; every downstream skill appends its own fields and never overwrites another's.

```yaml
---
type: content-piece
project: authentic-ai-os
slug: {kebab-case-slug}
pillar: {pillar-slug or null}
status: ideating
created: YYYY-MM-DD       # today, stamped once, never changed
last_updated: YYYY-MM-DD  # today; every skill that writes piece.md bumps this
anchor: "{Only when vid-ideas handed a picked seed: the full outlier receipt, source title + @channel + views + xMed. Omit otherwise.}"
tags: [piece, pillar-{slug}]
---
```
