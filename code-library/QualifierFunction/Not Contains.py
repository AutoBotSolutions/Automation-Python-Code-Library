## Me
python set a variable called 'not_contains' set the value to '10' now using a qualifier function set the condition to search a page for the number 10, if the page dose not contain the number 10 then set the variable 'not_contains' to true and if it dose contain the number 10 set it to false

## AI Assistant
To achieve the behavior you’re describing in Python, you can define a function that accepts the page content as an input and sets the variable `not_contains` based on whether the content includes the value `10`. Here's an example implementation for your request:

```python
not_contains = 10  # Initialize the variable with the value 10

def check_page_content(page_content):
    global not_contains  # Declare it as global to modify the variable outside the function
    if '10' not in page_content:
        not_contains = True  # Set to True if "10" is not found
    else:
        not_contains = False  # Set to False if "10" is found

# Example usage:
page = "This sample page does not contain the number."
check_page_content(page)
print(not_contains)  # Will print: True

page_with_10 = "This is a sample page containing the number 10."
check_page_content(page_with_10)
print(not_contains)  # Will print: False
```

### Explanation:
1. The function `check_page_content` takes the `page_content` (e.g., the content of a webpage or text).
2. It checks if the string `'10'` is present in the content using the `not in` operator.
3. Depending on the condition, the function sets `not_contains` to `True` if `'10'` is missing or `False` if it is present.

Let me know if you have further concerns!

