## Me
python ftp get folders

## AI Assistant
To retrieve folders (or directories) from an FTP server in Python, you can use the `ftplib` module, which provides a simple way to interact with an FTP server. Here’s how you can approach this task:

---

### Steps to Get Folders from an FTP Server
1. **Establish a Connection**: Use `FTP` from the `ftplib` module to connect to the FTP server.
2. **Login**: Provide the username and password (or use anonymous login if supported).
3. **Navigate and List Files**: Use the `nlst()` or `dir()` method to get a list of files and directories.
4. **Check for Folders**: Since FTP treats directories and files as strings in some cases (depending on the server implementation), you can distinguish folders and files by parsing their properties.

---

### Example Code
Here’s an example that retrieves directories from an FTP server:

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
        # List all items in the directory
        ftp.cwd(path)
        entries = ftp.mlsd(path=path)  # Use MLSD to get detailed info about files/folders
        for name, info in entries:
            if info['type'] == 'dir':  # Check if the entry is a directory
                folders.append(name)
    except Exception as e:
        print(f"Error: {e}")
    return folders

# Connect to FTP server
ftp = FTP()
ftp.connect('ftp.example.com', 21)  # Replace with your server details
ftp.login('username', 'password')   # Replace with your credentials

# Get list of folders in the root directory
folders = list_folders(ftp, path="/")
print("Folders:", folders)

# Close the connection
ftp.quit()
```

---

### Explanation of the Code
1. **`ftp.mlsd()`**: This is a modern FTP command that provides detailed information about each file and folder (such as type, size, modified date). It’s used to distinguish directories from files.
2. **Error Handling**: If the FTP server doesn’t support `mlsd()`, you might need to fall back to `ftp.dir()` and manually parse the output.
3. **`ftp.cwd()`**: Changes the current directory on the server.

---

### Alternative Approach (if `mlsd()` is not available)
If the `mlsd()` method is not supported or unavailable, use this fallback approach:

```python
def is_folder(ftp, item):
    """
    Check if the given item is a folder by trying to change the directory.
    :param ftp: FTP connection object
    :param item: Item name
    :return: True if it's a folder, False otherwise
    """
    current = ftp.pwd()
    try:
        ftp.cwd(item)
        ftp.cwd(current)  # Change back to the original directory
        return True
    except:
        return False

def list_folders_fallback(ftp, path="."):
    """
    List folders using the fallback method (parsing errors).
    :param ftp: FTP connection object
    :param path: Path to list folders from
    :return: List of folder names
    """
    folders = []
    ftp.cwd(path)
    for item in ftp.nlst():  # Basic list
        if is_folder(ftp, item):
            folders.append(item)
    return folders
```

---

### Dependencies
- Python standard library (`ftplib`).
- Ensure network access to the FTP server.
- If the server has advanced authentication (e.g., SFTP), consider using libraries like `pysftp` or `paramiko` instead since `ftplib` only supports plain FTP.

Let me know if you need further clarification!

