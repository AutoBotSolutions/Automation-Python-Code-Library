# auto_browser_cookie_keeper_proxy_useragent_set.v.1.0.py

**Path:** `ProxyFunction/auto_browser_cookie_keeper_proxy_useragent_set.v.1.0.py`

**Lines:** 161
**Size:** 6985 bytes

## Description

Configure logging

## Imports

- `logging`
- `os`
- `json`
- `time`
- `selenium.webdriver`
- `selenium.webdriver.chrome.options.Options`
- `selenium.webdriver.chrome.service.Service`
- `selenium.common.exceptions.TimeoutException`
- `selenium.common.exceptions.WebDriverException`

## Functions

### save_cookies

**Parameters:** driver, file_path

Save browser cookies to a file.

### load_cookies

**Parameters:** driver, file_path

Load browser cookies from a file.

### lanuch_initialize_driver

Initialize and return the Selenium WebDriver for Chromium.

### test_proxy_with_driver

**Parameters:** proxy, driver_path

Test a proxy using Selenium WebDriver.

