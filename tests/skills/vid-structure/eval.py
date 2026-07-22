#!/usr/bin/env python3
"""
Tier A eval for vid-structure. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

vid-structure mines the brain-dump into the outline. Each run produces, in
outputs/case_NN/:

  script.md      the skeleton: intro stub, one body section per planned point
                 (each carrying only its picked **Parable:** and **Principle:**
                 plan lines), ending stub, ## To build list, CUTS comment
  piece.md       frontmatter updated: status: drafting, segment_purposes,
                 segments_completed: [], tension_plan, last_updated; every
                 framing field preserved verbatim
  transcript.md  the spine + plan lock conversation. NEVER scored for
                 fabrication or brand rules: it legitimately echoes the
                 creator's own words.

An output passes Tier A only when every error-level assertion passes. Warnings
(AI-isms, hedge words) are reported but never gate. Exits non-zero when any
error-level assertion fails in any scored case (the mid-pipeline model, same
as vid-segment).

Assertions (error level, gate):
  no_em_dash, no_banned_words, no_fabrication,
  script_frontmatter, script_skeleton_shape, section_plan_lines,
  plan_completeness, to_build_rows,
  piece_structure_fields, piece_structure_values, purposes_match_sections,
  tension_plan_names_payoff, piece_fields_preserved,
  handoff_structure_to_intro, expected_links_present, expected_gaps_flagged
Warnings (reported only):
  no_aiisms, no_hedge_words

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

# --- constants per SKILL.md "What it produces" and assets/script-skeleton-template.md ---

# The five piece.md fields vid-structure writes at save time.
STRUCTURE_FIELDS = [
    "segment_purposes", "segments_completed", "tension_plan",
    "status", "last_updated",
]

# piece.md fields vid-structure must never touch: framing locked them, the
# skill is append-only across skills. Compared verbatim against the
# after-framing fixture.
PROTECTED_FIELDS = [
    "type", "slug", "selected_angle", "core_payoff",
    "format", "goal", "voice_context",
]

# Suite-local handoff contract: the piece.md fields vid-intro (and the chain
# after it) reads. vid-intro's Prerequisites demand script.md as the outline
# plus segment_purposes set in piece.md; the rest is what vid-segment and
# vid-ending read next. tests/lib/check_handoff.py is locked, so the
# "structure->intro" contract lives here until the lib catches up. Mirrors the
# HANDOFF_FIELDS pattern in vid-segment/eval.py.
HANDOFF_FIELDS = [
    "type", "slug", "status", "format", "goal", "voice_context",
    "segment_purposes", "segments_completed", "tension_plan", "last_updated",
]

# Parable type vocabulary, from knowledge/parable-decision-matrix.md plus the
# two plan states the skeleton template allows: "none" (an earlier section
# already carried the emotion) and "to build" (the bank had no match). Longer
# tokens first so prefix matching extracts the right remainder.
PARABLE_TYPES = [
    "show-the-problem", "show the problem", "visual demo",
    "breakdown", "contrast", "metaphor", "story", "demo",
    "none", "to build",
]

# A stub section (## Intro, ## Ending) is a placeholder line, never prose.
STUB_MAX_WORDS = 30
# A principle line must state the actual lesson, not a label.
PRINCIPLE_MIN_WORDS = 5
# A picked parable must name its material (or carry a bank wikilink).
MATERIAL_MIN_WORDS = 4


# --- loading helpers ---

def _load_manifest():
    with open(os.path.join(_HERE, "test_cases.json"), encoding="utf-8") as f:
        return json.load(f)


def _load_corpus(manifest):
    path = os.path.normpath(os.path.join(_HERE, manifest["corpus"]))
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _read(rel_root, *parts):
    path = os.path.join(rel_root, *parts)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def _read_case_files(outputs_dir, case_no):
    """Read every .md file under outputs/case_NN/, keyed by path relative to
    the case folder. Returns None if the folder is missing."""
    case_dir = os.path.join(outputs_dir, f"case_{case_no:02d}")
    if not os.path.isdir(case_dir):
        return None
    files = {}
    for root, _dirs, names in os.walk(case_dir):
        for name in names:
            if name.endswith(".md"):
                full = os.path.join(root, name)
                rel = os.path.relpath(full, case_dir).replace(os.sep, "/")
                with open(full, encoding="utf-8") as f:
                    files[rel] = f.read()
    return files


def _source_text(seed, fixtures_root, brain_dump_text, fixture_piece):
    """
    The only legitimate source for numbers, links, and claims in this run:
    the seed, the persona answers, the allowed bank entries, the after-intake
    brain dump, and the after-framing piece.md the skill consumed. Mirrors the
    vid-framing / vid-segment pattern.
    """
    parts = [seed.get("seed", "")]
    persona = seed.get("persona", {})
    parts += persona.get("reveals", [])
    parts += persona.get("withholds", [])
    for rel in seed.get("bank_pulls_allowed", []):
        parts.append(_read(fixtures_root, "banks", rel + ".md"))
    parts.append(brain_dump_text)
    parts.append(fixture_piece)
    return "\n\n".join(p for p in parts if p)


# --- markdown helpers ---

def _norm(s):
    return re.sub(r"\s+", " ", s).strip()


def _sections(body):
    """Split a markdown body into (heading_line, [body_lines]) per ## heading."""
    sections = []
    head = None
    buf = []
    for line in body.splitlines():
        if line.startswith("## "):
            if head is not None:
                sections.append((head, buf))
            head = line.strip()
            buf = []
        elif head is not None:
            buf.append(line)
    if head is not None:
        sections.append((head, buf))
    return sections


