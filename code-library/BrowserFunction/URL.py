## Me
python using selenium get the current page URL and store it in var

## AI Assistant
Here’s how you can retrieve the current page URL using Selenium in Python and store it in a variable:

```python
from selenium import webdriver

# Initialize the WebDriver (e.g., using Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get("http://example.com")

# Get the current page URL
current_url = driver.current_url

# Print or use the URL
print(current_url)

# Close the browser
driver.quit()
```

### Explanation:
1. **`driver.get(url)`**: Navigates to the specified URL.
2. **`driver.current_url`**: Retrieves the URL of the currently loaded page in the browser.
3. **Store in `current_url`**: The URL is stored in the `current_url` variable.

Make sure that the Selenium WebDriver is properly set up (e.g., the appropriate driver like `chromedriver` is installed) and that the browser instance matches the WebDriver used.

