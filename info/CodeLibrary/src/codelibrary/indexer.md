# indexer.py

**Path:** `CodeLibrary/src/codelibrary/indexer.py`

**Lines:** 102
**Size:** 3731 bytes

## Description

Code library indexer - extracts and indexes functions, classes, and documentation.

## Imports

- `inspect`
- `importlib`
- `typing.List`
- `typing.Dict`
- `typing.Any`
- `codelibrary.utils`
- `codelibrary.datastructures`
- `codelibrary.string_helpers`
- `codelibrary.file_operations`
- `codelibrary.math_helpers`
- `codelibrary.time_utils`

## Classes

### FunctionInfo

Stores information about a function.

**Methods:**
- `__init__`
- `to_dict`

### LibraryIndexer

Indexes the code library for searching.

**Methods:**
- `__init__`
- `_build_index`
- `search`
- `get_all_functions`
- `get_module_functions`
- `get_function_info`

## Functions

### __init__

**Parameters:** self, name, module, doc, signature, is_class

### to_dict

**Parameters:** self

Convert to dictionary for display.

### __init__

**Parameters:** self

### _build_index

**Parameters:** self

Build the index of all functions and classes.

### search

**Parameters:** self, query

Search for functions matching the query.

### get_all_functions

**Parameters:** self

Get all indexed functions.

### get_module_functions

**Parameters:** self, module_name

Get all functions from a specific module.

### get_function_info

**Parameters:** self, module_name, function_name

Get detailed info about a specific function.

