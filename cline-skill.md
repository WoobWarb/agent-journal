---
name: agent-journal
description: Human-readable project journal for AI agent work. Use for any coding task in this project to pre-journal the plan, log each execution step before doing it, and generate the HTML journal companion. Also use to resume interrupted work from the journal, regenerate Agent-Journal.html, or update the project map.
---

# Agent Journal

The human-readable diary of AI agent work on this project. The source of truth is `.agents/Agent-Journal.md`.

## Protocol

### 0. Context First
- If `.agents/PROJECT_MAP.md` exists, read it before searching or reading files.
- If `.agents/pipeline.md` exists, read it before running any build/test/lint/deploy command.
- If `.agents/AGENTS.md` exists, follow it — it contains the full journaling protocol.

### 1. Pre-Journaling (BEFORE coding)
Before making any code changes, append an entry to `.agents/Agent-Journal.md`. If the file does not exist, create it with this header:

```markdown
# 📓 Agent Journal — [Project Name]
> **Created:** YYYY-MM-DD | **Last Updated:** YYYY-MM-DD | **Sessions:** N
```

Entry template:

```markdown
---
## [YYYY-MM-DD] | Short description of task
**Status:** 🔄 In Progress
**Type:** [🚀 Feature | 🐛 Fix | 🎨 UI | 🔧 Refactor | 📦 Setup | 📄 Docs]
**Impact:** [🟢 Low | 🟡 Medium | 🔴 High]

### TL;DR
> One-line summary of what will be done.

### 📝 Planned Actions
- [ ] Action 1
- [ ] Action 2

### 🤔 Decisions
- Why this approach was chosen

### 📂 Files to Change
- `path/to/file` — what will change
---
```

### 2. Execution Log (DURING coding)
Before EACH action, log it in the entry under `### 🔨 Execution Log`. Update the icon AFTER the action.

- 🔲 Planned | ⏳ In progress | ✅ Done | ❌ Failed (add reason)

This makes interrupted sessions recoverable: the next agent reads the log and resumes exactly where you stopped.

### 3. Completion (AFTER coding)
- Set status to ✅ Complete, ⚠️ Partial, or ❌ Failed
- Check off completed planned actions
- Fill in `### 📂 Files Changed`, `### ⚠️ Risks & Blockers`, and `### 💡 Notes` as needed
- Bump the header's `Last Updated` date and `Sessions` counter

### 4. HTML Companion
After every journal update, regenerate `.agents/Agent-Journal.html` (structure defined in `.agents/AGENTS.md`): read the markdown, escape backticks, and paste it into `window.JOURNAL_DATA`.

### 5. Handoff Note (when interrupted or switching AI)
Append to the current entry:

```markdown
### 🔄 Handoff Note
**Last completed step:** N of M
**Resume from:** Step N+1 — description
**Current state:** What works, what doesn't
**Important context:** Anything the next AI must know
```

## Quick Fix Mini Format

For trivial changes:

```markdown
---
## [YYYY-MM-DD] | Quick Fix Title
**Status:** ✅ Complete | **Type:** 🐛 Fix | **Impact:** 🟢 Low
- [x] Fixed [issue] in `path/to/file`
- 💡 [Optional note]
---
```

## Commands

| Request | Action |
|---------|--------|
| "resume" / "continue" | Read `.agents/Agent-Journal.md` (and `.agents/active.md` if present), find the last entry with ⏳ or 🔲 steps, and continue from the Handoff Note |
| "generate html" | Regenerate `.agents/Agent-Journal.html` from the current markdown |
| "update map" | Run `python agent-map.py` to regenerate `.agents/PROJECT_MAP.md` |
| "show active" | Show the current task context from `.agents/active.md` |
