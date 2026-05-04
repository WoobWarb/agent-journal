# Agent Journal Skill

**"The human-readable diary of your AI agent's work."**

---

## 📌 How to Use

Put this to other project's root directory and run it:
iwr -useb https://raw.githubusercontent.com/WoobWarb/agent-journal/main/agent-map.py -OutFile agent-map.py; python agent-map.py

Tell your AI agent:
> *"Use the Agent Journal format to document our work in `.agents/Agent-Journal.md`"*

**🤖 Note to AI Agents:** 
If a `.agents/PROJECT_MAP.md` file exists in this repository, **you must read it first** to understand the architecture and file structure before executing commands, grepping, or making assumptions.

The agent will maintain a clean, chronological log of every session — structured so **humans** can actually read and understand what happened.

---

## 📐 Journal Format

Every journal file starts with a **Project Header**, followed by individual **Session Entries**.

### Project Header (Top of File)

```markdown
# 📓 Agent Journal — [Project Name]
> **Created:** YYYY-MM-DD | **Last Updated:** YYYY-MM-DD | **Sessions:** N
```

---

### Session Entry (One Per Work Session)

Use the **Full Format** for significant work, or the **Mini Format** for quick fixes.

---

#### ✅ Full Format

```markdown
---
## [YYYY-MM-DD] | Short Title of Work Done
**Status:** ✅ Complete | ⚠️ Partial | ❌ Failed | 🔄 In Progress
**Type:** 🚀 Feature | 🐛 Bug Fix | 🎨 UI/UX | 🔧 Refactor | 📦 Setup | 📄 Docs
**Impact:** 🔴 High | 🟡 Medium | 🟢 Low

### TL;DR
> One or two sentences summarizing what was accomplished and why.

### 📝 Actions
- [x] Completed task description (`path/to/file`)
- [x] Another completed task
- [ ] ⏳ Pending task for next session

### 🤔 Decisions
- Chose X over Y because [reason]
- Used [library/approach] because [trade-off explanation]

### ⚠️ Risks & Blockers
- [Blocker] Description of what's blocking progress
- [Risk] Something that could cause issues later

### 📂 Files Changed
- `path/to/file1.js` — Brief description of change
- `path/to/file2.css` — Brief description of change

### 💡 Notes
- Additional context, gotchas, or reminders for next session
```

---

#### ⚡ Mini Format (for quick fixes)

```markdown
---
## [YYYY-MM-DD] | Quick Fix Title
**Status:** ✅ Complete | **Type:** 🐛 Bug Fix | **Impact:** 🟢 Low

- [x] Fixed [issue] in `path/to/file`
- 💡 [Optional note]
```

---

## 🎯 Status Reference

| Emoji | Status | When to Use |
|-------|--------|-------------|
| ✅ | Complete | All goals achieved |
| ⚠️ | Partial | Some tasks done, others remaining |
| ❌ | Failed | Blocked or reverted |
| 🔄 | In Progress | Work started but not finished |

## 📦 Type Reference

| Emoji | Type | Description |
|-------|------|-------------|
| 🚀 | Feature | New functionality |
| 🐛 | Bug Fix | Error correction |
| 🎨 | UI/UX | Visual / experience changes |
| 🔧 | Refactor | Code restructuring |
| 📦 | Setup | Project configuration |
| 📄 | Docs | Documentation updates |

---

## 💡 Tips for Best Results

1. **Be specific** — Include file paths in action items
2. **Explain "Why"** — The Decisions section is the most valuable part
3. **Flag risks early** — Blockers section prevents forgotten issues
4. **Use Mini Format** — Don't over-document trivial fixes
5. **Keep TL;DR short** — If someone reads only one line, make it count
