# Fixtures Manifest

Tracks what produced each frozen fixture and when, so staleness is visible. A
fixture is stale only when the upstream skill's OUTPUT CONTRACT changes (a new
required frontmatter field, a renamed section). Cosmetic prose changes inside a
skill never invalidate a fixture.

> [!warning] All fixtures are synthetic
> The creator "Sam Rivera", clients "Marcus Lane" / "Maria Quinn" / "Jordan",
> and all numbers are fictional, built only to exercise the eval harness. None
> of this is Billy's real foundation, banks, or client data. Real creator data
> lives in the separate Content Vault and never enters this repo.

## shared/ (foundation + banks, read by every skill)

| Path | Produced by | Date | Notes |
|---|---|---|---|
| foundation/iceberg.md | split from creator-foundation.md | 2026-08-06 | Iceberg statement + content pillars. Text unchanged, file boundary new. |
| foundation/avatar.md | split from creator-foundation.md | 2026-08-06 | Avatar + Top 3 perceived problems. Text unchanged, file boundary new. |
| foundation/credibility.md | split from creator-foundation.md | 2026-08-06 | The proof points. Text unchanged, file boundary new. |
| foundation/creator-foundation.md | hand-authored | 2026-01-10 | **Superseded, kept for un-migrated suites.** See the split note below. |
| foundation/voice-profile.md | hand-authored | 2026-01-10 | Thin guardrail. Refusals + banned words mirror .vale/. |
| foundation/reference-pieces/youtube-script.md | hand-authored | 2026-01-10 | Read-aloud anchor for the Tier B judge (5/5 calibration). |
| banks/story-bank/agency-owner-fired-himself.md | hand-authored | 2026-01-08 | Delegation story, problem 2. Referenced by seeds 2, 4. |
| banks/proof-bank/onboarding-5h-to-1h.md | hand-authored | 2026-01-08 | "5 hours to 1 hour", problem 1. Referenced by seeds 1, 2. |
| banks/metaphor-bank/restaurant-kitchen-systems.md | hand-authored | 2026-01-08 | Non-visual metaphor, problem 1. Referenced by seeds 1, 3. |
| banks/framework-bank/3-part-onboarding-system.md | hand-authored | 2026-01-08 | The example framework. |
| banks/pattern-bank.md, title-bank.md, transition-bank.md | hand-authored | 2026-01-09 | Thin single-file banks so downstream skills have signal. |
| people/Marcus Lane.md | hand-authored | 2026-01-08 | Client stub referenced by the story and proof. |

## The foundation split (2026-08-06)

Commit 5fa8146 rewired the runtime skills to read five foundation files instead
of one, and the fixtures were left behind. Every skill that gates on
`foundation/avatar.md` or `foundation/iceberg.md` was aborting at its own
precondition check before producing any output, so those suites were reporting
nothing rather than failing loudly.

`iceberg.md`, `avatar.md` and `credibility.md` are a faithful repartition of
`creator-foundation.md`. No text was added, removed or reworded.

`backstory.md` and `offer.md` are deliberately absent. Nothing in the current
suites reads them, and authoring a backstory for a fictional creator that
nothing consumes is invention with no consumer. Add them when a skill under
test actually reads them.

`creator-foundation.md` stays on disk until the suites below are migrated.
Delete it only when this list is empty.

| Suite | Still references creator-foundation.md |
|---|---|
| post-write | rubric.md |
| vid-ending | eval.py, rubric.md, test_cases.json |
| vid-framing | rubric.md |
| vid-ideas | eval.py, rubric.md |
| vid-intake | rubric.md |
| vid-intro | eval.py, rubric.md |
| vid-title | rubric.md, test_cases.json, fixtures/persona/ |

## billy/ (removed)

The real-Billy fixtures were removed on 2026-07-22 per the owner's rule that real channel content must not live in the test corpus. Everything under tests/fixtures/ is synthetic.

## stages/ (frozen per-video upstream states)

Added as the rollout crosses each boundary. The front-of-pipeline pilot
(vid-intake) needs no stage fixture: intake is the first per-video step, its
input is the raw seed plus shared/. The first stage fixture to freeze is
`after-intake/{slug}/` once vid-intake output stabilizes, which then becomes the
input fixture for the vid-framing loop.

| Boundary | Produced by | Date | Status |
|---|---|---|---|
| after-intake/{slug}/ | vid-intake | 2026-06-29 | hand-authored to current vid-intake schema, 2026-06-29 |
| after-framing/{slug}/ | vid-framing | pending | not yet reached (shared/Sam corpus) |
| after-structure/{slug}/ | vid-structure | pending | not yet reached |

## Suite-local fixtures (live inside tests/skills/<suite>/fixtures/)

Some suites keep fixtures next to their eval because nothing else should read
them. They follow the same rule as everything here: synthetic, frozen, and
stale only when the consuming skill's output contract changes.

| Suite | Path | Produced by | Date | Notes |
|---|---|---|---|---|
| vid-title | tests/skills/vid-title/fixtures/{slug}/piece.md | hand-authored | 2026-07-22 | Upstream framed pieces in the current vid-framing schema. Reskinned to the synthetic "Nora Beck / Beck Builds" persona (woodworking); banks, foundation, and brain-dump stages now live suite-locally under tests/skills/vid-title/fixtures/persona/. |
| vid-ideas | tests/skills/vid-ideas/fixtures/pattern-bank.md | hand-authored | 2026-07-22 | Synthetic Sam-niche bank with per-channel raw outlier rows (the shared bank has none) plus the off-lane @agenticalex trap circle. Receipt ground truth. |
| vid-ideas | tests/skills/vid-ideas/fixtures/prior-backlog.md | hand-authored | 2026-07-22 | Prior backlog: 1 kept row (pick-from-backlog source) + 1 dropped row (never-re-propose trap). |
