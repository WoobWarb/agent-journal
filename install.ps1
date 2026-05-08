# Agent Journal Remote Installer
# 📓 "The human-readable diary of your AI agent's work."

param(
    [switch]$Global,
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$Version = "2.0.0"

Write-Host ""
Write-Host "  ╔══════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "  ║   📓 Agent Journal Installer v$Version  ║" -ForegroundColor Cyan
Write-Host "  ╚══════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# 1. Configuration
$RepoUrl = "https://raw.githubusercontent.com/WoobWarb/agent-journal/main"
$SkillFile = "Agent-Journal.md"

if ($Global) {
    $DestDir = Join-Path $env:USERPROFILE ".agents"
    Write-Host "  [i] Installing globally to: $DestDir" -ForegroundColor Gray
} else {
    $DestDir = Join-Path (Get-Location) ".agents"
    Write-Host "  [i] Installing to project: $DestDir" -ForegroundColor Gray
}

# 2. Ensure .agents directory exists
if (-not (Test-Path $DestDir)) {
    New-Item -ItemType Directory -Path $DestDir | Out-Null
    Write-Host "  [+] Created directory: .agents/" -ForegroundColor Green
} else {
    Write-Host "  [=] Directory already exists: .agents/" -ForegroundColor DarkGray
}

# 3. Check for existing file
$DestPath = Join-Path $DestDir $SkillFile

if ((Test-Path $DestPath) -and (-not $Force)) {
    Write-Host ""
    Write-Host "  [!] Agent-Journal.md already exists!" -ForegroundColor Yellow
    $answer = Read-Host "      Overwrite? (y/N)"
    if ($answer -ne "y" -and $answer -ne "Y") {
        Write-Host "  [x] Installation cancelled." -ForegroundColor Red
        Write-Host ""
        return
    }
}

# 4. Download the skill template
Write-Host "  [*] Downloading template from GitHub..." -ForegroundColor Gray

try {
    Invoke-WebRequest -Uri "$RepoUrl/$SkillFile" -OutFile $DestPath -UseBasicParsing
    Write-Host "  [+] Successfully installed Agent-Journal.md" -ForegroundColor Green
} catch {
    Write-Host "  [!] Download failed. Check your internet connection." -ForegroundColor Red
    return
}

# 5. Download and run Agent Map (only for local installs)
if (-not $Global) {
    Write-Host "  [*] Downloading Agent Map generator..." -ForegroundColor Gray
    $MapScriptPath = Join-Path (Get-Location) "agent-map.py"
    try {
        Invoke-WebRequest -Uri "$RepoUrl/agent-map.py" -OutFile $MapScriptPath -UseBasicParsing
        Write-Host "  [+] Successfully downloaded agent-map.py" -ForegroundColor Green
        Write-Host "  [*] Generating Project Map..." -ForegroundColor Gray
        python $MapScriptPath
    } catch {
        Write-Host "  [!] Failed to download or run agent-map.py." -ForegroundColor Yellow
    }
}

# 5. Add to .gitignore if not already there
$gitignorePath = Join-Path (Get-Location) ".gitignore"
if (Test-Path $gitignorePath) {
    $content = Get-Content $gitignorePath -Raw
    if ($content -notmatch "\.agents/") {
        Add-Content $gitignorePath "`n# Agent Journal`n.agents/"
        Write-Host "  [+] Added .agents/ to .gitignore" -ForegroundColor Green
    }
}

# 7. Configure AI Auto-Journaling
if (-not $Global) {
    Write-Host "  [*] Configuring AI Auto-Journaling..." -ForegroundColor Gray
    $RuleText = "`n# Documentation Rule`n- PRE-JOURNALING: ALWAYS write an initial entry in `.agents/Agent-Journal.md` BEFORE making any code changes. Set status to `🔄 In Progress` and list planned actions.`n- COMPLETION: Once work is complete, update the entry's status to `✅ Complete`.`n- Read `.agents/PROJECT_MAP.md` (if it exists) before starting.`n- Do not ask for permission to journal, just do it automatically.`n"
    
    $RulesFiles = @(".cursorrules", ".windsurfrules")
    foreach ($file in $RulesFiles) {
        $RulePath = Join-Path (Get-Location) $file
        if ((Test-Path $RulePath) -and ((Get-Content $RulePath -Raw) -match "Agent Journal")) {
            continue
        }
        Add-Content $RulePath $RuleText
        Write-Host "  [+] Configured auto-journaling for $file" -ForegroundColor Green
    }
}

# 8. Success Message
Write-Host ""
Write-Host "  ✅ Ready to start journaling!" -ForegroundColor Cyan
Write-Host ""
Write-Host "  ✨ Auto-Journaling is enabled. Your AI will now use the journal automatically!" -ForegroundColor Green
Write-Host ""
Write-Host "  ──────────────────────────────────────" -ForegroundColor DarkGray
Write-Host "  Options:  install.ps1 -Global  (install to ~\.agents\)" -ForegroundColor DarkGray
Write-Host "            install.ps1 -Force   (overwrite without asking)" -ForegroundColor DarkGray
Write-Host ""
