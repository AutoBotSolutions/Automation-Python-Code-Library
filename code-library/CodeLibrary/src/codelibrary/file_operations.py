"""
File system utilities.
"""

import os
import shutil
from pathlib import Path
from typing import List, Optional


def ensure_directory(path: str) -> None:
    """Ensure a directory exists, creating it if necessary."""
    Path(path).mkdir(parents=True, exist_ok=True)


def get_file_size(path: str) -> int:
    """Get the size of a file in bytes."""
    return os.path.getsize(path)


def get_file_extension(path: str) -> str:
    """Get the file extension from a path."""
    return Path(path).suffix.lower()


def list_files(directory: str, extension: Optional[str] = None) -> List[str]:
    """List all files in a directory, optionally filtered by extension."""
    path = Path(directory)
    if extension:
        return [str(f) for f in path.glob(f"*{extension}") if f.is_file()]
    return [str(f) for f in path.iterdir() if f.is_file()]


def list_directories(directory: str) -> List[str]:
    """List all subdirectories in a directory."""
    path = Path(directory)
    return [str(d) for d in path.iterdir() if d.is_dir()]


def is_empty_directory(path: str) -> bool:
    """Check if a directory is empty."""
    path = Path(path)
    return not any(path.iterdir())


def delete_directory(path: str) -> None:
    """Delete a directory and all its contents."""
    shutil.rmtree(path)


def copy_file(source: str, destination: str) -> None:
    """Copy a file from source to destination."""
    shutil.copy2(source, destination)


def move_file(source: str, destination: str) -> None:
    """Move a file from source to destination."""
    shutil.move(source, destination)


def read_file_lines(path: str, encoding: str = 'utf-8') -> List[str]:
    """Read a file and return its lines as a list."""
    with open(path, 'r', encoding=encoding) as f:
        return f.readlines()


def write_file_lines(path: str, lines: List[str], encoding: str = 'utf-8') -> None:
    """Write lines to a file."""
    ensure_directory(os.path.dirname(path))
    with open(path, 'w', encoding=encoding) as f:
        f.writelines(lines)


def get_absolute_path(path: str) -> str:
    """Get the absolute path from a relative or absolute path."""
    return str(Path(path).absolute())
