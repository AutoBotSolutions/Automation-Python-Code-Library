import tkinter as tk
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class FollowingFollowersScrapeOne:
    def __init__(self, root):
        # Initialize the browser driver
        self.driver = webdriver.Chrome()  # Make sure to have ChromeDriver installed and PATH configured

        # Initialize Tkinter UI
        self.root = root
        self.root.title("Instagram Scrape Tool")

        self.text_area = tk.Text(root, height=15, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.options_var = tk.StringVar()
        self.options_var.set("Select Option")

        self.options_menu = tk.OptionMenu(root, self.options_var, "Scrape Users Followers", "Scrape Users Following")
        self.options_menu.pack(pady=5)

        self.username_label = tk.Label(root, text="Enter Target Username:")
        self.username_label.pack(pady=5)

        self.username_entry = tk.Entry(root, width=30)
        self.username_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Scrape", command=self.run_scraper)
        self.start_button.pack(pady=10)

    def log_message(self, message_content):
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.text_area.insert(tk.END, f"{log_time} - {message_content}\n")
        self.text_area.see(tk.END)

    def navigate_to_user(self, username):
        url = f"https://www.instagram.com/{username}/"
        self.driver.get(url)
        self.log_message(f"BROWSER REQUEST SENT TO USER: [{username}]")
        self.driver.implicitly_wait(5)

    def click_element(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element.click()
            return True
        except Exception as e:
            self.log_message(f"Error: Unable to interact with element: {xpath}. Error: {str(e)}")
            return False

    def scrape_followers(self, username):
        self.navigate_to_user(username)

        if self.click_element('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'):
            self.log_message("Followers option clicked, scraping followers started.")
        else:
            self.log_message("Failed to click on Followers link.")

    def scrape_following(self, username):
        self.navigate_to_user(username)

        if self.click_element('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'):
            self.log_message("Following option clicked, scraping following started.")
        else:
            self.log_message("Failed to click on Following link.")

    def run_scraper(self):
        self.log_message("SOFTWARE RUNNING")

        username = self.username_entry.get().strip()
        if not username:
            self.log_message("Error: No Instagram username provided.")
            return

        scrape_option = self.options_var.get()
        if scrape_option == "Scrape Users Followers":
            self.log_message("Selected option: Scrape Users Followers")
            self.scrape_followers(username)
        elif scrape_option == "Scrape Users Following":
            self.log_message("Selected option: Scrape Users Following")
            self.scrape_following(username)
        else:
            self.log_message("Error: Please select a valid scrape option.")
            return

        # Add further functionalities based on your scraper logic

    def cleanup(self):
        self.driver.quit()


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = FollowingFollowersScrapeOne(root)
    root.protocol("WM_DELETE_WINDOW", app.cleanup)  # Ensure the driver quits on close
    root.mainloop()

class FollowingFollowersScrapeTwo:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def wait_for_element_enabled(self, xpath, timeout=5):
        """
        Wait for an element to be enabled on the page.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath))
            )
            self.logger("Waited for element to be enabled: " + xpath)
        except Exception as e:
            self.logger(f"Error: Timed out waiting for element. {str(e)}")

    def gather_users(self):
        """
        Scrape followers or following by extracting usernames.
        """
        user_list = set()  # Use a set to ensure uniqueness
        for _ in range(13):  # Repeat the scraping action 13 times, as per your logic
            try:
                # Collect the document HTML text
                page_html = self.driver.page_source
                # Extract the usernames using regex
                usernames = re.findall(r'(?!\"\shref=\"\\/)[a-z.0-9_]+(?=\\/\"\sstyle=\"width:\s30px;)', page_html)
                user_list.update(usernames)  # Add to the set to avoid duplicates

                # Clear the inner text of elements to scroll to more users
                elements = self.driver.find_elements(By.XPATH,
                                                     "x://html/body/div[3]/div/div[2]/div/div[2]/ul/div/li[*]")
                for element in elements:
                    self.driver.execute_script("arguments[0].innerText=''", element)

                # Scroll to load more elements
                scroll_target = self.driver.find_element(By.XPATH, "//*[@style='width: 30px; height: 30px;']")
                self.driver.execute_script("arguments[0].scrollIntoView();", scroll_target)

                time.sleep(1)  # Allow some time for the next batch of users to load
            except Exception as e:
                self.logger(f"Error during user collection step: {str(e)}")

        return list(user_list)

    def scrape(self, username):
        """
        Main function to scrape followers or following.
        """
        try:
            # Navigate to the user's followers/following page
            self.navigate_to_user(username)
            self.wait_for_element_enabled("x://html/body/div[3]/div/div[2]/div/div[2]/ul/div/li[*]")

            # Gather followers/following
            scraped_users = self.gather_users()

            # Remove duplicates and count the total scraped users
            total_users = len(scraped_users)
            # Log the successful scrape
            self.logger(
                f"Scrape completed. Target [{username}] Total Users Scraped: {total_users}"
            )

            # Return the scraped list
            return scraped_users
        except Exception as e:
            self.logger(f"Error in scrape process: {str(e)}")
            return []

    def log_message_in_ui(self, message):
        """
        Log a message into the connected Tkinter Text widget/log area.
        """
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logger.insert(tk.END, f"{log_time} - {message}\n")
        self.logger.see(tk.END)

    def run_scraper(self, username):
        """
        Perform the entire scrape routine for a given user.
        """
        self.logger("Starting scrape process...")
        scraped_users = self.scrape(username)

        # Show a log message in UI
        self.log_message_in_ui(f"Scrape complete. Total users scraped: {len(scraped_users)}")
        return scraped_users

    def navigate_to_user(self, username):
        """
        Navigate to a user's Instagram page.
        """
        url = f"https://www.instagram.com/{username}/"
        self.driver.get(url)
        self.logger(f"BROWSER SENT TO: {url}")


# Main Tkinter connection example for the UI
if __name__ == "__main__":
    def logger(message):
        print(message)  # A placeholder logger function


    # Example usage
    root = tk.Tk()
    root.title("Instagram Scrape Tool - Following & Followers")
    text_area = tk.Text(root, height=15, wrap=tk.WORD)
    text_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    # Initialize a Selenium driver
    driver = webdriver.Chrome(executable_path="<PATH_TO_CHROME_DRIVER>")

    # Create an instance of FollowingFollowersScrapeTwo
    scraper = FollowingFollowersScrapeTwo(driver, logger=text_area)

    # Run a scrape (replace USERNAME with the actual username)
    scraper.run_scraper("USERNAME")


    # Clean up Selenium driver when closing
    def on_close():
        scraper.driver.quit()
        root.destroy()


    # Attach close protocol
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

import os
import datetime
from tkinter import Tk, Text, Scrollbar, END
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FollowingFollowersScrapeThree:
    def __init__(self, driver, text_area, target_username):
        self.driver = driver
        self.text_area = text_area
        self.target_username = target_username
        self.scrape_data_folder = os.path.join(os.path.expanduser("~"), "Desktop", "ScrapeData")
        self.scraped_file_path = os.path.join(self.scrape_data_folder, f"[{self.target_username}].txt")

        # Ensure the ScrapeData folder exists
        os.makedirs(self.scrape_data_folder, exist_ok=True)

    def save_to_file(self, data):
        # Saves scraped data to file
        with open(self.scraped_file_path, 'w') as file:
            file.writelines(data)

    def log_message_in_ui(self, message):
        """Logs a message to the UI text area."""
        if self.text_area:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            full_message = f"{timestamp} - {message}\n"
            self.text_area.insert(END, full_message)
            self.text_area.see(END)

    def scrape_users(self):
        # Simulates the plugin `Large list return` function for scraping
        users = ["user1", "user2", "user3"]  # Mocked data, replace with actual scraping logic
        return users

    def scrape_user_count(self):
        # Simulates the plugin `Large list total` function
        return len(self.scrape_users())

    def clear_scraped_data(self):
        """Simulates the function 'Clear large list' in the plugin."""
        # Any cleanup code or resetting variables related to the data collected
        pass

    def run(self):
        try:
            # Scrape users and save to file
            scraped_users = self.scrape_users()
            self.save_to_file([user + "\n" for user in scraped_users])

            # Log saved output
            self.log_message_in_ui(
                f"SOFTWARE RUNNING - LIST AUTO TRANSFERRED TO TARGET MODULE - LOG RUNNING - INTERNALIZING COMPLETE")
            self.log_message_in_ui(f"SCRAPED LIST SAVED OUTPUT TO [Desktop\\ScrapeData\\[{self.target_username}].txt]")

            # Check if the scraped list is empty
            if self.scrape_user_count() == 0:
                # Log failure and handle the behavior
                self.log_message_in_ui("LIST SCRAPING FAILED - NO USERS FOUND")
            else:
                self.log_message_in_ui("SCRAPING COMPLETED SUCCESSFULLY")

            # Clear the data once done
            self.clear_scraped_data()
        except Exception as e:
            self.log_message_in_ui(f"An error occurred: {str(e)}")


# Example for Tkinter GUI integration
def main():
    # Create the main Tkinter application
    root = Tk()
    root.title("Following/Followers Scraper")
    root.geometry("600x400")

    # Text area for logging
    text_area = Text(root, wrap="word", height=15, width=70)
    text_area.pack(pady=10)

    # Add a scrollbar
    scrollbar = Scrollbar(root, command=text_area.yview)
    scrollbar.pack(side="right", fill="y")
    text_area['yscrollcommand'] = scrollbar.set

    # Setup Selenium driver (adjust as necessary)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Optional: Run in headless mode
    driver = webdriver.Chrome(options=options)

    # Initialize the scraper
    username = "TargetUsername"  # Replace with actual username entry from the UI
    scraper = FollowingFollowersScrapeThree(driver, text_area, username)

    # Run the scraper
    scraper.run()

    # tkinter loop
    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
from datetime import datetime


class CommentersCommentScrapeOne:
    def __init__(self, root, driver, text_area):
        self.root = root
        self.driver = driver
        self.text_area = text_area
        self.scrape_comment_options = tk.StringVar()
        self.scrape_comm_tag = ''
        self.top_posts = tk.StringVar()

    def log_message(self, message):
        """Logs a message to the Text widget in the UI."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{current_time} - {message}\n"
        self.text_area.insert(tk.END, formatted_message)
        self.text_area.see(tk.END)

    def run_app_running_module(self):
        """Simulates an app running module."""
        self.log_message("App Running Module Activated.")

    def send_tracking_request(self, action_name):
        """Simulates an external tracking action."""
        self.log_message(f"Tracking: {action_name}")

    def navigate_to_tag(self):
        """Navigates to the specific Instagram tag."""
        url = f"https://www.instagram.com/explore/tags/{self.scrape_comm_tag}/"
        self.log_message(f"Navigating to tag: {url}")
        try:
            self.driver.get(url)
            wait = WebDriverWait(self.driver, 5)
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='react-root']/section/main/article/div[1]/h2")
                )
            )
        except Exception as e:
            self.log_message(f"Error navigating to tag: {e}")

    def remove_top_posts(self):
        """Handles removing top posts if configured to do so."""
        if self.top_posts.get().upper() == "REMOVE":
            self.log_message("Removing Top Posts as per configuration.")
            try:
                element = self.driver.find_element(
                    By.XPATH, "//div[@id='react-root']/section/main/article/div[1]/div"
                )
                self.driver.execute_script("arguments[0].innerText = '';", element)
            except Exception as e:
                self.log_message(f"Error removing top posts: {e}")

    def scrape_process(self):
        """Main scraping logic."""
        self.log_message("Scraping process started.")
        self.navigate_to_tag()
        self.remove_top_posts()
        self.log_message("Scraping process completed.")

    def start_scrape(self):
        """Starts the scrape process based on user selection."""
        self.scrape_comm_tag = self.scrape_comm_tag.replace("#", "")
        self.log_message(f"Scrape Comm Tag processed: {self.scrape_comm_tag}")

        def thread_task():
            self.run_app_running_module()
            self.send_tracking_request(
                "Scrape Commenter's Function Activated"
                if self.scrape_comment_options.get() == "Scrape Commenters"
                else "Scrape Comments Function Activated"
            )
            self.scrape_process()

        self.log_message("Starting scraper thread.")
        Thread(target=thread_task).start()


