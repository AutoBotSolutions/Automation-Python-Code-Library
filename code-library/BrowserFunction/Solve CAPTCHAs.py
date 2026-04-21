from selenium import webdriver  # Import the Selenium WebDriver for browser automation
from selenium.webdriver.common.by import By  # Import locator strategy definitions for Selenium
from selenium.webdriver.common.action_chains import ActionChains  # Import for simulating complex user interactions
from selenium.webdriver.common.keys import Keys  # Import for simulating keyboard events in Selenium
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for waiting on elements
from selenium.webdriver.support import expected_conditions as EC  # Import expected conditions for element checks
from selenium.common.exceptions import NoSuchElementException, TimeoutException  # Import exceptions for error handling
import time  # Import for adding delays where needed
import base64  # Import for decoding base64 encoded image data
from PIL import Image  # Import for manipulating and displaying image data
import io  # Import for handling in-memory byte streams
import re  # Import for using regular expressions


class SimpleCaptchaSolver:
    """
    Solves very basic CAPTCHAs. Allows manual solving for image-based CAPTCHAs and supports simple math and text-based CAPTCHAs.
    """

    def __init__(self, driver, captcha_question_locator=None, captcha_answer_locator=None, submit_button_locator=None,
                 wait_timeout=10):
        """
        Initializes the CaptchaSolver.

        Args:
            driver: Selenium WebDriver instance.
            captcha_question_locator (tuple): Locator for text-based captcha question element.
            captcha_answer_locator (tuple): Locator for the captcha answer input field.
            submit_button_locator (tuple): Locator for the submit button.
            wait_timeout (int): Timeout in seconds for waiting for elements.
        """
        self.driver = driver  # Assign WebDriver instance to the class
        self.captcha_question_locator = captcha_question_locator  # Set locator to identify the captcha question element
        self.captcha_answer_locator = captcha_answer_locator  # Set locator for the captcha input field
        self.submit_button_locator = submit_button_locator  # Set locator for the form's submit button
        self.wait_timeout = wait_timeout  # Set the timeout duration for element waits

    def solve_captcha(self):
        """
        Attempts to solve the CAPTCHA.
        Handles text-based, math-based, and image-based CAPTCHAs.
        """
        try:
            if self.captcha_question_locator:  # Check if a locator for text-based CAPTCHAs is provided
                # Handle text-based or math-based CAPTCHA
                question = self._get_captcha_question()  # Retrieve the captcha question text
                answer = self._process_question(question)  # Process the question to generate an answer

                if answer is not None:  # Ensure that a valid answer was generated
                    self._enter_answer(answer)  # Enter the answer into the captcha input field
                    self._submit_form()  # Submit the form
                    return True  # Return True to indicate successful captcha solving

            else:
                # Handle image-based CAPTCHA
                self._solve_image_captcha()  # Solve image-based captcha manually
                return True  # Return True to indicate successful captcha solving

        # Handle possible exceptions during the process and log appropriate messages
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Element not found or timeout: {e}")  # Log error for element not found or timeout
            return False  # Return False to indicate failure
        except ValueError as e:
            print(f"Error processing captcha: {e}")  # Log error for invalid captcha processing
            return False  # Return False to indicate failure
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # Log any unexpected error
            return False  # Return False to indicate failure

    def _get_captcha_question(self):
        """Retrieves the captcha question text."""
        element = WebDriverWait(self.driver, self.wait_timeout).until(  # Wait for the presence of the question element
            EC.presence_of_element_located(self.captcha_question_locator)
            # Wait condition for question element presence
        )
        return element.text  # Return the text content of the question element

    def _process_question(self, question_text):
        """Processes the captcha question and returns the answer."""
        question_text = question_text.strip()  # Strip leading/trailing whitespace from the question text

        # Handle math-based CAPTCHAs with addition
        if "+" in question_text:
            try:
                num1, num2 = map(int, re.findall(r'\d+', question_text))  # Extract numbers from the text
                return str(num1 + num2)  # Return the sum as a string
            except ValueError:
                print(f"Invalid math captcha format: {question_text}")  # Log error for invalid math captcha format
                return None

        # Handle math-based CAPTCHAs with subtraction
        elif "-" in question_text:
            try:
                num1, num2 = map(int, re.findall(r'\d+', question_text))  # Extract numbers from the text
                return str(num1 - num2)  # Return the difference as a string
            except ValueError:
                print(f"Invalid math captcha format: {question_text}")  # Log error for invalid math captcha format
                return None

        # Handle math-based CAPTCHAs with multiplication
        elif "*" in question_text or "x" in question_text.lower():
            try:
                num1, num2 = map(int, re.findall(r'\d+', question_text))  # Extract numbers from the text
                return str(num1 * num2)  # Return the product as a string
            except ValueError:
                print(f"Invalid math captcha format: {question_text}")  # Log error for invalid math captcha format
                return None

        # Handle math-based CAPTCHAs with division
        elif "/" in question_text:
            try:
                num1, num2 = map(int, re.findall(r'\d+', question_text))  # Extract numbers from the text
                return str(num1 // num2)  # Return the quotient as a string (integer division)
            except (ValueError, ZeroDivisionError):
                print(
                    f"Invalid or zero division math captcha format: {question_text}")  # Log error for invalid or zero division
                return None

        # Handle CAPTCHAs requiring string reversal
        elif "reverse this" in question_text.lower():
            try:
                text_to_reverse = question_text.lower().replace("reverse this",
                                                                "").strip()  # Extract the text to reverse
                return text_to_reverse[::-1]  # Return the reversed string
            except Exception:
                print("Unable to reverse string")  # Log error for string reversal failure
                return None

        # Handle CAPTCHAs asking for the sum of digits
        elif "what is the sum of digits" in question_text.lower():
            try:
                digits = [int(d) for d in re.findall(r'\d', question_text)]  # Extract digits from the text
                return str(sum(digits))  # Return the sum of digits as a string
            except Exception:
                print("Unable to sum digits")  # Log error for digit summation failure
                return None

        # Handle CAPTCHAs asking for the square of a number
        elif "what is the square of" in question_text.lower():
            try:
                num = int(re.search(r'\d+', question_text).group())  # Extract the number from the text
                return str(num ** 2)  # Return the square of the number as a string
            except ValueError:
                print(f"Invalid square captcha format: {question_text}")  # Log error for invalid square captcha format
                return None

        # Handle CAPTCHAs asking if a number is even or odd
        elif "is this number even or odd" in question_text.lower():
            try:
                num = int(re.search(r'\d+', question_text).group())  # Extract the number from the text
                return "even" if num % 2 == 0 else "odd"  # Return 'even' or 'odd' based on the number
            except ValueError:
                print(f"Invalid even/odd captcha format: {question_text}")  # Log error for invalid format
                return None

        # Handle CAPTCHAs asking for the factorial of a number
        elif "what is the factorial of" in question_text.lower():
            try:
                num = int(re.search(r'\d+', question_text).group())  # Extract the number from the text
                factorial = 1
                for i in range(1, num + 1):
                    factorial *= i
                return str(factorial)  # Return the factorial as a string
            except ValueError:
                print(f"Invalid factorial captcha format: {question_text}")  # Log error for invalid format
                return None

        # Handle CAPTCHAs asking for the uppercase version of text
        elif "uppercase this" in question_text.lower():
            try:
                text_to_uppercase = question_text.lower().replace("uppercase this", "").strip()  # Extract the text
                return text_to_uppercase.upper()  # Return the text in uppercase
            except Exception:
                print("Unable to convert text to uppercase")  # Log error for uppercase conversion failure
                return None

        # Handle CAPTCHAs asking for a number's cube
        elif "what is the cube of" in question_text.lower():
            try:
                num = int(re.search(r'\d+', question_text).group())  # Extract the number from the text
                return str(num ** 3)  # Return the cube of the number as a string
            except ValueError:
                print(f"Invalid cube captcha format: {question_text}")  # Log error for invalid format
                return None

        # Handle CAPTCHAs asking for text palindrome check
        elif "is this text a palindrome" in question_text.lower():
            try:
                text_to_check = question_text.lower().replace("is this text a palindrome", "").strip()  # Extract text
                is_palindrome = text_to_check == text_to_check[::-1]  # Check if the text is a palindrome
                return "yes" if is_palindrome else "no"  # Return "yes" or "no" based on the result
            except Exception:
                print("Unable to check for palindrome")  # Log error for palindrome check failure
                return None

        # Handle unknown CAPTCHA types
        else:
            print(f"Unknown captcha type: {question_text}")  # Log error for unknown captcha type
            return None  # Return None for unsupported CAPTCHA

    def _enter_answer(self, answer):
        """Enters the answer into the captcha input field."""
        answer_input = WebDriverWait(self.driver, self.wait_timeout).until(  # Wait for the input field to be clickable
            EC.element_to_be_clickable(self.captcha_answer_locator)  # Wait condition for element to become clickable
        )
        answer_input.clear()  # Clear any existing content in the input field
        answer_input.send_keys(str(answer))  # Enter the answer into the input field

    def _submit_form(self):
        """Submits the form."""
        submit_button = WebDriverWait(self.driver, self.wait_timeout).until(
            # Wait for the submit button to be clickable
            EC.element_to_be_clickable(self.submit_button_locator)  # Wait condition for element to become clickable
        )
        submit_button.click()  # Perform a click action on the submit button

    def _solve_image_captcha(self):
        """Handles image-based CAPTCHA manually."""
        try:
            captcha_element = self.driver.find_element(By.ID,  # Locate the captcha image element by ID
                                                       'captchaImage')  # Replace with your CAPTCHA image element ID
            captcha_src = captcha_element.get_attribute('src')  # Retrieve the source attribute of the captcha image

            if captcha_src.startswith('data:image'):  # Check if the image source contains base64 data
                base64_data = captcha_src.split(",")[1]  # Extract the base64 encoded part of the source
                captcha_image_data = base64.b64decode(base64_data)  # Decode the base64 image data

                image = Image.open(io.BytesIO(captcha_image_data))  # Open the image from an in-memory byte stream
                image.show()  # Display the image to the user

                solved_captcha = input("Manually solve the CAPTCHA and enter the text: ")  # Prompt user for input

                captcha_input = self.driver.find_element(By.ID,  # Locate the captcha input field by ID
                                                         'captchaInput')  # Replace with your CAPTCHA input field ID
                captcha_input.send_keys(solved_captcha)  # Enter the manually solved captcha text

                submit_button = self.driver.find_element(By.ID,  # Locate the submit button by ID
                                                         'submitButton')  # Replace with your submit button ID
                submit_button.click()  # Perform a click action on the submit button
                print("Captcha solved and form submitted.")  # Log success message
            else:
                print("Unsupported image CAPTCHA format.")  # Log error for unsupported image formats
        except Exception as e:
            print(f"An error occurred while solving image CAPTCHA: {e}")  # Log any unexpected error


# --- Example Usage ---
def main():
    driver = webdriver.Chrome()  # Use the correct WebDriver instance (e.g., Chrome, Edge)

    try:
        # Replace with your test URL
        driver.get("https://example.com/your_test_captcha_page")  # Open the test webpage containing a CAPTCHA

        # Locators for text/math CAPTCHA
        captcha_question_locator = (By.ID, "captchaQuestion")  # Set locator for the captcha question element
        captcha_answer_locator = (By.ID, "captchaAnswer")  # Set locator for the captcha answer input field
        submit_button_locator = (By.ID, "submitButton")  # Set locator for the form's submit button

        # Initialize the solver
        solver = SimpleCaptchaSolver(driver, captcha_question_locator, captcha_answer_locator, submit_button_locator)

        # Attempt to solve the CAPTCHA
        if solver.solve_captcha():  # Check if captcha solving was successful
            print("Captcha Solved and form submitted!")  # Log success message
        else:
            print("Captcha solving failed.")  # Log failure message

    finally:
        driver.quit()  # Close the WebDriver instance after completing or failing the task


if __name__ == "__main__":
    main()  # Run the main function
