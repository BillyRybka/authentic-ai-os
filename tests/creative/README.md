# tests/creative/ : the blind A/B harness

For skills whose output is creative. The existing `tests/skills/` harness answers
"does it work" (fields present, nothing fabricated, no em-dash). This one answers
the question that harness cannot: **is it any good, and did the last change make
it better or worse.**

Dev-only, same as the rest of `tests/`. `scripts/release.ps1` rebuilds `main`
from an allowlist, so this tree never ships.

## Why it is built this way

A rubric cannot hold the line on creative work. Point a judge at a rubric and it
starts rewarding the rubric: every iteration scores higher and the output gets
safer, because "safe" is what a written-down standard describes. The score goes
up while the work gets worse, and nothing in the loop can see it happening.

So the scoreboard here is you, picking between two outputs without knowing which
is which. That is slower and it does not scale, and it is the only signal that
cannot drift.

Two rules make it work:

1. **The blinding is real.** Which version lands on the left is decided at pair
   time and written to `manifest.json`. It is never rendered into the review
   page. You cannot root for the new one because you cannot find it.
2. **Golds are the ratchet.** Once you see a batch you would actually film, it
   gets frozen. Every future change runs against the golds, blind. A candidate
   that loses to its own gold made the skill worse on that case, and it says so
   before the change lands.

That second one is the "refine, do not wreck it" guarantee. It is not a promise
the harness makes, it is a comparison it forces.

## What is under test

The **batch of framings and the recommendation**. That is the creative act, and
it is the part that feels weak.

Everything after the pick (the read, format, goal, the saved fields) is
mechanical and belongs to `tests/skills/vid-framing/eval.py`. Do not duplicate
those checks here. A rule that a script can check should be checked by a script,
so your attention goes to the part only you can judge.

The skill stops at the pick on its own, so the comparison needs no simulated
creator. That is why this harness has no persona and no judge.

## Run it

Two commands. One makes outputs, one shows them to you.

```bash
cd tests/creative

# 1. make the outputs
python ab.py new --baseline .claude/skills/vid-framing \
                 --candidate path/to/changed/vid-framing

# 2. look at them
python ab.py serve
```

`serve` opens your browser. Every run is listed, click one, read the two
options, click the one you'd film, type one line on why. It saves as you click,
no commands to copy. "Freeze picked as gold" at the bottom of a run.

Leave the tab open. The dashboard reads runs off disk on every request, so start
a run in another terminal, refresh, and it's there.

`--cases systems-beat-hustle,thin-pricing-dump` runs a subset. `--model sonnet`
overrides the model. Runs take a few minutes per arm per case.

Once you have golds, this is the whole loop for any change you make:

```bash
python ab.py new --baseline gold --candidate path/to/changed/vid-framing
python ab.py serve
```

If the change loses to its own gold, it made the skill worse. That's the ratchet.

### The CLI is still there

`record`, `bless` and `status` do the same jobs from the terminal, and the
browser calls the exact same functions rather than a parallel implementation.
Each run also writes a static `review.html` that works with no server, as a
fallback. `serve` is the path you want.

## The `--why` field

This is the part that pays off later. "Left won" is worthless in a month.
"Option 3 was the only one that named what they blame instead" tells you what to
protect in the next rewrite, and it is the raw material for the rubric in
`tests/skills/vid-framing/rubric.md` when that gets rewritten.

Skip it and the harness degrades into a scoreboard, which is the thing it exists
to avoid.

## Design decisions worth knowing

**Runs load project settings only** (`--setting-sources project`). Your global
`~/.claude/CLAUDE.md` is deliberately excluded. The skill ships to creators who
will not have your private rules, so it has to stand up without them. If an
output here breaks a rule your global file would have caught, the skill is
relying on your machine and that is a real defect.

**MCP is off** (`--strict-mcp-config`) so a flaky connector cannot change a
result between runs.

**Both arms can be the same skill.** That is not a mistake, it measures
run-to-run variance. If two runs of the identical skill produce batches you would
score differently, the gap between two *versions* has to clear that noise floor
before it means anything.

**`runs/` is gitignored.** Each run holds a full vault copy per arm per case.
`golds/` is committed: it is the thing worth keeping.

## Cases

**Synthetic**, six in `cases.json`, on the frozen `after-intake` fixtures. Four
ordinary, two adversarial. The adversarial ones (`thin-pricing-dump`,
`tempting-numbers-client-story`) catch invention: on those, an invented number or
an unearned proof point in *any* option, including the ones that lost, is a fail
no matter which side reads better. Judge that before you judge which is nicer.

**Real**, in `cases.local.json`, pointing into the creator's own vault. This file
is gitignored and holds paths only. Nothing is copied into the repo.

```json
{
  "vault_root": "C:/path/to/your/Content",
  "cases": [{"slug": "some-piece", "note": "why this case is worth testing"}]
}
```

The slug is a folder under `{vault_root}/pieces/`. Foundation, banks, people and
the vault `CLAUDE.md` come from the real vault; `knowledge/` still comes from
this repo, because that is plugin reference material rather than creator
material. The run always works on a copy, so it never writes into the real
vault.

Real cases exist because synthetic material cannot separate a great framing from
a decent one. Sam Rivera is too clean: no self-corrections, no arguing, no heat
in the wrong place, so every angle reads about equally plausible. Judge mechanics
on synthetic, judge quality on real.

Their golds land in `golds/local/` with their own `golds.json`, both gitignored,
because the reasons you write about a real piece are as much yours as the piece
is. The committed corpus stays synthetic.

## Adding a skill

`cases.json` names the skill, the input stage, and the prompt. Point those at
another skill and the harness works unchanged, as long as that skill also stops
and waits for a human decision. A skill that runs start to finish with no
decision point needs a simulated creator, and that is not built here yet.