# Example of integrating the above class with a Tkinter UI
def main():
    # Initialize Tkinter UI
    root = tk.Tk()
    root.title("Instagram Scraper")
    root.geometry("800x600")

    # Text widget for logging
    text_area = tk.Text(root, wrap=tk.WORD, height=20)
    text_area.pack(fill=tk.BOTH, expand=True)

    # WebDriver setup (replace ChromeDriver path as necessary)
    driver = webdriver.Chrome()  # Or another WebDriver instance like Firefox()

    # Create the scraper instance
    scraper = CommentersCommentScrapeOne(root, driver, text_area)

    # Add Tkinter options
    options_label = tk.Label(root, text="Scrape Options:")
    options_label.pack()

    scrape_options_menu = tk.OptionMenu(
        root, scraper.scrape_comment_options, "Scrape Commenters", "Scrape Comments"
    )
    scrape_options_menu.pack()

    # Entry for tag
    tag_label = tk.Label(root, text="Enter Tag:")
    tag_label.pack()

    tag_entry = tk.Entry(root, textvariable=tk.StringVar())
    tag_entry.pack()

    def start_scraper():
        scraper.scrape_comm_tag = tag_entry.get()
        scraper.start_scrape()

    # Start button
    start_button = tk.Button(root, text="Start Scraping", command=start_scraper)
    start_button.pack()

    # Mainloop
    root.protocol("WM_DELETE_WINDOW", lambda: on_close(driver, root))
    root.mainloop()


def on_close(driver, root):
    """Cleanup on closing the application."""
    driver.quit()
    root.destroy()


if __name__ == "__main__":
    main()

import re
import time
from tkinter import Tk, Text
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommentersCommentScrapeTwo:
    def __init__(self):
        # Browser setup
        service = Service("path_to_chromedriver")  # Replace with actual path to chromedriver
        self.driver = webdriver.Chrome(service=service)

        # Tkinter setup
        self.root = Tk()
        self.root.title("Commenters Comment Scraper")
        self.text_area = Text(self.root, wrap="word", height=20, width=80)
        self.text_area.pack()

        self.scrape_users = set()
        self.scrape_comment_queue = 0

    def run_javascript_in_ui(self, message):
        """Logs a message into the Tkinter UI and scrolls the UI."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.text_area.insert("end", f"{timestamp} - {message.strip()}\n")
        self.text_area.see("end")
        self.root.update()

    def scroll_browser(self, scroll_x, scroll_y):
        """Scrolls the browser window by the specified pixel amounts."""
        self.driver.execute_script(f"window.scrollBy({scroll_x}, {scroll_y});")

    def wait_for_element(self, xpath, condition="appear", timeout=3):
        """
        Waits for a specific HTML element to appear or disappear based on the condition.
        :param xpath: The element's locator (XPath).
        :param condition: 'appear' or 'disappear' to define when to stop waiting.
        :param timeout: Maximum time to wait in seconds.
        """
        try:
            if condition.lower() == "appear":
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
            elif condition.lower() == "disappear":
                WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located((By.XPATH, xpath)))
        except Exception as e:
            self.run_javascript_in_ui(f"Error: {str(e)}")

    def scrape_users_from_text(self, document_text):
        """
        Scrapes usernames matching the regex from the provided document text using a set to prevent duplicates.
        """
        regex_pattern = r"(?!<a\shref=\"\/p\/)[A-Z_a-z0-9]{9,14}(?=\/\?tagged=)"
        results = re.findall(regex_pattern, document_text)
        self.scrape_users.update(results)
        self.scrape_comment_queue = len(self.scrape_users)

    def execute_scrape_process(self):
        """Main scraper logic."""
        self.run_javascript_in_ui("SOFTWARE RUNNING - STARTING SCRAPE PROCESS...")

        # Simulate scraping document text (replace this with actual Selenium extraction logic)
        document_text = self.driver.execute_script("return document.body.textContent")
        self.scrape_users_from_text(document_text)

        # Log the size of the scrape queue
        self.run_javascript_in_ui(
            f"ITEMS SCRAPED TO LIST = [{self.scrape_comment_queue}] - LOG RUNNING - INTERNALIZING COMPLETE"
        )

        # Scroll down the page
        self.scroll_browser(0, 10000)
        time.sleep(1)

        # Wait for specific content in the DOM
        self.wait_for_element("x://span[@id='react-root']/section/main/article/div[3]/div")

    def start(self):
        """Starts the scraper."""
        try:
            self.run_javascript_in_ui("SOFTWARE INITIALIZED - READY TO RUN")
            self.execute_scrape_process()
        except Exception as e:
            self.run_javascript_in_ui(f"Error encountered: {e}")
        finally:
            self.driver.quit()
            self.root.mainloop()


if __name__ == "__main__":
    app = CommentersCommentScrapeTwo()
    app.start()

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommentersCommentScrapeThree:
    def __init__(self):
        # Initialize global variables
        self.scrape_comment_queue = 0
        self.scrape_users_pos = 0

        # Initialize attributes for UI and Selenium
        self.root = tk.Tk()  # tkinter UI root if needed
        self.driver = None  # Selenium WebDriver instance
        self.target_user = []  # To mimic clearing "target_user" list
        self.comment_scrape = []  # To mimic clearing "comment_scrape" list

        # Setup UI or Selenium-related elements as necessary
        self.setup_ui()

    def setup_ui(self):
        """Setup tkinter UI for the component."""
        self.root.title("Comment Scraper")
        text_area = tk.Text(self.root, height=10, width=50)
        text_area.pack()

    def clear_lists(self):
        """Clear the lists equivalent to plugin command (Bigtable.dll)."""
        self.target_user.clear()
        self.comment_scrape.clear()
        self.scrape_comment_queue = 0
        self.scrape_users_pos = 0

    def initialize_webdriver(self):
        """Initialize Selenium WebDriver."""
        self.driver = webdriver.Chrome()  # Example: using Chrome WebDriver
        self.driver.maximize_window()

    def run(self):
        """Main method to execute the scraping logic."""
        try:
            self.clear_lists()  # Clear necessary data
            # Additional scraping logic would go here
        finally:
            self.cleanup()

    def cleanup(self):
        """Cleanup resources before exit."""
        if self.driver:
            self.driver.quit()
        self.root.destroy()


if __name__ == "__main__":
    app = CommentersCommentScrapeThree()
    app.run()
    tk.mainloop()

import os
import re
import time
from datetime import datetime
from tkinter import Tk, Text, Button, END
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CommentersCommentScrapeFour:
    def __init__(self, root):
        self.root = root
        self.driver = webdriver.Chrome()  # Ensure you have installed the WebDriver for the browser of your choice
        self.text_area = Text(self.root, height=20, width=80)
        self.text_area.pack()
        self.scrape_comm_tag = "example_tag"  # Replace with your selected tag
        self.scrape_comment_options = "Scrape Commenters"  # Or "Scrape Comments"
        self.scrape_users_position = 0
        self.master_delay_trigger = 0
        self.number_to_scrape = 100  # Adjust as needed
        self.run_delay_after = 5
        self.scrape_data_folder = os.path.join(os.path.expanduser("~"), "Desktop", "ScrapeData")
        if not os.path.exists(self.scrape_data_folder):
            os.makedirs(self.scrape_data_folder)

    def log_message(self, message):
        """Log messages to the UI."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.text_area.insert(END, f"{timestamp} - {message}\n")
        self.text_area.see(END)

    def wait_for_element(self, timeout, condition):
        """Wait for a specific element to appear."""
        try:
            WebDriverWait(self.driver, timeout).until(condition)
        except TimeoutException:
            self.log_message("Timeout while waiting for element.")

    def start_scrape(self):
        """Main scraper logic."""
        target_url = f"https://www.instagram.com/p/{self.scrape_users_position}/?tagged={self.scrape_comm_tag}"
        self.driver.get(target_url)

        # Wait for the ellipsis to confirm page loading
        wait_breakout = 0
        while True:
            if "coreSpriteOptionsEllipsis" in self.driver.page_source:
                break
            time.sleep(0.1)
            wait_breakout += 1
            if wait_breakout > 100:
                self.log_message("Ellipsis not found in page source. Breaking wait.")
                break

        if self.scrape_comment_options == "Scrape Commenters":
            self.scrape_commenters()
        elif self.scrape_comment_options == "Scrape Comments":
            self.scrape_comments()

        self.after_scrape_check()

    def scrape_commenters(self):
        """Scrape commenter usernames."""
        self.log_message("Started scraping commenters.")
        regex_pattern = r"(?!\",\"username\":\")[a-z.0-9_]+(?=\"\}\}\})"
        users = re.findall(regex_pattern, self.driver.page_source)
        users = list(set(users))

        if users:
            file_path = os.path.join(self.scrape_data_folder, f"[{self.scrape_comm_tag}] Commenters.txt")
            with open(file_path, 'w') as file:
                file.write("\n".join(users))

            self.log_message(f"Users scraped to list. Total: {len(users)}")
        else:
            self.log_message("No users found to scrape.")

    def scrape_comments(self):
        """Scrape comments."""
        self.log_message("Started scraping comments.")
        regex_patterns = [
            r"(?!<span>)[a-zA-Z!@#$%^&*()0-9\s+]+(?=(?:\uD83C[\uDF00-\uDFFF])|(?:\uD83D[\uDC00-\uDDFF])<\/span>)",
            r"(?!<span><span>)[a-zA-Z!@#$%^&*()0-9\s+]+(?=<\/span><\/span>)"
        ]
        comments = []
        for pattern in regex_patterns:
            comments.extend(re.findall(pattern, self.driver.page_source))

        comments = list(set(comments))

        if comments:
            file_path = os.path.join(self.scrape_data_folder, f"[{self.scrape_comm_tag}] Comments.txt")
            with open(file_path, 'w') as file:
                file.write("\n".join(comments))

            self.log_message(f"Comments scraped to list. Total: {len(comments)}")
        else:
            self.log_message("No comments found to scrape.")

    def after_scrape_check(self):
        """Verify if the scraping goal is met."""
        if self.scrape_comment_options == "Scrape Comments" or self.scrape_comment_options == "Scrape Commenters":
            scraped_count = len(os.listdir(self.scrape_data_folder))
            if scraped_count >= self.number_to_scrape:
                self.log_message("Scraping goal met. Stopping the script.")
                return

        self.scrape_users_position += 1
        time.sleep(self.run_delay_after)
        self.start_scrape()

    def cleanup(self):
        """Clean up resources."""
        self.log_message("Cleaning up resources.")
        self.driver.quit()


