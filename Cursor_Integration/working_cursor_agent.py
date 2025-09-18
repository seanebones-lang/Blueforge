#!/usr/bin/env python3
"""
🎯 Working Cursor Agent
Creates a proper Cursor integration that actually works.
"""

import json
from datetime import datetime
from pathlib import Path

def create_working_cursor_agent():
"""Create a working Cursor agent integration."""

print("🎯 Creating Working Cursor Agent...")

# Cursor paths
cursor_config = Path.home() / "Library" / "Application Support" / "Cursor" / "User" / "settings.json"
cursor_extensions 

# Create DeepBlue agent extension
agent_dir 
agent_dir.mkdir(parents

# Create package.json
package_json = {
    "name": "deepblue-agent",
    "displayName": "DeepBlue Agent",
    "description": "Universal AI coding assistant with RAG capabilities",
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
            },
            {
                "command": "deepblue.query",
                "title": "DeepBlue Query",
                "category": "DeepBlue"
            }
        ],
        "menus": {
            "commandPalette": [
                {
                    "command": "deepblue.activate",
                    "when": "editorTextFocus"
                },
                {
                    "command": "deepblue.query",
                    "when": "editorTextFocus"
                }
            ]
        }
    }
}

with open(agent_dir / "package.json", 'w') as f:
    json.dump(package_json, f, indent

# Create extension.js
extension_js 
const vscode 
const { spawn } = require('child_process');
const path = require('path');

let deepblueActive 

function activate(context) {
console.log('🌊 DeepBlue Agent extension activated');

// Register commands
const activateCommand 
    deepblueActive = true;
    vscode.window.showInformationMessage('🌊 DeepBlue activated! Say "i found a bigger boat" to use DeepBlue capabilities.');
});

const queryCommand 
    const query 
        prompt: 'Enter your DeepBlue query',
        placeHolder: 'Ask about coding, building, debugging...'
    });
    
    if (query) {
        try {
            const result 
            vscode.window.showInformationMessage(`DeepBlue: ${result}`);
        } catch (error) {
            vscode.window.showErrorMessage(`DeepBlue Error: ${error.message}`);
        }
    }
});

context.subscriptions.push(activateCommand, queryCommand);

// Auto-activate DeepBlue
setTimeout(() => {
    deepblueActive = true;
    console.log('🌊 DeepBlue auto-activated');
}, 1000);

// Listen for chat messages
vscode.workspace.onDidChangeTextDocument((event) 
    if (deepblueActive && event.document.fileName.includes('chat')) {
        const text 
        if (text.includes('i found a bigger boat') || text.includes('bigger boat')) {
            vscode.window.showInformationMessage('🌊 DeepBlue activated! I can help with coding, building, debugging, and more!');
        }
    }
});
}

async function executeDeepBlueQuery(query) {
return new Promise((resolve, reject) 
    const deepbluePath = path.join(__dirname, '..', '..', '..', 'Universal_DeepBlue_Agent.py');
    const python 
    
    const child 
        cwd: path.dirname(deepbluePath)
    });
    
    let output 
    let error = '';
    
    child.stdout.on('data', (data) 
        output +
    });
    
    child.stderr.on('data', (data) => {
        error += data.toString();
    });
    
    child.on('close', (code) => {
        if (code === 0) {
            resolve(output.trim());
        } else {
            reject(new Error(error || 'DeepBlue query failed'));
        }
    });
});
}

function deactivate() {
console.log('🌊 DeepBlue Agent extension deactivated');
}

module.exports = { activate, deactivate };
'''

with open(agent_dir / "extension.js", 'w') as f:
    f.write(extension_js)

# Update Cursor settings
if cursor_config.exists():
    with open(cursor_config, 'r') as f:
        settings 
else:
    settings 

# Add DeepBlue settings
settings.update({
    "deepblue.enabled": True,
    "deepblue.agent": "universal",
    "deepblue.activationPhrase": "i found a bigger boat",
    "deepblue.systemPath": str(Path.cwd() / "Universal_DeepBlue_Agent.py"),
    "deepblue.webInterface": "http://localhost:5001",
    "deepblue.ragEnabled": True,
    "deepblue.buildDiagnosis": True,
    "deepblue.systemBuilding": True,
    "deepblue.lastUpdate": datetime.now().isoformat()
})

with open(cursor_config, 'w') as f:
    json.dump(settings, f, indent

print("✅ Working Cursor Agent created!")
print(f"📁 Agent extension: {agent_dir}")
print(f"⚙️ Settings updated: {cursor_config}")
print("")
print("🎯 DeepBlue Agent Features:")
print("   • Universal AI assistant")
print("   • Full RAG knowledge base")
print("   • Build diagnosis and troubleshooting")
print("   • System building capabilities")
print("   • Works in any project")
print("")
print("🚀 Next steps:")
print("1. Restart Cursor completely")
print("2. Open any project")
print("3. Press Cmd+L to open AI chat")
print("4. Say 'i found a bigger boat'")
print("5. DeepBlue will be available!")

if __name__ == "__main__":
create_working_cursor_agent()

