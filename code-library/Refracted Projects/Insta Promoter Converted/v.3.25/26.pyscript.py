import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class InstagramErrorHandlingApp:
    def __init__(self, root):
        # Setup Tkinter GUI
        self.root = root
        self.root.title("Instagram Error Handling")
        self.log_area = tk.Text(self.root, height=20, width=80)
        self.log_area.pack()

        # Initialize Selenium WebDriver
        self.driver = webdriver.Chrome(service=Service("/path/to/chromedriver"))  # Adjust the path to your chromedriver
        self.driver.get("https://www.instagram.com")  # Load Instagram's webpage

        # Run error handling process
        self.run_error_handling_process()

    def log_message(self, message: str):
        """Logs a message to the Tkinter text area."""
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_area.insert(tk.END, f"{current_time} - {message}\n")
        self.log_area.see(tk.END)

    def run_error_handling_process(self):
        try:
            # Wait until the page content is loaded and check for error
            wait = WebDriverWait(self.driver, 10)
            page_source = self.driver.page_source

            if ">Go back to Instagram.<" in page_source:
                self.log_message(
                    "SOFTWARE RUNNING - PAGE ERROR HANDLING ACTIVATED - RESENDING REQUEST - LOG RUNNING - INTERNALIZING COMPLETE")

                # Update log messages in the Tkinter interface
                self.update_log_ui("Please clean keyword list - Resending request")

                # Set skip_user as a global variable
                self.skip_user = 1

                # Simulate going back to Instagram
                self.back_to_instagram()
        except Exception as e:
            self.log_message(f"An error occurred: {str(e)}")

    def update_log_ui(self, additional_message: str):
        """Update the UI with informational logs."""
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_area.insert(tk.END, f"{current_time} - {additional_message}\n")
        self.log_area.see(tk.END)

    def back_to_instagram(self):
        """Handle the navigation back to Instagram."""
        self.driver.execute_script("window.history.back()")
        self.log_message("Navigated back to Instagram successfully")

    def close_app(self):
        """Safely close the web driver and the application."""
        self.driver.quit()
        self.root.destroy()


if __name__ == "__main__":
    # Create the Tkinter application
    root = tk.Tk()
    app = InstagramErrorHandlingApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close_app)  # Exit cleanly
    root.mainloop()

import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException


class AdvancedSkipTriggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Skip Trigger - Automation Panel")

        # Text area for logs
        self.log_area = tk.Text(self.root, height=25, width=100)
        self.log_area.pack()

        # Initialize Selenium WebDriver
        self.driver = webdriver.Chrome(service=Service("/path/to/chromedriver"))  # Adjust path
        self.skip_user = 0

        try:
            self.driver.get("https://www.instagram.com")  # Target Instagram URL
            self.log_message("Browser launched and Instagram page loaded.")
        except WebDriverException as e:
            self.log_message(f"Error while launching browser: {str(e)}")
            self.close_app()

        # Run the automation process
        self.run_advanced_skip_trigger()

    def log_message(self, message: str):
        """Logs a message to the Tkinter text area."""
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_area.insert(tk.END, f"{current_time} - {message}\n")
        self.log_area.see(tk.END)

    def run_advanced_skip_trigger(self):
        """Main logic for Advanced Skip Trigger."""
        try:
            wait = WebDriverWait(self.driver, 10)
            page_source = self.driver.page_source

            # Check advanced conditions here
            self.log_message("Starting Advanced Skip Trigger checks...")
            self.apply_advanced_skip_logic(page_source)
        except TimeoutException:
            self.log_message("Timeout while waiting for page to load!")
        except Exception as e:
            self.log_message(f"Unexpected error during automation: {e}")
        finally:
            self.log_message("Advanced Skip Trigger checks completed.")

    def apply_advanced_skip_logic(self, page_source: str):
        """Applies the various skip conditions."""
        # Example: Skip if doesn't contain current month
        if "Skip If Not Contains (Current Month)" in page_source:
            current_month = time.strftime("%B", time.localtime())
            if current_month not in page_source:
                self.log_message(f"Skip activated - Current month '{current_month}' not found.")
                self.skip_user = 1

        # Example: Check if page contains certain keywords
        if "minutes" not in page_source:
            self.log_message("Skip activated - 'minutes' keyword not found.")
            self.skip_user = 1

        if "seconds" not in page_source:
            self.log_message("Skip activated - 'seconds' keyword not found.")
            self.skip_user = 1

        # Example: Skip if account is private
        if "This Account is Private" in page_source:
            self.log_message("Skip activated - Account is private.")
            self.skip_user = 1

        # Example: Skip if no posts
        if "No posts yet" in page_source:
            self.log_message("Skip activated - No posts yet.")
            self.skip_user = 1

        # Example: Skip if the text contains non-English characters
        non_english_check = self.contains_non_english_characters(page_source)
        if non_english_check:
            self.log_message("Skip activated - Contains non-English text.")
            self.skip_user = 1

        if self.skip_user:
            self.log_message("Advanced skip logic triggered! Skipping the user.")
        else:
            self.log_message("Advanced skip logic passed. Proceeding with the user.")

    def contains_non_english_characters(self, text: str) -> bool:
        """Checks if a string contains non-ASCII characters."""
        return any(ord(char) > 127 for char in text)

    def close_app(self):
        """Safely closes the application."""
        try:
            if self.driver:
                self.driver.quit()
        except Exception as e:
            self.log_message(f"Error while closing the browser: {str(e)}")
        finally:
            self.root.destroy()

    def log_event_to_ui(self, message: str):
        """Simulates logging updates in the user interface."""
        self.log_message(message)


