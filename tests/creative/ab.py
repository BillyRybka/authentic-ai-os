#!/usr/bin/env python3
"""
Blind A/B harness for creative skills.

The premise: for a creative skill there is no scoring function that stays honest.
A rubric drifts toward whatever it describes, and a judge trained on the rubric
rewards the rubric rather than the work. So the scoreboard here is the creator
picking between two outputs without knowing which is which.

Three jobs:

  new     run two versions of a skill on the same material, blind the results,
          build a review page
  record  store a pick, resolving the blinding afterwards
  bless   promote a picked output to a gold, which every future change is
          measured against

The regression guarantee is `new --baseline gold`. A candidate that loses to a
gold made the skill worse on that case, and it says so before the change lands.

Nothing here scores. It arranges the comparison and remembers the answer.
"""

import argparse
import json
import random
import re
import shutil
import subprocess
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
RUNS = HERE / "runs"
GOLDS = HERE / "golds"
CANDIDATES = HERE / "candidates"
LOCAL_GOLDS = GOLDS / "local"
CASES_FILE = HERE / "cases.json"
LOCAL_CASES_FILE = HERE / "cases.local.json"

# Everything a synthetic arm vault needs to look like a real vault to the skill.
VAULT_PARTS = [
    ("tests/fixtures/shared/foundation", "foundation"),
    ("tests/fixtures/shared/banks", "banks"),
    ("tests/fixtures/shared/people", "people"),
    ("knowledge", "knowledge"),
    ("CLAUDE.md", "CLAUDE.md"),
]

# A local case runs on the creator's real vault. Foundation, banks, people and
# the vault CLAUDE.md come from there; knowledge/ still comes from this repo
# because it is plugin reference material, not creator material.
LOCAL_VAULT_PARTS = ["foundation", "banks", "people", "CLAUDE.md"]


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_cases():
    """
    Synthetic cases from cases.json, plus the creator's real cases from
    cases.local.json when it exists.

    Real material never enters this repo. cases.local.json holds paths only and
    is gitignored, runs/ is gitignored, and golds from local cases land in
    golds/local/ which is gitignored too. The committed corpus stays synthetic.
    """
    cfg = json.loads(CASES_FILE.read_text(encoding="utf-8"))
    for c in cfg["cases"]:
        c["local"] = False

    if LOCAL_CASES_FILE.exists():
        local = json.loads(LOCAL_CASES_FILE.read_text(encoding="utf-8"))
        root = Path(local["vault_root"])
        if not root.exists():
            print(f"warning: local vault_root missing, skipping local cases: {root}")
        else:
            for c in local["cases"]:
                c["local"] = True
                c["vault_root"] = str(root)
                cfg["cases"].append(c)
    return cfg


def is_local(case):
    return bool(case.get("local"))


def gold_path(case_or_slug, local=None):
    if isinstance(case_or_slug, dict):
        slug, local = case_or_slug["slug"], is_local(case_or_slug)
        return (LOCAL_GOLDS if local else GOLDS) / f"{slug}.md"
    return (LOCAL_GOLDS if local else GOLDS) / f"{case_or_slug}.md"


def copy_into(src: Path, dst: Path):
    if not src.exists():
        return False
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    return True


# ---------------------------------------------------------------- build a vault

def build_vault(vault: Path, skill_src: Path, case: dict, cfg: dict):
    """Assemble one isolated vault: material + this arm's skill + one piece.

    The vault is a copy in every case, so a run never writes into the creator's
    real vault even when it is the source.
    """
    vault.mkdir(parents=True, exist_ok=True)
    missing = []

    if is_local(case):
        root = Path(case["vault_root"])
        for part in LOCAL_VAULT_PARTS:
            if not copy_into(root / part, vault / part):
                missing.append(f"{root.name}/{part}")
        # knowledge/ is plugin reference material, always from this repo
        if not copy_into(REPO / "knowledge", vault / "knowledge"):
            missing.append("knowledge")
        stage = root / "pieces" / case["slug"]
    else:
        for src_rel, dst_rel in VAULT_PARTS:
            if not copy_into(REPO / src_rel, vault / dst_rel):
                missing.append(src_rel)
        stage = REPO / cfg["input_stage"] / case["slug"]

    skill_dst = vault / ".claude" / "skills" / cfg["skill"]
    shutil.copytree(skill_src, skill_dst, dirs_exist_ok=True)

    piece_dir = vault / "content" / "pieces" / case["slug"]
    piece_dir.mkdir(parents=True, exist_ok=True)
    if not stage.exists():
        missing.append(str(stage))
    else:
        for f in stage.glob("*.md"):
            shutil.copy2(f, piece_dir / f.name)

    return missing


