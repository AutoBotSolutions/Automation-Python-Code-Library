# Delete Folder.py

**Path:** `SystemCommands/Delete Folder.py`

**Automation Type:** General Automation
**Lines:** 39

## Purpose

using python delete folder

## Library Context

This script is part of the general automation library, providing utility functions for common automation tasks.

## Key Features

No specific features documented.

## Usage Pattern

Usage pattern not identified.

## Dependencies

- `os`

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
import os

folder_path = "path/to/your/folder"

try:
    os.rmdir(folder_path)  # This will only work if the folder is empty
    print(f"Folder '{folder_path}' deleted successfully.")
except OSError as e:
    print(f"Error: {e.strerror}")
```

