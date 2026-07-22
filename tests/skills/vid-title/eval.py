#!/usr/bin/env python3
"""
Tier A eval for vid-title. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

Synced 2026-07-21 to the CURRENT skill contract: vid-title writes the locked
title into piece.md (title: field, last_updated: bumped) and produces NO
titles.md. The candidate set, receipts, wide pass, and kill pass live in the
conversation, which the test runner captures as transcript.md.

Reads each run from outputs/case_NN/ and scores it against the suite-local
upstream fixtures (fixtures/{slug}/piece.md), the frozen billy brain-dumps
(../../fixtures/billy/stages/after-framing/{slug}/brain-dump.md, the lock-list
ground truth), and Billy's real banks (pattern-bank, title-bank,
power-words-bank). An output passes Tier A only when every error-level check
passes. Warnings are reported but never gate.

Output contract (what the test runner writes for each case):
  outputs/case_NN/piece.md
    - the suite-local upstream piece with ONLY two changes: title: set to the
      locked title, last_updated: bumped to the run date. Every other
      frontmatter field and the body preserved verbatim.
  outputs/case_NN/transcript.md
    - ## Lock list: bullets grounded in brain-dump.md
    - ## Wide pass: 20+ numbered candidates (the kill-rate floor)
    - a kill-pass note (what died and why)
    - ## Options: 3-5 proven structure groups + exactly one wildcard group.
      Proven group: '### <name>' heading, ONE receipt line
        receipt: "<source outlier title>" (@channel, <N.Nx>)
      and 1-2 numbered candidate lines
        N. "Title text"  <BENS letters>  (<char count>)
      Wildcard group: heading contains 'wildcard', NO receipt line, 1-2 swings.
    - ## Recommendation: names one presented candidate with its reason
    - 6-10 presented survivors total (proven + wildcard)

Case layout (matches test_cases.json):
  case_00 -> client-340k-to-1-3m   (case-study; dollar figures + counts)
  case_01 -> claude-content-skills  (listicle; count of 7 + named tools)
  case_02 -> claude-cowork-newsjack (news; ADVERSARIAL: no numbers exist)

Assertions (error level, gate):
  no_em_dash, no_banned_words, titles_no_em_dash, titles_no_banned_words,
  handoff_framing_to_title, title_written, last_updated_bumped,
  piece_fields_preserved, locked_title_valid, char_ceiling,
  char_count_honest, bens_annotation_present, survivor_count,
  structure_diversity, wildcard_present, kill_rate, receipt_attached,
  power_word_spent, anti_fabrication, no_generic_opener, no_colons_pipes,
  lock_list_grounded, recommendation_present, candidate_line_format

Warnings (reported only):
  char_target, no_aiisms, no_hedge_words

Brand and fabrication checks on titles are scoped to the extracted presented
candidate strings plus the locked title, never to the whole transcript (which
legitimately echoes the creator and quotes real bank outliers with their own
numbers). piece.md is scanned whole, as a vault file.

Usage:
  python eval.py [outputs_dir]
"""

import json
import os
import re
import sys
from datetime import date

# make tests/lib importable
_HERE = os.path.dirname(os.path.abspath(__file__))
_LIB = os.path.normpath(os.path.join(_HERE, "..", "..", "lib"))
sys.path.insert(0, _LIB)

import tier_a_universal as t  # noqa: E402
from frontmatter import split_frontmatter  # noqa: E402
from check_fabrication import find_fabricated_numbers  # noqa: E402
from check_handoff import check_handoff  # noqa: E402

# --- constants from SKILL.md and references/title-filters.md ---

# AI-default openers, hard cuts per title-filters.md ("dead on arrival").
_GENERIC_OPENERS = [
    "the truth about",
    "everything you need to know",
    "why you should",
    "the ultimate guide to",
    "discover the secret",
]

# SKILL.md Step 4: 50 target, 55 hard ceiling.
CHAR_CEILING = 55
CHAR_TARGET = 50

# SKILL.md Step 5: "Show the survivors (6 to 10)".
SURVIVOR_MIN = 6
SURVIVOR_MAX = 10

# SKILL.md Step 2: "Pick 3 to 5 distinct structures".
GROUPS_MIN = 3
GROUPS_MAX = 5

# SKILL.md Step 3: "20 or more candidates across the structures, then keep only
# the best 2 per group. Most of what you write should die."
WIDE_PASS_MIN = 20