# ------------------------------------------------------------------- run an arm

def run_arm(vault: Path, case: dict, cfg: dict, model: str, timeout: int):
    """Drive the skill once, headless, and capture what the creator would see."""
    prompt = cfg["prompt"].format(slug=case["slug"], skill=cfg["skill"])

    cmd = [
        "claude", "-p", prompt,
        "--permission-mode", "acceptEdits",
        "--output-format", "json",
        "--setting-sources", "project",
        "--strict-mcp-config",
    ]
    if model:
        cmd += ["--model", model]

    started = now()
    try:
        proc = subprocess.run(
            cmd, cwd=str(vault), capture_output=True, text=True,
            timeout=timeout, encoding="utf-8", errors="replace",
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"timed out after {timeout}s",
                "started": started, "text": ""}

    if proc.returncode != 0:
        return {"ok": False, "error": (proc.stderr or "")[-2000:],
                "started": started, "text": ""}

    text = proc.stdout
    try:
        payload = json.loads(proc.stdout)
        text = payload.get("result", proc.stdout)
    except json.JSONDecodeError:
        pass

    return {"ok": True, "error": None, "started": started, "text": text}


# ------------------------------------------------------------ resolve an arm src

def resolve_arm(spec: str, cfg: dict):
    """An arm is either a skill directory to run, or the frozen golds."""
    if spec == "gold":
        return {"kind": "gold", "path": str(GOLDS), "label": "gold"}
    p = Path(spec)
    if not p.is_absolute():
        p = (REPO / spec).resolve()
    if not (p / "SKILL.md").exists():
        sys.exit(f"not a skill directory (no SKILL.md): {p}")
    return {"kind": "skill", "path": str(p), "label": p.name}


def gold_text(case: dict):
    f = gold_path(case)
    return f.read_text(encoding="utf-8") if f.exists() else None


def gold_meta_file(local: bool):
    return (LOCAL_GOLDS if local else GOLDS) / "golds.json"


def load_gold_meta(local: bool):
    f = gold_meta_file(local)
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}


def save_gold_meta(meta: dict, local: bool):
    f = gold_meta_file(local)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(meta, indent=2), encoding="utf-8")


# -------------------------------------------------------------------- the review

