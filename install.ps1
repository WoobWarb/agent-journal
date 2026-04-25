# Agent Journal Auto-Install Script
# 📓 "The human-readable diary of your AI agent's work."

$ErrorActionPreference = "Stop"

Write-Host "--- Agent Journal Installer ---" -ForegroundColor Cyan

# 1. Define Paths
$SourceSkill = Join-Path $PSScriptRoot "Agent-Journal.md"
$GlobalAntigravityDir = Join-Path $HOME ".gemini\antigravity"
$GlobalSkillsDir = Join-Path $GlobalAntigravityDir "skills" # Or however they organize it

# Check if Antigravity exists
if (-not (Test-Path $GlobalAntigravityDir)) {
    Write-Host "[!] Could not find Antigravity global directory at $GlobalAntigravityDir" -ForegroundColor Yellow
    Write-Host "[!] I will install it in the current project instead." -ForegroundColor Gray
    $DestDir = Join-Path (Get-Location) ".agents"
} else {
    $DestDir = $GlobalSkillsDir
}

# 2. Create Directory
if (-not (Test-Path $DestDir)) {
    New-Item -ItemType Directory -Path $DestDir | Out-Null
    Write-Host "[+] Created directory: $DestDir" -ForegroundColor Green
}

# 3. Copy Skill
Copy-Item $SourceSkill -Destination $DestDir -Force
Write-Host "[+] Skill installed to: $(Join-Path $DestDir 'Agent-Journal.md')" -ForegroundColor Green

# 4. Instructions
Write-Host "`nInstallation Successful! 🎉" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor White
Write-Host "1. Register the skill in your config (if needed)."
Write-Host "2. Tell your agent:"
Write-Host "   'Use the Agent Journal skill to document our progress in .agents/Agent-Journal.md'" -ForegroundColor Yellow
Write-Host "-------------------------------"
