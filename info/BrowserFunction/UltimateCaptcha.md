# UltimateCaptcha.py

**Path:** `BrowserFunction/UltimateCaptcha.py`

**Lines:** 198
**Size:** 11020 bytes

## Description

Solves very basic CAPTCHAs. Allows manual solving for image-based CAPTCHAs and supports simple math and text-based CAPTCHAs.

## Imports

- `selenium.webdriver`
- `selenium.webdriver.common.by.By`
- `selenium.webdriver.common.action_chains.ActionChains`
- `selenium.webdriver.common.keys.Keys`
- `selenium.webdriver.support.ui.WebDriverWait`
- `selenium.webdriver.support.expected_conditions`
- `selenium.common.exceptions.NoSuchElementException`
- `selenium.common.exceptions.TimeoutException`
- `time`
- `base64`
- `PIL.Image`
- `io`
- `re`

## Classes

### SimpleCaptchaSolver

Solves very basic CAPTCHAs. Allows manual solving for image-based CAPTCHAs and supports simple math and text-based CAPTCHAs.

**Methods:**
- `__init__`
- `solve_captcha`
- `_get_captcha_question`
- `_process_question`
- `_enter_answer`
- `_submit_form`
- `_solve_image_captcha`

## Functions

### main

### __init__

**Parameters:** self, driver, captcha_question_locator, captcha_answer_locator, submit_button_locator, wait_timeout

Initializes the CaptchaSolver.

Args:
    driver: Selenium WebDriver instance.
    captcha_question_locator (tuple): Locator for text-based captcha question element.
    captcha_answer_locator (tuple): Locator for the captcha answer input field.
    submit_button_locator (tuple): Locator for the submit button.
    wait_timeout (int): Timeout in seconds for waiting for elements.

### solve_captcha

**Parameters:** self

Attempts to solve the CAPTCHA.
Handles text-based, math-based, and image-based CAPTCHAs.

### _get_captcha_question

**Parameters:** self

Retrieves the captcha question text.

### _process_question

**Parameters:** self, question_text

Processes the captcha question and returns the answer.

### _enter_answer

**Parameters:** self, answer

Enters the answer into the captcha input field.

### _submit_form

**Parameters:** self

Submits the form.

### _solve_image_captcha

**Parameters:** self

Handles image-based CAPTCHA manually.