REVIEW_CSS = """
:root { color-scheme: light dark; --bg:#fbfbfa; --fg:#1a1a19; --mut:#6b6b68;
  --line:#e4e4e1; --card:#fff; --accent:#2f6f4e; --warn:#9a4b2f; }
@media (prefers-color-scheme: dark) { :root { --bg:#16171a; --fg:#e9e9e6;
  --mut:#9a9a95; --line:#2c2e33; --card:#1d1f23; --accent:#7fbf9a; --warn:#d98b69; } }
:root[data-theme="dark"] { --bg:#16171a; --fg:#e9e9e6; --mut:#9a9a95;
  --line:#2c2e33; --card:#1d1f23; --accent:#7fbf9a; --warn:#d98b69; }
:root[data-theme="light"] { --bg:#fbfbfa; --fg:#1a1a19; --mut:#6b6b68;
  --line:#e4e4e1; --card:#fff; --accent:#2f6f4e; --warn:#9a4b2f; }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font:16px/1.6 ui-sans-serif,
  -apple-system,"Segoe UI",system-ui,sans-serif; padding:2rem 1.25rem 6rem; }
.wrap { max-width:1400px; margin:0 auto; }
h1 { font-size:1.5rem; margin:0 0 .25rem; letter-spacing:-.01em; }
.sub { color:var(--mut); font-size:.9rem; margin:0 0 2rem; }
.case { border:1px solid var(--line); border-radius:10px; background:var(--card);
  margin:0 0 2rem; overflow:hidden; }
.case > header { padding:.85rem 1.1rem; border-bottom:1px solid var(--line);
  display:flex; flex-wrap:wrap; gap:.75rem; align-items:baseline; }
.case h2 { font-size:1.05rem; margin:0; }
.case .note { color:var(--mut); font-size:.85rem; }
.pair { display:grid; grid-template-columns:1fr 1fr; gap:0; }
@media (max-width:900px) { .pair { grid-template-columns:1fr; } }
.side { padding:1.1rem; min-width:0; }
.side + .side { border-left:1px solid var(--line); }
@media (max-width:900px) { .side + .side { border-left:0; border-top:1px solid var(--line); } }
.side h3 { font-size:.8rem; text-transform:uppercase; letter-spacing:.09em;
  color:var(--mut); margin:0 0 .75rem; font-weight:600; }
pre { white-space:pre-wrap; word-wrap:break-word; margin:0; font:14px/1.65
  ui-monospace,"Cascadia Code",Consolas,monospace; overflow-x:auto; }
.controls { padding:1rem 1.1rem; border-top:1px solid var(--line);
  display:flex; flex-wrap:wrap; gap:.65rem; align-items:center; }
button.pick { font:inherit; font-size:.9rem; padding:.45rem 1.1rem; cursor:pointer;
  border:1px solid var(--line); border-radius:6px; background:transparent; color:var(--fg); }
button.pick[aria-pressed="true"] { border-color:var(--accent); color:var(--accent);
  font-weight:600; }
input.why { flex:1 1 320px; min-width:0; font:inherit; font-size:.9rem;
  padding:.45rem .7rem; border:1px solid var(--line); border-radius:6px;
  background:var(--bg); color:var(--fg); }
.out { position:fixed; left:0; right:0; bottom:0; background:var(--card);
  border-top:1px solid var(--line); padding:.85rem 1.25rem; }
.out pre { max-height:22vh; overflow:auto; font-size:12.5px; color:var(--mut); }
.err { color:var(--warn); font-size:.9rem; }
"""

REVIEW_JS = """
const picks = {};
document.querySelectorAll('button.pick').forEach(b => {
  b.addEventListener('click', () => {
    const c = b.dataset.case;
    document.querySelectorAll(`button.pick[data-case="${c}"]`)
      .forEach(o => o.setAttribute('aria-pressed', String(o === b)));
    picks[c] = b.dataset.side;
    emit();
  });
});
document.querySelectorAll('input.why').forEach(i =>
  i.addEventListener('input', emit));
function emit() {
  const lines = [];
  for (const [c, side] of Object.entries(picks)) {
    const why = (document.querySelector(`input.why[data-case="${c}"]`)?.value || '')
      .replace(/"/g, "'").trim();
    lines.push(`python ab.py record ${RUN_ID} --case ${c} --winner ${side}` +
      (why ? ` --why "${why}"` : ''));
  }
  document.getElementById('cmds').textContent =
    lines.length ? lines.join('\\n') : 'Pick a side to build the commands.';
}
"""


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def build_review(run_dir: Path, manifest: dict):
    """Render the blind page. Arm identity never enters this file."""
    parts = []
    for c in manifest["cases"]:
        if c.get("error"):
            parts.append(
                f'<section class="case"><header><h2>{esc(c["slug"])}</h2>'
                f'<span class="err">skipped: {esc(c["error"])}</span></header></section>')
            continue
        left, right = c["left_text"], c["right_text"]
        parts.append(f"""
<section class="case">
  <header><h2>{esc(c["slug"])}</h2>
  <span class="note">{esc(c.get("note", ""))}</span></header>
  <div class="pair">
    <div class="side"><h3>Option 1</h3><pre>{esc(left)}</pre></div>
    <div class="side"><h3>Option 2</h3><pre>{esc(right)}</pre></div>
  </div>
  <div class="controls">
    <button class="pick" data-case="{esc(c["slug"])}" data-side="left"
      aria-pressed="false">Option 1 is better</button>
    <button class="pick" data-case="{esc(c["slug"])}" data-side="right"
      aria-pressed="false">Option 2 is better</button>
    <input class="why" data-case="{esc(c["slug"])}"
      placeholder="What made it better? One line. This is the useful part.">
  </div>
</section>""")

    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Blind review {esc(manifest["run_id"])}</title>
