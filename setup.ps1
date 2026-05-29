# Universal Agent Skills Setup
# Works with: Claude Code, Antigravity, Cursor, Windsurf, any AI agent
# Usage: .\setup.ps1 -ProjectPath "D:\path\to\project"

param(
    [string]$ProjectPath = ".",
    [switch]$Global,
    [switch]$Force,
    [switch]$SkipMap
)

$ErrorActionPreference = "Stop"
$Version = "3.0.0"
$SkillsDir = $PSScriptRoot

Write-Host ""
Write-Host "  ══════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  Universal Agent Skills Setup v$Version" -ForegroundColor Cyan
Write-Host "  ══════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Resolve paths
if ($Global) {
    $ProjectPath = Join-Path $env:USERPROFILE ".agents-global"
    Write-Host "  Mode: Global (~/.agents-global/)" -ForegroundColor Gray
} else {
    $ProjectPath = Resolve-Path $ProjectPath
    Write-Host "  Project: $ProjectPath" -ForegroundColor Gray
}

$agentsDir = Join-Path $ProjectPath ".agents"

# Create directory structure
$dirs = @("sessions", "topics", "index", "private")
foreach ($dir in $dirs) {
    $path = Join-Path $agentsDir $dir
    New-Item -ItemType Directory -Path $path -Force | Out-Null
}
Write-Host "  [+] Created .agents/ structure" -ForegroundColor Green

# Copy unified skill as AGENTS.md
$skillSource = Join-Path $SkillsDir "unified-skill.md"
$agentsMdDest = Join-Path $agentsDir "AGENTS.md"
if (Test-Path $skillSource) {
    Copy-Item $skillSource $agentsMdDest -Force
    Write-Host "  [+] Installed AGENTS.md (unified rules)" -ForegroundColor Green
}

# Create Agent-Journal.md (empty template)
$journalPath = Join-Path $agentsDir "Agent-Journal.md"
$ExistingSessions = ""

if (Test-Path $journalPath) {
    if (-not $Force) {
        Write-Host "  [=] Agent-Journal.md already exists (skipped)" -ForegroundColor DarkGray
    } else {
        $content = Get-Content $journalPath -Raw
        if ($content -match "(?s)(---\s*\r?\n\s*##\s*\[.*)") {
            $ExistingSessions = $Matches[1]
            Write-Host "  [i] Found existing session logs. They will be preserved and merged." -ForegroundColor Gray
        }
    }
}

if (-not (Test-Path $journalPath) -or $Force) {
    $journalContent = @"
# Agent Journal

> Human-readable diary of AI agent work on this project.

---

"@
    if ($ExistingSessions) {
        $journalContent = $journalContent.TrimEnd() + "`n`n" + $ExistingSessions.Trim() + "`n"
        Set-Content $journalPath $journalContent -Encoding UTF8
        Write-Host "  [+] Updated Agent-Journal.md (merged old sessions)" -ForegroundColor Green
    } else {
        Set-Content $journalPath $journalContent -Encoding UTF8
        Write-Host "  [+] Created Agent-Journal.md" -ForegroundColor Green
    }
}

# Create active.md
$activePath = Join-Path $agentsDir "active.md"
$activeContent = @"
# Active Context

**Last Updated:** $(Get-Date -Format 'yyyy-MM-dd HH:mm')
**Project:** $ProjectPath

## Current Task
[No active task yet]

## Status
- [ ] In Progress
- [ ] Blocked
- [ ] Complete

## Next Action
[Start working — the agent will update this automatically]
"@
Set-Content $activePath $activeContent -Encoding UTF8
Write-Host "  [+] Created active.md" -ForegroundColor Green

# Create .gitignore for private folder
$privateGitignore = Join-Path $agentsDir "private\.gitignore"
Set-Content $privateGitignore "*`n!.gitignore" -Encoding UTF8

# Copy agent-map.py
$mapSource = Join-Path $SkillsDir "agent-map.py"
$mapDest = Join-Path $ProjectPath "agent-map.py"
if ((Test-Path $mapSource) -and (-not (Test-Path $mapDest) -or $Force)) {
    Copy-Item $mapSource $mapDest -Force
    Write-Host "  [+] Copied agent-map.py" -ForegroundColor Green
}

# Generate project map
if (-not $SkipMap -and -not $Global) {
    Write-Host "  [*] Generating project map..." -ForegroundColor Gray
    Push-Location $ProjectPath
    try {
        python agent-map.py 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  [+] Generated PROJECT_MAP.md" -ForegroundColor Green
        }
    } catch {
        Write-Host "  [!] Skipped map generation (python not found)" -ForegroundColor Yellow
    }
    Pop-Location
}

