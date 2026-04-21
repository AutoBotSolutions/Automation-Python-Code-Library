## Me
python using selenium get element parent and store it in var

## AI Assistant
Here's an example of how to get an element's parent using Selenium in Python and store it in a variable:

### Code Example
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open a webpage
    driver.get("https://example.com")

    # Locate a child element
    child_element = driver.find_element(By.ID, "child-element-id")

    # Get the parent element using XPath
    parent_element = child_element.find_element(By.XPATH, "./..")

    # You can now work with the parent_element
    print("Parent tag name:", parent_element.tag_name)
finally:
    # Close the driver
    driver.quit()
```

### Explanation:
1. **Locating the Parent**:
   - Each element in Selenium can be navigated relative to its position in the DOM.
   - The `XPath` expression `./..` selects the parent of the current node.

2. **Storing the Parent**:
   - The result of `find_element` is stored in the `parent_element` variable.

3. **Using the Parent**:
   - You can then interact with the parent element as needed, such as retrieving its tag name, text, attributes, or interacting with it.

Let me know if you need anything further!

