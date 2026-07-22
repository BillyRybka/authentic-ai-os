#!/usr/bin/env python3
"""
Tier A eval for vid-ideas. The read-only "does it work" judge.
DO NOT MODIFY during an autoresearch loop. Lock it, then optimize the skill.

Reads each run from outputs/case_NN/ (ideas-batch.md, ideas-backlog.md,
seed-packet.md; transcript.md is never scored) and scores it against the
shared foundation fixture plus the SUITE-LOCAL pattern-bank fixture (the only
bank with per-channel raw outlier rows) and, for cases that use it, the
SUITE-LOCAL prior backlog. An output passes Tier A only when every error-level
assertion passes. Warnings are reported but never gate. Prints a per-assertion
breakdown and a final METRIC line the autoresearch optimizer reads.

The produced files per case:
  ideas-batch.md     the surfaced batch, one strict block per idea
  ideas-backlog.md   backlog state after the run (absent when no prior backlog
                     and nothing was flagged; unflagged ideas are never saved)
  seed-packet.md     frontmatter-only handoff to vid-intake
  transcript.md      the conversation (echoes the creator; never scored)

Assertions (error level, gate):
  no_em_dash, no_banned_words, no_fabrication,
  batch_shape          5-6 ideas, exactly 4 anchored + 1-2 flagged swings,
                       3-4 distinct pillars from the creator's foundation
  receipt_valid        every anchored idea's title + @handle + views + xMed
                       traces verbatim to a pattern-bank fixture row
  engine_from_source   the quoted engine is verbatim from the cited source
                       title (the named load-bearing element is real)
  engine_carried       the named engine is detectably carried into the idea
                       line (a load-bearing word or the borrowed number)
  iceberg_gate         every idea carries an on-iceberg verdict; off-iceberg
                       verdicts and off-iceberg topic markers never surface
  backlog_contract     only creator-flagged keeps are saved; prior rows
                       survive; dropped ideas are never re-proposed; a pick
                       from the backlog flips its row to picked
  seed_packet_shape    {idea_title, pillar, top_3_problem, iceberg_fit,
                       anchor} with anchor carrying the FULL receipt (source
                       title + @channel + views + xMed), matching the pick
Warnings (reported only):
  sharpness_proxy      cited source title has digits or a parenthetical but
                       the idea line kept neither (likely engine loss)
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

# --- constants ---

VALID_STATUSES = {"kept", "dropped", "picked", "used"}
VALID_SIGNALS_ANCHORED = {"strong", "moderate"}
VALID_PROBLEMS = {"1", "2", "3", "none"}
SEED_FIELDS = ["idea_title", "pillar", "top_3_problem", "iceberg_fit", "anchor"]
FALLBACK_PILLARS = {"systems", "delegation", "pricing", "mindset"}

# Verdicts containing any of these words mean the idea is off the iceberg.
_OFF_VERDICT_RE = re.compile(r"\b(off|outside|wrong channel|no fit)\b", re.IGNORECASE)

# Tokens too generic to prove an engine survived into the line.
_STOPWORDS = {
    "the", "and", "for", "with", "that", "this", "from", "your", "you",
    "are", "was", "how", "why", "what", "when", "than", "then", "into",
    "over", "under", "their", "they", "them", "our", "out", "not", "all",
    "any", "can", "has", "have", "had", "its", "own", "who", "will",
    "would", "about", "because", "been", "being", "does", "doing", "done",
    "make", "makes", "made", "keep", "keeps", "more", "most", "much",
    "very", "just", "only", "also", "even", "still", "way", "get", "got",
    "new", "now", "use", "used", "using", "one", "my", "his", "her",
    "she", "him", "need", "needs", "want", "wants", "really", "thing",
    "things", "something", "every", "some", "many", "such", "like",
}

# --- parsers ---

_IDEA_HEAD_RE = re.compile(r"^##\s+Idea\s+\d+", re.IGNORECASE)
_BOLD_RE = re.compile(r"^\*\*(.+?)\*\*\s*$")
_RECEIPT_RE = re.compile(
    r'^inspired by:\s*"([^"]+)"\s*\(@([\w-]+),\s*([\d,]+)\s*views?,'
    r"\s*(\d+(?:\.\d+)?)x\s+median\)",
    re.IGNORECASE,
)
_ENGINE_RE = re.compile(r"^engine:\s*(.+)$", re.IGNORECASE)
_ENGINE_QUOTE_RE = re.compile(r'"([^"]+)"')
_SWING_RE = re.compile(r"^swing:\s*(.+)$", re.IGNORECASE)
_META_RE = re.compile(
    r"^Pillar:\s*([^|]+?)\s*\|\s*Iceberg:\s*([^|]+?)\s*\|\s*Signal:\s*"
    r"([^|]+?)\s*(?:\|\s*Problem:\s*(.+?))?\s*$",
    re.IGNORECASE,
)
_BANK_HEAD_RE = re.compile(r"^###\s+.*?\(@([\w-]+)\)")
_BANK_ROW_RE = re.compile(
    r'^\|\s*([\d,]+)\s*\|\s*(\d+(?:\.\d+)?)x\s*\|\s*[0-9-]+\s*\|\s*"?([^"|]+?)"?\s*\|'
)
_ANCHOR_RE = re.compile(
    r'"([^"]+)"\s*\(@([\w-]+),\s*([\d,]+)\s*views?,\s*(\d+(?:\.\d+)?)x'
)


def _normalize(text):
    """Whitespace, quote, and case normalization for substring tracing."""
    s = text.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = re.sub(r"\]\([^)]*\)", "]", s)  # [Title](url) -> [Title]
    s = s.replace("[", "").replace("]", "")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def _digits(text):
    return re.sub(r"[^\d]", "", text)


def _sig_tokens(text):
    """Load-bearing word tokens: alpha, length >= 4, not a generic stopword."""
    return {
        tok
        for tok in re.findall(r"[a-z]+", text.lower())
        if len(tok) >= 4 and tok not in _STOPWORDS
    }


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


def _parse_pattern_bank(text):
    """
    Per-channel outlier rows: normalized title -> {title, handle, views, xmed}.
    Rows live under '### ... (@handle)' channel headings in the fixture bank.
    """
    rows = {}
    handle = None
    for line in text.splitlines():
        s = line.strip()
        hm = _BANK_HEAD_RE.match(s)
        if hm:
            handle = hm.group(1)
            continue
        rm = _BANK_ROW_RE.match(s)
        if rm and handle:
            title = rm.group(3).strip()
            rows[_normalize(title)] = {
                "title": title,
                "handle": handle,
                "views": rm.group(1),
                "xmed": float(rm.group(2)),
            }
    return rows


def _parse_pillars(foundation_text):
    """The creator's content pillars from creator-foundation.md."""
    m = re.search(r"##\s+Content pillars(.*?)(?:\n##\s|\Z)", foundation_text, re.DOTALL | re.IGNORECASE)
    if not m:
        return set(FALLBACK_PILLARS)
    found = {p.lower() for p in re.findall(r"\*\*([a-z][a-z0-9-]*)\*\*", m.group(1))}
    return found or set(FALLBACK_PILLARS)


