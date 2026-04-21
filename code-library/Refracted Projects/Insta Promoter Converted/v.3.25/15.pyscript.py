import time
from tkinter import Tk, Text, Button, Scrollbar, END, RIGHT, Y, LEFT, BOTH
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class MultiToolBot:
    def __init__(self, log_textarea):
        self.log_textarea = log_textarea
        self.driver = None
        self.session_id = '123456'  # Example session ID placeholder
        self.master_delay_trigger = 0
        self.follow_counter = 0
        self.like_counter = 0
        self.comment_counter = 0
        self.initialize_driver()

    def initialize_driver(self):
        """Initialize the Selenium WebDriver."""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.log("WebDriver initialized.")

    def log(self, message):
        """Log messages to the Tkinter UI text area."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_textarea.insert(END, f"{timestamp} - {message}\n")
        self.log_textarea.see(END)

    def follow_user(self, username):
        """Simulate the Follow function using Selenium."""
        try:
            # Example code to go to a user's profile and follow
            self.driver.get(f"https://www.instagram.com/{username}/")
            time.sleep(2)
            follow_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Follow')]")
            follow_button.click()
            time.sleep(1)

            # Confirm Follow success
            if "Following" in self.driver.page_source:
                self.follow_counter += 1
                self.log(f"The bot successfully followed the user [{username}]. Total follows: {self.follow_counter}.")
            else:
                self.log(f"Failed to follow the user [{username}].")
        except Exception as e:
            self.log(f"Error in follow_user: {e}")

    def like_post(self, post_url):
        """Simulate the Like function using Selenium."""
        try:
            # Example logic to like an Instagram post
            self.driver.get(post_url)
            time.sleep(2)
            like_button = self.driver.find_element(By.XPATH, "//span[@aria-label='Like']")
            like_button.click()
            time.sleep(1)

            # Confirm Like success
            if "Unlike" in self.driver.page_source:
                self.like_counter += 1
                self.log(f"The bot successfully liked the post. Total likes: {self.like_counter}.")
            else:
                self.log("Failed to like the post.")
        except Exception as e:
            self.log(f"Error in like_post: {e}")

    def comment_post(self, post_url, comment_text):
        """Simulate the Comment function using Selenium."""
        try:
            # Example logic to comment on an Instagram post
            self.driver.get(post_url)
            time.sleep(2)
            comment_field = self.driver.find_element(By.XPATH, "//textarea[@aria-label='Add a comment…']")
            comment_field.click()
            comment_field.send_keys(comment_text)
            comment_field.send_keys(Keys.RETURN)
            time.sleep(1)

            # Confirm Comment success
            if comment_text in self.driver.page_source:
                self.comment_counter += 1
                self.log(f"The bot successfully commented on the post. Total comments: {self.comment_counter}.")
            else:
                self.log("Failed to comment on the post.")
        except Exception as e:
            self.log(f"Error in comment_post: {e}")

    def close_bot(self):
        """Close the Selenium driver."""
        if self.driver:
            self.driver.quit()
            self.log("WebDriver closed.")


# Tkinter GUI
class MultiToolGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Multi Tool Bot")
        self.create_widgets()
        self.bot = MultiToolBot(self.log_textarea)

    def create_widgets(self):
        """Create the Tkinter UI elements."""
        self.log_textarea = Text(self.root, wrap="word", height=20, width=80)
        self.log_textarea.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(self.root, command=self.log_textarea.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.log_textarea.config(yscrollcommand=scrollbar.set)

        self.start_follow_button = Button(self.root, text="Follow User", command=self.start_follow)
        self.start_follow_button.pack(side=LEFT, padx=5, pady=5)

        self.start_like_button = Button(self.root, text="Like Post", command=self.start_like)
        self.start_like_button.pack(side=LEFT, padx=5, pady=5)

        self.start_comment_button = Button(self.root, text="Comment Post", command=self.start_comment)
        self.start_comment_button.pack(side=LEFT, padx=5, pady=5)

        self.exit_button = Button(self.root, text="Exit", command=self.exit_program)
        self.exit_button.pack(side=LEFT, padx=5, pady=5)

    def start_follow(self):
        """Start the follow functionality."""
        # Replace 'example_user' with user input in the real implementation
        self.bot.log("Starting Follow Function.")
        self.bot.follow_user("example_user")

    def start_like(self):
        """Start the like functionality."""
        # Replace 'example_url' with user input in the real implementation
        self.bot.log("Starting Like Function.")
        self.bot.like_post("https://www.instagram.com/p/example_post/")

    def start_comment(self):
        """Start the comment functionality."""
        # Replace 'example_url' and 'example_comment' with user input in the real implementation
        self.bot.log("Starting Comment Function.")
        self.bot.comment_post("https://www.instagram.com/p/example_post/", "Nice post!")

    def exit_program(self):
        """Exit the application."""
        self.bot.close_bot()
        self.root.destroy()


if __name__ == "__main__":
    gui = MultiToolGUI()
    gui.root.mainloop()

import time
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class MultiToolBot:
    def __init__(self, driver, log_textarea, session_id):
        self.driver = driver
        self.log_textarea = log_textarea
        self.session_id = session_id
        self.master_delay_trigger = 0
        self.like_counter = 0
        self.comment_counter = 0

    def log(self, message):
        """Log the activity in the log_textarea"""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.log_textarea.insert("end", f"{timestamp} - {message}\n")
        self.log_textarea.see("end")

    def like_post(self):
        """Automates liking a post."""
        try:
            # Check if "Unlike" button does not exist
            if not self._element_exists(By.XPATH, "//button[contains(text(), 'Unlike')]"):
                self._execute_like()
        except Exception as e:
            self.log(f"Error during liking post: {e}")

    def comment_post(self, comment_text):
        """Automates commenting on a post."""
        try:
            # Check if "Delete Comment" button does not exist
            if not self._element_exists(By.XPATH, "//button[contains(text(), 'Delete Comment')]"):
                self._execute_comment(comment_text)
        except Exception as e:
            self.log(f"Error during commenting post: {e}")

    def _execute_like(self):
        """Executes the like action."""
        try:
            like_button = self.driver.find_element(By.XPATH,
                                                   "//span[@id='react-root']/section/main/div/div/article/div[2]/section[1]/a[1]/span")
            ActionChains(self.driver).scroll_to_element(like_button).click().perform()
            self.wait_for_condition(lambda: self._element_exists(By.XPATH, "//button[contains(text(), 'Unlike')]"),
                                    timeout=10)
            self.like_counter += 1
            self.master_delay_trigger += 1
            self.log(f"The software has successfully liked the post. Total likes: {self.like_counter}")
        except NoSuchElementException:
            self.log("Like button not found.")
        except TimeoutError:
            self.log("Timeout waiting for like action to complete.")

    def _execute_comment(self, comment_text):
        """Executes the comment action."""
        try:
            comment_box = self.driver.find_element(By.XPATH, "//textarea[contains(@aria-label, 'Add a comment')]")
            comment_box.clear()
            comment_box.send_keys(comment_text)
            comment_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Post')]")
            comment_button.click()
            self.wait_for_condition(lambda: comment_text in self.driver.page_source, timeout=10)
            self.comment_counter += 1
            self.master_delay_trigger += 1
            self.log(
                f"The software has successfully commented: '{comment_text}'. Total comments: {self.comment_counter}")
        except NoSuchElementException:
            self.log("Comment box or Post button not found.")
        except TimeoutError:
            self.log("Timeout waiting for comment action to complete.")

    def _element_exists(self, by, value):
        """Checks if an element exists in the DOM."""
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    def wait_for_condition(self, condition, timeout=10):
        """Waits for a specific condition to become True."""
        start_time = time.time()
        while time.time() - start_time < timeout:
            if condition():
                return
            time.sleep(0.1)
        raise TimeoutError("Condition not met within the timeout period.")

    def close_bot(self):
        """Closes the bot and webdriver."""
        self.driver.quit()


class MultiToolGUI:
    def __init__(self, root, bot):
        self.root = root
        self.bot = bot
        self.log_textarea = None
        self.create_widgets()

    def create_widgets(self):
        """Creates the UI for the bot."""
        self.log_textarea = tk.Text(self.root, width=80, height=20)
        self.log_textarea.pack()

        start_like_button = tk.Button(self.root, text="Start Like", command=self.start_like)
        start_like_button.pack()

        start_comment_button = tk.Button(self.root, text="Start Comment", command=self.start_comment)
        start_comment_button.pack()

        exit_button = tk.Button(self.root, text="Exit", command=self.exit_program)
        exit_button.pack()

    def start_like(self):
        """Starts the like automation."""
        threading.Thread(target=self.bot.like_post).start()

    def start_comment(self):
        """Starts the comment automation."""
        comment_text = "Amazing post!"  # Replace with dynamic input if needed
        threading.Thread(target=self.bot.comment_post, args=(comment_text,)).start()

    def exit_program(self):
        """Exits the program."""
        self.bot.close_bot()
        self.root.quit()


# Example initialization
if __name__ == "__main__":
    import tkinter as tk
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.chrome.webdriver import Options

    # Initialize Selenium WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to Instagram (or target URL)
    driver.get("https://www.instagram.com")

    # Setup the bot and GUI
    root = tk.Tk()
    root.title("Multi Tool Bot")
    log_textarea = tk.Text(root)

    bot = MultiToolBot(driver, log_textarea, session_id="example_session_id")
    app = MultiToolGUI(root, bot)
    root.mainloop()

import time
from tkinter import Tk, Text, Button, END
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MultiToolBot:
    def __init__(self, driver, log_textarea):
        self.driver = driver
        self.log_textarea = log_textarea
        self.follow_counter = 0
        self.comment_counter = 0
        self.master_delay_trigger = 0

    def log(self, message):
        """
        Logs a message in the GUI log textarea in a thread-safe way.
        """
        time_log = time.strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{time_log} - {message}\n"
        self.log_textarea.insert(END, log_message)
        self.log_textarea.see(END)

    def follow_user(self, user_url):
        """
        Completes the user follow logic.
        """
        try:
            self.driver.get(user_url)
            time.sleep(2)  # Wait for page load

            # Check if user is already followed
            if not self._element_exists(By.XPATH, '//button[contains(text(), "Following")]'):
                follow_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Follow")]'))
                )
                follow_button.click()

                self.log("Waiting for follow request to complete...")
                # Wait process logic
                wait_counter = 0
                while not self._element_exists(By.XPATH, '//button[contains(text(), "Following")]'):
                    wait_counter += 1
                    time.sleep(0.1)
                    if wait_counter >= 100:  # Timeout
                        self.log("Follow request timeout reached.")
                        return False

                self.follow_counter += 1
                self.log(f"Successfully followed user at {user_url}. Total follows: {self.follow_counter}")
                self.master_delay_trigger += 1
                return True
            else:
                self.log("User already followed.")
                return False
        except Exception as e:
            self.log(f"Error following user: {str(e)}")
            return False

    def comment_post(self, post_url, comment_text):
        """
        Completes the post commenting logic.
        """
        try:
            self.driver.get(post_url)
            time.sleep(2)  # Wait for page load

            # Find comment box and submit a comment
            comment_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//textarea[@aria-label="Add a comment…"]'))
            )
            comment_box.send_keys(comment_text)
            comment_box.submit()  # Submit the comment

            self.log("Waiting for comment action to complete...")
            # Confirm comment is visible or completes successfully
            time.sleep(2)  # Wait briefly to simulate confirmation

            self.comment_counter += 1
            self.log(f"Successfully commented: '{comment_text}' on {post_url}. Total comments: {self.comment_counter}")
            self.master_delay_trigger += 1
            return True

        except Exception as e:
            self.log(f"Error commenting on post: {str(e)}")
            return False

    def _element_exists(self, by, value):
        """
        Utility method to check if element exists by locator.
        """
        try:
            self.driver.find_element(by, value)
            return True
        except Exception:
            return False

    def close_bot(self):
        """
        Safely closes the Selenium webdriver.
        """
        self.driver.quit()


class MultiToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Tool Bot")
        self.log_textarea = Text(root, height=15, width=80)
        self.log_textarea.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Placeholder for Selenium WebDriver initialization
        self.bot = None

        # Create UI widgets
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the interface buttons and logic.
        """
        Button(self.root, text="Start Follow", command=self.start_follow).grid(row=1, column=0, padx=10, pady=5)
        Button(self.root, text="Start Comment", command=self.start_comment).grid(row=1, column=1, padx=10, pady=5)
        Button(self.root, text="Exit", command=self.exit_program).grid(row=1, column=2, padx=10, pady=5)

    def start_follow(self):
        """
        Button callback to start following logic.
        """
        if not self.bot:
            self.log_textarea.insert(END, "Bot not initialized.\n")
            return

        user_url = "https://instagram.com/example_user/"  # Replace with the actual user URL
        self.bot.follow_user(user_url)

    def start_comment(self):
        """
        Button callback to start commenting logic.
        """
        if not self.bot:
            self.log_textarea.insert(END, "Bot not initialized.\n")
            return

        post_url = "https://instagram.com/example_post/"  # Replace with the actual post URL
        comment_text = "Great post!"  # Replace with the actual comment
        self.bot.comment_post(post_url, comment_text)

    def exit_program(self):
        """
        Button callback to exit the program.
        """
        if self.bot:
            self.bot.close_bot()
        self.root.destroy()


