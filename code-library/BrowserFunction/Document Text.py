## Me
python using selenium get the current page document text and store it in var

## AI Assistant
To grab the current page's document text using Selenium in Python and store it in a variable, you can utilize the `execute_script` method to access the document object in the DOM.

Here's an example code snippet for achieving this:

```python
from selenium import webdriver

# Initialize the Selenium WebDriver (e.g., Chrome)
driver = webdriver.Chrome()  # Or use a different driver like Firefox, Edge, etc.

# Navigate to a webpage
driver.get('https://example.com')

# Get the current page's document text
page_text = driver.execute_script("return document.documentElement.innerText")

# Print or use the text
print(page_text)

# Close the browser
driver.quit()
```

### Explanation:
1. **`driver.execute_script`**: Executes JavaScript code in the context of the currently loaded page.  
   - `"return document.documentElement.innerText"` gets the textual content of the entire page (visible content).
   - Alternatively, `"return document.body.textContent"` can be used to return all text content (including hidden or structured).

2. **`page_text`**: Stores the captured text.

This will store the visible text of the current page in the `page_text` variable. Adjust the selector or JavaScript code if you need more specific elements.