<style>{REVIEW_CSS}</style></head><body><div class="wrap">
<h1>Blind review</h1>
<p class="sub">{esc(manifest["run_id"])} &middot; {len(manifest["cases"])} cases &middot;
Which one would you actually film? You cannot tell which version is which, and that is the point.</p>
{''.join(parts)}
</div>
<div class="out"><pre id="cmds">Pick a side to build the commands.</pre></div>
<script>const RUN_ID={json.dumps(manifest["run_id"])};{REVIEW_JS}</script>
</body></html>"""
    (run_dir / "review.html").write_text(html, encoding="utf-8")


# ------------------------------------------------------------------- subcommands

def cmd_new(args):
    cfg = load_cases()
    cases = cfg["cases"]
    if args.cases != "all":
        want = set(args.cases.split(","))
        cases = [c for c in cases if c["slug"] in want]
        if not cases:
            sys.exit(f"no cases matched {args.cases}")

    arm_a = resolve_arm(args.baseline, cfg)
    arm_b = resolve_arm(args.candidate, cfg)
    if arm_a["kind"] == "gold" and arm_b["kind"] == "gold":
        sys.exit("both arms are gold; nothing to compare")

    run_id = args.id or datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = RUNS / run_id
    if run_dir.exists() and not args.force:
        sys.exit(f"{run_dir} exists. Pass --force to overwrite or --id to name it.")
    run_dir.mkdir(parents=True, exist_ok=True)

    rng = random.Random(run_id)
    manifest = {
        "run_id": run_id, "created": now(), "skill": cfg["skill"],
        "model": args.model or "(session default)",
        "arms": {"a": arm_a, "b": arm_b}, "cases": [],
    }

    for case in cases:
        slug = case["slug"]
        print(f"[{slug}] ", end="", flush=True)
        entry = {"slug": slug, "note": case.get("note", ""), "local": is_local(case)}

        texts = {}
        failed = None
        for key, arm in (("a", arm_a), ("b", arm_b)):
            if arm["kind"] == "gold":
                t = gold_text(case)
                if t is None:
                    failed = f"no gold for {slug}; bless one first"
                    break
                texts[key] = t
                print("gold ", end="", flush=True)
                continue

            vault = run_dir / f"arm-{key}" / slug / "vault"
            missing = build_vault(vault, Path(arm["path"]), case, cfg)
            if missing:
                entry.setdefault("warnings", []).append(
                    "missing vault parts: " + ", ".join(missing))
            res = run_arm(vault, case, cfg, args.model, args.timeout)
            out_dir = run_dir / f"arm-{key}" / slug
            (out_dir / "output.md").write_text(res["text"], encoding="utf-8")
            (out_dir / "meta.json").write_text(
                json.dumps({k: v for k, v in res.items() if k != "text"}, indent=2),
                encoding="utf-8")
            if not res["ok"]:
                failed = f"arm {key}: {res['error'][:200]}"
                break
            piece = vault / "content" / "pieces" / slug / "piece.md"
            if piece.exists():
                shutil.copy2(piece, out_dir / "piece.md")
            texts[key] = res["text"]
            print("ok ", end="", flush=True)

        if failed:
            entry["error"] = failed
            manifest["cases"].append(entry)
            print(f"FAILED: {failed}")
            continue

        # Blind: which arm lands on which side is decided here and nowhere else.
        left_arm = rng.choice(["a", "b"])
        right_arm = "b" if left_arm == "a" else "a"
        entry.update({
            "left_arm": left_arm, "right_arm": right_arm,
            "left_text": texts[left_arm], "right_text": texts[right_arm],
        })
        manifest["cases"].append(entry)
        print("paired")

    (run_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8")
    build_review(run_dir, manifest)

    ok = [c for c in manifest["cases"] if not c.get("error")]
    print(f"\n{len(ok)}/{len(manifest['cases'])} cases paired")
    print(f"open  {run_dir / 'review.html'}")
    if len(ok) < len(manifest["cases"]):
        print("some cases failed; see manifest.json")


# --------------------------------------------------------------- split a batch

# Heading levels drift between runs (## on one case, ### on another), so match
# the word rather than the level.
_OPTION_RE = re.compile(r"^#{1,4}\s*Option\s*(\d+)\s*[:.\-]?\s*(.*)$", re.I)
_HEADING_RE = re.compile(r"^#{1,4}\s+\S")


def split_framings(text: str):
    """
    Break one batch into its individual framings.

    Returns {"preamble", "framings": [{"n", "title", "body"}], "trailer"}.
    The trailer is the recommendation, the count read, anything after the last
    framing. If no options are found the whole text comes back as one framing,
    so a batch in an unexpected shape still renders and can still be voted on.
    """
    lines = text.splitlines()
    starts = []
    for i, line in enumerate(lines):
        m = _OPTION_RE.match(line)
        if m:
            starts.append((i, m.group(1), m.group(2).strip()))

    if not starts:
        return {"preamble": "", "trailer": "",
                "framings": [{"n": "1", "title": "(whole batch)", "body": text.strip()}]}

    preamble = "\n".join(lines[:starts[0][0]]).strip()

    # The trailer begins at the first heading after the last option that is not
    # itself an option: the recommendation, the count read, whatever follows.
    last_start = starts[-1][0]
    trailer_at = len(lines)
    for i in range(last_start + 1, len(lines)):
        if _HEADING_RE.match(lines[i]) and not _OPTION_RE.match(lines[i]):
            trailer_at = i
            break

    framings = []
    for idx, (line_no, n, title) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else trailer_at
        framings.append({
            "n": n, "title": title,
            "body": "\n".join(lines[line_no + 1:end]).strip(),
        })

    return {"preamble": preamble, "framings": framings,
            "trailer": "\n".join(lines[trailer_at:]).strip()}


# --- shared by the CLI and the browser UI; one implementation, two front doors ---

def load_manifest(run_id: str):
    f = RUNS / run_id / "manifest.json"
    if not f.exists():
        raise FileNotFoundError(f"no run {run_id}")
    return json.loads(f.read_text(encoding="utf-8"))


def load_picks(run_id: str):
    f = RUNS / run_id / "picks.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}


def _derive_winner(manifest, case, entry):
    """
    The side winner falls out of the framing votes rather than being a separate
    decision. More framings you would actually film means the better batch.

    A tie leaves no winner on purpose. Two batches you rate equally is a real
    result, and calling it for one of them would invent a signal that is not
    there. bless skips those.
    """
    votes = entry.get("votes", {})
    tally = {"left": 0, "right": 0}
    for key, v in votes.items():
        if v.get("on"):
            tally[key.split(":", 1)[0]] += 1

    entry["tally"] = tally
    if tally["left"] == tally["right"]:
        entry.update({"side_shown": None, "winner_arm": None,
                      "winner_label": None, "winner_path": None})
        return entry

    side = "left" if tally["left"] > tally["right"] else "right"
    arm_key = case[f"{side}_arm"]
    arm = manifest["arms"][arm_key]
    entry.update({"side_shown": side, "winner_arm": arm_key,
                  "winner_label": arm["label"], "winner_path": arm["path"]})
    return entry


def record_framing_vote(run_id: str, slug: str, side: str, n: str,
                        on: bool, note: str = None):
    """Toggle one framing's vote, then recompute the side winner."""
    manifest = load_manifest(run_id)
    case = next((c for c in manifest["cases"] if c["slug"] == slug), None)
    if case is None:
        raise KeyError(f"no case {slug} in {run_id}")
    if side not in ("left", "right"):
        raise ValueError("side must be left or right")

    picks = load_picks(run_id)
    entry = picks.get(slug, {})
    votes = entry.setdefault("votes", {})
    key = f"{side}:{n}"
    v = votes.setdefault(key, {"on": False, "note": ""})
    v["on"] = bool(on)
    if note is not None:
        v["note"] = note
    if not v["on"] and not v["note"]:
        votes.pop(key, None)

    entry["recorded"] = now()
    _derive_winner(manifest, case, entry)
    picks[slug] = entry
    (RUNS / run_id / "picks.json").write_text(
        json.dumps(picks, indent=2), encoding="utf-8")
    return entry


