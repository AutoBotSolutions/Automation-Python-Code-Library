## Me
ftp rename file

## AI Assistant
To rename a file on an FTP server using Python, the `ftplib` library's `rename` method is helpful. Here's an example of how to do it:

```python
from ftplib import FTP

# Connect to the FTP server
ftp = FTP('ftp.example.com')
ftp.login('username', 'password')

# Rename the file
old_name = 'old_filename.txt'
new_name = 'new_filename.txt'

try:
    ftp.rename(old_name, new_name)
    print(f"File renamed from {old_name} to {new_name}")
except Exception as e:
    print(f"Error renaming file: {e}")

# Close the connection
ftp.quit()
```

### Explanation:

1. **Connect and Authenticate**:
   Use `FTP('ftp.example.com')` to connect to the FTP server and login with a username and password.

2. **Rename File**:
   Use `ftp.rename(<old_name>, <new_name>)` to rename the file on the server.

3. **Error Handling**:
   Wrap operations in a `try` block to manage errors, such as a missing file or permission issues.

4. **Close Connection**:
   Call `ftp.quit()` when done, to close the connection.

### Notes:
- Replace `'ftp.example.com'`, `'username'`, and `'password'` with the actual FTP server details.
- Ensure you have appropriate permissions on the FTP server for renaming files.

Let me know if you need further clarification!