if __name__ == "__main__":
    app = Tk()
    app.title("Instagram Scraper")
    scraper = CommentersCommentScrapeFour(app)

    start_button = Button(app, text="Start Scraping", command=scraper.start_scrape)
    start_button.pack()

    app.protocol("WM_DELETE_WINDOW", scraper.cleanup)
    app.mainloop()

import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time
import requests


class ScrapeGeoLocationOne:
    def __init__(self, driver, root, text_area, geo_location):
        self.driver = driver
        self.root = root
        self.text_area = text_area
        self.geo_location = geo_location
        self.delay_ticker = 0
        self.geo_location_queue = 0
        self.master_delay_trigger = 0
        self.top_posts_option = None

    def log_message(self, message):
        """Log messages to the UI text area with timestamp"""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.text_area.insert(tk.END, f"{timestamp} - {message}\n")
        self.text_area.see(tk.END)

    def send_tracking_request(self):
        """Send tracking request"""
        session_id = "example_session"  # Replace with your session ID
        anti_cache = str(time.time())
        tracking_url = f"http://app.tracking.softwareautomation.org/appstats/piwik.php?" \
                       f"&idsite=1&rec=1&_id={session_id}&rand={anti_cache}&apiv=1" \
                       f"&action_name=[Running Scrape Module Function] Scrape GeoLocation Function Activated" \
                       f"&url=http://app.tracking.org"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"
        }
        requests.get(tracking_url, headers=headers)

    def navigate_to_geolocation(self):
        """Navigate the browser to the geolocation page"""
        try:
            current_url = self.driver.current_url
            if self.geo_location not in current_url:
                self.driver.get(f"https://www.instagram.com/explore/locations/{self.geo_location}")
                self.log_message("Navigated to geolocation page. Please select your target city.")
        except Exception as e:
            self.log_message(f"Error navigating to geolocation page: {str(e)}")

    def wait_for_element_or_text(self, condition, description, wait_time=0.1):
        """Wait for a specific condition to be met in the document"""
        while not condition():
            time.sleep(wait_time)
        self.log_message(description)

    def scrape_geolocation(self):
        """Main logic to perform geolocation scraping"""
        threading.Thread(target=self.send_tracking_request).start()
        self.log_message("SOFTWARE RUNNING - GEOLOCATION TARGETING STARTED - LOG RUNNING")

        # Clear previous data
        self.delay_ticker = 0
        self.geo_location_queue = 0
        self.master_delay_trigger = 0

        # Navigate to the Geolocation page
        self.navigate_to_geolocation()

        # Wait for "Cities" text to disappear
        self.wait_for_element_or_text(
            lambda: "Cities" not in self.driver.page_source,
            "PLEASE SELECT YOUR TARGET LOCATION FROM THE PAGE"
        )

        # Wait for "Locations in" text if present
        if "Locations in" in self.driver.page_source:
            self.wait_for_element_or_text(
                lambda: "Locations in" not in self.driver.page_source,
                "PLEASE SELECT YOUR TARGET LOCATION FROM THE PAGE"
            )

        # Make sure "Top posts" appear before proceeding
        self.wait_for_element_or_text(
            lambda: "Top posts" in self.driver.page_source,
            "TARGET LOCATION SCRAPING PROCESS HAS BEGUN"
        )

        # Handle removal of "Top posts" if requested
        if self.top_posts_option == "REMOVE":
            self.log_message("REMOVE TOP POST OPTION SELECTED - REMOVING POPULAR POSTS")
            try:
                top_posts_element = self.driver.find_element(By.XPATH,
                                                             '//*[@id="react-root"]/section/main/article/div[1]/div')
                self.driver.execute_script("arguments[0].innerHTML = '';", top_posts_element)
                self.log_message("Removed 'Top posts'")
            except Exception as e:
                self.log_message(f"Error removing 'Top posts': {str(e)}")

        # Play an alert sound
        self.root.bell()

    def start_scraper(self):
        """Start the scraper in its own thread"""
        threading.Thread(target=self.scrape_geolocation).start()


# Main Application with Tkinter
class GeoLocationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GeoLocation Scraper")
        self.driver = None
        self.initialize_ui()

    def initialize_ui(self):
        """Set up the UI"""
        self.text_area = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.text_area.pack(padx=10, pady=10)

        start_button = tk.Button(self.root, text="Start Scraper", command=self.start_scraper)
        start_button.pack(pady=10)

    def start_scraper(self):
        """Initialize WebDriver and start the scraper"""
        if not self.driver:
            self.driver = webdriver.Chrome()  # Configure your WebDriver
        scraper = ScrapeGeoLocationOne(
            driver=self.driver,
            root=self.root,
            text_area=self.text_area,
            geo_location="example_city"  # Replace with your target geolocation
        )
        scraper.start_scraper()

    def on_close(self):
        """Clean up resources on close"""
        if self.driver:
            self.driver.quit()
        self.root.destroy()


# Run the application
if __name__ == "__main__":
    app_root = tk.Tk()
    app = GeoLocationApp(app_root)
    app_root.protocol("WM_DELETE_WINDOW", app.on_close)
    app_root.mainloop()

