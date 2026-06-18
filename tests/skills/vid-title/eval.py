#!/usr/bin/env python3
"""
Tier A eval for vid-title. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

Reads each run from outputs/case_NN/ (titles.md, optional transcript.md) and
scores it against the frozen Billy fixtures. An output passes Tier A only when
every error-level check passes. Warnings are reported but never gate.

Output contract (what the test runner writes for each case):
  outputs/case_NN/titles.md
    - YAML frontmatter: slug, locked_title, locked_bens
    - ## Candidates section: 5 to 8 numbered lines, each in the form:
        N. "Title text"  | pattern: <pattern_id or free-form>  | BENS: <letters>  | <charcount>
    - ## Recommendation section: 1-2 sentences naming the pick and why
  outputs/case_NN/transcript.md (the runner's reasoning trace, read by Tier B only)

Case layout (matches test_cases.json):
  case_00 -> client-340k-to-1-3m   (Case Study; has dollar figures + counts)
  case_01 -> claude-content-skills  (Listicle; count of 7 + named tools)
  case_02 -> claude-cowork-newsjack (News; ADVERSARIAL: no numbers exist, any digit fails)

Assertions (error level, gate):
  no_em_dash, no_banned_words, char_ceiling, bens_annotation_present,
  candidate_count, no_generic_opener, anti_fabrication, pattern_diversity,
  locked_title_valid, handoff

Warnings (reported only):
  char_target, no_aiisms, no_hedge_words

Usage:
  python eval.py [outputs_dir]
"""

import json
import os
import re
import sys

# make tests/lib importable
_HERE = os.path.dirname(os.path.abspath(__file__))
_LIB = os.path.normpath(os.path.join(_HERE, "..", "..", "lib"))
sys.path.insert(0, _LIB)

import tier_a_universal as t  # noqa: E402
from frontmatter import split_frontmatter  # noqa: E402
from check_fabrication import find_fabricated_numbers, _normalize_numbers  # noqa: E402


# --- constants ---

# The blocklist from SKILL.md "AI-default openers" (hard cuts, not soft flags).
# Match at the start of a candidate OR anywhere inside it for phrase-style blocklist.
_GENERIC_OPENERS = [
    "the truth about",
    "everything you need to know",
    "why you should",
    "the ultimate guide to",
    "discover the secret",
]

# BENS letters: any of B, E, N, S must appear in the candidate annotation.
_BENS_RE = re.compile(r"\bBENS:\s*([BENS+]+)", re.IGNORECASE)

# Pattern field in a candidate line: | pattern: <something> |
_PATTERN_RE = re.compile(r"\|\s*pattern:\s*([^|]+?)\s*\|", re.IGNORECASE)

# The candidate line shape: starts with a digit and a period (N. "Title ...")
_CANDIDATE_LINE_RE = re.compile(r"^\s*\d+\.\s+")

# Claim-shaped number detector for the anti-fabrication check on title text.
# We go broader here than the general fabrication lib: for titles we also catch
# plain integers (any digit token), because a title "7 Skills" must trace to
# the lock list count, not be invented. The adversarial case has NO digits at
# all, so any digit in a candidate fails.
_ANY_DIGIT_RE = re.compile(r"\d")

# Named entities to guard: any capitalized or all-caps token that looks like
# a proper noun (tool name, brand, person) extracted from the candidate.
# We do a light named-token check: words with an initial capital (3+ chars)
# that are NOT common English words. The lock list defines what is allowed.
_COMMON_WORDS = {
    "The", "A", "An", "In", "On", "Of", "To", "My", "Our", "Your", "How",
    "Why", "What", "When", "Where", "Who", "And", "But", "Or", "For", "With",
    "Without", "Stop", "Don", "Just", "Only", "Best", "No", "Not", "Never",
    "Still", "Right", "Now", "This", "That", "These", "Those", "From",
    "After", "Before", "Into", "Over", "Under", "Most", "Even", "All",
    "Its", "It", "You", "I", "We", "They", "He", "She", "Is", "Are",
    "Was", "Were", "Has", "Have", "Had", "Do", "Does", "Did", "Get",
    "Got", "Make", "Made", "Run", "Build", "Built", "Use", "Used",
    "Every", "Each", "More", "Less", "Same", "New", "Old", "Big", "Small",
}


