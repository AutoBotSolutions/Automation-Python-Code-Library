import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
import time
import random


class MultiLikeApp:
    def __init__(self):
        self.driver = None
        self.like_queue = 0
        self.session_id = random.randint(1000, 9999)  # example session_id
        self.running_log = ""
        self.keyword_list = ["travel", "nature", "food", "fitness"]  # example keywords

        # Initialize the Tkinter UI
        self.root = tk.Tk()
        self.root.title("Instagram Auto-Like Bot")

        # Text area for logs
        self.log_area = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.log_area.pack(pady=10)

        # Start button
        self.start_button = tk.Button(self.root, text="Start Automation", command=self.run_like_function)
        self.start_button.pack(pady=5)

    def launch_browser(self):
        self.driver = webdriver.Chrome()  # Ensures ChromeDriver is installed & in PATH
        self.driver.maximize_window()

    def update_log(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {message}\n"
        self.running_log += log_entry
        self.log_area.insert(tk.END, log_entry)
        self.log_area.see(tk.END)

    def random_keyword(self):
        return random.choice(self.keyword_list)

    def navigate_to_hashtag(self, keyword):
        url = f"https://www.instagram.com/explore/tags/{keyword}/"
        self.driver.get(url)

    def remove_top_posts(self):
        try:
            # Locate the top posts container using XPath and attempt to remove/populate
            top_posts_container = self.driver.find_element(By.XPATH,
                                                           "//span[@id='react-root']/section/main/article/div[1]/div")
            self.driver.execute_script("arguments[0].innerText = '';", top_posts_container)
            self.update_log("Removed popular posts on user request.")
        except Exception as e:
            self.update_log(f"Error occurred while removing top posts: {e}")

    def automation_thread(self):
        self.launch_browser()

        # Step 1: Launch the browser and log activity
        self.update_log("SOFTWARE RUNNING. Clearing scrape list, resetting queue.")

        # Step 2: Select a random keyword
        random_keyword = self.random_keyword()
        self.update_log(f"Accessing hashtag: {random_keyword}")

        # Step 3: Navigate to Instagram tag page
        self.navigate_to_hashtag(random_keyword)

        # Wait for element
        time.sleep(3)  # Adjust time as necessary for waiting page to load

        # Attempt to remove popular posts if required
        self.remove_top_posts()

        # Additional actions would go here...
        self.update_log("Automation completed successfully.")

    def run_like_function(self):
        # Run the automation in a separate thread to avoid freezing the Tkinter UI
        threading.Thread(target=self.automation_thread, daemon=True).start()

    def run_ui(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MultiLikeApp()
    app.run_ui()

import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time
import random


class MultiLikeApp:
    def __init__(self):
        self.driver = None
        self.like_queue = 0
        self.scrape_failed_count = 0
        self.loop_breakout = False
        self.keyword_list = ["travel", "nature", "food", "fitness"]  # Example hashtags
        self.session_id = random.randint(1000, 9999)  # Random session identifier for logging

        # Initialize the Tkinter UI
        self.root = tk.Tk()
        self.root.title("Instagram Auto-Like Bot")
        self.log_area = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.log_area.pack(pady=10)
        self.start_button = tk.Button(self.root, text="Start Automation", command=self.run_like_function)
        self.start_button.pack(pady=5)

    def launch_browser(self):
        """Opens the browser for automation."""
        self.driver = webdriver.Chrome()  # Ensure that the ChromeDriver is installed and in PATH
        self.driver.maximize_window()

    def update_log(self, message):
        """Logs a message to the Tkinter log display."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {message}\n"
        self.log_area.insert(tk.END, log_entry)
        self.log_area.see(tk.END)

    def random_keyword(self):
        """Retrieve a random keyword from the keyword list."""
        return random.choice(self.keyword_list)

    def navigate_to_hashtag(self, keyword):
        """Directs the browser to an Instagram hashtag page."""
        url = f"https://www.instagram.com/explore/tags/{keyword}/"
        try:
            self.driver.get(url)
            self.update_log(f"Navigated to hashtag: {keyword}")
        except Exception as e:
            self.update_log(f"Error navigating to hashtag: {e}")

    def remove_duplicates(self, data_list):
        """Simulates removal of duplicate items from a list."""
        return list(set(data_list))

    def scroll_and_wait(self):
        """Scroll the page and wait for elements."""
        self.update_log("Scrolling through the page.")
        for _ in range(5):  # Simulate multiple scrolls
            self.driver.execute_script("window.scrollBy(0,1000);")
            time.sleep(2)

    def check_scrape_results(self):
        """Checks the results of the 'scrape' process."""
        try:
            total_items = self.simulate_scraping_data()  # Example simulated function
            if total_items >= self.like_queue + 10:
                self.update_log("Scrape successful. Exiting loop.")
                self.loop_breakout = True
            elif total_items == 0:
                self.scrape_failed_count += 1
                self.update_log(f"Scrape failed {self.scrape_failed_count} times.")
                if self.scrape_failed_count >= 3:
                    self.update_log("Scrape failed 3 times. Exiting loop.")
                    self.loop_breakout = True
        except Exception as e:
            self.update_log(f"Error during scrape evaluation: {e}")

    def simulate_scraping_data(self):
        """
        Simulates scrape data extraction.
        This is a stand-in for actual scrape data results provided in your snippet.
        """
        # Example: Random integer representing queue size
        return random.randint(0, 20)

    def automation_thread(self):
        """Executes the main automation workflow in a separate thread."""
        try:
            self.launch_browser()
            self.update_log("Browser launched. Starting automation.")

            # Select a random keyword
            keyword = self.random_keyword()
            self.navigate_to_hashtag(keyword)

            # Emulate scrape check
            self.check_scrape_results()

            while not self.loop_breakout:
                self.scroll_and_wait()
                self.check_scrape_results()

            # Finalize
            self.update_log("Automation complete. Closing browser.")
            self.driver.quit()

        except Exception as e:
            self.update_log(f"Error during automation: {e}")
            if self.driver:
                self.driver.quit()

    def run_like_function(self):
        """Starts the automation process in a separate thread."""
        threading.Thread(target=self.automation_thread, daemon=True).start()

    def run_ui(self):
        """Launches the Tkinter UI."""
        self.root.mainloop()


if __name__ == "__main__":
    app = MultiLikeApp()
    app.run_ui()

import random
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk, Text, Button, END


class MultiLikeApp:
    def __init__(self):
        self.driver = None
        self.log_area = None
        self.keyword_list = []
        self.like_queue = []
        self.root = Tk()
        self.running_log = ""
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("MultiLike Automation App")
        self.log_area = Text(self.root, height=20, width=80)
        self.log_area.pack(pady=10)

        self.start_button = Button(self.root, text="Start Automation", command=self.run_like_function)
        self.start_button.pack(pady=5)

    def update_log(self, message: str):
        """ Update the log area in the interface with a formatted message. """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - {message}\n"
        self.log_area.insert(END, log_message)
        self.log_area.see(END)

    def randomize_scraped_list(self):
        """ Randomize the order of the scraped keyword list. """
        self.update_log("Randomizing scraped keyword list...")
        random.shuffle(self.keyword_list)

    def prepare_like_queue(self):
        """ Prepare the like queue based on the maximum items allowed per tag. """
        max_items = 10  # Modify this as needed
        self.like_queue = self.keyword_list[:max_items]
        self.update_log(f"Prepared like queue with {len(self.like_queue)} items.")

    def run_like_function(self):
        """ Main automation functionality. """
        self.update_log("Starting like function...")

        randomize_option = True  # This can be configured in the UI later
        if randomize_option:
            self.randomize_scraped_list()

        self.prepare_like_queue()

        # Run the actual browser automation for each keyword
        for position, keyword in enumerate(self.like_queue):
            self.update_log(f"Processing keyword {position + 1}/{len(self.like_queue)}: {keyword}")
            try:
                self.navigate_to_hashtag(keyword)
                self.like_posts(position, keyword)
            except Exception as e:
                self.update_log(f"Error during processing '{keyword}': {e}")

        self.update_log("Like function completed!")

    def navigate_to_hashtag(self, hashtag: str):
        """ Navigate the browser to a specific hashtag page. """
        self.update_log(f"Navigating to hashtag: {hashtag}")
        url = f"https://www.instagram.com/explore/tags/{hashtag}/"
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//header"))
        )
        self.update_log(f"Successfully navigated to hashtag: {hashtag}")

    def like_posts(self, position: int, keyword: str):
        """ Like posts for a particular keyword. """
        self.update_log(f"Liking posts for keyword: {keyword}")

        # Simulate the process of liking posts - this can be adjusted based on the site's structure
        posts = self.driver.find_elements(By.XPATH, '//article/div/div/div/div/a')
        for post_index, post in enumerate(posts[:5]):  # Limit to the first 5 posts per keyword
            try:
                self.update_log(f"Liking post {post_index + 1}/5 for keyword: {keyword}")
                post.click()
                like_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//button//*[local-name()="svg" and @aria-label="Like"]'))
                )
                like_button.click()
                self.driver.back()  # Navigate back to the hashtag page
            except Exception as e:
                self.update_log(f"Error while liking post {post_index + 1}: {e}")

    def launch_browser(self):
        """ Launch the browser instance for automation. """
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.update_log("Browser launched successfully.")

    def run_ui(self):
        """ Run the Tkinter UI event loop. """
        self.root.mainloop()


if __name__ == "__main__":
    app = MultiLikeApp()
    app.launch_browser()
    app.run_ui()

import random
import time
from tkinter import Tk, Text, Button, Scrollbar, VERTICAL, END
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from threading import Thread


class MultiLikeApp:
    def __init__(self):
        self.driver = None
        self.root = Tk()
        self.root.title("Instagram Multi-Like Bot")

        # Log display in Tkinter
        self.log_area = Text(self.root, height=20, width=80)
        self.log_area.pack()
        self.scroll = Scrollbar(self.root, command=self.log_area.yview, orient=VERTICAL)
        self.scroll.pack(side='right', fill='y')
        self.log_area.config(yscrollcommand=self.scroll.set)

        # Start button
        self.start_button = Button(self.root, text="Start Automation", command=self.start_automation)
        self.start_button.pack()

        self.keyword_list = ["nature", "travel", "fitness"]  # Example keywords
        self.like_queue = []
        self.running_log = []

    def update_log(self, message):
        """Update the log area in the UI."""
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{current_time} - {message}"
        self.log_area.insert(END, log_message + '\n')
        self.log_area.see(END)
        print(log_message)  # For debugging/console log purposes

    def launch_browser(self):
        """Launch the Selenium browser driver."""
        try:
            self.update_log("Launching browser...")
            self.driver = webdriver.Chrome()  # Adjust this to use the correct WebDriver
            self.driver.maximize_window()
            self.update_log("Browser launched successfully.")
        except WebDriverException as e:
            self.update_log(f"Browser launch failed: {e}")

    def random_keyword(self):
        """Pick a random keyword from the list."""
        if self.keyword_list:
            return random.choice(self.keyword_list)
        return None

    def navigate_to_post(self, post_id, keyword):
        """Navigate to the Instagram post using post ID and keyword."""
        try:
            url = f"https://www.instagram.com/p/{post_id}/?tagged={keyword}"
            self.driver.get(url)
            self.update_log(f"Navigating to URL: {url}")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//a[@role='button']"))
            )
            self.update_log(f"Successfully loaded the post: {post_id}.")
        except TimeoutException:
            self.update_log(f"Error loading post with ID {post_id}.")
        except WebDriverException as e:
            self.update_log(f"Navigation failed: {e}")

    def like_posts(self, like_count):
        """Perform the like action on multiple posts."""
        for _ in range(like_count):
            try:
                self.update_log("Looking for the Like button.")
                like_button = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, "//button//*[local-name()='svg' and @aria-label='Like']"))
                )
                like_button.click()
                self.update_log("Post liked successfully.")
                time.sleep(random.randint(2, 4))  # Simulate delay for human behavior
            except TimeoutException:
                self.update_log("Like button not found or already liked.")
            except Exception as e:
                self.update_log(f"Error during liking posts: {e}")

    def start_automation(self):
        """Begin the automation thread."""
        try:
            self.update_log("Starting automation thread...")
            Thread(target=self.automation_thread).start()
        except Exception as e:
            self.update_log(f"Error starting automation: {e}")

    def automation_thread(self):
        """Thread for running automation tasks."""
        self.launch_browser()
        keyword = self.random_keyword()  # Pick a random keyword
        if keyword:
            post_id = "examplePostId"  # Replace with actual dynamic ID fetching
            self.navigate_to_post(post_id, keyword)
            self.like_posts(like_count=3)

        self.update_log("Automation thread finished.")

    def run_ui(self):
        """Run the Tkinter main loop."""
        self.update_log("UI initialized. Ready to start.")
        self.root.mainloop()


# Main Execution
if __name__ == "__main__":
    app = MultiLikeApp()
    app.run_ui()

import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import threading


class MultiLikeApp:
    def __init__(self):
        # Initializing the root window
        self.root = tk.Tk()
        self.root.title("MultiLike Bot")
        self.root.geometry("800x600")

        # Setting application variables
        self.keyword_list = []
        self.like_queue = []
        self.keyword_file_pos = 0
        self.enable_account_rotation = True
        self.running_log = []
        self.driver = None

        # Creating UI components
        self.initialize_ui()

    def initialize_ui(self):
        # Start button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_automation)
        self.start_button.pack(pady=10)

        # Log area
        self.log_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=100, height=20)
        self.log_area.pack(pady=10)

    def update_log(self, message):
        """Update log area with timestamped messages."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} - {message}\n"
        self.running_log.append(log_message)
        self.log_area.insert(tk.END, log_message)
        self.log_area.see(tk.END)

    def launch_browser(self):
        """Launch the web browser using Selenium."""
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.update_log("Browser launched successfully.")

    def reset_keyword_position(self):
        """Reset keyword file position if processing is complete."""
        self.update_log("Keyword file processing complete. Resetting keyword list back to top.")
        self.keyword_file_pos = 0

    def run_like_function(self):
        """Perform the 'Like' functionality using Selenium."""
        if self.keyword_file_pos >= len(self.keyword_list):  # Check if the position exceeds list length
            self.reset_keyword_position()

        # Get the current keyword to process
        keyword = self.keyword_list[self.keyword_file_pos]
        self.update_log(f"Processing keyword: {keyword}")

        try:
            # Navigate to a hashtag or keyword URL
            url = f"https://www.example.com/hashtag/{keyword}"
            self.driver.get(url)
            self.update_log(f"Navigated to: {url}")

            # Simulate some 'Like' actions
            like_buttons = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "like-button"))
            )
            for button in like_buttons:
                button.click()
                self.update_log("Post liked.")

        except Exception as e:
            self.update_log(f"Error during liking process: {e}")
        finally:
            # Increment the file position for next iteration
            self.keyword_file_pos += 1

    def handle_account_rotation(self):
        """Rotate to the next account if the setting is enabled."""
        if self.enable_account_rotation:
            self.update_log("Rotating accounts... (Placeholder for account rotation logic)")

    def close_browser(self):
        """Close the browser and clean up Selenium driver."""
        if self.driver:
            self.driver.quit()
            self.update_log("Browser closed.")

    def start_automation(self):
        """Start the automation process."""
        self.update_log("Automation process started.")

        # Launch browser
        self.launch_browser()

        # Run automation in background thread to avoid UI freezing
        threading.Thread(target=self.automation_thread, daemon=True).start()

    def automation_thread(self):
        """Run the main automation process."""
        try:
            while True:
                self.run_like_function()  # Execute the like function
                self.handle_account_rotation()  # Perform any account rotation logic (if needed)
        except Exception as e:
            self.update_log(f"Automation stopped due to: {e}")
        finally:
            self.close_browser()

    def run_ui(self):
        """Start the Tkinter UI."""
        self.root.protocol("WM_DELETE_WINDOW", self.close_browser)  # Ensure browser closes on exit
        self.root.mainloop()


# Main function to initialize and run the app
if __name__ == "__main__":
    app = MultiLikeApp()
    app.run_ui()
