# test_string_helpers.py

**Path:** `CodeLibrary/tests/test_string_helpers.py`

**Automation Type:** Email Automation
**Lines:** 49

## Purpose

Tests for string_helpers module.

## Key Features

- Email sending/receiving

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `pytest`
- `codelibrary.string_helpers.camel_to_snake`
- `codelibrary.string_helpers.snake_to_camel`
- `codelibrary.string_helpers.truncate`
- `codelibrary.string_helpers.is_email`
- `codelibrary.string_helpers.remove_extra_spaces`
- `codelibrary.string_helpers.reverse_string`
- `codelibrary.string_helpers.count_words`

## Functions

### test_camel_to_snake

### test_snake_to_camel

### test_truncate

### test_is_email

### test_remove_extra_spaces

### test_reverse_string

### test_count_words

## Code Examples

### test_camel_to_snake

```python
def test_camel_to_snake():
    assert camel_to_snake("CamelCase") == "camel_case"
    assert camel_to_snake("myVariableName") == "my_variable_name"
```

### test_snake_to_camel

```python
def test_snake_to_camel():
    assert snake_to_camel("snake_case") == "SnakeCase"
    assert snake_to_camel("my_variable_name") == "MyVariableName"
```

### test_truncate

```python
def test_truncate():
    assert truncate("Hello World", 5) == "He..."
    assert truncate("Hi", 10) == "Hi"
```

