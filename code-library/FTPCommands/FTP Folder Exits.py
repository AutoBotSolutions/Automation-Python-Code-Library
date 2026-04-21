## Me
python FTP Folder Exits

## AI Assistant
To check whether a folder exists on an FTP server using Python, you can use a library like `ftplib`. Here is an example of how you can verify if a folder exists:

### Example Code

```python
from ftplib import FTP, error_perm

def folder_exists(ftp, folder_name):
    """Check if a folder exists on the FTP server."""
    try:
        ftp.cwd(folder_name)  # Try to change to the directory
        ftp.cwd('..')  # Change back to the original directory
        return True
    except error_perm as e:
        # Directory doesn't exist or insufficient permissions
        if str(e).startswith("550"):  # 550 is a common FTP error for "No such file or directory"
            return False
        raise  # Re-raise any unexpected errors

# Usage
ftp = FTP('ftp.example.com')  # Replace with the actual FTP server
ftp.login('username', 'password')  # Provide FTP credentials

folder_name = 'path/to/folder'
if folder_exists(ftp, folder_name):
    print(f"The folder '{folder_name}' exists!")
else:
    print(f"The folder '{folder_name}' does not exist!")

ftp.quit()
```

### Explanation

1. **`ftp.cwd(folder_name)`**: Attempts to change to the given folder. If successful, it means the folder exists.
2. **`ftp.cwd('..')`**: Brings you back to the original directory after checking.
3. **Catch `error_perm` Exception**: If the folder does not exist or there is insufficient permission, the server may return a `550` error ("No such file or directory").
4. **Server-Side Permissions**: Make sure the FTP credentials have the proper read and directory access permissions.

Let me know if you need further assistance!

