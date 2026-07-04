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
| foundation/creator-foundation.md | hand-authored | 2026-01-10 | Iceberg, avatar, Top 3, pillars. The alignment-check input. |
| foundation/voice-profile.md | hand-authored | 2026-01-10 | Thin guardrail. Refusals + banned words mirror .vale/. |
| foundation/reference-pieces/youtube-script.md | hand-authored | 2026-01-10 | Read-aloud anchor for the Tier B judge (5/5 calibration). |
| banks/story-bank/agency-owner-fired-himself.md | hand-authored | 2026-01-08 | Delegation story, problem 2. Referenced by seeds 2, 4. |
| banks/proof-bank/onboarding-5h-to-1h.md | hand-authored | 2026-01-08 | "5 hours to 1 hour", problem 1. Referenced by seeds 1, 2. |
| banks/metaphor-bank/restaurant-kitchen-systems.md | hand-authored | 2026-01-08 | Non-visual metaphor, problem 1. Referenced by seeds 1, 3. |
| banks/framework-bank/3-part-onboarding-system.md | hand-authored | 2026-01-08 | The example framework. |
| banks/pattern-bank.md, title-bank.md, transition-bank.md | hand-authored | 2026-01-09 | Thin single-file banks so downstream skills have signal. |
| people/Marcus Lane.md | hand-authored | 2026-01-08 | Client stub referenced by the story and proof. |

## billy/ (real frozen creator data, real-conditions evals)

> [!warning] billy/ is Billy's REAL data, not synthetic
> Unlike shared/ (synthetic Sam Rivera), the billy/ tree is a frozen snapshot of
> Billy's actual Content Vault: real foundation, real competitor research, real
> banks. It exists so a skill can be evaluated under real conditions. The question
> "does vid-title draw well from a rich, real bank?" cannot be answered against the
> thin synthetic shared/ bank. This is dev-only test infra and never ships: the
> release script rebuilds main from an allowlist that excludes tests/.

| Path | Source | Frozen | Notes |
|---|---|---|---|
| banks/pattern-bank.md | Content Vault | with vid-ideas suite | 103 outliers, 11 channels. The vid-ideas eval fixture. |
| banks/title-bank.md | Content Vault (last_refreshed 2026-06-17) | 2026-06-18 | 9 researched patterns with worked examples. vid-title input. |
| banks/power-words-bank.md | Content Vault (last_refreshed 2026-06-17) | 2026-06-18 | 17 global + 18 audience words, each with land/fail notes. vid-title input. |
| foundation/creator-foundation.md | Content Vault | with vid-ideas suite | Real avatar, Top 3, iceberg, pillars, credibility. The alignment-check input. |
| foundation/packaging-system.md | Content Vault (last_refreshed 2026-06-17) | 2026-06-18 | Format rotation + thumbnail/title defaults. vid-title input. Checklist sets title ceiling ~50 chars. |
| foundation/voice-profile.md | Content Vault | with vid-ideas suite | Signature phrases + hard refusals. |
| foundation/reference-pieces/youtube-script.md | Content Vault | with vid-ideas suite | Read-aloud anchor for the Tier B judge. |

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

Billy real-conditions stage (hand-authored framed pieces, for the vid-title eval under real banks):

| Boundary | Produced by | Date | Status |
|---|---|---|---|
| billy/stages/after-framing/client-340k-to-1-3m/ | hand-authored | 2026-06-18 | Case Study. Rich real-proof lock list ($340K, $1.3M, 1yr, 2,500 subs). |
| billy/stages/after-framing/claude-content-skills/ | hand-authored | 2026-06-18 | Listicle. Count (7) + named tools. Solo-leverage angle. |
| billy/stages/after-framing/claude-cowork-newsjack/ | hand-authored | 2026-06-18 | News. ADVERSARIAL: no numbers available, a correct title invents none. |
