# Not Contains.py

**Path:** `QualifierFunction/Not Contains.py`

**Automation Type:** General Automation
**Lines:** 33

## Purpose

python set a variable called 'not_contains' set the value to '10' now using a qualifier function set the condition to search a page for the number 10, if the page dose not contain the number 10 then set the variable 'not_contains' to true and if it dose contain the number 10 set it to false

## Library Context

This script is part of the general automation library, providing utility functions for common automation tasks.

## Key Features

No specific features documented.

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

No external dependencies identified.

## Function Descriptions

- check_page_content - Parameters: page_content. Performs a specific operation.

## Functions

No functions defined in this script.

## Classes

No classes defined in this script.

## External APIs

No external API interactions identified.

## Code Examples

### check_page_content

```python
def check_page_content(page_content):
    global not_contains  # Declare it as global to modify the variable outside the function
    if '10' not in page_content:
        not_contains = True  # Set to True if "10" is not found
    else:
        not_contains = False
```

