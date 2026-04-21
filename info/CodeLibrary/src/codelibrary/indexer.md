# indexer.py

**Path:** `CodeLibrary/src/codelibrary/indexer.py`

**Automation Type:** HTTP Requests
**Lines:** 102

## Purpose

Code library indexer - extracts and indexes functions, classes, and documentation.

## Library Context

This script is part of the HTTP/Network library, providing functions for making HTTP requests, interacting with web APIs, and handling network communications.

## Key Features

- Web API interaction

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

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

## Function Descriptions

- __init__ - Parameters: self, name, module, doc, signature, is_class. Performs a specific operation.
- to_dict - Parameters: self. Performs a specific operation.
- __init__ - Parameters: self. Performs a specific operation.
- get_all_functions - Parameters: self. Performs a specific operation.
- get_module_functions - Parameters: self, module_name. Performs a specific operation.

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
- ... and 1 more

## Code Examples

### __init__

```python
def __init__(self, name: str, module: str, doc: str, signature: str, is_class: bool = False):
        self.name = name
        self.module = module
        self.doc = doc
        self.signature = signature
        self.is_class = is_class
```

### to_dict

```python
def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for display."""
        return {
            "name": self.name,
            "module": self.module,
            "doc": self.doc,
            "signature": self.signature,
            "is_class": self.is_class
        }
```

### __init__

```python
def __init__(self):
        self.modules = {
            "utils": utils,
            "datastructures": datastructures,
            "string_helpers": string_helpers,
            "file_operations": file_operations,
            "math_helpers": math_helpers,
            "time_utils": time_utils
        
```

### get_all_functions

```python
def get_all_functions(self) -> List[FunctionInfo]:
        """Get all indexed functions."""
        all_funcs = []
        for functions in self.index.values():
            all_funcs.extend(functions)
        return all_funcs
```

### get_module_functions

```python
def get_module_functions(self, module_name: str) -> List[FunctionInfo]:
        """Get all functions from a specific module."""
        return self.index.get(module_name, [])
```

