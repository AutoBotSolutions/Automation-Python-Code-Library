import tkinter as tk
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import requests
import random


def post_tracking_data(session_id):
    """
    Simulates the HTTP POST request to the tracking endpoint for logging.
    """
    tracking_url = (
        f"http://app.tracking.softwareautomation.org/appstats/piwik.php?"
        f"&idsite=1&rec=1&_id={session_id}&rand={random.randint(1000, 9999)}"
        f"&apiv=1&action_name=[Running Succession Module Function] Comment Function Activated"
        f"&url=http://app.tracking.org"
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"
    }
    response = requests.get(tracking_url, headers=headers, timeout=20)
    return response.status_code


def append_to_log(textarea, message):
    """
    Appends a log message to the Tkinter text area with a timestamp.
    """
    current_time = datetime.now().strftime("%H:%M:%S")
    log_message = f"{current_time} - {message}\n"
    textarea.insert(tk.END, log_message)
    textarea.see(tk.END)


class MultiCommentBot:
    def __init__(self):
        # Initialize the UI
        self.root = tk.Tk()
        self.root.title("Multi Comment Bot")

        self.textarea = tk.Text(self.root, width=100, height=30, bg="black", fg="yellow")
        self.textarea.pack()

        self.start_button = tk.Button(
            self.root, text="Start Bot", command=self.run_comment_function_two
        )
        self.start_button.pack()

        # Selenium WebDriver setup
        options = FirefoxOptions()
        options.add_argument("--headless")  # Run browser in headless mode
        self.driver = webdriver.Firefox(
            service=FirefoxService(), options=options  # Adjust if using other drivers
        )

        self.session_id = "123456"  # Simulated session ID for tracking

    def clear_scrape_list_and_log(self):
        append_to_log(
            self.textarea,
            "SOFTWARE RUNNING - CLEARING SCRAPE LIST, RESETTING QUEUE - COMMENT BOT - LOG RUNNING - INTERNALIZING COMPLETE",
        )

    def send_browser_request(self):
        random_keywords = ["automation", "software", "python", "instagram"]
        keyword = random.choice(random_keywords)
        keyword = keyword.replace("#", "")
        append_to_log(
            self.textarea,
            f"SOFTWARE RUNNING - COMMENT BOT SENDING BROWSER REQUEST TO KEYWORD [{keyword}] - COMMENT BOT - LOG RUNNING - INTERNALIZING COMPLETE",
        )

        # Open Instagram tag page
        try:
            self.driver.get(f"https://www.instagram.com/explore/tags/{keyword}/")
            time.sleep(5)  # Allow page to load
        except TimeoutException:
            append_to_log(self.textarea, "Failed to navigate to the Instagram page")
            return

        # Fallback if specific elements are not found
        try:
            self.driver.find_element(
                By.XPATH, "//section/main/article/div[1]/h2"
            ).is_displayed()
        except NoSuchElementException:
            append_to_log(self.textarea, "Fallback triggered for navigating elements.")

    def run_comment_function_two(self):
        # Step 1: Start log
        append_to_log(
            self.textarea,
            "COMMENT BOT - Logging started. Tracking initiated with the backend system.",
        )

        # Step 2: HTTP POST Request to tracking
        status = post_tracking_data(self.session_id)
        append_to_log(
            self.textarea,
            f"Tracking HTTP request completed with status code: {status}",
        )

        # Step 3: Clear scrape list
        self.clear_scrape_list_and_log()

        # Step 4: Send Selenium browser requests
        self.send_browser_request()

        # Step 5: Log completion message
        append_to_log(self.textarea, "COMMENT BOT PROCESS COMPLETED.")

    def run(self):
        self.root.mainloop()
        self.driver.quit()


if __name__ == "__main__":
    bot = MultiCommentBot()
    bot.run()

import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import datetime
import re


