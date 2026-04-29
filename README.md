# 📓 Agent Journal

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/WoobWarb/agent-journal/pulls)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-lightgrey.svg)]()

> **The human-readable diary of your AI agent's work.**

Agent Journal is a lightweight, portable "skill" for AI coding assistants that ensures every change to your codebase is documented in a way that *humans* can actually read and enjoy.

No databases. No API keys. Just one Markdown file.

---

## ✨ Why Agent Journal?

Most AI agents focus on machine-readable context. **Agent Journal** focuses on **human communication**.

| Feature | Description |
|---------|-------------|
| 🧠 **Decision Memory** | Captures *why* decisions were made, not just *what* changed |
| 📱 **Truly Portable** | Plain Markdown — read on your phone, Obsidian, VS Code, anywhere |
| 🎯 **Impact Tracking** | Status badges, impact levels, and risk flags for every session |
| 📋 **TL;DR Summaries** | Skim 50 sessions in under a minute |
| 🔄 **Flexible Format** | Full format for features, mini format for quick fixes |
| ⚡ **Zero Setup** | One command to install, one sentence to activate |

---

## 🚀 Quick Start

### Windows (PowerShell)

```powershell
iwr -useb https://raw.githubusercontent.com/WoobWarb/agent-journal/main/install.ps1 | iex
```

### macOS / Linux (Bash)

```bash
curl -fsSL https://raw.githubusercontent.com/WoobWarb/agent-journal/main/install.sh | bash
```

Then tell your AI agent:

> *"Use the Agent Journal format to document our work in `.agents/Agent-Journal.md`"*

### Installer Options

| Flag | PowerShell | Bash | Description |
|------|-----------|------|-------------|
| Global install | `-Global` | `--global` | Install to `~/.agents/` instead of project |
| Force overwrite | `-Force` | `--force` | Overwrite existing file without asking |

---

## 📝 Example Entry

```markdown
## [2026-04-29] | Redesigned Login Page
**Status:** ✅ Complete
**Type:** 🎨 UI/UX | **Impact:** 🔴 High

### TL;DR
> Rebuilt login with glassmorphism card and Google OAuth2 integration.

### 📝 Actions
- [x] Implemented glassmorphism card `src/Login.jsx`
- [x] Added Google OAuth2 flow `src/hooks/useAuth.js`
- [ ] ⏳ Add "Remember Me" functionality

### 🤔 Decisions
- Chose OAuth over email/password for better UX
- Used glassmorphism to match the new design system

### ⚠️ Risks & Blockers
- OAuth redirect not yet configured on production

### 📂 Files Changed
- `src/components/Login.jsx` — Main login component
- `src/styles/login.css` — Glassmorphism styles
- `src/hooks/useAuth.js` — OAuth integration hook

### 💡 Notes
- Need to request OAuth Client ID from Google Console before deploy
```

---

## 🤝 Compatible AI Agents

Agent Journal works with **any AI coding assistant** that can write Markdown:

| Agent | Status |
|-------|--------|
| 🚀 Antigravity (Google) | ✅ Fully compatible |
| 🔮 Cursor | ✅ Fully compatible |
| 🏄 Windsurf | ✅ Fully compatible |
| 🤖 GitHub Copilot | ✅ Fully compatible |
| ✨ Any LLM-based agent | ✅ Works out of the box |

---

## 🛠️ Advanced Setup

### Global Skill (Antigravity AI)

Add to your global skills so every project gets journaling:

```json
{
  "id": "agent-journal",
  "name": "Agent Journal",
  "description": "Clean & Portable project development journal",
  "enabled": true,
  "path": "./Agent-Journal.md"
}
```

### Manual Installation

Just download `Agent-Journal.md` and place it in your project's `.agents/` directory:

```
your-project/
├── .agents/
│   └── Agent-Journal.md    ← The skill template
├── src/
└── ...
```

---

## 📄 Status & Type Reference

### Status Emojis

| Emoji | Meaning |
|-------|---------|
| ✅ | Complete — all goals achieved |
| ⚠️ | Partial — some tasks remaining |
| ❌ | Failed — blocked or reverted |
| 🔄 | In Progress — work started |

### Type Emojis

| Emoji | Type |
|-------|------|
| 🚀 | New Feature |
| 🐛 | Bug Fix |
| 🎨 | UI/UX Change |
| 🔧 | Refactor |
| 📦 | Setup/Config |
| 📄 | Documentation |

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/awesome`)
3. **Commit** your changes (`git commit -m 'Add awesome feature'`)
4. **Push** to the branch (`git push origin feature/awesome`)
5. **Open** a Pull Request

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

Made with ❤️ by [WoobWarb](https://github.com/WoobWarb)
