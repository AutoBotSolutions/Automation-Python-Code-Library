#!/usr/bin/env python3
"""
Enhanced documentation generator that deeply analyzes code snippets
and explains their function within the library system.
"""

import os
import ast
import re
from pathlib import Path

CODE_LIBRARY_PATH = "/home/robbie/Desktop/CodeLibrary/code-library"
INFO_OUTPUT_PATH = "/home/robbie/Desktop/CodeLibrary/info"

def analyze_code_functionality(content, filename):
    """Deep analysis of code functionality"""
    analysis = {
        'purpose': '',
        'key_features': [],
        'dependencies': [],
        'external_apis': [],
        'automation_type': '',
        'usage_pattern': '',
        'code_examples': [],
        'function_descriptions': [],
        'library_context': ''
    }
    
    lines = content.split('\n')
    
    # Extract purpose from comments and docstrings
    # Handle AI conversation format: "## Me" on line 1, purpose on line 2
    if len(lines) >= 2 and lines[0].strip() == '## Me':
        analysis['purpose'] = lines[1].strip()
    else:
        purpose_lines = []
        for i, line in enumerate(lines[:30]):
            stripped = line.strip()
            if stripped.startswith('#') and not stripped.startswith('##'):
                purpose_lines.append(stripped[1:].strip())
            elif '"""' in stripped or "'''" in stripped:
                # Extract docstring
                doc_match = re.search(r'["\']{3}([^"\']+)["\']{3}', content, re.DOTALL)
                if doc_match:
                    analysis['purpose'] = doc_match.group(1).strip()[:500]
                    break
        
        if purpose_lines and not analysis['purpose']:
            analysis['purpose'] = ' '.join(purpose_lines[:10])
    
    # Detect automation type based on imports and patterns
    selenium_keywords = ['selenium', 'webdriver', 'chrome', 'firefox', 'browser']
    db_keywords = ['sqlite', 'mysql', 'postgres', 'database', 'sql', 'cursor']
    file_keywords = ['open(', 'read(', 'write(', 'os.path', 'shutil']
    http_keywords = ['requests', 'urllib', 'http', 'post(', 'get(']
    email_keywords = ['smtp', 'email', 'sendmail']
    threading_keywords = ['threading', 'Thread', 'thread']
    
    if any(kw in content.lower() for kw in selenium_keywords):
        analysis['automation_type'] = 'Browser Automation'
        analysis['key_features'].append('Web browser control')
    elif any(kw in content.lower() for kw in db_keywords):
        analysis['automation_type'] = 'Database Operations'
        analysis['key_features'].append('Database interaction')
    elif any(kw in content.lower() for kw in file_keywords):
        analysis['automation_type'] = 'File Operations'
        analysis['key_features'].append('File system manipulation')
    elif any(kw in content.lower() for kw in http_keywords):
        analysis['automation_type'] = 'HTTP Requests'
        analysis['key_features'].append('Web API interaction')
    elif any(kw in content.lower() for kw in email_keywords):
        analysis['automation_type'] = 'Email Automation'
        analysis['key_features'].append('Email sending/receiving')
    elif any(kw in content.lower() for kw in threading_keywords):
        analysis['automation_type'] = 'Threading/Multi-processing'
        analysis['key_features'].append('Parallel execution')
    else:
        analysis['automation_type'] = 'General Automation'
    
    # Extract external APIs
    api_patterns = [
        r'https?://[^\s\']+',
        r'api[_-]?key',
        r'endpoint',
        r'base[_-]?url'
    ]
    for pattern in api_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        analysis['external_apis'].extend(matches)
    
    # Extract usage pattern
    if 'def ' in content:
        analysis['usage_pattern'] = 'Function-based - Provides reusable functions'
    if 'class ' in content:
        analysis['usage_pattern'] = 'Object-oriented - Provides classes and methods'
    if 'if __name__' in content:
        analysis['usage_pattern'] += ' with standalone execution capability'
    
    # Extract code snippets and function descriptions
    code_snippets = []
    try:
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_code = ast.get_source_segment(content, node)
                if func_code and len(func_code) < 500:
                    code_snippets.append({
                        'name': node.name,
                        'code': func_code[:300]
                    })
                    # Add function description
                    desc = f"{node.name} - "
                    if node.args.args:
                        desc += f"Parameters: {', '.join([arg.arg for arg in node.args.args])}. "
                    if node.name.lower() in ['connect', 'open', 'start', 'begin']:
                        desc += "Initializes a connection or process."
                    elif node.name.lower() in ['close', 'end', 'stop', 'shutdown']:
                        desc += "Terminates or closes a connection or process."
                    elif node.name.lower() in ['get', 'fetch', 'retrieve', 'read']:
                        desc += "Retrieves data or information."
                    elif node.name.lower() in ['set', 'update', 'modify', 'change']:
                        desc += "Modifies or updates data or settings."
                    elif node.name.lower() in ['send', 'post', 'submit']:
                        desc += "Sends data or requests to a target."
                    elif node.name.lower() in ['delete', 'remove']:
                        desc += "Deletes or removes data or resources."
                    elif node.name.lower() in ['create', 'add', 'insert']:
                        desc += "Creates or adds new data or resources."
                    elif node.name.lower() in ['execute', 'run', 'perform']:
                        desc += "Executes an action or command."
                    else:
                        desc += "Performs a specific operation."
                    analysis['function_descriptions'].append(desc)
                if len(code_snippets) >= 5:
                    break
    except:
        pass
    
    analysis['code_examples'] = code_snippets
    
    # Add library context based on automation type
    if analysis['automation_type'] == 'Browser Automation':
        analysis['library_context'] = "This script is part of the browser automation library, providing functions for controlling web browsers, navigating to URLs, interacting with web elements, and automating web-based tasks."
    elif analysis['automation_type'] == 'Database Operations':
        analysis['library_context'] = "This script is part of the database operations library, providing functions for connecting to databases, executing SQL queries, and managing database transactions."
    elif analysis['automation_type'] == 'File Operations':
        analysis['library_context'] = "This script is part of the file operations library, providing functions for file system manipulation including creating, reading, writing, and deleting files and directories."
    elif analysis['automation_type'] == 'HTTP Requests':
        analysis['library_context'] = "This script is part of the HTTP/Network library, providing functions for making HTTP requests, interacting with web APIs, and handling network communications."
    elif analysis['automation_type'] == 'Email Automation':
        analysis['library_context'] = "This script is part of the email automation library, providing functions for sending, receiving, and managing email communications."
    elif analysis['automation_type'] == 'Threading/Multi-processing':
        analysis['library_context'] = "This script is part of the threading library, providing functions for parallel execution, multi-threading, and concurrent task processing."
    else:
        analysis['library_context'] = "This script is part of the general automation library, providing utility functions for common automation tasks."
    
    return analysis

