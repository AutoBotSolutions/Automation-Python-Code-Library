import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class FollowButtonAutomation:
    def __init__(self):
        # Selenium WebDriver setup
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def scroll_browser(self):
        """Scroll the browser by a specified amount."""
        self.driver.execute_script("window.scrollBy(-10000, -10000);")

    def element_exists(self, xpath):
        """Check if an element exists on the webpage."""
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except:
            return False

    def click_element(self, xpath):
        """Click an element based on the provided xpath."""
        if self.element_exists(xpath):
            element = self.driver.find_element(By.XPATH, xpath)
            ActionChains(self.driver).move_to_element(element).click().perform()

    def run_follow_button_click(self):
        """Core automation logic to locate and click Follow buttons."""
        self.scroll_browser()

        # First span button
        self.click_element('//*[@id="react-root"]/section/main/article/header/section/div[1]/span')

        # Second button
        self.click_element('/html/body/div[4]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/span[2]/button')

        # Third button
        self.click_element(
            '//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[2]/span[2]/button')

        # Fourth button
        self.click_element('//*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button')

        # Fifth button
        self.click_element('//*[@id="react-root"]/section/main/div/header/section/div[1]/span/button')


class FollowButtonUI:
    def __init__(self, automation):
        self.automation = automation
        self.setup_ui()

    def setup_ui(self):
        """Setup the Tkinter User Interface."""
        self.root = tk.Tk()
        self.root.title("Follow Button Automation")
        self.root.geometry("400x200")

        label = tk.Label(self.root, text="Click the button to run automation", font=("Arial", 12))
        label.pack(pady=20)

        run_button = tk.Button(self.root, text="Run Follow Automation", command=self.automation.run_follow_button_click,
                               font=("Arial", 14), bg="green", fg="white", padx=10, pady=5)
        run_button.pack(pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.exit_application,
                                font=("Arial", 14), bg="red", fg="white", padx=10, pady=5)
        exit_button.pack(pady=10)

        self.root.mainloop()

    def exit_application(self):
        """Clean up on exit."""
        self.automation.driver.quit()
        self.root.destroy()


# Application entry point
if __name__ == "__main__":
    automation = FollowButtonAutomation()
    ui = FollowButtonUI(automation)

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class LikeButtonAutomation:
    def __init__(self):
        # Selenium WebDriver setup
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def element_exists(self, xpath):
        """Check if an element exists on the webpage."""
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except:
            return False

    def click_element(self, xpath):
        """Click an element based on the provided xpath."""
        if self.element_exists(xpath):
            element = self.driver.find_element(By.XPATH, xpath)
            ActionChains(self.driver).move_to_element(element).click().perform()

    def run_like_button_click(self):
        """Core automation logic to locate and click Like buttons."""
        # First possible Like button
        self.click_element("x://html/body/div[4]/div/div[2]/div/article/div[2]/section[1]/a[1]")

        # Second possible Like button
        self.click_element("x://html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/a[1]")

        # Third possible Like button
        self.click_element("x://html/body/div[4]/div/div[2]/div/article/div[2]/section[1]/a[1]/span")


class LikeButtonUI:
    def __init__(self, automation):
        self.automation = automation
        self.setup_ui()

    def setup_ui(self):
        """Setup the Tkinter User Interface."""
        self.root = tk.Tk()
        self.root.title("Like Button Automation")
        self.root.geometry("400x200")

        label = tk.Label(self.root, text="Click the button to run automation", font=("Arial", 12))
        label.pack(pady=20)

        run_button = tk.Button(self.root, text="Run Like Automation", command=self.automation.run_like_button_click,
                               font=("Arial", 14), bg="green", fg="white", padx=10, pady=5)
        run_button.pack(pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.exit_application,
                                font=("Arial", 14), bg="red", fg="white", padx=10, pady=5)
        exit_button.pack(pady=10)

        self.root.mainloop()

    def exit_application(self):
        """Clean up on exit."""
        self.automation.driver.quit()
        self.root.destroy()