def _heading_text(head):
    """'## Mistake 1: No written steps' -> 'mistake 1: no written steps'."""
    return head.lstrip("#").strip().lower()


def _heading_label(head):
    """The section's short label: heading text before any colon."""
    return _heading_text(head).split(":", 1)[0].strip()


def _find_section(sections, name):
    """Exact heading-text match, case-insensitive. Returns (head, lines)."""
    for head, lines in sections:
        if _heading_text(head) == name.lower():
            return head, lines
    return None, None


def _body_sections(sections):
    """The planned point sections: everything between ## Intro and ## Ending."""
    names = [_heading_text(h) for h, _ in sections]
    if "intro" not in names or "ending" not in names:
        return []
    i = names.index("intro")
    j = names.index("ending")
    return sections[i + 1:j]


def _plan_lines(lines):
    """The **Parable:** / **Principle:** lines of a body section."""
    out = []
    for line in lines:
        s = line.strip()
        if s.lower().startswith("**parable:**") or s.lower().startswith("**principle:**"):
            out.append(s)
    return out


def _fm_list(fm, key):
    """Parse a frontmatter field into a list of strings (inline or yaml list)."""
    v = fm.get(key)
    if v is None:
        return []
    if isinstance(v, list):
        return [str(x) for x in v]
    s = str(v).strip()
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        if not inner:
            return []
        return [p.strip().strip('"').strip("'") for p in inner.split(",")]
    return [s.strip('"').strip("'")] if s else []


# --- skill-specific assertions ---

def check_script_frontmatter(script_text, slug):
    """
    script.md frontmatter per assets/script-skeleton-template.md:
    type: script, piece: [[{slug}]], status: outlined, tier, last_refreshed.
    A wrong status or a missing piece link breaks vid-intro's prerequisite
    scan and the vault queries that find the outline.
    """
    fm, _ = split_frontmatter(script_text)
    problems = {}
    for field in ["type", "piece", "status", "tier", "last_refreshed"]:
        v = fm.get(field)
        if v is None or str(v).strip().lower() in ("", "null"):
            problems[field] = "missing"
    if "type" not in problems and str(fm.get("type", "")).strip().lower() != "script":
        problems["type"] = f"want 'script', got {fm.get('type')!r}"
    if "status" not in problems and str(fm.get("status", "")).strip().lower() != "outlined":
        problems["status"] = f"want 'outlined', got {fm.get('status')!r}"
    if "piece" not in problems and slug not in str(fm.get("piece", "")):
        problems["piece"] = f"want a link naming '{slug}', got {fm.get('piece')!r}"
    ok = not problems
    return t.CheckResult("script_frontmatter", ok, "error", problems)