def generate_enhanced_markdown(file_path, analysis, basic_info):
    """Generate enhanced markdown documentation"""
    md = f"# {basic_info['filename']}\n\n"
    
    md += f"**Path:** `{basic_info['relative_path']}`\n\n"
    md += f"**Automation Type:** {analysis['automation_type']}\n"
    md += f"**Lines:** {basic_info['lines']}\n\n"
    
    # Purpose section
    if analysis['purpose']:
        md += "## Purpose\n\n"
        md += f"{analysis['purpose']}\n\n"
    else:
        md += "## Purpose\n\n"
        md += "No specific purpose documented in the file.\n\n"
    
    # Library context
    if analysis['library_context']:
        md += "## Library Context\n\n"
        md += f"{analysis['library_context']}\n\n"
    
    # Key features
    if analysis['key_features']:
        md += "## Key Features\n\n"
        for feature in analysis['key_features']:
            md += f"- {feature}\n"
        md += "\n"
    else:
        md += "## Key Features\n\n"
        md += "No specific features documented.\n\n"
    
    # Usage pattern
    if analysis['usage_pattern']:
        md += "## Usage Pattern\n\n"
        md += f"{analysis['usage_pattern']}\n\n"
    else:
        md += "## Usage Pattern\n\n"
        md += "Usage pattern not identified.\n\n"
    
    # Dependencies
    if basic_info['imports']:
        md += "## Dependencies\n\n"
        for imp in basic_info['imports'][:15]:
            md += f"- `{imp}`\n"
        if len(basic_info['imports']) > 15:
            md += f"- ... and {len(basic_info['imports']) - 15} more\n"
        md += "\n"
    else:
        md += "## Dependencies\n\n"
        md += "No external dependencies identified.\n\n"
    
    # Functions
    if analysis['function_descriptions']:
        md += "## Function Descriptions\n\n"
        for desc in analysis['function_descriptions']:
            md += f"- {desc}\n"
        md += "\n"
    else:
        md += "## Function Descriptions\n\n"
        md += "No function descriptions available.\n\n"
    
    if basic_info['functions']:
        md += "## Functions\n\n"
        for func in basic_info['functions'][:10]:
            md += f"### {func['name']}\n\n"
            if func['args']:
                md += f"**Parameters:** {', '.join(func['args'])}\n\n"
            if func['docstring']:
                md += f"{func['docstring'][:300]}\n\n"
        if len(basic_info['functions']) > 10:
            md += f"... and {len(basic_info['functions']) - 10} more functions\n\n"
    else:
        md += "## Functions\n\n"
        md += "No functions defined in this script.\n\n"
    
    # Classes
    if basic_info['classes']:
        md += "## Classes\n\n"
        for cls in basic_info['classes']:
            md += f"### {cls['name']}\n\n"
            if cls['docstring']:
                md += f"{cls['docstring'][:300]}\n\n"
            if cls['methods']:
                md += "**Methods:**\n"
                for method in cls['methods'][:5]:
                    md += f"- `{method}`\n"
                if len(cls['methods']) > 5:
                    md += f"- ... and {len(cls['methods']) - 5} more\n"
                md += "\n"
    else:
        md += "## Classes\n\n"
        md += "No classes defined in this script.\n\n"
    
    # External APIs
    if analysis['external_apis']:
        md += "## External APIs\n\n"
        md += "This script interacts with external services:\n"
        for api in analysis['external_apis'][:5]:
            md += f"- `{api}`\n"
        md += "\n"
    else:
        md += "## External APIs\n\n"
        md += "No external API interactions identified.\n\n"
    
    # Code examples
    if analysis['code_examples']:
        md += "## Code Examples\n\n"
        for snippet in analysis['code_examples']:
            md += f"### {snippet['name']}\n\n"
            md += "```python\n"
            md += snippet['code']
            md += "\n```\n\n"
    else:
        md += "## Code Examples\n\n"
        md += "No code examples available.\n\n"
    
    return md

