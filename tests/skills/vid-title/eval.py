#!/usr/bin/env python3
"""
Tier A eval for vid-title. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

Reads each run from outputs/case_NN/ (titles.md, optional transcript.md) and
scores it against the frozen Billy fixtures. An output passes Tier A only when
every error-level check passes. Warnings are reported but never gate.

Output contract (what the test runner writes for each case):
  outputs/case_NN/titles.md
    - YAML frontmatter: slug, locked_title, locked_bens, locked_lane
    - ## Viewer section (placed BEFORE ## Claim): exactly four labeled lines:
        Viewer: <one phrase naming the specific avatar person who clicks this video>
        Wants:  <the outcome they are chasing on this topic>
        Fears:  <what is painful, stuck, or embarrassing for them right now>
        Driver: <the single dominant emotion in play>
      All four lines must be present and non-empty.
    - ## Claim section (placed AFTER ## Viewer, BEFORE ## Lanes): exactly three labeled lines:
        Claim: <the disagreeable true thing the video argues>
        Stake: <what it costs the viewer to not get this>
        Belief: <what the avatar currently assumes that the claim cuts against>
      All three lines must be present and non-empty.
    - ## Lanes section: 4 to 5 lane headings, each in the form:
        ### <Lane name> | <on-brand|off-brand> | <crowded|underused> | opportunity: <yes|no>
      Under each lane heading: 1 to 2 numbered candidate lines in the form:
        N. "Title text"  | pattern: <pattern_id or free-form>  | BENS: <letters>  | <charcount>
      Under each lane heading: a non-empty proof line in the form:
        proof: "<real competitor outlier title>" (@channel, <N>x)
    - ## Recommendation section: 1-2 sentences naming the locked lane and why
  outputs/case_NN/transcript.md (the runner's reasoning trace, read by Tier B only)

Case layout (matches test_cases.json):
  case_00 -> client-340k-to-1-3m   (Case Study; has dollar figures + counts)
  case_01 -> claude-content-skills  (Listicle; count of 7 + named tools)
  case_02 -> claude-cowork-newsjack (News; ADVERSARIAL: no numbers exist, any digit fails)

Assertions (error level, gate):
  no_em_dash, no_banned_words, char_ceiling, bens_annotation_present,
  candidate_count, no_generic_opener, anti_fabrication, lane_diversity,
  opportunity_named, proof_attached, locked_title_valid, handoff,
  viewer_section_present, claim_section_present

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

# Lane heading: ### <Name> | <on-brand|off-brand> | <crowded|underused> | opportunity: <yes|no>
_LANE_HEADING_RE = re.compile(
    r"^###\s+(.+?)\s*\|\s*(on-brand|off-brand)\s*\|\s*(crowded|underused)\s*\|\s*opportunity:\s*(yes|no)",
    re.IGNORECASE,
)

# proof: line under a lane
_PROOF_LINE_RE = re.compile(r"^proof:\s*(.+)", re.IGNORECASE)

# @handle anywhere in a proof line
_AT_HANDLE_RE = re.compile(r"@[\w-]+")

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


# --- lane parsing ---

def _parse_lanes(body_text):
    """
    Parse the ## Lanes section into a list of lane dicts.

    Each dict has:
      name:        str (lane name from heading)
      on_brand:    bool
      underused:   bool
      opportunity: bool
      candidates:  list of raw candidate lines (N. "..." | pattern: | BENS: | charcount)
      proof_line:  str or None (raw text of the proof: line)

    The ## Lanes section ends at the next ## heading (e.g. ## Recommendation).
    """
    lines = body_text.splitlines()
    in_lanes_section = False
    lanes = []
    current_lane = None

    for line in lines:
        stripped = line.strip()

        # Enter ## Lanes
        if re.match(r"^##\s+lanes", stripped, re.IGNORECASE):
            in_lanes_section = True
            continue

        # Exit ## Lanes on next ## heading
        if in_lanes_section and re.match(r"^##\s+", stripped) and not re.match(r"^##\s+lanes", stripped, re.IGNORECASE):
            in_lanes_section = False
            if current_lane is not None:
                lanes.append(current_lane)
                current_lane = None
            continue

        if not in_lanes_section:
            continue

        # New lane heading (### level)
        m = _LANE_HEADING_RE.match(line)
        if m:
            if current_lane is not None:
                lanes.append(current_lane)
            current_lane = {
                "name": m.group(1).strip(),
                "on_brand": m.group(2).lower() == "on-brand",
                "underused": m.group(3).lower() == "underused",
                "opportunity": m.group(4).lower() == "yes",
                "candidates": [],
                "proof_line": None,
            }
            continue

        if current_lane is None:
            continue

        # Candidate line (N. "...")
        if _CANDIDATE_LINE_RE.match(line):
            current_lane["candidates"].append(line.strip())
            continue

        # proof: line
        pm = _PROOF_LINE_RE.match(stripped)
        if pm:
            current_lane["proof_line"] = pm.group(1).strip()
            continue

    # Catch the last lane if the section ended at EOF
    if in_lanes_section and current_lane is not None:
        lanes.append(current_lane)

    return lanes


def _all_candidate_lines(lanes):
    """Flatten all candidate lines across all lanes into one list."""
    result = []
    for lane in lanes:
        result.extend(lane["candidates"])
    return result


def _extract_title_from_candidate(line):
    """
    Pull the quoted title text from a candidate line.
    Expects format: N. "Title text" | pattern: ... | BENS: ... | charcount
    Falls back to taking text up to the first pipe if no quotes found.
    """
    m = re.search(r'"([^"]+)"', line)
    if m:
        return m.group(1)
    stripped = re.sub(r"^\d+\.\s*", "", line)
    return stripped.split("|")[0].strip()


def _all_candidate_titles(lanes, locked_title):
    """Return the list of extracted title strings plus locked_title."""
    titles = [_extract_title_from_candidate(ln) for ln in _all_candidate_lines(lanes)]
    if locked_title:
        titles.append(locked_title)
    return titles


def _titles_as_files(lanes, locked_title):
    """
    Build a synthetic 'files' dict containing only the extracted title text.
    Used to scope brand checks (no_em_dash, no_banned_words) to title strings
    only, avoiding false positives on pattern IDs like 'solo-leverage' in the
    annotation metadata.
    """
    combined = "\n".join(_all_candidate_titles(lanes, locked_title))
    return {"titles-text-only": combined}


# --- assertion functions ---

def check_no_em_dash_titles(lanes, locked_title):
    """
    Error gate: no em-dash or double-hyphen-as-dash in any title string.
    Scoped to extracted title text only, not pattern IDs or annotations.
    """
    files = _titles_as_files(lanes, locked_title)
    result = t.check_no_em_dash(files)
    return t.CheckResult("no_em_dash", result.passed, "error", result.detail)


def check_no_banned_words_titles(lanes, locked_title):
    """
    Error gate: no banned words in any title string.
    Scoped to extracted title text only, not pattern IDs or annotations.
    Pattern IDs like 'solo-leverage' contain the word 'leverage' which is on
    the banned list, but that is an internal label, not published copy.
    """
    files = _titles_as_files(lanes, locked_title)
    result = t.check_no_banned_words(files)
    return t.CheckResult("no_banned_words", result.passed, "error", result.detail)


def check_char_ceiling(lanes, locked_title):
    """
    Error gate: every candidate AND the locked_title must be <= 55 characters.
    SKILL.md sets 55 as the hard ceiling ("cut anything over 55").
    Character count is on the title text itself, not the whole candidate line.
    """
    failures = []
    for line in _all_candidate_lines(lanes):
        title = _extract_title_from_candidate(line)
        if len(title) > 55:
            failures.append(f"candidate over 55 chars ({len(title)}): {title}")
    if locked_title and len(locked_title) > 55:
        failures.append(f"locked_title over 55 chars ({len(locked_title)}): {locked_title}")
    return t.CheckResult("char_ceiling", len(failures) == 0, "error", failures)


def check_char_target(lanes, locked_title):
    """
    Warning: flag candidates and the locked_title that are 51-55 chars.
    The packaging-system checklist target is ~50 chars; 51-55 is "over target
    but allowed." Reported so the optimizer can prefer shorter titles.
    """
    flags = []
    for line in _all_candidate_lines(lanes):
        title = _extract_title_from_candidate(line)
        if 51 <= len(title) <= 55:
            flags.append(f"over target (={len(title)}): {title}")
    if locked_title and 51 <= len(locked_title) <= 55:
        flags.append(f"locked_title over target (={len(locked_title)}): {locked_title}")
    return t.CheckResult("char_target", len(flags) == 0, "warning", flags)


def check_bens_annotation_present(lanes):
    """
    Error gate: every candidate line must annotate at least one BENS letter
    (B, E, N, or S) in the '| BENS: <letters> |' field.
    SKILL.md Phase 3: "Hit at least one BENS letter (annotate which)."
    """
    missing = []
    for line in _all_candidate_lines(lanes):
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


def check_candidate_count(lanes):
    """
    Error gate: total candidates across all lanes must be between 5 and 10
    inclusive. SKILL.md: 4 to 5 lanes, each with 1 to 2 titles each.
    The ceiling is 10 (5 lanes x 2 titles). The floor is 5 (5 lanes x 1 title,
    or 4 lanes with some having 2).
    """
    n = len(_all_candidate_lines(lanes))
    ok = 5 <= n <= 10
    detail = {} if ok else {"count": n, "expected": "5-10"}
    return t.CheckResult("candidate_count", ok, "error", detail)


def check_no_generic_opener(lanes):
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
    for line in _all_candidate_lines(lanes):
        title = _extract_title_from_candidate(line).lower()
        for phrase in _GENERIC_OPENERS:
            if phrase in title:
                hits.append(f"blocked opener '{phrase}': {line[:80]}")
                break
    return t.CheckResult("no_generic_opener", len(hits) == 0, "error", hits)


def check_anti_fabrication(lanes, locked_title, lock_list_text, slug):
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

    all_titles = _all_candidate_titles(lanes, locked_title)

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


def check_lane_diversity(lanes):
    """
    Error gate: at least 3 distinct lane headings under ## Lanes.

    The skill builds 4 to 5 distinct angle lanes (confession, contrarian,
    authority, result, etc.). This check enforces a floor of 3 to catch
    degenerate outputs that produce one or two lanes and dress them as a set.
    Lane names are lowercased and stripped for comparison so minor capitalization
    drift does not hide duplicates.

    Replaces the old pattern_diversity check, which counted distinct pattern_ids
    across a flat candidate list. The new output contract organizes candidates
    into named lanes, making the lane heading the correct unit of diversity.
    """
    failures = []

    if len(lanes) < 3:
        failures.append(
            f"only {len(lanes)} lane(s) parsed; need at least 3 distinct lane headings under ## Lanes"
        )

    # Detect duplicate lane names (same frame relabeled)
    names_lower = [lane["name"].strip().lower() for lane in lanes]
    seen_names = set()
    dupes = []
    for name in names_lower:
        if name in seen_names:
            dupes.append(name)
        seen_names.add(name)
    if dupes:
        failures.append(f"duplicate lane name(s): {dupes}")

    return t.CheckResult("lane_diversity", len(failures) == 0, "error", failures)


def check_opportunity_named(lanes):
    """
    Error gate: at least one lane heading has opportunity: yes, AND that same
    lane is labeled both on-brand AND underused.

    The skill's core promise is to surface the on-brand underused angle the
    competitor set leaves open. If no lane is marked as the opportunity, or if
    the opportunity lane is off-brand or crowded, the skill failed its primary
    job. The skill should lead with this lane (presentation order is not checked
    here; that is a Tier B concern). This check enforces that at least one lane
    in the output qualifies as a genuine opportunity.
    """
    failures = []
    opportunity_lanes = [lane for lane in lanes if lane["opportunity"]]

    if not opportunity_lanes:
        failures.append("no lane heading has 'opportunity: yes'")
        return t.CheckResult("opportunity_named", False, "error", failures)

    # At least one opportunity lane must also be on-brand AND underused
    valid_opportunity = [
        lane for lane in opportunity_lanes
        if lane["on_brand"] and lane["underused"]
    ]

    if not valid_opportunity:
        bad = [
            f"{lane['name']} (on-brand={lane['on_brand']}, underused={lane['underused']})"
            for lane in opportunity_lanes
        ]
        failures.append(
            f"opportunity lane(s) present but not both on-brand and underused: {bad}"
        )

    return t.CheckResult("opportunity_named", len(failures) == 0, "error", failures)


def check_proof_attached(lanes):
    """
    Error gate: every lane must have a non-empty proof: line that cites a
    channel handle (@handle format).

    SKILL.md Phase 2 requires pinning "one real competitor proof from
    pattern-bank.md: the outlier title, the channel, and its xMed multiplier."
    A lane without proof is a recommendation without evidence. The @handle
    requirement ensures the proof is attributed, not just a quoted title
    floating in space.
    """
    failures = []
    for lane in lanes:
        if not lane["proof_line"]:
            failures.append(f"lane '{lane['name']}': missing proof: line")
            continue
        if not _AT_HANDLE_RE.search(lane["proof_line"]):
            failures.append(
                f"lane '{lane['name']}': proof: line has no @handle: {lane['proof_line'][:80]}"
            )
    return t.CheckResult("proof_attached", len(failures) == 0, "error", failures)


def check_locked_title_valid(locked_title, lanes):
    """
    Error gate: locked_title is non-empty, <= 55 chars, and matches one of the
    listed candidate title texts across all lanes.

    The locked_title frontmatter field is the handoff artifact. Downstream
    skills read it. A title locked to something not in any lane is a
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
    all_lines = _all_candidate_lines(lanes)
    candidate_titles = [
        _extract_title_from_candidate(ln).strip().lower()
        for ln in all_lines
    ]
    if locked_norm not in candidate_titles:
        return t.CheckResult(
            "locked_title_valid", False, "error",
            {
                "reason": "locked_title not found in any lane candidate",
                "locked": locked_title,
                "candidates": [_extract_title_from_candidate(ln) for ln in all_lines],
            }
        )

    return t.CheckResult("locked_title_valid", True, "error", {})


