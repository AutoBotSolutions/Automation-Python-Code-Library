# 2captcha reCAPTCHA
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import random
import os

# Initialize variables
username = ""
password = ""
save_image_path = os.path.join(os.getenv('APPDATA'), "CaptchaImage.jpg")

# Initialize browser
browser = webdriver.Chrome()
browser.get("https://goo.gl")

# Wait for page to load
time.sleep(5)

# Click reCAPTCHA checkbox
recaptcha_checkbox = browser.find_element(By.CLASS_NAME, "recaptcha-checkbox-checkmark")
recaptcha_checkbox.click()

# Wait for challenge to load
time.sleep(5)

# Get banner text
banner_text_element = browser.find_element(By.CLASS_NAME, "rc-imageselect-desc-wrapper")
banner_text = banner_text_element.get_attribute("innerText").strip()

# Save CAPTCHA image
captcha_element = browser.find_element(By.CLASS_NAME, "rc-imageselect-target")
captcha_location = captcha_element.location
captcha_size = captcha_element.size
browser.save_screenshot(save_image_path)

# Crop CAPTCHA image
image = Image.open(save_image_path)
left = captcha_location['x']
top = captcha_location['y']
right = captcha_location['x'] + captcha_size['width']
bottom = captcha_location['y'] + captcha_size['height']
captcha_image = image.crop((left, top, right, bottom))
captcha_image = captcha_image.resize((300, 300))
captcha_image.save(save_image_path)

# Plugin function simulation (dummy response for captcha recognition)
raw_captcha = ["dummy_captcha_response"]

captcha_id = raw_captcha[0]
raw_captcha.pop(0)

# Simulate clicking tiles based on raw_captcha
for i in range(len(raw_captcha)):
    random_offset = random.choice(raw_captcha)
    tile = browser.find_element(By.CLASS_NAME, "rc-image-tile-target")
    ActionChains(browser).move_to_element_with_offset(tile, random.uniform(1, 10),
                                                      random.uniform(1, 10)).click().perform()
    time.sleep(random.uniform(1.1, 2.9))

# Click verify button
verify_button = browser.find_element(By.ID, "recaptcha-verify-button")
verify_button.click()