def check_script_skeleton_shape(script_text, case):
    """
    The skeleton shape per the template: an ## Intro stub (placeholder, never
    prose), one body section per planned point, an ## Ending stub, and a
    ## To build heading. Section count and labels come from the case spec:
    they are the mining result this seed must yield, so a dropped, padded, or
    re-labeled point fails here.
    """
    _, body = split_frontmatter(script_text)
    sections = _sections(body)
    problems = {}

    ihead, ilines = _find_section(sections, "intro")
    if ihead is None:
        problems["intro"] = "missing ## Intro"
    else:
        itext = _norm(" ".join(ilines))
        if "vid-intro" not in itext.lower():
            problems["intro"] = "not a stub: no vid-intro placeholder (structure never writes the intro)"
        elif len(itext.split()) > STUB_MAX_WORDS:
            problems["intro"] = f"not a stub: {len(itext.split())} words of prose"

    ehead, elines = _find_section(sections, "ending")
    if ehead is None:
        problems["ending"] = "missing ## Ending"
    else:
        etext = _norm(" ".join(elines))
        if "vid-ending" not in etext.lower():
            problems["ending"] = "not a stub: no vid-ending placeholder (structure never writes the ending)"
        elif len(etext.split()) > STUB_MAX_WORDS:
            problems["ending"] = f"not a stub: {len(etext.split())} words of prose"

    if not any(_heading_text(h).startswith("to build") for h, _ in sections):
        problems["to_build"] = "missing ## To build"

    body_secs = _body_sections(sections)
    want_n = case["expected_section_count"]
    if len(body_secs) != want_n:
        problems["section_count"] = f"want {want_n} body sections, got {len(body_secs)}"
    heads_lower = [_heading_text(h) for h, _ in body_secs]
    missing_labels = [
        label for label in case["expected_section_labels"]
        if not any(label.lower() in h for h in heads_lower)
    ]
    if missing_labels:
        problems["section_labels"] = {"missing": missing_labels}

    ok = not problems
    return t.CheckResult("script_skeleton_shape", ok, "error", problems)


def check_section_plan_lines(script_text):
    """
    Every body section carries exactly its picked plan: a **Parable:** line
    and a **Principle:** line, and nothing else. Any other line is prose (or
    notes) leaking into the outline, which breaks the two-tier split:
    structure plans, vid-segment writes.
    """
    _, body = split_frontmatter(script_text)
    problems = {}
    for head, lines in _body_sections(_sections(body)):
        label = _heading_label(head)
        plans = _plan_lines(lines)
        has_parable = any(p.lower().startswith("**parable:**") for p in plans)
        has_principle = any(p.lower().startswith("**principle:**") for p in plans)
        issues = []
        if not has_parable:
            issues.append("no **Parable:** line")
        if not has_principle:
            issues.append("no **Principle:** line")
        stray = [
            l.strip()[:80] for l in lines
            if l.strip() and not l.strip().lower().startswith(("**parable:**", "**principle:**"))
        ]
        if stray:
            issues.append(f"non-plan lines (prose in the outline): {stray[:3]}")
        if issues:
            problems[label] = issues
    ok = not problems
    return t.CheckResult("section_plan_lines", ok, "error", problems)