if __name__ == "__main__":
    # Create and run the Tkinter application
    root = tk.Tk()
    app = AdvancedSkipTriggerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close_app)  # Clean close
    root.mainloop()

import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class AdvancedSkipTriggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Skip Trigger App")
        self.driver = webdriver.Chrome()  # Replace with your WebDriver setup
        self.skip_user = 0

        # Setting up the log area
        self.log_area = ScrolledText(root, wrap=tk.WORD, width=100, height=20)
        self.log_area.pack(pady=10)

        # Adding UI Buttons
        self.run_button = tk.Button(root, text="Run Skip Trigger", command=self.run_advanced_skip_trigger)
        self.run_button.pack(pady=5)

        self.close_button = tk.Button(root, text="Close", command=self.close_app)
        self.close_button.pack(pady=5)

    def log_message(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {message}\n"
        self.log_area.insert(tk.END, log_entry)
        self.log_area.see(tk.END)

    def run_advanced_skip_trigger(self):
        # Placeholder for actual URL
        self.driver.get("https://www.instagram.com")

        if self.skip_user != 1:
            self.skip_user = 0
            self.log_message("BIO SKIP OPTION ACTIVATED!")

            try:
                # Check for the presence of specific bio element
                bio_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[@id='react-root']/section/main/div/div/article/header/div[2]/div[1]/div[1]"))
                )
                if bio_element:
                    bio_element.click()
                    self.log_message("Bio Element Found and Clicked.")

            except Exception as e:
                self.log_message(f"Error with Bio Element: {str(e)}")

            # Wait for the condition based on the document text
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.text_to_be_present_in_element((By.XPATH, "//body"), "following")
                )
            except Exception:
                wait_breakout = 0
                self.log_message("Waiting for bio skip option request to complete.")
                while wait_breakout < 100:
                    if "following" in self.driver.page_source:
                        break
                    time.sleep(0.1)
                    wait_breakout += 1

            # Additional logic for bio scraping
            self.set_urls()

            if self.skip_user == 1:
                self.log_message("Skipping request as bio contains a link.")

    def set_urls(self):
        """ Scraping bio URLs via XPath and running skip logic """
        urls = []
        try:
            # Example XPath scraping
            bio_links = self.driver.find_elements(By.XPATH,
                                                  "//span[@id='react-root']/section/main/article/header/section/div[2]/a")
            urls = [link.get_attribute('href') for link in bio_links if link.get_attribute('href')]

            # Validate links from scraped data
            url_pattern = re.compile(r"(http|https)\:\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,4}(\/[\w\.?=\/\#\%&\-]+|\/|)")
            for url in urls:
                if url_pattern.search(url):
                    self.log_message(f"Skipped Bio Link Found: {url}")
                    self.skip_user = 1
                    break
        except Exception as e:
            self.log_message(f"Error during URL scraping: {str(e)}")

    def close_app(self):
        """ Closes the application """
        self.driver.quit()
        self.log_message("Application Closed.")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedSkipTriggerApp(root)
    root.mainloop()

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import threading
import time


class AutoRatioCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Ratio Calculator")
        self.driver = None

        # UI setup
        self.log_area = ScrolledText(root, wrap=tk.WORD, height=20, width=60)
        self.log_area.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Auto Ratio Calculate", command=self.start_auto_calculate)
        self.start_button.pack(pady=5)

        self.close_button = tk.Button(root, text="Close App", command=self.close_app)
        self.close_button.pack(pady=5)

        # Variables
        self.skip_user = 0
        self.follow_greater_than = None
        self.follow_less_than = None
        self.follow_equal_to = None

    def log_message(self, message):
        """Log a message into the UI log text area."""
        current_time = time.strftime("%H:%M:%S")  # Get current time as a string
        self.log_area.insert(tk.END, f"{current_time} - {message}\n")
        self.log_area.see(tk.END)  # Scroll to the end

    def start_auto_calculate(self):
        """Start the ratio calculation in a separate thread."""
        self.log_message("Starting Auto Ratio Calculation Process...")
        self.skip_user = 0  # Initial value

        # Start browser automation in a thread.
        threading.Thread(target=self.run_auto_calculate, daemon=True).start()

    def run_auto_calculate(self):
        """Perform automation logic using Selenium."""
        # Selenium Setup
        try:
            self.driver = webdriver.Chrome()  # Ensure you have 'chromedriver' installed and in PATH
            self.driver.get("https://example.com")  # Replace with actual URL

            self.log_message("Browser Launched. Accessing the website...")

            # Example login or navigation logic
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
            )
            username_input = self.driver.find_element(By.XPATH, "//input[@name='username']")
            username_input.send_keys("your_username")  # Replace with actual username
            self.log_message("Logging in to the account.")

            password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
            password_input.send_keys("your_password")  # Replace with actual password
            password_input.send_keys(Keys.RETURN)

            # Wait for login
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@id='react-root']"))
            )
            self.log_message("Logged in successfully!")

            # Process users for ratio calculation
            while True:
                if self.skip_user != 0:
                    break

                self.log_message("Fetching data for the next user...")

                # Example logic: Wait for DOM and then scrape ratio values
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//section[@id='user-section']"))
                )
                try:
                    followers = int(
                        self.driver.find_element(By.XPATH, "//*[@id='followers-count']").text.replace(",", ""))
                    following = int(
                        self.driver.find_element(By.XPATH, "//*[@id='following-count']").text.replace(",", ""))
                    ratio = round(followers / following, 1)

                    self.log_message(f"Followers: {followers}, Following: {following}, Ratio: {ratio}")

                    # Custom logic for ratio-based action
                    if self.follow_greater_than and ratio > self.follow_greater_than:
                        self.log_message(
                            f"Ratio {ratio} greater than threshold {self.follow_greater_than}. Following user!"
                        )
                        # Perform follow action here
                    elif self.follow_less_than and ratio < self.follow_less_than:
                        self.log_message(
                            f"Ratio {ratio} less than threshold {self.follow_less_than}. Skipping user."
                        )
                        self.skip_user = 1
                    else:
                        self.log_message(f"Ratio {ratio} does not meet any threshold. Skipping user.")

                except (NoSuchElementException, ValueError):
                    self.log_message("Error while calculating ratio for the user. Skipping...")
                    continue

                # Navigate Back
                self.driver.back()
                time.sleep(2)  # Allow loading time
                self.log_message("Navigated back successfully. Checking next user...")

        except Exception as e:
            self.log_message(f"An error occurred: {str(e)}")
        finally:
            if self.driver:
                self.driver.quit()
                self.log_message("Browser closed.")

    def close_app(self):
        """Close the application."""
        if self.driver:
            self.driver.quit()
        self.root.quit()
        self.log_message("Application closed.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AutoRatioCalculatorApp(root)
    root.mainloop()