# A presented candidate line: 1. "Title text"  B+N  (48)
_CANDIDATE_RE = re.compile(
    r'^\s*(\d+)\.\s+"([^"]+)"\s+([A-Za-z](?:\+[A-Za-z])*)\s+\((\d+)\)\s*$'
)
# Any numbered line (to catch malformed candidates inside ## Options)
_NUMBERED_RE = re.compile(r"^\s*\d+\.\s+")
# A receipt line: receipt: "Source outlier" (@handle, 12.3x)
_RECEIPT_RE = re.compile(
    r'^\s*receipt:\s*"([^"]+)"\s*\(@([\w-]+),\s*(\d+(?:\.\d+)?)x\s*\)\s*$',
    re.IGNORECASE,
)
# Any digit at all (for the adversarial no-numbers check)
_ANY_DIGIT_RE = re.compile(r"\d")
# @handle anywhere in the banks
_AT_HANDLE_RE = re.compile(r"@[\w-]+")
# Power-word entries in power-words-bank.md: ### "WORD"
_POWER_WORD_RE = re.compile(r'^###\s+"([^"]+)"', re.MULTILINE)
# xMed token on a pattern-bank table row
_XMED_RE = re.compile(r"(\d+(?:\.\d+)?)x")

# All-caps tokens that are legitimate emphasis choices (they appear in the
# power-words bank as plain English words, not as named entities). All-caps
# tokens outside this set must trace to the lock list (MCP, VEO, SOP...).
_CAPS_EMPHASIS_WORDS = {
    "STOP", "DON", "WRONG", "BEST", "FREE", "NEW", "ONLY", "JUST", "STILL",
    "RIGHT", "NOW", "MOST", "EVERY", "NEVER", "NO", "NOT", "ALL", "EVEN",
    "MORE", "LESS", "EASY", "FAST", "LAZY", "LAZIEST", "MASTER", "BETTER",
    "STEAL", "WITHOUT", "FOREVER", "INSANE", "VIRAL", "FULL", "REAL",
}

# piece.md frontmatter fields vid-title may write. Everything else is another
# skill's field and must survive byte-identical ("never re-argues the video").
_MUTABLE_FIELDS = {"title", "last_updated"}


# --- loading helpers ---

def _load_manifest():
    with open(os.path.join(_HERE, "test_cases.json"), encoding="utf-8") as f:
        return json.load(f)


def _norm_path(*parts):
    return os.path.normpath(os.path.join(*parts))


def _read(path):
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


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


def _normalize(text):
    """Whitespace, quote, and case normalization for substring tracing."""
    s = text.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = re.sub(r"\]\([^)]*\)", "]", s)  # [Title](url) -> [Title]
    s = s.replace("[", "").replace("]", "")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


# --- fixture parsing ---

def _parse_lock_list(brain_dump_text):
    """Raw text of the '### Verifiable specifics (lock list)' block."""
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


def _parse_power_words(bank_text):
    return _POWER_WORD_RE.findall(bank_text)


# --- transcript parsing ---

def _section_lines(body_text, heading_regex):
    """Lines between a ## heading matching heading_regex and the next ## one."""
    lines = body_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s+", line.strip()) and heading_regex.search(line):
            start = i + 1
            break
    if start is None:
        return None
    out = []
    for line in lines[start:]:
        if re.match(r"^##\s+", line.strip()):
            break
        out.append(line)
    return out


def _parse_options(body_text):
    """
    Parse ## Options into a list of group dicts:
      name, wildcard (bool), receipt (dict|None), candidates (list[dict]),
      malformed (list of numbered lines that failed the strict candidate regex)
    Candidate dict: num, title, bens, chars (annotated), raw.
    """
    lines = _section_lines(body_text, re.compile(r"^##\s+options\b", re.IGNORECASE))
    if lines is None:
        return None
    groups = []
    current = None
    for line in lines:
        s = line.strip()
        hm = re.match(r"^###\s+(.+)$", s)
        if hm:
            current = {
                "name": hm.group(1).strip(),
                "wildcard": "wildcard" in hm.group(1).lower(),
                "receipt": None,
                "candidates": [],
                "malformed": [],
            }
            groups.append(current)
            continue
        if current is None:
            continue
        rm = _RECEIPT_RE.match(s)
        if rm:
            current["receipt"] = {
                "title": rm.group(1), "handle": rm.group(2),
                "xmed": float(rm.group(3)), "raw": s,
            }
            continue
        cm = _CANDIDATE_RE.match(line)
        if cm:
            current["candidates"].append({
                "num": int(cm.group(1)), "title": cm.group(2),
                "bens": cm.group(3), "chars": int(cm.group(4)),
                "raw": line.strip(),
            })
            continue
        if _NUMBERED_RE.match(line):
            current["malformed"].append(line.strip())
    return groups


