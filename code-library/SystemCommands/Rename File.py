To rename a file in Python, you can use the built-in `os` module, which provides a method called `os.rename()`. Here's an example:

### Example Code:
```python
import os

# Current file name
old_file_name = "old_file_name.txt"

# New file name
new_file_name = "new_file_name.txt"

try:
    # Renaming the file
    os.rename(old_file_name, new_file_name)
    print(f"File renamed successfully from {old_file_name} to {new_file_name}")
except FileNotFoundError:
    print(f"The file '{old_file_name}' does not exist.")
except PermissionError:
    print("Permission denied. Unable to rename the file.")
except Exception as e:
    print(f"An error occurred: {e}")
```

### Explanation:
1. **`os.rename(src, dst)`**:
   - `src`: The current name (and path if needed) of the file.
   - `dst`: The new name (and path if needed) for the file.

2. **Error Handling**:
   - `FileNotFoundError`: The file does not exist.
   - `PermissionError`: Insufficient permissions to rename the file.
   - Catch all other unexpected exceptions with `except Exception`.

Let me know if you need more help!