def _parse_batch(text):
    """
    Parse ideas-batch.md into idea dicts:
      line, receipt (dict|None), engine_core (quoted str|None), engine_raw,
      swing (str|None), pillar, iceberg, signal, problem.
    """
    ideas = []
    current = None
    for line in text.splitlines():
        s = line.strip()
        if _IDEA_HEAD_RE.match(s):
            if current is not None:
                ideas.append(current)
            current = {
                "line": "", "receipt": None, "engine_core": None,
                "engine_raw": None, "swing": None, "pillar": None,
                "iceberg": None, "signal": None, "problem": None,
            }
            continue
        if current is None:
            continue
        bm = _BOLD_RE.match(s)
        if bm and not current["line"]:
            current["line"] = bm.group(1).strip()
            continue
        rm = _RECEIPT_RE.match(s)
        if rm:
            current["receipt"] = {
                "title": rm.group(1), "handle": rm.group(2),
                "views": rm.group(3), "xmed": float(rm.group(4)),
            }
            continue
        em = _ENGINE_RE.match(s)
        if em:
            current["engine_raw"] = em.group(1).strip()
            q = _ENGINE_QUOTE_RE.search(current["engine_raw"])
            current["engine_core"] = q.group(1) if q else None
            continue
        sm = _SWING_RE.match(s)
        if sm:
            current["swing"] = sm.group(1).strip()
            continue
        mm = _META_RE.match(s)
        if mm:
            current["pillar"] = mm.group(1).strip()
            current["iceberg"] = mm.group(2).strip()
            current["signal"] = mm.group(3).strip()
            current["problem"] = (mm.group(4) or "").strip() or None
            continue
    if current is not None:
        ideas.append(current)
    return ideas


