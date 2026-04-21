## Me
ftp download file

## AI Assistant
If you want to download a file using FTP in Python, you can use the built-in `ftplib` module. Below is a simple example of how to connect to an FTP server and download a file:
### Example Code
``` python
from ftplib import FTP

# FTP server details
ftp_server = "ftp.example.com"  # Replace with the FTP server's address
ftp_user = "your_username"  # Replace with your FTP username
ftp_password = "your_password"  # Replace with your FTP password
remote_file_path = "path/to/remote/file.txt"  # Path of the file on the server
local_file_path = "downloaded_file.txt"  # Local path to save the downloaded file

try:
    # Connect to the FTP server
    ftp = FTP(ftp_server)
    ftp.login(user=ftp_user, passwd=ftp_password)
    print(f"Connected to FTP server: {ftp_server}")

    # Open a file in write-binary mode to save the content
    with open(local_file_path, "wb") as local_file:
        # Retrieve the file and write its content to the local file
        ftp.retrbinary(f"RETR {remote_file_path}", local_file.write)

    print(f"File downloaded successfully to {local_file_path}")

    # Close the FTP connection
    ftp.quit()

except Exception as e:
    print(f"An error occurred: {e}")
```


