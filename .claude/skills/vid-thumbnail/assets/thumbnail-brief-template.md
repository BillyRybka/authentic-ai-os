---
type: thumbnail-brief
project: youtube-content-os
piece: "[[{slug}]]"
title_paired: "{exact title this thumbnail pairs with}"
strategies_tested: [strategy-slug, strategy-slug]
picks: 2
captured: YYYY-MM-DD
status: brief-ready
tags: [thumbnail, brief, strategy-{slug}]
---

# Thumbnail brief — {piece slug}

## Title this pairs with

> **{Exact title}**

## Text options generated (Phase 1)

1. "TEXT OPTION 1"            — pattern, BENS letters
2. "TEXT OPTION 2"            — pattern, BENS letters
3. "TEXT OPTION 3"            — pattern, BENS letters
...

## Picks

### Pick A — "{Text}"

- **Strategy:** {strategy-name}
- **BENS letters hit:** {letters}
- **Why it lands:** {one sentence — what gap does the text create, what proof does it offer?}

### Pick B — "{Text}"

- **Strategy:** {strategy-name}
- **BENS letters hit:** {letters}
- **Why it lands:** {one sentence}

## Title-pairing checks

- [ ] Title under 50 characters
- [ ] Title hits at least one BENS letter
- [ ] Each pick follows its committed strategy
- [ ] Thumbnail text ≤ 5 words (or pure number-hero)
- [ ] Thumbnail and title carry DIFFERENT curiosity hooks (no word repeats unless flagged exception)
- [ ] Tonal pairing — thumbnail tone matches or productively contrasts title tone
- [ ] Clickbait test — the script delivers what each thumbnail implies. If not, kick back.

## Notes

*Anything the creator should know — borderline title-overlap exception flagged, no past winners in packaging-bank yet, etc.*

- {note}

## Related

- Video piece: [[Content/pieces/{slug}]]
- Creator packaging system: [[foundation/packaging-system]]
- Past winners pulled from: [[banks/packaging-bank]]

## Next step (creator-driven)

The creator takes these picks and designs the actual thumbnail using their committed creation path (Photoshop / AI workflow / batch photos / outsource) per `foundation/packaging-system.md`. This skill does NOT design the visual — it produces the locked text + rationale and stops.

For automated image generation: the future `vid-thumbnail-gen` skill takes a brief like this one + the creator's packaging-system guardrails + their AI tool config and produces the actual images.

## After publishing

If either pick wins (outperforms channel baseline for CTR / retention through hook), create an entry in `banks/packaging-bank/{slug}.md` with the performance data, the thumbnail asset, and this thumbnail text as reference for future packages.
