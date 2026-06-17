# Skill testing plan: the vid-* pipeline

How to test the video-pipeline skills without re-deriving the method each time.
The harness lives in `tests/`. This doc is the why and the order. Companion to
`tests/README.md` (the how).

## The reframe

Testing creative skills feels unbounded because "grade a finished video" is
infinite and subjective. It is not what we do. The pipeline is a chain of
artifact steps: each skill eats one defined file and writes another. We test
stages, not videos. And most of what makes content bad is rule-breaking a script
catches, not taste: an em-dash, a fabricated `[[link]]`, an invented number, a
dropped handoff field, a banned word.

Two engines we already own carry this: `autoresearch` (four-way separation,
deterministic + AI-judge modes, averaging across many inputs) and `skill-creator`
(benchmark + variance, triggering evals). The only new assets are a corpus and
fixtures, both built once and reused across every skill.

## The model

- **Tier A ("does it work")**: deterministic `eval.py`, runs every iteration,
  gates Tier B. Checks: no em-dash, no banned words, no fabrication (every cited
  bank entry exists on disk, every claim-shaped number traces to source),
  frontmatter complete, alignment captured, required sections present, verbatim
  preserved, handoff fields present.
- **Tier B ("is it good")**: AI-judge `rubric.md`, runs only on Tier-A-clean
  outputs. 1 to 5 on voice (read-aloud against reference-pieces), alignment
  correctness, capture without interrogation, fabrication resistance.
- **Corpus = generalization.** 6 seeds across pillars, formats, intake modes,
  including 2 adversarial (a thin dump, a fabrication-bait dump). The score is
  the average across all 6. A skill that only works on one example is exposed.
- **Fixtures = speed.** Freeze a known-good upstream state once, feed it to the
  one skill under test, judge only its output. No re-running the chain per tweak.
- **Simulator = honest conversational tests.** Front-of-pipeline skills are
  multi-turn. A creator-simulator plays the creator from the seed and withholds
  on adversarial seeds, so "does it fabricate when pushed" is a real test.

## Status (pilot done)

Built and verified on `dev`:

- `tests/lib/` : the reusable Tier A checks (brand rules mirrored from `.vale/`,
  anti-fabrication, handoff contracts).
- `tests/corpus/seeds.json` : 6 seeds, synthetic creator "Sam Rivera".
- `tests/fixtures/shared/` : frozen foundation, voice-profile, reference-pieces,
  banks, people. `tests/fixtures/MANIFEST.md` tracks staleness.
- `tests/skills/vid-intake/` : the pilot suite (test_cases, creator-simulator,
  eval.py, rubric.md) with a committed all-passing baseline in `outputs/`.

Verification run: a good output scores `tier_a_pass_rate=1.0`. A planted
fabrication (invented `$250K`/`3x`, fake `[[story-bank/jordan-growth]]`, banned
word, dropped `aligned_with`) flips to FAIL on exactly those assertions, and the
handoff check catches the missing field. The eval discriminates.

## Rollout order

vid-intake (done) -> vid-ideas -> vid-framing -> [freeze after-framing fixture]
-> vid-structure -> [freeze after-structure] -> vid-intro -> vid-segment ->
vid-ending -> vid-pressure-test -> post-write. Each new skill is the same four
steps: filter the corpus, point at the right fixture stage, let autoresearch's
eval-agent write `eval.py` + `rubric.md`, run the loop. Prove it once on
vid-intake (done), the rest is repetition.

## Open dependency

Tier B's read-aloud judge anchors on real creator passages. The fixture currently
uses synthetic "Sam Rivera" passages so the harness is self-contained and
reproducible. For higher-fidelity voice judging, drop 3 to 5 real (redacted)
passages into `tests/fixtures/shared/foundation/reference-pieces/youtube-script.md`.
Tier A works fully without this; only Tier B voice fidelity gets sharper.
