---
type: reference
scope: skill-local
loaded_by: [vid-intake]
status: active
tags: [reference, vid-intake, verification, anti-fabrication]
---

# Verify, don't replace

When the creator brings something real but uncertain (a metaphor, a stat, a claim), intake verifies the real thing instead of dismissing it, watering it down, or swapping it for something safer. Reaching for the safe, generic version is the exact instinct that produces slop, which is the one thing this brand exists to kill.

The research runs in an isolated sub-agent with its own context window, so the search noise never enters the brain-dump conversation. Intake ingests only the compact verdict.

## The sub-agent prompt

Spawn a sub-agent with this prompt, filling the two placeholders:

```
You are a verification sub-agent with your own context window. Research ONE specific
thing thoroughly, then report back two things only: is it true, and what is it.

VERIFY: {the creator's exact claim, metaphor, or stat, quoted}
HOW THEY'RE USING IT: {what it illustrates in the video, one line}

Research (be thorough, not endless):
- Search the web and read the actual sources. Never trust a single result or a snippet.
- Cross-check a few independent, authoritative sources: primary/official sources,
  reputable outlets, real subject experts. Not SEO blogs or AI-generated filler.
- Verify the MECHANISM, how the thing actually works, not just that the topic exists.
  The creator's whole point rests on the mechanism being right.
- Stop once a few solid sources genuinely agree. Don't spiral into a literature review.

Return ONLY this, nothing else:

VERDICT: holds | does not hold as used | can't confirm either way
WHAT IT IS: {1-3 sentences. The real mechanism, stated tightly, framed to fit how the
  creator is using it so it drops straight into the brain dump. If it does not hold, say
  what is actually true instead, in one line, so they can adjust or drop it.}
SOURCES: {2-3, title + link}

Rules: thorough research, lean report. No recap of your search process, no extra fields.
Do NOT rewrite or "improve" the creator's wording or metaphor, only confirm the mechanics.
No em-dashes.
```

## What intake does with the return

- **Holds** → keep the creator's material verbatim, add a one-line verified note plus the sources to the relevant Material entry.
- **Does not hold as used** → tell the creator in one line what is actually true, let them adjust or drop it. Never silently replace their material.
- **Can't confirm** → mark a TODO ("verify [X] before script"), keep the material, move on.

Never research inline. Never replace the creator's specific, real material with a safe generic substitute.
