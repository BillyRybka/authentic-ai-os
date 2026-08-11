#!/usr/bin/env python3
"""
The review dashboard. `python ab.py serve` and it opens in your browser.

Reads runs off disk on every request, so it is always current: leave the tab
open, start a run in another terminal, refresh, the new run is there. Picks and
blesses POST straight back and write the same files the CLI writes, because both
front doors call the same functions in ab.py.

Stdlib only. Binds to localhost.
"""

import html
import json
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

import ab

CSS = """
:root { color-scheme: light dark; --bg:#fbfbfa; --fg:#1a1a19; --mut:#6b6b68;
  --line:#e4e4e1; --card:#fff; --accent:#2f6f4e; --accent-bg:#eaf4ee;
  --warn:#9a4b2f; --gold:#8a6d1f; --gold-bg:#faf4e2; }
@media (prefers-color-scheme: dark) { :root { --bg:#141518; --fg:#e9e9e6;
  --mut:#9a9a95; --line:#2a2c31; --card:#1c1e22; --accent:#7fbf9a;
  --accent-bg:#1d2b24; --warn:#d98b69; --gold:#d8bd76; --gold-bg:#2a2519; } }
:root[data-theme="dark"] { --bg:#141518; --fg:#e9e9e6; --mut:#9a9a95;
  --line:#2a2c31; --card:#1c1e22; --accent:#7fbf9a; --accent-bg:#1d2b24;
  --warn:#d98b69; --gold:#d8bd76; --gold-bg:#2a2519; }
:root[data-theme="light"] { --bg:#fbfbfa; --fg:#1a1a19; --mut:#6b6b68;
  --line:#e4e4e1; --card:#fff; --accent:#2f6f4e; --accent-bg:#eaf4ee;
  --warn:#9a4b2f; --gold:#8a6d1f; --gold-bg:#faf4e2; }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font:16px/1.6 ui-sans-serif,
  -apple-system,"Segoe UI",system-ui,sans-serif; padding:2rem 1.25rem 5rem; }
.wrap { max-width:1400px; margin:0 auto; }
a { color:var(--accent); }
h1 { font-size:1.45rem; margin:0 0 .3rem; letter-spacing:-.01em; }
.sub { color:var(--mut); font-size:.9rem; margin:0 0 2rem; }
.sub code { background:var(--card); border:1px solid var(--line); border-radius:4px;
  padding:.1rem .35rem; font-size:.85em; }
.card { border:1px solid var(--line); border-radius:10px; background:var(--card);
  margin:0 0 1.5rem; overflow:hidden; }
.card > header { padding:.85rem 1.1rem; border-bottom:1px solid var(--line);
  display:flex; flex-wrap:wrap; gap:.6rem 1rem; align-items:baseline; }
.card h2 { font-size:1rem; margin:0; }
.note { color:var(--mut); font-size:.85rem; }
.pill { font-size:.72rem; text-transform:uppercase; letter-spacing:.08em;
  padding:.14rem .5rem; border-radius:99px; border:1px solid var(--line);
  color:var(--mut); }
.pill.real { color:var(--accent); border-color:var(--accent); }
.pill.gold { color:var(--gold); border-color:var(--gold); background:var(--gold-bg); }
.pair { display:grid; grid-template-columns:1fr 1fr; }
@media (max-width:980px) { .pair { grid-template-columns:1fr; } }
.side { padding:1.1rem; min-width:0; }
.side + .side { border-left:1px solid var(--line); }
@media (max-width:980px) { .side + .side { border-left:0; border-top:1px solid var(--line); } }
.side h3 { font-size:.78rem; text-transform:uppercase; letter-spacing:.09em;
  color:var(--mut); margin:0 0 .8rem; font-weight:600; display:flex;
  justify-content:space-between; align-items:baseline; gap:.5rem; }
.cnt { text-transform:none; letter-spacing:0; font-weight:500; }
.fr { border:1px solid var(--line); border-radius:8px; padding:.75rem .85rem;
  margin:0 0 .8rem; }
.fr.on { border-color:var(--accent); background:var(--accent-bg); }
.fr-head { display:flex; gap:.6rem; align-items:center; margin:0 0 .5rem;
  flex-wrap:wrap; }
.fr-head strong { font-size:.95rem; }
button.vote { font-size:.76rem; padding:.22rem .6rem; white-space:nowrap; }
input.fnote { width:100%; margin:.6rem 0 0; font:inherit; font-size:.83rem;
  padding:.35rem .6rem; border:1px solid var(--line); border-radius:5px;
  background:var(--bg); color:var(--fg); }
.fr.on input.fnote { border-color:var(--accent); }
details.rest { margin:.4rem 0 0; }
details.rest summary { cursor:pointer; color:var(--mut); font-size:.83rem;
  padding:.4rem 0; }
details.rest pre { margin:.5rem 0 0; font-size:12.5px; color:var(--mut); }
.verdict { margin-left:auto; }
pre { white-space:pre-wrap; word-wrap:break-word; margin:0; font:13.5px/1.65
  ui-monospace,"Cascadia Code",Consolas,monospace; overflow-x:auto; }
.controls { padding:.9rem 1.1rem; border-top:1px solid var(--line);
  display:flex; flex-wrap:wrap; gap:.6rem; align-items:center; }
button { font:inherit; font-size:.88rem; padding:.42rem 1rem; cursor:pointer;
  border:1px solid var(--line); border-radius:6px; background:transparent;
  color:var(--fg); }
button:hover { border-color:var(--accent); }
button[aria-pressed="true"] { border-color:var(--accent); color:var(--accent);
  background:var(--accent-bg); font-weight:600; }
button.primary { border-color:var(--accent); color:var(--accent); }
input.why { flex:1 1 340px; min-width:0; font:inherit; font-size:.88rem;
  padding:.42rem .7rem; border:1px solid var(--line); border-radius:6px;
  background:var(--bg); color:var(--fg); }
.saved { color:var(--accent); font-size:.82rem; opacity:0; transition:opacity .2s; }
.saved.on { opacity:1; }
.err { color:var(--warn); font-size:.88rem; }
table { width:100%; border-collapse:collapse; }
td, th { text-align:left; padding:.6rem 1.1rem; border-bottom:1px solid var(--line);
  font-size:.9rem; }
th { color:var(--mut); font-weight:600; font-size:.78rem; text-transform:uppercase;
  letter-spacing:.07em; }
tr:last-child td { border-bottom:0; }
.bar { display:flex; gap:.6rem; align-items:center; margin:0 0 1.5rem;
  flex-wrap:wrap; }
.empty { padding:2.5rem 1.1rem; text-align:center; color:var(--mut); }
"""

