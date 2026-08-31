---
type: person
bucket: active-client
status: active
tags: [person, client]
---

# {Full Name}

> [!note] Stub created automatically when mentioned in [[source-entry-slug|a bank entry]]. Flesh out when needed. This is the second brain pattern.

---

## Filling instructions (delete this section before save)

This template creates a `people/{Full Name}.md` stub whenever a bank entry mentions a client by name and no profile exists yet. Per the person-stub rule in `knowledge/bank-contract.md`, which is also where the deferral lives: `vid-braindump` never creates stubs, this skill does.

**Frontmatter fields:**

- `bucket`: one of `active-client`, `former-client`, `prospect`, `community-network`, `vendor`, `key-relationship`, `team`
- `status`: usually `active`
- `tags`: at minimum `person` and the bucket-specific tag (`client`, `partner`, etc.)

**Body:**

- `# {Full Name}` heading
- One Obsidian note callout linking back to the bank entry that triggered the stub creation

**When to use this template:**

- Any time a creator mentions a client in a story, proof, or testimonial and `people/{Full Name}.md` doesn't exist.
- Never save a bank entry with an unresolved `[[Client Name]]` wikilink. Create the stub first, then save the entry.

**When NOT to use this template:**

- If the profile already exists (check first with a Glob or direct read).
- If the person is fictional or composite. Bank entries should never reference fictional people.