def record_pick(run_id: str, slug: str, winner: str, why: str = ""):
    """Resolve the blinding for one case and store the pick. Returns the entry."""
    manifest = load_manifest(run_id)
    case = next((c for c in manifest["cases"] if c["slug"] == slug), None)
    if case is None:
        raise KeyError(f"no case {slug} in {run_id}")
    if case.get("error"):
        raise ValueError(f"case {slug} failed to run; nothing to record")
    if winner not in ("left", "right"):
        raise ValueError("winner must be left or right")

    arm_key = case[f"{winner}_arm"]
    arm = manifest["arms"][arm_key]
    picks = load_picks(run_id)
    entry = picks.get(slug, {})
    # An explicit side pick overrides the derived one and says so, so a later
    # reader can tell a deliberate call from a vote count.
    entry.update({
        "winner_arm": arm_key, "winner_label": arm["label"],
        "winner_path": arm["path"], "side_shown": winner,
        "override": True, "why": why or entry.get("why", ""), "recorded": now(),
    })
    picks[slug] = entry
    (RUNS / run_id / "picks.json").write_text(
        json.dumps(picks, indent=2), encoding="utf-8")
    return entry


def set_case_note(run_id: str, slug: str, why: str):
    picks = load_picks(run_id)
    entry = picks.setdefault(slug, {})
    entry["why"] = why
    entry["recorded"] = now()
    (RUNS / run_id / "picks.json").write_text(
        json.dumps(picks, indent=2), encoding="utf-8")
    return entry