# Basic Setup
if __name__ == "__main__":
    root = Tk()
    gui = MultiToolGUI(root)

    # Initialize Selenium WebDriver (Example only, driver setup is required based on your environment)
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.chrome.webdriver import WebDriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument("--headless")  # Run in headless mode if desired
    service = ChromeService(executable_path='/path/to/chromedriver')  # Set the ChromeDriver path
    driver = WebDriver(service=service, options=options)

    # Pass driver and UI log to bot
    gui.bot = MultiToolBot(driver, gui.log_textarea)

    # Start the Tkinter main loop
    root.mainloop()

from tkinter import Tk, Text, Button, Scrollbar, VERTICAL, END
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# MultiToolBot Class: Handles Selenium operations for follow and like functionality.
class MultiToolBot:
    def __init__(self, log_textarea):
        self.log_textarea = log_textarea
        self.driver = None
        self.follow_counter = 0
        self.like_counter = 0
        self.master_delay_trigger = 0
        self.session_id = time.time()  # For demonstration purposes

    def initialize_driver(self):
        """ Initialize the Selenium WebDriver. """
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Comment this line for debugging
        options.add_argument('--log-level=3')
        service = ChromeService("path_to_chromedriver")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.log("WebDriver initialized.")

    def log(self, message):
        """ Log messages to the Tkinter UI and the console. """
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_message = f"{timestamp} - {message}\n"
        self.log_textarea.insert(END, log_message)
        self.log_textarea.see(END)

    def follow_user(self, username):
        """ Follow a specific user. """
        self.log(f"Attempting to follow user: {username}...")
        self.driver.get(f"https://www.instagram.com/{username}/")

        try:
            # Wait for the Follow button to appear
            follow_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Follow']"))
            )
            follow_button.click()
            self.log(f"Successfully followed user: {username}")
            self.follow_counter += 1
        except Exception as e:
            self.log(f"Error following user {username}: {e}")

    def like_post(self, post_url):
        """ Like a specific post. """
        self.log(f"Attempting to like post: {post_url}...")
        self.driver.get(post_url)

        try:
            # Wait for the Like button and click it
            like_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Like']"))
            )
            ActionChains(self.driver).move_to_element(like_button).click().perform()
            self.log(f"Successfully liked post: {post_url}")
            self.like_counter += 1
        except Exception as e:
            self.log(f"Error liking post {post_url}: {e}")

    def close_bot(self):
        """ Close the Selenium WebDriver. """
        if self.driver:
            self.driver.quit()
        self.log("WebDriver closed.")


