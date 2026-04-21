using selenium set website credentials

## Me
using selenium set website credentials

## AI Assistant
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver (choose your browser driver, e.g., Chrome, Firefox)
driver = webdriver.Chrome()  # Make sure the `chromedriver` is in your PATH!

# Navigate to the website
url = "https://example.com/login"
driver.get(url)

# Locate the username and password input fields
username_field = driver.find_element(By.ID, "username-id")  # Replace with the actual ID or locator
password_field = driver.find_element(By.ID, "password-id")  # Replace with the actual ID or locator

# Enter credentials
username = "your-username"
password = "your-password"
username_field.send_keys(username)
password_field.send_keys(password)

# Press the login button
login_button = driver.find_element(By.ID, "login-button-id")  # Replace with the actual ID or locator
login_button.click()

# Optional: Wait for the next page to load, verify successful login, etc.


