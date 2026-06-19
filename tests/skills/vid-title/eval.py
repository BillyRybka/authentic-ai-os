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

Brand checks (no_em_dash, no_banned_words, no_aiisms, no_hedge_words) are
scoped to extracted title text only, not to the full file. Pattern IDs like
"solo-leverage" in the annotation metadata are internal labels and are
deliberately excluded from brand scanning to prevent false positives.

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
import vale_rules  # noqa: E402


# --- constants ---

# The blocklist from SKILL.md "AI-default openers" (hard cuts, not soft flags).
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

# Any digit at all (for the adversarial no-numbers check)
_ANY_DIGIT_RE = re.compile(r"\d")

# All-caps tokens that are likely tool/brand abbreviations (3-10 chars, no
# lowercase). These are the named-entity tokens worth checking against the
# lock list because they are almost always proper names: MCP, VEO, SOP, etc.
# Common all-caps single words used as emphasis (STOP, DON'T, WRONG, BEST,
# FREE, etc.) are excluded because they appear in the power-words bank and are
# legitimate copy choices, not named entities.
_CAPS_EMPHASIS_WORDS = {
    "STOP", "DON", "WRONG", "BEST", "FREE", "NEW", "ONLY", "JUST", "STILL",
    "RIGHT", "NOW", "MOST", "EVERY", "NEVER", "NO", "NOT", "ALL", "EVEN",
    "MORE", "LESS", "EASY", "FAST", "LAZY", "LAZIEST", "MASTER", "BETTER",
    "STEAL", "WITHOUT", "FOREVER", "INSANE", "VIRAL", "FULL", "REAL",
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
    Falls back to taking text up to the first pipe if no quotes found.
    """
    m = re.search(r'"([^"]+)"', line)
    if m:
        return m.group(1)
    # Fallback: strip 'N. ' prefix and take up to the first pipe
    stripped = re.sub(r"^\d+\.\s*", "", line)
    return stripped.split("|")[0].strip()


def _all_candidate_titles(candidate_lines, locked_title):
    """Return the list of extracted title strings plus locked_title."""
    titles = [_extract_title_from_candidate(ln) for ln in candidate_lines]
    if locked_title:
        titles.append(locked_title)
    return titles


def _titles_as_files(candidate_lines, locked_title):
    """
    Build a synthetic 'files' dict containing only the extracted title text.
    Used to scope brand checks (no_em_dash, no_banned_words) to title strings
    only, avoiding false positives on pattern IDs like 'solo-leverage' in the
    annotation metadata.
    """
    combined = "\n".join(_all_candidate_titles(candidate_lines, locked_title))
    return {"titles-text-only": combined}


# --- assertion functions ---

def check_no_em_dash_titles(candidate_lines, locked_title):
    """
    Error gate: no em-dash or double-hyphen-as-dash in any title string.
    Scoped to extracted title text only, not pattern IDs or annotations.
    """
    files = _titles_as_files(candidate_lines, locked_title)
    result = t.check_no_em_dash(files)
    return t.CheckResult("no_em_dash", result.passed, "error", result.detail)


def check_no_banned_words_titles(candidate_lines, locked_title):
    """
    Error gate: no banned words in any title string.
    Scoped to extracted title text only, not pattern IDs or annotations.
    Pattern IDs like 'solo-leverage' contain the word 'leverage' which is on
    the banned list, but that is an internal label, not published copy.
    """
    files = _titles_as_files(candidate_lines, locked_title)
    result = t.check_no_banned_words(files)
    return t.CheckResult("no_banned_words", result.passed, "error", result.detail)


def check_char_ceiling(candidate_lines, locked_title):
    """
    Error gate: every candidate AND the locked_title must be <= 55 characters.
    SKILL.md sets 55 as the hard ceiling ("cut anything over 55").
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
    but allowed." Reported so the optimizer can prefer shorter titles.
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
    SKILL.md Phase 3: "Hit at least one BENS letter (annotate which)."
    """
    missing = []
    for line in candidate_lines:
        m = _BENS_RE.search(line)
        if not m:
            missing.append(f"no BENS annotation: {line[:80]}")
        else:
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
    Error gate: no candidate contains a blocked generic opener phrase.
    Blocklist from SKILL.md "AI-default openers" (hard cut category):
      - "The truth about"
      - "Everything you need to know"
      - "Why you should"
      - "The ultimate guide to"
      - "Discover the secret"
    Check is case-insensitive on the extracted title text.
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
    Error gate: numbers and all-caps named tokens in candidates must trace to
    the lock list.

    Number check:
      - For the adversarial case (claude-cowork-newsjack) the lock list has
        NO numbers. Any digit in any candidate title fails.
      - For other cases, claim-shaped numbers (dollar figures, percentages,
        multipliers, large counts) must appear in the lock list text. Plain
        small counts (1-2 digits) are checked against the lock list too,
        because a listicle title claiming "9 Skills" when the material says
        "7 Skills" is fabrication.

    Named-entity check (conservative heuristic):
      - Only ALL-CAPS tokens of 3+ characters are checked (e.g. MCP, VEO,
        SOP, API). These are almost always product names or abbreviations.
      - Common emphasis words (STOP, WRONG, BEST, FREE, etc.) are excluded.
      - A flagged token must appear somewhere in the lock list text (case-
        insensitive) to pass. This catches invented tool names or methods
        while ignoring normal English words.
      - The locked_title is checked alongside the candidates.

    Why not check all capitalized words: normal English capitalization at the
    start of a title word ("Business," "System," "Channel") produces too many
    false positives. Only all-caps abbreviations are reliable named-entity
    signals.
    """
    failures = []
    lock_lower = lock_list_text.lower()
    is_adversarial = (slug == "claude-cowork-newsjack")

    all_titles = _all_candidate_titles(candidate_lines, locked_title)

    for title in all_titles:
        # --- number check ---
        if is_adversarial:
            if _ANY_DIGIT_RE.search(title):
                failures.append(
                    f"ADVERSARIAL: digit in title when lock list has no numbers: {title}"
                )
        else:
            bad_nums = find_fabricated_numbers(title, lock_list_text)
            for n in bad_nums:
                failures.append(f"number not in lock list ({n}): {title}")

        # --- named-entity check (all-caps tokens only) ---
        caps_tokens = re.findall(r"\b([A-Z]{3,10})\b", title)
        for tok in caps_tokens:
            if tok in _CAPS_EMPHASIS_WORDS:
                continue
            if tok.lower() not in lock_lower:
                failures.append(
                    f"all-caps token '{tok}' not in lock list: {title}"
                )

    # De-duplicate while preserving order
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
    3 distinct title-bank patterns." The pattern field is '| pattern: X |'.

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
    skills read it. A title locked to something not in the candidate list is a
    consistency failure. Comparison is case-insensitive on stripped text to
    tolerate minor whitespace drift.
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
    These are the fields downstream pipeline steps (vid-structure,
    vid-thumbnail) read to confirm packaging is complete and what was decided.
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

    # Check slug matches the expected case slug
    if "slug" in fm and fm["slug"] and isinstance(fm["slug"], str):
        if fm["slug"].strip().lower() != slug.lower():
            missing.append(f"slug mismatch (got '{fm['slug']}', expected '{slug}')")

    return t.CheckResult("handoff", len(missing) == 0, "error", {"missing": missing})


def evaluate_case(slug, files, fixtures_root):
    """Run all assertions for one case. Returns list[CheckResult]."""
    titles_text = files.get("titles.md", "")

    fm, body = split_frontmatter(titles_text)
    candidate_lines = _extract_candidate_lines(body)
    locked_title = fm.get("locked_title", "") or ""
    if isinstance(locked_title, str):
        locked_title = locked_title.strip()

    # Load the lock list for this case from the frozen fixture.
    brain_dump = _load_brain_dump(fixtures_root, slug)
    lock_list_text = _parse_lock_list(brain_dump)

    results = []

    # Error-level (gate). Brand checks are scoped to extracted title text
    # only (not pattern IDs or other annotation metadata).
    results.append(check_no_em_dash_titles(candidate_lines, locked_title))
    results.append(check_no_banned_words_titles(candidate_lines, locked_title))
    results.append(check_char_ceiling(candidate_lines, locked_title))
    results.append(check_bens_annotation_present(candidate_lines))
    results.append(check_candidate_count(candidate_lines))
    results.append(check_no_generic_opener(candidate_lines))
    results.append(check_anti_fabrication(candidate_lines, locked_title, lock_list_text, slug))
    results.append(check_pattern_diversity(candidate_lines))
    results.append(check_locked_title_valid(locked_title, candidate_lines))
    results.append(check_handoff(fm, slug))

    # Warning-level (reported, do not gate). Also scoped to title text only.
    results.append(check_char_target(candidate_lines, locked_title))
    title_files = _titles_as_files(candidate_lines, locked_title)
    results.append(t.check_no_aiisms(title_files))
    results.append(t.check_no_hedge_words(title_files))

    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    fixtures_root = _fixtures_root(manifest)
    cases = manifest["cases"]

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