def _presented(groups):
    """All presented candidate dicts (proven + wildcard), flattened."""
    out = []
    for g in groups or []:
        out.extend(g["candidates"])
    return out


def _wide_pass_count(body_text):
    lines = _section_lines(body_text, re.compile(r"^##\s+wide pass\b", re.IGNORECASE))
    if lines is None:
        return 0
    return sum(1 for line in lines if _NUMBERED_RE.match(line))


def _transcript_lock_bullets(body_text):
    lines = _section_lines(body_text, re.compile(r"^##\s+lock list\b", re.IGNORECASE))
    if lines is None:
        return None
    return [l.strip() for l in lines if l.strip().startswith("-")]


# --- assertion functions ---

def check_handoff_framing_to_title(upstream_piece):
    """
    Error gate: the upstream piece.md carries what vid-title reads from
    framing (tests/lib/check_handoff.py 'framing->title': type, slug,
    selected_angle, core_payoff, format, goal, voice_context).
    """
    ok, detail = check_handoff("framing->title", {"piece.md": upstream_piece})
    return t.CheckResult("handoff_framing_to_title", ok, "error", detail)


def check_title_written(piece_text):
    """Error gate: piece.md frontmatter title: is set and within the ceiling."""
    fm, _ = split_frontmatter(piece_text)
    title = fm.get("title")
    if title is None or str(title).strip() in ("", "null"):
        return t.CheckResult(
            "title_written", False, "error",
            {"reason": "piece.md frontmatter has no title: field"},
        )
    title = str(title).strip()
    if len(title) > CHAR_CEILING:
        return t.CheckResult(
            "title_written", False, "error",
            {"reason": f"title over {CHAR_CEILING} chars ({len(title)}): {title}"},
        )
    return t.CheckResult("title_written", True, "error", {})


def check_last_updated_bumped(fixture_text, piece_text):
    """Error gate: last_updated moved forward from the upstream fixture."""
    f_fm, _ = split_frontmatter(fixture_text)
    o_fm, _ = split_frontmatter(piece_text)
    old, new = str(f_fm.get("last_updated", "")).strip(), str(o_fm.get("last_updated", "")).strip()
    if not new or new.lower() == "null":
        return t.CheckResult(
            "last_updated_bumped", False, "error", {"reason": "last_updated missing in output"}
        )
    if old and new == old:
        return t.CheckResult(
            "last_updated_bumped", False, "error",
            {"reason": f"last_updated unchanged ({old}); SKILL Step 6 bumps it to today"},
        )
    try:
        ok = date.fromisoformat(new) > date.fromisoformat(old)
    except ValueError:
        ok = new != old
    detail = {} if ok else {"old": old, "new": new, "reason": "last_updated did not move forward"}
    return t.CheckResult("last_updated_bumped", ok, "error", detail)


def check_piece_fields_preserved(fixture_text, piece_text):
    """
    Error gate: every upstream frontmatter field except title/last_updated is
    present and unchanged, no new fields appeared, and the body is unchanged.
    vid-title packages the locked angle; it never re-argues it (SKILL Step 1
    and Related skills), so framing's fields must survive byte-identical.
    """
    f_fm, f_body = split_frontmatter(fixture_text)
    o_fm, o_body = split_frontmatter(piece_text)
    problems = []
    for key, val in f_fm.items():
        if key in _MUTABLE_FIELDS:
            continue
        if key not in o_fm:
            problems.append(f"frontmatter field dropped: {key}")
        elif str(o_fm[key]) != str(val):
            problems.append(f"frontmatter field changed: {key}")
    for key in o_fm:
        if key not in f_fm and key not in _MUTABLE_FIELDS:
            problems.append(f"unexpected new frontmatter field: {key}")
    norm = lambda b: re.sub(r"[ \t]+$", "", b, flags=re.MULTILINE).strip()
    if norm(f_body) != norm(o_body):
        problems.append("piece.md body changed; only frontmatter title/last_updated may change")
    return t.CheckResult("piece_fields_preserved", not problems, "error", problems)


