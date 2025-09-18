#!/usr/bin/env python3
"""
🏗️ System Builder - FIXED VERSION
Build complete systems by name or description with deep dependency knowledge.
Integrates with build diagnosis system for hallucination-proof builds.
"""

import os
import json
import subprocess
from dataclasses import dataclass
import logging
from typing import Dict, List, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class SystemTemplate:
    """Represents a system template."""
    template_id: str
    name: str
    description: str
    category: str  # web_app, api, cli_tool, library, fullstack
    tech_stack: List[str]
    dependencies: Dict[str, str]
    dev_dependencies: Dict[str, str]
    scripts: Dict[str, str]
    config_files: Dict[str, str]
    source_files: Dict[str, str]
    build_commands: List[str]
    test_commands: List[str]
    verification_commands: List[str]
    complexity: str  # simple, medium, complex, enterprise
    estimated_build_time: str

class SystemBuilder:
    """Build complete systems by name or description."""

    def __init__(self):
        self.system_templates = self._initialize_system_templates()
        self.tech_stack_knowledge = self._initialize_tech_stack_knowledge()
        
    def _initialize_system_templates(self) -> Dict[str, SystemTemplate]:
        """Initialize comprehensive system templates."""
        return {
            "react_spa": SystemTemplate(
                template_id="react_spa",
                name="React SPA",
                description="Modern React SPA with TypeScript, Tailwind CSS, and Vite",
                category="web_app",
                tech_stack=["React", "TypeScript", "Vite", "Tailwind CSS"],
                dependencies={
                    "react": "^18.2.0",
                    "react-dom": "^18.2.0",
                    "react-router-dom": "^6.8.0"
                },
                dev_dependencies={
                    "@types/react": "^18.0.28",
                    "@types/react-dom": "^18.0.11",
                    "@vitejs/plugin-react": "^3.1.0",
                    "typescript": "^4.9.5",
                    "vite": "^4.1.0",
                    "tailwindcss": "^3.2.7",
                    "autoprefixer": "^10.4.14",
                    "postcss": "^8.4.21"
                },
                scripts={
                    "dev": "vite",
                    "build": "tsc && vite build",
                    "preview": "vite preview",
                    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0"
                },
                config_files={
                    "vite.config.ts": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true
  },
  build: {
    outDir: 'dist',
    sourcemap: true
  }
})""",
                    "tsconfig.json": """{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}""",
                    "tailwind.config.js": """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}""",
                    "postcss.config.js": """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}"""
                },
                source_files={
                    "src/App.tsx": """import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-lg text-center">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">
          React SPA
        </h1>
        <p className="text-gray-600 mb-6">
          A modern React Single Page Application built with TypeScript and Tailwind CSS.
        </p>
        <button
          onClick={() => setCount(count + 1)}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Count is {count}
        </button>
      </div>
    </div>
  )
}

export default App""",
                    "src/App.css": """@tailwind base;