def check_plan_completeness(script_text):
    """
    The downstream writer must not need to re-plan. Per body section:
      - the parable line opens with a known type (the decision-matrix
        vocabulary, or 'none', or 'to build')
      - a picked parable names its material: a bank wikilink or a real
        description of the dump material, never a bare type
      - the principle line states the actual lesson (a word floor, so
        '**Principle:** documentation.' fails)
      - wherever a plan line mentions proof, the proof is resolved
        ([[wikilink]]) or honestly flagged (to build / TODO), never vague
    """
    _, body = split_frontmatter(script_text)
    problems = {}
    for head, lines in _body_sections(_sections(body)):
        label = _heading_label(head)
        issues = []
        for p in _plan_lines(lines):
            low = p.lower()
            if low.startswith("**parable:**"):
                rest = p.split("**Parable:**", 1)[-1] if "**Parable:**" in p else p.split(":", 1)[-1]
                rest = rest.strip()
                rest_low = rest.lower()
                ptype = next((tp for tp in PARABLE_TYPES if rest_low.startswith(tp)), None)
                if ptype is None:
                    issues.append(f"parable type not from the matrix vocabulary: {rest[:60]!r}")
                elif ptype not in ("none", "to build"):
                    material = rest[len(ptype):].strip()
                    if "[[" not in material and len(material.split()) < MATERIAL_MIN_WORDS:
                        issues.append(f"parable is a bare type, no material named: {rest[:60]!r}")
            elif low.startswith("**principle:**"):
                rest = p.split(":", 1)[-1].strip()
                if len(rest.split()) < PRINCIPLE_MIN_WORDS:
                    issues.append(f"principle too thin to write from: {rest[:60]!r}")
            if re.search(r"\bproof\b", low):
                if "[[" not in p and "to build" not in low and "todo" not in low:
                    issues.append(f"proof mentioned but neither linked nor flagged: {p[:60]!r}")
        if issues:
            problems[label] = issues
    ok = not problems
    return t.CheckResult("plan_completeness", ok, "error", problems)


def check_to_build_rows(script_text):
    """
    Every 'to build' flag in a section plan lands as a checkbox row in
    ## To build, named by its section. The To build list is the single record
    of what still needs sourcing; a flag with no row is a gap the next skill
    cannot see.
    """
    _, body = split_frontmatter(script_text)
    sections = _sections(body)
    rows = []
    for head, lines in sections:
        if _heading_text(head).startswith("to build"):
            rows = [l.strip().lower() for l in lines if l.strip().startswith("- [ ]")]
            break
    missing = []
    for head, lines in _body_sections(sections):
        plans = _plan_lines(lines)
        if any("to build" in p.lower() for p in plans):
            label = _heading_label(head)
            if not any(label in r for r in rows):
                missing.append(label)
    ok = not missing
    detail = {} if ok else {"flagged_sections_without_rows": missing}
    return t.CheckResult("to_build_rows", ok, "error", detail)


def check_piece_structure_values(piece_text):
    """
    The values vid-structure must write, not just the keys: status flips to
    drafting (the outline exists, prose does not), segments_completed starts
    empty (nothing is written yet), and segment_purposes is a non-empty list
    (the point list the writer works from).
    """
    fm, _ = split_frontmatter(piece_text)
    problems = {}
    status = str(fm.get("status", "")).strip().lower()
    if status != "drafting":
        problems["status"] = f"want 'drafting', got {fm.get('status')!r}"
    completed = _fm_list(fm, "segments_completed")
    if completed:
        problems["segments_completed"] = f"want [], got {completed}"
    purposes = _fm_list(fm, "segment_purposes")
    if not purposes:
        problems["segment_purposes"] = "empty: the point list is the whole deliverable"
    ok = not problems
    return t.CheckResult("piece_structure_values", ok, "error", problems)


