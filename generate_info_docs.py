#!/usr/bin/env python3
"""
Auto-generate documentation for all Python files in code-library
"""

import os
import ast
import re
from pathlib import Path

CODE_LIBRARY_PATH = "/home/robbie/Desktop/CodeLibrary/code-library"
INFO_OUTPUT_PATH = "/home/robbie/Desktop/CodeLibrary/info"

def extract_file_info(file_path):
    """Extract information from a Python file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        return None, f"Error reading file: {e}"
    
    info = {
        'filename': os.path.basename(file_path),
        'path': file_path,
        'relative_path': os.path.relpath(file_path, CODE_LIBRARY_PATH),
        'imports': [],
        'functions': [],
        'classes': [],
        'description': '',
        'lines': len(content.splitlines()),
        'size': len(content)
    }
    
    # Extract docstrings and comments
    lines = content.split('\n')
    description_lines = []
    for line in lines[:20]:  # Check first 20 lines for description
        stripped = line.strip()
        if stripped.startswith('#'):
            description_lines.append(stripped[1:].strip())
        elif stripped.startswith('"""') or stripped.startswith("'''"):
            # Docstring
            desc_match = re.search(r'["\']{3}([^"\']+)["\']{3}', content, re.DOTALL)
            if desc_match:
                info['description'] = desc_match.group(1).strip()
                break
        elif description_lines:
            break
    
    if description_lines and not info['description']:
        info['description'] = ' '.join(description_lines[:5])
    
    # Parse AST for functions and classes
    try:
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    info['imports'].append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module if node.module else ''
                for alias in node.names:
                    info['imports'].append(f"{module}.{alias.name}")
            elif isinstance(node, ast.FunctionDef):
                func_info = {
                    'name': node.name,
                    'args': [arg.arg for arg in node.args.args],
                    'docstring': ast.get_docstring(node)
                }
                info['functions'].append(func_info)
            elif isinstance(node, ast.ClassDef):
                class_info = {
                    'name': node.name,
                    'docstring': ast.get_docstring(node),
                    'methods': [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                }
                info['classes'].append(class_info)
    except Exception as e:
        info['parse_error'] = str(e)
    
    return info, None

def generate_markdown(info):
    """Generate markdown documentation from file info"""
    md = f"# {info['filename']}\n\n"
    md += f"**Path:** `{info['relative_path']}`\n\n"
    md += f"**Lines:** {info['lines']}\n"
    md += f"**Size:** {info['size']} bytes\n\n"
    
    if info['description']:
        md += f"## Description\n\n{info['description']}\n\n"
    
    if info['imports']:
        md += "## Imports\n\n"
        for imp in info['imports'][:20]:  # Limit to first 20 imports
            md += f"- `{imp}`\n"
        if len(info['imports']) > 20:
            md += f"- ... and {len(info['imports']) - 20} more\n"
        md += "\n"
    
    if info['classes']:
        md += "## Classes\n\n"
        for cls in info['classes']:
            md += f"### {cls['name']}\n\n"
            if cls['docstring']:
                md += f"{cls['docstring']}\n\n"
            if cls['methods']:
                md += "**Methods:**\n"
                for method in cls['methods']:
                    md += f"- `{method}`\n"
                md += "\n"
    
    if info['functions']:
        md += "## Functions\n\n"
        for func in info['functions'][:15]:  # Limit to first 15 functions
            md += f"### {func['name']}\n\n"
            if func['args']:
                md += f"**Parameters:** {', '.join(func['args'])}\n\n"
            if func['docstring']:
                md += f"{func['docstring']}\n\n"
        if len(info['functions']) > 15:
            md += f"... and {len(info['functions']) - 15} more functions\n\n"
    
    if 'parse_error' in info:
        md += f"## Parse Error\n\n{info['parse_error']}\n\n"
    
    return md

def main():
    """Main function to generate documentation"""
    print("Starting documentation generation...")
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
    
    # Generate documentation for each file
    success_count = 0
    error_count = 0
    
    for i, file_path in enumerate(python_files, 1):
        print(f"Processing {i}/{len(python_files)}: {os.path.basename(file_path)}")
        
        info, error = extract_file_info(file_path)
        if error:
            print(f"  Error: {error}")
            error_count += 1
            continue
        
        # Create output path matching directory structure
        rel_path = os.path.relpath(file_path, CODE_LIBRARY_PATH)
        output_path = os.path.join(INFO_OUTPUT_PATH, rel_path.replace('.py', '.md'))
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Generate markdown
        md = generate_markdown(info)
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md)
        
        success_count += 1
    
    print(f"\nDocumentation generation complete!")
    print(f"Success: {success_count}")
    print(f"Errors: {error_count}")
    print(f"Total: {len(python_files)}")

if __name__ == '__main__':
    main()
