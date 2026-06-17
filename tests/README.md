# tests/ : the vid-* skill testing harness

How to test the video-pipeline skills fast, prove they work (not "perfect"), and
prove they generalize across many videos instead of one cherry-picked example.

This whole tree is test infra. It never ships: the release script
(`scripts/release.ps1`) rebuilds `main` from an allowlist of named skills plus
the knowledge they reference, so `tests/` is excluded by construction. It lives
on `dev` only.

## The idea in one screen

You are not grading "a video". The pipeline is a chain of artifact steps: each
skill eats one file and writes another. You test stages, and most failures are
rule-breaks a script can catch (em-dash, fabricated `[[link]]`, invented number,
dropped handoff field, banned word).

Two tiers, hard gate between them:

- **Tier A ("does it work")** is `eval.py`. Deterministic, cheap, runs every
  iteration. An output passes Tier A only when every error-level check passes.
- **Tier B ("is it good")** is `rubric.md`. An AI judge scores 1 to 5 on voice,
  alignment, capture quality, and fabrication resistance. Only run it on outputs
  that already passed Tier A.

One shared **corpus** of 6 seeds (`corpus/seeds.json`), including 2 adversarial
ones, runs against every skill. The score is the average across all 6, so a
skill that only works on one example gets exposed. Frozen **fixtures**
(`fixtures/shared/`) are a known-good upstream state, so you test one skill in
isolation without re-running the whole chain.

## Layout

```
tests/
  corpus/seeds.json        the 6 shared seeds (creator "Sam Rivera", all synthetic)
  fixtures/shared/         frozen foundation + banks + reference-pieces (read by every skill)
  fixtures/stages/         frozen per-video upstream states (added as the rollout advances)
  fixtures/MANIFEST.md     what produced each fixture + staleness tracking
  lib/                     the reusable Tier A checks (brand rules, fabrication, handoff)
  skills/<skill>/          one eval suite per skill (test_cases.json, eval.py, rubric.md, ...)
  integration/             manual end-to-end handoff checks
```

## lib/ (write the rules once)

- `vale_rules.py` mirrors `.vale/styles/ProductVoice/` (em-dash, en-dash, banned
  words, AI-isms, hedge words). The brand rules live in Vale at save time and
  here at eval time. Keep them in sync.
- `frontmatter.py` reads YAML frontmatter without a hard pyyaml dependency.
- `check_fabrication.py` flags cited `[[bank/slug]]` links that do not exist in
  the fixtures and claim-shaped numbers ($, %, x, big counts) absent from the
  seed's source. This is the anti-fabrication spine.
- `check_handoff.py` asserts a skill's output carries the fields the NEXT skill
  reads (`HANDOFF_CONTRACTS`). Keep it in sync with each SKILL.md Prerequisites.
- `tier_a_universal.py` composes the above into named checks every `eval.py`
  imports.

## Running the pilot (vid-intake)

The pilot is `skills/vid-intake/`. Its only input fixture is `fixtures/shared/`
because intake is the first per-video step.

```bash
cd tests/skills/vid-intake
python eval.py            # scores whatever is in outputs/case_NN/
```

`outputs/case_00/` and `outputs/case_05/` are committed as a worked, all-passing
baseline. The test runner overwrites `outputs/` each iteration.

## The four-way loop (autoresearch)

This harness plugs into the `autoresearch` skill. The four roles stay isolated so
the optimizer cannot game the eval:

1. **Optimizer** (you): edit `vid-intake/SKILL.md`, read only the two numbers
   (`tier_a_pass_rate`, then `quality_score`). Never edit `eval.py` or `rubric.md`
   mid-loop, they are locked.
2. **Test runner** (fresh agent): for each seed, runs the skill while a
   **creator-simulator** (`creator-simulator.md`) plays Sam Rivera from the seed,
   dumping naturally and withholding on adversarial seeds. Writes each run to
   `outputs/case_NN/` (brain-dump.md, piece.md, transcript.md).
3. **Tier A judge**: `eval.py`. Deterministic gate.
4. **Tier B judge** (fresh agent): scores Tier-A-clean outputs against `rubric.md`.

Conversational skills (the whole front of the pipeline) need the simulator. That
is what makes the fabrication test honest: if the simulator stays thin, does the
skill invent or flag the gap?

## Variance (skill-creator)

To check an eval is not flaky, run the same locked eval N times via
skill-creator's `aggregate_benchmark.py` and confirm low stddev. A flaky eval is
not trustworthy.

## Rollout order (pipeline order)

vid-intake (pilot, done) -> vid-ideas -> vid-framing -> [freeze
`stages/after-framing`] -> vid-structure -> [freeze `stages/after-structure`] ->
vid-intro -> vid-segment -> vid-ending -> vid-pressure-test -> post-write. Each
new skill is the same four steps: filter the corpus, point at the right fixture
stage, let autoresearch's eval-agent write `eval.py` + `rubric.md`, run the loop.

## Adding a skill suite

1. `mkdir tests/skills/<skill>` and add `test_cases.json` (point at the corpus,
   name the input fixture stage).
2. Write `eval.py` that imports `tier_a_universal` and adds skill-specific
   error checks (required frontmatter, sections, handoff boundary).
3. Write `rubric.md` with 3 to 5 dimensions, each anchored on the
   reference-pieces for the read-aloud test.
4. If the skill is conversational, add a `creator-simulator.md` persona note.
5. Freeze the upstream fixture stage it consumes, update `fixtures/MANIFEST.md`.
