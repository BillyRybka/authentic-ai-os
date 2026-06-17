# Feedback offer

When and how a skill proactively offers feedback. The goal is to catch friction Billy would never otherwise hear about, without nagging. Conservative by default. One light offer, easy to decline, never blocks the creator's work.

Any skill can reference this. The `aaios-feedback` skill owns the actual capture and submit (see `knowledge/feedback-submit.md`). This file only governs the offer.

## The once-per-session guard

Run this check before offering. Scan the session so far:

- Has feedback already been offered this session? Skip.
- Has the creator already given feedback this session (the `aaios-feedback` skill ran)? Skip.
- Did the creator already wave off an offer this session ("not now", "no", "later")? Skip for the rest of the session.

If any are true, do not offer again. The creator can still ask for the `aaios-feedback` skill by name at any time. The guard only limits the proactive offer, not manual use.

## When to offer

Offer in these situations, and only these:

1. **On failure.** A skill errored, could not complete, or produced something visibly broken (a missing input it could not recover, a write that failed, a hard stop it could not pass).
2. **On clear frustration.** The creator plainly expressed that the output was wrong or unhelpful. Not a routine correction ("make it shorter", "use my other example") and not a single tweak. Repeated dissatisfaction, "that's not what I wanted", "this is off", "that didn't work".
3. **At the end of a completed journey.** A full sequence finished (for example the foundation chain completing). A natural close, not after every single skill.

Do not offer after a normal, successful single-skill run with no signal. Do not offer in the middle of active work. Do not offer twice for the same rough patch.

## How to offer

One short line, conversational, after the work (or after the failure is acknowledged). Make declining trivial.

On failure or frustration:

> "That didn't go the way it should have. Want to fire off quick feedback to Billy so this gets fixed? One or two questions, takes a few seconds. Or we keep going, your call."

At the end of a completed journey:

> "Before you go, anything about that run you'd want Billy to know, good or rough? I can send quick feedback. Otherwise you're all set."

If the creator says yes (or starts describing the problem), invoke the `aaios-feedback` skill via the Skill tool and let it take over. If they decline or ignore it and move on, drop it for the rest of the session per the guard. Never push twice.
