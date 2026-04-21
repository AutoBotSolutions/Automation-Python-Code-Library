# Change Proxy.py

**Path:** `BrowserSettingsCommands/Change Proxy.py`

**Automation Type:** Browser Automation
**Lines:** 53

## Purpose

Define your proxy settings Setup Proxy Add the proxy to Chrome options Start Chrome WebDriver with Proxy

## Library Context

This script is part of the browser automation library, providing functions for controlling web browsers, navigating to URLs, interacting with web elements, and automating web-based tasks.

## Key Features

- Web browser control

## Usage Pattern

Usage pattern not identified.

## Dependencies

- `Proxy`
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
- `http://www.example.com")`

## Code Examples

### Example Code

```python
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Define your proxy settings
my_proxy = "123.45.67.89:8080"

# Setup Proxy
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = my_proxy
proxy.ssl_proxy = my_proxy

# Add the proxy to Chrom
```

