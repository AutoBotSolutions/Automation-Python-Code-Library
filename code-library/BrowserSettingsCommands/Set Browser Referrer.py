using selenium set browser referrer

## Me
using selenium set browser referrer

## AI Assistant
``` python
from selenium import webdriver

# Start the browser
driver = webdriver.Chrome()

# Navigate to a webpage with referer header
driver.get("https://example.com/some-path")  # Target URL
driver.execute_script("document.referrer = 'https://my-referer-site.com';")

driver.get("https://example.com")  # Load the URL with the updated Referer header
```
``` python
from selenium import webdriver

# Start the Chrome browser with options
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Enable CDP on the browser session
driver.execute_cdp_cmd(
    'Network.enable', {}
)

# Set the Referer Header
driver.execute_cdp_cmd(
    'Network.setExtraHTTPHeaders',
    {
        "headers": {
            "Referer": "https://your-referer-site.com"
        }
    }
```


