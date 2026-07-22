---
type: bank
project: authentic-ai-os
kind: bank
status: active
tags: [bank, hooks]
---

# Hook Bank

Your channel's proven hooks. creator-setup seeds this file into your `banks/` as a starter; from then on it is yours. When a hook you wrote holds retention on a published video, add it here. `vid-intro` reads this bank next to the plugin's hook pattern library and weights your winners heavier. A missing or empty bank is fine; the skill runs on the plugin library alone.

The plugin's hook pattern library (`hook-patterns.md`, shipped inside the `vid-intro` skill) is the craft reference: the 5 hook types, the fill-in-the-blank patterns, the worked and near-miss examples. This bank is not a copy of it. This bank is your own proven winners, in your voice, for your avatar.

## Entry schema

One entry per proven hook:

- **Hook:** the line as you actually said it
- **Type:** Question | Contrarian | Statement | Fact | Credibility (the 5 types in [[intro-architecture]])
- **Used in:** [[{the piece it ran in}]]
- **Receipt:** the signal that proves it held (retention at 30 seconds, average view duration, a comment pattern)
- **Why it worked:** one line, your read

## Example entries (delete once you add your own)

- **Hook:** "My last client went from zero booked calls to 14 in six weeks, off one email."
  - Type: Credibility
  - Used in: [[the-one-email-video]]
  - Receipt: 81% still watching at 30 seconds
  - Why it worked: specific numbers plus an open loop on "one email"

- **Hook:** "You are losing half your viewers in the first minute, and the fix is not a better hook."
  - Type: Contrarian
  - Used in: [[first-minute-retention-video]]
  - Receipt: 76% still watching at 30 seconds
  - Why it worked: names the pain, then denies the obvious fix

## Growing this bank

- Add a hook only after it has run and held. Unproven ideas stay in the plugin's pattern library, not here.
- Write entries the way you talk. If you would not say the line out loud, it does not belong in this bank.
- Cut entries that stop landing. A short list of winners beats a long list of maybes.