import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class GeoLocationScraper:
    def __init__(self, root):
        # Initialize UI elements
        self.root = root
        self.root.geometry("600x400")
        self.root.title("GeoLocation Scraper")

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=70, height=20)
        self.text_area.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Scraper", command=self.run_scraper)
        self.start_button.pack(pady=5)

        # Set up Selenium WebDriver
        self.driver = webdriver.Chrome()  # Replace with the path to your browser driver if needed

    def log_message(self, message):
        """Log messages to the UI text area."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.text_area.insert(tk.END, f"{timestamp} - {message}\n")
        self.text_area.see(tk.END)

    def run_scraper(self):
        """Main function to run the geolocation scraping process."""
        try:
            self.log_message("SOFTWARE RUNNING - GEO LOCATION SCRAPE STARTED")

            # Open initial URL
            self.driver.get("https://example.com")  # Replace with the appropriate URL

            # Execute arbitrary JavaScript command for logging (example purpose)
            js_script = (
                "var textarea = document.getElementById('textarea_id');"
                "textarea.value += 'Scraper initialized';"
                "textarea.scrollTop = textarea.scrollHeight;"
            )
            self.driver.execute_script(js_script)

            # Scroll the browser window
            scroll_script = "window.scrollTo(0, 10000);"
            self.driver.execute_script(scroll_script)

            time.sleep(1)  # Wait for a while

            # Use Selenium to wait for a specific element
            self.log_message("Waiting for elements to appear...")
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[@id='react-root']/section/main/article/div[3]/div")
                )
            )
            self.log_message("Element found: Proceeding with scraping...")

            # Additional scraping logic here
            # ...

            self.log_message("GEO LOCATION SCRAPE COMPLETED")
        except Exception as e:
            self.log_message(f"Error occurred: {str(e)}")
        finally:
            self.cleanup()

    def cleanup(self):
        """Clean up resources."""
        if self.driver:
            self.driver.quit()
        self.log_message("WebDriver stopped. Resources cleaned up.")


def main():
    root = tk.Tk()
    app = GeoLocationScraper(root)
    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Class for Scraping GeoLocation Data
class ScrapeGeoLocationThree:
    def __init__(self, parent_ui, driver: webdriver.Chrome):
        """
        Initialize the ScrapeGeoLocationThree class.

        :param parent_ui: The root or parent Tkinter UI element for logging and status updates.
        :param driver: Selenium WebDriver instance (e.g., ChromeDriver).
        """
        self.ui = parent_ui  # Reference to the GUI application, typically to log or show status
        self.driver = driver
        self.geo_location_queue = 0
        self.scrape_users_pos = 0

    def log_message(self, message: str):
        """
        Log a message in the parent UI, typically a log area or notification.

        :param message: String message to display/log in the UI.
        """
        if hasattr(self.ui, "text_area"):
            self.ui.text_area.insert(tk.END, message + "\n")
            self.ui.text_area.see(tk.END)
        print(message)  # Console logging (if needed)

    def clear_geo_location_data(self):
        """
        Clears large lists related to GeoLocation data, simulating the 'Bigtable.dll' plugin call.
        """
        try:
            # Simulating clearing large geolocation data
            self.log_message("Clearing large GeoLocation lists (via simulated plugin command)...")
            self.geo_location_queue = 0
            self.scrape_users_pos = 0
        except Exception as e:
            self.log_message(f"Error clearing GeoLocation data: {str(e)}")

    def run(self):
        """
        Run the ScrapeGeoLocationThree process.
        Includes clearing geolocation data and initiating scraping tasks.
        """
        self.log_message("Starting GeoLocation scraping process...")
        self.clear_geo_location_data()


# Example Usage
if __name__ == "__main__":
    # Setting up the Selenium WebDriver for Chrome
    chrome_driver_path = "path_to_chromedriver"  # Replace with path to your actual chromedriver
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # Setting up Tkinter UI
    root = tk.Tk()
    root.title("ScrapeGeoLocationThree UI")

    # Adding a basic text area for logging
    text_area = tk.Text(root, height=20, width=50)
    text_area.pack()

    # Instantiate the scrape class
    app = ScrapeGeoLocationThree(parent_ui=root, driver=driver)
    app.ui.text_area = text_area  # Assigning text area to the app UI reference

    # Adding a start button to trigger the scraping
    start_button = tk.Button(root, text="Start Scrape", command=app.run)
    start_button.pack()

    # Run the Tkinter main loop
    root.mainloop()

    # Quit the WebDriver after UI is closed
    driver.quit()

import os
import re
import time
from datetime import datetime
from tkinter import Tk, Text, Scrollbar, Button, END
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ScrapeGeoLocationFour:
    def __init__(self, driver_path, text_area):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.text_area = text_area
        self.target_user = None
        self.scrape_users_pos = 0
        self.geo_location_queue = 0

    def log_message(self, message):
        """Logs a message to the UI text area."""
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.text_area.insert(END, f"{current_time} - {message}\n")
        self.text_area.see(END)

    def navigate_to_user(self, target_user):
        """Navigates to the Instagram page of the target user."""
        url = f"https://www.instagram.com/p/{target_user}"
        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "coreSpriteOptionsEllipsis"))
            )
            return True
        except:
            return False

    def scrape_from_regex(self, text, pattern):
        """Extracts data from the given text using the specified regex pattern."""
        return re.findall(pattern, text)

    def save_to_file(self, file_path, data):
        """Saves the scraped data to a file."""
        with open(file_path, 'w') as file:
            file.write("\n".join(data))

    def scrape_geo_location(self, geo_location, scrape_data_folder):
        """Main function to scrape geo-location data."""
        self.log_message(f"SOFTWARE RUNNING - GEO LOCATION SENDING REQUEST TO USER ID: {self.target_user}")

        if not self.navigate_to_user(self.target_user):
            self.log_message("Waiting for page to load...")
            wait_breakout = 0
            while wait_breakout < 100:
                time.sleep(0.1)
                wait_breakout += 1
                if "coreSpriteOptionsEllipsis" in self.driver.page_source:
                    break

        page_source = self.driver.page_source
        target_users = []

        # Scrape using regex patterns
        pattern1 = r"(?!\\s\\(@)[a-z.0-9_-]+(?=\\)\\son\\sI)"
        pattern2 = r"(?!\"\\shref=\"\\/)[a-z.0-9_-]+(?=\\/\"\\sstyle)"
        target_users.extend(self.scrape_from_regex(page_source, pattern1))
        target_users.extend(self.scrape_from_regex(page_source, pattern2))

        # Remove duplicates
        target_users = list(set(target_users))

        # Save scraped data to file
        os.makedirs(scrape_data_folder, exist_ok=True)
        file_path = os.path.join(scrape_data_folder, f"[{geo_location}].txt")
        self.save_to_file(file_path, target_users)

        self.geo_location_queue = len(target_users)
        self.scrape_users_pos += 1

        self.log_message(f"GEO LOCATION SCRAPE TOTAL = {self.geo_location_queue}")
        if not target_users:
            self.log_message("No users found, triggering failure process.")

    def cleanup(self):
        """Cleans up resources by closing the web driver."""
        self.driver.quit()


def run_app():
    """Creates a basic Tkinter UI for the scraper."""
    root = Tk()
    root.title("Geo-location Scraper")

    # Create text area
    text_area = Text(root, wrap="word", height=20, width=80)
    text_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    text_area_scrollbar = Scrollbar(root, command=text_area.yview)
    text_area_scrollbar.grid(row=0, column=2, sticky="ns")
    text_area["yscrollcommand"] = text_area_scrollbar.set

    # Start button
    def start_scraping():
        text_area.delete(1.0, END)

        driver_path = "path/to/chromedriver"  # Provide a valid path to your ChromeDriver
        geo_location = "example_location"
        scrape_data_folder = os.path.expanduser("~/Desktop/ScrapeData")

        scraper = ScrapeGeoLocationFour(driver_path, text_area)
        try:
            scraper.target_user = "example_target_user"  # Example user ID
            scraper.scrape_geo_location(geo_location, scrape_data_folder)
        finally:
            scraper.cleanup()

    start_button = Button(root, text="Start Scraping", command=start_scraping)
    start_button.grid(row=1, column=0, pady=10, padx=10)

    # Close button
    def close_app():
        root.destroy()

    close_button = Button(root, text="Exit", command=close_app)
    close_button.grid(row=1, column=1, pady=10, padx=10)

    root.mainloop()


if __name__ == "__main__":
    run_app()

import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import datetime


class TagsScraperOne:
    def __init__(self, root):
        self.root = root
        self.driver = None
        self.scrape_option_var = tk.StringVar(value="Scrape All Tags")
        self.text_area = tk.Text(self.root, height=20, width=80)
        self.text_area.pack()
        self.setup_ui()

    def setup_ui(self):
        options = ["Scrape All Tags", "Scrape Related Tags", "Scrape Top Post Tags"]
        options_menu = ttk.OptionMenu(self.root, self.scrape_option_var, options[0], *options)
        options_menu.pack(pady=10)

        start_button = ttk.Button(self.root, text="Start Scraping", command=self.run_scraper)
        start_button.pack(pady=10)

    def log_message(self, message):
        # Log messages in the text area
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.text_area.insert(tk.END, f"{timestamp} - {message}\n")
        self.text_area.see(tk.END)

    def initialize_webdriver(self):
        # Initialize Selenium WebDriver
        self.log_message("Initializing WebDriver...")
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(executable_path="path_to_chromedriver", options=options)

    def scrape_all_tags(self):
        self.log_message("Scrape All Tags function activated.")
        # Add logic to perform scraping for all tags
        self.navigate_to_url(f"https://www.instagram.com/explore/tags/{self.scrape_tag}/")

    def scrape_related_tags(self):
        self.log_message("Scrape Related Tags function activated.")
        # Add logic to perform scraping for related tags
        self.navigate_to_url(f"https://www.instagram.com/explore/tags/{self.scrape_tag}/")

    def scrape_top_post_tags(self):
        self.log_message("Scrape Top Post Tags function activated.")
        # Add logic to perform scraping for the top post tags
        self.navigate_to_url(f"https://www.instagram.com/explore/tags/{self.scrape_tag}/")

    def navigate_to_url(self, url):
        self.log_message(f"Navigating to URL: {url}")
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//span[@id="react-root"]/section/main/article/div[1]/h2')))
            self.log_message("Navigation successful.")
        except Exception as e:
            self.log_message(f"Error navigating to the URL: {e}")
            self.scrape_tag_nav_fallback()

    def scrape_tag_nav_fallback(self):
        self.log_message("Fallback function for navigation triggered.")

    def run_scraper(self):
        # Run the scraping operation based on the selected option
        thread = threading.Thread(target=self._run_scraper_thread)
        thread.start()

    def _run_scraper_thread(self):
        # This function runs in a separate thread
        try:
            self.initialize_webdriver()
            scrape_option = self.scrape_option_var.get()

            if scrape_option == "Scrape All Tags":
                self.scrape_all_tags()
            elif scrape_option == "Scrape Related Tags":
                self.scrape_related_tags()
            elif scrape_option == "Scrape Top Post Tags":
                self.scrape_top_post_tags()

            self.log_message("Scraping completed.")
        finally:
            if self.driver:
                self.driver.quit()
                self.log_message("WebDriver closed.")


# Entry point of the application
def main():
    root = tk.Tk()
    root.title("Tags Scraper")
    scraper = TagsScraperOne(root)
    root.protocol("WM_DELETE_WINDOW", scraper.log_message("App closed."))
    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


class TagsScraperTwo:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None
        self.root = tk.Tk()
        self.root.title("Tags Scraper")
        self.setup_ui()

    def setup_ui(self):
        # Setting up the UI elements
        self.text_area = tk.Text(self.root, wrap=tk.WORD, height=20, width=60)
        self.text_area.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Scraping", command=self.run_scraper)
        self.start_button.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def open_browser(self):
        # Launching the browser
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(executable_path=self.driver_path, options=options)

    def log_message(self, message):
        # Log message in the text area
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.text_area.insert(tk.END, f"{time_stamp} - {message}\n")
        self.text_area.see(tk.END)

    def scrape_tags(self):
        try:
            if not self.driver:
                self.open_browser()

            self.log_message("Navigating to the target page...")
            self.driver.get("https://example.com")  # Replace with the actual page URL

            self.log_message("Scrolling the browser...")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            self.log_message("Waiting for elements to appear...")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//section/main/article/div[3]/div")))

            self.log_message("Extracting tags using regex...")
            page_source = self.driver.page_source

            import re
            tags = re.findall(r"(?!<a\shref=\"\/p\/)[A-Z_a-z0-9]{9,14}(?=\/\?tagged=)", page_source)

            tags = list(set(tags))  # Remove duplicates
            self.log_message(f"Number of unique tags found: {len(tags)}")

            if not tags:
                self.log_message("No tags found! Exiting scraper.")
                return

            self.log_message("Appending tags to the UI...")
            for tag in tags:
                self.text_area.insert(tk.END, f"{tag}\n")

        except Exception as e:
            self.log_message(f"An error occurred: {e}")

    def run_scraper(self):
        self.log_message("Starting the scraping process...")
        self.scrape_tags()
        self.log_message("Scraping process completed.")

    def on_close(self):
        # Close the browser and the application
        if self.driver:
            self.driver.quit()
        self.root.destroy()


# Main entry point of the application
if __name__ == "__main__":
    # Provide the path to your ChromeDriver executable
    chrome_driver_path = "path/to/chromedriver"  # Replace with actual path

    app = TagsScraperTwo(driver_path=chrome_driver_path)
    app.root.mainloop()

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TagsScraperThree:
    def __init__(self):
        self.tags_in_queue = 0  # Equivalent of `set(#TagsInQueue,0,"Global")`
        self.tags_in_queue_pos = 0  # Equivalent of `set(#TagsInQueuePos,0,"Global")`

    # You can add additional methods or functionality to this class as needed


def main():
    # Initialize the TagsScraperThree class.
    scraper = TagsScraperThree()

    # Simulate adding tasks or queue functionality (if needed).
    scraper.tags_in_queue = 5  # Example usage
    scraper.tags_in_queue_pos = 1  # Example usage

    print(f"Tags in Queue: {scraper.tags_in_queue}")
    print(f"Tags in Queue Position: {scraper.tags_in_queue_pos}")


if __name__ == "__main__":
    main()

import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk, Text, Label, Button, StringVar, OptionMenu, Scrollbar, RIGHT, Y


# Define the TagsScraperFour class
class TagsScraperFour:
    def __init__(self, text_area, driver, scrape_data_folder):
        self.text_area = text_area
        self.driver = driver
        self.scrape_data_folder = scrape_data_folder
        self.tags_in_queue_pos = 0
        self.master_delay_trigger = 0
        self.scrape_tags_option = "Scrape All Tags"  # Default option, changeable via UI
        self.tags_to_scrape = 50
        self.scraped_tags = []

    def log_message(self, message):
        """Log messages to the Tkinter text_area."""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.text_area.insert('end', f"{timestamp} - {message}\n")
        self.text_area.see('end')

    def navigate_to_target(self, target_user, scrape_tag):
        """Navigate to the Instagram tagged page for the specified user and tag."""
        url = f"https://www.instagram.com/p/{target_user}/?tagged={scrape_tag}"
        self.log_message(f"Sending request to ID: [{target_user}] KEYWORD: [{scrape_tag}]")
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/about/us/'][text()='About us']"))
        )

    def scrape_all_tags(self):
        """Scrape all tags from the page."""
        page_source = self.driver.page_source
        tags = re.findall(r"(?!/explore/tags/[\w.]+/\">)[@#.\w]+(?=</a>)", page_source)
        self.scraped_tags.extend(tags)
        self.scraped_tags = list(set(self.scraped_tags))  # Remove duplicates
        self.save_to_file(f"All [{self.scrape_tags_option}] Tags.txt", self.scraped_tags)
        self.log_message(f"Scraped {len(self.scraped_tags)} tags.")

    def scrape_related_tags(self, scrape_tag):
        """Scrape related tags."""
        page_source = self.driver.page_source
        tags = re.findall(rf"(?!/explore/tags/){scrape_tag}\w+(?=(/\">#))", page_source)
        self.scraped_tags.extend(tags)
        self.scraped_tags = list(set(self.scraped_tags))
        self.log_message(f"Collected {len(self.scraped_tags)} related tags.")

    def save_to_file(self, file_name, data):
        """Write the scraped data to a file."""
        os.makedirs(self.scrape_data_folder, exist_ok=True)
        full_path = os.path.join(self.scrape_data_folder, file_name)
        with open(full_path, 'w') as file:
            file.write("\n".join(data))
        self.log_message(f"Data saved to file: {full_path}")

    def run_scrape(self, target_user, scrape_tag, scrape_option):
        self.scrape_tags_option = scrape_option
        self.navigate_to_target(target_user, scrape_tag)

        if scrape_option == "Scrape All Tags":
            self.scrape_all_tags()
        elif scrape_option == "Scrape Related Tags":
            self.scrape_related_tags(scrape_tag)

        if len(self.scraped_tags) >= self.tags_to_scrape:
            self.log_message("Scraping complete! Reached the limit.")


# UI setup with Tkinter
class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Tags Scraper Four")
        self.root.geometry("600x400")

        # Output text area
        self.text_area = Text(self.root, wrap='word', height=15, width=70)
        self.text_area.pack()

        # Entry for username
        Label(root, text="Target User:").pack()
        self.target_user = StringVar()
        self.target_user.set("target_user")

        # Entry for keyword
        Label(root, text="Keyword:").pack()
        self.keyword = StringVar()
        self.keyword.set("keyword")

        # Dropdown for scraping options
        self.scrape_option_var = StringVar(value="Scrape All Tags")
        self.scrape_options = ["Scrape All Tags", "Scrape Related Tags"]
        self.scrape_option_menu = OptionMenu(root, self.scrape_option_var, *self.scrape_options)
        self.scrape_option_menu.pack()

        # Start button
        self.start_button = Button(self.root, text="Start Scraper", command=self.run_scraper)
        self.start_button.pack()

        # Initialize the scraper
        chrome_driver_path = "./chromedriver"  # Replace with the correct path to chromedriver
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        self.scraper = TagsScraperFour(text_area=self.text_area, driver=driver, scrape_data_folder="./ScrapeData")

    def run_scraper(self):
        """Run the scraper with the specified options."""
        target_user = self.target_user.get()
        scrape_tag = self.keyword.get()
        scrape_option = self.scrape_option_var.get()
        self.scraper.run_scrape(target_user, scrape_tag, scrape_option)

    def cleanup(self):
        """Clean up resources before closing."""
        if self.scraper.driver:
            self.scraper.driver.quit()
        self.root.destroy()


# Run the application
if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.protocol("WM_DELETE_WINDOW", app.cleanup)
    root.mainloop()

import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time


class ScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Scraper")

        # Initialize UI components
        self.text_area = scrolledtext.ScrolledText(root, width=80, height=20)
        self.text_area.pack(padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start Scraping", command=self.run_scraper)
        self.start_button.pack(pady=10)

        # Selenium WebDriver setup
        self.chrome_driver_path = "path_to_chromedriver"  # Update this path to your chromedriver
        self.driver = None

    def log_message(self, message):
        """Logs messages to the text area in the UI."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.text_area.insert(tk.END, f"{timestamp} - {message}\n")
        self.text_area.see(tk.END)

    def navigate_to(self, url):
        """Navigates to a specific URL using Selenium."""
        self.driver.get(url)
        self.log_message(f"Navigated to: {url}")

    def wait_for_element(self, xpath, mode="appear", timeout=5):
        """Waits for an element to either appear or disappear."""
        try:
            if mode == "appear":
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                self.log_message(f"Element appeared: {xpath}")
            elif mode == "disappear":
                WebDriverWait(self.driver, timeout).until_not(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                self.log_message(f"Element disappeared: {xpath}")
        except Exception as e:
            self.log_message(f"Error waiting for element: {xpath}, mode: {mode}, error: {e}")

    def scrape_likes_one(self):
        """Main scraping function."""
        try:
            self.log_message("Scraper initialized...")
            self.driver = webdriver.Chrome(self.chrome_driver_path)
            scrape_tag = "scrapeliketag"  # Replace this with your desired tag
            scrape_tag = scrape_tag.replace("#", "")

            url = f"https://www.instagram.com/explore/tags/{scrape_tag}/"
            self.navigate_to(url)

            # Simulate waiting for an element to appear
            self.wait_for_element(
                xpath="//span[@id='react-root']/section/main/article/div[1]/h2",
                mode="appear",
                timeout=5
            )

            self.log_message("Scraping process started...")

            # Simulate removing popular/top posts if required
            remove_top_posts = True  # Change based on requirement
            if remove_top_posts:
                self.log_message("Removing top posts...")
                try:
                    top_posts_xpath = "//span[@id='react-root']/section/main/article/div[1]/div"
                    # Clear top posts by changing attribute (if supported)
                    self.driver.execute_script("arguments[0].innerText = '';",
                                               self.driver.find_element(By.XPATH, top_posts_xpath))
                    self.log_message("Top posts removed successfully.")
                except Exception as e:
                    self.log_message(f"Failed to remove top posts: {e}")

            # Log progress in the UI
            self.log_message(f"SCRAPING PROCESS STARTED FOR TAG: [{scrape_tag}]")

        except Exception as exc:
            self.log_message(f"An error occurred during scraping: {exc}")
        finally:
            if self.driver:
                self.driver.quit()
            self.log_message("Scraping process completed.")

    def run_scraper(self):
        """Runs the scraper in a separate thread."""
        scrape_thread = threading.Thread(target=self.scrape_likes_one)
        scrape_thread.start()


# Tkinter application setup
if __name__ == "__main__":
    root = tk.Tk()
    app = ScraperApp(root)
    root.mainloop()

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


class ScrapeLikesTwo:
    def __init__(self, driver, text_area):
        self.driver = driver
        self.text_area = text_area

    def log_message_in_ui(self, message):
        """
        Logs a message in the provided Tkinter text area.
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {message}\n"
        self.text_area.insert(tk.END, log_entry)
        self.text_area.see(tk.END)

    def remove_duplicates(self, users_list):
        """
        Removes duplicates from a list of scraped users.
        """
        return list(set(users_list))

    def scrape_likes(self):
        """
        Function to perform the scraping operation for likes.
        """

        # Step 1: Use regex to identify user IDs
        try:
            document_text = self.driver.execute_script("return document.body.innerText")
            users = set()
            regex_pattern = r"(?!<a\shref=\"\/p\/)[A-Za-z0-9_]{9,14}(?=\/\?tagged=)"
            import re
            users.update(re.findall(regex_pattern, document_text))
        except Exception as e:
            self.log_message_in_ui(f"Error while gathering document text: {e}")
            return

        # Step 2: Remove duplicates
        users = self.remove_duplicates(users)
        likes_scraped_count = len(users)

        # Step 3: Log the count of scraped users
        self.log_message_in_ui(
            f"SOFTWARE RUNNING - ITEMS SCRAPED TO LIST = [{likes_scraped_count}] - LOG RUNNING - INTERNALIZING COMPLETE")

        # Step 4: Scroll the browser
        try:
            self.driver.execute_script("window.scrollBy(0, 10000);")
            self.log_message_in_ui("Browser scrolled successfully.")
        except Exception as e:
            self.log_message_in_ui(f"Error while scrolling: {e}")

        # Step 5: Wait for a specific element to appear
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[3]/div'))
            )
            self.log_message_in_ui("Target element appeared.")
        except Exception as e:
            self.log_message_in_ui(f"Error waiting for target element: {e}")
            return

        # Conclusion of scraping run
        self.log_message_in_ui("Scraping completed successfully!")


def setup_driver(chrome_driver_path):
    """
    Sets up a Selenium ChromeDriver.
    """
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options

    chrome_service = Service(chrome_driver_path)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--headless")  # Run in headless mode
    return webdriver.Chrome(service=chrome_service, options=chrome_options)


def setup_tkinter_ui(driver):
    """
    Sets up the Tkinter UI and binds actions.
    """

    # Tkinter root initialization
    root = tk.Tk()
    root.title("Scraping Likes")

    # Create and pack a text area for displaying logs
    text_area = tk.Text(root, height=20, width=80)
    text_area.pack()

    # Create and pack the Start button
    def start_scraping():
        scraper = ScrapeLikesTwo(driver, text_area)
        scraper.scrape_likes()

    start_button = tk.Button(root, text="Start Scraping", command=start_scraping)
    start_button.pack()

    # Handle cleanup when the window is closed
    def on_close():
        driver.quit()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)  # Close handler
    return root


if __name__ == "__main__":
    # Path to the ChromeDriver executable
    chrome_driver_path = "/path/to/chromedriver"  # Replace with the correct path

    # Setup the Selenium WebDriver
    driver = setup_driver(chrome_driver_path)

    # Navigate to the starting URL
    driver.get("https://example.com")  # Replace with the target URL

    # Setup the Tkinter UI
    tkinter_app = setup_tkinter_ui(driver)
    tkinter_app.mainloop()

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ScrapeLikesThree:
    def __init__(self):
        self.driver = None
        self.likes_scrape_queue = 0  # Global variable
        self.scrape_users_pos = 0  # Global variable

    def setup_driver(self, chrome_driver_path):
        """Setup the Selenium WebDriver."""
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    def clear_large_list(self, target_user):
        """Simulate clearing a large list similar to the plugin command."""
        # Add selenium actions relevant to the operation here
        print(f"Clearing large list for the target_user: {target_user}")

    def run_scrape_likes_three(self, target_user):
        """Ported functionality of 'ScrapeLikesThree'."""
        self.clear_large_list(target_user)
        self.scrape_users_pos = 0
        self.likes_scrape_queue = 0


class MainApplication:
    def __init__(self, root, driver_path):
        self.root = root
        self.driver_path = driver_path
        self.text_area = None
        self.start_button = None
        self.scraper = ScrapeLikesThree()
        self.setup_tkinter_ui()

    def setup_tkinter_ui(self):
        """Setup Tkinter UI elements."""
        self.root.title("Scrape Likes Three")

        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Run Scrape", command=self.run_scrape)
        self.start_button.pack(pady=10)

    def log_message(self, message):
        """Log messages to the Tkinter Text Area."""
        self.text_area.insert(tk.END, message + '\n')
        self.text_area.see(tk.END)

    def run_scrape(self):
        """Run ScrapeLikesThree functionality."""
        self.log_message("Initializing scraper...")
        try:
            self.scraper.setup_driver(self.driver_path)
            self.log_message("Driver setup successful.")
            target_user = "example_user"  # Replace this with actual username
            self.scraper.run_scrape_likes_three(target_user)
            self.log_message("ScrapeLikesThree executed successfully.")
        except Exception as e:
            self.log_message(f"An error occurred: {e}")
        finally:
            if self.scraper.driver:
                self.scraper.driver.quit()
                self.log_message("Driver closed.")


if __name__ == "__main__":
    chrome_driver_path = "path/to/chromedriver"  # Replace with the actual ChromeDriver path
    root = tk.Tk()
    app = MainApplication(root, chrome_driver_path)
    root.mainloop()

import time
import re
from tkinter import Tk, Text, Button, Label, StringVar, OptionMenu, END, Scrollbar, filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ScrapeLikesFour:
    def __init__(self, driver_path):
        # Setup WebDriver
        self.driver_path = driver_path
        self.driver = webdriver.Chrome(executable_path=self.driver_path)

        # Tkinter UI Setup
        self.root = Tk()
        self.root.title("Scrape Likes Tool")

        # Log Display
        self.text_area = Text(self.root, wrap="word", height=20, width=80, state="normal")
        self.text_area.grid(row=0, column=0, sticky="nsew")
        scrollbar = Scrollbar(self.root, command=self.text_area.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.text_area['yscrollcommand'] = scrollbar.set

        # Start Button
        self.start_button = Button(self.root, text="Start", command=self.run_scraper)
        self.start_button.grid(row=1, column=0)

        # Scrape Options
        self.options_var = StringVar(self.root)
        self.options_var.set("Scrape Comments")
        options_menu = OptionMenu(self.root, self.options_var, "Scrape Comments", "Scrape Commenters")
        options_menu.grid(row=2, column=0)

    def log_message(self, message):
        """Logs a given message to the UI."""
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.text_area.insert(END, f"{current_time} - {message}\n")
        self.text_area.see(END)

    def run_scraper(self):
        """Main scraping function."""
        self.log_message("SOFTWARE RUNNING - SENDING REQUEST TO TAG")
        target_key = "example_target_key"  # Replace with actual logic to fetch the target key
        scrape_tag = "example_tag"  # Replace with actual logic to fetch ScrapelikeTag
        try:
            # Navigate to the targeted Instagram post
            self.driver.get(f"https://www.instagram.com/p/{target_key}/?tagged={scrape_tag}")
            self.wait_for_element_to_appear("//a[contains(@href, 'liked_by') or contains(@href, 'commenters')]", 10)

            # Scrape Data
            page_source = self.driver.page_source
            user_list = []
            user_list += re.findall(r"(?:\"href=\"\/)([a-zA-Z0-9._]+)(?:\/\" style=\"width:\s30px;)", page_source)
            user_list += re.findall(r"(?:title=\"[a-zA-Z0-9._]+\" href=\"\/)([a-zA-Z0-9._]+)(?:\/\">)", page_source)

            # Remove duplicates and save
            user_list = list(set(user_list))
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")],
                initialfile=f"[{scrape_tag}] Likes.txt"
            )
            with open(file_path, "w") as file:
                for user in user_list:
                    file.write(user + "\n")

            # Log success
            self.log_message(f"USERS SCRAPED TO LIST = [{scrape_tag}] - Total: {len(user_list)}")
        except Exception as e:
            self.log_message(f"Error occurred: {str(e)}")
        finally:
            self.cleanup()

    def wait_for_element_to_appear(self, xpath, timeout):
        """Waits for a specific element to appear."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            self.log_message("Timeout waiting for element.")
            return False

    def cleanup(self):
        """Cleanup resources."""
        self.log_message("SOFTWARE STOPPED - CLEANING UP")
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    chrome_driver_path = "path_to_chromedriver"  # Update to your local ChromeDriver path
    scraper = ScrapeLikesFour(chrome_driver_path)
    scraper.root.mainloop()

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import os


class ScrapeLikesFive:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Scraper - Likes")
        self.text_area = tk.Text(root, width=80, height=20)
        self.text_area.pack(pady=10)
        self.start_button = tk.Button(root, text="Start Scraping", command=self.start_scraping)
        self.start_button.pack(pady=5)
        self.driver = None
        self.target_key = None
        self.likes_scraped = 0

        # Set scraping options
        self.OptionsVar = {
            "ScrapeComments": "Scrape Comments",
            "ScrapeCommenters": "Scrape Commenters"
        }
        self.NumberToScrape = 100  # Example limit

    def log_message(self, message):
        """Log message to the Tkinter text area."""
        self.text_area.insert(tk.END, f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
        self.text_area.see(tk.END)

    def setup_driver(self):
        """Setup Selenium WebDriver."""
        chrome_driver_path = "path_to_chromedriver"  # Replace this with your ChromeDriver path
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    def navigate_to_tag_url(self, tag_url):
        """Navigate to the tag URL."""
        self.driver.get(tag_url)
        self.log_message("Navigated to the Tag URL.")

    def fetch_target_key(self):
        """Extract the target_key from the current page URL."""
        current_url = self.driver.current_url
        tagged_regex = re.search(r"(?!https://www.instagram.com/p/)[-a-zA-Z0-9_]+(?=/\?tagged=\w+)", current_url)
        post_regex = re.search(r"(?<=https://www.instagram.com/p/)[-a-zA-Z0-9_]+(?=/)", current_url)

        if tagged_regex:
            self.target_key = tagged_regex.group()
        elif post_regex:
            self.target_key = post_regex.group()
        self.log_message(f"Target key extracted: {self.target_key}")

    def click_likes_button(self):
        """Click the likes button on the page."""
        try:
            likes_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/liked_by')]"))
            )
            likes_button.click()
            self.log_message("Clicked on Likes button.")
        except Exception as e:
            self.log_message(f"Failed to locate likes button. Error: {e}")

    def scroll_and_scrape_usernames(self):
        """Scroll through the likes list and scrape usernames."""
        inc_num = 24  # Incremental variable for scrolling
        username_list = set()

        while self.likes_scraped < self.NumberToScrape:
            for _ in range(2):  # Scroll down twice
                try:
                    user_element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, f"//html/body/div[3]/div/div[2]/div/div/div[2]/ul/div/li[{inc_num}]"))
                    )
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", user_element)
                except Exception as e:
                    self.log_message(f"Error during scrolling: {e}")

            time.sleep(0.5)
            page_source = self.driver.page_source
            usernames = re.findall(r'(?:" href="/)[a-zA-Z0-9_.]+(?=/")', page_source)
            username_list.update(usernames)
            self.likes_scraped = len(username_list)
            inc_num += 5  # Increment the scroll index

            self.log_message(f"Total likes scraped: {self.likes_scraped}")
            if self.likes_scraped >= self.NumberToScrape:
                break

        # Write usernames to file
        os.makedirs(os.path.expanduser("~/Desktop/ScrapeData"), exist_ok=True)
        file_path = os.path.expanduser(f"~/Desktop/ScrapeData/{self.target_key}_Likes.txt")
        with open(file_path, 'w') as file:
            file.writelines(f"{username}\n" for username in username_list)
        self.log_message(f"Usernames saved to {file_path}")

    def start_scraping(self):
        """Start the scraping process."""
        try:
            self.setup_driver()
            tag_url = "https://www.instagram.com/explore/tags/example/"  # Replace this URL with the Tag URL
            self.navigate_to_tag_url(tag_url)
            time.sleep(2)

            self.fetch_target_key()
            self.click_likes_button()
            time.sleep(2)
            self.scroll_and_scrape_usernames()

            self.log_message("Scraping completed successfully.")
        except Exception as e:
            self.log_message(f"An error occurred: {e}")
        finally:
            if self.driver:
                self.driver.quit()