def check_locked_title_valid(piece_text, presented):
    """Error gate: the locked title is one of the presented candidates."""
    fm, _ = split_frontmatter(piece_text)
    title = str(fm.get("title", "")).strip()
    if not title:
        return t.CheckResult(
            "locked_title_valid", False, "error", {"reason": "no locked title in piece.md"}
        )
    titles = [c["title"].strip().lower() for c in presented]
    ok = title.lower() in titles
    detail = {} if ok else {
        "reason": "locked title was never presented to the creator in ## Options",
        "locked": title,
        "presented": [c["title"] for c in presented],
    }
    return t.CheckResult("locked_title_valid", ok, "error", detail)


def check_char_ceiling(presented, locked_title):
    """Error gate: every presented candidate and the locked title <= 55."""
    failures = []
    for c in presented:
        if len(c["title"]) > CHAR_CEILING:
            failures.append(f"over {CHAR_CEILING} ({len(c['title'])}): {c['title']}")
    if locked_title and len(locked_title) > CHAR_CEILING:
        failures.append(f"locked title over {CHAR_CEILING} ({len(locked_title)}): {locked_title}")
    return t.CheckResult("char_ceiling", not failures, "error", failures)


def check_char_target(presented, locked_title):
    """Warning: flag 51-55 char titles (over the 50 target, under ceiling)."""
    flags = []
    for c in presented:
        if CHAR_TARGET < len(c["title"]) <= CHAR_CEILING:
            flags.append(f"over target ({len(c['title'])}): {c['title']}")
    if locked_title and CHAR_TARGET < len(locked_title) <= CHAR_CEILING:
        flags.append(f"locked title over target ({len(locked_title)}): {locked_title}")
    return t.CheckResult("char_target", not flags, "warning", flags)


def check_char_count_honest(presented):
    """Error gate: the annotated (NN) char count equals the real count."""
    failures = []
    for c in presented:
        actual = len(c["title"])
        if c["chars"] != actual:
            failures.append(f"annotated ({c['chars']}) != actual ({actual}): {c['title']}")
    return t.CheckResult("char_count_honest", not failures, "error", failures)


def check_bens_annotation_present(presented):
    """Error gate: every presented candidate carries at least one BENS letter."""
    failures = []
    for c in presented:
        letters = c["bens"].upper().split("+")
        if not any(ch in "BENS" for ch in letters):
            failures.append(f"no valid BENS letter in '{c['bens']}': {c['raw'][:80]}")
    return t.CheckResult("bens_annotation_present", not failures, "error", failures)


def check_candidate_line_format(groups):
    """Error gate: every numbered line inside ## Options parses as a candidate."""
    failures = []
    for g in groups:
        for raw in g["malformed"]:
            failures.append(f"malformed candidate line in '{g['name']}': {raw[:80]}")
    return t.CheckResult("candidate_line_format", not failures, "error", failures)


def check_survivor_count(presented):
    """Error gate: 6-10 presented survivors (SKILL Step 5)."""
    n = len(presented)
    ok = SURVIVOR_MIN <= n <= SURVIVOR_MAX
    detail = {} if ok else {"count": n, "expected": f"{SURVIVOR_MIN}-{SURVIVOR_MAX}"}
    return t.CheckResult("survivor_count", ok, "error", detail)


def check_structure_diversity(groups):
    """
    Error gate: 3-5 distinct proven structure groups with unique names
    (SKILL Step 2: different shapes with different pulls, not one shape
    reworded).
    """
    proven = [g for g in groups if not g["wildcard"]]
    failures = []
    if not (GROUPS_MIN <= len(proven) <= GROUPS_MAX):
        failures.append(
            f"{len(proven)} proven structure group(s); need {GROUPS_MIN}-{GROUPS_MAX}"
        )
    seen, dupes = set(), []
    for g in proven:
        key = g["name"].strip().lower()
        if key in seen:
            dupes.append(g["name"])
        seen.add(key)
    if dupes:
        failures.append(f"duplicate structure name(s): {dupes}")
    return t.CheckResult("structure_diversity", not failures, "error", failures)


