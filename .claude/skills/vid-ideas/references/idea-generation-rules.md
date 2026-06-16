# Idea generation rules

Runtime logic for `vid-ideas` Phase 2 (generate) and Phase 3 (the dial). Not chat content. This is how Claude turns positioning plus evidence into a batch that is sharp, on-channel, and not crappy.

## The raw material

Every idea is built from a cross of three things already loaded:
- A **pillar** (the teaching territory, from the creator's 8-12 pillars)
- A **Top 3 problem** (what the avatar actually complains about, in their words)
- A **signal** (a pattern, outlier, or confirmed winner from `pattern-bank.md` that proves a shape works)

An idea is a pillar's territory, aimed at one avatar problem, wearing the shape of a proven signal, said in the creator's voice. Miss any of the three and it drifts: no pillar means off-positioning, no problem means content-only filler, no signal means a guess.

## The generative move: anchor, then adjust

This is the heart of the skill, and it is not "invent a topic." It is Ed Lawrence's actual ideation mechanic: take a proven shape and bend it onto the one specific thing this avatar wants.

1. **Anchor.** Pick a real signal from the pattern-bank (a pattern, an outlier, a confirmed winner). Never start from a blank guess. No anchor means it does not get surfaced (guard 1).
2. **Adjust.** Translate that shape onto a pillar AND the avatar's specific named want, not a generic problem. Ed picks "Drumming MISTAKES That KILL Your Progress" and bends it to "...That Kill Your Hand Speed" because that audience cares about speed. The signal supplies the shape; the avatar supplies the substance.

The adjustment IS the idea. A pattern handed back with the nouns swapped is not an idea (guard 2). A pattern bent onto what the avatar actually wants from THIS creator is.

## Signal tiers (what counts as "proven")

Read the anchor's strength from the pattern-bank fields (same logic `vid-framing` uses in `references/angle-anchor-rules.md`):

- **STRONG:** `own_channel_proven: true` (the creator already won with this shape), OR `spread` >= 5 channels, OR a Confirmed winner row. Highest-confidence anchors. Lead with these.
- **MODERATE:** `spread` of 3-4 channels, not own-channel-proven. Real cross-channel signal, lower certainty.
- **WEAK:** `spread` of 1-2 channels. Do not surface as an anchored idea. If a weak pattern is interesting, it becomes an experimental swing (flagged unproven), not a proven anchor.
- **EXPERIMENTAL SWING:** no anchor. The creator's pillar material that does not map to a proven pattern, a contrarian take, or an adjacent-niche shape transferred in. Always flagged `experimental swing (no anchor, unproven)`.

Rank ideas by anchor strength, not by raw view count. A 3x own-channel-proven shape beats a 12x one-channel fluke.

## Differentiation tiebreaker (the three circles)

When two anchors are equally strong, prefer the one that DIFFERENTIATES this creator. Ed's three circles: your own channel, your niche, and adjacent niches. The glory is your channel crossed with the wider and adjacent space, not the direct niche everyone already copies.

- **Own-channel-proven** is always first. Repeat what already won here.
- **Adjacent-niche shapes translated in** are the differentiation goldmine. A shape proven in a neighboring niche, bent onto this creator's pillar, reads as original because nobody in the direct niche is running it yet.
- **Niche-saturated patterns** (the same shape every direct competitor already uses) are the trap. Proven but unoriginal, and a channel built only on them looks derivative and often underperforms. Usable, never the tiebreaker winner.

So on a tie: own-channel or adjacent-transferred beats niche-saturated.

## The default batch (~5-6)

- 4 anchored to STRONG or MODERATE signals (favor STRONG, favor the creator's OWN winners first, then convergent patterns, then niche-specific).
- 1-2 experimental swings, flagged.
- Spread across at least 2-3 different pillars and at least 2 of the Top 3 problems, unless the creator gave a focus. One pillar, one problem, six ideas reads as a rut.

Never proven-only (the channel goes derivative). Never all-experimental (the channel gambles with no signal).

**Why this mix (Ed's 100 doors).** Most doors punch you; a few hand you cash. Once a door pays, you keep opening that one and only gamble on a new door occasionally. So the batch leans proven (repeat what works) and spends 1-2 slots on swings (the every-fourth experiment). Proven-heavy is not laziness; it is how a channel compounds. The swings are what keep it from going stale.

## Anti-skew guards (the "don't be crappy" rules)

1. **Anchor or flag, never fake.** Every anchored idea cites a real `pattern-bank.md` entry by name (pattern label, or outlier title + channel). Never invent an outlier, a multiplier, or a spread. If you cannot anchor it and it is not a deliberate swing, drop it.
2. **Translate, never transcribe.** An anchor is a SHAPE to adapt ("titles that open with a named enemy", "the receipts-first case study"). Apply that shape to the creator's pillar and problem. Never hand back a competitor's title with the nouns swapped.
3. **Iceberg gate first.** Run the 2-layer check (`iceberg-and-top-3-alignment.md`) before surfacing. Inside iceberg + lands on a Top 3 problem = clean, lead with these. Inside iceberg + no Top 3 = allowed, flagged `outlier_within_iceberg`. Off iceberg = never surfaced.
4. **Theory of One.** A pattern that works on every channel in the niche can still miss THIS audience's expectation of the creator. When an anchor is niche-wide but the fit is uncertain, name the tension (per `theory-of-one-curation.md`) instead of assuming it transfers.
5. **Respect the drop list.** Skip any idea built on a `Considered + dropped` pattern. If it is genuinely strong, surface the drop rationale and ask before using it. Never silently re-propose a dropped pattern or a `dropped` backlog idea.
6. **Specificity bar.** A category is not an idea. "Pricing" fails. "The pricing mistake that makes clients ghost after the proposal" passes. If you cannot say the specific tension in one line, the idea is not ready.
7. **Working-title bar.** Each idea is surfaced as a working title (Ed: an idea is a title). Run it past the title rules in `knowledge/BENS-framework.md` lightly: under ~50 characters, specific not vague, reads as one human thought, credible for this creator. This is a quick legitimacy check so the idea can be judged, NOT full title craft. The working title is a provisional seed; `vid-title` does the real craft later against the full title-bank. Do not spin title variants or load the title / power-words banks here.

## The dial (Phase 3 postures)

The creator turns the dial; re-roll the batch with the new posture. Keep the same shape and tags, just shift the mix or the territory.

- **"more"** -> generate a fresh batch of the same shape (new ideas, same default mix). Do not repeat ideas already surfaced or in the backlog.
- **"tighter" / "safer"** -> drop the experimental swings. All 5-6 anchored to STRONG signals only (own-channel-proven and Confirmed winners first). Lowest crap risk, least range.
- **"wilder" / "more original"** -> flip the mix: 3-4 experimental swings, 2 anchored. Push contrarian takes, adjacent-niche transfers, and the creator's unique pillar angles. Higher risk, more voice. Still iceberg-gated; wild does not mean off-channel.
- **"different pillar" / "different problem"** -> regenerate aimed at the named pillar or problem (or rotate to ones the last batch underused).
- **"regenerate"** -> same posture, all-new ideas.

After any roll, surface the new batch and repeat the one-line dial offer. Do not narrate the change.

## What gets saved (Phase 4)

Only ideas the creator flags to keep. The unflagged batch is discarded, not logged. The backlog is a curated queue of ideas the creator actually liked, never a dump of everything generated. See `assets/ideas-backlog-template.md` for the row shape.