def check_purposes_match_sections(piece_text, script_text):
    """
    piece.md and script.md agree: one body section per segment_purposes entry,
    and each purpose's label (the text before any colon) shows up in a body
    heading. vid-segment reads the purpose list to know what to write and the
    skeleton to know where to write it; a drift between the two strands it.
    """
    fm, _ = split_frontmatter(piece_text)
    purposes = _fm_list(fm, "segment_purposes")
    _, body = split_frontmatter(script_text)
    body_secs = _body_sections(_sections(body))
    heads_lower = [_heading_text(h) for h, _ in body_secs]
    problems = {}
    if len(purposes) != len(body_secs):
        problems["count"] = f"{len(purposes)} purposes vs {len(body_secs)} body sections"
    unmatched = [
        p for p in purposes
        if not any(p.split(":", 1)[0].strip().lower() in h for h in heads_lower)
    ]
    if unmatched:
        problems["unmatched_purposes"] = unmatched
    ok = not problems
    return t.CheckResult("purposes_match_sections", ok, "error", problems)


def check_tension_plan_names_payoff(piece_text, script_text):
    """
    tension_plan is the setup/payoff plan: central question, which point pays
    off the title, any threads. A plan that never names a body point cannot
    tell the writer where the title pays off, so at least one body-section
    label must appear in it. Proxy for 'which point pays off the title', not a
    full quality read (that is Tier B).
    """
    fm, _ = split_frontmatter(piece_text)
    plan = str(fm.get("tension_plan", "")).lower()
    _, body = split_frontmatter(script_text)
    labels = [_heading_label(h) for h, _ in _body_sections(_sections(body))]
    found = [l for l in labels if l and l in plan]
    ok = bool(plan.strip()) and bool(found)
    detail = {} if ok else {"tension_plan": plan[:120], "section_labels": labels}
    return t.CheckResult("tension_plan_names_payoff", ok, "error", detail)


def check_piece_fields_preserved(fixture_piece, output_piece):
    """
    Append-only discipline: the fields framing owns (angle, payoff, format,
    goal, voice_context) must be byte-identical to the after-framing fixture
    after normalization. Structure never re-locks them.
    """
    f_fm, _ = split_frontmatter(fixture_piece)
    o_fm, _ = split_frontmatter(output_piece)
    changed = []
    for field in PROTECTED_FIELDS:
        fv = _norm(str(f_fm.get(field, "")))
        ov = _norm(str(o_fm.get(field, "")))
        if fv != ov:
            changed.append({"field": field, "was": fv[:80], "now": ov[:80]})
    ok = not changed
    return t.CheckResult(
        "piece_fields_preserved", ok, "error", {"changed": changed} if changed else {}
    )


def check_expected_links(script_text, case):
    """
    Blocks are picked, not surfaced. The brain-dump names specific bank
    material for specific points (case spec), so the built plan must cite
    those exact wikilinks. A missing link means the skill dropped material the
    creator already captured; the universal no_fabrication check gates the
    opposite direction (invented links).
    """
    missing = [link for link in case.get("expected_links", []) if link not in script_text]
    ok = not missing
    detail = {} if ok else {"missing": missing}
    return t.CheckResult("expected_links_present", ok, "error", detail)


def check_expected_gaps_flagged(script_text, case):
    """
    The adversarial direction: where the banks and the dump have no material,
    the plan must name the gap, not fill it. Each case-spec'd section must
    carry a to-build flag in its plan lines and a matching ## To build row.
    A run that 'helpfully' invents the proof fails here and on no_fabrication.
    """
    _, body = split_frontmatter(script_text)
    sections = _sections(body)
    rows = []
    for head, lines in sections:
        if _heading_text(head).startswith("to build"):
            rows = [l.strip().lower() for l in lines if l.strip().startswith("- [ ]")]
            break
    problems = {}
    for label in case.get("expected_to_build", []):
        target = None
        for head, lines in _body_sections(sections):
            if label.lower() in _heading_text(head):
                target = (head, lines)
                break
        issues = []
        if target is None:
            issues.append("section missing")
        else:
            plans = _plan_lines(target[1])
            if not any("to build" in p.lower() or "todo" in p.lower() for p in plans):
                issues.append("no to-build flag in plan lines (gap was filled, not named)")
        if not any(label.lower() in r for r in rows):
            issues.append("no ## To build row names this section")
        if issues:
            problems[label] = issues
    ok = not problems
    return t.CheckResult("expected_gaps_flagged", ok, "error", problems)


