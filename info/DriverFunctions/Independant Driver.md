# Independant Driver.py

**Path:** `DriverFunctions/Independant Driver.py`

**Automation Type:** Browser Automation
**Lines:** 579

## Purpose

can you code an independent drive like selenium

## Library Context

This script is part of the browser automation library, providing functions for controlling web browsers, navigating to URLs, interacting with web elements, and automating web-based tasks.

## Key Features

- Web browser control

## Usage Pattern

Object-oriented - Provides classes and methods with standalone execution capability

## Dependencies

No external dependencies identified.

## Function Descriptions

- __init__ - Parameters: self, headless. Performs a specific operation.
- open_page - Parameters: self, url. Performs a specific operation.
- get_element - Parameters: self, selector. Performs a specific operation.
- click - Parameters: self, selector. Performs a specific operation.
- get_text - Parameters: self, selector. Performs a specific operation.

## Functions

No functions defined in this script.

## Classes

No classes defined in this script.

## External APIs

This script interacts with external services:
- `https://example.com")`
- `https://chromedevtools.github.io/devtools-protocol/)`
- `https://example.com")`
- `http://proxy:3128`

## Code Examples

### __init__

```python
def __init__(self, headless=True):
        self.browser = None
        self.page = None
        self.headless = headless
```

### open_page

```python
def open_page(self, url: str):
        """Opens a new page with the specified URL."""
        self.page = self.context.new_page()
        self.page.goto(url)
        print(f"Page opened: {url}")
```

### get_element

```python
def get_element(self, selector: str):
        """Gets a DOM element using a CSS selector."""
        element = self.page.query_selector(selector)
        if element:
            return element
        else:
            raise ValueError(f"Element not found for selector: {selector}")
```

### click

```python
def click(self, selector: str):
        """Clicks an element specified by the CSS selector."""
        element = self.get_element(selector)
        element.click()
        print(f"Clicked element with selector: {selector}")
```

### get_text

```python
def get_text(self, selector: str):
        """Gets the text content of an element."""
        element = self.get_element(selector)
        return element.text_content()
```