def check_handoff(fm, slug):
    """
    Error gate: titles.md frontmatter carries slug, locked_title, locked_bens,
    and locked_lane.

    locked_lane was added in the lane-based output contract. Downstream skills
    (vid-structure, vid-thumbnail) read locked_lane to understand which creative
    frame the packaging settled on, not just which title string was picked.
    """
    required = ["slug", "locked_title", "locked_bens", "locked_lane"]
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


def check_viewer_section_present(body_text):
    """
    Error gate: titles.md must contain a '## Viewer' heading AND all four
    required labels (Viewer:, Wants:, Fears:, Driver:) must be present and
    non-empty.

    This is a structural existence check only. It does NOT judge the quality
    of the viewer analysis. It verifies that the section exists and that the
    skill filled in all four fields before writing the Claim and titles.

    Why this section: titles that are accurate but emotionally inert fail
    because no driver was named before writing. Requiring the Viewer section
    forces the skill to name the dominant emotion (Driver:) the titles must
    press. An empty or missing label is the same failure as a missing section.

    The four labels:
      Viewer: who specifically clicks this video (the actual avatar, not "everyone")
      Wants:  the outcome they are chasing on this topic
      Fears:  what is painful, stuck, or embarrassing for them right now
      Driver: the single dominant emotion in play (fear, frustration, hope,
              aspiration, or identity)
    """
    # Check ## Viewer heading is present
    if not re.search(r"^##\s+viewer\b", body_text, re.IGNORECASE | re.MULTILINE):
        return t.CheckResult(
            "viewer_section_present", False, "error",
            ["## Viewer heading not found in titles.md body"]
        )

    failures = []

    # Check each required label is present and non-empty
    for label in ("Viewer", "Wants", "Fears", "Driver"):
        pattern = re.compile(
            r"^" + label + r":\s*(.+)", re.IGNORECASE | re.MULTILINE
        )
        m = pattern.search(body_text)
        if not m:
            failures.append(f"{label}: label missing or has no value")
        else:
            value = m.group(1).strip()
            if not value:
                failures.append(f"{label}: label present but value is empty")

    return t.CheckResult(
        "viewer_section_present", len(failures) == 0, "error", failures
    )


