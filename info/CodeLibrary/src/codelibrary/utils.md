# utils.py

**Path:** `CodeLibrary/src/codelibrary/utils.py`

**Automation Type:** HTTP Requests
**Lines:** 57

## Purpose

General utility functions.

## Library Context

This script is part of the HTTP/Network library, providing functions for making HTTP requests, interacting with web APIs, and handling network communications.

## Key Features

- Web API interaction

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `typing.Any`
- `typing.Callable`
- `typing.List`
- `typing.Optional`
- `hashlib`
- `json`

## Function Descriptions

- flatten - Parameters: nested_list. Performs a specific operation.
- chunk_list - Parameters: items, chunk_size. Performs a specific operation.
- safe_get - Parameters: dictionary, key, default. Performs a specific operation.
- memoize - Parameters: func. Performs a specific operation.
- generate_hash - Parameters: data, algorithm. Performs a specific operation.

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

## Classes

No classes defined in this script.

## External APIs

No external API interactions identified.

## Code Examples

### flatten

```python
def flatten(nested_list: List[Any]) -> List[Any]:
    """Flatten a nested list structure."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
```

### chunk_list

```python
def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks of specified size."""
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
```

### safe_get

```python
def safe_get(dictionary: dict, key: str, default: Any = None) -> Any:
    """Safely get a value from a dictionary with a default fallback."""
    return dictionary.get(key, default)
```

### memoize

```python
def memoize(func: Callable) -> Callable:
    """Simple memoization decorator for functions."""
    cache = {}
    
    def wrapper(*args, **kwargs):
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[
```

### generate_hash

```python
def generate_hash(data: str, algorithm: str = "sha256") -> str:
    """Generate a hash of the given data using specified algorithm."""
    hash_func = getattr(hashlib, algorithm, hashlib.sha256)
    return hash_func(data.encode()).hexdigest()
```