def bless_run(run_id: str, slug: str = None):
    """Promote picked outputs to golds. Returns a list of (slug, label, local)."""
    manifest = load_manifest(run_id)
    picks = load_picks(run_id)
    if not picks:
        raise ValueError("no picks recorded in this run")

    slugs = [slug] if slug else list(picks.keys())
    GOLDS.mkdir(parents=True, exist_ok=True)
    # Two ledgers on purpose: the local one names real pieces and carries the
    # creator's own reasons, so it stays beside the local golds and out of git.
    metas = {False: load_gold_meta(False), True: load_gold_meta(True)}
    done, skipped = [], []

    for s in slugs:
        if s not in picks:
            continue
        if not picks[s].get("side_shown"):
            # Tied on votes, or votes cleared. Nothing to freeze, and it must not
            # be reported as frozen: a bless that claims a gold it did not write
            # is the one lie this tool cannot afford.
            skipped.append(s)
            continue
        case = next(c for c in manifest["cases"] if c["slug"] == s)
        text = case[f"{picks[s]['side_shown']}_text"]
        local = bool(case.get("local"))
        dest = gold_path(s, local=local)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        metas[local][s] = {
            "from_run": run_id, "arm": picks[s]["winner_arm"],
            "produced_by": picks[s]["winner_path"], "local": local,
            "why": picks[s]["why"], "blessed": now(),
        }
        done.append((s, picks[s]["winner_label"], local))

    for local, meta in metas.items():
        if meta:
            save_gold_meta(meta, local)
    return done, skipped


def list_runs():
    if not RUNS.exists():
        return []
    out = []
    for r in sorted((p for p in RUNS.iterdir() if p.is_dir()), reverse=True):
        if not (r / "manifest.json").exists():
            continue
        m = json.loads((r / "manifest.json").read_text(encoding="utf-8"))
        picks = load_picks(r.name)
        ok = [c for c in m["cases"] if not c.get("error")]
        out.append({"run_id": r.name, "created": m.get("created", ""),
                    "cases": len(ok), "total": len(m["cases"]),
                    "picks": len(picks), "arms": m["arms"]})
    return out


def cmd_record(args):
    entry = record_pick(args.run_id, args.case, args.winner, args.why or "")
    manifest = load_manifest(args.run_id)
    picks = load_picks(args.run_id)

    print(f"{args.case}: {entry['winner_label']} won ({entry['winner_arm']})")
    if not entry["why"]:
        print("  no reason recorded. In a month the reason is the only part still useful.")

    tally = {}
    for p in picks.values():
        tally[p["winner_label"]] = tally.get(p["winner_label"], 0) + 1
    print("  " + "  ".join(f"{k}: {v}" for k, v in sorted(tally.items()))
          + f"   ({len(picks)}/{len(manifest['cases'])} recorded)")


