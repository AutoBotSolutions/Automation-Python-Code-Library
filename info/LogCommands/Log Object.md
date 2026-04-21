# Log Object.py

**Path:** `LogCommands/Log Object.py`

**Automation Type:** General Automation
**Lines:** 84

## Purpose

Create a logger object Set the severity level (default is WARNING) Create a console handler (for output to terminal) Create a file handler (for output to a file) Set the severity level for the handlers if you want different levels

## Library Context

This script is part of the general automation library, providing utility functions for common automation tasks.

## Key Features

No specific features documented.

## Usage Pattern

Usage pattern not identified.

## Dependencies

- `logging`

## Function Descriptions

No function descriptions available.

## Functions

No functions defined in this script.

## Classes

No classes defined in this script.

## External APIs

No external API interactions identified.

## Code Examples

### Example Code

```python
import logging

# Create a logger object
logger = logging.getLogger("my_logger")

# Set the severity level (default is WARNING)
logger.setLevel(logging.DEBUG)

# Create a console handler (for output to terminal)
console_handler = logging.StreamHandler()

# Create a file handler (for output to a file
```

