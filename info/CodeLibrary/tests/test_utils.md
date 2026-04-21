# test_utils.py

**Path:** `CodeLibrary/tests/test_utils.py`

**Automation Type:** HTTP Requests
**Lines:** 45

## Purpose

Tests for utils module.

## Library Context

This script is part of the HTTP/Network library, providing functions for making HTTP requests, interacting with web APIs, and handling network communications.

## Key Features

- Web API interaction

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `pytest`
- `codelibrary.utils.flatten`
- `codelibrary.utils.chunk_list`
- `codelibrary.utils.safe_get`
- `codelibrary.utils.memoize`
- `codelibrary.utils.generate_hash`

## Function Descriptions

- test_flatten - Performs a specific operation.
- test_chunk_list - Performs a specific operation.
- test_safe_get - Performs a specific operation.
- test_memoize - Performs a specific operation.
- test_generate_hash - Performs a specific operation.

## Functions

### test_flatten

### test_chunk_list

### test_safe_get

### test_memoize

### test_generate_hash

### expensive_function

**Parameters:** x

## Code Examples

### test_flatten

```python
def test_flatten():
    assert flatten([1, [2, [3, 4], 5]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
```

### test_chunk_list

```python
def test_chunk_list():
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list([1, 2, 3], 5) == [[1, 2, 3]]
```

### test_safe_get

```python
def test_safe_get():
    d = {"a": 1, "b": 2}
    assert safe_get(d, "a") == 1
    assert safe_get(d, "c", "default") == "default"
```

### test_memoize

```python
def test_memoize():
    call_count = 0
    
    @memoize
    def expensive_function(x):
        nonlocal call_count
        call_count += 1
        return x * 2
    
    assert expensive_function(5) == 10
    assert call_count == 1
    assert expensive_function(5) == 10
    assert call_count == 1
```

### test_generate_hash

```python
def test_generate_hash():
    hash1 = generate_hash("test")
    hash2 = generate_hash("test")
    assert hash1 == hash2
    assert hash1 != generate_hash("different")
```