def _parse_backlog(text):
    """Backlog table rows: status, date, idea, pillar, problem, receipt."""
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 6:
            continue
        head = cells[0].lower()
        if head in ("status", "") or set(cells[0]) <= {"-", ":", " "}:
            continue
        rows.append({
            "status": head,
            "date": cells[1],
            "idea": cells[2],
            "pillar": cells[3],
            "problem": cells[4],
            "receipt": cells[5],
        })
    return rows


# --- assertion functions ---

def check_batch_shape(ideas, valid_pillars):
    """
    Error gate: 5-6 ideas, exactly 4 anchored to proven raw titles plus 1-2
    flagged swings, spread across 3-4 of the creator's pillars. Every idea
    carries the Pillar/Iceberg/Signal meta line; anchored ideas are STRONG or
    MODERATE, swings are flagged swing and carry no receipt.
    """
    failures = []
    n = len(ideas)
    if not 5 <= n <= 6:
        failures.append(f"{n} idea(s) surfaced; the batch is 5-6")
    anchored = [i for i in ideas if i["receipt"] is not None]
    swings = [i for i in ideas if i["swing"] is not None]
    for i in ideas:
        if not i["line"]:
            failures.append("an idea block has no **idea line**")
        if i["receipt"] is None and i["swing"] is None:
            failures.append(f"neither anchored nor flagged swing: {i['line'][:60]}")
        if i["receipt"] is not None and i["swing"] is not None:
            failures.append(f"swing carries a receipt; swings are unproven: {i['line'][:60]}")
        if i["pillar"] is None or i["iceberg"] is None or i["signal"] is None:
            failures.append(f"missing Pillar/Iceberg/Signal meta line: {i['line'][:60]}")
    if 5 <= n <= 6:
        if len(anchored) != 4:
            failures.append(f"{len(anchored)} anchored idea(s); the default mix is 4 anchored")
        if not 1 <= len(swings) <= 2 or len(swings) + len(anchored) != n:
            failures.append(f"{len(swings)} swing(s); the default mix is 1-2 flagged swings")
    for i in anchored:
        if i["engine_core"] is None:
            failures.append(f"anchored idea names no quoted engine: {i['line'][:60]}")
        if i["signal"] and i["signal"].lower() not in VALID_SIGNALS_ANCHORED:
            failures.append(f"anchored idea signal '{i['signal']}'; must be STRONG or MODERATE: {i['line'][:60]}")
    for i in swings:
        if i["signal"] and i["signal"].lower() != "swing":
            failures.append(f"swing signal '{i['signal']}'; must be flagged swing: {i['line'][:60]}")
    pillars = {i["pillar"].lower() for i in ideas if i["pillar"]}
    bad = pillars - set(valid_pillars)
    if bad:
        failures.append(f"pillar(s) not in the creator's foundation: {sorted(bad)}")
    if not 3 <= len(pillars) <= 4:
        failures.append(f"batch spans {len(pillars)} pillar(s); it ranges across 3-4")
    return t.CheckResult("batch_shape", not failures, "error", failures)


