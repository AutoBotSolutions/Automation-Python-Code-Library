from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import base64
from PIL import Image
import io

# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
driver.maximize_window()

# Replace with the URL of the website containing the CAPTCHA
website_url = 'https://example-captcha-website.com'  # *** REPLACE WITH ACTUAL URL ***
driver.get(website_url)

try:
    # Wait for the CAPTCHA image to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'captchaImage'))  # *** REPLACE 'captchaImage' with actual ID ***
    )

    # Locate the CAPTCHA image element
    captcha_element = driver.find_element(By.ID, 'captchaImage')  # *** REPLACE 'captchaImage' with actual ID ***
    captcha_src = captcha_element.get_attribute('src')

    image_data = None

    if captcha_src.startswith('data:image'):
        image_type, image_base64_string = captcha_src.split(',')
        image_data = base64.b64decode(image_base64_string)
    else:
        print("CAPTCHA image is not base64 encoded. Handling external URLs can be added if needed.")

    if image_data:
        # Save and display the CAPTCHA image
        image = Image.open(io.BytesIO(image_data))
        image.save("captcha.png")  # Save the image locally (optional)
        image.show()  # Open the image in the default viewer

        # Prompt user to manually solve the CAPTCHA
        solved_captcha_text = input("Please solve the CAPTCHA shown in 'captcha.png' and enter the text: ")

        # Wait for the CAPTCHA input field to load
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'captchaInput'))  # *** REPLACE 'captchaInput' with actual ID ***
        )

        # Enter the solved CAPTCHA text
        captcha_input_field = driver.find_element(By.ID,
                                                  'captchaInput')  # *** REPLACE 'captchaInput' with actual ID ***
        captcha_input_field.clear()
        captcha_input_field.send_keys(solved_captcha_text)

        # Wait for the submit button to be clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'submitButton'))  # *** REPLACE 'submitButton' with actual ID ***
        )

        # Submit the form
        submit_button = driver.find_element(By.ID, 'submitButton')  # *** REPLACE 'submitButton' with actual ID ***
        submit_button.click()

        print("CAPTCHA text entered and form submitted. Check the website for results.")
        time.sleep(5)  # Wait to observe the result

    else:
        print("Could not retrieve CAPTCHA image data.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()

