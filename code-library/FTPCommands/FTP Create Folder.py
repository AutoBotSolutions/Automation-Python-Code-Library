## Me
ftp create folder on server

## AI Assistant
To create a folder on an FTP server using Python, you can utilize the `ftplib` library, which provides tools to interact with an FTP server. Here's an example of how you can connect to an FTP server, navigate to a specific location, and create a new folder (directory):

### Example Code

```python
from ftplib import FTP

# FTP server credentials
ftp_server = "example.com"  # Replace with your FTP server address
ftp_user = "your_username"  # Replace with your FTP username
ftp_password = "your_password"  # Replace with your FTP password

# Name of the directory to create
directory_to_create = "new_folder"

# Connect to the FTP server
ftp = FTP(ftp_server)
ftp.login(user=ftp_user, passwd=ftp_password)

try:
    # Create a new directory on the server
    ftp.mkd(directory_to_create)
    print(f"Directory '{directory_to_create}' created successfully.")
except Exception as e:
    print(f"Error creating directory: {e}")

# Quit and close the FTP connection
ftp.quit()
```

### Explanation of the Code
1. **Connect to FTP server**: Use `FTP(ftp_server)` to connect and `ftp.login()` to log in with your credentials.
2. **Create Directory**: Use `ftp.mkd(directory_name)` to create a folder in the current directory on the FTP server.
3. **Error Handling**: Wrap the operation in a `try-except` block to handle any errors (e.g., if the directory already exists).
4. **Disconnect**: Use `ftp.quit()` to terminate the connection after the operation is complete.

### Things to Ensure
- Replace placeholders like `ftp_server`, `ftp_user`, and `ftp_password` with actual valid credentials.
- Ensure you have the necessary permissions on the FTP server to create directories.
- If targeting a specific directory path for creation (e.g., `/parent/new_folder`), ensure its parent directory exists.

Let me know if you need further clarification!