def check_receipt_valid(ideas, bank_rows):
    """
    Error gate: every anchored idea's receipt (title + @handle + views + xMed)
    traces verbatim to a per-channel row in the pattern-bank fixture. An
    invented title, a wrong handle, an invented view count, or a wrong
    multiple is a fabricated signal.
    """
    failures = []
    for i in ideas:
        if i["swing"] is not None:
            continue
        rec = i["receipt"]
        if rec is None:
            failures.append(f"anchored idea has no receipt line: {i['line'][:60]}")
            continue
        row = bank_rows.get(_normalize(rec["title"]))
        if row is None:
            failures.append(f"receipt title not found in pattern-bank: \"{rec['title']}\"")
            continue
        if row["handle"].lower() != rec["handle"].lower():
            failures.append(
                f"receipt handle @{rec['handle']} but the row lives under "
                f"@{row['handle']}: \"{rec['title']}\""
            )
        if _digits(row["views"]) != _digits(rec["views"]):
            failures.append(
                f"receipt views {rec['views']} but the row says {row['views']}: \"{rec['title']}\""
            )
        if row["xmed"] != rec["xmed"]:
            failures.append(
                f"receipt {rec['xmed']}x but the row says {row['xmed']}x: \"{rec['title']}\""
            )
    return t.CheckResult("receipt_valid", not failures, "error", failures)


def check_engine_from_source(ideas):
    """
    Error gate: the engine an anchored idea names (the quoted load-bearing
    element) appears verbatim in the cited source title. A named engine that
    is not a real element of the receipt is an invented rationale.
    """
    failures = []
    for i in ideas:
        if i["receipt"] is None:
            continue
        core = i["engine_core"]
        if core is None:
            failures.append(f"anchored idea names no quoted engine: {i['line'][:60]}")
            continue
        if _normalize(core) not in _normalize(i["receipt"]["title"]):
            failures.append(
                f"engine \"{core}\" is not verbatim from the cited source "
                f"\"{i['receipt']['title']}\""
            )
    return t.CheckResult("engine_from_source", not failures, "error", failures)


def check_engine_carried(ideas):
    """
    Error gate: the named engine is detectably carried into the idea line.
    Two carry routes: (1) the line shares a load-bearing word with the engine
    (alpha token, length >= 4, not generic), or (2) the line keeps the
    engine's number. A dull synonym of the sharp form ('most people' for
    '95%', 'no payroll' for 'Zero Employees') fails both routes: the receipt
    no longer backs the idea, so the citation is decoration.
    """
    failures = []
    for i in ideas:
        if i["receipt"] is None or i["engine_core"] is None:
            continue
        core = i["engine_core"]
        line = i["line"]
        word_hit = bool(_sig_tokens(core) & _sig_tokens(line))
        core_digits = re.findall(r"\d+", core)
        line_digits = set(re.findall(r"\d+", line))
        digit_hit = any(d in line_digits for d in core_digits)
        if not (word_hit or digit_hit):
            failures.append(
                f"engine \"{core}\" not detectably carried into the line "
                f"(dull synonym of the sharp form): {line[:80]}"
            )
    return t.CheckResult("engine_carried", not failures, "error", failures)


def check_iceberg_gate(ideas, off_tokens):
    """
    Error gate: every idea carries a non-empty iceberg verdict, no idea
    surfaces with an off-iceberg verdict, and no idea line contains an
    off-iceberg topic marker (the adversarial trap: huge-view rows from the
    off-lane circle whose TOPICS sit outside the creator's iceberg).
    """
    failures = []
    for i in ideas:
        verdict = (i["iceberg"] or "").strip()
        if not verdict:
            failures.append(f"idea has no iceberg verdict: {i['line'][:60]}")
        elif _OFF_VERDICT_RE.search(verdict):
            failures.append(f"off-iceberg idea surfaced (verdict '{verdict}'): {i['line'][:60]}")
        norm_line = _normalize(i["line"])
        for tok in off_tokens:
            if _normalize(tok) in norm_line:
                failures.append(f"off-iceberg topic marker '{tok}' in idea line: {i['line'][:70]}")
    return t.CheckResult("iceberg_gate", not failures, "error", failures)