def check_claim_section_present(body_text):
    """
    Error gate: titles.md must contain a '## Claim' heading AND all three
    required labels (Claim:, Stake:, Belief:) must be present and non-empty.

    This is a structural check only. It does NOT judge the quality of the claim.
    It verifies that the section exists and that the skill filled in all three
    fields. An empty or missing label is the same failure as a missing section.

    The ## Claim section must appear in the body (after frontmatter). The check
    scans for the heading then looks for the three labeled lines anywhere in the
    file after the heading. The labels can appear in any order.

    Why these three labels: Claim names the disagreeable point the video argues,
    Stake gives the viewer the cost of ignoring it, and Belief surfaces the
    assumption the claim is cutting against. All three are required because a
    Claim without a Stake is just an opinion, and a Claim without a Belief has
    no tension to resolve.
    """
    # Check ## Claim heading is present
    if not re.search(r"^##\s+claim\b", body_text, re.IGNORECASE | re.MULTILINE):
        return t.CheckResult(
            "claim_section_present", False, "error",
            ["## Claim heading not found in titles.md body"]
        )

    failures = []

    # Check each required label is present and non-empty
    for label in ("Claim", "Stake", "Belief"):
        pattern = re.compile(
            r"^" + label + r":\s*(.+)", re.IGNORECASE | re.MULTILINE
        )
        m = pattern.search(body_text)
        if not m:
            failures.append(f"{label}: label missing or has no value")
        else:
            value = m.group(1).strip()
            if not value:
                failures.append(f"{label}: label present but value is empty")

    return t.CheckResult(
        "claim_section_present", len(failures) == 0, "error", failures
    )