SHELL = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{css}</style></head><body><div class="wrap">{body}</div>
<script>{js}</script></body></html>"""

RUN_JS = """
const RUN = document.body.dataset.run;
async function post(path, payload) {
  const r = await fetch(path, {method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify(payload)});
  if (!r.ok) { alert('failed: ' + await r.text()); return null; }
  return r.json();
}
function flash(slug) {
  const el = document.querySelector(`.saved[data-case="${slug}"]`);
  if (!el) return;
  el.classList.add('on'); setTimeout(()=>el.classList.remove('on'), 1200);
}
function paint(slug, res) {
  const t = res.tally || {left:0, right:0};
  const card = document.querySelector(`.card[data-case="${slug}"]`);
  if (!card) return;
  card.querySelectorAll('.cnt').forEach(c =>
    c.textContent = t[c.dataset.side] + ' picked');
  const v = card.querySelector('.verdict');
  if (t.left === t.right) {
    v.innerHTML = (t.left || t.right)
      ? '<span class="note">tied, no gold</span>'
      : '<span class="note">not reviewed</span>';
  } else {
    const w = t.left > t.right ? 'Version 1' : 'Version 2';
    v.innerHTML = `<span class="pill gold">${w} leads ` +
      `${Math.max(t.left,t.right)}&ndash;${Math.min(t.left,t.right)}</span>`;
  }
}

// vote on one framing
document.querySelectorAll('.fr .vote').forEach(b => b.addEventListener('click', async () => {
  const fr = b.closest('.fr');
  const on = b.getAttribute('aria-pressed') !== 'true';
  const res = await post('/api/vote', {run: RUN, case: fr.dataset.case,
    side: fr.dataset.side, n: fr.dataset.n, on,
    note: fr.querySelector('.fnote').value.trim()});
  if (!res) return;
  b.setAttribute('aria-pressed', String(on));
  b.innerHTML = on ? '&check; would film' : 'would film';
  fr.classList.toggle('on', on);
  paint(fr.dataset.case, res);
  flash(fr.dataset.case);
}));

// per-framing note, debounced
document.querySelectorAll('.fr .fnote').forEach(i => {
  let t; i.addEventListener('input', () => {
    const fr = i.closest('.fr');
    clearTimeout(t);
    t = setTimeout(async () => {
      const on = fr.querySelector('.vote').getAttribute('aria-pressed') === 'true';
      const res = await post('/api/vote', {run: RUN, case: fr.dataset.case,
        side: fr.dataset.side, n: fr.dataset.n, on, note: i.value.trim()});
      if (res) { paint(fr.dataset.case, res); flash(fr.dataset.case); }
    }, 700);
  });
});

