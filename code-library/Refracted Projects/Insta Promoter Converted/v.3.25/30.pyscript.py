# Reset BITS transfers (optional, only if necessary)
Get-BitsTransfer | Remove-BitsTransfer

# Set download path dynamically
$DownloadPath = [Environment]::GetFolderPath("Desktop")

# URL of the file to download
$Url = "https://softwareautomation.org/home/software/Insta-Promoter.zip"

# Destination file path
$Destination = Join-Path -Path $DownloadPath -ChildPath "Insta-Promoter.zip"

# Start downloading the file using BITS
Start-BitsTransfer -Source $Url -Destination $Destination -DisplayName "Server Transfer"
bitsadmin /reset
set DownloadPath=%USERPROFILE%\Desktop
bitsadmin.exe /transfer "Server Transfer" https://softwareautomation.org/home/software/Insta-Promoter.zip %DownloadPath%\Insta-Promoter.zip

##############################################################33


import os
import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests


# Function to set up download path
def get_default_download_path():
    """
    Returns the desktop path as the default download path.
    """
    return os.path.join(os.path.expanduser("~"), "Desktop")


def download_file(url, download_path):
    """
    Downloads a file from the given URL to the specified download path.

    :param url: The URL of the file to download.
    :param download_path: The path where the file should be saved.
    """
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(download_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            messagebox.showinfo("Download Complete", f"The file has been downloaded to: {download_path}")
        else:
            messagebox.showerror("Download Error", f"Failed to download the file. Status Code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while downloading: {e}")


# Function to automate browser tasks using Selenium
def start_browser_automation():
    """
    Automates browser tasks using Selenium, such as visiting a website and interacting with it.
    """
    try:
        # Set up Chrome WebDriver
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)

        # Open the website
        driver.get("https://softwareautomation.org/home/software/")

        # Add custom web automation tasks here as needed
        # Example: Wait for 5 seconds to simulate an action
        time.sleep(5)

        # Close the browser
        driver.quit()
        messagebox.showinfo("Automation Complete", "Browser automation completed successfully.")
    except Exception as e:
        messagebox.showerror("Automation Error", f"An error occurred during browser automation: {e}")


# Function to handle the file download and browser automation
def handle_download_and_automation():
    """
    Handles downloading the file and automating browser tasks.
    """
    # Prompt the user to select a save location for the file
    save_path = filedialog.asksaveasfilename(
        initialdir=get_default_download_path(),
        defaultextension=".zip",
        filetypes=[("ZIP files", "*.zip"), ("All files", "*.*")]
    )
    if save_path:
        # Download the file
        download_url = "https://softwareautomation.org/home/software/Insta-Promoter.zip"
        download_file(download_url, save_path)

        # Start browser automation after download
        start_browser_automation()


# Set up the UI using Tkinter
def main():
    """
    Main function to create the Tkinter interface.
    """
    app = tk.Tk()
    app.title("Insta-Promoter Tool")
    app.geometry("400x200")

    # Label
    label = tk.Label(app, text="Welcome to Insta-Promoter Tool!", font=("Arial", 14))
    label.pack(pady=10)

    # Download Button
    download_button = tk.Button(app, text="Download and Automate", command=handle_download_and_automation,
                                font=("Arial", 12))
    download_button.pack(pady=10)

    # Exit Button
    exit_button = tk.Button(app, text="Exit", command=app.quit, font=("Arial", 12))
    exit_button.pack(pady=10)

    # Run the Tkinter loop
    app.mainloop()


if __name__ == "__main__":
    main()
