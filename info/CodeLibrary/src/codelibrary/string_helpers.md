# string_helpers.py

**Path:** `CodeLibrary/src/codelibrary/string_helpers.py`

**Automation Type:** HTTP Requests
**Lines:** 72

## Purpose

String manipulation and validation utilities.

## Library Context

This script is part of the HTTP/Network library, providing functions for making HTTP requests, interacting with web APIs, and handling network communications.

## Key Features

- Web API interaction

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `re`
- `typing.List`
- `typing.Optional`

## Function Descriptions

- camel_to_snake - Parameters: name. Performs a specific operation.
- snake_to_camel - Parameters: name. Performs a specific operation.
- truncate - Parameters: text, max_length, suffix. Performs a specific operation.
- is_email - Parameters: email. Performs a specific operation.
- is_url - Parameters: url. Performs a specific operation.

## Functions

### camel_to_snake

**Parameters:** name

Convert CamelCase to snake_case.

### snake_to_camel

**Parameters:** name

Convert snake_case to CamelCase.

### truncate

**Parameters:** text, max_length, suffix

Truncate text to a maximum length with optional suffix.

### is_email

**Parameters:** email

Validate if a string is a valid email format.

### is_url

**Parameters:** url

Validate if a string is a valid URL format.

### remove_extra_spaces

**Parameters:** text

Remove extra whitespace from a string.

### reverse_string

**Parameters:** text

Reverse a string.

### count_words

**Parameters:** text

Count the number of words in a string.

### extract_numbers

**Parameters:** text

Extract all numbers from a string.

### mask_string

**Parameters:** text, visible_chars, mask_char

Mask a string showing only the first and last few characters.

... and 1 more functions

## Classes

No classes defined in this script.

## External APIs

No external API interactions identified.

## Code Examples

### camel_to_snake

```python
def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
```

### snake_to_camel

```python
def snake_to_camel(name: str) -> str:
    """Convert snake_case to CamelCase."""
    components = name.split('_')
    return ''.join(x.title() for x in components)
```

### truncate

```python
def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to a maximum length with optional suffix."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
```

### is_email

```python
def is_email(email: str) -> bool:
    """Validate if a string is a valid email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

### is_url

```python
def is_url(url: str) -> bool:
    """Validate if a string is a valid URL format."""
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))
```

