# string_helpers.py

**Path:** `CodeLibrary/src/codelibrary/string_helpers.py`

**Lines:** 72
**Size:** 2085 bytes

## Description

String manipulation and validation utilities.

## Imports

- `re`
- `typing.List`
- `typing.Optional`

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

### slugify

**Parameters:** text

Convert a string to a URL-friendly slug.