def check_wildcard_present(groups):
    """
    Error gate: exactly one wildcard group, flagged in its heading, holding
    1-2 swings and NO receipt line (SKILL Step 3: written cold, no pattern
    behind it, flagged as the experiment).
    """
    wilds = [g for g in groups if g["wildcard"]]
    if len(wilds) != 1:
        return t.CheckResult(
            "wildcard_present", False, "error",
            {"wildcard_groups": len(wilds), "expected": 1},
        )
    w = wilds[0]
    failures = []
    if not (1 <= len(w["candidates"]) <= 2):
        failures.append(f"wildcard holds {len(w['candidates'])} candidate(s); need 1-2")
    if w["receipt"] is not None:
        failures.append("wildcard carries a receipt line; it is written cold, no pattern behind it")
    return t.CheckResult("wildcard_present", not failures, "error", failures)


def check_kill_rate(body_text, presented):
    """
    Error gate: the wide pass lists >= 20 candidates and at least half of
    everything written died before presentation (SKILL Step 3: '20 or more
    candidates... Most of what you write should die. The kill rate is where
    quality comes from').
    """
    wide = _wide_pass_count(body_text)
    survivors = len(presented)
    killed = wide - survivors
    failures = []
    if wide < WIDE_PASS_MIN:
        failures.append(f"wide pass has {wide} candidate(s); SKILL writes {WIDE_PASS_MIN} or more")
    elif killed < survivors:
        failures.append(
            f"only {killed} of {wide} written candidates died ({survivors} survived); most must die"
        )
    return t.CheckResult("kill_rate", not failures, "error", failures)


def check_receipt_attached(groups, banks_text, pattern_bank_text):
    """
    Error gate: every proven group pins a real receipt (SKILL Step 2: 'For
    each, note its receipt: the source outlier title, the channel, the
    multiplier'). The quoted outlier must exist in the banks, the @handle must
    exist in the banks, and when the outlier sits on a pattern-bank table row
    the cited multiplier must equal that row's xMed. A receipt that traces to
    nothing is a fabricated proof.
    """
    banks_norm = _normalize(banks_text)
    failures = []
    for g in groups:
        if g["wildcard"]:
            continue
        rec = g["receipt"]
        if rec is None:
            failures.append(f"group '{g['name']}': missing receipt line")
            continue
        if _normalize(rec["title"]) not in banks_norm:
            failures.append(
                f"group '{g['name']}': receipt title not found in banks: \"{rec['title']}\""
            )
        if not _AT_HANDLE_RE.search("@" + rec["handle"]) or (
            "@" + rec["handle"] not in banks_text
        ):
            failures.append(
                f"group '{g['name']}': receipt handle @{rec['handle']} not found in banks"
            )
        # xMed verification against the pattern-bank table row, when present
        row_xmed = None
        norm_title = _normalize(rec["title"])
        for line in pattern_bank_text.splitlines():
            if norm_title in _normalize(line):
                m = _XMED_RE.search(line)
                if m:
                    row_xmed = float(m.group(1))
                break
        if row_xmed is not None and row_xmed != rec["xmed"]:
            failures.append(
                f"group '{g['name']}': cited {rec['xmed']}x but pattern-bank row says "
                f"{row_xmed}x for \"{rec['title']}\""
            )
    return t.CheckResult("receipt_attached", not failures, "error", failures)


def check_power_word_spent(presented, locked_title, power_words):
    """
    Error gate: at least one presented or locked title spends a power word
    from power-words-bank.md (SKILL Step 3 Heat: 'A set with zero hot words
    means the banks were loaded and never spent').
    """
    titles = [c["title"] for c in presented] + ([locked_title] if locked_title else [])
    for title in titles:
        low = title.lower()
        for word in power_words:
            if re.search(r"\b" + re.escape(word.lower()) + r"\b", low):
                return t.CheckResult("power_word_spent", True, "error", {})
    return t.CheckResult(
        "power_word_spent", False, "error",
        {"reason": "no presented or locked title uses a power-words-bank word"},
    )