def _load_manifest():
    path = os.path.join(_HERE, "test_cases.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _fixtures_root(manifest):
    return os.path.normpath(os.path.join(_HERE, manifest["fixtures"]))


def _read_case_files(outputs_dir, i):
    case_dir = os.path.join(outputs_dir, f"case_{i:02d}")
    if not os.path.isdir(case_dir):
        return None
    files = {}
    for name in os.listdir(case_dir):
        if name.endswith(".md"):
            with open(os.path.join(case_dir, name), encoding="utf-8") as f:
                files[name] = f.read()
    return files


def _load_brain_dump(fixtures_root, slug):
    """Read brain-dump.md for a given slug from the stages/after-framing fixture."""
    path = os.path.join(
        fixtures_root, "stages", "after-framing", slug, "brain-dump.md"
    )
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def _parse_lock_list(brain_dump_text):
    """
    Extract the content of the '### Verifiable specifics (lock list)' block
    from a brain-dump. Returns the raw text of that section.
    """
    # Find the heading and collect lines until the next heading.
    lines = brain_dump_text.splitlines()
    in_section = False
    collected = []
    for line in lines:
        stripped = line.strip()
        if stripped.lower().startswith("### verifiable specifics"):
            in_section = True
            continue
        if in_section:
            if stripped.startswith("#"):
                break
            collected.append(line)
    return "\n".join(collected)


def _extract_candidate_lines(body_text):
    """
    Return the list of raw candidate lines from the ## Candidates section.
    A candidate line starts with a digit and a period: '1. "Title ..."'.
    """
    lines = body_text.splitlines()
    in_candidates = False
    candidates = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^##\s+candidates", stripped, re.IGNORECASE):
            in_candidates = True
            continue
        if in_candidates:
            if stripped.startswith("##") and not re.match(
                r"^##\s+candidates", stripped, re.IGNORECASE
            ):
                break
            if _CANDIDATE_LINE_RE.match(line):
                candidates.append(line.strip())
    return candidates


def _extract_title_from_candidate(line):
    """
    Pull the quoted title text from a candidate line.
    Expects format: N. "Title text" | pattern: ... | BENS: ... | charcount
    Falls back to taking the first token after 'N. ' if no quotes found.
    """
    # Try quoted form first
    m = re.search(r'"([^"]+)"', line)
    if m:
        return m.group(1)
    # Fallback: strip 'N. ' prefix and take up to the first pipe
    stripped = re.sub(r"^\d+\.\s*", "", line)
    return stripped.split("|")[0].strip()


def _named_tokens_in_title(title_text):
    """
    Light named-entity heuristic: words that start with a capital letter
    (or are all-caps), are 3+ chars, and are not in the common-words set.
    These are candidates that should appear in the lock list.
    """
    tokens = re.findall(r"\b[A-Z][A-Za-z0-9]*\b", title_text)
    return [tok for tok in tokens if tok not in _COMMON_WORDS and len(tok) >= 3]


# --- assertion functions ---

def check_char_ceiling(candidate_lines, locked_title):
    """
    Error gate: every candidate AND the locked_title must be <= 55 characters.
    The SKILL.md sets 55 as the hard ceiling ("cut anything over 55").
    Character count is on the title text itself, not the whole candidate line.
    """
    failures = []
    for line in candidate_lines:
        title = _extract_title_from_candidate(line)
        if len(title) > 55:
            failures.append(f"candidate over 55 chars ({len(title)}): {title}")
    if locked_title and len(locked_title) > 55:
        failures.append(f"locked_title over 55 chars ({len(locked_title)}): {locked_title}")
    return t.CheckResult("char_ceiling", len(failures) == 0, "error", failures)


def check_char_target(candidate_lines, locked_title):
    """
    Warning: flag candidates and the locked_title that are 51-55 chars.
    The packaging-system checklist target is ~50 chars; 51-55 is "over target
    but allowed." Reported so the optimizer knows to prefer shorter titles.
    """
    flags = []
    for line in candidate_lines:
        title = _extract_title_from_candidate(line)
        if 51 <= len(title) <= 55:
            flags.append(f"over target (={len(title)}): {title}")
    if locked_title and 51 <= len(locked_title) <= 55:
        flags.append(f"locked_title over target (={len(locked_title)}): {locked_title}")
    return t.CheckResult("char_target", len(flags) == 0, "warning", flags)


def check_bens_annotation_present(candidate_lines):
    """
    Error gate: every candidate line must annotate at least one BENS letter
    (B, E, N, or S) in the '| BENS: <letters> |' field.
    The SKILL.md requires "Hit at least one BENS letter (annotate which)."
    """
    missing = []
    for line in candidate_lines:
        m = _BENS_RE.search(line)
        if not m:
            missing.append(f"no BENS annotation: {line[:80]}")
        else:
            # Check that the value contains at least one of B, E, N, S
            val = m.group(1).upper()
            if not any(ch in val for ch in "BENS"):
                missing.append(f"BENS field has no valid letter: {line[:80]}")
    return t.CheckResult(
        "bens_annotation_present", len(missing) == 0, "error", missing
    )


def check_candidate_count(candidate_lines):
    """
    Error gate: between 5 and 8 candidates inclusive.
    SKILL.md Phase 3: "cut the pool down to the 5 to 8 strongest."
    """
    n = len(candidate_lines)
    ok = 5 <= n <= 8
    detail = {} if ok else {"count": n, "expected": "5-8"}
    return t.CheckResult("candidate_count", ok, "error", detail)


def check_no_generic_opener(candidate_lines):
    """
    Error gate: no candidate starts with or contains a blocked generic opener.
    Blocklist from SKILL.md "AI-default openers" (hard cut category):
      - "The truth about"
      - "Everything you need to know"
      - "Why you should"
      - "The ultimate guide to"
      - "Discover the secret"
    These are the on-distribution center the skill is explicitly told to cut.
    The check is case-insensitive and matches anywhere in the title, not just
    the start, because "Discover the secret" inside a title is equally dead.
    """
    hits = []
    for line in candidate_lines:
        title = _extract_title_from_candidate(line).lower()
        for phrase in _GENERIC_OPENERS:
            if phrase in title:
                hits.append(f"blocked opener '{phrase}': {line[:80]}")
                break
    return t.CheckResult("no_generic_opener", len(hits) == 0, "error", hits)


def check_anti_fabrication(candidate_lines, locked_title, lock_list_text, slug):
    """
    Error gate: numbers and named entities in candidates must trace to the lock list.

    Number check (reuses check_fabrication logic for digit-form numbers):
      - For the adversarial case (claude-cowork-newsjack) the lock list has
        NO numbers. Any digit, $, or % in a candidate title fails.
      - For other cases, claim-shaped numbers (dollar figures, percentages,
        multipliers, 3+ digit numbers) and plain integers must appear in the
        lock list text.

    Named-entity check (light heuristic):
      - Capitalized tokens (3+ chars, not common words) in each candidate are
        checked against the lock list. If the token appears nowhere in the lock
        list text, it is flagged as a potential fabricated named entity.
      - This catches invented tool names, brand names, or people names.
    """
    failures = []
    lock_norm = _normalize_numbers(lock_list_text)
    lock_lower = lock_list_text.lower()
    is_adversarial = (slug == "claude-cowork-newsjack")

    all_titles = [_extract_title_from_candidate(ln) for ln in candidate_lines]
    if locked_title:
        all_titles.append(locked_title)

    for title in all_titles:
        # --- number check ---
        if is_adversarial:
            # Any digit at all is fabrication for the adversarial case.
            if _ANY_DIGIT_RE.search(title):
                failures.append(f"ADVERSARIAL: digit in title when lock list has no numbers: {title}")
        else:
            # Use the same digit normalization as check_fabrication.py.
            # find_fabricated_numbers expects body_text and source_text.
            bad_nums = find_fabricated_numbers(title, lock_list_text)
            for n in bad_nums:
                failures.append(f"number not in lock list ({n}): {title}")

        # --- named entity check (light) ---
        for tok in _named_tokens_in_title(title):
            if tok.lower() not in lock_lower:
                failures.append(f"named token '{tok}' not in lock list: {title}")

    # De-duplicate while preserving order.
    seen = set()
    deduped = []
    for f in failures:
        if f not in seen:
            seen.add(f)
            deduped.append(f)

    return t.CheckResult("anti_fabrication", len(deduped) == 0, "error", deduped)


def check_pattern_diversity(candidate_lines):
    """
    Error gate: candidates draw from at least 3 distinct pattern values AND
    no more than 2 candidates share the same primary BENS letter.

    Pattern diversity: SKILL.md Phase 3 "the 5 to 8 should draw from at least
    3 distinct title-bank patterns." The pattern field in each candidate line
    is '| pattern: <pattern_id or free-form> |'. We extract those values and
    count distinct non-empty ones.

    BENS diversity: "no more than 2 candidates share the same primary BENS
    letter." The primary letter is the first BENS letter annotated.
    """
    failures = []

    # Pattern diversity
    patterns = []
    for line in candidate_lines:
        m = _PATTERN_RE.search(line)
        if m:
            p = m.group(1).strip().lower()
            if p:
                patterns.append(p)

    distinct_patterns = len(set(patterns))
    if distinct_patterns < 3:
        failures.append(
            f"only {distinct_patterns} distinct pattern(s); need at least 3"
        )

    # BENS diversity: count primary letter occurrences
    primary_counts = {}
    for line in candidate_lines:
        m = _BENS_RE.search(line)
        if m:
            val = m.group(1).upper()
            # First valid BENS letter is the primary
            for ch in val:
                if ch in "BENS":
                    primary_counts[ch] = primary_counts.get(ch, 0) + 1
                    break

    for letter, count in primary_counts.items():
        if count > 2:
            failures.append(
                f"primary BENS letter '{letter}' appears in {count} candidates (max 2)"
            )

    return t.CheckResult("pattern_diversity", len(failures) == 0, "error", failures)


def check_locked_title_valid(locked_title, candidate_lines):
    """
    Error gate: locked_title is non-empty, <= 55 chars, and matches one of the
    listed candidate title texts.

    The locked_title frontmatter field is the handoff artifact. Downstream
    skills (vid-structure, vid-thumbnail) read it. A title locked to something
    not in the candidate list is a consistency failure.
    """
    if not locked_title or not locked_title.strip():
        return t.CheckResult(
            "locked_title_valid", False, "error",
            {"reason": "locked_title is empty"}
        )

    if len(locked_title) > 55:
        return t.CheckResult(
            "locked_title_valid", False, "error",
            {"reason": f"locked_title over 55 chars ({len(locked_title)}): {locked_title}"}
        )

    # The locked_title must match one of the candidates. Compare
    # case-insensitively on stripped text to tolerate minor whitespace drift.
    locked_norm = locked_title.strip().lower()
    candidate_titles = [
        _extract_title_from_candidate(ln).strip().lower()
        for ln in candidate_lines
    ]
    if locked_norm not in candidate_titles:
        return t.CheckResult(
            "locked_title_valid", False, "error",
            {
                "reason": "locked_title not found in candidate list",
                "locked": locked_title,
                "candidates": [_extract_title_from_candidate(ln) for ln in candidate_lines],
            }
        )

    return t.CheckResult("locked_title_valid", True, "error", {})


def check_handoff(fm, slug):
    """
    Error gate: titles.md frontmatter carries slug, locked_title, locked_bens.
    These are the fields downstream pipeline steps (vid-structure, vid-thumbnail)
    read to know the packaging is complete and what was decided.
    """
    required = ["slug", "locked_title", "locked_bens"]
    missing = []
    for field in required:
        if field not in fm:
            missing.append(field)
            continue
        val = fm[field]
        if val is None:
            missing.append(field)
            continue
        if isinstance(val, str) and val.strip().lower() in ("", "null"):
            missing.append(field)

    # Also check slug matches the expected case slug
    if "slug" in fm and fm["slug"] and isinstance(fm["slug"], str):
        if fm["slug"].strip().lower() != slug.lower():
            missing.append(f"slug mismatch (got '{fm['slug']}', expected '{slug}')")

    return t.CheckResult("handoff", len(missing) == 0, "error", {"missing": missing})


def check_no_aiisms_titles(files):
    """Warning: AI-isms in the titles file. Thin wrapper so the name is clear."""
    return t.check_no_aiisms(files)


def check_no_hedge_words_titles(files):
    """Warning: hedge words in the titles file."""
    return t.check_no_hedge_words(files)


def evaluate_case(slug, files, fixtures_root):
    """Run all assertions for one case. Returns list[CheckResult]."""
    titles_text = files.get("titles.md", "")
    # Brand checks look at titles.md only (not transcript, which echoes reasoning).
    brand_files = {k: v for k, v in files.items() if k == "titles.md"}

    fm, body = split_frontmatter(titles_text)
    candidate_lines = _extract_candidate_lines(body)
    locked_title = fm.get("locked_title", "") or ""
    if isinstance(locked_title, str):
        locked_title = locked_title.strip()

    # Load the lock list for this case from the frozen fixture.
    brain_dump = _load_brain_dump(fixtures_root, slug)
    lock_list_text = _parse_lock_list(brain_dump)

    results = []

    # Error-level (gate)
    results.append(t.check_no_em_dash(brand_files))
    results.append(t.check_no_banned_words(brand_files))
    results.append(check_char_ceiling(candidate_lines, locked_title))
    results.append(check_bens_annotation_present(candidate_lines))
    results.append(check_candidate_count(candidate_lines))
    results.append(check_no_generic_opener(candidate_lines))
    results.append(check_anti_fabrication(candidate_lines, locked_title, lock_list_text, slug))
    results.append(check_pattern_diversity(candidate_lines))
    results.append(check_locked_title_valid(locked_title, candidate_lines))
    results.append(check_handoff(fm, slug))

    # Warning-level (reported, do not gate)
    results.append(check_char_target(candidate_lines, locked_title))
    results.append(t.check_no_aiisms(brand_files))
    results.append(t.check_no_hedge_words(brand_files))

    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    fixtures_root = _fixtures_root(manifest)
    cases = manifest["cases"]  # ["client-340k-to-1-3m", "claude-content-skills", "claude-cowork-newsjack"]

    error_assertions = [
        "no_em_dash", "no_banned_words", "char_ceiling",
        "bens_annotation_present", "candidate_count", "no_generic_opener",
        "anti_fabrication", "pattern_diversity", "locked_title_valid", "handoff",
    ]
    warn_assertions = ["char_target", "no_aiisms", "no_hedge_words"]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in error_assertions}
    warn_hits = {a: 0 for a in warn_assertions}

    print(f"--- vid-title Tier A ({len(cases)} cases) ---")

    for i, slug in enumerate(cases):
        files = _read_case_files(outputs_dir, i)
        if files is None:
            print(f"  case {i:02d} [{slug}]: NO OUTPUT (skipped)")
            continue
        if "titles.md" not in files:
            print(f"  case {i:02d} [{slug}]: MISSING titles.md (skipped)")
            continue

        total += 1
        results = evaluate_case(slug, files, fixtures_root)
        by_name = {r.name: r for r in results}

        if t.gate(results):
            total_pass += 1
        for a in error_assertions:
            if by_name[a].passed:
                assertion_pass[a] += 1
        for a in warn_assertions:
            if not by_name[a].passed:
                warn_hits[a] += 1

        print(t.format_case(f"{i:02d} [{slug}]", results))

    if total == 0:
        print("\nERROR: no output case folders found under " + outputs_dir)
        print("METRIC tier_a_pass_rate=0.0000")
        sys.exit(1)

    print(f"\n--- Assertion breakdown ({total} scored) ---")
    for a in error_assertions:
        pct = assertion_pass[a] / total * 100
        print(f"  {a}: {assertion_pass[a]}/{total} ({pct:.0f}%)")
    print("  warnings (not gating):")
    for a in warn_assertions:
        print(f"    {a}: {warn_hits[a]}/{total} cases had hits")

    pass_rate = total_pass / total
    print(f"\nDETAIL {total_pass}/{total} outputs passed ALL Tier A error checks")
    print(f"METRIC tier_a_pass_rate={pass_rate:.4f}")


if __name__ == "__main__":
    main()
