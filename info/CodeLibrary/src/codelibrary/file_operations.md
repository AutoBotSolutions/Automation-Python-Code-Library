# file_operations.py

**Path:** `CodeLibrary/src/codelibrary/file_operations.py`

**Automation Type:** File Operations
**Lines:** 76

## Purpose

File system utilities.

## Library Context

This script is part of the file operations library, providing functions for file system manipulation including creating, reading, writing, and deleting files and directories.

## Key Features

- File system manipulation

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `os`
- `shutil`
- `pathlib.Path`
- `typing.List`
- `typing.Optional`

## Function Descriptions

- ensure_directory - Parameters: path. Performs a specific operation.
- get_file_size - Parameters: path. Performs a specific operation.
- get_file_extension - Parameters: path. Performs a specific operation.
- list_files - Parameters: directory, extension. Performs a specific operation.
- list_directories - Parameters: directory. Performs a specific operation.

## Functions

### ensure_directory

**Parameters:** path

Ensure a directory exists, creating it if necessary.

### get_file_size

**Parameters:** path

Get the size of a file in bytes.

### get_file_extension

**Parameters:** path

Get the file extension from a path.

### list_files

**Parameters:** directory, extension

List all files in a directory, optionally filtered by extension.

### list_directories

**Parameters:** directory

List all subdirectories in a directory.

### is_empty_directory

**Parameters:** path

Check if a directory is empty.

### delete_directory

**Parameters:** path

Delete a directory and all its contents.

### copy_file

**Parameters:** source, destination

Copy a file from source to destination.

### move_file

**Parameters:** source, destination

Move a file from source to destination.

### read_file_lines

**Parameters:** path, encoding

Read a file and return its lines as a list.

... and 2 more functions

## Code Examples

### ensure_directory

```python
def ensure_directory(path: str) -> None:
    """Ensure a directory exists, creating it if necessary."""
    Path(path).mkdir(parents=True, exist_ok=True)
```

### get_file_size

```python
def get_file_size(path: str) -> int:
    """Get the size of a file in bytes."""
    return os.path.getsize(path)
```

### get_file_extension

```python
def get_file_extension(path: str) -> str:
    """Get the file extension from a path."""
    return Path(path).suffix.lower()
```

### list_files

```python
def list_files(directory: str, extension: Optional[str] = None) -> List[str]:
    """List all files in a directory, optionally filtered by extension."""
    path = Path(directory)
    if extension:
        return [str(f) for f in path.glob(f"*{extension}") if f.is_file()]
    return [str(f) for f in
```

### list_directories

```python
def list_directories(directory: str) -> List[str]:
    """List all subdirectories in a directory."""
    path = Path(directory)
    return [str(d) for d in path.iterdir() if d.is_dir()]
```

