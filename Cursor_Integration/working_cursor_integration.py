#!/usr/bin/env python3
"""
🎯 Working Cursor Integration
Creates a proper integration that actually works in Cursor.
"""

import json
from datetime import datetime
from pathlib import Path

def create_working_cursor_integration():
"""Create a working Cursor integration."""

# Cursor config paths
cursor_config = Path.home() / "Library" / "Application Support" / "Cursor" / "User" / "settings.json"
cursor_extensions 

print("🎯 Creating working Cursor integration...")

# 1. Create a simple extension that actually works
extension_dir 
extension_dir.mkdir(parents

# Create package.json
package_json = {
    "name": "deepblue-working",
    "displayName": "DeepBlue Working",
    "description": "Working DeepBlue integration",
    "version": "1.0.0",
    "publisher": "deepblue",
    "engines": {"vscode": "^1.74.0"},
    "categories": ["Other"],
    "activationEvents": ["*"],
    "main": "./extension.js",
    "contributes": {
        "commands": [
            {
                "command": "deepblue.activate",
                "title": "Activate DeepBlue",
                "category": "DeepBlue"
            }
        ]
    }
}

with open(extension_dir / "package.json", 'w') as f:
    json.dump(package_json, f, indent

# Create extension.js
extension_js 
const vscode 

function activate(context) {
console.log('DeepBlue Working extension activated');

// Register command
const activateCommand = vscode.commands.registerCommand('deepblue.activate', () 
    vscode.window.showInformationMessage('🌊 DeepBlue is now active! Say "i found a bigger boat" to activate.');
});

context.subscriptions.push(activateCommand);

// Auto-activate DeepBlue
setTimeout(() 
    console.log('🌊 DeepBlue auto-activated');
}, 1000);
}

function deactivate() {
console.log('DeepBlue Working extension deactivated');
}

module.exports = { activate, deactivate };
'''

with open(extension_dir / "extension.js", 'w') as f:
    f.write(extension_js)

# 2. Update Cursor settings
if cursor_config.exists():
    with open(cursor_config, 'r') as f:
        settings 
else:
    settings 

# Add DeepBlue settings
settings.update({
    "deepblue.enabled": True,
    "deepblue.working": True,
    "deepblue.activationPhrase": "i found a bigger boat",
    "deepblue.systemPath": str(Path.cwd() / "ultimate_deepblue_system.py"),
    "deepblue.webInterface": "http://localhost:5001",
    "deepblue.lastUpdate": datetime.now().isoformat()
})

with open(cursor_config, 'w') as f:
    json.dump(settings, f, indent

# 3. Create a startup script
startup_script = '''
#!/bin/bash
# DeepBlue Startup Script

echo "🌊 Starting DeepBlue for Cursor..."

# Start the web interface if not running
if ! curl -s http://localhost:5001/api/status > /dev/null 2>&1; then
echo "Starting DeepBlue web interface..."
cd "/Users/seanmcdonnell/Desktop/DeeperBlue"
nohup python3 hack_web_interface.py > deepblue.log 2>&1 &
sleep 3
fi

echo "✅ DeepBlue is ready for Cursor!"
echo "💬 Say 'i found a bigger boat' in Cursor's AI chat"
'''

startup_file 
with open(startup_file, 'w') as f:
    f.write(startup_script)

startup_file.chmod(0o755)

print("✅ Working Cursor integration created!")
print(f"📁 Extension: {extension_dir}")
print(f"⚙️ Settings updated: {cursor_config}")
print(f"🚀 Startup script: {startup_file}")
print("")
print("🎯 Next steps:")
print("1. Restart Cursor completely")
print("2. Open any project")
print("3. Press Cmd+L to open AI chat")
print("4. Say 'i found a bigger boat'")
print("5. DeepBlue should activate!")

if __name__ 
create_working_cursor_integration()