# Tkinter App Initialization
if __name__ == "__main__":
    root = tk.Tk()
    app = ScrapeLikesFive(root)
    root.mainloop()

import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class LikeScrapeNavFallback:
    def __init__(self, driver, scrapelike_tag, user_profile):
        self.driver = driver
        self.scrapelike_tag = scrapelike_tag
        self.user_profile = user_profile

    def navigate_back(self):
        """Navigate back and handle potential pop-ups."""
        try:
            # Navigate Back
            self.driver.back()
            time.sleep(2)

            # Handle potential pop-up button
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//html/body/div[3]/div/button"))
                )
                button = self.driver.find_element(By.XPATH, "//html/body/div[3]/div/button")
                button.click()
            except Exception:
                pass
        except Exception as e:
            print(f"Error during navigation back: {e}")

    def profile_link_grabber(self):
        """Navigate to the user's profile."""
        profile_link = f"//a[@href='/{self.user_profile}/' and text()='Profile']"
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, profile_link))
        )
        self.driver.find_element(By.XPATH, profile_link).click()

    def start_navigation(self):
        """Perform the scrape navigation."""
        # Check for "Go Back" in document text
        page_source = self.driver.page_source
        if "Go Back" in page_source or "Go back" in page_source:
            # Navigate back if text exists
            self.navigate_back()

            # Grab profile link
            self.profile_link_grabber()

            # Handling UI interactions
            nav_element_xpath = "//span[@id='react-root']/section/nav/div[2]/div/div/div[2]/div/div/span[1]"
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, nav_element_xpath))
            )
            self.driver.find_element(By.XPATH, nav_element_xpath).click()

            # Input text into tag search
            input_xpath = "//input[@value='']"
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, input_xpath))
            )
            search_input = self.driver.find_element(By.XPATH, input_xpath)
            search_input.send_keys(self.scrapelike_tag)
            search_input.send_keys(Keys.RETURN)

            # Wait for results to appear
            results_xpath = "//span[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]"
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, results_xpath))
            )

            # Extract `class` attribute using regex from document text
            page_source = self.driver.page_source
            tag_regex_span = r'(?!<span\sclass=\")[_a-z0-9\s]+(?=\">' + re.escape(self.scrapelike_tag) + r'</span>)'
            tag_regex_input = r'(?!<input\stype=\"text\"\sclass=\")[_a-z0-9\s]+(?=\"\splaceholder=\"Search\")'
            tag_span_class = re.search(tag_regex_span, page_source)
            tag_input_class = re.search(tag_regex_input, page_source)

            # Use the extracted class to click
            if tag_span_class or tag_input_class:
                tag_class = tag_span_class.group() if tag_span_class else tag_input_class.group()
                clickable_xpath = f"//span[@class='{tag_class}' and text()='{self.scrapelike_tag}']"
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, clickable_xpath))
                )
                self.driver.find_element(By.XPATH, clickable_xpath).click()

            # Wait for appearance of the desired element
            article_xpath = "//span[@id='react-root']/section/main/article/div[1]/h2"
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, article_xpath))
            )

