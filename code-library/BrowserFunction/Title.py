## Me
python using selenium get the current page title and store it in var

## AI Assistant
Here’s how to use Selenium in Python to get the title of the current webpage and store it in a variable:

```python
from selenium import webdriver

# Example using Chrome
driver = webdriver.Chrome()

# Open a website
driver.get("https://example.com")

# Get the title of the current page
page_title = driver.title

# Store it in a variable and print it
print("The title of the page is:", page_title)

# Close the browser
driver.quit()
```

Make sure to replace `webdriver.Chrome()` with the appropriate driver for your browser, such as `webdriver.Firefox()` or `webdriver.Edge()`, and ensure you have the correct WebDriver installed.

### Breakdown:
- `driver.get("URL")`: Opens the specified URL.
- `driver.title`: Retrieves the title of the current page.
- `print`: Outputs the title for verification (optional).
- `driver.quit()`: Closes the browser after use to free resources.

