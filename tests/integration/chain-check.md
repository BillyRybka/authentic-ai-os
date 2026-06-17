# Integration chain-check (manual)

Unit tests prove each skill works in isolation against a frozen fixture.
Integration proves the skills compose: that skill N's real output satisfies skill
N+1's input contract. skill-creator has no built-in multi-skill chain testing, so
this is a manual checklist. Run it on `dev`, by hand, after any change that
touches an output contract, and once before graduating a vid-* skill into the
release allowlist.

Run it on 2 seeds: one clean (`systems-beat-hustle`) and one adversarial
(`tempting-numbers-client-story`). The adversarial seed is the one that catches
fabrication leaking across a handoff.

## How to run one boundary

For each adjacent pair (skill N -> skill N+1):

1. Run skill N for real on the seed (use the creator-simulator for conversational
   skills). Do not use a fixture for N's output, use the live output.
2. Assert the handoff contract holds: skill N+1's required input fields exist in
   N's output. The contracts live in `lib/check_handoff.py` (`HANDOFF_CONTRACTS`).
   You can check programmatically:

   ```python
   import sys; sys.path.insert(0, "tests/lib")
   from check_handoff import check_handoff
   ok, detail = check_handoff("intake->framing",
       {"brain-dump.md": brain_text, "piece.md": piece_text})
   ```

3. If `ok` is False, the chain is broken at that seam even if both skills pass
   their own unit evals. Fix the upstream skill's output, not the contract.

## Boundaries to check (add rows as the rollout advances)

| Boundary | Contract key | Status |
|---|---|---|
| vid-intake -> vid-framing | `intake->framing` | defined, ready |
| vid-framing -> vid-structure | `framing->structure` | defined, ready when framing lands |
| vid-structure -> vid-intro | (add to HANDOFF_CONTRACTS) | pending |
| vid-intro -> vid-segment | (add) | pending |
| vid-segment -> vid-ending | (add) | pending |
| vid-ending -> vid-pressure-test | (add) | pending |

## The adversarial pass

After the clean seed, run `tempting-numbers-client-story` all the way through the
boundaries built so far. At every stage assert no invented number or fabricated
bank link appeared. A fabrication that passes one skill's unit eval can still get
introduced at a later stage, so the end-to-end pass on the adversarial seed is
the real integration guarantee.
