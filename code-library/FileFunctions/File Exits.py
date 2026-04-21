## Me
python check if file exits

## AI Assistant
To check if a file exists in Python, you can use the `os` module or the `pathlib` module. Here's how you can do it:

### Using `os.path`:
```python
import os

file_path = "example.txt"

if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")
```

### Using `pathlib.Path` (Preferred for modern Python versions):
```python
from pathlib import Path

file_path = Path("example.txt")

if file_path.exists():
    print("File exists")
else:
    print("File does not exist")
```

Both approaches above check if the specified file (or directory) exists. To specifically check for files and exclude directories, you can use:

### Using `os.path.isfile`:
```python
if os.path.isfile(file_path):
    print("File exists and it is a file")
else:
    print("File does not exist, or it is not a file")
```

### Using `pathlib.Path.is_file`:
```python
if file_path.is_file():
    print("File exists and it is a file")
else:
    print("File does not exist, or it is not a file")
```

---

Let me know if you require further assistance!

