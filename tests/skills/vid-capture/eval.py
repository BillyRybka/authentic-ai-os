#!/usr/bin/env python3
"""
Tier A eval for vid-capture. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

vid-capture writes bank entries, not per-video pieces. Each case in
test_cases.json names one capture flow (stage S/M/P/T/F) driven by one seed.
The runner writes each run to outputs/case_NN/ using this flat-folder
convention (mirroring vid-intake's people-*.md convention):

  {entry_type}-{slug}.md   the bank entry written this run. The story-,
                           metaphor-, proof-, testimonial-, framework- prefix
                           stands in for the banks/{type}-bank/ folder.
  people-{Full-Name}.md    people stub created this run, or an "already exists"
                           note when the profile was already in the vault.
  transcript.md            the capture conversation. Never scored for brand
                           rules or fabrication (it legitimately echoes the
                           creator). It IS part of the legitimate source text:
                           a number in an entry must trace to the seed, the
                           persona, or something the creator said on record.

An output passes Tier A only when every error-level assertion passes.

Assertions (error level, gate):
  no_em_dash, no_banned_words, no_fabrication,
  entry_present, entry_frontmatter, status_captured, used_in_empty,
  captured_date_format, enum_values, expected_fields, slug_rules, tag_rules,
  body_sections, visual_consistency, people_links, people_stub,
  dedup_no_duplicate, gap_flagged, verbatim_traceable
Warnings (reported only):
  no_aiisms, no_hedge_words, dedup_prompt_shown

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
from frontmatter import split_frontmatter, has_fields  # noqa: E402

BANK_TYPES = ["story", "metaphor", "proof", "testimonial", "framework"]

# Required frontmatter, enum values, body sections, and required callouts per
# bank type, per knowledge/vault-integration.md, the skill's assets/ templates,
# and knowledge/framework-builder.md ("Entry schema + worked body example",
# which is why framework entries carry `shape` even though vault-integration's
# own framework block does not list it).
SCHEMAS = {
    "story": {
        "required": ["type", "project", "story_type", "illustrates", "themes",
                     "captured", "status", "tags", "used_in"],
        "enums": {"story_type": {"client", "own", "viewer"}},
        "sections": ["problem", "action", "outcome"],
        "callout": "[!tip]",
        "callout_key": "why this story lands",
    },
    "metaphor": {
        "required": ["type", "project", "concept", "category", "visual",
                     "themes", "captured", "status", "tags", "used_in"],
        "enums": {"category": {"food", "cars", "clothes", "sports", "travel", "other"}},
        "sections": ["concept being clarified"],
        "callout": "[!tip]",
        "callout_key": "pivot phrase",
    },
    "proof": {
        "required": ["type", "project", "proof_type", "illustrates", "themes",
                     "captured", "status", "tags", "used_in"],
        "enums": {"proof_type": {"personal-result", "client-win"}},
        "sections": ["what it proves", "the asset", "presentation format", "context"],
        "callout": None,
        "callout_key": None,
    },
    "testimonial": {
        "required": ["type", "project", "source", "illustrates", "themes",
                     "client", "anonymized", "captured", "status", "tags", "used_in"],
        "enums": {"source": {"comment", "dm", "email", "video"}},
        "sections": ["context", "anonymization"],
        "callout": "[!quote]",
        "callout_key": None,
    },
    "framework": {
        "required": ["type", "project", "name", "framework_type", "shape",
                     "components", "problem_it_solves", "themes", "maturity",
                     "captured", "status", "tags", "used_in"],
        "enums": {
            "framework_type": {"process", "categorization", "decision-model", "mental-model"},
            "shape": {"arrows", "pyramid", "cycle", "venn", "funnel", "acronym"},
            "maturity": {"draft", "active", "retired"},
        },
        "sections": ["problem", "components", "shape"],
        "callout": None,
        "callout_key": None,
    },
}

_SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+){2,5}$")  # 3 to 6 hyphenated words
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_TAG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

ERROR_CHECKS = [
    "no_em_dash", "no_banned_words", "no_fabrication",
    "entry_present", "entry_frontmatter", "status_captured", "used_in_empty",
    "captured_date_format", "enum_values", "expected_fields", "slug_rules",
    "tag_rules", "body_sections", "visual_consistency", "people_links",
    "people_stub", "dedup_no_duplicate", "gap_flagged", "verbatim_traceable",
]
WARN_CHECKS = ["no_aiisms", "no_hedge_words", "dedup_prompt_shown"]


# --- small value normalizers (tests/lib/frontmatter.py returns strings when
# --- pyyaml is absent, so booleans and lists arrive as raw text) ---

def _norm(v):
    s = str(v if v is not None else "").strip()
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        s = s[1:-1]
    return s.strip()


def _tags_list(raw):
    if isinstance(raw, list):
        return [str(x).strip() for x in raw]
    s = _norm(raw)
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    return [p.strip().strip('"').strip("'") for p in s.split(",") if p.strip()]


def _headings(text):
    return [
        line.strip().lstrip("#").strip().lower()
        for line in text.splitlines()
        if line.strip().startswith("#")
    ]


# --- loaders ---

def _load_manifest():
    with open(os.path.join(_HERE, "test_cases.json"), encoding="utf-8") as f:
        return json.load(f)


def _load_seeds(manifest):
    """Corpus seeds plus suite-local capture seeds, keyed by slug."""
    corpus_path = os.path.normpath(os.path.join(_HERE, manifest["corpus"]))
    with open(corpus_path, encoding="utf-8") as f:
        seeds = {s["slug"]: s for s in json.load(f)}
    local = manifest.get("local_seeds")
    if local:
        local_path = os.path.normpath(os.path.join(_HERE, local))
        with open(local_path, encoding="utf-8") as f:
            for s in json.load(f):
                seeds[s["slug"]] = s
    return seeds


def _fixtures_root(manifest):
    return os.path.normpath(os.path.join(_HERE, manifest["fixtures"]))


def _source_text(seed, fixtures_root, transcript):
    """
    The only legitimate source for an entry's numbers, links, and claims: the
    seed dump, the persona reveals and withholds, any bank entries the seed
    allows, and the capture transcript itself (the entry is distilled from
    what the creator said on record).
    """
    parts = [seed.get("seed", "")]
    persona = seed.get("persona", {})
    parts += persona.get("reveals", [])
    parts += persona.get("withholds", [])
    for rel in seed.get("bank_pulls_allowed", []):
        bank_path = os.path.join(fixtures_root, "banks", rel + ".md")
        if os.path.exists(bank_path):
            with open(bank_path, encoding="utf-8") as f:
                parts.append(f.read())
    if transcript:
        parts.append(transcript)
    return "\n\n".join(parts)


def _read_case_files(outputs_dir, case_id):
    case_dir = os.path.join(outputs_dir, case_id)
    if not os.path.isdir(case_dir):
        return None
    files = {}
    for name in os.listdir(case_dir):
        if name.endswith(".md"):
            with open(os.path.join(case_dir, name), encoding="utf-8") as f:
                files[name] = f.read()
    return files


# --- per-case evaluation ---

def evaluate_case(case, seed, files, fixtures_root):
    """Run all assertions for one case. Returns list[CheckResult]."""
    entry_type = case["entry_type"]
    schema = SCHEMAS[entry_type]
    transcript = files.get("transcript.md", "")

    entry_files = sorted(
        f for f in files if f.startswith(entry_type + "-") and f.endswith(".md")
    )
    all_entry_files = sorted(
        f for f in files
        if any(f.startswith(p + "-") for p in BANK_TYPES) and f.endswith(".md")
    )
    people_files = {f: txt for f, txt in files.items() if f.startswith("people-")}
    vault_files = {
        f: txt for f, txt in files.items()
        if f in all_entry_files or f in people_files
    }

    source_text = _source_text(seed, fixtures_root, transcript)
    bundle = {"files": vault_files, "source_text": source_text,
              "fixtures_root": fixtures_root}

    results = [
        t.check_no_em_dash(vault_files),
        t.check_no_banned_words(vault_files),
        t.check_fabrication(bundle),
    ]

    def skip(name, level="error"):
        return t.CheckResult(name, True, level, {"skipped": "not applicable for this case"})

    # entry_present: exactly one entry of the expected type (one item at a
    # time, no batching), or zero files at all when the case expects the skill
    # to walk away empty-handed.
    expect = case.get("expect_entry", True)
    if expect:
        ok = len(entry_files) == 1 and len(all_entry_files) == 1
        detail = {} if ok else {"entry_files": entry_files, "all_bank_files": all_entry_files}
    else:
        ok = len(all_entry_files) == 0
        detail = {} if ok else {"unexpected": all_entry_files}
    results.append(t.CheckResult("entry_present", ok, "error", detail))

    entry_name = entry_files[0] if entry_files else None
    entry = files.get(entry_name, "") if entry_name else ""
    fm, body = split_frontmatter(entry)
    headings = _headings(entry)

    # entry_frontmatter
    if entry:
        results.append(t.check_frontmatter_complete(
            "entry_frontmatter", entry, schema["required"]))
    else:
        results.append(skip("entry_frontmatter"))

    # status_captured: capture always starts the lifecycle at `captured`;
    # writing skills move it to `used` later, never vid-capture.
    if entry:
        val = _norm(fm.get("status", "")).lower()
        ok = val == "captured"
        results.append(t.CheckResult("status_captured", ok, "error",
                                     {} if ok else {"status": val}))
    else:
        results.append(skip("status_captured"))

    # used_in_empty: starts []; populated by writing skills only.
    if entry:
        raw = fm.get("used_in", "")
        val = raw if isinstance(raw, list) else _norm(raw)
        ok = val == [] or (isinstance(val, str) and val in ("[]", ""))
        results.append(t.CheckResult("used_in_empty", ok, "error",
                                     {} if ok else {"used_in": str(raw)}))
    else:
        results.append(skip("used_in_empty"))

    # captured_date_format: ISO YYYY-MM-DD, dates live in frontmatter not filenames.
    if entry:
        val = _norm(fm.get("captured", ""))
        ok = bool(_DATE_RE.match(val))
        results.append(t.CheckResult("captured_date_format", ok, "error",
                                     {} if ok else {"captured": val}))
    else:
        results.append(skip("captured_date_format"))

    # enum_values: `type` matches the bank folder, plus per-type enum fields.
    if entry:
        bad = {}
        tv = _norm(fm.get("type", "")).lower()
        if tv != entry_type:
            bad["type"] = tv or "(missing)"
        for field, allowed in schema["enums"].items():
            v = _norm(fm.get(field, "")).lower()
            if v not in allowed:
                bad[field] = v or "(missing)"
        results.append(t.CheckResult("enum_values", not bad, "error", bad))
    else:
        results.append(skip("enum_values"))

    # expected_fields: the specific values this case's material implies
    # (e.g. story_type own, source dm, visual true).
    if entry:
        exp = case.get("expected_fields", {})
        mismatch = {
            k: {"expected": v, "got": _norm(fm.get(k, ""))}
            for k, v in exp.items()
            if _norm(fm.get(k, "")).lower() != str(v).lower()
        }
        results.append(t.CheckResult("expected_fields", not mismatch, "error", mismatch))
    else:
        results.append(skip("expected_fields"))

    # slug_rules: lowercase, hyphenated, 3-6 words, no dates, no redundant
    # type prefix (the folder carries that context).
    if entry:
        slug = entry_name[len(entry_type) + 1:-3]
        problems = []
        if not _SLUG_RE.match(slug):
            problems.append("not 3-6 lowercase hyphenated words")
        if re.search(r"\d{4}", slug):
            problems.append("looks like a year or date")
        if slug.split("-")[0] == entry_type:
            problems.append("redundant type prefix")
        results.append(t.CheckResult("slug_rules", not problems, "error",
                                     {"slug": slug, "problems": problems} if problems else {}))
    else:
        results.append(skip("slug_rules"))

    # tag_rules: required base tags per type, all tags lowercase-hyphenated.
    if entry:
        tags = _tags_list(fm.get("tags", ""))
        required_tags = [entry_type]
        if entry_type == "metaphor":
            cat = _norm(fm.get("category", "")).lower()
            vis = _norm(fm.get("visual", "")).lower() == "true"
            required_tags.append("category-" + cat)
            required_tags.append("visual-metaphor" if vis else "non-visual-metaphor")
        if entry_type == "proof":
            required_tags.append(_norm(fm.get("proof_type", "")).lower())
        if entry_type == "testimonial":
            required_tags.append("source-" + _norm(fm.get("source", "")).lower())
        if entry_type == "framework":
            sh = _norm(fm.get("shape", "")).lower()
            if sh:
                required_tags.append(sh)
        missing = [tg for tg in required_tags if tg and tg not in tags]
        malformed = [tg for tg in tags if not _TAG_RE.match(tg)]
        ok = not missing and not malformed
        detail = {} if ok else {"missing": missing, "malformed": malformed, "tags": tags}
        results.append(t.CheckResult("tag_rules", ok, "error", detail))
    else:
        results.append(skip("tag_rules"))

    # body_sections: required headings plus required callouts per template.
    if entry:
        missing = [k for k in schema["sections"]
                   if not any(k in h for h in headings)]
        callout = schema.get("callout")
        if callout and callout not in entry:
            missing.append("callout " + callout)
        ck = schema.get("callout_key")
        if ck and ck not in entry.lower():
            missing.append("callout text: " + ck)
        results.append(t.CheckResult("body_sections", not missing, "error",
                                     {"missing": missing} if missing else {}))
    else:
        results.append(skip("body_sections"))

    # visual_consistency (metaphor only): visual true needs the two-layer
    # Spoken + Shown body; visual false must stay a single spoken block.
    if entry and entry_type == "metaphor":
        vis = _norm(fm.get("visual", "")).lower() == "true"
        if vis:
            missing = [k for k in ("spoken", "shown")
                       if not any(k in h for h in headings)]
            ok = not missing
            detail = {"missing": missing} if missing else {}
        else:
            ok = not any("shown" in h for h in headings)
            detail = {} if ok else {"unexpected": "Shown section on a non-visual metaphor"}
        results.append(t.CheckResult("visual_consistency", ok, "error", detail))
    else:
        results.append(skip("visual_consistency"))

    # people_links: named clients are wikilinked in BOTH frontmatter `client:`
    # and the body's first mention. Bidirectional or it is an orphan.
    people = case.get("named_people", [])
    if entry and people:
        bad = []
        client_fm = _norm(fm.get("client", ""))
        for p in people:
            link = "[[" + p["name"] + "]]"
            if link not in client_fm:
                bad.append(p["name"] + ": missing from client: frontmatter")
            if link not in body:
                bad.append(p["name"] + ": missing from body first mention")
        results.append(t.CheckResult("people_links", not bad, "error",
                                     {"problems": bad} if bad else {}))
    else:
        results.append(skip("people_links"))

    # people_stub: a stub file with the person schema exists for every newly
    # named client; an already-known client must resolve in the vault people/.
    if people:
        bad = []
        for p in people:
            name = p["name"]
            fname = "people-" + name.replace(" ", "-") + ".md"
            if p.get("stub_expected", False):
                txt = people_files.get(fname)
                if txt is None:
                    bad.append(fname + " not created")
                    continue
                pfm, _ = split_frontmatter(txt)
                okf, miss = has_fields(pfm, ["type", "bucket", "status", "tags"])
                if not okf:
                    bad.append(fname + " missing fields: " + ",".join(miss))
                elif _norm(pfm.get("type", "")).lower() != "person":
                    bad.append(fname + " type is not person")
            else:
                existing = os.path.join(fixtures_root, "people", name + ".md")
                if not os.path.exists(existing):
                    bad.append(name + " not in vault people/ and no stub written")
        results.append(t.CheckResult("people_stub", not bad, "error",
                                     {"problems": bad} if bad else {}))
    else:
        results.append(skip("people_stub"))

    # dedup_no_duplicate: when the captured material matches an existing bank
    # entry, a correct run reuses the existing slug (update) instead of
    # minting a second entry about the same thing.
    dedup = case.get("dedup_against", [])
    if dedup and entry:
        slug = entry_name[len(entry_type) + 1:-3]
        allowed = {rel.split("/", 1)[1] for rel in dedup}
        ok = slug in allowed
        detail = {} if ok else {
            "slug": slug,
            "existing": sorted(allowed),
            "why": "capturing a duplicate must update under the existing slug, not mint a second entry",
        }
        results.append(t.CheckResult("dedup_no_duplicate", ok, "error", detail))
    else:
        results.append(skip("dedup_no_duplicate"))

    # gap_flagged: adversarial honesty. Gaps the creator withheld must be
    # visible as TODOs, in the entry (thin story saved with gaps) or in the
    # transcript (nothing saved at all).
    mode = case.get("gap_flag_in", "")
    if mode == "entry":
        ok = "todo" in entry.lower()
        results.append(t.CheckResult("gap_flagged", ok, "error",
                                     {} if ok else {"missing": "TODO flag inside the entry"}))
    elif mode == "transcript":
        ok = "todo" in transcript.lower()
        results.append(t.CheckResult("gap_flagged", ok, "error",
                                     {} if ok else {"missing": "TODO flag in the transcript"}))
    else:
        results.append(skip("gap_flagged"))

    # verbatim_traceable: distinctive creator phrasings survive into the entry
    # unaltered. Polishing them away erases the voice the bank exists to keep.
    phrases = case.get("verbatim_required", [])
    if entry and phrases:
        r = t.check_verbatim_preserved(entry, phrases)
        results.append(t.CheckResult("verbatim_traceable", r.passed, "error", r.detail))
    else:
        results.append(skip("verbatim_traceable"))

    # warnings (reported, never gate)
    results.append(t.check_no_aiisms(vault_files))
    results.append(t.check_no_hedge_words(vault_files))

    # dedup_prompt_shown (warning): on dedup cases the transcript should show
    # the skill surfacing the existing entry and asking update / new / merge.
    if dedup:
        low = transcript.lower()
        slug_hit = any(rel.split("/", 1)[1] in transcript for rel in dedup)
        word_hit = any(w in low for w in ("already", "existing", "duplicate", "update"))
        ok = slug_hit or word_hit
        results.append(t.CheckResult(
            "dedup_prompt_shown", ok, "warning",
            {} if ok else {"missing": "transcript never surfaces the existing bank entry"}))
    else:
        results.append(skip("dedup_prompt_shown", level="warning"))

    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    seeds = _load_seeds(manifest)
    fixtures_root = _fixtures_root(manifest)
    cases = manifest["cases"]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in ERROR_CHECKS}
    warn_hits = {a: 0 for a in WARN_CHECKS}

    print(f"--- vid-capture Tier A ({len(cases)} cases) ---")
    for case in cases:
        case_id = case["id"]
        seed = seeds.get(case["seed"])
        if seed is None:
            print(f"  {case_id}: ERROR unknown seed '{case['seed']}' (skipped)")
            continue
        files = _read_case_files(outputs_dir, case_id)
        if files is None:
            print(f"  {case_id} [{case['seed']}]: NO OUTPUT (skipped)")
            continue
        total += 1
        results = evaluate_case(case, seed, files, fixtures_root)
        by_name = {r.name: r for r in results}

        if t.gate(results):
            total_pass += 1
        for a in ERROR_CHECKS:
            if by_name[a].passed:
                assertion_pass[a] += 1
        for a in WARN_CHECKS:
            if not by_name[a].passed:
                warn_hits[a] += 1

        print(t.format_case(f"{case_id} [{case['seed']}]", results))

    if total == 0:
        print("\nERROR: no output case folders found under " + outputs_dir)
        print("METRIC tier_a_pass_rate=0.0000")
        sys.exit(1)

    print(f"\n--- Assertion breakdown ({total} scored) ---")
    for a in ERROR_CHECKS:
        pct = assertion_pass[a] / total * 100
        print(f"  {a}: {assertion_pass[a]}/{total} ({pct:.0f}%)")
    print("  warnings (not gating):")
    for a in WARN_CHECKS:
        print(f"    {a}: {warn_hits[a]}/{total} cases had hits")

    pass_rate = total_pass / total
    print(f"\nDETAIL {total_pass}/{total} outputs passed ALL Tier A error checks")
    print(f"METRIC tier_a_pass_rate={pass_rate:.4f}")
    sys.exit(0 if total_pass == total else 1)


if __name__ == "__main__":
    main()
