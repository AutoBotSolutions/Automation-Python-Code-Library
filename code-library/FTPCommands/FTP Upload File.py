## Me
FTP upload file

## AI Assistant
To upload a file using FTP in Python, you can use the built-in **`ftplib`** library. Below is an example of how you can implement FTP file uploads:

```python
import ftplib

def upload_file_to_ftp(server, username, password, file_path, remote_path):
    try:
        # Establish connection to the FTP server
        with ftplib.FTP(server) as ftp:
            ftp.login(user=username, passwd=password)
            print("Connected to FTP server")

            # Open the local file in binary-read mode
            with open(file_path, 'rb') as file:
                # Upload the file to the desired remote path
                ftp.storbinary(f'STOR {remote_path}', file)
                print(f"File uploaded successfully to {remote_path}")
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

# Example usage:
# Replace 'ftp.example.com', 'username', 'password', 'local_file_path', and 'remote_file_path'
upload_file_to_ftp(
    server='ftp.example.com',
    username='your_username', 
    password='your_password', 
    file_path='/path/to/your/local_file.txt', 
    remote_path='remote/path/on/server.txt'
)
```

### Code Explanation:
1. Import the `ftplib` library.
2. Use the **`FTP`** object to establish a connection with the FTP server.
3. Log in with credentials (`username` and `password`).
4. Open the local file in binary mode using `open(file_path, 'rb')`.
5. Use the **`storbinary`** method to upload the file to the desired remote location.
6. Handle exceptions with **`ftplib.all_errors`** to catch any FTP-related errors.

### Placeholders to Replace:
- `ftp.example.com` → The domain or IP of your FTP server.
- `your_username` → The username for your FTP server.
- `your_password` → The corresponding password.
- `/path/to/your/local_file.txt` → The full path of the file you want to upload.
- `remote/path/on/server.txt` → The file's destination path on the server.

Let me know if you need clarification or help with modifying the code!

