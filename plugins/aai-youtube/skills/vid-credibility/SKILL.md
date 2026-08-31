---
name: vid-credibility
description: Locks three viewer-relevant credibility brags for intros. Specific numbers, real wins, declarative past tense. Big plus Specific plus Personal. 4th foundation skill, runs after vid-pillars. Triggers on "build my credibility brags" or "lock my three brags".
---

# Credibility

Lock three viewer-relevant credibility brags. Each one: Big, Specific, Personal. Declarative past tense. No years, no credentials, no anti-proof.

These are the sentences the creator says in nearly every intro to signal "I know what I'm talking about on THIS topic." They are NOT a resume. They are NOT a client list. They are three sharp wins the viewer cares about.

## Contract

**Inputs (required):** `foundation/avatar.md` with the Avatar and Top 3 problems locked. The brags have to match what the avatar actually cares about.

**Inputs (optional):** `foundation/voice-profile.md`, `foundation/iceberg.md` (the statement grounds Step 1 and the tension coverage check), `foundation/offer.md`.

**Outputs:** `foundation/credibility.md`, created from its template in `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-templates.md` if missing. Three numbered brag sentences.

**Downstream consumers:** `vid-intro` (rotates brags through hook sections), `vid-segment`, `vid-ending`, `vid-structure` (plans where the brags land), every per-video skill that touches the intro.

## Load at session start

1. `${CLAUDE_PLUGIN_ROOT}/knowledge/interview-posture.md`. Shared posture. Non-negotiable.
2. `${CLAUDE_PLUGIN_ROOT}/knowledge/vault-integration.md`. The foundation-doc schema plus tag and naming conventions.
3. `foundation/avatar.md` (Avatar and Top 3 problems), `foundation/iceberg.md` (the statement), and `foundation/offer.md`.
4. `foundation/voice-profile.md` if it exists.
5. `references/credibility-method.md` when drafting starts. Holds the Big plus Specific plus Personal rule, the anti-proof check, and the good/bad pairs.

## Pre-check (silent)

Migration first: if `foundation/creator-foundation.md` exists, the breakup into the five foundation files hasn't finished. Follow `${CLAUDE_PLUGIN_ROOT}/knowledge/foundation-migration.md`, then resume this pre-check after the migration completes.

Then read `foundation/avatar.md` and `foundation/credibility.md`. Three states:

- **No Avatar or no Top 3.** Stop. Tell the creator: "Run `vid-avatar` first. I need to know who you're building credibility WITH before I can tell what proof actually lands."
- **Avatar plus Top 3 present, no Credibility brags yet.** Fresh run.
- **Credibility brags already locked.** Surface them and ask: "Three brags locked. Refresh, keep, or replace?"

## What a brag is

A credibility brag answers: "Why should I trust THIS person on THIS topic?"

It does NOT answer: "Why should I respect this person?"

### A brag IS

- "I made $4M from my YouTube channel in 2025."
- "I went from 400 subscribers to 358,000 in just over a year."
- "I've treated 3,000+ patients in my clinic."

Three things: Big, Specific, Personal. Past tense. Number attached.

### A brag is NOT

- "I've been doing this for 10 years." (years say nothing about what was produced)
- "I have an MBA from Stanford." (credential, not result)
- "I've worked with Fortune 500 companies." (name-drop, not viewer outcome)
- "I've helped many businesses become more efficient." (no number, no scale, no result)

## How this skill runs

Collect proof through sharp guided prompts, one at a time, so the creator can answer fast. Then rank the pile and lock the three that make THIS avatar trust the creator fastest. Bank the rest.

Internal, do not say this aloud: the prompts surface material, they are not the locked slots. A prompt asked third does not become brag three. Surface more than three, then rank in Step 4. The creator never needs the methodology explained to them. They just answer good questions.

### Step 1: Mirror the foundation, ask the first question

Read the Offer, Avatar, Top 3 problems, and Iceberg Statement. Mirror it in a line, then ground the first question in what the avatar actually wants before you ask it. That grounding is what makes the question land as "oh, that's easy" instead of a blank-page ask. Conversational, like a coach talking. Not a form label.

> "Reading your foundation. Iceberg Statement: '[the statement].'
>
> Your avatar wants [the result they want, in their words, tied to the Iceberg]. So your proof has to live there. What's the biggest result you've personally pulled off in that world?"

### Step 2: Guided proof prompts (one at a time, conversational)

