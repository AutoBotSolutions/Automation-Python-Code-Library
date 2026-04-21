# file_operations.py

**Path:** `CodeLibrary/src/codelibrary/file_operations.py`

**Lines:** 76
**Size:** 2176 bytes

## Description

File system utilities.

## Imports

- `os`
- `shutil`
- `pathlib.Path`
- `typing.List`
- `typing.Optional`

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

### write_file_lines

**Parameters:** path, lines, encoding

Write lines to a file.

### get_absolute_path

**Parameters:** path

Get the absolute path from a relative or absolute path.

