import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


# Functions and global settings
class MultiFollowFunctionTwo:
    def __init__(self):
        self.session_id = "unique_session_id"  # Example placeholder for session ID
        self.anti_cache = random.randint(1000, 9999)
        self.active_function = None
        self.follow_color = "#ffff00"
        self.follow_queue = 0
        self.ran_keyword = ""
        self.scrape_failed = 0
        self.loop_breakout = 0
        self.top_posts = "REMOVE"

        # Initialize Selenium WebDriver
        self.driver = webdriver.Firefox()  # Make sure geckodriver is installed and added to PATH

    # Simulate tracking HTTP requests
    def track_action(self):
        tracking_url = f"http://app.tracking.softwareautomation.org/appstats/piwik.php?idsite=1&rec=1&_id={self.session_id}&rand={self.anti_cache}&apiv=1&action_name=[Running Succession Module Function] Follow Function Activated&url=http://app.tracking.org"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"}

        # Example to simulate HTTP GET (Consider using requests library if needed)
        print(f"HTTP Tracking Request Sent: {tracking_url}")

    # Log messages to a UI textarea or console
    def log_message(self, message, textarea=None):
        current_time = time.strftime("%H:%M:%S")
        log_entry = f"{current_time} - {message}\n"
        print(log_entry)
        if textarea:
            textarea.insert(tk.END, log_entry)
            textarea.see(tk.END)

    # Random keyword generator
    def random_keyword(self):
        keywords = ["nature", "travel", "food", "technology", "art"]  # Placeholder list of keywords
        return random.choice(keywords)

    # Run the function core logic
    def run_follow_function_two(self, textarea=None):
        self.track_action()  # Simulate the tracking request

        # Log start of the process
        self.log_message("SOFTWARE RUNNING - CLEARING SCRAPE LIST, RESETTING QUEUE - FOLLOW BOT - LOG RUNNING",
                         textarea)
        self.follow_queue = 0
        self.ran_keyword = self.random_keyword()

        # Log selected keyword
        self.log_message(
            f"SOFTWARE RUNNING - THE BOT IS SEARCHING FOR THE KEYWORD [{self.ran_keyword}] - FOLLOW BOT - LOG RUNNING",
            textarea)

        # Navigate to Instagram Explore Tags page
        self.driver.get(f"https://www.instagram.com/explore/tags/{self.ran_keyword}/")

        try:
            # Wait for specific element to appear
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//span[@id="react-root"]/section/main/article/div[1]/h2'))
            )
        except Exception as e:
            self.log_message(f"Navigation failed or fallback needed: {str(e)}", textarea)
            self.scrape_failed += 1

        # Condition to handle top posts removal
        if self.top_posts == "REMOVE":
            self.log_message(
                "SOFTWARE RUNNING - REMOVE TOP POST OPTION SELECTED - REMOVING POPULAR POSTS - LOG RUNNING", textarea)
            try:
                top_posts_element = self.driver.find_element(By.XPATH,
                                                             '//span[@id="react-root"]/section/main/article/div[1]/div')
                self.driver.execute_script("arguments[0].innerText = '';", top_posts_element)
            except Exception as e:
                self.log_message(f"Failed to remove top posts: {str(e)}", textarea)

        self.scrape_failed = 0
        self.loop_breakout = 0

        # Log completion
        self.log_message("SOFTWARE RUNNING - INTERNALIZING COMPLETE", textarea)


# Tkinter-based UI
class AutomationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Automation Bot")
        self.geometry("700x400")

        # Textarea to display logs
        self.textarea = tk.Text(self, wrap=tk.WORD, bg="black", fg="white", font=("Courier", 10))
        self.textarea.pack(fill=tk.BOTH, expand=True)

        # Start button
        self.start_button = tk.Button(self, text="Start Follow Function", command=self.start_follow_function)
        self.start_button.pack(pady=10)

        # Initialize bot instance
        self.bot = MultiFollowFunctionTwo()

    def start_follow_function(self):
        # Disable button while running
        self.start_button.config(state=tk.DISABLED)
        self.bot.run_follow_function_two(self.textarea)
        self.start_button.config(state=tk.NORMAL)


# Run the application
if __name__ == "__main__":
    app = AutomationApp()
    app.mainloop()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import tkinter as tk