Ask like a person, not a form. Each ask is a real question with just enough framing to make it easy to answer. No "Question 2." No bare label. Wait, react, move on when there's a usable answer or the creator has nothing there.

1. **Personal result.** Asked in Step 1, grounded in what the avatar wants.
2. **Client or customer result.** "Now the client side. What's the strongest result you got someone else? Walk me the before, the after, how long it took."
3. **Authority or operator proof.** "Any role, brand, or person you've worked with that this avatar would recognize the second they heard it?"
4. **Volume proof.** "What's the biggest number you can put on the table? Clients, videos, views, dollars. Only counts if it actually produced something."

Pull a fifth if it opens, conversationally: "Anything you've done that this avatar would swear is impossible?"

Keep the pile bigger than three. Don't announce that you're doing that.

### Step 3: Pushback while collecting

- Years with no output: "'10 years of experience' tells me nothing. What did 10 years produce? A number."
- Generic credentials: "An MBA is the setup. What did it produce in the avatar's world?"
- Hedges: "'I've been building' is in-progress. 'I built' is proof. Past tense."
- Vague scale: "'I've helped many businesses' doesn't work. How many specifically? Best result?"

**Recognized authority is not a name-drop.** This overrides the credential pushback. If the creator names a brand, role, platform, or person the avatar recognizes and respects in their own world, the name IS the proof. Don't force a number onto it. Keep it. It is often a near-permanent brag. The credential trap is only generic credentials the avatar has no relationship with. Full rule in `references/credibility-method.md`.

### Step 4: Ranking pass (do not lock the first three collected)

Score every candidate against these. Make the ranking visible to the creator when more than three surface ("We've got more than three. I wouldn't just pick the biggest numbers. I'd pick the three that make this avatar trust you fastest."):

1. Does it prove the creator can get this avatar the Iceberg promise?
2. Is it a result the avatar actually wants?
3. Does it kill a false belief the avatar holds?
4. Is it specific enough to trust?
5. Did the creator personally cause or contribute to it?
6. Would the avatar recognize the name, role, number, or outcome as meaningful?

Pick the strongest three. Cover distinct trust types where possible (personal, client or customer outcome, recognized authority, volume), but never lock a weak one just to fill a type.

### Step 5: False-belief test

Every locked brag either builds direct trust or destroys a false belief the avatar holds. If a brag is impressive but does neither for THIS avatar, it goes to the proof bank, not the locked three.

A brag that kills a belief beats a bigger number that kills nothing. An avatar who believes "I need a huge audience before this works" is destroyed by a result from a tiny starting point, not by a giant aggregate stat.

### Step 6: Iceberg-tension coverage check

The Iceberg Statement names a tension or enemy. Check: does at least one locked brag prove the creator can deliver on THAT specific part of the promise?

If yes, good. If no, flag it. Do not fake it:

> "Your three prove [what they prove]. None prove the [tension] part of your promise yet. Fine if that's newer. Not faking it. Banking that as the next proof to collect."

### Step 7: Unknown-client rule

If a client in a brag is not recognizable to the avatar, drop the name. Lead with the avatar's own label plus the surprising-small-input, big-result contrast.

Not the client's name. Not a generic "creator." If the avatar is business owners, it is "a business owner [surprising small inputs] to [big result]." The descriptor mirrors the buyer. The small numbers are the proof. Full rule in `references/credibility-method.md`.

If the client IS recognizable, use the name and create or update the person stub (stub if missing) with a wikilink. Per the vault rule, every recognizable human named gets a profile.

**Where to write the person stub:** default path is `people/{Full Name}.md` inside the workspace. Before writing, check the workspace `CLAUDE.md` for a `## Path overrides` section. If it specifies an alternate person-stub path (e.g., a vault-root `../../People/` folder), follow that override instead of the default. The override is the source of truth; the default applies only when no override is set.

### Step 8: Synthesis

Draft the three brags. Each one: Big, Specific, Personal. One proof point per brag, no cramming two numbers into one sentence. Show all three back:

> "Three brags. Read each one out loud. Anything off, or any need different wording?"

Iterate on whatever they reword. Run the anti-proof check below. Save when the creator gives an explicit lock.

### Anti-proof check (mandatory before lock)

For each brag, ask silently: "Does this make the CREATOR the source of failure?"

Example of accidental anti-proof:

