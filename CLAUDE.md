# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

Agent Journal is a **distributable skill for AI coding assistants** — not a software application. The deliverables are Markdown templates, shell/PowerShell installers, a Python utility, and a static landing page. There is no build system, test suite, or package manager.

## Core Deliverables

| File | Purpose |
|------|---------|
| `Agent-Journal.md` | The skill template users download and drop into their projects |
| `unified-skill.md` | The comprehensive AGENTS.md rules file (installed as `.agents/AGENTS.md` by `setup.ps1`) |
| `agent-map.py` | Python script users run to generate `.agents/PROJECT_MAP.md` + `graph.json` |
| `install.sh` | Bash one-liner installer (downloads `Agent-Journal.md` + `agent-map.py` from GitHub) |
| `install.ps1` | PowerShell equivalent of `install.sh` |
| `setup.ps1` | Full setup script: copies all skills, creates `.agents/` structure, configures Claude Code/Cursor/Windsurf/Antigravity |
| `index.html` + `style.css` | Static marketing/landing page, no framework |

## Commands

**Regenerate the project map** (run after adding/removing files):
```bash
python agent-map.py
```
This writes `.agents/PROJECT_MAP.md` and `.agents/graph.json`.

**Preview the landing page** — open `index.html` directly in a browser; it has no server-side dependencies.

**Test the installers** — the installers fetch files from GitHub (`https://raw.githubusercontent.com/WoobWarb/agent-journal/main/`), so changes must be pushed to `main` before the installers will pick them up.

## Architecture & Key Conventions

### The Two-Tier Skill System

The project ships two levels of journaling rules:
1. **`Agent-Journal.md`** — lightweight template focused on the journal format. Used by `install.sh`/`install.ps1` for the simple one-liner install.
2. **`unified-skill.md`** — comprehensive rules file that becomes `.agents/AGENTS.md`. Installed by `setup.ps1` for full multi-platform setup. This is the authoritative source for agent behavior rules (pre-journaling, step-by-step logging, handoff protocol, session context).

When updating journaling rules or format, changes may need to be applied to **both** files for consistency.

### `.agents/` Directory Convention

This repo dogfoods its own convention. The `.agents/` folder holds:
- `Agent-Journal.md` — the live journal for work done on this repo itself
- `PROJECT_MAP.md` — auto-generated map (regenerated via `python agent-map.py`)
- `graph.json` — machine-readable project graph

**Always read `.agents/PROJECT_MAP.md` before navigating the codebase.**

### Journaling Rules (This Repo Uses Agent Journal)

Before making any code changes to this repository, write a pre-journal entry in `.agents/Agent-Journal.md`:
- Set status to `🔄 In Progress` and list planned actions
- Log each step **before** executing it, updating status after
- On completion, update status to `✅ Complete` (or `⚠️ Partial`)
- If interrupted, write a `### 🔄 Handoff Note` with resume point and context

### Installer Parity

`install.sh` and `install.ps1` must remain functionally equivalent. Both:
- Download `Agent-Journal.md` (the template) from GitHub raw
- Download and run `agent-map.py`
- Append journaling rules to `.cursorrules` / `.windsurfrules`
- Support `--global`/`-Global` and `--force`/`-Force` flags

`setup.ps1` is a superset: it also installs `unified-skill.md` as `AGENTS.md`, creates `active.md`, configures Antigravity, and writes a `CLAUDE.md` stub.

### Landing Page

`index.html` is self-contained with inline JS and a single external CSS file (`style.css`). It uses Google Fonts (Inter, Fira Code) loaded via CDN. The dark theme CSS variables are defined in `:root` at the top of `style.css`.