def main():
    """Main function to generate enhanced documentation"""
    print("Starting enhanced documentation generation...")
    print(f"Code library path: {CODE_LIBRARY_PATH}")
    print(f"Output path: {INFO_OUTPUT_PATH}")
    
    # Find all Python files
    python_files = []
    for root, dirs, files in os.walk(CODE_LIBRARY_PATH):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    print(f"Found {len(python_files)} Python files")
    
    # Import the basic extraction functions
    import sys
    sys.path.insert(0, '/home/robbie/Desktop/CodeLibrary')
    from generate_info_docs import extract_file_info
    
    # Generate enhanced documentation for each file
    success_count = 0
    error_count = 0
    
    for i, file_path in enumerate(python_files, 1):
        if i % 50 == 0:
            print(f"Processing {i}/{len(python_files)}...")
        
        # Get basic info
        basic_info, error = extract_file_info(file_path)
        if error:
            print(f"  Error: {error}")
            error_count += 1
            continue
        
        # Read content for deep analysis
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"  Error reading: {e}")
            error_count += 1
            continue
        
        # Deep analysis
        analysis = analyze_code_functionality(content, basic_info['filename'])
        
        # Create output path
        rel_path = os.path.relpath(file_path, CODE_LIBRARY_PATH)
        output_path = os.path.join(INFO_OUTPUT_PATH, rel_path.replace('.py', '.md'))
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Generate enhanced markdown
        md = generate_enhanced_markdown(file_path, analysis, basic_info)
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md)
        
        success_count += 1
    
    print(f"\nEnhanced documentation generation complete!")
    print(f"Success: {success_count}")
    print(f"Errors: {error_count}")
    print(f"Total: {len(python_files)}")

if __name__ == '__main__':
    main()