def cmd_bless(args):
    try:
        done, skipped = bless_run(args.run_id, args.case)
    except (ValueError, FileNotFoundError) as e:
        sys.exit(str(e))
    for slug, label, local in done:
        where = "golds/local" if local else "golds"
        print(f"{slug}: gold set from {label} -> {where}/")
    for slug in skipped:
        print(f"{slug}: no clear winner, nothing frozen")
    n_local = len(load_gold_meta(True))
    total = len(load_gold_meta(False)) + n_local
    print(f"\n{total} golds ({n_local} on real material). Guard a change with:")
    print("  python ab.py new --baseline gold --candidate <skill-dir>")


def cmd_fork(args):
    """Copy the live skill to a candidate you can edit freely.

    The live skill is the baseline and never gets edited to test something. It
    changes only when a candidate wins and you copy it back on purpose.
    """
    cfg = load_cases()
    src = Path(args.source) if args.source else (
        REPO / ".claude" / "skills" / cfg["skill"])
    if not src.is_absolute():
        src = (REPO / src).resolve()
    if not (src / "SKILL.md").exists():
        sys.exit(f"not a skill directory (no SKILL.md): {src}")

    dst = CANDIDATES / args.name
    if dst.exists() and not args.force:
        sys.exit(f"{dst} exists. Pass --force to overwrite.")
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

    print(f"forked {src.name} -> {dst}")
    print("edit that copy. live stays untouched. then:")
    print(f"  python ab.py new --baseline {src.relative_to(REPO).as_posix()} \\")
    print(f"                   --candidate {dst.relative_to(REPO).as_posix()}")


def cmd_serve(args):
    import dashboard
    dashboard.serve(args.port, open_browser=not args.no_open)


def cmd_status(args):
    meta = {**load_gold_meta(False), **load_gold_meta(True)}
    cfg = load_cases()
    n_local = sum(1 for c in cfg["cases"] if is_local(c))
    print(f"skill: {cfg['skill']}   cases: {len(cfg['cases'])} "
          f"({n_local} real)   golds: {len(meta)}\n")
    for c in cfg["cases"]:
        g = meta.get(c["slug"])
        mark = "gold" if g else "  - "
        tag = " [real]" if is_local(c) else ""
        why = f'  "{g["why"]}"' if g and g.get("why") else ""
        print(f"  {mark}  {c['slug']}{tag}{why}")
    if not n_local:
        print("\n  no real cases. add cases.local.json to judge on real material.")

    if not RUNS.exists():
        return
    runs = sorted([p for p in RUNS.iterdir() if p.is_dir()], reverse=True)[:5]
    if runs:
        print("\nrecent runs:")
    for r in runs:
        pf = r / "picks.json"
        n = len(json.loads(pf.read_text(encoding="utf-8"))) if pf.exists() else 0
        print(f"  {r.name}   {n} picks recorded")


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("new", help="run two versions on the same cases, blind them")
    p.add_argument("--baseline", required=True,
                   help="skill dir, or 'gold' to guard against blessed outputs")
    p.add_argument("--candidate", required=True, help="skill dir to test")
    p.add_argument("--cases", default="all", help="comma-separated slugs, or 'all'")
    p.add_argument("--model", default=None, help="e.g. opus, sonnet")
    p.add_argument("--timeout", type=int, default=900)
    p.add_argument("--id", default=None)
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_new)

    p = sub.add_parser("record", help="record a pick (resolves the blinding)")
    p.add_argument("run_id")
    p.add_argument("--case", required=True)
    p.add_argument("--winner", required=True, choices=["left", "right"])
    p.add_argument("--why", default=None)
    p.set_defaults(func=cmd_record)

    p = sub.add_parser("bless", help="promote picked outputs to golds")
    p.add_argument("run_id")
    p.add_argument("--case", default=None, help="one slug, or all picked")
    p.set_defaults(func=cmd_bless)

    p = sub.add_parser("status", help="golds and recent runs")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("fork", help="copy the live skill to an editable candidate")
    p.add_argument("name", help="candidate name, e.g. count-inside-options")
    p.add_argument("--source", default=None, help="skill dir to fork (default: live)")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_fork)

    p = sub.add_parser("serve", help="open the review dashboard in your browser")
    p.add_argument("--port", type=int, default=7654)
    p.add_argument("--no-open", action="store_true", help="do not launch a browser")
    p.set_defaults(func=cmd_serve)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
