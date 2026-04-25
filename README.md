# 📓 Agent Journal

> **The human-readable diary of your AI agent's work.**

Agent Journal is a lightweight, portable "skill" for AI coding assistants (like Antigravity, Cursor, or Windsurf) that ensures every change made to your codebase is documented in a way that *humans* can actually read and enjoy.

![Showcase](website/preview.png) *(Preview coming soon)*

## ✨ Why Agent Journal?

Most AI agents focus on technical context saving (long-term memory). **Agent Journal** focuses on **Communication**.

- 🧠 **Context Awareness**: Helps the agent remember what it did 5 minutes ago or 5 days ago.
- 📱 **Mobile Friendly**: It's just Markdown. Open it on your phone, Obsidian, or Notepad.
- 🤝 **Human-First**: Structured timelines that make sense to developers, not just machines.
- ⚡ **Zero Setup**: No database, no API keys. Just one file.

## 🚀 Quick Start

### 1. Installation
Copy `Agent-Journal.md` to your global AI skills folder or your project's `.agents/` directory.

### 2. Usage
Tell your AI Agent:
> *"Use the Agent-Journal format to document our work in .agents/Agent-Journal.md"*

## 📝 Example Entry

```markdown
## [2026-04-25] | Refined UI for Login Page
**Status:** ✅ Success
**Type:** UI Improvement

### 📝 Actions
- [x] Added glassmorphism effect to the login card
- [x] Updated primary button colors to HSL(210, 100%, 50%)
- [ ] Add mobile responsiveness for the footer

### 📂 Files
- src/components/Login.jsx
- src/styles/global.css

### 💡 Notes
- Used standard HSL variables to match the new design system.
```

## 🛠️ Global Setup (Antigravity AI)
Add the skill to your `.antigravity/extensions.json`:

```json
{
  "id": "agent-journal",
  "name": "Agent Journal",
  "description": "Clean & Portable project development journal",
  "enabled": true,
  "path": "./Agent-Journal.md"
}
```

---
Made with ❤️ by [WoobWarb](https://github.com/WoobWarb)
