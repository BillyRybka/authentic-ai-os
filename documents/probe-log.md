# Probe log

Defects found while running a real piece through the pipeline in probe mode. Builder-facing. Never ships (`documents/` is not on the `release.ps1` allowlist).

## The rule this file exists to protect

**No skill files get edited during a probe run.** A defect goes here, the run continues. Fixes happen in one batch after the run ends, with the whole list visible, so patterns get fixed instead of symptoms.

If you catch yourself opening a `SKILL.md` mid-run, the run is over and you're back to where you started. Write the line here instead.

## Verdicts

- `flawed` — output is usable. Logged, kept, run continues on it.
- `bad` — output would poison every downstream stage. Logged, checkpoint restored, stage re-run or the artifact hand-written.

## Format

One entry per defect, newest at the bottom.

```
### {stage} · {verdict} · {slug}
- **Went in:** what the stage received
- **Came out:** what it produced
- **Should have:** what a good output looks like
- **Read:** why it went wrong, if you can see it. Skip if you can't.
```

`Read` is optional on purpose. Guessing at the cause mid-run is how you end up editing the skill. Leave it blank and let the batch pass figure it out.

## Runs

<!-- Log entries below. -->