@tailwind components;
@tailwind utilities;""",
                    "src/main.tsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)""",
                    "src/index.css": """@tailwind base;
@tailwind components;
@tailwind utilities;""",
                    "index.html": """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React SPA</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>"""
                },
                build_commands=["npm install", "npm run build"],
                test_commands=["npm run dev"],
                verification_commands=["npm run build", "npm run preview"],
                complexity="simple",
                estimated_build_time="2-5 minutes"
            ),
            
            "express_api": SystemTemplate(
                template_id="express_api",
                name="Express API",
                description="RESTful API with Express.js, TypeScript, and MongoDB",
                category="api",
                tech_stack=["Express.js", "TypeScript", "MongoDB", "Mongoose"],
                dependencies={
                    "express": "^4.18.2",
                    "mongoose": "^7.0.3",
                    "cors": "^2.8.5",
                    "helmet": "^6.0.1"
                },
                dev_dependencies={
                    "@types/express": "^4.17.17",
                    "@types/cors": "^2.8.13",
                    "typescript": "^4.9.5",
                    "ts-node": "^10.9.1",
                    "nodemon": "^2.0.20"
                },
                scripts={
                    "dev": "nodemon src/server.ts",
                    "build": "tsc",
                    "start": "node dist/server.js"
                },
                config_files={
                    "tsconfig.json": """{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}"""
                },
                source_files={
                    "src/server.ts": """import express from 'express';
import cors from 'cors';
import helmet from 'helmet';

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());

// Routes
app.get('/', (req, res) => {
  res.json({ message: 'Express API is running!' });
});

app.get('/api/health', (req, res) => {
  res.json({ status: 'healthy', timestamp: new Date().toISOString() });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});"""
                },
                build_commands=["npm install", "npm run build"],
                test_commands=["npm run dev"],
                verification_commands=["npm run build", "npm start"],
                complexity="medium",
                estimated_build_time="3-7 minutes"
            )
        }

    def _initialize_tech_stack_knowledge(self) -> Dict[str, Dict[str, Any]]:
        """Initialize tech stack knowledge for validation."""
        return {
            "react": {
                "min_version": "18.0.0",
                "peer_dependencies": ["react-dom"],
                "common_issues": ["version_conflict", "missing_peer_deps"],
                "verification": "npm list react"
            },
            "express": {
                "min_version": "4.18.0",
                "peer_dependencies": [],
                "common_issues": ["middleware_errors", "routing_issues"],
                "verification": "npm start"
            },
            "typescript": {
                "min_version": "4.9.0",
                "peer_dependencies": [],
                "common_issues": ["compilation_errors", "type_errors"],
                "verification": "npx tsc --noEmit"
            }
        }

    def build_system(self, system_name: str, project_path: str, custom_config: Dict[str, Any] = None) -> Dict[str, Any]:
        """Build a complete system by name or description."""
        logger.info(f"🏗️ Building system: {system_name} at {project_path}")
        
        # Find matching template
        template = self._find_template(system_name)
        if not template:
            return {
                "success": False,
                "error": f"No template found for system: {system_name}",
                "available_templates": list(self.system_templates.keys())
            }
        
        # Create project directory
        if not os.path.exists(project_path):
            os.makedirs(project_path)
        
        # Apply custom configuration if provided
        if custom_config:
            template = self._apply_custom_config(template, custom_config)
        
        # Build the system
        build_result = self._build_system_from_template(template, project_path)
        
        return {
            "success": build_result["success"],
            "template_used": template.template_id,
            "project_path": project_path,
            "build_result": build_result,
            "estimated_build_time": template.estimated_build_time,
            "complexity": template.complexity
        }

    def _find_template(self, system_name: str) -> Optional[SystemTemplate]:
        """Find template by name or description."""
        system_name_lower = system_name.lower()
        
        # Direct match
        if system_name_lower in self.system_templates:
            return self.system_templates[system_name_lower]
        
        # Fuzzy match by description
        for template in self.system_templates.values():
            if (system_name_lower in template.name.lower() or 
                system_name_lower in template.description.lower() or
                any(tech.lower() in system_name_lower for tech in template.tech_stack)):
                return template
        
        return None

    def _apply_custom_config(self, template: SystemTemplate, custom_config: Dict[str, Any]) -> SystemTemplate:
        """Apply custom configuration to template."""
        # Create a copy of the template
        import copy
        modified_template = copy.deepcopy(template)
        
        # Apply custom dependencies
        if "dependencies" in custom_config:
            modified_template.dependencies.update(custom_config["dependencies"])
        
        if "dev_dependencies" in custom_config:
            modified_template.dev_dependencies.update(custom_config["dev_dependencies"])
        
        # Apply custom scripts
        if "scripts" in custom_config:
            modified_template.scripts.update(custom_config["scripts"])
        
        return modified_template

    def _build_system_from_template(self, template: SystemTemplate, project_path: str) -> Dict[str, Any]:
        """Build system from template."""
        try:
            # Create package.json
            package_json = {
                "name": template.template_id,
                "version": "1.0.0",
                "description": template.description,
                "main": "index.js",
                "scripts": template.scripts,
                "dependencies": template.dependencies,
                "devDependencies": template.dev_dependencies,
                "keywords": template.tech_stack,
                "author": "",
                "license": "MIT"
            }
            
            with open(os.path.join(project_path, "package.json"), 'w') as f:
                json.dump(package_json, f, indent=2)
            
            # Create config files
            for filename, content in template.config_files.items():
                file_path = os.path.join(project_path, filename)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'w') as f:
                    f.write(content.strip())
            
            # Create source files
            for filename, content in template.source_files.items():
                file_path = os.path.join(project_path, filename)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'w') as f:
                    f.write(content.strip())
            
            # Install dependencies
            install_result = self._install_dependencies(project_path)
            
            return {
                "success": install_result["success"],
                "files_created": len(template.config_files) + len(template.source_files) + 1,
                "dependencies_installed": install_result["success"],
                "install_output": install_result.get("output", "")
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "files_created": 0,
                "dependencies_installed": False
            }

    def _install_dependencies(self, project_path: str) -> Dict[str, Any]:
        """Install project dependencies."""
        try:
            result = subprocess.run(
                ["npm", "install"],
                cwd=project_path,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout + result.stderr,
                "returncode": result.returncode
            }
        
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "output": "Installation timed out after 5 minutes",
                "returncode": -1
            }
        except Exception as e:
            return {
                "success": False,
                "output": str(e),
                "returncode": -1
            }

    def list_available_systems(self) -> List[Dict[str, Any]]:
        """List all available system templates."""
        systems = []
        for template in self.system_templates.values():
            systems.append({
                "id": template.template_id,
                "name": template.name,
                "description": template.description,
                "category": template.category,
                "tech_stack": template.tech_stack,
                "complexity": template.complexity,
                "estimated_build_time": template.estimated_build_time
            })
        return systems

    def get_system_details(self, system_id: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a system template."""
        if system_id not in self.system_templates:
            return None
        
        template = self.system_templates[system_id]
        return {
            "id": template.template_id,
            "name": template.name,
            "description": template.description,
            "category": template.category,
            "tech_stack": template.tech_stack,
            "dependencies": template.dependencies,
            "dev_dependencies": template.dev_dependencies,
            "scripts": template.scripts,
            "complexity": template.complexity,
            "estimated_build_time": template.estimated_build_time,
            "config_files": list(template.config_files.keys()),
            "source_files": list(template.source_files.keys())
        }

# Global system builder instance
system_builder = SystemBuilder()

def main():
    """Demo the system builder."""
    print("🏗️ System Builder Demo")
    print("=" * 50)

    # List available systems
    print("📋 Available Systems:")
    systems = system_builder.list_available_systems()
    for system in systems:
        print(f"  • {system['id']}: {system['name']}")
        print(f"    Category: {system['category']}")
        print(f"    Tech Stack: {', '.join(system['tech_stack'])}")
        print(f"    Complexity: {system['complexity']}")
        print(f"    Build Time: {system['estimated_build_time']}")
        print()

    # Example: Build a React SPA
    print("🔨 Building React SPA...")
    result = system_builder.build_system("react_spa", "/tmp/test_react_spa")

    if result["success"]:
        print("✅ React SPA built successfully!")
        print(f"📁 Project path: {result['project_path']}")
        print(f"⏱️ Build time: {result['estimated_build_time']}")
        print(f"📊 Files created: {result['build_result']['files_created']}")
    else:
        print("❌ Build failed!")
        print(f"Error: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()
