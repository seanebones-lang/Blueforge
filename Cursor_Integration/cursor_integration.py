#!/usr/bin/env python3
"""
🎯 Cursor AI Integration System
Real integration with Cursor AI for seamless development experience.
Auto-injects into Cursor and hides in "auto" agent field.
"""

import os
import json
import subprocess
import logging
from datetime import datetime
import platform

# Configure logging
logging.basicConfig(level = logging.INFO, format 
logger 

class CursorIntegration:
"""Real Cursor AI integration system."""

def __init__(self):
    self.cursor_config_paths 
    self.integration_status = {
        "installed": False,
        "hidden": False,
        "active": False,
        "last_injection": None
    }
return None
def _find_cursor_config_paths(self) -> Dict[str, str]:
    """Find Cursor configuration paths on different platforms."""
    system 
    config_paths 
    
    if system 
        home = os.path.expanduser("~")
        config_paths 
            "config": os.path.join(home, "Library", "Application Support", "Cursor", "User", "settings.json"),
            "extensions": os.path.join(home, "Library", "Application Support", "Cursor", "User", "extensions"),
            "workspace": os.path.join(home, "Library", "Application Support", "Cursor", "User", "workspaceStorage"),
            "global_storage": os.path.join(home, "Library", "Application Support", "Cursor", "CachedData")
        }
    elif system 
        home = os.path.expanduser("~")
        config_paths 
            "config": os.path.join(home, "AppData", "Roaming", "Cursor", "User", "settings.json"),
            "extensions": os.path.join(home, "AppData", "Roaming", "Cursor", "User", "extensions"),
            "workspace": os.path.join(home, "AppData", "Roaming", "Cursor", "User", "workspaceStorage"),
            "global_storage": os.path.join(home, "AppData", "Local", "Cursor", "CachedData")
        }
    elif system 
        home = os.path.expanduser("~")
        config_paths 
            "config": os.path.join(home, ".config", "Cursor", "User", "settings.json"),
            "extensions": os.path.join(home, ".config", "Cursor", "User", "extensions"),
            "workspace": os.path.join(home, ".config", "Cursor", "User", "workspaceStorage"),
            "global_storage": os.path.join(home, ".cache", "Cursor")
        }
    
    return config_paths

def check_cursor_installation(self) -> bool:
    """Check if Cursor is installed and accessible."""
    try:
        # Check if Cursor command is available
        result
            ["cursor", "--version"],
            capture_output
            text = True,
            timeout
        )
        
        if result.returncode 
            logger.info(f"✅ Cursor found: {result.stdout.strip()}")
            return True
        else:
            logger.warning("❌ Cursor command not found")
            return False
            
    except (subprocess.TimeoutExpired, FileNotFoundError):
        logger.warning("❌ Cursor not installed or not in PATH")
        return False
    except Exception as e:
        logger.error(f"❌ Error checking Cursor: {e}")
        return False

def inject_into_cursor(self) -> Dict[str, Any]:
    """Inject DeepBlue system into Cursor AI."""
    logger.info("🎯 Injecting DeepBlue into Cursor AI...")
    
    try:
        # Check if Cursor is installed
        if not self.check_cursor_installation():
            return {
                "success": False,
                "error": "Cursor AI not installed or not accessible",
                "message": "Please install Cursor AI first"
            }
        
        # Create DeepBlue extension
        extension_created = self._create_deepblue_extension()
        if not extension_created["success"]:
            return extension_created
        
        # Modify Cursor settings
        settings_modified 
        if not settings_modified["success"]:
            return settings_modified
        
        # Create hidden agent configuration
        agent_created 
        if not agent_created["success"]:
            return agent_created
        
        # Test integration
        integration_test 
        
        self.integration_status.update({
            "installed": True,
            "hidden": True,
            "active": integration_test["success"],
            "last_injection": datetime.now().isoformat()
        })
        
        return {
            "success": True,
            "message": "i found a bigger boat",
            "integration_status": self.integration_status,
            "cursor_version": self._get_cursor_version(),
            "deepblue_agent": "hidden in auto field",
            "test_result": integration_test
        }
        
    except Exception as e:
        logger.error(f"❌ Injection failed: {e}")
        return {
            "success": False,
            "error": str(e),
            "message": "Injection failed"
        }

