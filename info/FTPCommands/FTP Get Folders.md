# FTP Get Folders.py

**Path:** `FTPCommands/FTP Get Folders.py`

**Automation Type:** General Automation
**Lines:** 106

## Purpose

python ftp get folders

## Library Context

This script is part of the general automation library, providing utility functions for common automation tasks.

## Key Features

No specific features documented.

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `ftplib`
- `FTP`

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
from ftplib import FTP

def list_folders(ftp, path="."):
    """
    List folders in the given path on the FTP server.
    :param ftp: FTP connection object
    :param path: Path to list folders from
    :return: List of folder names
    """
    folders = []
    try:
        # List all items in the 
```

