import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import requests

# Replace with your 2captcha API key
api_key = "XXXXXX"

# Start WebDriver
driver = webdriver.Chrome()
driver.get("https://goo.gl")

# Wait for page to load
time.sleep(5)

# Click the reCAPTCHA checkbox
checkbox = driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-checkmark")
checkbox.click()

# Wait for reCAPTCHA to load
time.sleep(5)

# Get banner text
banner_element = driver.find_element(By.CLASS_NAME, "rc-imageselect-desc-wrapper")
banner_text = banner_element.get_attribute("innerText").strip()

# Save image for CAPTCHA
save_image_path = "CaptchaImage.jpg"
captcha_target = driver.find_element(By.CLASS_NAME, "rc-imageselect-target")
captcha_target.screenshot(save_image_path)

# Count CAPTCHA tiles
tiles = driver.find_elements(By.CLASS_NAME, "rc-image-tile-33")
captcha_count = len(tiles)

# Resize the image based on the number of tiles
image = Image.open(save_image_path)
if captcha_count in [8, 9]:
    image = image.resize((300, 300))
else:
    image = image.resize((600, 600))
image.save(save_image_path)

# Send image to 2captcha for solving
with open(save_image_path, "rb") as file:
    response = requests.post(
        f"http://2captcha.com/in.php",
        files={"file": file},
        data={"key": api_key, "method": "post", "json": 1, "banner": banner_text}
    )
captcha_id = response.json().get("request")

# Wait for solution
solution = None
while True:
    result = requests.get(
        f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}&json=1"
    ).json()
    if result.get("status") == 1:
        solution = result.get("request").split("|")
        break
    time.sleep(5)

# Click on the solved CAPTCHA tiles
captcha_tiles = driver.find_elements(By.CLASS_NAME, "rc-image-tile-target")
actions = ActionChains(driver)
for index in map(int, solution):
    actions.move_to_element(captcha_tiles[index]).click().perform()
    time.sleep(1)

# Click verify button
verify_button = driver.find_element(By.ID, "recaptcha-verify-button")
verify_button.click()

# Cleanup
driver.quit()