// case-level note
document.querySelectorAll('input.why').forEach(i => {
  let t; i.addEventListener('input', () => {
    clearTimeout(t);
    t = setTimeout(async () => {
      const res = await post('/api/note',
        {run: RUN, case: i.dataset.case, why: i.value.trim()});
      if (res) flash(i.dataset.case);
    }, 700);
  });
});

const bless = document.getElementById('bless');
if (bless) bless.addEventListener('click', async () => {
  const res = await post('/api/bless', {run: RUN});
  if (!res) return;
  const n = res.blessed.length, sk = (res.skipped || []).length;
  alert(`${n} gold(s) set.` + (sk ? `\\n${sk} skipped (no clear winner).` : ''));
  location.reload();
});
"""


def esc(s):
    return html.escape(str(s), quote=True)


# ------------------------------------------------------------------------ pages

def page_index():
    runs = ab.list_runs()
    cfg = ab.load_cases()
    golds = {**ab.load_gold_meta(False), **ab.load_gold_meta(True)}

    if runs:
        rows = "".join(
            f'<tr><td><a href="/run/{esc(r["run_id"])}">{esc(r["run_id"])}</a></td>'
            f'<td class="note">{esc(r["created"][:16].replace("T"," "))}</td>'
            f'<td>{r["cases"]}/{r["total"]}</td>'
            f'<td>{r["picks"]} picked</td></tr>'
            for r in runs)
        runs_card = (
            '<div class="card"><header><h2>Runs</h2>'
            '<span class="note">newest first</span></header>'
            '<table><tr><th>Run</th><th>When</th><th>Paired</th><th>Reviewed</th></tr>'
            + rows + "</table></div>")
    else:
        runs_card = ('<div class="card"><div class="empty">No runs yet.<br>'
                     '<code>python ab.py new --baseline &lt;skill&gt; '
                     '--candidate &lt;skill&gt;</code></div></div>')

    case_rows = "".join(
        f'<tr><td>{esc(c["slug"])}'
        + (' <span class="pill real">real</span>' if ab.is_local(c) else "")
        + "</td><td>"
        + ('<span class="pill gold">gold</span>' if c["slug"] in golds else
           '<span class="note">no gold</span>')
        + "</td>"
        + f'<td class="note">{esc(golds.get(c["slug"], {}).get("why", "") or c.get("note", ""))}</td></tr>'
        for c in cfg["cases"])

    body = f"""
<h1>{esc(cfg["skill"])} review</h1>
<p class="sub">Blind A/B. You pick, nothing scores. {len(golds)} gold(s) frozen.</p>
{runs_card}
<div class="card"><header><h2>Cases</h2>
<span class="note">a gold is the version you blessed; every change is measured against it</span>
</header><table><tr><th>Case</th><th>Gold</th><th>Why / note</th></tr>{case_rows}</table></div>
"""
    return SHELL.format(title=f'{cfg["skill"]} review', css=CSS, body=body, js="")


def render_side(slug, side, label, text, votes):
    """One column: its framings as votable cards, then the rest as context."""
    parsed = ab.split_framings(text)
    n_on = sum(1 for k, v in votes.items()
               if k.startswith(f"{side}:") and v.get("on"))

    cards = ""
    for f in parsed["framings"]:
        key = f"{side}:{f['n']}"
        v = votes.get(key, {})
        on = bool(v.get("on"))
        cards += f"""
<div class="fr{' on' if on else ''}" data-case="{esc(slug)}" data-side="{side}" data-n="{esc(f['n'])}">
  <div class="fr-head">
    <button class="vote" aria-pressed="{'true' if on else 'false'}"
      title="Would you film this one?">{'&check; would film' if on else 'would film'}</button>
    <strong>{esc(f['title']) or "Option " + esc(f['n'])}</strong>
  </div>
  <pre>{esc(f['body'])}</pre>
  <input class="fnote" value="{esc(v.get('note',''))}"
    placeholder="why this one? (optional, but this is the part worth keeping)">
