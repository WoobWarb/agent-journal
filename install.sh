#!/bin/bash
# Agent Journal Remote Installer
# 📓 "The human-readable diary of your AI agent's work."

set -e

VERSION="2.0.0"
REPO_URL="https://raw.githubusercontent.com/WoobWarb/agent-journal/main"
SKILL_FILE="Agent-Journal.md"
GLOBAL=false
FORCE=false

# Parse flags
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --global|-g) GLOBAL=true ;;
        --force|-f) FORCE=true ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
    shift
done

echo ""
echo "  ╔══════════════════════════════════════╗"
echo "  ║   📓 Agent Journal Installer v$VERSION  ║"
echo "  ╚══════════════════════════════════════╝"
echo ""

# Set destination
if [ "$GLOBAL" = true ]; then
    DEST_DIR="$HOME/.agents"
    echo "  [i] Installing globally to: $DEST_DIR"
else
    DEST_DIR="$(pwd)/.agents"
    echo "  [i] Installing to project: $DEST_DIR"
fi

# Create directory
if [ ! -d "$DEST_DIR" ]; then
    mkdir -p "$DEST_DIR"
    echo "  [+] Created directory: .agents/"
else
    echo "  [=] Directory already exists: .agents/"
fi

DEST_PATH="$DEST_DIR/$SKILL_FILE"

# Check existing
if [ -f "$DEST_PATH" ] && [ "$FORCE" = false ]; then
    echo ""
    echo "  [!] Agent-Journal.md already exists!"
    read -p "      Overwrite? (y/N) " answer
    if [[ "$answer" != "y" && "$answer" != "Y" ]]; then
        echo "  [x] Installation cancelled."
        echo ""
        exit 0
    fi
fi

# Download
echo "  [*] Downloading template from GitHub..."

if command -v curl &> /dev/null; then
    curl -fsSL "$REPO_URL/$SKILL_FILE" -o "$DEST_PATH"
elif command -v wget &> /dev/null; then
    wget -q "$REPO_URL/$SKILL_FILE" -O "$DEST_PATH"
else
    echo "  [!] Error: curl or wget is required."
    exit 1
fi

echo "  [+] Successfully installed Agent-Journal.md"

# Download and run Agent Map (only for local installs)
if [ "$GLOBAL" = false ]; then
    echo "  [*] Downloading Agent Map generator..."
    MAP_SCRIPT_PATH="$(pwd)/agent-map.py"
    if command -v curl &> /dev/null; then
        curl -fsSL "$REPO_URL/agent-map.py" -o "$MAP_SCRIPT_PATH"
    else
        wget -q "$REPO_URL/agent-map.py" -O "$MAP_SCRIPT_PATH"
    fi
    echo "  [+] Successfully downloaded agent-map.py"
    echo "  [*] Generating Project Map..."
    if command -v python3 &> /dev/null; then
        python3 "$MAP_SCRIPT_PATH"
    elif command -v python &> /dev/null; then
        python "$MAP_SCRIPT_PATH"
    else
        echo "  [!] Could not run Python automatically."
    fi
fi

# Add to .gitignore
if [ -f ".gitignore" ]; then
    if ! grep -q ".agents/" .gitignore; then
        echo -e "\n# Agent Journal\n.agents/" >> .gitignore
        echo "  [+] Added .agents/ to .gitignore"
    fi
fi

# Configure AI Auto-Journaling
if [ "$GLOBAL" = false ]; then
    echo "  [*] Configuring AI Auto-Journaling..."
    RULE_TEXT="\n# Documentation Rule\nAlways document our work at the end of the session using the Agent Journal format found in .agents/Agent-Journal.md. Do not ask for permission, just do it automatically.\n"
    
    for file in ".cursorrules" ".windsurfrules"; do
        if [ -f "$file" ] && grep -q "Agent Journal" "$file"; then
            continue
        fi
        echo -e "$RULE_TEXT" >> "$file"
        echo "  [+] Configured auto-journaling for $file"
    done
fi

echo ""
echo "  ✅ Ready to start journaling!"
echo ""
echo "  ✨ Auto-Journaling is enabled. Your AI will now use the journal automatically!"
echo ""
echo "  ──────────────────────────────────────"
echo "  Options:  install.sh --global  (install to ~/.agents/)"
echo "            install.sh --force   (overwrite without asking)"
echo ""