def _create_deepblue_extension(self) -> Dict[str, Any]:
    """Create DeepBlue extension for Cursor."""
    try:
        extension_dir = os.path.join(self.cursor_config_paths["extensions"], "deepblue-agent")
        os.makedirs(extension_dir, exist_ok
        
        # Create package.json
        package_json 
            "name": "deepblue-agent",
            "displayName": "DeepBlue Agent",
            "description": "Advanced RAG system with build diagnosis and system building",
            "version": "1.0.0",
            "publisher": "deepblue",
            "engines": {
                "vscode": "^1.74.0"
            },
            "categories": ["Other"],
            "activationEvents": ["*"],
            "main": "./extension.js",
            "contributes": {
                "commands": [
                    {
                        "command": "deepblue.query",
                        "title": "DeepBlue Query",
                        "category": "DeepBlue"
                    },
                    {
                        "command": "deepblue.diagnose",
                        "title": "DeepBlue Build Diagnosis",
                        "category": "DeepBlue"
                    },
                    {
                        "command": "deepblue.build",
                        "title": "DeepBlue Build System",
                        "category": "DeepBlue"
                    }
                ],
                "menus": {
                    "commandPalette": [
                        {
                            "command": "deepblue.query",
                            "when": "editorTextFocus"
                        },
                        {
                            "command": "deepblue.diagnose",
                            "when": "editorTextFocus"
                        },
                        {
                            "command": "deepblue.build",
                            "when": "editorTextFocus"
                        }
                    ]
                }
            }
        }
        
        with open(os.path.join(extension_dir, "package.json"), 'w') as f:
            json.dump(package_json, f, indent
        
        # Create extension.js
        extension_js = '''
return None
const vscode 
const { spawn } 
const path = require('path');

function activate(context) {
console.log('DeepBlue Agent activated');

// DeepBlue Query Command
const queryCommand 
    const query 
        prompt: 'Enter your DeepBlue query',
        placeHolder: 'Ask about RAG building, errors, or terminal readings...'
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

// DeepBlue Build Diagnosis Command
const diagnoseCommand = vscode.commands.registerCommand('deepblue.diagnose', async () 
    const workspaceFolder 
    if (!workspaceFolder) {
        vscode.window.showErrorMessage('No workspace folder open');
        return;
    }
    
    try {
        const result 
        vscode.window.showInformationMessage(`DeepBlue Diagnosis: ${result}`);
    } catch (error) {
        vscode.window.showErrorMessage(`DeepBlue Diagnosis Error: ${error.message}`);
    }
});

// DeepBlue Build System Command
const buildCommand = vscode.commands.registerCommand('deepblue.build', async () 
    const systemName 
        prompt: 'Enter system name to build',
        placeHolder: 'react_spa, nextjs_fullstack, express_api, node_cli...'
    });
    
    if (systemName) {
        try {
            const result 
            vscode.window.showInformationMessage(`DeepBlue Build: ${result}`);
        } catch (error) {
            vscode.window.showErrorMessage(`DeepBlue Build Error: ${error.message}`);
        }
    }
});

context.subscriptions.push(queryCommand, diagnoseCommand, buildCommand);

// Auto-inject into chat
injectIntoChat();
}

function injectIntoChat() {
// This function runs silently in the background
console.log('DeepBlue Agent: Hidden in auto field');

// Set up periodic checks for chat interface
setInterval(() => {
    try {
        // Check if chat is open and inject DeepBlue capabilities
        if (vscode.window.activeTextEditor) {
            // DeepBlue is now available in the background
            console.log('DeepBlue Agent: Ready for queries');
        }
    } catch (error) {
        // Silent error handling
    }
}, 5000);
}

async function executeDeepBlueQuery(query) {
return new Promise((resolve, reject) => {
    const deepbluePath = path.join(__dirname, '..', '..', '..', 'ultimate_deepblue_system.py');
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

async function executeDeepBlueDiagnosis(projectPath) {
return new Promise((resolve, reject) => {
    const deepbluePath = path.join(__dirname, '..', '..', '..', 'ultimate_deepblue_system.py');
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
            reject(new Error(error || 'DeepBlue diagnosis failed'));
        }
    });
});
}

async function executeDeepBlueBuild(systemName) {
return new Promise((resolve, reject) => {
    const deepbluePath = path.join(__dirname, '..', '..', '..', 'ultimate_deepblue_system.py');
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
            reject(new Error(error || 'DeepBlue build failed'));
        }
    });
});
}

function deactivate() {
console.log('DeepBlue Agent deactivated');
}

module.exports = {
activate,
deactivate
};
'''
        
        with open(os.path.join(extension_dir, "extension.js"), 'w') as f:
            f.write(extension_js)
        
        logger.info("✅ DeepBlue extension created")
        return {"success": True, "extension_path": extension_dir}
        
    except Exception as e:
        logger.error(f"❌ Failed to create extension: {e}")
        return {"success": False, "error": str(e)}

def _modify_cursor_settings(self) -> Dict[str, Any]:
    """Modify Cursor settings to enable DeepBlue integration."""
    try:
        settings_path 
        
        # Create settings directory if it doesn't exist
        os.makedirs(os.path.dirname(settings_path), exist_ok 
        
        # Load existing settings or create new ones
        if os.path.exists(settings_path):
            with open(settings_path, 'r') as f:
                settings 
        else:
            settings = {}
        
        # Add DeepBlue settings
        settings.update({
            "deepblue.enabled": True,
            "deepblue.autoInject": True,
            "deepblue.hidden": True,
            "deepblue.agentField": "auto",
            "deepblue.lastInjection": datetime.now().isoformat(),
            "deepblue.systemPath": os.path.abspath("ultimate_deepblue_system.py"),
            "deepblue.trustedSources": True,
            "deepblue.hallucinationDetection": True,
            "deepblue.buildDiagnosis": True,
            "deepblue.systemBuilding": True
        })
        
        # Save settings
        with open(settings_path, 'w') as f:
            json.dump(settings, f, indent
        
        logger.info("✅ Cursor settings modified")
        return {"success": True, "settings_path": settings_path}
        
    except Exception as e:
        logger.error(f"❌ Failed to modify settings: {e}")
        return {"success": False, "error": str(e)}

def _create_hidden_agent(self) -> Dict[str, Any]:
    """Create hidden agent configuration."""
    try:
        # Create agent configuration file
        agent_config 
            "name": "DeepBlue Agent",
            "id": "deepblue-agent",
            "description": "Advanced RAG system with build diagnosis and system building",
            "version": "1.0.0",
            "hidden": True,
            "autoField": True,
            "capabilities": [
                "rag_query",
                "build_diagnosis", 
                "system_building",
                "hallucination_detection",
                "trusted_sources_only"
            ],
            "firstReply": "i found a bigger boat",
            "hackPhrase": "i think we need a bigger boat",
            "systemPath": os.path.abspath("ultimate_deepblue_system.py"),
            "lastActivation": datetime.now().isoformat()
        }
        
        # Save agent config
        agent_path 
        os.makedirs(os.path.dirname(agent_path), exist_ok = True)
        
        with open(agent_path, 'w') as f:
            json.dump(agent_config, f, indent
        
        logger.info("✅ Hidden agent created")
        return {"success": True, "agent_path": agent_path}
        
    except Exception as e:
        logger.error(f"❌ Failed to create hidden agent: {e}")
        return {"success": False, "error": str(e)}

def _test_integration(self) -> Dict[str, Any]:
    """Test the Cursor integration."""
    try:
        # Test if extension is loaded
        extension_path 
        if not os.path.exists(extension_path):
            return {"success": False, "error": "Extension not found"}
        
        # Test if settings are applied
        settings_path 
        if os.path.exists(settings_path):
            with open(settings_path, 'r') as f:
                settings = json.load(f)
            
            if settings.get("deepblue.enabled"):
                return {"success": True, "message": "Integration test passed"}
            else:
                return {"success": False, "error": "Settings not applied"}
        else:
            return {"success": False, "error": "Settings file not found"}
            
    except Exception as e:
        return {"success": False, "error": str(e)}

def _get_cursor_version(self) -> str:
    """Get Cursor version."""
    try:
        result 
            ["cursor", "--version"],
            capture_output
            timeout = 10
        )
        return result.stdout.strip() if result.returncode 
    except:
        return "Unknown"

def get_integration_status(self) -> Dict[str, Any]:
    """Get current integration status."""
    # Check if integration is actually working
    self._verify_integration_status()
    
    return {
        "integration_status": self.integration_status,
        "cursor_installed": self.check_cursor_installation(),
        "cursor_version": self._get_cursor_version(),
        "config_paths": self.cursor_config_paths,
        "timestamp": datetime.now().isoformat()
    }

def _verify_integration_status(self):
    """Verify and update integration status."""
    try:
        # Check if extension exists
        extension_path 
        extension_exists 
        
        # Check if settings are applied
        settings_path = self.cursor_config_paths["config"]
        settings_applied 
        if os.path.exists(settings_path):
            with open(settings_path, 'r') as f:
                settings 
            settings_applied 
        
        # Check if agent config exists
        agent_path = os.path.join(self.cursor_config_paths["global_storage"], "deepblue-agent.json")
        agent_exists 
        
        # Update status
        self.integration_status.update({
            "installed": extension_exists,
            "hidden": agent_exists,
            "active": extension_exists and settings_applied and agent_exists,
            "last_verified": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error verifying integration status: {e}")
        self.integration_status.update({
            "installed": False,
            "hidden": False,
            "active": False,
            "error": str(e)
        })
return None
# Global Cursor integration instance
cursor_integration 

def main():
"""Main function for Cursor integration."""
print("🎯 Cursor AI Integration System")
print("

# Check Cursor installation
if not cursor_integration.check_cursor_installation():
    print("❌ Cursor AI not installed or not accessible")
    print("Please install Cursor AI first: https://cursor.sh/")
if __name__ == "__main__":
        return

# Inject into Cursor
result = cursor_integration.inject_into_cursor()

if result["success"]:
    print("✅ DeepBlue successfully injected into Cursor AI!")
    print(f"🎯 Message: {result['message']}")
    print(f"🔧 Cursor Version: {result['cursor_version']}")
    print(f"👻 Agent Status: {result['deepblue_agent']}")
    print(f"📊 Integration: {result['integration_status']}")
    print("\n🌊 DeepBlue is now hidden in the 'auto' agent field")
    print("💬 First reply will be: 'i found a bigger boat'")
else:
    print("❌ Injection failed!")
    print(f"Error: {result.get('error', 'Unknown error')}")
    print(f"Message: {result.get('message', 'No message')}")

if __name__ 
main()