> "Since 2022, I've built systems for over 50 businesses. The #1 reason those systems fail..."

That reads like the creator's systems fail. Reframe to:

> "Since 2022, I've built systems for over 50 businesses. The #1 mistake business owners make before they come to me..."

The creator is the expert. The mistake is the viewer's, the avatar's, or the niche default. NOT the creator's own work.

If any brag triggers anti-proof, push back:

> "Read that one again. Listen for whether it sounds like YOU produced the failure, or like the avatar produced the failure before finding you. The frame matters."

Lock only after every brag passes the anti-proof check.

## When the creator has no big numbers yet

Brand-new creator. No client wins. Three fallback angles, ranked weakest to strongest:

- **Education:** "I spent 2 years studying [specific thing]."
- **Consumption:** "I've read 300+ books on [topic]."
- **Personal transformation:** "I went from [bad state with numbers] to [good state with numbers] myself."

Personal transformation is strongest because it's a result, just the creator's own.

Flag the MVP caveat:

> "These are MVP brags. They work for cold viewers. As soon as you produce real client wins, replace them. Stronger proof always wins."

## Save

Two writes on lock.

**1. The locked three to the foundation.** Write the three brags to `foundation/credibility.md` (create from its template if missing). Three numbered lines. Creator's words verbatim where possible. Sharpen only by trimming filler or fixing tense.

**2. The leftover wins to the proof bank.** Every strong proof point that surfaced but did not make the locked three goes to `banks/proof-bank/` as its own entry, so future intros and scripts can pull it. Follow `${CLAUDE_PLUGIN_ROOT}/knowledge/proof-bank-schema.md` for what qualifies and the body sections, and `${CLAUDE_PLUGIN_ROOT}/knowledge/bank-contract.md` for the frontmatter block and the person-stub rule (`proof_type` is `personal-result` or `client-win`, kebab-case filename). Load both at this step, not at session start. The proof entries themselves are written to `banks/proof-bank/` in the creator's vault.

Rules for the bank write:
- Do not create a duplicate if an entry already covers that proof. Check first.
- Do not overwrite an existing proof entry without asking.
- Anonymize unknown clients the same way as the locked brags (avatar label, not the name).
- If a recognizable person is named, the same person-stub rule applies (default path `people/{Full Name}.md`; respect any `## Path overrides` in the workspace `CLAUDE.md`).

Tell the creator plainly:

> "Locked three to your foundation. The other [n] wins are saved to your proof bank so scripts can pull them when they fit."

## Closing the skill

Announce the lock and auto-advance to `vid-backstory`. No friction step.

> "Three brags locked. Moving to vid-backstory for your Problem-Action-Outcome story."

Then immediately invoke `vid-backstory` via the Skill tool. If the creator explicitly says they want to stop, respect that.

## Edge cases

**Creator gives all three brags as one type (e.g. all personal results, no client wins).** Push back once:

> "All three are your own results. The avatar trusts personal proof plus client proof plus volume. Do you have a client win you can swap in for one of these?"

If they genuinely don't have a client win, lock as-is and flag MVP.

**Creator gives a brag in the wrong topic.** A creator helping people quit smoking shouldn't lead with "I sold $1M in t-shirts." Push back:

> "That's a real number, but the avatar here is trying to quit smoking. Is there a brag closer to that result, even a smaller one?"

**Creator gives a name-drop ("I worked with Brand X").** Convert to a result:

> "Working with Brand X is the setup. What did you actually produce for them? A number, a result, a before-after?"

**Creator wants more than three brags.** Three is the rotation set. More brags get used in different videos, but the locked set is three. Tell them:

> "Three for the foundation. Extra wins can live in your story bank for video-specific intros. The Top 3 is the rotation that signals trust on every video."

## References

- `references/credibility-method.md`. Big plus Specific plus Personal rule. Good/bad pairs by trap type. Anti-proof check in depth. Fallback brags for new creators.

## Anti-patterns

- Locking a brag without running the anti-proof check.
- Letting "I've been doing this for X years" pass as a brag. Years aren't proof.
- Accepting credentials ("MBA from X") in place of results.
- Locking a hedged brag ("I've been working on building..."). Past tense or rewrite.
- Locking a name-drop ("I worked with Fortune 500"). Result or rewrite.
- Locking brags without showing the creator the exact proposed text first.
- Asking for the avatar or Top 3. Those were locked by `vid-avatar`. Read them.
