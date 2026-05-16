# Universal Agent Skill: Context + Journal + Map

**Version:** 3.0
**Compatible:** Claude Code, Antigravity, Cursor, Windsurf, GitHub Copilot, any LLM agent

---

## Rules for AI Agent

When working on this project, follow these rules automatically:

### 1. Pre-Journaling (BEFORE coding)

Before making any code changes, write an entry in `.agents/Agent-Journal.md`:

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

### 2. Completion (AFTER coding)

Update the same entry:
- Change status to `✅ Complete` (or `⚠️ Partial` / `❌ Failed`)
- Check off completed actions
- Add any notes or blockers discovered

### 3. Read Project Map First

If `.agents/PROJECT_MAP.md` exists, read it before searching or reading files.
This saves tokens and prevents hallucinations about project structure.

### 4. Session Context

Update `.agents/active.md` with current task focus so the next session can resume.

### 5. Technical Decisions

For significant architectural decisions, add notes to `.agents/topics/[topic].md`.

---

## File Structure

```
.agents/
├── AGENTS.md           # This rules file (universal)
├── Agent-Journal.md    # Human-readable work diary
├── active.md           # Current task context (for AI resume)
├── PROJECT_MAP.md      # Auto-generated codebase map
├── graph.json          # Machine-readable project graph
├── sessions/           # Detailed session checkpoints
├── topics/             # Architectural decision records
├── index/              # Filesystem snapshots
└── private/            # Git-ignored local notes
```

---

## Platform-Specific Integration

### Claude Code
Add to project `CLAUDE.md`:
```
Read and follow .agents/AGENTS.md for journaling rules.
```

### Cursor / Windsurf
Rules are auto-added to `.cursorrules` / `.windsurfrules` by the installer.

### Antigravity
Register as skill in `.antigravity/extensions.json`:
```json
{
  "id": "unified-agent-skill",
  "name": "Agent Context + Journal",
  "enabled": true,
  "path": "./unified-skill.md"
}
```

### Any Other Agent
Just tell it: "Follow the rules in .agents/AGENTS.md"

---

## Journal Format Reference

### Full Entry (features, big changes)
```markdown
## [2026-05-16] | Built payment integration
**Status:** ✅ Complete
**Type:** 🚀 Feature | **Impact:** 🔴 High

### TL;DR
> Integrated Stripe for one-time payments with webhook handling.

### 📝 Actions
- [x] Created payment service `src/services/payment.ts`
- [x] Added webhook endpoint `src/api/webhooks/stripe.ts`
- [x] Updated schema with payments table
- [ ] ⏳ Add subscription support (next sprint)

### 🤔 Decisions
- Stripe over PayPal: better developer experience, lower fees in TH
- Webhook-first: ensures payment state is always accurate

### ⚠️ Risks & Blockers
- Need production Stripe keys before deploy

### 📂 Files Changed
- `src/services/payment.ts` — Payment service with Stripe SDK
- `src/api/webhooks/stripe.ts` — Webhook handler
- `prisma/schema.prisma` — Added Payment model

### 💡 Notes
- Test with `stripe listen --forward-to localhost:3000/api/webhooks/stripe`
```

### Mini Entry (quick fixes, small changes)
```markdown
## [2026-05-16] | Fixed login redirect loop
**Status:** ✅ Complete | **Type:** 🐛 Fix | **Impact:** 🟡 Medium
- Fixed infinite redirect in `src/middleware/auth.ts` line 42
- Root cause: missing `return` after `redirect()` call
```

---

## Commands (for agents that support them)

| Command | Action |
|---------|--------|
| `@agents show active` | Show current task context |
| `@agents resume` | Load context and continue work |
| `@agents update map` | Regenerate PROJECT_MAP.md |
| `@agents list sessions` | Show recent session files |