def check_backlog_contract(case, ideas, backlog_text, prior_rows):
    """
    Error gate: the backlog is a curated queue. Only ideas the creator flagged
    are saved (status kept, matching a surfaced line); unflagged batch ideas
    never appear; prior rows survive; a dropped idea is never re-proposed in
    the batch; a pick from the backlog flips that row to picked. When there is
    no prior backlog and nothing was flagged, no backlog file is created.
    """
    flags = case.get("flags", [])
    has_prior = bool(case.get("prior_backlog"))
    if backlog_text is None:
        if has_prior or flags:
            return t.CheckResult(
                "backlog_contract", False, "error",
                ["ideas-backlog.md missing though a prior backlog exists or keeps were flagged"],
            )
        return t.CheckResult("backlog_contract", True, "error", {})

    rows = _parse_backlog(backlog_text)
    failures = []
    for r in rows:
        if r["status"] not in VALID_STATUSES:
            failures.append(f"backlog row with invalid status '{r['status']}': {r['idea'][:60]}")

    prior_by_idea = {_normalize(r["idea"]): r for r in prior_rows}
    out_by_idea = {_normalize(r["idea"]): r for r in rows}
    for key, r in prior_by_idea.items():
        if key not in out_by_idea:
            failures.append(f"prior backlog row lost: {r['idea'][:60]}")

    batch_lines = {_normalize(i["line"]) for i in ideas}
    for r in prior_rows:
        if r["status"] == "dropped" and _normalize(r["idea"]) in batch_lines:
            failures.append(f"dropped backlog idea re-proposed: {r['idea'][:60]}")

    flagged_keys = set()
    for num in flags:
        if 1 <= num <= len(ideas):
            flagged_keys.add(_normalize(ideas[num - 1]["line"]))
    new_rows = [r for key, r in out_by_idea.items() if key not in prior_by_idea]
    for r in new_rows:
        key = _normalize(r["idea"])
        if key not in flagged_keys:
            failures.append(f"backlog saved an idea the creator never flagged: {r['idea'][:60]}")
        elif r["status"] != "kept":
            failures.append(f"flagged keep saved with status '{r['status']}', expected kept: {r['idea'][:60]}")
    saved_keys = {_normalize(r["idea"]) for r in new_rows}
    for key in sorted(flagged_keys - saved_keys):
        failures.append(f"creator flagged this idea to keep but it was never saved: {key[:60]}")

    if case.get("pick_from") == "backlog":
        pick_key = _normalize(case.get("pick_backlog_idea", ""))
        row = out_by_idea.get(pick_key)
        if row is None:
            failures.append(f"picked backlog idea not found in ideas-backlog.md: {case.get('pick_backlog_idea')}")
        elif row["status"] != "picked":
            failures.append(f"picked backlog idea has status '{row['status']}'; the pick flips it to picked")
    return t.CheckResult("backlog_contract", not failures, "error", failures)


