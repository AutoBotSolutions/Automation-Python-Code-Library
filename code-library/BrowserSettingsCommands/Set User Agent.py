using selenium set user agent

## Me
using selenium set user agent

## AI Assistant
To set a custom **User-Agent** using Selenium, you can configure it during the initialization of the WebDriver. Here's an example for Google Chrome and Firefox:

---

### Example for Chrome:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("user-agent=Your_Custom_User_Agent_String")

# Initialize the WebDriver with the options
driver = webdriver.Chrome(options=chrome_options)

# Example usage
driver.get("https://www.whatismybrowser.com/")  # Check user agent
```

---

### Example for Firefox:

```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Set up Firefox options
firefox_options = Options()
firefox_options.set_preference("general.useragent.override", "Your_Custom_User_Agent_String")

# Initialize the WebDriver with the options
driver = webdriver.Firefox(options=firefox_options)

# Example usage
driver.get("https://www.whatismybrowser.com/")  # Check user agent
```

---

### Explanation:
1. Replace `"Your_Custom_User_Agent_String"` with the desired User-Agent string.
2. You can use [https://www.whatismybrowser.com/](https://www.whatismybrowser.com/) to verify whether the desired User-Agent is applied.

Let me know if you need further clarifications!

