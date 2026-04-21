# Code Snippets Documentation

This directory contains auto-generated documentation for all Python files in the code-library.

## Overview

Every Python script in the `code-library/` directory has been documented with markdown files that include:
- File name and path
- Line count and size
- Description (from comments/docstrings)
- Import statements
- Classes and their methods
- Functions and their parameters
- Docstrings

## Structure

The documentation mirrors the directory structure of the code-library:

```
info/
├── AccountFuntions/
│   ├── Account Login.py.md
│   └── ...
├── BrowserCommands/
│   ├── NavigateTo URL.py.md
│   └── ...
├── ...
```

## Statistics

- **Total Files Documented:** 371
- **Categories:** 36
- **Generation Date:** 2026-04-20

## Documentation Format

Each markdown file includes:

### Header
- File name
- Relative path
- Line count
- File size

### Description
- Extracted from comments or docstrings
- Purpose and functionality

### Imports
- All imported modules and functions
- Limited to first 20 imports for readability

### Classes
- Class names
- Docstrings
- Methods

### Functions
- Function names
- Parameters
- Docstrings
- Limited to first 15 functions for readability

## Regenerating Documentation

To regenerate the documentation:

```bash
python3 generate_info_docs.py
```

This will:
- Scan all Python files in code-library
- Extract information using AST parsing
- Generate markdown documentation
- Save to info directory with matching structure

## Usage

Navigate to any category directory to find documentation for specific scripts. Each file is named with `.md` extension matching the original Python file.

Example:
- Original: `code-library/BrowserCommands/NavigateTo URL.py`
- Documentation: `info/BrowserCommands/NavigateTo URL.py.md`
