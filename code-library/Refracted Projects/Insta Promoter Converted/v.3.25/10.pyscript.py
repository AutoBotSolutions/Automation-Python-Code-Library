from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import tkinter as tk
from tkinter import messagebox

# Global Variables Emulation
global_state = {
    "ActiveFunction": None,
    "image_paths": [],
    "image_captions": [],
    "post_schedule": [],
    "image_captions_pos": 0,
    "post_schedule_pos": 0,
    "image_paths_pos": 0,
    "master_delay_trigger": 0,
    "count_ui_display": 0,
    "display_running": "",
    "post_counter": 0,
    "delay_ticker": 0,
    "delay_time": 0,
}


def AppRunningModule():
    """Placeholder: Emulate `AppRunningModule` Function Behavior."""
    print("AppRunningModule Initialized")


def DateTimeLogStamp():
    """Returns the current time in a log-stamped format."""
    return time.strftime("%Y-%m-%d %H:%M:%S")


def add_to_list(target_list, source_list, delete_duplicates=False):
    """Utility function to add items from one list to another."""
    if delete_duplicates:
        target_list.extend(item for item in source_list if item not in target_list)
    else:
        target_list.extend(source_list)


def SetPostSystemUp():
    """Converted Functionality of SetPostSystemUp."""
    global global_state

    # Initialize AppRunningModule
    AppRunningModule()

    # Set Active Function (Using Selenium Example for HTTP Post)
    driver = webdriver.Firefox()
    try:
        driver.get(
            "http://app.tracking.softwareautomation.org/appstats/piwik.php?"
            f"&idsite=1&rec=1&_id=some-session-id&rand={int(time.time())}&apiv=1"
            "&action_name=[Running Post Module Function] Function Activated"
            "&url=http://app.tracking.org"
        )
        global_state["ActiveFunction"] = "HTTP GET completed"
    finally:
        driver.quit()

    # Reset Global State Lists
    global_state["post_schedule"].clear()
    global_state["image_paths"].clear()
    global_state["image_captions"].clear()

    # Load Data Folder Path
    uploads_path = os.path.join(os.getenv("APPDATA"), "uploads")
    if not os.path.exists(uploads_path):
        uploads_path = os.path.join(os.getenv("USERPROFILE"), "Documents", "Insta Promoter Data Folder", "uploads")

    image_files = [f for f in os.listdir(uploads_path) if os.path.isfile(os.path.join(uploads_path, f))]
    add_to_list(global_state["image_paths"], image_files)

    # Log Initialization
    log_message("SOFTWARE RUNNING - RESETTING ALL INTERNALIZED LIST AND PATHS - LOG RUNNING - INTERNALIZING COMPLETE")

    # Handle Image Paths
    if global_state["image_paths"]:
        log_message(
            "SOFTWARE RUNNING - YOUR POST IMAGES FOLDER HAS IMAGES BOTTING CAN COMMENCE - LOG RUNNING"
        )
    else:
        log_message(
            "SOFTWARE RUNNING - YOUR POST IMAGES FOLDER IS EMPTY PLEASE LOAD MORE IMAGES TO USE THE POST BOT - LOG RUNNING"
        )
        messagebox.showerror("Error", "Uploads folder is empty!")
        return

    # Handle Image Captions
    if global_state["image_captions"]:
        add_to_list(global_state["image_captions"], global_state["image_captions"])
        log_message(
            "SOFTWARE RUNNING - IMAGE CAPTIONS LIST DETECTED AND LOADED SUCCESSFULLY - LOG RUNNING"
        )
    else:
        log_message(
            "SOFTWARE RUNNING - CAPTIONS LIST NOT DETECTED PLEASE LOAD CAPTION FILE TO POST WITH CAPTIONS - LOG RUNNING"
        )

    # Handle Post Schedule
    if global_state["post_schedule"]:
        add_to_list(global_state["post_schedule"], global_state["post_schedule"])
        log_message(
            "SOFTWARE RUNNING - SCHEDULED DATE AND TIMESTAMPS DETECTED SCHEDULED POSTING CAN COMMENCE - LOG RUNNING"
        )
    else:
        log_message(
            "SOFTWARE RUNNING - DATE & TIME STAMPS NOT DETECTED PLEASE LOAD IF RUNNING SCHEDULED POSTS - LOG RUNNING"
        )

    # Reset Global Counters
    global_state.update({
        "image_captions_pos": 0,
        "post_schedule_pos": 0,
        "image_paths_pos": 0,
        "master_delay_trigger": 0,
        "count_ui_display": 0,
        "display_running": "",
        "post_counter": 0,
        "delay_ticker": 0,
        "delay_ticker": global_state["delay_time"],
    })


