using selenium clear cookies

## Me
using selenium clear cookies

## AI Assistant
To clear cookies using Selenium in Python, you can use the following methods:

### Clearing All Cookies

To clear all cookies for the browser session:

```python
from selenium import webdriver

# Initialize the WebDriver (choose the browser you're automating)
driver = webdriver.Chrome()

# Open a website
driver.get("https://example.com")

# Clear all cookies
driver.delete_all_cookies()

# Optionally, verify cookies are cleared
print("Cookies after deletion:", driver.get_cookies())

# Close the browser
driver.quit()
```

### Deleting a Specific Cookie

To clear a specific cookie by its name:

```python
from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open a website
driver.get("https://example.com")

# Add a sample cookie for demonstration
driver.add_cookie({"name": "sample_cookie", "value": "sample_value"})

# Delete a specific cookie by its name
driver.delete_cookie("sample_cookie")

# Verify the specific cookie is deleted
print("Cookies after deleting 'sample_cookie':", driver.get_cookies())

# Close the browser
driver.quit()
```

### Notes:
1. **`delete_all_cookies()`** - Deletes all cookies for the current browser session.
2. **`delete_cookie('name')`** - Deletes a specific cookie by name.

You can run these snippets depending on whether you want to clear all cookies or just a specific one. Let me know if you have any additional questions!

