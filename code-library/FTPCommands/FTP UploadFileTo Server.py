## Me
ftp upload file to server

## AI Assistant
To upload a file to an FTP server using Python, you can use the built-in `ftplib` module. Below is a simple example showing how to connect to an FTP server and upload a file:

### Code Example: FTP Upload
```python
from ftplib import FTP

def upload_file_to_ftp(host, username, password, file_path, remote_path):
    try:
        # Connect to the FTP server
        ftp = FTP(host)
        ftp.login(user=username, passwd=password)
        print(f"Connected to FTP server: {host}")
        
        # Open the file to be uploaded
        with open(file_path, 'rb') as file:
            # Upload the file to the specified remote path
            ftp.storbinary(f"STOR {remote_path}", file)
            print(f"File uploaded successfully to: {remote_path}")
        
        # Close the FTP connection
        ftp.quit()
        print("Connection closed.")
    except Exception as e:
        print(f"Failed to upload file: {e}")

# Usage
host = "ftp.example.com"  # Replace with your FTP server
username = "your-username"
password = "your-password"
file_path = "/path/to/local/file.txt"
remote_path = "server/directory/file.txt"

upload_file_to_ftp(host, username, password, file_path, remote_path)
```

### Explanation:
1. **FTP Connection**:
   - Use `FTP(host)` to connect to the server.
   - Login with `ftp.login(user=username, passwd=password)`.

2. **File Upload**:
   - Open the local file in binary read mode (`rb`).
   - Use the `storbinary()` method with the `STOR` command to upload the file to the desired location on the server.

3. **Closing the Connection**:
   - Always call `ftp.quit()` after completing the transfer to properly close the connection.

### Things to Note:
- Confirm the `host`, `username`, and `password` with your FTP server configuration.
- Ensure paths (`file_path` and `remote_path`) are correct.
- Make sure the user has the necessary write permissions on the specified server directory.

### Common Errors:
- `FTPError` for incorrect credentials or server issues.
- FileNotFoundError if the local file path is invalid.

If you require advanced file handling or need to work securely over SFTP, you can use libraries like `paramiko` instead of `ftplib`. Let me know if you need more details!