import os
from tkinter import Tk, Text
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def scrape_variable_list_clear():
    """
    This function clears several variables and ensures the required folder exists on the desktop.
    """

    # Ensure the "ScrapeData" folder exists on the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    scrape_data_folder = os.path.join(desktop_path, "ScrapeData")
    if not os.path.exists(scrape_data_folder):
        os.makedirs(scrape_data_folder)

    # Command to clear plugin-based data (No direct Python equivalent, plugin implementation would vary)
    # Place a placeholder for clearing Bigtable-like storage or other related data
    clear_bigtable_plugin_data()

    # Reset variables (assuming we use a dictionary for global-like variable handling)
    global_state_variables = {
        "TagsInQueue": 0,
        "GeoLocationQueue": 0,
        "ScrapeFollowersQueue": 0,
        "ScrapeCommentQueue": 0,
        "master_delay_trigger": 0,
        "delay_ticker": 0,
        "ClearLogSystem": clear_log_system("LogClearCommand")  # Placeholder for ‘ClearLogSystem’
    }
    return global_state_variables


def clear_bigtable_plugin_data():
    """
    Placeholder for clearing bigtable data. This should be replaced with actual logic
    if there's integration with a specialized plugin or database.
    """
    print("Cleared all large lists in plugin")


def clear_log_system(command):
    """
    Placeholder for clearing logs based on a system command.
    Replace this with actual log-clearing logic.
    """
    print(f"Clearing logs with command: {command}")
    return True  # This is a simplified example


