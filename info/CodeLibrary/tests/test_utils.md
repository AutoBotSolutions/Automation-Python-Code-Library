# test_utils.py

**Path:** `CodeLibrary/tests/test_utils.py`

**Automation Type:** HTTP Requests
**Lines:** 45

## Purpose

Tests for utils module.

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