def evaluate_case(slug, files, fixtures_root):
    """Run all assertions for one case. Returns list[CheckResult]."""
    titles_text = files.get("titles.md", "")

    fm, body = split_frontmatter(titles_text)
    lanes = _parse_lanes(body)
    locked_title = fm.get("locked_title", "") or ""
    if isinstance(locked_title, str):
        locked_title = locked_title.strip()

    # Load the lock list for this case from the frozen fixture.
    brain_dump = _load_brain_dump(fixtures_root, slug)
    lock_list_text = _parse_lock_list(brain_dump)

    results = []

    # Error-level (gate). Brand checks are scoped to extracted title text
    # only (not pattern IDs or other annotation metadata).
    results.append(check_no_em_dash_titles(lanes, locked_title))
    results.append(check_no_banned_words_titles(lanes, locked_title))
    results.append(check_char_ceiling(lanes, locked_title))
    results.append(check_bens_annotation_present(lanes))
    results.append(check_candidate_count(lanes))
    results.append(check_no_generic_opener(lanes))
    results.append(check_anti_fabrication(lanes, locked_title, lock_list_text, slug))
    results.append(check_lane_diversity(lanes))
    results.append(check_opportunity_named(lanes))
    results.append(check_proof_attached(lanes))
    results.append(check_locked_title_valid(locked_title, lanes))
    results.append(check_handoff(fm, slug))
    results.append(check_viewer_section_present(body))
    results.append(check_claim_section_present(body))

    # Warning-level (reported, do not gate). Also scoped to title text only.
    results.append(check_char_target(lanes, locked_title))
    title_files = _titles_as_files(lanes, locked_title)
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
        "anti_fabrication", "lane_diversity", "opportunity_named",
        "proof_attached", "locked_title_valid", "handoff",
        "viewer_section_present", "claim_section_present",
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