# Example Tkinter code to integrate into a UI
def setup_tkinter_ui():
    """
    Initializes Tkinter for a basic interface to demonstrate the scrape_variable_list_clear function.
    """
    root = Tk()
    root.title("Scrape Variable List Clear Example")

    # Text widget to display execution results
    text_area = Text(root, height=10, width=60)
    text_area.pack()

    # Function to trigger the scrape_variable_list_clear and display results
    def run_scrape_variable_list_clear():
        results = scrape_variable_list_clear()
        text_area.insert('1.0', "Scrape Variable List Cleared:\n")
        for key, value in results.items():
            text_area.insert('end', f"{key}: {value}\n")

    # Button to execute the function
    start_button = tk.Button(root, text="Run Clear Function", command=run_scrape_variable_list_clear)
    start_button.pack()

    root.mainloop()


# Selenium Setup Example
def setup_driver():
    """
    Sets up a Selenium WebDriver. Modify the 'chromedriver_path' to point to the chromedriver executable.
    """
    chrome_driver_path = "path_to_chromedriver"  # Replace with actual chromedriver path
    service = Service(chrome_driver_path)

    # Use Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service, options=options)
    print("WebDriver Setup Completed")

    return driver


# Example execution
if __name__ == "__main__":
    # Uncomment the below line to set up and run the Tkinter UI
    # setup_tkinter_ui()

    # Example browser driver setup (for testing or scraping functionality)
    driver = setup_driver()

import os
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PrefixHashTagsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prefix HashTags Generator")
        self.root.geometry("600x400")

        # Set up UI elements
        self.text_area = tk.Text(root, height=20, width=70)
        self.text_area.pack(padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.run)
        self.start_button.pack(pady=10)

        # Browser Driver
        self.driver = None
        # Temporary variables for hashtag management
        self.prefix_hashtag = []
        self.hashtag = []

    def setup_driver(self):
        """Initialize the Selenium WebDriver."""
        try:
            chrome_driver_path = "path/to/chromedriver"  # Update this to your ChromeDriver path
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # Run browser in headless mode
            self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize WebDriver: {e}")

    def run(self):
        """Main workflow function."""
        self.setup_driver()
        if not self.driver:
            return

        try:
            # Replace plugin command functionality with Selenium operations or mocks
            self.prefix_hashtag = self.scrape_tags()
            self.hashtag = self.append_prefix_suffix(self.prefix_hashtag, "#", "")

            if self.get_user_input("Spin scraped tags (YES/NO)?") == "YES":
                self.hashtag = self.convert_to_spin_syntax(self.hashtag)

            generated_file_path = self.save_to_file(self.hashtag)
            self.display_result(generated_file_path)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            if self.driver:
                self.driver.quit()

    def scrape_tags(self):
        """Simulate scraping tags."""
        tags = ["tag1", "tag2", "tag3"]  # Replace with actual scraping logic
        self.driver.get("https://example.com/tags")  # Example URL
        return tags

    def append_prefix_suffix(self, tags, prefix, suffix):
        """Append prefix and suffix to each tag."""
        return [f"{prefix}{tag}{suffix}" for tag in tags]

    def convert_to_spin_syntax(self, tags):
        """Convert tags to spin syntax."""
        spin_syntax = "{" + "|".join(tags) + "}"
        return spin_syntax.split("|")  # Example splitting logic

    def save_to_file(self, tags):
        """Save tags to a file."""
        desktop = os.path.expanduser("~/Desktop")
        file_path = os.path.join(desktop, f"ScrapeData/Related To [ScrapeTag] Tags.txt")

        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            file.write("\n".join(tags))

        return file_path

    def display_result(self, file_path):
        """Show the result to the user."""
        messagebox.showinfo("Success", f"Tags saved to: {file_path}")

    def get_user_input(self, prompt):
        """Ask for user input via a dialog."""
        return "YES"  # Simulating input for now, replace with a dialog later


if __name__ == "__main__":
    root = tk.Tk()
    app = PrefixHashTagsApp(root)
    root.mainloop()

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