# Main entry point
if __name__ == "__main__":
    automation = LikeButtonAutomation()
    ui = LikeButtonUI(automation)

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Automation Class for Unfollow Button
class UnfollowButtonAutomation:
    def __init__(self, driver: webdriver.Chrome):
        """
        Initialize the UnfollowButtonAutomation with a Selenium WebDriver.
        """
        self.driver = driver

    def element_exists(self, xpath: str) -> bool:
        """
        Check if an element exists on the page.
        """
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except Exception:
            return False

    def move_mouse_to_element(self, xpath: str):
        """
        Move the mouse to an element specified by the given XPath.
        """
        element = self.driver.find_element(By.XPATH, xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def click_element(self, xpath: str):
        """
        Scroll to and click the element at the specified XPath.
        """
        element = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("window.scrollBy(-10000, -10000);")  # Scroll up if necessary
        element.click()

    def run_unfollow_button_click(self):
        """
        Execute the logic to find and click the unfollow button if it exists.
        """
        xpaths = [
            "//span[@id='react-root']/section/main/article/header/section/div[1]/span/span[1]/button",
            "//span[@id='react-root']/section/main/div/header/section/div[1]/span/span[1]/button",
            "//span[@id='react-root']/section/main/div/header/section/div[1]/span/button"
        ]
        for xpath in xpaths:
            if self.element_exists(xpath):
                self.move_mouse_to_element(xpath)
                self.click_element(xpath)
                break


# UI Class for Unfollow Button
class UnfollowButtonUI:
    def __init__(self, root: tk.Tk, automation: UnfollowButtonAutomation):
        """
        Initialize the Tkinter user interface with automation logic for the unfollow button.
        """
        self.root = root
        self.automation = automation
        self.setup_ui()

    def setup_ui(self):
        """
        Set up the user interface elements.
        """
        self.root.title("Unfollow Button Automation")

        # Add widgets for the UI
        label = tk.Label(self.root, text="Unfollow Button Automation")
        label.pack(pady=10)

        unfollow_button = tk.Button(self.root, text="Run Unfollow", command=self.run_unfollow_automation)
        unfollow_button.pack(pady=5)

        exit_button = tk.Button(self.root, text="Exit", command=self.exit_application)
        exit_button.pack(pady=5)

    def run_unfollow_automation(self):
        """
        Trigger the unfollow button automation.
        """
        try:
            self.automation.run_unfollow_button_click()
            messagebox.showinfo("Success", "Unfollow button automation completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def exit_application(self):
        """
        Exit the Tkinter application.
        """
        self.root.quit()


# Main Function
def main():
    # Set up a Selenium WebDriver
    driver = webdriver.Chrome()  # Ensure the ChromeDriver is in your PATH
    driver.get("https://www.instagram.com")  # Replace with the target website

    # Initialize the automation and UI components
    automation = UnfollowButtonAutomation(driver)
    root = tk.Tk()
    ui = UnfollowButtonUI(root, automation)

    # Start the Tkinter main loop
    root.mainloop()

    # Close the browser after the UI is closed
    driver.quit()


if __name__ == "__main__":
    main()

import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk, Label, Button


class NavigateFallbackMethodAutomation:
    def __init__(self, driver):
        """
        Automation class to handle fallback navigation.
        :param driver: WebDriver instance for Selenium
        """
        self.driver = driver

    def scroll_browser(self, x_offset, y_offset):
        """Scrolls the browser window by the specified offsets."""
        self.driver.execute_script(f"window.scrollBy({x_offset}, {y_offset});")
        time.sleep(1)

    def element_exists(self, xpath):
        """Check if an element exists in the DOM by its XPath."""
        try:
            return self.driver.find_element(By.XPATH, xpath).is_displayed()
        except Exception:
            return False

    def click_element(self, xpath):
        """Click on an element if it exists."""
        if self.element_exists(xpath):
            self.driver.find_element(By.XPATH, xpath).click()
            time.sleep(1)

    def type_text(self, xpath, text):
        """Type text into an input field."""
        if self.element_exists(xpath):
            input_element = self.driver.find_element(By.XPATH, xpath)
            input_element.clear()
            input_element.send_keys(text)
            time.sleep(1)

    def wait_for_element(self, xpath, timeout):
        """Wait for an element to appear within a timeout period."""
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def run_navigate_fallback(self, ran_keyword):
        """
        Executes the fallback navigation logic.
        :param ran_keyword: The keyword to interact with on the page
        """
        # Fallback cases based on page content
        page_source = self.driver.page_source

        # Check for "Go Back"
        if "Go Back" in page_source:
            self.driver.back()
            time.sleep(3)
            self.click_element("//html/body/div[3]/div/button")
            self.type_text("//input[@value='']", ran_keyword)

            # Wait and click based on keyword
            self.wait_for_element("//span[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]", 5)
            matching_class = re.search(r'(?!\"><span\sclass=\")[_A-Z0-9a-z\s]+(?=\">' + ran_keyword + '</span></div>)',
                                       page_source)
            if matching_class:
                class_name = matching_class.group()
                self.click_element(f"//span[@class='{class_name}'][.='{ran_keyword}']")
                self.wait_for_element("//span[@id='react-root']/section/main/article/div[1]/h2", 5)

        # Check for "Go back"
        elif "Go back" in page_source:
            self.driver.back()
            time.sleep(3)
            self.click_element("//html/body/div[3]/div/button")
            self.type_text("//input[@value='']", ran_keyword)

            # Wait and interact with the keyword element
            self.wait_for_element("//span[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]", 5)
            matching_class = re.search(r'(?!\"><span\sclass=\")[_A-Z0-9a-z\s]+(?=\">' + ran_keyword + '</span></div>)',
                                       page_source)
            if matching_class:
                class_name = matching_class.group()
                self.click_element(f"//span[@class='{class_name}'][.='{ran_keyword}']")
                self.wait_for_element("//span[@id='react-root']/section/main/article/div[1]/h2", 5)

        # Check for the fallback condition to direct navigation
        elif 'value="#"' in page_source:
            self.driver.get(f"https://www.instagram.com/explore/tags/{ran_keyword}/")
            self.wait_for_element("//span[@id='react-root']/section/main/article/div[1]/h2", 5)


class NavigateFallbackMethodUI:
    def __init__(self, automation):
        """
        UI class to handle the interface for navigating fallback actions.
        :param automation: NavigateFallbackMethodAutomation instance
        """
        self.automation = automation
        self.root = Tk()
        self.root.title("Navigate Fallback Method")
        self.setup_ui()

    def setup_ui(self):
        """Setup UI elements."""
        Label(self.root, text="Fallback Navigation Automation").pack(pady=20)

        Button(self.root, text="Run Navigate Fallback", command=self.run_navigate_automation).pack(pady=10)
        Button(self.root, text="Exit", command=self.exit_application).pack(pady=10)

    def run_navigate_automation(self):
        """Run the navigate fallback automation."""
        # Example keyword passed dynamically (could be dynamically fetched in a larger setup)
        ran_keyword = "example_keyword"
        self.automation.run_navigate_fallback(ran_keyword)

    def exit_application(self):
        """Exit the application."""
        self.root.quit()

    def start(self):
        """Start the Tkinter main loop."""
        self.root.mainloop()

# Usage Example:
# Please ensure you have a Selenium WebDriver instance set up as `driver` before running this example.
# from selenium import webdriver
# driver = webdriver.Chrome()  # Adjust based on your browser and setup
# automation = NavigateFallbackMethodAutomation(driver)
# ui = NavigateFallbackMethodUI(automation)
# ui.start()

import time
from tkinter import Tk, Label, Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MultiCommentAutomation:
    def __init__(self, driver, random_comment):
        self.driver = driver
        self.random_comment = random_comment

    def element_exists(self, xpath):
        """Check if an element is present on the page."""
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except:
            return False

    def type_text_with_delay(self, element, text, delay_min=10, delay_max=50):
        """Simulate human typing with a delay."""
        for char in text:
            element.send_keys(char)
            time.sleep((delay_min + delay_max) / 1000)

    def send_comment(self, xpath):
        if not self.random_comment in self.driver.page_source:
            try:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                element.click()
                self.type_text_with_delay(element, self.random_comment)
                element.send_keys(Keys.ENTER)
            except Exception as e:
                print(f"Error sending comment at {xpath}: {e}")

    def run_multi_comment_action(self):
        """Perform the multi-comment action."""
        xpaths = [
            "//*[@id='react-root']/section/main/div/div/article/div[2]/section[3]/form/textarea",
            "/html/body/div[4]/div/div[2]/div/article/div[2]/section[3]/form/textarea",
            "//*[@id='react-root']/section/main/div/div/article/div[2]/section[3]/form",
            "//textarea[@aria-label='Add a comment…']",
            "//textarea[@placeholder='Add a comment…']",
        ]
        for xpath in xpaths:
            print(f"Attempting comment on element: {xpath}")
            self.send_comment(xpath)


class MultiCommentUI:
    def __init__(self, automation):
        self.automation = automation
        self.root = Tk()

    def setup_ui(self):
        """Setup the User Interface for triggering actions."""
        self.root.title("Multi Comment Automation")
        Label(self.root, text="Multi Comment Automation Tool", font=("Arial", 16)).pack(pady=10)

        Button(self.root, text="Run Multi Comment Automation", command=self.run_automation, width=30).pack(pady=10)
        Button(self.root, text="Exit", command=self.exit_application, width=30).pack(pady=10)

    def run_automation(self):
        """Run the multi-comment automation."""
        self.automation.run_multi_comment_action()

    def exit_application(self):
        """Exit the application."""
        self.root.quit()
        self.root.destroy()

    def start(self):
        """Start the Tkinter UI loop."""
        self.setup_ui()
        self.root.mainloop()


def main():
    # Initialize WebDriver
    driver = webdriver.Chrome()  # Make sure you have the appropriate WebDriver (e.g., chromedriver)
    driver.get("https://example.com")  # Replace with the appropriate URL

    random_comment = "This is a random comment."  # Replace with your desired comment

    # Set up automation and UI
    automation = MultiCommentAutomation(driver, random_comment)
    ui = MultiCommentUI(automation)

    try:
        ui.start()
    finally:
        driver.quit()


if __name__ == "__main__":
    main()

import time
from tkinter import Tk, Button, Label, Text, Scrollbar, END
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# Helper class for automation tasks
class MultiCommentAutomation:
    def __init__(self, driver: webdriver.Chrome, random_comment: str):
        self.driver = driver
        self.random_comment = random_comment

    # Check if an element exists based on a locator
    def element_exists(self, by: By, value: str) -> bool:
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    # Types text with a delay character by character
    def type_text_with_delay(self, element, text: str, delay: float = 0.1):
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    # Simulates sending a comment in the browser
    def send_comment(self, textarea_id: str, comment: str):
        textarea = self.driver.find_element(By.ID, textarea_id)
        textarea.clear()
        self.type_text_with_delay(textarea, comment)
        textarea.send_keys("\n")  # Simulating the comment submission

    # Main method to run the comment automation
    def run_multi_comment_action(self, textarea_id: str):
        if not self.element_exists(By.ID, textarea_id):
            print(f"Textarea with ID '{textarea_id}' does not exist.")
            return

        # Wait loop breakout mechanism
        wait_breakout = 0
        wait_trigger = 0

        print("SOFTWARE RUNNING - WAITING FOR COMMENT REQUEST TO COMPLETE")
        while wait_trigger == 0:
            time.sleep(0.1)
            wait_breakout += 1

            # Break the loop if the random comment is found
            page_source = self.driver.page_source
            if self.random_comment in page_source:
                wait_trigger = 1

            elif wait_breakout >= 100:
                print("Wait breakout threshold reached.")
                wait_trigger = 1

        # Send the comment after wait conditions are met
        self.send_comment(textarea_id, f"{time.ctime()} - AUTOMATIC COMMENT")

        print("COMMENT COMPLETED - SOFTWARE INTERNAL LOGGING COMPLETE")


# UI Class integrated with Tkinter
class MultiCommentUI:
    def __init__(self, root: Tk, automation: MultiCommentAutomation):
        self.root = root
        self.automation = automation

    # Sets up the user interface
    def setup_ui(self):
        self.root.title("Multi Tool Bot - Automation")

        # Instruction Label
        Label(self.root, text="Automate Comment Submission").pack(pady=10)

        # Text Input Area (for textarea ID)
        Label(self.root, text="Enter TextArea ID:").pack(pady=5)
        self.textarea_id_input = Text(self.root, height=1, width=30)
        self.textarea_id_input.pack(pady=5)

        # Random Comment Display Area
        self.output_label = Label(self.root, text="Output Logs:", anchor="w")
        self.output_label.pack(pady=5)
        self.output_display = Text(self.root, height=10, width=50)
        self.output_display.pack(pady=5)
        scrollbar = Scrollbar(self.root, command=self.output_display.yview)
        scrollbar.pack(side="right", fill="y")
        self.output_display.config(yscrollcommand=scrollbar.set)

        # Submit Button
        Button(self.root, text="Run Automation", command=self.run_automation).pack(pady=10)

        # Exit Button
        Button(self.root, text="Exit", command=self.exit_application).pack(pady=10)

    # Executes automation and logs output
    def run_automation(self):
        textarea_id = self.textarea_id_input.get("1.0", END).strip()

        if not textarea_id:
            self.output_display.insert(END, "Error: Textarea ID cannot be empty!\n")
            return

        try:
            self.automation.run_multi_comment_action(textarea_id)
            self.output_display.insert(END, f"Comment Submitted to TextArea ID: {textarea_id}\n")
        except Exception as e:
            self.output_display.insert(END, f"Error during automation: {str(e)}\n")

    # Terminates the Tkinter application
    def exit_application(self):
        self.root.quit()
        self.root.destroy()


# Main driver function
def main():
    # Selenium WebDriver setup
    driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and set in PATH
    random_comment = "sample comment for automation"
    automation = MultiCommentAutomation(driver, random_comment)

    # Tkinter UI setup
    root = Tk()
    app_ui = MultiCommentUI(root, automation)
    app_ui.setup_ui()

    # Starting the Tkinter event loop
    root.mainloop()

    # Cleanup after closing the UI
    driver.quit()


if __name__ == "__main__":
    main()
