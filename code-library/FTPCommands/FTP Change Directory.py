## Me
ftp change directory

## AI Assistant
To change directories when using FTP, you'll typically use the `cd` or `cwd` command in the FTP client. Here is how you can change the directory using Python's `ftplib` module:

### Example: Changing Directory in FTP Using Python

```python
from ftplib import FTP

# Connect to the FTP server
ftp = FTP('ftp.example.com')  # Replace with the FTP server address
ftp.login(user='username', passwd='password')  # Replace with valid credentials

# Change directory on the FTP server
directory = '/path/to/target/directory'  # Replace with the desired directory path
ftp.cwd(directory)

print(f"Current directory: {ftp.pwd()}")  # Print current directory

# Close the FTP connection
ftp.quit()
```

### Explanation:
1. **`ftp.cwd(directory)`** - This is the function that changes the current directory on the FTP server to the one specified.
2. **`ftp.pwd()`** - This retrieves the current working directory on the FTP server, which is useful to confirm you've navigated correctly.
3. **Login details** - Replace values like `ftp.example.com`, `username`, and `password` with the actual server address and credentials.

If you face errors such as "directory does not exist," ensure that the directory path you're trying to navigate to already exists on the server. If you're unsure of the directory structure, you can use **`ftp.retrlines('LIST')`** to list the files and directories in the current location.

Let me know if you'd like further assistance!