</div>"""

    rest = ""
    tail = "\n\n".join(x for x in (parsed["preamble"], parsed["trailer"]) if x)
    if tail:
        rest = (f'<details class="rest"><summary>the rest of this batch '
                f'(recommendation, count, notes)</summary><pre>{esc(tail)}</pre></details>')

    return (f'<div class="side" data-side="{side}">'
            f'<h3>{label} <span class="cnt" data-side="{side}">{n_on} picked</span></h3>'
            f'{cards}{rest}</div>')


def page_run(run_id):
    manifest = ab.load_manifest(run_id)
    picks = ab.load_picks(run_id)
    parts = []

    for c in manifest["cases"]:
        slug = c["slug"]
        if c.get("error"):
            parts.append(
                f'<section class="card"><header><h2>{esc(slug)}</h2>'
                f'<span class="err">skipped: {esc(c["error"])}</span></header></section>')
            continue

        entry = picks.get(slug, {})
        votes = entry.get("votes", {})
        why = entry.get("why", "")
        tally = entry.get("tally", {"left": 0, "right": 0})
        real = ' <span class="pill real">real</span>' if c.get("local") else ""

        if tally["left"] == tally["right"]:
            verdict = ('<span class="note">tied, no gold</span>'
                       if any(tally.values()) else
                       '<span class="note">not reviewed</span>')
        else:
            w = "Version 1" if tally["left"] > tally["right"] else "Version 2"
            verdict = f'<span class="pill gold">{w} leads {max(tally.values())}&ndash;{min(tally.values())}</span>'

        pair = (render_side(slug, "left", "Version 1", c["left_text"], votes)
                + render_side(slug, "right", "Version 2", c["right_text"], votes))

        parts.append(f"""
<section class="card" data-case="{esc(slug)}">
  <header><h2>{esc(slug)}</h2>{real}
  <span class="note">{esc(c.get("note", ""))}</span>
  <span class="verdict" data-case="{esc(slug)}">{verdict}</span></header>
  <div class="pair">{pair}</div>
  <div class="controls">
    <input class="why" data-case="{esc(slug)}" value="{esc(why)}"
      placeholder="anything about this case as a whole? (optional)">
    <span class="saved" data-case="{esc(slug)}">saved</span>
  </div>
</section>""")

    n_ok = len([c for c in manifest["cases"] if not c.get("error")])
    body = f"""
<div class="bar"><a href="/">&larr; all runs</a></div>
<h1>{esc(run_id)}</h1>
<p class="sub">{n_ok} case(s). Vote on each framing you would actually film.
The version with more picks wins the case; a tie stays a tie.
You cannot tell which version is which. Everything saves as you click.</p>
{''.join(parts)}
<div class="bar"><button class="primary" id="bless">Freeze winners as gold</button>
<span class="note">a gold is what every future change gets measured against</span></div>
"""
    return SHELL.format(title=run_id, css=CSS, body=body, js=RUN_JS).replace(
        "<body>", f'<body data-run="{esc(run_id)}">')


# ----------------------------------------------------------------------- server

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass  # the terminal stays readable

    def _send(self, code, body, ctype="text/html; charset=utf-8"):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlparse(self.path).path
        try:
            if path == "/":
                return self._send(200, page_index())
            if path.startswith("/run/"):
                return self._send(200, page_run(path[len("/run/"):]))
            self._send(404, "not found", "text/plain; charset=utf-8")
        except FileNotFoundError as e:
            self._send(404, str(e), "text/plain; charset=utf-8")
        except Exception as e:
            self._send(500, f"{type(e).__name__}: {e}", "text/plain; charset=utf-8")

    def do_POST(self):
        path = urlparse(self.path).path
        try:
            n = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(n) or b"{}")
            if path == "/api/vote":
                entry = ab.record_framing_vote(
                    payload["run"], payload["case"], payload["side"],
                    str(payload["n"]), bool(payload["on"]), payload.get("note"))
                return self._send(200, json.dumps(
                    {"ok": True, "tally": entry.get("tally", {})}), "application/json")
            if path == "/api/note":
                ab.set_case_note(payload["run"], payload["case"], payload.get("why", ""))
                return self._send(200, json.dumps({"ok": True}), "application/json")
            if path == "/api/pick":
                entry = ab.record_pick(payload["run"], payload["case"],
                                       payload["winner"], payload.get("why", ""))
                return self._send(200, json.dumps({"ok": True, "arm": entry["winner_arm"]}),
                                  "application/json")
            if path == "/api/bless":
                done, skipped = ab.bless_run(payload["run"], payload.get("case"))
                return self._send(200, json.dumps(
                    {"ok": True, "blessed": [d[0] for d in done], "skipped": skipped}),
                    "application/json")
            self._send(404, "not found", "text/plain; charset=utf-8")
        except Exception as e:
            self._send(400, f"{type(e).__name__}: {e}", "text/plain; charset=utf-8")


def serve(port=7654, open_browser=True):
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{port}/"
    print(f"review dashboard on {url}")
    print("reads runs off disk on every request, so refresh picks up new runs")
    print("ctrl-c to stop")
    if open_browser:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
        srv.shutdown()


if __name__ == "__main__":
    serve()
