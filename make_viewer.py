
html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Agent Journal Viewer</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0a0a0f;--surface:rgba(255,255,255,0.05);--border:rgba(255,255,255,0.08);--text:#e2e8f0;--muted:#64748b;--accent:#818cf8;--accent2:#a78bfa;--green:#22c55e;--yellow:#eab308;--red:#ef4444;--blue:#3b82f6}
body{background:var(--bg);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;overflow-x:hidden}
.orb{position:fixed;border-radius:50%;filter:blur(80px);pointer-events:none;z-index:0}
.orb1{width:500px;height:500px;background:rgba(129,140,248,0.12);top:-150px;right:-150px}
.orb2{width:350px;height:350px;background:rgba(167,139,250,0.08);bottom:5%;left:-100px}
#drop-zone{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;padding:2rem;text-align:center}
.drop-box{border:2px dashed rgba(129,140,248,0.4);border-radius:24px;padding:4rem 3rem;max-width:520px;width:100%;background:rgba(129,140,248,0.04);cursor:pointer;transition:all .3s;backdrop-filter:blur(10px)}
.drop-box:hover,.drop-box.over{border-color:var(--accent);background:rgba(129,140,248,0.1);transform:translateY(-4px)}
.drop-icon{font-size:4rem;margin-bottom:1rem;display:inline-block;animation:float 3s ease-in-out infinite}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
.drop-box h1{font-size:1.8rem;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:.75rem}
.drop-box p{color:var(--muted);margin-bottom:1.5rem;line-height:1.7}
.code-chip{background:rgba(129,140,248,0.15);color:var(--accent);padding:.1rem .5rem;border-radius:4px;font-family:monospace;font-size:.9em}
.browse-btn{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;padding:.75rem 2rem;border-radius:50px;font-size:1rem;font-weight:600;cursor:pointer;transition:all .3s}
.browse-btn:hover{opacity:.85;transform:translateY(-2px)}
#file-input{display:none}
#app{display:none;position:relative;z-index:1;min-height:100vh}
.app-header{background:rgba(10,10,15,0.85);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);padding:1.5rem 2rem;position:sticky;top:0;z-index:10}
.header-top{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;margin-bottom:1.2rem}
.project-name{font-size:1.4rem;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.reset-btn{background:transparent;border:1px solid var(--border);color:var(--muted);padding:.4rem 1rem;border-radius:50px;font-size:.8rem;cursor:pointer;transition:all .2s;font-family:'Inter',sans-serif}
.reset-btn:hover{border-color:var(--accent);color:var(--accent)}
.stats-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:.75rem;margin-bottom:1.2rem}
.stat-card{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:.9rem;text-align:center}
.stat-val{font-size:1.8rem;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1}
.stat-lbl{font-size:.72rem;color:var(--muted);margin-top:.25rem;text-transform:uppercase;letter-spacing:.05em}
.controls{display:flex;flex-wrap:wrap;gap:.75rem;align-items:center}
.filter-pills{display:flex;flex-wrap:wrap;gap:.4rem}
.pill{padding:.3rem .85rem;border-radius:50px;border:1px solid var(--border);background:transparent;color:var(--muted);font-size:.78rem;cursor:pointer;transition:all .2s;font-family:'Inter',sans-serif}
.pill:hover,.pill.active{background:var(--accent);border-color:var(--accent);color:#fff}
.search-box{flex:1;min-width:200px;max-width:280px;position:relative}
.search-box input{width:100%;background:var(--surface);border:1px solid var(--border);border-radius:50px;padding:.4rem 1rem .4rem 2.2rem;color:var(--text);font-size:.82rem;outline:none;font-family:'Inter',sans-serif;transition:border-color .2s}
.search-box input:focus{border-color:var(--accent)}
.search-box::before{content:'🔍';position:absolute;left:.7rem;top:50%;transform:translateY(-50%);font-size:.75rem;pointer-events:none}
.timeline{padding:2rem;max-width:880px;margin:0 auto}
.session-card{background:var(--surface);border:1px solid var(--border);border-radius:16px;margin-bottom:.9rem;overflow:hidden;transition:all .3s;backdrop-filter:blur(10px)}
.session-card:hover{border-color:rgba(129,140,248,0.3);transform:translateY(-2px);box-shadow:0 8px 30px rgba(0,0,0,0.3)}
.session-card.s-complete{border-left:3px solid var(--green)}
.session-card.s-partial{border-left:3px solid var(--yellow)}
.session-card.s-failed{border-left:3px solid var(--red)}
.session-card.s-in-progress{border-left:3px solid var(--blue)}
.card-head{padding:1.2rem 1.5rem;cursor:pointer;display:flex;align-items:flex-start;gap:1rem;user-select:none}
.date-chip{background:rgba(129,140,248,0.12);color:var(--accent);padding:.2rem .6rem;border-radius:6px;font-size:.72rem;font-weight:600;white-space:nowrap;font-family:'Fira Code',monospace;margin-top:.1rem}
.files-note{color:var(--muted);font-size:.68rem;margin-top:.35rem;text-align:center}
.card-info{flex:1;min-width:0}
.card-title{font-size:.98rem;font-weight:600;margin-bottom:.4rem;line-height:1.35}
.badges{display:flex;flex-wrap:wrap;gap:.35rem;margin-bottom:.4rem}
.badge{padding:.15rem .55rem;border-radius:50px;font-size:.68rem;font-weight:500}
.b-complete{background:rgba(34,197,94,0.12);color:var(--green)}
.b-partial{background:rgba(234,179,8,0.12);color:var(--yellow)}
.b-failed{background:rgba(239,68,68,0.12);color:var(--red)}
.b-in-progress{background:rgba(59,130,246,0.12);color:var(--blue)}
.b-type{background:rgba(129,140,248,0.12);color:var(--accent)}
.b-high{background:rgba(239,68,68,0.08);color:var(--red)}
.b-medium{background:rgba(234,179,8,0.08);color:var(--yellow)}
.b-low{background:rgba(34,197,94,0.08);color:var(--green)}
.tldr{color:var(--muted);font-size:.82rem;line-height:1.55;font-style:italic}
.prog-wrap{background:rgba(255,255,255,0.04);border-radius:50px;height:3px;margin-top:.6rem;overflow:hidden}
.prog-bar{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:50px;transition:width .8s ease}
.chev{color:var(--muted);transition:transform .3s;font-size:.85rem;flex-shrink:0;padding-top:.15rem}
.card-body{display:none;padding:0 1.5rem 1.5rem;border-top:1px solid var(--border)}
.open .card-body{display:block}
.open .chev{transform:rotate(180deg)}
.section{margin-top:1rem}
.sec-title{font-size:.72rem;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.5rem;opacity:.8}
.sec-content{font-size:.84rem;line-height:1.7;color:var(--muted)}
.task-done{color:var(--green);margin:.18rem 0}
.task-pend{color:var(--muted);margin:.18rem 0}
.task-prog{color:var(--blue);margin:.18rem 0}
.blockq{border-left:3px solid var(--accent);padding:.1rem 0 .1rem .75rem;color:var(--text);margin:.3rem 0}
.file-chip{display:inline-flex;background:rgba(0,0,0,0.25);border:1px solid var(--border);border-radius:5px;padding:.1rem .45rem;font-size:.72rem;font-family:'Fira Code',monospace;color:var(--muted);margin:.15rem .1rem}
.inline-code{background:rgba(129,140,248,0.12);color:var(--accent);padding:.05rem .3rem;border-radius:4px;font-family:'Fira Code',monospace;font-size:.85em}
.empty-state{text-align:center;padding:5rem 2rem;color:var(--muted)}
.empty-state .empty-icon{font-size:3rem;margin-bottom:1rem;opacity:.5}
.fade-in{animation:fadeIn .4s ease both}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
</style>
</head>
<body>
<div class="orb orb1"></div>
<div class="orb orb2"></div>

<!-- Drop Zone -->
<div id="drop-zone">
  <div class="drop-box" id="drop-box">
    <div class="drop-icon">📓</div>
    <h1>Agent Journal Viewer</h1>
    <p>Drop your <span class="code-chip">.agents/Agent-Journal.md</span> file here, or click to browse.</p>
    <button class="browse-btn" id="browse-btn">📂 Open Journal File</button>
  </div>
  <input type="file" id="file-input" accept=".md,.txt">
</div>

<!-- App -->
<div id="app">
  <div class="app-header">
    <div class="header-top">
      <div class="project-name" id="project-name">📓 Agent Journal</div>
      <button class="reset-btn" id="reset-btn">↩ Load Another File</button>
    </div>
    <div class="stats-grid" id="stats-grid"></div>
    <div class="controls">
      <div class="filter-pills" id="filter-pills">
        <button class="pill active" data-f="all">All</button>
        <button class="pill" data-f="complete">✅ Complete</button>
        <button class="pill" data-f="partial">⚠️ Partial</button>
        <button class="pill" data-f="in-progress">🔄 In Progress</button>
        <button class="pill" data-f="failed">❌ Failed</button>
        <button class="pill" data-f="high">🔴 High Impact</button>
      </div>
      <div class="search-box">
        <input type="text" id="search-input" placeholder="Search sessions…">
      </div>
    </div>
  </div>
  <div class="timeline" id="timeline"></div>
</div>

<script>
// ── State ──────────────────────────────────────────
let sessions = [];
let activeFilter = 'all';

// ── DOM refs ───────────────────────────────────────
const dropZone  = document.getElementById('drop-zone');
const dropBox   = document.getElementById('drop-box');
const fileInput = document.getElementById('file-input');
const appEl     = document.getElementById('app');

// ── Drop zone wiring ───────────────────────────────
document.getElementById('browse-btn').onclick = () => fileInput.click();
document.getElementById('reset-btn').onclick  = resetApp;
fileInput.onchange = e => e.target.files[0] && readFile(e.target.files[0]);
dropBox.ondragover = e => { e.preventDefault(); dropBox.classList.add('over'); };
dropBox.ondragleave = () => dropBox.classList.remove('over');
dropBox.ondrop = e => {
  e.preventDefault(); dropBox.classList.remove('over');
  const f = e.dataTransfer.files[0]; if (f) readFile(f);
};

document.getElementById('filter-pills').onclick = e => {
  const btn = e.target.closest('[data-f]'); if (!btn) return;
  activeFilter = btn.dataset.f;
  document.querySelectorAll('[data-f]').forEach(b => b.classList.toggle('active', b === btn));
  renderSessions();
};
document.getElementById('search-input').oninput = renderSessions;

// ── File reading ───────────────────────────────────
function readFile(file) {
  const r = new FileReader();
  r.onload = e => loadJournal(e.target.result);
  r.readAsText(file);
}

// ── Parse ──────────────────────────────────────────
function loadJournal(md) {
  const { name, items } = parse(md);
  sessions = items;
  document.getElementById('project-name').textContent = '📓 ' + name;
  renderStats();
  renderSessions();
  dropZone.style.display = 'none';
  appEl.style.display = 'block';
}

function parse(md) {
  let name = 'Agent Journal';
  md.split('\n').slice(0,5).forEach(l => {
    if (l.startsWith('# ')) name = l.replace(/^#\s+📓?\s*Agent Journal\s*[—\-]?\s*/,'').trim() || 'Agent Journal';
  });
  const chunks = md.split(/\n---\n/);
  const items = [];
  for (let i = 1; i < chunks.length; i++) {
    const s = parseSession(chunks[i].trim());
    if (s) items.push(s);
  }
  return { name, items };
}

function parseSession(chunk) {
  const lines = chunk.split('\n');
  let hi = -1;
  for (let i = 0; i < lines.length; i++) { if (/^##\s+\[/.test(lines[i])) { hi = i; break; } }
  if (hi < 0) return null;
  const m = lines[hi].match(/^##\s+\[(\d{4}-\d{2}-\d{2})\]\s*\|\s*(.+)$/);
  if (!m) return null;

  const date = m[1], title = m[2].trim();
  let status = '', type = '', impact = '', tldr = '', tasksT = 0, tasksD = 0, filesC = 0;
  const secs = {};
  let cur = null, buf = [];

  const pick = (l, map) => { for (const [k,v] of Object.entries(map)) { if (l.includes(k)) return v; } return ''; };

  for (let i = hi + 1; i < lines.length; i++) {
    const l = lines[i];
    if (/^###\s+/.test(l)) {
      if (cur) secs[cur] = buf.join('\n').trim();
      cur = l.replace(/^###\s+/,'').trim(); buf = [];
    } else if (cur) {
      buf.push(l);
    } else {
      if (l.includes('**Status:**') || l.includes('Status:')) {
        if (!status) status = pick(l,{'✅':'complete','⚠️':'partial','❌':'failed','🔄':'in-progress'});
      }
      if (l.includes('**Type:**') || l.includes('Type:')) {
        if (!type) type = pick(l,{'🚀':'feature','🐛':'bug-fix','🎨':'ui-ux','🔧':'refactor','📦':'setup','📄':'docs'});
      }
      if (l.includes('**Impact:**') || l.includes('Impact:')) {
        if (!impact) impact = pick(l,{'🔴':'high','🟡':'medium','🟢':'low'});
      }
      // Also check combined lines
      if (!status) status = pick(l,{'✅ Complete':'complete','⚠️ Partial':'partial','❌ Failed':'failed','🔄 In Progress':'in-progress'});
      if (!type) type = pick(l,{'🚀 Feature':'feature','🐛 Bug Fix':'bug-fix','🎨 UI/UX':'ui-ux','🔧 Refactor':'refactor','📦 Setup':'setup','📄 Docs':'docs'});
      if (!impact) impact = pick(l,{'🔴 High':'high','🟡 Medium':'medium','🟢 Low':'low'});
    }
  }
  if (cur) secs[cur] = buf.join('\n').trim();

  const tldrKey = Object.keys(secs).find(k => k.includes('TL;DR'));
  if (tldrKey) tldr = secs[tldrKey].replace(/^>\s*/gm,'').trim();

  const actKey = Object.keys(secs).find(k => /actions|planned/i.test(k));
  if (actKey) secs[actKey].split('\n').forEach(l => {
    if (/^\s*-\s*\[/.test(l)) { tasksT++; if (/^\s*-\s*\[x\]/i.test(l)) tasksD++; }
  });

  const fKey = Object.keys(secs).find(k => /files changed/i.test(k));
  if (fKey) filesC = secs[fKey].split('\n').filter(l => l.trim().startsWith('-')).length;

  return { date, title, status, type, impact, tldr, tasksT, tasksD, filesC, secs };
}

// ── Render Stats ───────────────────────────────────
function renderStats() {
  const total  = sessions.length;
  const done   = sessions.filter(s => s.status === 'complete').length;
  const high   = sessions.filter(s => s.impact === 'high').length;
  const pct    = total ? Math.round(done/total*100) : 0;
  document.getElementById('stats-grid').innerHTML = `
    <div class="stat-card"><div class="stat-val">${total}</div><div class="stat-lbl">Sessions</div></div>
    <div class="stat-card"><div class="stat-val">${pct}%</div><div class="stat-lbl">Complete</div></div>
    <div class="stat-card"><div class="stat-val">${done}</div><div class="stat-lbl">Done</div></div>
    <div class="stat-card"><div class="stat-val">${high}</div><div class="stat-lbl">High Impact</div></div>
  `;
}

// ── Render Sessions ────────────────────────────────
function renderSessions() {
  const q = document.getElementById('search-input').value.toLowerCase();
  let list = [...sessions].reverse();
  if (activeFilter === 'high') { list = list.filter(s => s.impact === 'high'); }
  else if (activeFilter !== 'all') { list = list.filter(s => s.status === activeFilter); }
  if (q) list = list.filter(s => s.title.toLowerCase().includes(q) || s.tldr.toLowerCase().includes(q));

  const tl = document.getElementById('timeline');
  if (!list.length) {
    tl.innerHTML = '<div class="empty-state"><div class="empty-icon">🔍</div><p>No sessions match your filter.</p></div>';
    return;
  }
  tl.innerHTML = list.map((s, i) => card(s, i)).join('');
}

// ── Card HTML ──────────────────────────────────────
const STATUS_LABEL = {complete:'✅ Complete',partial:'⚠️ Partial',failed:'❌ Failed','in-progress':'🔄 In Progress'};
const TYPE_LABEL   = {feature:'🚀 Feature','bug-fix':'🐛 Bug Fix','ui-ux':'🎨 UI/UX',refactor:'🔧 Refactor',setup:'📦 Setup',docs:'📄 Docs'};
const IMPACT_LABEL = {high:'🔴 High',medium:'🟡 Medium',low:'🟢 Low'};

function card(s, i) {
  const pct = s.tasksT ? Math.round(s.tasksD/s.tasksT*100) : -1;
  const body = Object.entries(s.secs).map(([k,v]) => section(k,v)).join('');
  return `<div class="session-card s-${s.status} fade-in" style="animation-delay:${i*0.04}s">
  <div class="card-head" onclick="toggle(this.parentElement)">
    <div>
      <div class="date-chip">${s.date}</div>
      ${s.filesC ? `<div class="files-note">📂 ${s.filesC}</div>` : ''}
    </div>
    <div class="card-info">
      <div class="card-title">${esc(s.title)}</div>
      <div class="badges">
        ${s.status ? `<span class="badge b-${s.status}">${STATUS_LABEL[s.status]||s.status}</span>` : ''}
        ${s.type   ? `<span class="badge b-type">${TYPE_LABEL[s.type]||s.type}</span>` : ''}
        ${s.impact ? `<span class="badge b-${s.impact}">${IMPACT_LABEL[s.impact]||s.impact}</span>` : ''}
      </div>
      ${s.tldr ? `<div class="tldr">${esc(s.tldr)}</div>` : ''}
      ${pct >= 0 ? `<div class="prog-wrap"><div class="prog-bar" style="width:${pct}%"></div></div>` : ''}
    </div>
    <div class="chev">▼</div>
  </div>
  <div class="card-body">${body}</div>
</div>`;
}

function section(title, content) {
  if (!content.trim()) return '';
  return `<div class="section"><div class="sec-title">${esc(title)}</div><div class="sec-content">${mdToHtml(content)}</div></div>`;
}

function mdToHtml(text) {
  return text.split('\n').map(l => {
    if (/^\s*-\s*\[x\]/i.test(l)) return `<div class="task-done">✅ ${esc(l.replace(/^\s*-\s*\[x\]\s*/i,''))}</div>`;
    if (/^\s*-\s*\[\s\]/.test(l))  return `<div class="task-pend">🔲 ${esc(l.replace(/^\s*-\s*\[\s\]\s*/,''))}</div>`;
    if (/^\s*-\s*⏳/.test(l))       return `<div class="task-prog">⏳ ${esc(l.replace(/^\s*-\s*⏳\s*/,''))}</div>`;
    if (/^>\s/.test(l))             return `<div class="blockq">${esc(l.replace(/^>\s/,''))}</div>`;
    if (/^\s*-\s+`([^`]+)`/.test(l)) {
      const fm = l.match(/^\s*-\s+`([^`]+)`(.*)/);
      if (fm) return `<div style="margin:.2rem 0"><span class="file-chip">${esc(fm[1])}</span><span style="font-size:.8rem"> ${esc(fm[2])}</span></div>`;
    }
    if (/^\s*-\s+/.test(l))        return `<div style="margin:.2rem 0;padding-left:.4rem">• ${inlineMd(esc(l.replace(/^\s*-\s+/,'')))}</div>`;
    if (/^\d+\.\s/.test(l))        return `<div style="margin:.2rem 0;padding-left:.6rem">${inlineMd(esc(l))}</div>`;
    if (l.trim())                  return `<div style="margin:.15rem 0">${inlineMd(esc(l))}</div>`;
    return '<div style="height:.35rem"></div>';
  }).join('');
}

function inlineMd(s) {
  return s.replace(/`([^`]+)`/g,'<span class="inline-code">$1</span>')
          .replace(/\*\*([^*]+)\*\*/g,'<strong style="color:var(--text)">$1</strong>');
}

function esc(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function toggle(card) { card.classList.toggle('open'); }

function resetApp() {
  appEl.style.display = 'none';
  dropZone.style.display = 'flex';
  fileInput.value = '';
  sessions = [];
}
</script>
</body>
</html>"""

with open('journal-viewer.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('journal-viewer.html created successfully!')
