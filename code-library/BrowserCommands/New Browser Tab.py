## Me
using selenium new browser tab

## AI Assistant
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Launch the browser
driver = webdriver.Chrome()  # Replace with the driver you are using (e.g., Firefox, Edge)

# Open a webpage
driver.get("https://www.example.com")

# Open a new tab
driver.execute_script("window.open('');")  # Opens a new blank tab

# Switch to the newly opened tab
driver.switch_to.window(driver.window_handles[1])

# Navigate to a new URL in the new tab
driver.get("https://www.google.com")

# Close the new tab
driver.close()

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])

# Close the original browser window
driver.quit()


