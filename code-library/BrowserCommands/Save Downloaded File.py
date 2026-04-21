## Me
using selenium save downloaded file

## AI Assistant
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Specify the download directory
download_dir = "/path/to/download/directory"

# Chrome Options to handle downloads
chrome_options = Options()
prefs = {
    "download.default_directory": download_dir,  # Set default download path
    "download.prompt_for_download": False,  # Disable download prompt
    "download.directory_upgrade": True,  # Allows download directory updates without prompting
    "safebrowsing.enabled": True  # Enable safe browsing feature
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the WebDriver
service = Service("/path/to/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open a website
    driver.get("https://example.com/a_download_link")

    # Example: Find and click the download link/button
    download_button = driver.find_element(By.ID, "download-id")
    download_button.click()

    # Wait for the file to be downloaded - Adjust this wait time as per file size
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()