# MultiToolGUI Class: Handles Tkinter UI for interacting with the bot functions.
class MultiToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Multi-Tool Bot")
        self.bot = None  # The bot instance
        self.log_textarea = None
        self.create_widgets()

    def create_widgets(self):
        """ Create UI components. """
        # Log display
        self.log_textarea = Text(self.root, wrap='word', height=20, width=70)
        self.log_textarea.grid(row=0, column=0, pady=10, padx=10, columnspan=3)

        # Scrollbar for log
        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.log_textarea.yview)
        self.log_textarea.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=3, sticky='ns')

        # Control buttons
        start_follow_button = Button(self.root, text="Start Follow", command=self.start_follow)
        start_follow_button.grid(row=1, column=0, pady=10, padx=10)

        start_like_button = Button(self.root, text="Start Like", command=self.start_like)
        start_like_button.grid(row=1, column=1, pady=10, padx=10)

        exit_button = Button(self.root, text="Exit", command=self.exit_program)
        exit_button.grid(row=1, column=2, pady=10, padx=10)

    def initialize_bot(self):
        """ Initialize the bot if not already initialized. """
        if not self.bot:
            self.bot = MultiToolBot(self.log_textarea)
            self.bot.initialize_driver()

    def start_follow(self):
        """ Start the follow operation. """
        self.initialize_bot()
        usernames = ["user1", "user2"]  # Replace with the list of usernames to follow
        for username in usernames:
            self.bot.follow_user(username)

    def start_like(self):
        """ Start the like operation. """
        self.initialize_bot()
        post_urls = ["https://www.instagram.com/p/xxxxx/",
                     "https://www.instagram.com/p/yyyyy/"]  # Replace with post URLs
        for post_url in post_urls:
            self.bot.like_post(post_url)

    def exit_program(self):
        """ Exit the application. """
        if self.bot:
            self.bot.close_bot()
        self.root.destroy()


# Main Application Execution
if __name__ == "__main__":
    root = Tk()
    app = MultiToolGUI(root)
    root.mainloop()