class MultiCommentBot:
    def __init__(self, root):
        # Tkinter UI setup
        self.root = root
        self.root.title("Comment Bot GUI")

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Bot", command=self.run_comment_function_three)
        self.start_button.pack(pady=10)

        # Selenium setup
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")  # Run browser in headless mode
        self.driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)

        # Control Variables
        self.comment_queue = 0
        self.loop_breakout = False
        self.scrape_failed = 0

    def append_to_log(self, message):
        """Log messages to the text area in the UI."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.text_area.insert(tk.END, f"{timestamp} - {message}\n")
        self.text_area.see(tk.END)

    def add_to_list_via_regex(self, source_text):
        """Extract items matching regex and remove duplicates."""
        regex_pattern = r"(?!<a\shref=\"\/p\/)[A-Z_a-z0-9]{9,14}(?=\/\?tagged=)"
        matches = re.findall(regex_pattern, source_text)
        return list(set(matches))  # Remove duplicates

    def get_time_stamp(self):
        """Return the current timestamp for logging purposes."""
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def run_comment_function_three(self):
        self.append_to_log("SOFTWARE RUNNING - COMMENT BOT START")

        # Scrape data from the current webpage
        try:
            page_source = self.driver.page_source
            scraped_list = self.add_to_list_via_regex(page_source)
            self.comment_queue = len(scraped_list)
        except Exception as e:
            self.append_to_log(f"Error during scraping: {e}")
            self.comment_queue = 0

        # Handle scrape results
        if self.comment_queue >= 10:
            self.append_to_log(
                f"{self.get_time_stamp()} - SOFTWARE RUNNING - COMMENT BOT SCRAPE SUCCESS - "
                "TRIGGERING LOOP BREAKOUT - LOG RUNNING - INTERNALIZING COMPLETE"
            )
            self.loop_breakout = True
        elif self.comment_queue == 0:
            self.scrape_failed += 1
            if self.scrape_failed >= 3:
                self.append_to_log(
                    f"{self.get_time_stamp()} - SOFTWARE RUNNING - COMMENT BOT SCRAPE FAILED - "
                    "TRIGGERING LOOP BREAKOUT - LOG RUNNING - INTERNALIZING COMPLETE"
                )
                self.loop_breakout = True

        # Simulate scrolling and waiting for specific elements
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait for an element to appear
            self.driver.implicitly_wait(3)
            self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/article/div[3]/div")
        except TimeoutException:
            self.append_to_log("Scrolling or waiting for element failed.")

        if not self.comment_queue:
            self.append_to_log("No data scraped, invoking AppListScrapingFailed.")
            self.app_list_scraping_failed()

    def app_list_scraping_failed(self):
        """Handle failed scraping by logging an error."""
        self.append_to_log(f"{self.get_time_stamp()} - SOFTWARE RUNNING - SCRAPING FAILED.")

    def run(self):
        """Entry point to start the bot."""
        try:
            self.append_to_log("Starting Bot...")
            self.run_comment_function_three()
        finally:
            self.driver.quit()
            self.append_to_log("Bot finished execution. WebDriver closed.")


if __name__ == "__main__":
    root = tk.Tk()
    bot_ui = MultiCommentBot(root)
    root.mainloop()

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import datetime


class MultiCommentBot:
    def __init__(self, driver_path, ui_root):
        self.driver_path = driver_path
        self.root = ui_root
        self.text_area = None
        self.initialize_ui()
        self.driver = None
        self.comment_queue = []
        self.scraped_list = []
        self.advanced_comment_scrape = []

    def initialize_ui(self):
        """Sets up the basic UI with tkinter."""
        self.root.title("MultiCommentBot")

        self.text_area = tk.Text(self.root, width=80, height=20)
        self.text_area.pack()

        start_button = tk.Button(self.root, text="Start", command=self.run_comment_function_four)
        start_button.pack()

    def append_to_log(self, message):
        """Logs a message to the UI text area with timestamps."""
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.text_area.insert(tk.END, f"{time_stamp} - {message}\n")
        self.text_area.see(tk.END)

    def setup_browser(self):
        """Initializes the Selenium WebDriver."""
        options = FirefoxOptions()
        options.add_argument("--headless")
        service = FirefoxService(self.driver_path)
        self.driver = webdriver.Firefox(service=service, options=options)

    def randomize_scraped_list(self, scraped_list):
        """Randomizes and de-duplicates the scraped list."""
        import random
        randomized_list = list(set(scraped_list))  # Removes duplicates
        random.shuffle(randomized_list)
        return randomized_list

    def run_comment_function_four(self):
        """Implementation of the Python version of MultiCommentFunctionFour."""
        self.append_to_log("SOFTWARE RUNNING - INITIALIZING")

        if self.is_randomize_scrape_list():
            self.append_to_log("RANDOMIZE SCRAPED LIST OPTION SELECTED - RANDOMIZING LIST")
            randomized_list = self.randomize_scraped_list(self.scraped_list)

            # Mimic advanced processing with scraping logic
            temp_list = []
            for random_item in randomized_list:
                temp_list.append(random_item)

            # Clear and populate advanced_comment_scrape list
            self.advanced_comment_scrape.clear()
            self.advanced_comment_scrape.extend(temp_list)
            self.append_to_log("LIST RANDOMIZATION COMPLETE")

        # Reduce list size according to `comment_per_tag`
        comment_per_tag = 10  # Example value
        if len(self.advanced_comment_scrape) > comment_per_tag:
            self.advanced_comment_scrape = self.advanced_comment_scrape[:comment_per_tag]

        self.comment_queue = len(self.advanced_comment_scrape)

        self.append_to_log(f"COMMENT SCRAPE QUEUE TOTAL = [{self.comment_queue}] - FINALIZED")
        self.append_to_log("PROCESS COMPLETE")

    def is_randomize_scrape_list(self):
        """Simulates the checking of a condition."""
        # For example, hardcoded to return True
        return True

    def run(self):
        """Start the bot with UI."""
        self.root.mainloop()


# Usage Example (assuming GeckoDriver is in the same directory):
if __name__ == "__main__":
    driver_path = "./geckodriver"  # Path to the GeckoDriver
    root = tk.Tk()

    bot = MultiCommentBot(driver_path, root)
    bot.run()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import random
import time


class MultiCommentBot:
    def __init__(self, driver_path, root):
        self.driver_path = driver_path
        self.root = root
        self.driver = None
        self.text_area = None
        self.advanced_comment_scrape = 0
        self.comment_queue = 0
        self.scraped_list = []
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("MultiCommentBot - Instagram Automation")

        # Textarea for logging
        self.text_area = tk.Text(self.root, wrap=tk.WORD, height=20, width=80)
        self.text_area.pack(pady=10)

        # Start Button
        start_button = tk.Button(self.root, text="Start Bot", command=self.run_comment_function_five)
        start_button.pack()

    def append_to_log(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.text_area.insert(tk.END, f"{timestamp} - {message}\n")
        self.text_area.see(tk.END)

    def setup_browser(self):
        self.append_to_log("Setting up Firefox WebDriver...")
        try:
            options = FirefoxOptions()
            options.add_argument("--headless")  # Comment this line to see the browser
            service = FirefoxService(self.driver_path)
            self.driver = webdriver.Firefox(service=service, options=options)
            self.append_to_log("Browser setup complete.")
        except Exception as e:
            self.append_to_log(f"Error while setting up browser: {e}")
            messagebox.showerror("Error", "Browser setup failed. Please check the driver path.")

    def scrape_target_user(self, url, keyword):
        self.append_to_log(f"Navigating to post URL with keyword [{keyword}]...")
        try:
            self.driver.get(url)
            time.sleep(3)  # Adjust as needed based on network speed

            # Example: Wait for buttons or certain element to appear
            button = self.driver.find_element(By.XPATH, "//a[@role='button']")
            if button:
                self.append_to_log("Button located. Starting user scraping.")
                page_source = self.driver.page_source
                usernames = set()  # Avoid duplicates
                for match in re.findall(r'\"username\":\"([a-zA-Z0-9_.]+)\"', page_source):
                    usernames.add(match)
                self.scraped_list = list(usernames)
                self.append_to_log(f"Scraped {len(self.scraped_list)} users successfully.")
        except TimeoutException:
            self.append_to_log("Error: Timeout while trying to locate element.")
        except NoSuchElementException:
            self.append_to_log("Error: Required element not found in page.")
        except Exception as e:
            self.append_to_log(f"Unexpected error occurred: {e}")

    def comment_on_posts(self, usernames):
        for user in usernames[:5]:  # Limit to first 5 for demo; adjust limit as needed
            self.append_to_log(f"Preparing to comment on user {user}'s profile page.")
            user_url = f"https://www.instagram.com/{user}/"
            try:
                self.driver.get(user_url)
                time.sleep(2)  # Adjust depending on page load speed

                comment_box = self.driver.find_element(By.XPATH, "//textarea")  # Replace with exact element locator
                random_comment = random.choice(["Nice post!", "Amazing content!", "Keep it up!"])
                comment_box.send_keys(random_comment)
                time.sleep(1)  # Adjust if needed for loading delays

                self.append_to_log(f"Commented '{random_comment}' on user {user}'s post.")
            except NoSuchElementException:
                self.append_to_log(f"Failed to comment on {user}: Comment box not found.")
            except Exception as e:
                self.append_to_log(f"Unexpected error while commenting on {user}: {e}")

    def safety_check(self):
        # Example check: stop function on certain bot criteria
        if self.comment_queue >= 100:
            self.append_to_log(f"Safety criteria met: Comment queue = {self.comment_queue}. Stopping bot.")
            return False
        return True

    def run_comment_function_five(self):
        self.setup_browser()
        self.advanced_comment_scrape = 0  # Example of starting scrape position
        # Demo data for scraping
        sample_post_url = "https://www.instagram.com/p/sample_post_id/?tagged=sample_keyword"
        keyword = "sample_keyword"

        self.scrape_target_user(sample_post_url, keyword)

        if self.scraped_list:
            self.append_to_log("Starting comment process for scraped users.")
            self.comment_on_posts(self.scraped_list)

        while self.safety_check():
            self.advanced_comment_scrape += 1
            new_sample_url = "https://www.instagram.com/p/another_post_id/?tagged=keyword2"
            self.scrape_target_user(new_sample_url, "keyword2")
            self.comment_on_posts(self.scraped_list)
            self.comment_queue += len(self.scraped_list)
            time.sleep(3)  # Simulate a delay between actions

        self.driver.quit()
        self.append_to_log("Bot session complete. Browser closed.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    DRIVER_PATH = "/path/to/geckodriver"  # Replace with your actual geckodriver path
    root = tk.Tk()
    bot = MultiCommentBot(DRIVER_PATH, root)
    bot.run()

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from datetime import datetime


class MultiCommentBot:
    def __init__(self, driver_path, enable_account_rotation="NO"):
        # Selenium setup
        options = FirefoxOptions()
        options.add_argument("--headless")  # Optional: Run browser in headless mode
        self.driver = webdriver.Firefox(service=FirefoxService(driver_path), options=options)

        # Tkinter setup
        self.root = tk.Tk()
        self.root.title("Multi Comment Bot")
        self.text_area = tk.Text(self.root, bg="#d9d9d9", wrap=tk.WORD, height=20, width=80)
        self.text_area.pack()

        # Other instance variables
        self.comment_color = "#d9d9d9"  # Default comment color
        self.keyword_file_pos = 0
        self.enable_account_rotation = enable_account_rotation
        self.time_format = "%Y-%m-%d %H:%M:%S"

    def get_time_stamp(self):
        """Generate a timestamp for logs."""
        return datetime.now().strftime(self.time_format)

    def append_to_log(self, message):
        """Append text to the UI log area."""
        timestamp = self.get_time_stamp()
        log_message = f"{timestamp} - {message}\n"
        self.text_area.insert(tk.END, log_message)
        self.text_area.see(tk.END)

    def run_javascript(self, script):
        """Execute JavaScript in the Selenium-controlled browser."""
        self.driver.execute_script(script)

    def multi_comment_function_six(self):
        """Translated functionality of $MultiCommentFunctionSix."""
        # Simulated comparison result for #keyword_file_pos with external function
        big_table_total_count = self.get_big_table_keyword_count()
        if self.keyword_file_pos >= big_table_total_count:
            self.append_to_log(
                "SOFTWARE RUNNING - KEYWORD FILE PROCESSING COMPLETE, RESETTING KEYWORD LIST BACK TO TOP OF LIST - COMMENT BOT - LOG RUNNING - INTERNALIZING COMPLETE")
            js_script = """
                var textarea = document.getElementById('textarea_id');
                textarea.value += "{time} - INTERNALIZING COMPLETE - {time}\\n";
                textarea.scrollTop = textarea.scrollHeight;
            """.replace("{time}", self.get_time_stamp())
            self.run_javascript(js_script)
            self.keyword_file_pos = 0

        # Update comment color globally
        self.comment_color = "#d9d9d9"

        # Check and apply account rotation
        if self.enable_account_rotation == "YES":
            self.run_succession_account_rotation()

    def get_big_table_keyword_count(self):
        """Simulated external plugin call to get the total keywords."""
        # Placeholder implementation, should be replaced with actual logic
        return 100

    def run_succession_account_rotation(self):
        """Simulated account rotation logic."""
        # Placeholder implementation for account rotation
        self.append_to_log("Succession Account Rotation executed.")

    def close_info_box(self):
        """Simulate closing an 'information box' in the UI."""
        # Placeholder implementation, can be tied to UI or web action
        self.append_to_log("InfoBox closed.")

    def run(self):
        """Main execution point for the bot."""
        self.append_to_log("Bot starting...")
        try:
            self.multi_comment_function_six()
        finally:
            self.append_to_log("Bot terminated.")


if __name__ == "__main__":
    DRIVER_PATH = "path_to_geckodriver"  # Replace with the actual path to GeckoDriver
    bot = MultiCommentBot(driver_path=DRIVER_PATH, enable_account_rotation="YES")
    bot.run()
    bot.root.mainloop()


