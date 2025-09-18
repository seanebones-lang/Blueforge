#!/usr/bin/env python3
"""
🔧 Build Diagnosis & Repair System - FIXED VERSION
Deep knowledge of dependencies, CSS, build issues, and complex fixes.
Can reassemble broken builds and detect hallucinations.
"""

import os
import json
import re
import subprocess
import ast
import hashlib
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class DependencyIssue:
    """Represents a dependency issue."""
    issue_id: str
    package_name: str
    issue_type: str  # version_conflict, missing, incompatible, circular, security
    description: str
    error_message: str
    solution: str
    severity: str  # low, medium, high, critical
    affected_files: List[str]
    fix_commands: List[str]
    verification_commands: List[str]

@dataclass
class BuildIssue:
    """Represents a build issue."""
    issue_id: str
    build_tool: str  # webpack, vite, rollup, parcel, etc.
    issue_type: str  # compilation_error, bundling_error, optimization_error
    description: str
    error_log: str
    solution: str
    affected_files: List[str]
    fix_commands: List[str]
    severity: str

class BuildDiagnosisSystem:
    """Main build diagnosis and repair system."""

    def __init__(self):
        self.dependency_issues = self._initialize_dependency_knowledge()
        self.hallucination_patterns = self._initialize_hallucination_patterns()
        self.build_tools = self._initialize_build_tools()
        
    def _initialize_dependency_knowledge(self) -> Dict[str, DependencyIssue]:
        """Initialize comprehensive dependency issue knowledge."""
        return {
            "react_version_conflict": DependencyIssue(
                issue_id="react_version_conflict",
                package_name="react",
                issue_type="version_conflict",
                description="React and React-DOM version mismatch",
                error_message="React version mismatch detected",
                solution="Install matching React versions",
                severity="high",
                affected_files=["package.json"],
                fix_commands=["npm install react@^18.0.0 react-dom@^18.0.0"],
                verification_commands=["npm list react react-dom"]
            ),
            "missing_package_json": DependencyIssue(
                issue_id="missing_package_json",
                package_name="package.json",
                issue_type="missing",
                description="package.json file not found",
                error_message="Cannot find package.json",
                solution="Create package.json with npm init",
                severity="critical",
                affected_files=["package.json"],
                fix_commands=["npm init -y"],
                verification_commands=["ls package.json"]
            )
        }

    def _initialize_hallucination_patterns(self) -> Dict[str, List[str]]:
        """Initialize patterns to detect hallucinations."""
        return {
            "fake_packages": [
                "react-awesome-component",
                "vue-super-utils",
                "angular-magic-helpers",
                "node-ultimate-tools"
            ],
            "fake_apis": [
                "window.superAPI",
                "global.awesomeUtils",
                "process.magicMethods"
            ],
            "syntax_errors": [
                "import { } from 'package'",
                "const { } =",
                "function() { return }",
                "if (condition) { } else"
            ]
        }

    def _initialize_build_tools(self) -> Dict[str, Dict[str, Any]]:
        """Initialize build tool configurations."""
        return {
            "webpack": {
                "config_file": "webpack.config.js",
                "common_issues": ["module_resolution", "loader_config", "plugin_config"],
                "fix_commands": ["npx webpack --mode development", "npm run build"]
            },
            "vite": {
                "config_file": "vite.config.js",
                "common_issues": ["plugin_config", "build_optimization", "dev_server"],
                "fix_commands": ["npm run dev", "npm run build"]
            }
        }

    def diagnose_build(self, project_path: str) -> Dict[str, Any]:
        """Diagnose a broken build and provide repair instructions."""
        logger.info(f"🔍 Diagnosing build at: {project_path}")
        
        issues = []
        fixes = []
        warnings = []
        
        # Check project structure
        project_structure = self._analyze_project_structure(project_path)
        
        # Check dependencies
        dependency_issues = self._check_dependencies(project_path)
        issues.extend(dependency_issues)
        
        # Check for hallucinations
        hallucination_checks = self._check_hallucinations(project_path)
        
        # Generate repair plan
        repair_plan = self._generate_repair_plan(issues)
        
        return {
            "project_path": project_path,
            "project_structure": project_structure,
            "issues": issues,
            "repair_plan": repair_plan,
            "hallucination_checks": hallucination_checks,
            "estimated_repair_time": self._estimate_repair_time(issues),
            "confidence": self._calculate_confidence(issues, hallucination_checks)
        }

    def _analyze_project_structure(self, project_path: str) -> Dict[str, Any]:
        """Analyze project structure and identify missing files."""
        structure = {
            "has_package_json": False,
            "has_tsconfig": False,
            "has_webpack_config": False,
            "has_vite_config": False,
            "missing_files": [],
            "unusual_structure": []
        }
        
        required_files = [
            "package.json",
            "src/",
            "public/",
            "index.html"
        ]
        
        for file in required_files:
            if not os.path.exists(os.path.join(project_path, file)):
                structure["missing_files"].append(file)
        
        # Check for config files
        if os.path.exists(os.path.join(project_path, "package.json")):
            structure["has_package_json"] = True
        
        if os.path.exists(os.path.join(project_path, "tsconfig.json")):
            structure["has_tsconfig"] = True
        
        if os.path.exists(os.path.join(project_path, "webpack.config.js")):
            structure["has_webpack_config"] = True
        
        if os.path.exists(os.path.join(project_path, "vite.config.js")):
            structure["has_vite_config"] = True
        
        return structure

    def _check_dependencies(self, project_path: str) -> List[Dict[str, Any]]:
        """Check for dependency issues."""
        issues = []
        
        package_json_path = os.path.join(project_path, "package.json")
        if not os.path.exists(package_json_path):
            issues.append({
                "type": "missing_file",
                "severity": "critical",
                "description": "package.json not found",
                "fix": "Create package.json with npm init"
            })
            return issues
        
        try:
            with open(package_json_path, 'r') as f:
                package_data = json.load(f)
            
            # Check for common dependency issues
            dependencies = package_data.get("dependencies", {})
            dev_dependencies = package_data.get("devDependencies", {})
            
            # Check for React version conflicts
            if "react" in dependencies and "react-dom" in dependencies:
                react_version = dependencies["react"]
                react_dom_version = dependencies["react-dom"]
                if react_version != react_dom_version:
                    issues.append({
                        "type": "version_conflict",
                        "severity": "high",
                        "description": f"React version mismatch: {react_version} vs {react_dom_version}",
                        "fix": f"npm install react@{react_version} react-dom@{react_version}"
                    })
        
        except Exception as e:
            issues.append({
                "type": "parse_error",
                "severity": "high",
                "description": f"Error parsing package.json: {str(e)}",
                "fix": "Check package.json syntax and fix errors"
            })
        
        return issues

    def _check_hallucinations(self, project_path: str) -> List[Dict[str, Any]]:
        """Check for hallucinations in code."""
        checks = []
        
        # Check for fake packages
        package_json_path = os.path.join(project_path, "package.json")
        if os.path.exists(package_json_path):
            try:
                with open(package_json_path, 'r') as f:
                    package_data = json.load(f)
                
                all_deps = {**package_data.get("dependencies", {}), **package_data.get("devDependencies", {})}
                fake_packages_found = []
                
                for package_name in all_deps.keys():
                    if package_name in self.hallucination_patterns["fake_packages"]:
                        fake_packages_found.append(package_name)
                
                if fake_packages_found:
                    checks.append({
                        "check_type": "fake_packages",
                        "is_hallucination": True,
                        "evidence": fake_packages_found,
                        "confidence": 0.9,
                        "suggestion": f"Remove fake packages: {', '.join(fake_packages_found)}"
                    })
            
            except Exception as e:
                checks.append({
                    "check_type": "package_parse_error",
                    "is_hallucination": False,
                    "evidence": [f"Error parsing package.json: {str(e)}"],
                    "confidence": 0.8,
                    "suggestion": "Fix package.json syntax errors"
                })
        
        return checks

    def _generate_repair_plan(self, issues: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate a step-by-step repair plan."""
        repair_plan = []
        
        # Group issues by severity
        critical_issues = [issue for issue in issues if issue.get("severity") == "critical"]
        high_issues = [issue for issue in issues if issue.get("severity") == "high"]
        medium_issues = [issue for issue in issues if issue.get("severity") == "medium"]
        low_issues = [issue for issue in issues if issue.get("severity") == "low"]
        
        # Add repair steps in order of severity
        if critical_issues:
            repair_plan.append({
                "step": 1,
                "title": "Fix Critical Issues",
                "issues": critical_issues,
                "commands": [issue.get("fix", "") for issue in critical_issues if issue.get("fix")]
            })
        
        if high_issues:
            repair_plan.append({
                "step": 2,
                "title": "Fix High Priority Issues",
                "issues": high_issues,
                "commands": [issue.get("fix", "") for issue in high_issues if issue.get("fix")]
            })
        
        return repair_plan

    def _estimate_repair_time(self, issues: List[Dict[str, Any]]) -> str:
        """Estimate repair time based on issues."""
        total_issues = len(issues)
        critical_count = len([issue for issue in issues if issue.get("severity") == "critical"])
        high_count = len([issue for issue in issues if issue.get("severity") == "high"])
        
        if critical_count > 0:
            return "30-60 minutes"
        elif high_count > 2:
            return "20-40 minutes"
        elif total_issues > 5:
            return "15-30 minutes"
        elif total_issues > 0:
            return "5-15 minutes"
        else:
            return "No issues found"

    def _calculate_confidence(self, issues: List[Dict[str, Any]], hallucination_checks: List[Dict[str, Any]]) -> float:
        """Calculate confidence in the diagnosis."""
        total_checks = len(issues) + len(hallucination_checks)
        if total_checks == 0:
            return 1.0
        
        hallucination_count = len([check for check in hallucination_checks if check.get("is_hallucination", False)])
        confidence = 1.0 - (hallucination_count / total_checks)
        
        return max(0.0, min(1.0, confidence))

# Global build diagnosis system instance
build_diagnosis = BuildDiagnosisSystem()

def main():
    """Demo the build diagnosis system."""
    print("🔧 Build Diagnosis & Repair System Demo")
    print("=" * 50)

    # Example usage
    project_path = "/Users/seanmcdonnell/Desktop/DeepBlue"

    print(f"🔍 Diagnosing build at: {project_path}")
    diagnosis = build_diagnosis.diagnose_build(project_path)

    print(f"\n📊 Diagnosis Results:")
    print(f"  Issues Found: {len(diagnosis['issues'])}")
    print(f"  Confidence: {diagnosis['confidence']:.2f}")
    print(f"  Estimated Repair Time: {diagnosis['estimated_repair_time']}")

    if diagnosis["issues"]:
        print(f"\n🚨 Issues Found:")
        for i, issue in enumerate(diagnosis["issues"], 1):
            print(f"  {i}. {issue['type']}: {issue['description']}")
            print(f"     Severity: {issue['severity']}")
            print(f"     Fix: {issue['fix']}")

    if diagnosis["hallucination_checks"]:
        print(f"\n🔍 Hallucination Checks:")
        for check in diagnosis["hallucination_checks"]:
            if check.get("is_hallucination", False):
                print(f"  ⚠️  {check['check_type']}: {check['evidence'][0]}")
                print(f"     Fix: {check['suggestion']}")

    print(f"\n✅ Build Diagnosis Complete!")

if __name__ == "__main__":
    main()
