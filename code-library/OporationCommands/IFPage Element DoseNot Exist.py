Here’s how you can use an **if-else if** statement in Python 
using Selenium to check if a page element does not exist and 
handle cases accordingly:
#///////////////////////////////////////////////////////////#

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Initialize the Chrome driver (or another driver of your choice)
driver = webdriver.Chrome()

# Navigate to the desired URL
driver.get("https://example.com")


# Function to check if an element exists
def is_element_present(driver, by, value):
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False


# Example usage
if not is_element_present(driver, "id", "non_existent_element_id"):
    print("Element does not exist")
elif is_element_present(driver, "class name", "some_class_name"):
    print("Other element exists")
else:
    print("Default case: No matching conditions met")

# Close the driver when done
driver.quit()


#///////////////////////////////////////////////////////////#
### Explanation:
1. **`is_element_present()` function**: This checks for the 
presence of an element using the `find_element` method. If the 
element is not found, it catches the `NoSuchElementException` 
and returns `False`.

2. **`if-elif-else` conditions**:
    - The first `if` checks if a specific element is missing (`not is_element_present`).
    - The `elif` is an additional condition, checking for the presence of another element.
    - The `else` covers any remaining cases.

### Notes:
Replace `"id"`, `"non_existent_element_id"`, `"class name"`, and `"some_class_name"` 
with your specific attribute and value.
Use appropriate selectors such as `"id"`, `"class name"`, `"xpath"`, etc., based on your needs.
If you have any additional details to refine the code, feel free to share!

