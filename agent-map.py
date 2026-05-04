import os
import json
from pathlib import Path

# Directories to ignore to keep the map clean and focused
IGNORE_DIRS = {
    '.git', 'node_modules', '.venv', 'venv', '__pycache__', 
    '.agents', 'dist', 'build', '.idea', '.vscode'
}

# File extensions to ignore for text context extraction
IGNORE_EXTS = {
    '.pyc', '.pyo', '.pyd', '.so', '.dll', '.exe', 
    '.png', '.jpg', '.jpeg', '.gif', '.mp4', '.mp3', '.wav', '.zip', '.tar', '.gz'
}

def generate_map(root_dir='.'):
    root_path = Path(root_dir)
    tree_lines = []
    file_details = []
    
    for current_root, dirs, files in os.walk(root_path):
        # Modify dirs in-place to skip ignored directories and hidden dirs
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
        
        rel_path = Path(current_root).relative_to(root_path)
        level = len(rel_path.parts) if rel_path.name else 0
        indent = '  ' * level
        
        if rel_path.name:
            tree_lines.append(f"{indent}📂 {rel_path.name}/")
            
        sub_indent = '  ' * (level + 1)
        for f in sorted(files):
            file_path = Path(current_root) / f
            
            # Skip hidden files
            if f.startswith('.'):
                continue
                
            tree_lines.append(f"{sub_indent}📄 {f}")
            
            if file_path.suffix.lower() in IGNORE_EXTS:
                continue
                
            # Attempt to read the first few lines for context
            context = ""
            try:
                with open(file_path, 'r', encoding='utf-8') as file_obj:
                    # Try to get the first 5 lines
                    lines = []
                    for _ in range(5):
                        try:
                            line = next(file_obj).strip()
                            if line and not line.startswith(('import', 'from', '//', '/*', '*')):
                                lines.append(line)
                        except StopIteration:
                            break
                    context = " ".join(lines)
            except Exception:
                context = "[Binary or unreadable]"
                
            file_details.append({
                "path": str(file_path.relative_to(root_path)).replace('\\', '/'),
                "ext": file_path.suffix,
                "context": context[:150] + "..." if len(context) > 150 else context
            })
            
    return tree_lines, file_details

def write_project_map(tree_lines, file_details):
    agents_dir = Path('.agents')
    agents_dir.mkdir(exist_ok=True)
    
    map_path = agents_dir / 'PROJECT_MAP.md'
    json_path = agents_dir / 'graph.json'
    
    with open(map_path, 'w', encoding='utf-8') as f:
        f.write("# 🗺️ Agent Project Map\n")
        f.write("> **Auto-generated knowledge graph to help AI agents understand the codebase.**\n\n")
        f.write("> *Note for AI: Read this file to understand the architecture before searching or reading individual files.*\n\n")
        
        f.write("## 📂 File Tree\n```text\n")
        f.write("📦 Project Root\n")
        f.write("\n".join(tree_lines))
        f.write("\n```\n\n")
        
        f.write("## 📄 File Contexts\n")
        f.write("Brief descriptions or first lines of files:\n\n")
        for detail in file_details:
            f.write(f"- **`{detail['path']}`**\n")
            if detail['context']:
                f.write(f"  > {detail['context']}\n")
                
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(file_details, f, indent=2)
        
    print(f"Generated map at: {map_path}")
    print(f"Generated JSON at: {json_path}")

if __name__ == '__main__':
    print("Generating Agent Project Map...")
    tree, details = generate_map()
    write_project_map(tree, details)