from datetime import datetime
import re


class MultiFollowFunctionThree:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Replace with the necessary WebDriver
        self.scrape_failed = 0
        self.loop_breakout = 0
        self.follow_queue = 0
        self.follow_per_tag = 10  # Example default value
        self.textarea_id = None

    def log_message(self, textarea, message: str):
        """Logs a message to the specified UI textarea."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        textarea.insert(tk.END, f"{timestamp} - {message}\n")
        textarea.see(tk.END)  # Scrolls down to the latest log

    def remove_duplicates(self, data: list) -> list:
        """Removes duplicates from a large list."""
        return list(set(data))

    def get_data_by_regex(self, content: str, regex: str) -> list:
        """Extract matches using regex from given content."""
        return re.findall(regex, content)

    def fetch_advanced_follow_scrape(self):
        """Simulates fetching data from the browser or an imaginary plugin."""
        # Example of scraping content; replace with actual scraping logic
        page_source = self.driver.page_source
        regex = r"(?!<a\shref=\"\/p\/)[A-Z_a-z0-9]{9,14}(?=\/\?tagged=)"
        scraped_data = self.get_data_by_regex(page_source, regex)
        return scraped_data

    def run_follow_function_three(self, textarea):
        """Main function that executes the 'follow bot' logic."""
        # Fetch data (simulate plugin command: ExBrowser Document Text)
        advanced_follow_scrape = self.fetch_advanced_follow_scrape()
        advanced_follow_scrape = self.remove_duplicates(advanced_follow_scrape)

        # Check conditions for loop breakout
        if len(advanced_follow_scrape) >= self.follow_per_tag + 10:
            self.log_message(textarea, "SOFTWARE RUNNING - FOLLOW BOT SCRAPE SUCCESS - TRIGGERING LOOP BREAKOUT")
            self.loop_breakout = 1
            return

        if len(advanced_follow_scrape) == 0:
            self.scrape_failed += 1
            if self.scrape_failed >= 3:
                self.log_message(textarea, "SOFTWARE RUNNING - FOLLOW BOT SCRAPE FAILED - TRIGGERING LOOP BREAKOUT")
                self.loop_breakout = 1
                return

        # Set follow queue and scroll the browser
        self.follow_queue = len(advanced_follow_scrape)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll the browser
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@id='react-root']/section/main/article/div[3]/div")
            )
        )

        # Check if follow scrape returned nothing
        if self.follow_queue == 0:
            self.app_list_scraping_failed(textarea)

    def app_list_scraping_failed(self, textarea):
        """Logs a message when app scraping fails."""
        self.log_message(textarea, "APP SCRAPING FAILED")


# Tkinter Application
class AutomationApp:
    def __init__(self, root):
        self.root = root
        self.bot = MultiFollowFunctionThree()
        self.textarea = None

        # Create TextArea for logging
        self.textarea = tk.Text(root, wrap=tk.WORD, height=15, width=60)
        self.textarea.pack()

        # Start Button to trigger function
        self.start_button = tk.Button(root, text="Start Follow Function", command=self.start_follow_function)
        self.start_button.pack()

    def start_follow_function(self):
        """Triggers the follow function and logs output."""
        if self.bot and self.textarea:
            self.bot.run_follow_function_three(self.textarea)


if __name__ == "__main__":
    # Tkinter app loop
    root = tk.Tk()
    root.title("Follow Bot Automation")
    app = AutomationApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


class MultiFollowFunctionFour:
    def __init__(self):
        self.follow_queue = 0
        self.follow_per_tag = 10
        self.browser = webdriver.Chrome()  # Use your preferred driver here
        self.randomized_list = []
        self.advanced_follow_scrape = []

    def log_message(self, message):
        # Assuming we are using a Tkinter textarea for logs
        textarea.insert(tk.END, message + "\n")
        textarea.see(tk.END)

    def randomize_list(self, input_list):
        self.log_message("Randomizing list...")
        self.randomized_list = random.sample(input_list, len(input_list))

    def remove_duplicates(self):
        self.log_message("Removing duplicates from randomized list...")
        unique_items = set()
        for item in self.randomized_list:
            if item not in unique_items:
                unique_items.add(item)
            else:
                self.randomized_list.remove(item)

    def process_advanced_follow_scrape(self):
        self.log_message("Processing advanced follow scrape...")
        total_items = len(self.advanced_follow_scrape)
        if total_items > self.follow_per_tag:
            while len(self.advanced_follow_scrape) != self.follow_per_tag:
                self.advanced_follow_scrape.pop(-1)  # Remove last item
                self.follow_queue = len(self.advanced_follow_scrape)

    def run_follow_function_four(self):
        self.log_message(f"{self.get_timestamp()} - SOFTWARE RUNNING - RANDOMIZE SCRAPED LIST OPTION SELECTED")

        # Process randomization
        if "YES" == "YES":  # Replace with actual condition
            self.randomize_list(self.advanced_follow_scrape)
            self.remove_duplicates()
            self.advanced_follow_scrape.extend(self.randomized_list)
            self.randomized_list.clear()

        # Prepare the follow queue
        self.process_advanced_follow_scrape()

        self.log_message(f"{self.get_timestamp()} - FOLLOW BOT SCRAPE QUEUE TOTAL = [{self.follow_queue}]")
        self.close_info_box()

    def get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def close_info_box(self):
        # Logic to close an info box (if applicable)
        self.log_message("Info box closed.")


class AutomationApp:
    def __init__(self, root):
        self.root = root
        self.textarea = None
        self.bot = MultiFollowFunctionFour()
        self.create_ui()

    def create_ui(self):
        self.root.title("Automation App")
        self.textarea = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.textarea.pack()

        self.start_button = tk.Button(self.root, text="Start Follow Function", command=self.start_follow_function)
        self.start_button.pack()

    def start_follow_function(self):
        self.bot.run_follow_function_four()


if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import re


class MultiFollowFunctionFive:
    def __init__(self, driver, textarea, follow_queue, follow_counter):
        self.driver = driver
        self.textarea = textarea
        self.follow_queue = follow_queue
        self.follow_counter = follow_counter
        self.adv_follow_scrape_pos = 0
        self.stop_bot_at = 0

    def log_message(self, message):
        current_time = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
        formatted_message = f"{current_time} - {message}\n"
        self.textarea.insert(tk.END, formatted_message)
        self.textarea.yview(tk.END)

    def navigate_to_post(self, post_id, keyword):
        url = f"https://www.instagram.com/p/{post_id}/?tagged={keyword}"
        self.log_message(f"SOFTWARE RUNNING - SENDING BROWSER REQUEST TO POST: [{post_id}] KEYWORD: [{keyword}].")
        self.driver.get(url)

    def wait_for_element(self, xpath, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            return False

    def follow_user(self, target_user):
        # Simulate pressing follow button
        self.log_message(f"SENDING FOLLOW REQUEST TO USER: [{target_user}]")
        follow_button = self.driver.find_element(By.XPATH, "//button[text()='Follow']")
        follow_button.click()

        # Wait to confirm follow succeeded
        for i in range(100):  # Wait loop breakout after 100 attempts
            time.sleep(0.1)
            if ">Following<" in self.driver.page_source:
                self.log_message(f"SOFTWARE HAS SUCCESSFULLY FOLLOWED THE USER: [{target_user}]")
                self.follow_queue -= 1
                self.follow_counter += 1
                return True
        self.log_message(f"FAILED TO FOLLOW USER: [{target_user}]")
        return False

    def fetch_user_list(self):
        page_source = self.driver.page_source
        user_list = re.findall(r"(?!\",\"username\":\")[A-Za-z.0-9_-]+(?=\",\"blocked)", page_source)
        return list(set(user_list))  # Remove duplicates

    def run_follow_function_five(self):
        # Example placeholders for generating a post ID and random keyword
        post_id = "sample_post_id"  # Replace with actual logic to fetch post_id
        keyword = "sample_keyword"  # Replace with actual logic to fetch random keyword

        self.navigate_to_post(post_id, keyword)
        if not self.wait_for_element("//a[@role='button']"):
            self.log_message("Failed to load post elements. Skipping this post...")
            return

        users_to_follow = self.fetch_user_list()
        for user in users_to_follow:
            if "Following" not in self.driver.page_source:
                self.follow_user(user)
                self.log_message(f"QUEUE AFTER ACTION COMPLETE TOTAL = [{self.follow_queue}]")
                self.log_message(f"FOLLOW BOT SESSION FOLLOWED USER TOTAL = [{self.follow_counter}]")
            else:
                self.log_message(f"ALREADY FOLLOWING USER: [{user}] - SKIPPING.")

            # Delay to avoid bot detection
            time.sleep(2)

            if self.follow_counter >= self.stop_bot_at:
                self.log_message("SOFTWARE STOPPED - FOLLOW BOT STOP CRITERIA MET.")
                return


class AutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automation App")
        self.textarea = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.textarea.pack(padx=10, pady=10)
        self.start_button = tk.Button(root, text="Start Follow Bot", command=self.start_follow_function)
        self.start_button.pack(pady=10)

        # Set up Selenium WebDriver
        self.driver = webdriver.Chrome()  # You can replace with the browser of your choice, e.g., Firefox
        self.bot = MultiFollowFunctionFive(self.driver, self.textarea, follow_queue=10, follow_counter=0)

    def start_follow_function(self):
        self.bot.run_follow_function_five()

    def close_app(self):
        self.driver.quit()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close_app)
    root.mainloop()

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import tkinter as tk


class MultiFollowFunctionSix:
    def __init__(self, driver, textarea):
        # Selenium WebDriver instance
        self.driver = driver
        # Tkinter Text Area element
        self.textarea = textarea
        # Global Variables
        self.keyword_file_pos = 0
        self.follow_color = "#d9d9d9"
        self.enable_account_rotation = "YES"

    def log_message(self, message: str):
        """Helper method to log messages into a Tkinter Text widget."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        full_message = f"{timestamp} - {message}\n"

        # Log into tkinter UI - Text area
        self.textarea.insert(tk.END, full_message)
        self.textarea.see(tk.END)  # Auto-scroll to the bottom

        # Optionally log to console
        print(full_message)

    def javascript_injection(self, js_code: str):
        """Run JavaScript code in Selenium's browser context."""
        self.driver.execute_script(js_code)

    def close_info_box(self):
        """
        A placeholder for the `CloseInfoBox` action that might close an info box in the UI.
        Implement Selenium logic for closing an info box here if applicable.
        """
        pass  # Add logic to find and close the notification/info box using Selenium.

    def run_follow_function_six(self):
        """Core logic for the function."""
        # Compare keyword_file_pos to an external function equivalent
        keyword_limit = self.get_large_list_total()  # Example method to get total keywords dynamically.

        # Check if keyword_file_pos exceeds or equals the keyword total
        if self.keyword_file_pos >= keyword_limit:
            self.log_message(
                "SOFTWARE RUNNING - KEYWORD FILE PROCESSING COMPLETE, RESETTING KEYWORD LIST BACK TO TOP OF LIST - FOLLOW BOT - LOG RUNNING - INTERNALIZING COMPLETE")

            # Reset keyword position
            self.keyword_file_pos = 0

            # Scroll text in textarea via JavaScript (mimicking the provided JavaScript behavior)
            js_code = (
                f"var textarea = document.getElementById('textarea_id');"
                f"textarea.value += \"{datetime.now()} - SOFTWARE RUNNING - KEYWORD FILE PROCESSING COMPLETE, RESETTING KEYWORD LIST BACK TO TOP OF LIST - FOLLOW BOT - LOG RUNNING - INTERNALIZING COMPLETE - {datetime.now()}\\n\";"
                f"textarea.scrollTop = textarea.scrollHeight;"
            )
            self.javascript_injection(js_code)

        # Update global variable follow_color
        self.follow_color = "#d9d9d9"

        # Check EnableAccountRotation and execute logic
        if self.enable_account_rotation == "YES":
            self.log_message("Executing account rotation...")
            self.run_succession_account_rotation()

        # Close the info box
        self.close_info_box()

    def get_large_list_total(self) -> int:
        """Placeholder for the external plugin function `Large list total`."""
        return 100  # Replace with actual logic as per your application's needs.

    def run_succession_account_rotation(self):
        """Placeholder for account rotation logic."""
        self.log_message("Account rotation function executed.")
        # Implement account rotation logic here