def check_anti_fabrication(presented, locked_title, lock_list_text, no_numbers):
    """
    Error gate: numbers and all-caps named tokens in titles trace to the lock
    list built from brain-dump.md. For the adversarial case (lock list has NO
    numbers) any digit in any presented or locked title fails.
    """
    failures = []
    lock_lower = lock_list_text.lower()
    titles = [c["title"] for c in presented] + ([locked_title] if locked_title else [])
    for title in titles:
        if no_numbers:
            if _ANY_DIGIT_RE.search(title):
                failures.append(
                    f"ADVERSARIAL: digit in title when the lock list has no numbers: {title}"
                )
        else:
            for n in find_fabricated_numbers(title, lock_list_text):
                failures.append(f"number not in lock list ({n}): {title}")
        for tok in re.findall(r"\b([A-Z]{3,10})\b", title):
            if tok in _CAPS_EMPHASIS_WORDS:
                continue
            if tok.lower() not in lock_lower:
                failures.append(f"all-caps token '{tok}' not in lock list: {title}")
    seen, deduped = set(), []
    for f in failures:
        if f not in seen:
            seen.add(f)
            deduped.append(f)
    return t.CheckResult("anti_fabrication", not deduped, "error", deduped)


def check_no_generic_opener(presented, locked_title):
    """Error gate: no AI-default opener (title-filters.md hard-cut list)."""
    hits = []
    titles = [c["title"] for c in presented] + ([locked_title] if locked_title else [])
    for title in titles:
        low = title.lower()
        for phrase in _GENERIC_OPENERS:
            if phrase in low:
                hits.append(f"blocked opener '{phrase}': {title}")
                break
    return t.CheckResult("no_generic_opener", not hits, "error", hits)


def check_no_colons_pipes(presented, locked_title):
    """Error gate: SKILL Step 4, 'No colons, no pipes' in presented titles."""
    hits = []
    titles = [c["title"] for c in presented] + ([locked_title] if locked_title else [])
    for title in titles:
        if ":" in title or "|" in title:
            hits.append(f"colon or pipe in title: {title}")
    return t.CheckResult("no_colons_pipes", not hits, "error", hits)


def check_lock_list_grounded(body_text, brain_dump_text):
    """
    Error gate: the transcript's ## Lock list exists (>= 2 bullets) and every
    bullet's substance traces verbatim to brain-dump.md. SKILL Step 1 builds
    the lock list FROM the material; a lock-list entry that appears nowhere in
    the brain-dump was invented, and every title built on it inherits the
    fabrication.
    """
    bullets = _transcript_lock_bullets(body_text)
    if bullets is None:
        return t.CheckResult(
            "lock_list_grounded", False, "error", ["## Lock list section not found in transcript.md"]
        )
    if len(bullets) < 2:
        return t.CheckResult(
            "lock_list_grounded", False, "error",
            [f"## Lock list has {len(bullets)} bullet(s); a real lock list has several"],
        )
    dump_norm = _normalize(brain_dump_text)
    failures = []
    for b in bullets:
        substance = b.lstrip("-").strip()
        substance = substance.split("(", 1)[0].strip()
        if not substance:
            continue
        if _normalize(substance) not in dump_norm:
            failures.append(f"lock-list bullet not in brain-dump: {b[:80]}")
    return t.CheckResult("lock_list_grounded", not failures, "error", failures)


def check_recommendation_present(body_text, presented):
    """
    Error gate: ## Recommendation exists and names one of the presented
    candidates (SKILL Step 5: 'Lead with a recommendation and a reason. You
    are a partner with a point of view, not a menu').
    """
    lines = _section_lines(body_text, re.compile(r"^##\s+recommendation\b", re.IGNORECASE))
    if lines is None:
        return t.CheckResult(
            "recommendation_present", False, "error",
            ["## Recommendation section not found in transcript.md"],
        )
    section = _normalize("\n".join(lines))
    for c in presented:
        if _normalize(c["title"]) in section:
            return t.CheckResult("recommendation_present", True, "error", {})
    return t.CheckResult(
        "recommendation_present", False, "error",
        {"reason": "## Recommendation names no presented candidate"},
    )


def _title_strings_file(presented, locked_title):
    """Synthetic 'files' dict scoping brand checks to title strings only."""
    titles = [c["title"] for c in presented] + ([locked_title] if locked_title else [])
    return {"title-strings": "\n".join(titles)}