def check_seed_packet_shape(case, ideas, packet_text, prior_rows, bank_rows):
    """
    Error gate: the handoff to vid-intake carries {idea_title, pillar,
    top_3_problem, iceberg_fit, anchor}, the values match the picked idea, and
    anchor is the FULL receipt (source title + @channel + views + xMed) traced
    verbatim to the pattern-bank row and matching the picked idea's citation.
    """
    if packet_text is None:
        return t.CheckResult(
            "seed_packet_shape", False, "error",
            ["seed-packet.md missing; the pick hands vid-intake a seed packet"],
        )
    failures = []
    fm, _ = split_frontmatter(packet_text)
    for field in SEED_FIELDS:
        val = fm.get(field)
        if val is None or str(val).strip().lower() in ("", "null"):
            failures.append(f"seed packet missing field: {field}")
    if failures:
        return t.CheckResult("seed_packet_shape", False, "error", failures)

    if case.get("pick_from") == "backlog":
        pick_line = case.get("pick_backlog_idea", "")
        prior = {_normalize(r["idea"]): r for r in prior_rows}
        row = prior.get(_normalize(pick_line))
        src_pillar = row["pillar"] if row else None
        src_problem = row["problem"] if row else None
        src_receipt_title = None
        if row:
            m = re.search(r'"([^"]+)"', row["receipt"])
            src_receipt_title = m.group(1) if m else None
    else:
        num = case.get("pick", 0)
        picked = ideas[num - 1] if 1 <= num <= len(ideas) else None
        pick_line = picked["line"] if picked else ""
        src_pillar = picked["pillar"] if picked else None
        src_problem = (picked["problem"] or "none") if picked else None
        src_receipt_title = picked["receipt"]["title"] if picked and picked["receipt"] else None

    if _normalize(str(fm["idea_title"])) != _normalize(pick_line):
        failures.append(f"seed packet idea_title does not match the picked idea: {fm['idea_title']}")
    if src_pillar and str(fm["pillar"]).strip().lower() != src_pillar.strip().lower():
        failures.append(f"seed packet pillar '{fm['pillar']}' != picked idea pillar '{src_pillar}'")
    prob = str(fm["top_3_problem"]).strip().lower()
    if prob not in VALID_PROBLEMS:
        failures.append(f"seed packet top_3_problem '{fm['top_3_problem']}'; must be 1, 2, 3, or none")
    elif src_problem and prob != src_problem.strip().lower():
        failures.append(f"seed packet top_3_problem '{prob}' != picked idea problem tag '{src_problem}'")

    anchor = str(fm["anchor"])
    am = _ANCHOR_RE.search(anchor)
    if not am:
        failures.append(
            "seed packet anchor is not a full receipt (source title + "
            f"@channel + views + xMed): {anchor[:80]}"
        )
    else:
        a_title, a_handle, a_views = am.group(1), am.group(2), am.group(3)
        a_xmed = float(am.group(4))
        row = bank_rows.get(_normalize(a_title))
        if row is None:
            failures.append(f"anchor title not found in pattern-bank: \"{a_title}\"")
        else:
            if row["handle"].lower() != a_handle.lower():
                failures.append(f"anchor handle @{a_handle} but the row lives under @{row['handle']}")
            if _digits(row["views"]) != _digits(a_views):
                failures.append(f"anchor views {a_views} but the row says {row['views']}")
            if row["xmed"] != a_xmed:
                failures.append(f"anchor {a_xmed}x but the row says {row['xmed']}x")
        if src_receipt_title and _normalize(a_title) != _normalize(src_receipt_title):
            failures.append(
                f"anchor source \"{a_title}\" does not match the picked "
                f"idea's cited receipt \"{src_receipt_title}\""
            )
    return t.CheckResult("seed_packet_shape", not failures, "error", failures)


def check_sharpness_proxy(ideas):
    """
    Warning (never gates): when the cited source title carries a number or a
    parenthetical kicker and the idea line kept neither (nor a bracketed
    placeholder like [N]), the bend probably dulled the engine's sharp form.
    """
    flags = []
    for i in ideas:
        if i["receipt"] is None:
            continue
        src = i["receipt"]["title"]
        line = i["line"]
        src_sharp = bool(re.search(r"\d", src)) or "(" in src
        line_sharp = (
            bool(re.search(r"\d", line)) or "(" in line or re.search(r"\[[^\]]*\]", line)
        )
        if src_sharp and not line_sharp:
            flags.append(
                f"source has a number or parenthetical kicker, the line kept "
                f"neither (likely engine loss): {line[:70]}"
            )
    return t.CheckResult("sharpness_proxy", not flags, "warning", flags)


