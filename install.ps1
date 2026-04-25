# Agent Journal Remote Installer
# 📓 "The human-readable diary of your AI agent's work."

$ErrorActionPreference = "Stop"

Write-Host "`n--- Agent Journal Setup ---" -ForegroundColor Cyan

# 1. Configuration
$RepoUrl = "https://raw.githubusercontent.com/WoobWarb/agent-journal/main"
$SkillFile = "Agent-Journal.md"
$DestDir = Join-Path (Get-Location) ".agents"

# 2. Ensure .agents directory exists
if (-not (Test-Path $DestDir)) {
    New-Item -ItemType Directory -Path $DestDir | Out-Null
    Write-Host "[+] Created directory: $DestDir" -ForegroundColor Green
}

# 3. Download the skill template
$DestPath = Join-Path $DestDir $SkillFile
Write-Host "[*] Downloading template from GitHub..." -ForegroundColor Gray

try {
    Invoke-WebRequest -Uri "$RepoUrl/$SkillFile" -OutFile $DestPath -UseBasicParsing
    Write-Host "[+] Successfully installed to: $DestPath" -ForegroundColor Green
} catch {
    Write-Host "[!] Failed to download template. Please check your internet connection." -ForegroundColor Red
    return
}

# 4. Success Message
Write-Host "`nReady to start journaling! 🚀" -ForegroundColor Cyan
Write-Host "Next Step: Tell your AI agent:" -ForegroundColor White
Write-Host "   'Use the Agent Journal format to document our work in .agents/Agent-Journal.md'" -ForegroundColor Yellow
Write-Host "-------------------------------`n"