# --- case evaluation ---

def evaluate_case(case, seed, files, fixtures_root, input_stage_root, suite_fixtures_root):
    slug = case["slug"]
    script = files.get("script.md", "")
    piece = files.get("piece.md", "")

    fixture_piece = _read(suite_fixtures_root, slug, "piece.md")
    brain_dump = _read(input_stage_root, slug, "brain-dump.md")

    # transcript.md is excluded everywhere: it legitimately echoes the creator.
    vault_files = {k: v for k, v in files.items() if k != "transcript.md"}

    source_text = _source_text(seed, fixtures_root, brain_dump, fixture_piece)
    bundle = {
        "files": vault_files,
        "source_text": source_text,
        "fixtures_root": fixtures_root,
    }

    results = []
    # universal brand + fabrication spine
    results.append(t.check_no_em_dash(vault_files))
    results.append(t.check_no_banned_words(vault_files))
    results.append(t.check_fabrication(bundle))

    # script.md: the skeleton and the per-point plan
    results.append(check_script_frontmatter(script, slug))
    results.append(check_script_skeleton_shape(script, case))
    results.append(check_section_plan_lines(script))
    results.append(check_plan_completeness(script))
    results.append(check_to_build_rows(script))
    results.append(check_expected_links(script, case))
    results.append(check_expected_gaps_flagged(script, case))

    # piece.md: the save contract, the values, and the cross-file agreement
    results.append(
        t.check_frontmatter_complete("piece_structure_fields", piece, STRUCTURE_FIELDS)
    )
    results.append(check_piece_structure_values(piece))
    results.append(check_purposes_match_sections(piece, script))
    results.append(check_tension_plan_names_payoff(piece, script))
    results.append(check_piece_fields_preserved(fixture_piece, piece))
    results.append(
        t.check_frontmatter_complete("handoff_structure_to_intro", piece, HANDOFF_FIELDS)
    )

    # warnings (reported, never gate)
    results.append(t.check_no_aiisms(vault_files))
    results.append(t.check_no_hedge_words(vault_files))
    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    corpus = _load_corpus(manifest)
    fixtures_root = os.path.normpath(os.path.join(_HERE, manifest["fixtures"]))
    input_stage_root = os.path.normpath(os.path.join(_HERE, manifest["input_stage"]))
    suite_fixtures_root = os.path.normpath(os.path.join(_HERE, manifest["suite_fixtures"]))
    cases = manifest["cases"]

    error_assertions = [
        "no_em_dash",
        "no_banned_words",
        "no_fabrication",
        "script_frontmatter",
        "script_skeleton_shape",
        "section_plan_lines",
        "plan_completeness",
        "to_build_rows",
        "expected_links_present",
        "expected_gaps_flagged",
        "piece_structure_fields",
        "piece_structure_values",
        "purposes_match_sections",
        "tension_plan_names_payoff",
        "piece_fields_preserved",
        "handoff_structure_to_intro",
    ]
    warn_assertions = ["no_aiisms", "no_hedge_words"]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in error_assertions}
    warn_hits = {a: 0 for a in warn_assertions}

    print(f"--- vid-structure Tier A ({len(cases)} cases) ---")
    for case in cases:
        i = case["case"]
        slug = case["slug"]
        files = _read_case_files(outputs_dir, i)
        if files is None:
            print(f"  case {i:02d} [{slug}]: NO OUTPUT (skipped)")
            continue
        if "script.md" not in files or "piece.md" not in files:
            print(f"  case {i:02d} [{slug}]: MISSING script.md or piece.md (skipped)")
            continue
        seed = corpus[case["seed_index"]]
        total += 1
        results = evaluate_case(
            case, seed, files, fixtures_root, input_stage_root, suite_fixtures_root
        )
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
    sys.exit(0 if total_pass == total else 1)


if __name__ == "__main__":
    main()