def log_message(message):
    """Logs a message to the tkinter UI."""
    timestamp = DateTimeLogStamp()
    full_message = f"{timestamp} - {message} - {timestamp}\n"
    print(full_message)  # Placeholder for actual UI element logging.


# Example Tkinter UI Setup
def create_ui():
    root = tk.Tk()
    root.title("Post System UI")

    # Log Textbox
    log_text = tk.Text(root, height=20, width=80)
    log_text.pack()

    # Buttons
    def start_system():
        log_text.insert(tk.END, "Starting Post System...\n")
        SetPostSystemUp()

    start_button = tk.Button(root, text="Start", command=start_system)
    start_button.pack()

    root.mainloop()


if __name__ == "__main__":
    create_ui()

import time
from tkinter import Tk, Text, Scrollbar, Button, StringVar, Label, END
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Define the application class
class InstagramUploader:

    def __init__(self):
        self.driver = None
        self.image_paths = []  # List of image paths to be uploaded
        self.image_captions = []  # List of captions for the images
        self.image_paths_pos = 0
        self.image_captions_pos = 0
        self.post_counter = 0
        self.stop_bot_at = 10  # Define how many posts before stopping
        self.create_ui()

    def start_browser(self):
        """Starts the Selenium webdriver."""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # Initialize WebDriver
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://instagram.com")

    def log_message(self, message: str):
        """Logs a message to the UI text box."""
        current_time = time.strftime("[%Y-%m-%d %H:%M:%S]")
        self.text_area.insert(END, f"{current_time} {message}\n")
        self.text_area.yview(END)

    def wait_for_element(self, xpath, appear=True, timeout=10):
        """Waits for an element to appear or disappear."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            if appear:
                wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            else:
                wait.until(EC.staleness_of(self.driver.find_element(By.XPATH, xpath)))
            return True
        except Exception as e:
            self.log_message(f"Error waiting for element: {e}")
            return False

    def click_element(self, xpath):
        """Clicks an element by its XPath."""
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.click()
        except Exception as e:
            self.log_message(f"Error clicking element: {e}")

    def upload_file(self, xpath, file_path):
        """Handles file upload."""
        try:
            file_input = self.driver.find_element(By.XPATH, xpath)
            file_input.send_keys(file_path)
        except Exception as e:
            self.log_message(f"Error during file upload: {e}")

    def post_image(self):
        """Main function to handle the image posting process."""
        # Navigate to upload section
        self.click_element('//span[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/div')
        self.log_message("Navigated to Upload Section.")
        time.sleep(4)

        # Upload image
        current_image_path = self.image_paths[self.image_paths_pos]
        self.upload_file("//input[@type='file']", current_image_path)
        self.log_message(f"Uploading image: {current_image_path}")

        # Wait for the upload to complete
        if not self.wait_for_element("//button/span[contains(text(),'Next')]", appear=True, timeout=10):
            self.log_message("Error: Upload did not complete in time.")
            return

        self.click_element("//button/span[contains(text(),'Next')]")  # First 'Next'

        # Add caption if available
        if self.image_captions_pos < len(self.image_captions):
            current_caption = self.image_captions[self.image_captions_pos]
            caption_box = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Write a caption…']")
            caption_box.send_keys(current_caption)
            self.log_message(f"Added caption: {current_caption}")

        self.click_element("//button[contains(text(),'Share')]")  # Click 'Share'
        self.log_message("Image post shared successfully!")

        # Wait for post confirmation
        if not self.wait_for_element("//span[contains(text(),'View'), 'More options')]", appear=True, timeout=10):
            self.log_message("Error: Could not confirm post success.")
            return

        # Log post success
        self.post_counter += 1
        self.log_message(f"Post count updated: {self.post_counter}")

        # Stop criteria
        if self.post_counter >= self.stop_bot_at:
            self.log_message("Stopping... Reached maximum posts.")
            self.driver.quit()

        # Update counters
        self.image_paths_pos += 1
        self.image_captions_pos += 1

    def create_ui(self):
        """Sets up the tkinter user interface."""
        self.root = Tk()
        self.root.title("Instagram Uploader")

        Label(self.root, text="Instagram Automation").pack()

        # Text area with scrolling
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side="right", fill="y")

        self.text_area = Text(self.root, wrap="word", yscrollcommand=scrollbar.set, height=20, width=60)
        self.text_area.pack()
        scrollbar.config(command=self.text_area.yview)

        # Buttons
        Button(self.root, text="Start", command=self.start_bot).pack()
        Button(self.root, text="Exit", command=self.root.quit).pack()

        self.root.mainloop()

    def start_bot(self):
        """Starts the Instagram bot."""
        self.log_message("Starting browser and automation process...")
        self.start_browser()
        self.post_image()
        self.log_message("Automation process completed.")


if __name__ == "__main__":
    app = InstagramUploader()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import messagebox


class InstagramUploader:
    def __init__(self):
        self.driver = None
        self.root = tk.Tk()
        self.text_area = None
        self.image_paths = []
        self.image_paths_pos = 0
        self.image_captions = []
        self.image_captions_pos = 0
        self.post_counter = 0
        self.stop_bot_at = 0

    def start_browser(self):
        self.driver = webdriver.Chrome()  # Path to your chrome driver
        self.driver.get("https://instagram.com")
        self.log_message("Browser started and navigated to Instagram.")

    def log_message(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {message}\n"
        if self.text_area:
            self.text_area.insert(tk.END, log_entry)
            self.text_area.see(tk.END)
        print(log_entry)  # Output log to console as well.

    def wait_for_element(self, xpath, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            self.log_message(f"Error waiting for element: {e}")
            return None

    def click_element(self, xpath):
        element = self.wait_for_element(xpath)
        if element:
            element.click()
            self.log_message(f"Clicked element at '{xpath}'.")

    def upload_file(self, filepath, input_xpath):
        try:
            file_input = self.wait_for_element(input_xpath)
            if file_input:
                file_input.send_keys(filepath)
                self.log_message(f"Uploaded file: {filepath}")
        except Exception as e:
            self.log_message(f"Error uploading file: {e}")

    def post_image(self):
        while self.image_paths_pos < len(self.image_paths):
            # Log starting of post process
            self.log_message("Starting post upload process...")

            # Access image and caption data
            current_image = self.image_paths[self.image_paths_pos]
            current_caption = None
            if self.image_captions_pos < len(self.image_captions):
                current_caption = self.image_captions[self.image_captions_pos]

            # Clicking button to trigger upload/start process
            self.click_element("x://span[@id='react-root']/section/nav[2]/div/div/div[2]/div/div/div[3]/div")

            # Uploading the file
            self.upload_file(current_image, "//input[@type='file']")
            time.sleep(2)  # Wait for the upload to complete

            # Adding a caption if available
            if current_caption:
                caption_field = self.wait_for_element("//textarea[@placeholder='Write a caption…']")
                if caption_field:
                    caption_field.send_keys(current_caption)
                    self.log_message(f"Caption added: {current_caption}")
                else:
                    self.log_message("No caption provided.")

            # Finalize posting
            self.click_element("x://span[@id='react-root']/section/div[1]/header/div[2]/button")
            time.sleep(3)

            # Increment positions
            self.image_paths_pos += 1
            if current_caption:
                self.image_captions_pos += 1

            # Log post success
            self.post_counter += 1
            self.log_message(f"Post #{self.post_counter} uploaded successfully.")

            # Stop the bot if reached the defined limit
            if self.post_counter >= self.stop_bot_at > 0:
                self.log_message("Post limit reached. Stopping bot...")
                break

    def create_ui(self):
        self.root.title("Instagram Uploader")

        # Text area for log messages
        self.text_area = tk.Text(self.root, state='normal', width=80, height=20)
        self.text_area.pack()

        # Start Button
        start_button = tk.Button(self.root, text="Start Bot", command=self.start_bot)
        start_button.pack()

        # Stop Button
        stop_button = tk.Button(self.root, text="Stop Bot", command=self.stop_bot)
        stop_button.pack()

    def start_bot(self):
        self.log_message("Starting bot...")
        self.start_browser()
        self.post_image()

    def stop_bot(self):
        self.log_message("Stopping bot...")
        if self.driver:
            self.driver.quit()
        self.root.quit()


# Instantiate and run the application
if __name__ == "__main__":
    app = InstagramUploader()
    app.create_ui()
    app.root.mainloop()

import tkinter as tk
import threading
from datetime import datetime
from time import sleep
from selenium import webdriver


class InstagramUploader:
    def __init__(self):
        self.root = tk.Tk()
        self.text_area = tk.Text(self.root, wrap=tk.WORD, height=20, width=80)
        self.text_area.pack()
        self.stop_schedule = False
        self.driver = None
        self.post_schedule = []
        self.post_schedule_pos = 0

    def log_message(self, message):
        """Append the log messages to the text area and scroll."""
        current_time = datetime.now().strftime("%H:%M:%S")
        log_entry = f"{current_time} - {message}\n"
        self.text_area.insert(tk.END, log_entry)
        self.text_area.see(tk.END)

    def start_browser(self):
        """Start the Selenium web browser."""
        self.log_message("Starting browser...")
        self.driver = webdriver.Chrome()  # Use the appropriate driver for the browser
        self.log_message("Browser started.")

    def stop_scheduler(self):
        """Stop the scheduler loop."""
        self.stop_schedule = True
        self.log_message("Stopping scheduler...")

    def scheduler_trigger(self):
        """Main scheduler logic."""
        self.log_message("SCHEDULER TRIGGERS HAVE BEEN INITIATED.")

        while not self.stop_schedule:
            current_date_time = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
            self.log_message(f"Current Date/Time: {current_date_time}")

            # Simulate post scheduler logic
            if self.post_schedule:
                try:
                    next_post_in = self.post_schedule[self.post_schedule_pos]
                except IndexError:
                    next_post_in = "No scheduled posts"

                self.log_message(f"Next Post In: {next_post_in}s")
            else:
                self.log_message("No scheduled posts available.")

            sleep(0.1)

        self.log_message("SCHEDULER STOPPED.")

    def start_scheduler(self):
        """Launch the scheduler in a separate thread."""
        self.stop_schedule = False
        scheduler_thread = threading.Thread(target=self.scheduler_trigger)
        scheduler_thread.daemon = True
        scheduler_thread.start()

    def create_ui(self):
        """Create the user interface."""
        start_button = tk.Button(
            self.root,
            text="Start Scheduler",
            command=self.start_scheduler,
        )
        start_button.pack(pady=5)

        stop_button = tk.Button(
            self.root,
            text="Stop Scheduler",
            command=self.stop_scheduler,
        )
        stop_button.pack(pady=5)

        self.log_message("UI Initialized.")
        self.root.mainloop()


# Main application logic
if __name__ == "__main__":
    app = InstagramUploader()
    app.create_ui()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import os


class InstagramUploader:
    def __init__(self):
        self.driver = None
        self.root = tk.Tk()
        self.text_area = tk.Text(self.root, height=20, width=80)
        self.text_area.pack()
        self.post_options = None
        self.account_file = None
        self.image_captions = None
        self.post_schedule = None
        self.num_post_now = None
        self.stop_bot_at = None
        self.delay_time = None
        self.schedule_trigger = None
        self.create_ui()

    def log_message(self, message):
        """
        Logs a message to the TextArea in the UI and appends timestamp.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - {message}\n"
        self.text_area.insert(tk.END, log_message)
        self.text_area.see(tk.END)
        print(log_message)  # for debugging purposes

    def create_ui(self):
        """
        Creates the UI for the Instagram Bot.
        """
        self.root.title("Instagram Post Bot")

        # Buttons to trigger actions
        run_bot_btn = tk.Button(self.root, text="Run Bot", command=self.start_bot)
        run_bot_btn.pack()

        # Dropdown for post options
        self.post_options_var = tk.StringVar(self.root)
        self.post_options_var.set("Select Post Option")
        post_options_menu = tk.OptionMenu(self.root, self.post_options_var, "Post Now", "On Schedule")
        post_options_menu.pack()

        # Entry field for account file
        tk.Label(self.root, text="Account File:").pack()
        self.account_file_entry = tk.Entry(self.root)
        self.account_file_entry.pack()

        # Entry field for caption file
        tk.Label(self.root, text="Caption File:").pack()
        self.caption_file_entry = tk.Entry(self.root)
        self.caption_file_entry.pack()

        # Entry field for number of posts
        tk.Label(self.root, text="Number of Posts (Post Now):").pack()
        self.num_post_now_entry = tk.Entry(self.root)
        self.num_post_now_entry.pack()

        # Entry field for delay time
        tk.Label(self.root, text="Delay Time (seconds):").pack()
        self.delay_time_entry = tk.Entry(self.root)
        self.delay_time_entry.pack()

    def start_browser(self):
        """
        Launches the Selenium WebDriver and opens the Instagram login page.
        """
        self.driver = webdriver.Chrome()  # Update to the correct driver path
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")

    def wait_for_element(self, locator, wait_time=10):
        """
        Waits for an element to appear on the page.
        """
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            self.log_message("Element not found within the given time.")

    def start_bot(self):
        """
        Main function to start the bot based on parameters.
        """
        self.log_message("SOFTWARE RUNNING - INSTAGRAM POST BOT STARTED SUCCESSFULLY")

        self.post_options = self.post_options_var.get()
        self.account_file = self.account_file_entry.get()
        self.image_captions = self.caption_file_entry.get()
        self.num_post_now = self.num_post_now_entry.get()
        self.delay_time = self.delay_time_entry.get()

        # Validate inputs
        if self.post_options == "Select Post Option":
            self.log_message(
                "TO USE THE POST BOT YOU MUST FIRST SELECT A POST OPTION FROM THE DROPDOWN"
            )
            messagebox.showerror("Error", "Please select a post option.")
            return

        if not self.account_file:
            self.log_message("TO USE THE POST BOT YOU MUST FIRST SELECT YOUR ACCOUNT FILE")
            messagebox.showerror("Error", "Account file is required.")
            return

        # Check for Post Now settings
        if self.post_options == "Post Now":
            if not self.num_post_now.isdigit():
                self.log_message(
                    "TO USE THE POST NOW SETTING ENTER A NUMBER IN THE BOX TO POST NOW BOX"
                )
                messagebox.showerror("Error", "Please enter a valid number.")
                return

            if not self.delay_time.isdigit():
                self.log_message(
                    "TO USE THE POST NOW SETTING ENTER A NUMBER IN THE DELAY BOX TO DELAY YOUR POSTS"
                )
                messagebox.showerror("Error", "Please enter a valid delay time.")
                return

            self.log_message(
                f"Starting to post {self.num_post_now} images with a delay of {self.delay_time}s."
            )
            # Add further implementation for posting images

        # Check for Schedule settings
        elif self.post_options == "On Schedule":
            self.schedule_trigger = True  # A placeholder for scheduling logic
            if not self.schedule_trigger:
                self.log_message("PLEASE PRESS THE RUN SCHEDULE BUTTON BEFORE LOGGING IN WITH THE BOT")
                messagebox.showerror("Error", "Run Schedule Trigger is missing.")
                return

            if not self.post_schedule:
                self.log_message(
                    "PLEASE ADD YOUR DATE AND TIME STAMPS INTO THE POST SCHEDULED BOX"
                )
                messagebox.showerror("Error", "Schedule time is required.")
                return

            self.log_message("Scheduled Posting Started.")
            # Add further implementation for scheduled posting

    def stop_bot(self):
        """
        Stops the bot if running.
        """
        if self.driver:
            self.driver.quit()
        self.log_message("Bot Stopped.")

    def run(self):
        """
        Runs the main Tkinter loop.
        """
        self.root.mainloop()


# Start the bot
if __name__ == "__main__":
    uploader = InstagramUploader()
    uploader.run()