def evaluate_case(case, files, fixtures):
    """Run all assertions for one case. Returns list[CheckResult]."""
    batch_text = files.get("ideas-batch.md", "")
    backlog_text = files.get("ideas-backlog.md")
    packet_text = files.get("seed-packet.md")

    ideas = _parse_batch(batch_text)
    prior_rows = _parse_backlog(fixtures["prior_backlog"]) if case.get("prior_backlog") else []
    off_tokens = case.get("off_iceberg_tokens", [])

    vault_files = {"ideas-batch.md": batch_text}
    if backlog_text is not None:
        vault_files["ideas-backlog.md"] = backlog_text
    if packet_text is not None:
        vault_files["seed-packet.md"] = packet_text

    # Receipts legitimately quote the pattern-bank's own numbers, so the bank,
    # the prior backlog, and the shared foundation are the legitimate source.
    source_text = "\n\n".join(
        p for p in [fixtures["pattern_bank"], fixtures["prior_backlog"], fixtures["foundation"]] if p
    )
    bundle = {
        "files": vault_files,
        "source_text": source_text,
        "fixtures_root": fixtures["shared_root"],
    }

    results = []
    results.append(t.check_no_em_dash(vault_files))
    results.append(t.check_no_banned_words(vault_files))
    results.append(t.check_fabrication(bundle))
    results.append(check_batch_shape(ideas, fixtures["pillars"]))
    results.append(check_receipt_valid(ideas, fixtures["bank_rows"]))
    results.append(check_engine_from_source(ideas))
    results.append(check_engine_carried(ideas))
    results.append(check_iceberg_gate(ideas, off_tokens))
    results.append(check_backlog_contract(case, ideas, backlog_text, prior_rows))
    results.append(check_seed_packet_shape(case, ideas, packet_text, prior_rows, fixtures["bank_rows"]))

    # warnings (reported, never gate)
    results.append(check_sharpness_proxy(ideas))
    results.append(t.check_no_aiisms(vault_files))
    results.append(t.check_no_hedge_words(vault_files))
    return results


def main():
    outputs_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(_HERE, "outputs")
    manifest = _load_manifest()
    cases = manifest["cases"]

    shared_root = _norm_path(_HERE, manifest["fixtures"])
    suite_root = _norm_path(_HERE, manifest["suite_fixtures"])
    pattern_bank = _read(os.path.join(suite_root, "pattern-bank.md"))
    prior_backlog = _read(os.path.join(suite_root, "prior-backlog.md"))
    foundation = _read(os.path.join(shared_root, "foundation", "creator-foundation.md"))
    fixtures = {
        "shared_root": shared_root,
        "pattern_bank": pattern_bank,
        "prior_backlog": prior_backlog,
        "foundation": foundation,
        "bank_rows": _parse_pattern_bank(pattern_bank),
        "pillars": _parse_pillars(foundation),
    }

    error_assertions = [
        "no_em_dash", "no_banned_words", "no_fabrication",
        "batch_shape", "receipt_valid", "engine_from_source",
        "engine_carried", "iceberg_gate", "backlog_contract",
        "seed_packet_shape",
    ]
    warn_assertions = ["sharpness_proxy", "no_aiisms", "no_hedge_words"]

    total = 0
    total_pass = 0
    assertion_pass = {a: 0 for a in error_assertions}
    warn_hits = {a: 0 for a in warn_assertions}

    print(f"--- vid-ideas Tier A ({len(cases)} cases) ---")
    for case in cases:
        i, slug = case["case"], case["slug"]
        files = _read_case_files(outputs_dir, i)
        if files is None:
            print(f"  case {i:02d} [{slug}]: NO OUTPUT (skipped)")
            continue
        if "ideas-batch.md" not in files:
            print(f"  case {i:02d} [{slug}]: MISSING ideas-batch.md (skipped)")
            continue
        total += 1
        results = evaluate_case(case, files, fixtures)
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
    print("  (case_02 is the designed dull-bend failure: it MUST fail engine_carried")
    print("   until a run genuinely carries the engines it cites)")
    print(f"METRIC tier_a_pass_rate={pass_rate:.4f}")


if __name__ == "__main__":
    main()