def evaluate_case(case, files, manifest):
    """Run all assertions for one case. Returns list[CheckResult]."""
    slug = case["slug"]
    no_numbers = bool(case.get("no_numbers", False))

    piece = files.get("piece.md", "")
    transcript = files.get("transcript.md", "")

    fixtures_root = _norm_path(_HERE, manifest["fixtures"])
    input_stage = _norm_path(_HERE, manifest["input_stage"])
    suite_fixtures = _norm_path(_HERE, manifest["suite_fixtures"])

    upstream_piece = _read(_norm_path(suite_fixtures, slug, "piece.md"))
    brain_dump = _read(_norm_path(input_stage, slug, "brain-dump.md"))
    lock_list_text = _parse_lock_list(brain_dump)

    banks_dir = os.path.join(fixtures_root, "banks")
    pattern_bank = _read(os.path.join(banks_dir, "pattern-bank.md"))
    banks_text = pattern_bank + "\n" + _read(os.path.join(banks_dir, "title-bank.md"))
    power_words = _parse_power_words(_read(os.path.join(banks_dir, "power-words-bank.md")))

    _, transcript_body = split_frontmatter(transcript)
    groups = _parse_options(transcript_body) or []
    presented = _presented(groups)

    fm, _ = split_frontmatter(piece)
    locked_title = str(fm.get("title", "") or "").strip()

    results = []

    # Brand gates on the vault file (whole file) and on title strings only.
    vault_files = {"piece.md": piece}
    title_files = _title_strings_file(presented, locked_title)
    em = t.check_no_em_dash(title_files)
    bw = t.check_no_banned_words(title_files)
    results.append(t.check_no_em_dash(vault_files))
    results.append(t.check_no_banned_words(vault_files))
    results.append(t.CheckResult("titles_no_em_dash", em.passed, "error", em.detail))
    results.append(t.CheckResult("titles_no_banned_words", bw.passed, "error", bw.detail))

    # The piece.md save contract (SKILL Step 6) and the no-reargument rule.
    results.append(check_handoff_framing_to_title(upstream_piece))
    results.append(check_title_written(piece))
    results.append(check_last_updated_bumped(upstream_piece, piece))
    results.append(check_piece_fields_preserved(upstream_piece, piece))
    results.append(check_locked_title_valid(piece, presented))

    # The presented set (SKILL Steps 2-5).
    results.append(check_char_ceiling(presented, locked_title))
    results.append(check_char_count_honest(presented))
    results.append(check_bens_annotation_present(presented))
    results.append(check_candidate_line_format(groups))
    results.append(check_survivor_count(presented))
    results.append(check_structure_diversity(groups))
    results.append(check_wildcard_present(groups))
    results.append(check_kill_rate(transcript_body, presented))
    results.append(check_receipt_attached(groups, banks_text, pattern_bank))
    results.append(check_power_word_spent(presented, locked_title, power_words))
    results.append(check_anti_fabrication(presented, locked_title, lock_list_text, no_numbers))
    results.append(check_no_generic_opener(presented, locked_title))
    results.append(check_no_colons_pipes(presented, locked_title))
    results.append(check_lock_list_grounded(transcript_body, brain_dump))
    results.append(check_recommendation_present(transcript_body, presented))

    # Warnings (reported, never gate).
    results.append(check_char_target(presented, locked_title))
    warn_files = dict(vault_files)
    warn_files.update(title_files)
    results.append(t.check_no_aiisms(warn_files))
    results.append(t.check_no_hedge_words(warn_files))

    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    cases = manifest["cases"]

    error_assertions = [
        "no_em_dash", "no_banned_words", "titles_no_em_dash",
        "titles_no_banned_words", "handoff_framing_to_title", "title_written",
        "last_updated_bumped", "piece_fields_preserved", "locked_title_valid",
        "char_ceiling", "char_count_honest", "bens_annotation_present",
        "candidate_line_format", "survivor_count", "structure_diversity",
        "wildcard_present", "kill_rate", "receipt_attached",
        "power_word_spent", "anti_fabrication", "no_generic_opener",
        "no_colons_pipes", "lock_list_grounded", "recommendation_present",
    ]
    warn_assertions = ["char_target", "no_aiisms", "no_hedge_words"]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in error_assertions}
    warn_hits = {a: 0 for a in warn_assertions}

    print(f"--- vid-title Tier A ({len(cases)} cases) ---")

    for case in cases:
        i, slug = case["case"], case["slug"]
        files = _read_case_files(outputs_dir, i)
        if files is None:
            print(f"  case {i:02d} [{slug}]: NO OUTPUT (skipped)")
            continue
        if "piece.md" not in files or "transcript.md" not in files:
            print(f"  case {i:02d} [{slug}]: MISSING piece.md or transcript.md (skipped)")
            continue

        total += 1
        results = evaluate_case(case, files, manifest)
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
    if pass_rate < 1.0:
        sys.exit(1)


if __name__ == "__main__":
    main()