# Function to scrape and process tags
def spin_scraped_tags():
    # Assuming this is the path to the ChromeDriver
    chrome_driver_path = "path/to/chromedriver"

    # Setup Selenium browser
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("URL_TO_SCRAPE")  # Replace with the URL you need to scrape

    try:
        # Example for obtaining data - Update as per your specific requirements
        # Logic to scrape the tags
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#ScrapeTags"))
        )
        scraped_tags = driver.find_element(By.CSS_SELECTOR, "#ScrapeTags").text

        # Process tags into a list
        tag_list = scraped_tags.split("\n")
        tag_list_cleaned = list(set(tag_list))  # Remove duplicates

        # Prepare the output in spin syntax format
        spin_syntax = "{" + "|".join(tag_list_cleaned) + "}"

        # Save data to a file
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "ScrapeData")
        os.makedirs(desktop_path, exist_ok=True)

        scrape_tag = "DefaultScrapeTag"  # Replace with dynamic tag if available
        output_file = os.path.join(desktop_path, f"All [{scrape_tag}] Tags.txt")
        with open(output_file, "w") as f:
            f.write(spin_syntax)

        # Update loaded list variable (if needed for UI/other operations)
        print(f"Saved to file: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


# Function to setup Tkinter UI
def setup_tkinter_ui():
    # Create the main Tkinter application window
    root = tk.Tk()
    root.title("Spin Scraped Tags Tool")

    # Add a text area
    text_area = tk.Text(root, height=15, width=50)
    text_area.pack(pady=10)

    # Add a button to start the process
    def start_scraping():
        text_area.insert(tk.END, "Scraping started...\n")
        spin_scraped_tags()
        text_area.insert(tk.END, "Scraping completed and file has been saved.\n")

    start_button = tk.Button(root, text="Start Scraping", command=start_scraping)
    start_button.pack(pady=10)

    # Run the Tkinter main loop
    root.mainloop()


# Main function to initiate the application
if __name__ == "__main__":
    setup_tkinter_ui()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RemoveNonTags:
    def __init__(self, driver, bigtable_plugin_data):
        self.driver = driver
        self.bigtable_plugin_data = bigtable_plugin_data
        self.position = 0

    def run_remove_non_tags(self):
        """
        Remove items from a list that do not contain the '#' symbol.
        """
        while self.position < len(self.bigtable_plugin_data):
            current_item = self.bigtable_plugin_data[self.position]

            # Check if the current item does not contain the '#' symbol
            if '#' not in current_item:
                self.bigtable_plugin_data.pop(self.position)
                self.position -= 1  # Adjust position due to removal

            self.position += 1


class App:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        """
        Set up the UI components using Tkinter.
        """
        self.root.title("Remove Non-Tags Application")

        # Add UI elements
        self.text_area = tk.Text(self.root, height=20, width=60)
        self.text_area.pack(pady=20)

        self.start_button = tk.Button(
            self.root, text="Start Process", command=self.start_process
        )
        self.start_button.pack(pady=10)

    def start_process(self):
        """
        Connect to Selenium and handle the removal of non-tagged items.
        """
        # Example: Replace this with the actual logic to set up Selenium
        bigtable_plugin_data = [
            "Tag#1",
            "ItemWithoutTag",
            "#" * 3,
            "AnotherItemWithout#",
            "#TaggedItem",
            ]

        # Example: Initialize the RemoveNonTags functionality
        try:
            # Initialize Selenium WebDriver (example: Chrome)
            driver = webdriver.Chrome(executable_path="./chromedriver")

            # Perform the scraping/removal operation
            scraper = RemoveNonTags(driver, bigtable_plugin_data)
            scraper.run_remove_non_tags()

            # Update the UI with results
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(
                tk.END, f"Filtered Data:\n\n{bigtable_plugin_data}"
            )

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            driver.quit()


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()

import time
from tkinter import Tk, Text, Button, Label
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ScrapeTagNavFallback:
    def __init__(self, driver):
        self.driver = driver

    def run_scrape_tag_nav_fallback(self, scrape_tag, user_profile):
        try:
            document_text = self.driver.find_element(By.TAG_NAME, "body").text

            # If "Go Back" exists
            if "Go Back" in document_text:
                self.navigate_back()
                time.sleep(2)

                # Check if the specific element exists
                if self.is_element_present(By.XPATH, "//html/body/div[3]/div/button"):
                    self.driver.find_element(By.XPATH, "//html/body/div[3]/div/button").click()

                # Call ProfileLinkGraber (assume implemented elsewhere)
                self.profile_link_graber()

                # Navigate to profile
                profile_xpath = f"//a[@href='/{user_profile}/'][.='Profile']"
                self.driver.find_element(By.XPATH, profile_xpath).click()

                # Wait and interact with various elements for scraping tags
                self.wait_and_click(By.XPATH,
                                    "//span[@id='react-root']/section/nav/div[2]/div/div/div[2]/div/div/span[1]")
                self.type_text(By.XPATH, "//input[@value='']", scrape_tag)

                self.wait_until_element_appears(By.XPATH,
                                                "//span[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]",
                                                5)

                # Process classes or specific elements based on documents
                classes = self.extract_classes(scrape_tag, document_text)

                if classes:
                    class_to_find = classes[0]  # Example: Taking the first match
                    tag_xpath = f"//span[@class='{class_to_find}'][.='{scrape_tag}']"
                    self.driver.find_element(By.XPATH, tag_xpath).click()

                self.wait_until_element_appears(By.XPATH, "//span[@id='react-root']/section/main/article/div[1]/h2", 5)

        except Exception as e:
            print(f"Error encountered: {e}")

    def navigate_back(self):
        self.driver.execute_script("window.history.back()")

    def is_element_present(self, by, locator):
        try:
            self.driver.find_element(by, locator)
            return True
        except:
            return False

    def profile_link_graber(self):
        # Placeholder implementation if this function interacts with the driver
        pass

    def wait_and_click(self, by, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, locator))).click()

    def type_text(self, by, locator, text):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, locator)))
        element.clear()
        element.send_keys(text)

    def wait_until_element_appears(self, by, locator, timeout):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))

    def extract_classes(self, scrape_tag, document_text):
        import re
        # Example pattern, adjust as needed:
        class_pattern = rf'(?<!<span\sclass=")[_a-z0-9\s]+(?=">{scrape_tag}</span>)'
        found_classes = re.findall(class_pattern, document_text)
        return found_classes


# Basic Tkinter UI
def setup_tkinter_ui():
    root = Tk()
    root.title("Web Scraper")

    # Text area for logs
    label = Label(root, text="Output Logs:")
    label.pack()

    text_area = Text(root, height=10, width=50)
    text_area.pack()

    # Start button functionality
    def start_scraping():
        text_area.insert("end", "Starting scraping...\n")

        # Example Selenium driver setup
        chrome_driver_path = "path_to_chromedriver"  # Replace this with the correct path
        driver = webdriver.Chrome(chrome_driver_path)

        # Open example website (replace with an actual URL)
        driver.get("https://example.com")

        # Initialize a scraper instance
        scraper = ScrapeTagNavFallback(driver)

        scrape_tag = "ExampleTag"  # Replace with the desired tag
        user_profile = "user123"  # Replace with the user profile value

        scraper.run_scrape_tag_nav_fallback(scrape_tag, user_profile)

        text_area.insert("end", "Scraping completed.\n")
        driver.quit()

    # Start button
    start_button = Button(root, text="Start Scraper", command=start_scraping)
    start_button.pack()

    # Run the UI loop
    root.mainloop()


# Initialize the UI
setup_tkinter_ui()

import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import messagebox


class CommTagNavFallBack:
    def __init__(self, driver, scrape_comm_tag, user_profile):
        self.driver = driver
        self.scrape_comm_tag = scrape_comm_tag
        self.user_profile = user_profile

    def profile_link_grabber(self):
        # Example implementation of ProfileLinkGraber logic
        print("ProfileLinkGraber action executed")

    def run(self):
        # Main logic to navigate and perform actions
        if "Go Back" in self.driver.page_source:
            self.navigate_back()
            if self.element_exists(By.XPATH, "//html/body/div[3]/div/button"):
                self.click_element(By.XPATH, "//html/body/div[3]/div/button")

            self.profile_link_grabber()
            self.click_element(By.XPATH, f"//a[@href='/{self.user_profile}/'][text()='Profile']")
            self.wait_for_element(By.XPATH,
                                  "//span[@id='react-root']/section/nav/div[2]/div/div/div[2]/div/div/span[1]",
                                  "Appear", timeout=5)
            self.click_element(By.XPATH,
                               "//span[@id='react-root']/section/nav/div[2]/div/div/div[2]/div/div/span[1]")
            self.type_text(By.XPATH, "//input[@value='']", self.scrape_comm_tag)
            self.wait_for_element(By.XPATH,
                                  "//span[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]",
                                  "Appear", timeout=5)

            page_source = self.driver.page_source

            # Extract and set class using regex
            scraped_class = self.extract_regex(
                page_source, r'(?!<span\sclass=")[_a-z0-9\s]+(?=">{})</span>'.format(self.scrape_comm_tag))

            input_class = self.extract_regex(
                page_source, r'(?!<input\stype="text"\sclass=")[_a-z0-9\s]+(?="\splaceholder="Search")')

            self.click_element(By.XPATH,
                               f"//span[@class='{scraped_class}'][text()='{self.scrape_comm_tag}']")
            self.wait_for_element(By.XPATH,
                                  "//span[@id='react-root']/section/main/article/div[1]/h2", "Appear",
                                  timeout=5)

    def navigate_back(self):
        self.driver.back()
        time.sleep(2)

    def element_exists(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except Exception:
            return False

    def click_element(self, by, value):
        try:
            element = self.driver.find_element(by, value)
            element.click()
        except Exception as e:
            print(f"Error clicking element {value}: {e}")

    def type_text(self, by, value, text):
        try:
            input_element = self.driver.find_element(by, value)
            input_element.clear()
            input_element.send_keys(text)
            input_element.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"Error typing text into element {value}: {e}")

    def wait_for_element(self, by, value, action, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            if action.lower() == "appear":
                wait.until(EC.presence_of_element_located((by, value)))
            elif action.lower() == "disappear":
                wait.until_not(EC.presence_of_element_located((by, value)))
        except Exception as e:
            print(f"Error waiting for element {value}: {e}")

    @staticmethod
    def extract_regex(text, pattern):
        match = re.search(pattern, text)
        if match:
            return match.group(0)
        else:
            return ""


def setup_driver(chrome_driver_path):
    """Setup Selenium WebDriver with Chrome browser."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    return driver


# Tkinter-based UI Interface
def setup_tkinter_ui():
    root = tk.Tk()
    root.title("Web Automation")

    # UI Elements
    tk.Label(root, text="Scrape Comm Tag:").pack()
    tag_entry = tk.Entry(root, width=50)
    tag_entry.pack()

    tk.Label(root, text="User Profile:").pack()
    profile_entry = tk.Entry(root, width=50)
    profile_entry.pack()

    def start_scraping():
        scrape_comm_tag = tag_entry.get()
        user_profile = profile_entry.get()

        if not scrape_comm_tag or not user_profile:
            messagebox.showerror("Error", "Both fields are required!")
            return

        chrome_driver_path = "path/to/chromedriver"  # Update with the path to your ChromeDriver

        driver = setup_driver(chrome_driver_path)
        try:
            driver.get("https://example.com")  # Replace with the actual URL
            fallback = CommTagNavFallBack(driver, scrape_comm_tag, user_profile)
            fallback.run()
        except Exception as e:
            print(f"Error during execution: {e}")
        finally:
            driver.quit()

    start_button = tk.Button(root, text="Start Scraping", command=start_scraping)
    start_button.pack()

    root.mainloop()


if __name__ == '__main__':
    setup_tkinter_ui()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


def validate_num_scrape():
    """Function to validate input and take actions for scraping."""
    # Assuming `number_to_scrape` is an input field from tkinter
    if number_to_scrape.get() == "":
        # Play system sound (Note: Windows only)
        try:
            import winsound
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        except ImportError:
            print("Sound playback not available on this platform.")

        # Log to text area
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text_area.insert(tk.END,
                         f"{current_time} - SOFTWARE STOPPED - PLEASE ENTER A NUMBER TO SCRAPE TO USE THIS FUNCTION - "
                         f"LOG RUNNING - INTERNALIZING COMPLETE - {current_time}\n")
        text_area.see(tk.END)

        # Show alert
        messagebox.showwarning("Input Error", "Please enter a number to scrape.")

        return  # Stop further script execution


# Root tkinter window setup
root = tk.Tk()
root.title("Number Validation and Scrape Tool")

# Input field
number_to_scrape = tk.StringVar()
entry = tk.Entry(root, textvariable=number_to_scrape)
entry.pack(pady=10)

# Text area for logging
text_area = tk.Text(root, height=15, width=80)
text_area.pack(pady=10)

# Button to trigger validation and potential scraping
validate_button = tk.Button(root, text="Validate and Scrape", command=validate_num_scrape)
validate_button.pack(pady=10)

# Main application loop
root.mainloop()