# Setup AI rule files (only for local projects)
if (-not $Global) {
    $ruleBlock = @"

# Agent Journal Rules
- PRE-JOURNALING: ALWAYS write an initial entry in ``.agents/Agent-Journal.md`` BEFORE making any code changes. Set status to ``In Progress``.
- COMPLETION: Once work is complete, update the entry's status to ``Complete``.
- Read ``.agents/PROJECT_MAP.md`` (if it exists) before starting to understand the project structure.
- Do not ask for permission to journal, just do it automatically.
"@

    # Claude Code - CLAUDE.md (uses @import so rules are always loaded)
    $claudeMd = Join-Path $ProjectPath "CLAUDE.md"
    if (-not (Test-Path $claudeMd)) {
        Set-Content $claudeMd "# Project Rules`n`n@.agents/AGENTS.md`n" -Encoding UTF8
        Write-Host "  [+] Created CLAUDE.md" -ForegroundColor Green
    } elseif (-not (Select-String -Path $claudeMd -Pattern "AGENTS\.md" -Quiet)) {
        Add-Content $claudeMd "`n@.agents/AGENTS.md`n"
        Write-Host "  [+] Updated CLAUDE.md with journal import" -ForegroundColor Green
    }

    # Cursor
    $cursorRules = Join-Path $ProjectPath ".cursorrules"
    if (-not (Test-Path $cursorRules) -or -not (Select-String -Path $cursorRules -Pattern "Agent Journal" -Quiet)) {
        Add-Content $cursorRules $ruleBlock
        Write-Host "  [+] Configured .cursorrules" -ForegroundColor Green
    }

    # Windsurf
    $windsurfRules = Join-Path $ProjectPath ".windsurfrules"
    if (-not (Test-Path $windsurfRules) -or -not (Select-String -Path $windsurfRules -Pattern "Agent Journal" -Quiet)) {
        Add-Content $windsurfRules $ruleBlock
        Write-Host "  [+] Configured .windsurfrules" -ForegroundColor Green
    }

    # GitHub Copilot - .github/copilot-instructions.md
    $githubDir = Join-Path $ProjectPath ".github"
    if (-not (Test-Path $githubDir)) {
        New-Item -ItemType Directory -Path $githubDir -Force | Out-Null
    }
    $copilotPath = Join-Path $githubDir "copilot-instructions.md"
    if (-not (Test-Path $copilotPath) -or -not (Select-String -Path $copilotPath -Pattern "Agent Journal" -Quiet)) {
        Add-Content $copilotPath $ruleBlock
        Write-Host "  [+] Configured .github/copilot-instructions.md" -ForegroundColor Green
    }

    # Antigravity
    $antigravDir = Join-Path $ProjectPath ".antigravity"
    if (-not (Test-Path $antigravDir)) {
        New-Item -ItemType Directory -Path $antigravDir -Force | Out-Null
    }
    $extJson = @"
{
  "version": "1.0",
  "extensions": [
    {
      "id": "unified-agent-skill",
      "name": "Agent Context + Journal",
      "description": "Universal journaling, context saving, and project mapping",
      "enabled": true,
      "path": "../.agents/AGENTS.md"
    }
  ]
}
"@
    Set-Content (Join-Path $antigravDir "extensions.json") $extJson -Encoding UTF8
    Write-Host "  [+] Configured .antigravity/" -ForegroundColor Green
}

# Summary
Write-Host ""
Write-Host "  ══════════════════════════════════════════" -ForegroundColor Green
Write-Host "  Setup complete!" -ForegroundColor Green
Write-Host "  ══════════════════════════════════════════" -ForegroundColor Green
Write-Host ""
Write-Host "  Installed for:" -ForegroundColor White
Write-Host "    - Claude Code    (CLAUDE.md)" -ForegroundColor Gray
Write-Host "    - Cursor         (.cursorrules)" -ForegroundColor Gray
Write-Host "    - Windsurf       (.windsurfrules)" -ForegroundColor Gray
Write-Host "    - GitHub Copilot (.github/copilot-instructions.md)" -ForegroundColor Gray
Write-Host "    - Antigravity    (.antigravity/)" -ForegroundColor Gray
Write-Host ""
Write-Host "  Your AI agent will now automatically:" -ForegroundColor White
Write-Host "    1. Read PROJECT_MAP.md before working" -ForegroundColor Gray
Write-Host "    2. Write journal entries before/after changes" -ForegroundColor Gray
Write-Host "    3. Update active.md for session resume" -ForegroundColor Gray
Write-Host ""
Write-Host "  To regenerate the project map:" -ForegroundColor DarkGray
Write-Host "    python agent-map.py" -ForegroundColor DarkGray
Write-Host ""
