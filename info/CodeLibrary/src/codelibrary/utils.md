# utils.py

**Path:** `CodeLibrary/src/codelibrary/utils.py`

**Lines:** 57
**Size:** 1638 bytes

## Description

General utility functions.

## Imports

- `typing.Any`
- `typing.Callable`
- `typing.List`
- `typing.Optional`
- `hashlib`
- `json`

## Functions

### flatten

**Parameters:** nested_list

Flatten a nested list structure.

### chunk_list

**Parameters:** items, chunk_size

Split a list into chunks of specified size.

### safe_get

**Parameters:** dictionary, key, default

Safely get a value from a dictionary with a default fallback.

### memoize

**Parameters:** func

Simple memoization decorator for functions.

### generate_hash

**Parameters:** data, algorithm

Generate a hash of the given data using specified algorithm.

### to_json

**Parameters:** data, indent

Convert Python object to JSON string.

### from_json

**Parameters:** json_str

Parse JSON string to Python object.

### wrapper

