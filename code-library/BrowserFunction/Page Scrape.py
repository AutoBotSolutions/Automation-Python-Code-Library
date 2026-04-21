## Me
python using selenium get the current page scrape and store it in var

## AI Assistant
Here’s how you can scrape the contents of the current page using Selenium in Python and store it in a variable:

```python
from selenium import webdriver

# Example setup, replace 'your_driver_path' with the path to your driver
driver_path = 'your_driver_path'
driver = webdriver.Chrome(driver_path)

# Open a page
driver.get("https://example.com")

# Get the page source and store it in a variable
page_source = driver.page_source

# Print the content
print(page_source)

# Close the browser
driver.quit()
```

### Explanation:
1. **`driver.get("https://example.com")`**
   - This navigates to the specified URL.

2. **`driver.page_source`**
   - This gets the entire HTML content of the current page, storing it in the `page_source` variable.

3. **`driver.quit()`**
   - Always close the browser session when done to ensure no processes are left running.

You can manipulate or process the `page_source` variable for further scraping tasks, like parsing with libraries such as `BeautifulSoup` from the `bs4` module. Let me know if you need help with that!

