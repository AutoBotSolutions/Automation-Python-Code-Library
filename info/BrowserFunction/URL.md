# URL.py

**Path:** `BrowserFunction/URL.py`

**Automation Type:** Browser Automation
**Lines:** 32

## Purpose

python using selenium get the current page URL and store it in var

## Library Context

This script is part of the browser automation library, providing functions for controlling web browsers, navigating to URLs, interacting with web elements, and automating web-based tasks.

## Key Features

- Web browser control

## Usage Pattern

Usage pattern not identified.

## Dependencies

- `webdriver`
- `selenium`

## Function Descriptions

No function descriptions available.

## Functions

No functions defined in this script.

## Classes

No classes defined in this script.

## External APIs

This script interacts with external services:
- `http://example.com")`

## Code Examples

### Example Code

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

