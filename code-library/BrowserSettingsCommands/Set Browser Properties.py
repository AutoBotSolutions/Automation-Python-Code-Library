using selenium set browser properties

## Me
using selenium set browser properties

## AI Assistant
To set browser properties in Selenium, you need to configure `webdriver` options that allow you to customize your browser's properties or behavior. For example, you can set properties like the browser window size, user-agent, or even run the browser in headless mode.
Here's an example of how to set browser properties for two common browsers:
### For Chrome
``` python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create Options for Chrome browser
chrome_options = Options()

# Set browser properties
chrome_options.add_argument("--start-maximized")  # Start browser maximized
chrome_options.add_argument("--incognito")  # Open in incognito mode
chrome_options.add_argument("--disable-extensions")  # Disable browser extensions

# Set headless mode if needed
# chrome_options.add_argument("--headless")

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

# Perform your actions
driver.get("https://example.com")
```
### For Firefox
``` python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Create Options for Firefox browser
firefox_options = Options()

# Set browser properties
firefox_options.add_argument("--width=1920")  # Set width of the browser
firefox_options.add_argument("--height=1080")  # Set height of the browser
firefox_options.set_preference("browser.privatebrowsing.autostart", True)  # Open in private mode

# Set headless mode if needed
# firefox_options.add_argument("--headless")

# Initialize the WebDriver with options
driver = webdriver.Firefox(options=firefox_options)

# Perform your actions
driver.get("https://example.com")
```


