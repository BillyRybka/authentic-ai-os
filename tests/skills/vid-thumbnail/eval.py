#!/usr/bin/env python3
"""
Tier A eval for vid-thumbnail. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

Reads each run from outputs/case_NN/ (piece.md, transcript.md) and scores it
against the frozen corpus + shared fixtures + the suite-local after-title
stage. An output passes Tier A only when every error-level assertion passes.
Warnings are reported but never gate. Prints a per-assertion breakdown and a
final METRIC line the autoresearch optimizer reads.

vid-thumbnail is thumbnail TEXT only (no visual design). It shows 3-5
candidates against the locked title in chat, the creator picks 1-2, and the
picks save to piece.md as thumbnail_text + thumbnail_shape. Candidates live in
transcript.md only; piece.md holds the locked picks.

Scoping: piece.md is scored whole. From transcript.md only the extracted
candidate texts are scored (for brand rules, word count, pairing, numbers);
the surrounding transcript prose is never checked because it legitimately
echoes the creator's own words.

Case layout (matches test_cases.json, input stage = suite-local
fixtures/after-title because the global stage tree stops at after-intake):
  case_00 -> systems-beat-hustle            (deep-dive; 80 hour weeks + 5 to 1 numbers)
  case_01 -> fired-himself-delegation       (case-study; number is already in the title)
  case_02 -> new-scheduling-feature-reaction(news; no numbers in the material)
  case_03 -> 5-onboarding-mistakes          (listicle; count is already in the title)
  case_04 -> thin-pricing-dump              (ADVERSARIAL: no numbers, any digit fails)
  case_05 -> tempting-numbers-client-story  (ADVERSARIAL: numbers withheld, any digit fails)

Assertions (error level, gate):
  no_em_dash, no_banned_words, no_fabrication, no_fabricated_numbers,
  thumbnail_locked, candidate_count, word_count_cap, pairing_no_overlap,
  no_anti_pattern, picks_from_candidates, pattern_annotation_present,
  handoff_thumbnail_to_structure
Warnings (reported only):
  no_aiisms, no_hedge_words, word_count_ideal, casing_default

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
from check_fabrication import _normalize_numbers  # noqa: E402

# --- constants from knowledge/thumbnail-text-patterns.md ---

# Anti-patterns: automatic rejects (patterns file "Anti-patterns" section).
# Single words match on word boundaries, phrases match as substrings.
_ANTI_PATTERN_WORDS = [
    "roadmap", "blueprint", "unlock", "journey", "framework", "toolkit",
    "maybe", "probably", "might", "could",
    "insane", "revolutionary", "shocked", "game-changer", "life-changing",
]
_ANTI_PATTERN_PHRASES = [
    "the truth about", "mind blown", "game changer",
    "increase productivity", "grow your business", "get results",
]

# Word count: 2-4 preferred, 5 is the ceiling, 6+ auto-rejects (hard rule 1).
WORDS_ERROR = 5   # strictly greater than this fails
WORDS_WARN = 4    # strictly greater than this is flagged

# Candidate line in transcript.md: N. "TEXT" | pattern: <name>
_CANDIDATE_RE = re.compile(r'^\s*(\d+)\.\s*"([^"]+)"\s*(.*)$')
_PATTERN_LABEL_RE = re.compile(r"\bpattern\s*:\s*[^|\s]+", re.IGNORECASE)
_ANY_DIGIT_RE = re.compile(r"\d")

# What vid-structure reads next (suite-local contract; tests/lib/check_handoff.py
# has no thumbnail->structure boundary and lib is locked). vid-structure reads
# the framing fields plus the title it must pay off late; the pipeline routes on
# thumbnail_text. vid-thumbnail appends, it never overwrites.
HANDOFF_PIECE_FIELDS = [
    "type", "slug", "frame", "core_payoff",
    "format", "goal", "title", "thumbnail_text",
]

# Words ignored when testing title-thumbnail overlap. Numbers always count as
# content (repeating the title's number is a package break).
_STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "of", "to", "in", "on", "for",
    "with", "from", "by", "at", "as", "is", "are", "was", "were", "be",
    "been", "being", "do", "does", "did", "done", "have", "has", "had",
    "i", "you", "your", "yours", "my", "me", "mine", "we", "our", "us",
    "they", "them", "their", "it", "its", "he", "she", "him", "his", "her",
    "this", "that", "these", "those", "there", "here", "what", "which",
    "who", "whom", "when", "where", "why", "how", "not", "no", "nor", "so",
    "if", "then", "than", "too", "very", "just", "only", "also", "more",
    "most", "less", "least", "much", "many", "own", "same", "can", "could",
    "will", "would", "should", "shall", "may", "might", "must", "about",
    "into", "over", "under", "again", "once", "out", "up", "down", "off",
    "between", "through", "during", "before", "after", "without", "within",
    "across", "per", "vs", "via", "all", "any", "both", "each", "few",
    "other", "some", "such",
}


def _load_manifest():
    path = os.path.join(_HERE, "test_cases.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _load_corpus(manifest):
    corpus_path = os.path.normpath(os.path.join(_HERE, manifest["corpus"]))
    with open(corpus_path, encoding="utf-8") as f:
        return json.load(f)


def _fixtures_root(manifest):
    return os.path.normpath(os.path.join(_HERE, manifest["fixtures"]))


def _stage_root(manifest):
    return os.path.normpath(os.path.join(_HERE, manifest["input_stage"]))


def _read_if_exists(path):
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def _source_text(seed, fixtures_root, stage_root, slug):
    """
    The only legitimate source for numbers, links, and claims in this video's
    thumbnail text:

      1. The original seed text (the creator's raw dump from the corpus).
      2. The persona reveals (the creator's answers to follow-up questions).
      3. The persona withholds (gap labels only, never approved numbers).
      4. Any bank entries the seed explicitly allows (bank_pulls_allowed).
      5. The after-title stage files for this slug: brain-dump.md (the
         material and its lock-list numbers) and piece.md (the locked title
         and framing fields).

    Mirrors the vid-framing pattern, extended with (5).
    """
    parts = [seed.get("seed", "")]
    persona = seed.get("persona", {})
    parts += persona.get("reveals", [])
    parts += persona.get("withholds", [])
    for rel in seed.get("bank_pulls_allowed", []):
        parts.append(_read_if_exists(os.path.join(fixtures_root, "banks", rel + ".md")))
    stage_dir = os.path.join(stage_root, slug)
    parts.append(_read_if_exists(os.path.join(stage_dir, "brain-dump.md")))
    parts.append(_read_if_exists(os.path.join(stage_dir, "piece.md")))
    return "\n\n".join(p for p in parts if p)


def _read_case_files(outputs_dir, i):
    """Read all .md files from outputs/case_NN/. Returns None if folder missing."""
    case_dir = os.path.join(outputs_dir, f"case_{i:02d}")
    if not os.path.isdir(case_dir):
        return None
    files = {}
    for name in os.listdir(case_dir):
        if name.endswith(".md"):
            with open(os.path.join(case_dir, name), encoding="utf-8") as f:
                files[name] = f.read()
    return files


def _fixture_title(stage_root, slug):
    """The locked title from the after-title fixture piece.md."""
    text = _read_if_exists(os.path.join(stage_root, slug, "piece.md"))
    fm, _ = split_frontmatter(text)
    return str(fm.get("title", "")).strip().strip('"')


# --- candidate + pick extraction helpers ---

def _parse_candidates(transcript_text):
    """
    Parse the shown package from transcript.md: numbered lines in the form
    N. "TEXT" | pattern: <name>. Returns a list of dicts {text, annotation}.

    If the transcript carries more than one numbered block (a regeneration
    before the final shown set), the final block wins: parsing restarts at the
    last line numbered 1, per the output contract in test_cases.json.
    """
    matches = []
    for line in transcript_text.splitlines():
        m = _CANDIDATE_RE.match(line)
        if m:
            matches.append({
                "num": int(m.group(1)),
                "text": m.group(2).strip(),
                "annotation": m.group(3).strip(),
            })
    if not matches:
        return []
    restarts = [i for i, c in enumerate(matches) if c["num"] == 1]
    return matches[restarts[-1]:]


def _fm_list(raw):
    """
    Normalize a frontmatter inline-list field to a list of non-empty strings.
    Handles a real list (pyyaml present), the string form '["a", "b"]' or
    '[a, b]' (minimal parser), and a bare scalar.
    """
    if raw is None:
        return []
    if isinstance(raw, list):
        return [str(x).strip() for x in raw if str(x).strip()]
    s = str(raw).strip()
    if s.lower() in ("", "null", "[]"):
        return []
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        if not inner:
            return []
        items = []
        for m in re.finditer(r'"([^"]*)"|\'([^\']*)\'|([^,]+)', inner):
            val = next(g for g in m.groups() if g is not None)
            val = val.strip().strip('"').strip("'").strip()
            if val:
                items.append(val)
        return items
    return [s.strip('"').strip("'").strip()]


def _locked_picks(piece_text):
    """Return (thumbnail_text list, thumbnail_shape list) from piece.md."""
    fm, _ = split_frontmatter(piece_text)
    return _fm_list(fm.get("thumbnail_text")), _fm_list(fm.get("thumbnail_shape"))


def _content_tokens(text):
    """
    Content tokens for the title-overlap test: lowercased alphanumeric runs,
    stopwords dropped, plural 's' stemmed (both forms indexed). Digits always
    count as content: repeating the title's number is a package break.
    """
    out = set()
    for tok in re.findall(r"[a-z0-9]+", text.lower()):
        if tok.isdigit():
            out.add(tok)
            continue
        if len(tok) < 2 or tok in _STOPWORDS:
            continue
        out.add(tok)
        if tok.endswith("s") and len(tok) > 3:
            out.add(tok[:-1])
    return out


def _scoped_files(piece_text, candidates, picks):
    """
    Build the file dict for brand checks: piece.md whole, plus a synthetic file
    holding only the extracted thumbnail texts (candidates + locked picks).
    Transcript prose stays out of scope; pattern annotations stay out too.
    """
    thumb_texts = [c["text"] for c in candidates] + picks
    return {
        "piece.md": piece_text,
        "thumbnail-text-only": "\n".join(thumb_texts),
    }


# --- skill-specific assertion functions ---

def check_no_fabricated_numbers(candidates, picks, source_text, is_adversarial):
    """
    Error gate: every number in a candidate or locked pick must trace to the
    material, and thumbnail text never carries a wikilink.

    The lib number check runs on body prose, but thumbnail text lives in
    frontmatter and chat, so this suite-local check scans the extracted texts
    directly. Any digit run (not just claim-shaped ones) must appear in the
    source: a "6 HOURS" against a "5 hours" source is fabrication at any size.
    On adversarial seeds the material carries no numbers at all, so any digit
    in a candidate or pick fails with an explicit message.
    """
    failures = []
    source_norm = _normalize_numbers(source_text)
    for kind, texts in (("candidate", [c["text"] for c in candidates]),
                        ("pick", picks)):
        for text in texts:
            if "[[" in text:
                failures.append(f"{kind} carries a wikilink: \"{text}\"")
            if is_adversarial and _ANY_DIGIT_RE.search(text):
                failures.append(
                    f"ADVERSARIAL: digit in {kind} when the material has no numbers: \"{text}\""
                )
                continue
            for digits in sorted(_normalize_numbers(text)):
                if digits not in source_norm:
                    failures.append(
                        f"number not in the material ({digits}): {kind} \"{text}\""
                    )
    seen = set()
    deduped = []
    for f in failures:
        if f not in seen:
            seen.add(f)
            deduped.append(f)
    return t.CheckResult("no_fabricated_numbers", not deduped, "error", deduped)


def check_thumbnail_locked(piece_text):
    """
    Error gate: piece.md frontmatter carries thumbnail_text (1-2 non-empty
    picks) and thumbnail_shape (same count, same order, non-empty pattern
    names). This pair is the skill's only vault write and the pipeline's
    signal that the step is done.
    """
    fm, _ = split_frontmatter(piece_text)
    texts = _fm_list(fm.get("thumbnail_text"))
    shapes = _fm_list(fm.get("thumbnail_shape"))
    problems = []
    if "thumbnail_text" not in fm:
        problems.append("thumbnail_text field missing")
    elif not 1 <= len(texts) <= 2:
        problems.append(f"thumbnail_text must hold 1-2 picks, found {len(texts)}")
    if "thumbnail_shape" not in fm:
        problems.append("thumbnail_shape field missing")
    elif len(shapes) != len(texts):
        problems.append(
            f"thumbnail_shape count {len(shapes)} != thumbnail_text count {len(texts)}"
        )
    if any(not s for s in shapes):
        problems.append("empty thumbnail_shape entry")
    return t.CheckResult(
        "thumbnail_locked", not problems, "error",
        {"problems": problems} if problems else {},
    )


def check_candidate_count(candidates):
    """
    Error gate: the transcript shows 3-5 numbered candidates before locking.
    SKILL.md Step 3: only the strongest 3-5 survive and get shown. The parse
    failing (0 found) means the package was never shown in the contracted
    shape, which is itself the failure.
    """
    n = len(candidates)
    ok = 3 <= n <= 5
    detail = {} if ok else {"count": n, "expected": "3-5"}
    return t.CheckResult("candidate_count", ok, "error", detail)


def check_word_count_cap(candidates, picks):
    """
    Error gate: every candidate and locked pick is at most 5 words.
    Patterns file hard rule 1: 2-4 preferred, 5 is the absolute ceiling,
    6+ auto-rejects. A pure number or arc counts as one unit; whitespace
    tokens are the count.
    """
    failures = []
    for kind, texts in (("candidate", [c["text"] for c in candidates]),
                        ("pick", picks)):
        for text in texts:
            words = len(text.split())
            if words > WORDS_ERROR:
                failures.append(f"{kind} over {WORDS_ERROR} words ({words}): \"{text}\"")
    return t.CheckResult("word_count_cap", not failures, "error", failures)


def check_word_count_ideal(candidates, picks):
    """Warning: flag texts at exactly 5 words (over the 2-4 preferred band)."""
    flags = []
    for kind, texts in (("candidate", [c["text"] for c in candidates]),
                        ("pick", picks)):
        for text in texts:
            words = len(text.split())
            if WORDS_WARN < words <= WORDS_ERROR:
                flags.append(f"{kind} at {words} words (2-4 preferred): \"{text}\"")
    return t.CheckResult("word_count_ideal", not flags, "warning", flags)


def check_pairing_no_overlap(candidates, picks, title):
    """
    Error gate: no candidate or locked pick repeats a title content word.

    Patterns file rule 6 and reject rule 3: the thumbnail adds a second,
    different hook; repeating the title's key words is a package break that
    gets cut before the creator ever sees it. Content words are lowercased,
    stopword-free, plural-stemmed; numbers always count as content. Judged
    against the locked title from the after-title fixture (the title the skill
    was handed).
    """
    title_tokens = _content_tokens(title)
    failures = []
    for kind, texts in (("candidate", [c["text"] for c in candidates]),
                        ("pick", picks)):
        for text in texts:
            shared = sorted(_content_tokens(text) & title_tokens)
            if shared:
                failures.append(
                    f"{kind} repeats title word(s) {shared}: \"{text}\""
                )
    return t.CheckResult("pairing_no_overlap", not failures, "error", failures)


def check_no_anti_pattern(candidates, picks):
    """
    Error gate: no candidate or locked pick hits the anti-pattern list from
    knowledge/thumbnail-text-patterns.md: visual-metaphor words (ROADMAP,
    BLUEPRINT, JOURNEY, FRAMEWORK, TOOLKIT), hedge words (MAYBE, PROBABLY,
    MIGHT, COULD), stock phrases (INSANE, REVOLUTIONARY, LIFE-CHANGING),
    open-mouth language (MIND BLOWN, SHOCKED), and the listed vague/generic
    phrases (THE TRUTH ABOUT, GET RESULTS, ...).
    """
    hits = []
    for kind, texts in (("candidate", [c["text"] for c in candidates]),
                        ("pick", picks)):
        for text in texts:
            low = text.lower()
            for word in _ANTI_PATTERN_WORDS:
                if re.search(r"\b" + re.escape(word) + r"\b", low):
                    hits.append(f"anti-pattern '{word}' in {kind}: \"{text}\"")
            for phrase in _ANTI_PATTERN_PHRASES:
                if phrase in low:
                    hits.append(f"anti-pattern '{phrase}' in {kind}: \"{text}\"")
    return t.CheckResult("no_anti_pattern", not hits, "error", hits)


def check_picks_from_candidates(candidates, picks):
    """
    Error gate: every locked pick appears verbatim in the shown candidate set.
    SKILL.md Step 4: the creator picks 1-2 of the shown options by number, and
    the pick saves verbatim. A pick that was never shown is a consistency
    failure. Comparison is case-insensitive with whitespace collapsed, so only
    real text drift fails.
    """
    shown = {re.sub(r"\s+", " ", c["text"].lower()) for c in candidates}
    failures = []
    for pick in picks:
        if re.sub(r"\s+", " ", pick.lower()) not in shown:
            failures.append(f"locked pick was never shown: \"{pick}\"")
    return t.CheckResult("picks_from_candidates", not failures, "error", failures)


def check_pattern_annotation(candidates):
    """
    Error gate: every shown candidate line carries a pattern label.
    SKILL.md Step 3: each line is the text in quotes plus its pattern name,
    nothing else. The label keeps the set honest about which pattern each
    candidate runs.
    """
    failures = []
    for c in candidates:
        if not _PATTERN_LABEL_RE.search(c["annotation"]):
            failures.append(f"no pattern label: \"{c['text']}\"")
    return t.CheckResult("pattern_annotation_present", not failures, "error", failures)


def check_casing_default(candidates, picks):
    """
    Warning: flag texts that are not ALL CAPS. The default casing is ALL CAPS
    (patterns file rule 9) unless the creator's packaging guardrails say
    otherwise, and these fixtures ship no packaging-system.md override.
    """
    flags = []
    for kind, texts in (("candidate", [c["text"] for c in candidates]),
                        ("pick", picks)):
        for text in texts:
            letters = [ch for ch in text if ch.isalpha()]
            if letters and any(ch.islower() for ch in letters):
                flags.append(f"{kind} not ALL CAPS: \"{text}\"")
    return t.CheckResult("casing_default", not flags, "warning", flags)


def check_handoff_thumbnail_to_structure(piece_text, fixture_title):
    """
    Error gate: piece.md still carries everything vid-structure and the
    pipeline read after this step, and the locked title survived verbatim.

    vid-structure reads frame, core_payoff, format, goal, and the
    title it must pay off late; the pipeline routes on thumbnail_text. The
    skill appends thumbnail_text + thumbnail_shape and never overwrites
    another skill's fields, so the framing fields and the exact title string
    must be present and unchanged from the after-title fixture.
    """
    fm, _ = split_frontmatter(piece_text)
    detail = {}
    ok = True
    missing = [
        f for f in HANDOFF_PIECE_FIELDS
        if f not in fm or str(fm.get(f, "")).strip() in ("", "null", "[]")
    ]
    if missing:
        detail["missing"] = missing
        ok = False
    out_title = str(fm.get("title", "")).strip().strip('"')
    if fixture_title and out_title != fixture_title:
        detail["title_changed"] = {"expected": fixture_title, "got": out_title}
        ok = False
    return t.CheckResult("handoff_thumbnail_to_structure", ok, "error", detail)


def evaluate_case(seed, files, fixtures_root, stage_root):
    """Run all assertions for one case. Returns list[CheckResult]."""
    piece = files.get("piece.md", "")
    transcript = files.get("transcript.md", "")
    slug = seed.get("slug", "")
    is_adversarial = bool(seed.get("is_adversarial"))

    candidates = _parse_candidates(transcript)
    picks, _shapes = _locked_picks(piece)
    fixture_title = _fixture_title(stage_root, slug)

    # piece.md is the only vault file vid-thumbnail writes. transcript.md is
    # excluded from lib checks: it legitimately echoes the creator's words.
    # Candidate and pick texts are checked by the skill-specific assertions.
    vault_files = {"piece.md": piece}
    source_text = _source_text(seed, fixtures_root, stage_root, slug)
    bundle = {
        "files": vault_files,
        "source_text": source_text,
        "fixtures_root": fixtures_root,
    }

    scoped = _scoped_files(piece, candidates, picks)

    results = []
    results.append(t.check_no_em_dash(scoped))
    results.append(t.check_no_banned_words(scoped))
    results.append(t.check_fabrication(bundle))
    results.append(check_no_fabricated_numbers(candidates, picks, source_text, is_adversarial))
    results.append(check_thumbnail_locked(piece))
    results.append(check_candidate_count(candidates))
    results.append(check_word_count_cap(candidates, picks))
    results.append(check_pairing_no_overlap(candidates, picks, fixture_title))
    results.append(check_no_anti_pattern(candidates, picks))
    results.append(check_picks_from_candidates(candidates, picks))
    results.append(check_pattern_annotation(candidates))
    results.append(check_handoff_thumbnail_to_structure(piece, fixture_title))

    # warnings (reported, never gate)
    results.append(t.check_no_aiisms(scoped))
    results.append(t.check_no_hedge_words(scoped))
    results.append(check_word_count_ideal(candidates, picks))
    results.append(check_casing_default(candidates, picks))
    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    corpus = _load_corpus(manifest)
    fixtures_root = _fixtures_root(manifest)
    stage_root = _stage_root(manifest)

    error_assertions = [
        "no_em_dash",
        "no_banned_words",
        "no_fabrication",
        "no_fabricated_numbers",
        "thumbnail_locked",
        "candidate_count",
        "word_count_cap",
        "pairing_no_overlap",
        "no_anti_pattern",
        "picks_from_candidates",
        "pattern_annotation_present",
        "handoff_thumbnail_to_structure",
    ]
    warn_assertions = [
        "no_aiisms",
        "no_hedge_words",
        "word_count_ideal",
        "casing_default",
    ]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in error_assertions}
    warn_hits = {a: 0 for a in warn_assertions}

    print(f"--- vid-thumbnail Tier A ({len(corpus)} seeds) ---")
    for i, seed in enumerate(corpus):
        files = _read_case_files(outputs_dir, i)
        if files is None:
            print(f"  case {i:02d} [{seed['slug']}]: NO OUTPUT (skipped)")
            continue
        if "piece.md" not in files or "transcript.md" not in files:
            print(f"  case {i:02d} [{seed['slug']}]: MISSING piece.md or transcript.md (skipped)")
            continue
        total += 1
        results = evaluate_case(seed, files, fixtures_root, stage_root)
        by_name = {r.name: r for r in results}

        if t.gate(results):
            total_pass += 1
        for a in error_assertions:
            if by_name[a].passed:
                assertion_pass[a] += 1
        for a in warn_assertions:
            if not by_name[a].passed:
                warn_hits[a] += 1

        print(t.format_case(f"{i:02d} [{seed['slug']}]", results))

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
