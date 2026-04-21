import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class SocialMediaAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Automation Tool")

        # Initialize variables for UI elements
        self.num_follow = tk.StringVar()
        self.enable_following = tk.BooleanVar()
        self.follow_list_queue = tk.StringVar(value="0")
        self.follow_list_counter = tk.StringVar(value="0")

        self.num_like = tk.StringVar()
        self.enable_likes = tk.BooleanVar()
        self.like_queue = tk.StringVar(value="0")
        self.like_counter = tk.StringVar(value="0")

        self.num_comment = tk.StringVar()
        self.enable_commenting = tk.BooleanVar()
        self.comment_queue = tk.StringVar(value="0")
        self.comment_counter = tk.StringVar(value="0")

        self.num_multi_actions = tk.StringVar()
        self.enable_multi_tool = tk.BooleanVar()
        self.multi_tool_queue = tk.StringVar(value="0")
        self.multi_action_counter = tk.StringVar(value="0")

        self.num_unfollow = tk.StringVar()
        self.enable_unfollowing = tk.BooleanVar()
        self.unfollow_list_queue = tk.StringVar(value="0")
        self.unfollow_list_counter = tk.StringVar(value="0")

        # Build UI
        self.build_ui()

    def build_ui(self):
        row = 0
        # Inputs and actions for following
        tk.Label(self.root, text="Number To Follow (list):").grid(row=row, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.num_follow).grid(row=row, column=1, sticky="w")

        tk.Checkbutton(self.root, text="Enable Following", variable=self.enable_following).grid(row=row, column=2,
                                                                                                sticky="w")

        row += 1
        tk.Label(self.root, text="Users In Queue:", fg="#00AEEF").grid(row=row, column=0, sticky="w")
        tk.Label(self.root, textvariable=self.follow_list_queue).grid(row=row, column=1, sticky="w")

        row += 1
        tk.Label(self.root, text="Follows Complete:", fg="#00AEEF").grid(row=row, column=0, sticky="w")
        tk.Label(self.root, textvariable=self.follow_list_counter).grid(row=row, column=1, sticky="w")

        row += 1

        # Inputs and actions for liking
        tk.Label(self.root, text="Number To Like (list):").grid(row=row, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.num_like).grid(row=row, column=1, sticky="w")

        tk.Checkbutton(self.root, text="Enable Liking", variable=self.enable_likes).grid(row=row, column=2, sticky="w")

        row += 1
        tk.Label(self.root, text="Users In Queue:", fg="#FFA500").grid(row=row, column=0, sticky="w")
        tk.Label(self.root, textvariable=self.like_queue).grid(row=row, column=1, sticky="w")

        row += 1
        tk.Label(self.root, text="Likes Complete:", fg="#FFA500").grid(row=row, column=0, sticky="w")
        tk.Label(self.root, textvariable=self.like_counter).grid(row=row, column=1, sticky="w")

        row += 1

        # Inputs and actions for commenting
        tk.Label(self.root, text="Number To Comment (list):").grid(row=row, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.num_comment).grid(row=row, column=1, sticky="w")

        tk.Checkbutton(self.root, text="Enable Commenting", variable=self.enable_commenting).grid(row=row, column=2,
                                                                                                  sticky="w")

        row += 1
        tk.Label(self.root, text="Users In Queue:", fg="#008000").grid(row=row, column=0, sticky="w")
        tk.Label(self.root, textvariable=self.comment_queue).grid(row=row, column=1, sticky="w")

        row += 1
        tk.Label(self.root, text="Comments Complete:", fg="#008000").grid(row=row, column=0, sticky="w")
        tk.Label(self.root, textvariable=self.comment_counter).grid(row=row, column=1, sticky="w")

        row += 1

        # Inputs and actions for unfollowing
        tk.Label(self.root, text="Number To Unfollow (list):").grid(row=row, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.num_unfollow).grid(row=row, column=1, sticky="w")

        tk.Checkbutton(self.root, text="Enable Unfollowing", variable=self.enable_unfollowing).grid(row=row, column=2,
                                                                                                    sticky="w")

        row += 1
        tk.Label(self.root, text="Users In Queue:", fg="#800080").grid(row=row, column=0, sticky="w")
        tk.Label(self.root, textvariable=self.unfollow_list_queue).grid(row=row, column=1, sticky="w")

        row += 1
        tk.Label(self.root, text="Unfollows Complete:", fg="#800080").grid(row=row, column=0, sticky="w")
        tk.Label(self.root, textvariable=self.unfollow_list_counter).grid(row=row, column=1, sticky="w")

        row += 1

        # Settings Button
        tk.Button(self.root, text="Open Settings", command=self.open_settings).grid(row=row, column=0, sticky="w")

    def open_settings(self):
        # Placeholder for "Open Settings" button logic
        messagebox.showinfo("Settings", "This will open the settings dialog (not implemented).")

    def start_browser(self):
        # Sample function to demonstrate Selenium usage
        # Path to your ChromeDriver
        chrome_driver_path = "/path/to/chromedriver"
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)

        driver.get("https://example.com")  # Example site
        messagebox.showinfo("Browser", "Opened browser and navigated to example.com")
        driver.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = SocialMediaAutomationApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Placeholder functions for undefined logic
def StartLogRunning(param):
    print("StartLogRunning called with param:", param)


def InstaPromoterDriverKiller(param):
    print("InstaPromoterDriverKiller called with param:", param)


def AccountRest(param):
    print("AccountRest called with param:", param)


def DateTimeLogStamp(param):
    print("DateTimeLogStamp called with param:", param)


def TargetRestSoftwareButton(param):
    print("TargetRestSoftwareButton called with param:", param)


# Main application class
class SocialMediaAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Automation")

        # UI Elements
        self.build_ui()

    def build_ui(self):
        # Add "Rest Software" Button
        rest_button = tk.Button(self.root, text="Rest Software", command=self.rest_software)
        rest_button.pack(pady=10)

        # Log text area
        self.textarea = tk.Text(self.root, height=10, width=50)
        self.textarea.pack(pady=10)

    def rest_software(self):
        # Display Confirmation Dialog
        result = messagebox.askyesnocancel("ALERT!",
                                           "Are you sure you want to close the browser and reset the accounts list?")

        if result is True:  # Yes
            # Placeholder actions called according to your logic
            StartLogRunning("#OpenLog")
            InstaPromoterDriverKiller("#RunInstaPromoterDriverKiller")
            AccountRest("#Rest Accounts")
            DateTimeLogStamp("#RunDateTimeLogStamp")

            # Log update in the tkinter textarea
            current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            log_message = (
                f"{current_time} - SOFTWARE STOPPED - STOP BUTTON ENGAGED\n"
                f"SOFTWARE STOPPED - LOG RUNNING - INTERNALIZING COMPLETE - {current_time}\n"
            )
            self.textarea.insert(tk.END, log_message)
            self.textarea.see(tk.END)  # Auto-scroll

            # Placeholder for sound and button interaction
            print("Playing system sound: Exclamation")
            TargetRestSoftwareButton("#RunRestTargetRestSoftwareButton")
            print("Simulated Stop Button Click")

            # Optional: Stop Application Logic
            self.root.quit()

        elif result is False:  # No
            print("Operation canceled by the user.")
        else:  # Cancel
            print("User clicked Cancel, no action taken.")


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = SocialMediaAutomationApp(root)
    root.mainloop()

from tkinter import Tk, Text, Button, Label, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time


class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Master Countdown")

        # UI Elements
        self.label = Label(root, text="Master Countdown", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.textarea = Text(root, height=15, width=50)
        self.textarea.pack(pady=10)

        self.start_button = Button(
            root, text="Start Software", command=self.start_software
        )
        self.start_button.pack(pady=10)

        # Selenium Driver (Placeholder)
        self.driver = None
        self.is_running = False

    def start_software(self):
        response = messagebox.askyesnocancel(
            "ALERT!", "Are you sure you want to start the software?"
        )

        if response is None:  # Cancel
            return

        if response:  # User selected 'Yes'
            self.start_log_running()
            self.date_time_log_stamp()

            self.append_textarea(
                f"{self.get_current_time()} - SOFTWARE RUNNING - THE START BUTTON HAS BEEN ENGAGED "
                f"BOTTING OPERATION NOW STARTED - LOG RUNNING - INTERNALIZING COMPLETE - {self.get_current_time()}\n"
            )

            self.initiate_browser_task()
            self.is_running = True

    def start_log_running(self):
        """Simulate the start of a log-running process."""
        # Placeholder for logging-related implementation
        self.append_textarea("Log Running: Initializing...\n")

    def date_time_log_stamp(self):
        """Add a timestamp log."""
        timestamp = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
        self.append_textarea(f"Log Timestamp: {timestamp}\n")

    def initiate_browser_task(self):
        """Perform automated tasks using Selenium."""
        # Configure Selenium WebDriver
        self.append_textarea("Starting Selenium Browser Automation...\n")

        # Replace 'chromedriver_path' with the path to your actual ChromeDriver
        driver_service = Service("chromedriver_path")
        self.driver = webdriver.Chrome(service=driver_service)

        # Open a dummy landing page (replace with desired URL)
        try:
            self.driver.get("https://example.com")
            textarea_script = """
            var textarea = document.getElementById('textarea_id');
            textarea.value += "{0} - Browser Task Executed.\\n";
            textarea.scrollTop = textarea.scrollHeight;
            """.format(
                self.get_current_time()
            )
            self.driver.execute_script(textarea_script)
            self.append_textarea("JavaScript executed on browser page.\n")

            # Mimic a button click if main button exists
            button = self.driver.find_element(By.TAG_NAME, "button")
            if button:
                self.append_textarea("Main button found. Triggering click...\n")
                ActionChains(self.driver).click(button).perform()

            self.append_textarea("Browser automation completed.\n")
        except Exception as e:
            self.append_textarea(f"Error during browser automation: {e}\n")
            if self.driver:
                self.driver.quit()

    def append_textarea(self, text):
        """Append text to the textarea and ensure scrolling to the bottom."""
        self.textarea.insert("end", text)
        self.textarea.see("end")

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import threading


# Utility functions corresponding to your original logic
def start_log_running():
    print("Logging started...")  # Replace with actual logging logic if needed


def kill_insta_promoter_driver():
    print("Killing any existing InstaPromoter driver instances...")  # Replace with actual process handling logic


def rotation_login_function():
    print("Performing Rotation Login...")  # Replace with custom login functionality


def create_stats_table():
    print("Creating stats table...")  # Replace with your implementation


class SocialMediaAutomationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Social Media Automation")
        self.geometry("400x200")

        self.build_ui()

    def build_ui(self):
        # Create the Account Login button
        login_button = tk.Button(self, text="Account - Login", command=self.account_login)
        login_button.pack(pady=20)

    def account_login(self):
        # Show a confirmation dialog
        result = messagebox.askquestion(
            title="ALERT!",
            message=(
                "Are you sure you want to login?\n"
                "If you are already logged in to the browser, this action will close the current browser, "
                "launch a new one, and log in to the next account in the list."
            ),
            icon='question'
        )

        if result == 'yes':
            # Proceed with login logic
            start_log_running()  # Start log running
            kill_insta_promoter_driver()  # Close existing drivers
            rotation_login_function()  # Perform login

            # Simulate a condition where stats table needs to be created
            stats_columns = 8  # Replace with actual table column count logic
            if stats_columns < 10:
                create_stats_table()


# Main application entry point
if __name__ == "__main__":
    app = SocialMediaAutomationApp()
    app.mainloop()

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Application:
    def __init__(self, root):
        self.root = root  # Root window
        self.root.title("Software Monitor")

        # Set up Text Area (to simulate the textarea updates in original)
        self.textarea = tk.Text(self.root, height=20, width=70)
        self.textarea.pack(pady=10)

        # Add a Stop button
        self.stop_button = tk.Button(self.root, text="Stop Software", command=self.stop_software)
        self.stop_button.pack(pady=10)

        # Variables to mimic original
        self.software_running = True

    def stop_software(self):
        """Handles the 'Stop Software' button click."""
        confirmation = messagebox.askquestion(
            "Alert!", "Are you sure you want to stop the software?", icon="question"
        )

        if confirmation == "yes":  # User confirms to stop the software
            self.software_running = False
            self.start_log_running()
            self.append_to_textarea(
                f"{self.get_current_time()} - SOFTWARE RUNNING - THE STOP BUTTON HAS BEEN ENGAGED. "
                "BOTTING OPERATION NOW STOPPED - LOG RUNNING - INTERNALIZING COMPLETE."
            )
            self.clear_data()
            self.play_notification()
            self.textarea.insert(tk.END, "\nSoftware has been stopped.\n")
            self.scroll_to_bottom()
        else:
            self.append_to_textarea("Stop software aborted by the user.")

    def start_log_running(self):
        """Starts logging the stop process."""
        time_log = f"Log started at {self.get_current_time()}"
        print(time_log)
        self.append_to_textarea(time_log)

    def get_current_time(self):
        """Returns the current time as a string."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return current_time

    def append_to_textarea(self, message):
        """Append a message to the textarea."""
        self.textarea.insert(tk.END, message + "\n")
        self.scroll_to_bottom()

    def scroll_to_bottom(self):
        """Scroll the textarea to the bottom."""
        self.textarea.see(tk.END)
        self.textarea.update()

    def clear_data(self):
        """Simulates the clearing of data and resetting states."""
        # Reset application variables/data
        print("Clearing data and resetting application states...")
        # Add corresponding actions if needed

    def play_notification(self):
        """Simulates playing a notification sound."""
        # For simplicity, a message box may suffice instead of actual sound.
        messagebox.showinfo("Notification", "Exclamation sound played!")


def run_application():
    root = tk.Tk()
    app = Application(root)
    root.mainloop()


# Run the application
if __name__ == "__main__":
    run_application()

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Placeholder to simulate log writing
def start_log_running():
    print("Log started...")


def date_time_log_stamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Pause Software")

        # Adding a textarea for logs
        self.textarea = tk.Text(root, width=80, height=20)
        self.textarea.pack(pady=10)

        # Adding the pause button
        self.pause_button = tk.Button(root, text="Pause Software", command=self.pause_software)
        self.pause_button.pack(pady=5)

        # Initialize Selenium WebDriver (adjust driver to your browser)
        # Example: Using Chrome WebDriver
        # Make sure you have 'chromedriver' installed and configured
        self.driver = webdriver.Chrome()

    def pause_software(self):
        # Show a confirmation dialog
        result = messagebox.askquestion("Pause Software", "Are you sure you want to pause the software?",
                                        icon='warning')
        if result == "yes":
            # Log messages
            start_log_running()
            timestamp = date_time_log_stamp()

            # Simulate logging in the textarea
            log_message = f"{timestamp} - SOFTWARE PAUSED - THE PAUSE BUTTON HAS BEEN ENGAGED BOTTING OPERATION NOW PAUSED - LOG RUNNING - INTERNALIZING COMPLETE - {timestamp}\n"
            self.textarea.insert(tk.END, log_message)
            self.textarea.see(tk.END)  # Auto scroll to the latest log

            # Simulate interaction with JavaScript via Selenium
            try:
                # Example: Finding an element with id 'textarea_id' and appending text to it
                self.driver.get("http://example.com")  # Replace with your actual URL
                textarea = self.driver.find_element(By.ID, "textarea_id")
                textarea.send_keys(f"{log_message}")
                textarea.send_keys(Keys.CONTROL + Keys.END)  # Scroll to the bottom
            except Exception as e:
                print(f"Error interacting with browser: {e}")

            # Placeholder to simulate a plugin command execution
            print("Plugin command executed: Pause")


# Create the Tkinter app
root = tk.Tk()
app = App(root)

# Start the Tkinter main loop
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class DelaySettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Delay Settings")
        self.root.geometry("600x400")

        # UI Elements
        self.build_ui()

        # Initialize variables
        self.delay_time = tk.StringVar()
        self.stop_bot_at = tk.StringVar()
        self.master_delay = tk.StringVar()
        self.run_when_complete = tk.StringVar()
        self.random_wait_one = tk.StringVar()
        self.random_wait_two = tk.StringVar()
        self.wait_after = tk.StringVar()

    def build_ui(self):
        """Build the main UI elements."""

        # Delay Counter
        ttk.Label(self.root, text="Set Delay Counter (Sec.):").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.delay_time).grid(row=0, column=1, padx=10, pady=5)

        # Stop Bot At
        ttk.Label(self.root, text="Stop The Software At:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.stop_bot_at).grid(row=1, column=1, padx=10, pady=5)

        # Master Delay
        ttk.Label(self.root, text="Master Delay - Seconds:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.master_delay).grid(row=2, column=1, padx=10, pady=5)

        # Run When Complete
        ttk.Label(self.root, text="Run When Complete:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.run_when_complete).grid(row=3, column=1, padx=10, pady=5)

        # Random Wait .1
        ttk.Label(self.root, text="Random Wait .1:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        random_wait_one_options = [str(i) for i in range(0, 300, 6)]
        ttk.Combobox(self.root, textvariable=self.random_wait_one, values=random_wait_one_options).grid(row=4, column=1,
                                                                                                        padx=10, pady=5)

        # Random Wait .2
        ttk.Label(self.root, text="Random Wait .2:").grid(row=5, column=0, sticky="w", padx=10, pady=5)
        random_wait_two_options = [str(i) for i in range(0, 300, 6)]
        ttk.Combobox(self.root, textvariable=self.random_wait_two, values=random_wait_two_options).grid(row=5, column=1,
                                                                                                        padx=10, pady=5)

        # Wait After Action Delay
        ttk.Label(self.root, text="Wait After Action Delay:").grid(row=6, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.wait_after).grid(row=6, column=1, padx=10, pady=5)

        # Information Button
        ttk.Button(self.root, text="Settings Instructions & Uses", command=self.show_instructions).grid(row=7, column=0,
                                                                                                        columnspan=2,
                                                                                                        pady=20)

    def show_instructions(self):
        """Display a dialog with detailed instructions."""
        instructions = """
        --------------------------------------------------------------------
        "Set Delay Counter (Sec.)" = This is a delay that only waits for a set amount of time. This is a flat wait.
        --------------------------------------------------------------------
        "Master Delay - Seconds" & "Run When Complete" are delay settings that work together.
        Master delay will run after the bot has completed the actions in "Run When Complete" box.
        --------------------------------------------------------------------
        "Random Wait .1" and "Random Wait .2" pick a random wait time between each action.
        --------------------------------------------------------------------
        "Wait After Action Delay" waits for a set time after each action (e.g., like, comment, unfollow).
        --------------------------------------------------------------------
        """
        messagebox.showinfo("Settings and Their Uses", instructions)


class AutomationBot:
    def __init__(self):
        """Initialize Selenium WebDriver."""
        self.driver = None

    def start_browser(self):
        """Start the WebDriver for automation."""
        service = Service("/path/to/chromedriver")  # Replace with your path to chromedriver
        self.driver = webdriver.Chrome(service=service)

    def close_browser(self):
        """Close the WebDriver."""
        if self.driver:
            self.driver.quit()

    def run_actions(self, settings):
        """
        Run automated actions based on the provided settings.

        :param settings: Dictionary containing delay and automation settings
        """
        # Example of waiting between actions
        try:
            self.start_browser()

            # Example: Navigate to a URL (replace with your logic)
            self.driver.get("https://example.com")

            # Implement delays based on the settings
            import time
            time.sleep(int(settings.get("delay_time", 1)))  # Flat delay

            # Example: Perform an action, then wait for random delay
            # (replace with your specific actions)
            time.sleep(int(settings.get("master_delay", 1)))

        finally:
            self.close_browser()


if __name__ == "__main__":
    root = tk.Tk()
    app = DelaySettingsApp(root)

    # Example usage of AutomationBot (for integration with button-click events)
    bot = AutomationBot()
    settings = {
        "delay_time": app.delay_time.get(),
        "stop_bot_at": app.stop_bot_at.get(),
        "master_delay": app.master_delay.get(),
        "run_when_complete": app.run_when_complete.get(),
        "random_wait_one": app.random_wait_one.get(),
        "random_wait_two": app.random_wait_two.get(),
        "wait_after": app.wait_after.get(),
    }

    # For starting automation (call `bot.run_actions(settings)` after UI inputs are set)
    root.mainloop()

import tkinter as tk
from tkinter import filedialog


class ListSettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("List Settings")

        # Initialize variables for buttons and textboxes tracking
        self.white_trigger = 0
        self.black_trigger = 0
        self.black_like_trigger = 0
        self.black_comm_trigger = 0

        # Build UI elements
        self.build_ui()

    def build_ui(self):
        # Ban Unfollow Whitelist Section
        tk.Label(self.root, text="Ban Unfollow Whitelist").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.white_list_entry = tk.Entry(self.root, width=40)
        self.white_list_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Load Whitelist - Don't Unfollow", command=self.load_whitelist).grid(row=0, column=2,
                                                                                                       padx=10, pady=5)

        # Stat Monitor - Spacer
        tk.Label(self.root, text=" ").grid(row=1, column=0, columnspan=3, pady=5)

        # Ban Follow Blacklist Section
        tk.Label(self.root, text="Ban Follow Blacklist").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.black_list_entry = tk.Entry(self.root, width=40)
        self.black_list_entry.grid(row=2, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Load Blacklist - Don't Follow", command=self.load_blacklist).grid(row=2, column=2,
                                                                                                     padx=10, pady=5)

        # Stat Monitor - Spacer
        tk.Label(self.root, text=" ").grid(row=3, column=0, columnspan=3, pady=5)

        # Ban Like Blacklist Section
        tk.Label(self.root, text="Ban Like Blacklist").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.black_list_likes_entry = tk.Entry(self.root, width=40)
        self.black_list_likes_entry.grid(row=4, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Load Blacklist - Don't Like", command=self.load_blacklist_likes).grid(row=4,
                                                                                                         column=2,
                                                                                                         padx=10,
                                                                                                         pady=5)

        # Stat Monitor - Spacer
        tk.Label(self.root, text=" ").grid(row=5, column=0, columnspan=3, pady=5)

        # Ban Comment Blacklist Section
        tk.Label(self.root, text="Ban Comment Blacklist").grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.black_list_comments_entry = tk.Entry(self.root, width=40)
        self.black_list_comments_entry.grid(row=6, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Load Blacklist - Don't Comment", command=self.load_blacklist_comments).grid(row=6,
                                                                                                               column=2,
                                                                                                               padx=10,
                                                                                                               pady=5)

        # Stat Monitor - Placeholder
        tk.Label(self.root, text="").grid(row=7, column=0, columnspan=3, pady=10)

    def load_whitelist(self):
        self.white_trigger = 1
        file_path = filedialog.askopenfilename(title="Select Whitelist File")
        if file_path:
            self.white_list_entry.delete(0, tk.END)
            self.white_list_entry.insert(0, file_path)
            self.load_custom_list_files(file_path)

    def load_blacklist(self):
        self.black_trigger = 1
        file_path = filedialog.askopenfilename(title="Select Blacklist File")
        if file_path:
            self.black_list_entry.delete(0, tk.END)
            self.black_list_entry.insert(0, file_path)
            self.load_custom_list_files(file_path)

    def load_blacklist_likes(self):
        self.black_like_trigger = 1
        file_path = filedialog.askopenfilename(title="Select Blacklist for Likes File")
        if file_path:
            self.black_list_likes_entry.delete(0, tk.END)
            self.black_list_likes_entry.insert(0, file_path)
            self.load_custom_list_files(file_path)

    def load_blacklist_comments(self):
        self.black_comm_trigger = 1
        file_path = filedialog.askopenfilename(title="Select Blacklist for Comments File")
        if file_path:
            self.black_list_comments_entry.delete(0, tk.END)
            self.black_list_comments_entry.insert(0, file_path)
            self.load_custom_list_files(file_path)

    def load_custom_list_files(self, file_path):
        # Placeholder function for integrating file handling logic
        # Replace this section with the actual logic you need for file processing
        print(f"Loaded custom list file: {file_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ListSettingsApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox


class RatioCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ratio Calculator")

        # Entry for Followers total
        self.lbl_followers = tk.Label(root, text="Enter Followers Total:")
        self.lbl_followers.grid(row=0, column=0, padx=10, pady=10)

        self.entry_followers = tk.Entry(root)
        self.entry_followers.grid(row=0, column=1, padx=10, pady=10)

        # Entry for Following total
        self.lbl_following = tk.Label(root, text="Enter Following Total:")
        self.lbl_following.grid(row=1, column=0, padx=10, pady=10)

        self.entry_following = tk.Entry(root)
        self.entry_following.grid(row=1, column=1, padx=10, pady=10)

        # Calculate button
        self.btn_calculate = tk.Button(root, text="Calculate Your Account Ratio", command=self.calculate_ratio)
        self.btn_calculate.grid(row=2, column=0, columnspan=2, pady=10)

        # Result display
        self.lbl_result = tk.Label(root, text="Ratio Results:")
        self.lbl_result.grid(row=3, column=0, padx=10, pady=10)

        self.result_text = tk.Text(root, height=5, width=40)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Option to stop the application at a given number
        self.lbl_stop = tk.Label(root, text="Stop The Software At:")
        self.lbl_stop.grid(row=5, column=0, padx=10, pady=10)

        self.entry_stop = tk.Entry(root)
        self.entry_stop.grid(row=5, column=1, padx=10, pady=10)

    def calculate_ratio(self):
        try:
            # Get inputs from the Entries
            followers = int(self.entry_followers.get())
            following = int(self.entry_following.get())

            # Validate inputs
            if following == 0:
                raise ValueError("Following count cannot be zero.")

            # Calculate the Follower-Following ratio
            ratio = followers / following

            # Display the results
            result = (
                f"Followers: {followers}\n"
                f"Following: {following}\n"
                f"{followers} ÷ {following} = {ratio:.2f}\n"
                f"Your Account Ratio = {ratio:.2f}"
            )
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

        except ValueError as ve:
            messagebox.showerror("Invalid Input", str(ve))


if __name__ == "__main__":
    root = tk.Tk()
    app = RatioCalculatorApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import webbrowser


def open_file_url(url):
    """
    Open a file or URL in the default browser.
    """
    webbrowser.open(url)


def run_advanced_settings():
    """
    Open the Advanced Settings Instructions URLs.
    """
    open_file_url("https://softwareautomation.org/home/insta-promoter.html")
    open_file_url("https://softwareautomation.org/pdf/Insta-Promoter-Instructions.pdf")


# Initialize the main application window
root = tk.Tk()
root.title("Advanced Settings")

# Drop-down options
options_likes = [str(i) for i in range(1, 21)]
options_show_hide = ["SHOW", "HIDE"]
options_comments = [str(i) for i in range(1, 21)]
options_multi_tool = ["Follow - Like - Comment", "Like - Comment", "Follow - Comment", "Follow - Like"]
options_yes_no = ["YES", "NO"]

# UI Widgets and Layout
tk.Label(root, text="Likes Per User - Min").grid(row=0, column=0)
likes_per_user_min = ttk.Combobox(root, values=options_likes)
likes_per_user_min.grid(row=0, column=1)

tk.Label(root, text="Likes Per User - Max").grid(row=1, column=0)
likes_per_user_max = ttk.Combobox(root, values=options_likes)
likes_per_user_max.grid(row=1, column=1)

tk.Label(root, text="Show Hide Browser").grid(row=2, column=0)
show_hide_browser = ttk.Combobox(root, values=options_show_hide)
show_hide_browser.grid(row=2, column=1)

tk.Label(root, text="Comment Per User - Min").grid(row=3, column=0)
comments_per_user_min = ttk.Combobox(root, values=options_comments)
comments_per_user_min.grid(row=3, column=1)

tk.Label(root, text="Comment Per User - Max").grid(row=4, column=0)
comments_per_user_max = ttk.Combobox(root, values=options_comments)
comments_per_user_max.grid(row=4, column=1)

tk.Button(root, text="Module Settings Instructions", command=run_advanced_settings).grid(row=5, column=0, columnspan=2)

tk.Label(root, text="Select Multi Tool Action").grid(row=6, column=0)
multi_tool_action = ttk.Combobox(root, values=options_multi_tool)
multi_tool_action.grid(row=6, column=1)

tk.Label(root, text="End Target Comments").grid(row=7, column=0)
end_target_comments = tk.Entry(root)
end_target_comments.grid(row=7, column=1)

tk.Label(root, text="End Target Liking").grid(row=8, column=0)
end_target_liking = tk.Entry(root)
end_target_liking.grid(row=8, column=1)

tk.Label(root, text="End Target Following").grid(row=9, column=0)
end_target_following = tk.Entry(root)
end_target_following.grid(row=9, column=1)

tk.Label(root, text="End Target Unfollowing").grid(row=10, column=0)
end_target_unfollowing = tk.Entry(root)
end_target_unfollowing.grid(row=10, column=1)

tk.Label(root, text="End Target Multi Tool").grid(row=11, column=0)
end_target_multi_tool = tk.Entry(root)
end_target_multi_tool.grid(row=11, column=1)

tk.Label(root, text="Remove Targeted Users").grid(row=12, column=0)
remove_users = ttk.Combobox(root, values=options_yes_no)
remove_users.grid(row=12, column=1)

tk.Label(root, text="Stop Target Module").grid(row=13, column=0)
stop_target_module = tk.Entry(root)
stop_target_module.grid(row=13, column=1)

tk.Label(root, text="Save Log To File").grid(row=14, column=0)
save_log_to_file = ttk.Combobox(root, values=options_yes_no)
save_log_to_file.grid(row=14, column=1)

tk.Label(root, text="Randomize Succession").grid(row=15, column=0)
randomize_succession = ttk.Combobox(root, values=options_yes_no)
randomize_succession.grid(row=15, column=1)

tk.Label(root, text="Enable Account Rotation").grid(row=16, column=0)
enable_account_rotation = ttk.Combobox(root, values=options_yes_no)
enable_account_rotation.grid(row=16, column=1)

tk.Label(root, text="Rotate Account At Total").grid(row=17, column=0)
rotate_account_at = tk.Entry(root)
rotate_account_at.grid(row=17, column=1)

tk.Label(root, text="Rotate On End Criteria").grid(row=18, column=0)
rotate_on_end_criteria = ttk.Combobox(root, values=options_yes_no)
rotate_on_end_criteria.grid(row=18, column=1)

tk.Label(root, text="Stop Bot On End Criteria").grid(row=19, column=0)
stop_bot_on_end_criteria = ttk.Combobox(root, values=options_yes_no)
stop_bot_on_end_criteria.grid(row=19, column=1)


# Selenium Placeholder
def start_browser():
    """
    Placeholder for starting Selenium browser (Chrome).
    """
    try:
        service = Service("path/to/chromedriver")
        driver = webdriver.Chrome(service=service)
        # Example of opening a browser (customize based on needs)
        driver.get("https://www.google.com")
    except WebDriverException as e:
        print(f"Selenium Error: {e}")


tk.Button(root, text="Open Browser Task", command=start_browser).grid(row=20, column=0, columnspan=2)

# Run the Application
root.mainloop()

import os
from tkinter import Tk, Label, Button, Entry, filedialog, Text, Scrollbar, END


class FileLoaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Required Files")

        self.account_file_path = ""
        self.proxy_file_path = ""
        self.target_user_file_path = ""
        self.comment_file_path = ""

        Label(root, text="Account File Path").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.account_file_entry = Entry(root, width=50)
        self.account_file_entry.grid(row=0, column=1, padx=10, pady=5)
        Button(root, text="Select Account File", command=self.select_account_file).grid(row=0, column=2, padx=10,
                                                                                        pady=5)

        Label(root, text="Proxy File Path").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.proxy_file_entry = Entry(root, width=50)
        self.proxy_file_entry.grid(row=1, column=1, padx=10, pady=5)
        Button(root, text="Select Proxy File", command=self.select_proxy_file).grid(row=1, column=2, padx=10, pady=5)

        Label(root, text="Target User List").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.target_user_file_entry = Entry(root, width=50)
        self.target_user_file_entry.grid(row=2, column=1, padx=10, pady=5)
        Button(root, text="Select Target File", command=self.select_target_user_file).grid(row=2, column=2, padx=10,
                                                                                           pady=5)

        Label(root, text="Comment File Path").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.comment_file_entry = Entry(root, width=50)
        self.comment_file_entry.grid(row=3, column=1, padx=10, pady=5)
        Button(root, text="Select Comment File", command=self.select_comment_file).grid(row=3, column=2, padx=10,
                                                                                        pady=5)

        Label(root, text="Log").grid(row=4, column=0, padx=10, pady=5, sticky="nw")
        self.log_text = Text(root, width=70, height=15, wrap="none")
        self.log_text.grid(row=4, column=1, columnspan=2, padx=10, pady=5)
        scrollbar = Scrollbar(root, command=self.log_text.yview)
        scrollbar.grid(row=4, column=3, sticky="ns")
        self.log_text.config(yscrollcommand=scrollbar.set)

    def log_message(self, message: str):
        self.log_text.insert(END, message + "\n")
        self.log_text.see(END)

    def select_account_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.csv")])
        if file_path:
            self.account_file_path = file_path
            self.account_file_entry.delete(0, END)
            self.account_file_entry.insert(0, file_path)
            self.log_message(
                f"{self.get_timestamp()} - SOFTWARE RUNNING - ACCOUNTS FILE LOADED SUCCESSFULLY - INTERNALIZING COMPLETE")
        else:
            self.log_message(
                f"{self.get_timestamp()} - SOFTWARE RUNNING - ACCOUNT FILE NOT LOADED OR DETECTED - TRY AGAIN!")

    def select_proxy_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.csv")])
        if file_path:
            self.proxy_file_path = file_path
            self.proxy_file_entry.delete(0, END)
            self.proxy_file_entry.insert(0, file_path)
            self.log_message(
                f"{self.get_timestamp()} - SOFTWARE RUNNING - PROXY FILE LOADED SUCCESSFULLY - INTERNALIZING COMPLETE")
        else:
            self.log_message(
                f"{self.get_timestamp()} - SOFTWARE RUNNING - PROXY FILE NOT LOADED OR DETECTED - TRY AGAIN!")

    def select_target_user_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.target_user_file_path = file_path
            self.target_user_file_entry.delete(0, END)
            self.target_user_file_entry.insert(0, file_path)
            file_lines = self.count_lines(file_path)
            self.log_message(
                f"{self.get_timestamp()} - SOFTWARE RUNNING - TARGET USER FILE LOADED SUCCESSFULLY - TOTAL = {file_lines}")
        else:
            self.log_message(
                f"{self.get_timestamp()} - SOFTWARE RUNNING - TARGET FILE NOT LOADED OR DETECTED - TRY AGAIN!")

    def select_comment_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.comment_file_path = file_path
            self.comment_file_entry.delete(0, END)
            self.comment_file_entry.insert(0, file_path)
            file_lines = self.count_lines(file_path)
            self.log_message(
                f"{self.get_timestamp()} - SOFTWARE RUNNING - COMMENT FILE LOADED SUCCESSFULLY - TOTAL = {file_lines}")
        else:
            self.log_message(
                f"{self.get_timestamp()} - SOFTWARE RUNNING - COMMENT FILE NOT LOADED OR DETECTED - TRY AGAIN!")

    def get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def count_lines(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return sum(1 for line in file if line.strip())
        except Exception as e:
            self.log_message(f"Error reading file: {e}")
            return 0


if __name__ == "__main__":
    root = Tk()
    app = FileLoaderApp(root)
    root.mainloop()


import tkinter as tk
from tkinter import filedialog
from tkinter import StringVar


class SaveLoadSettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Save/Load Settings")

        # Variables to hold custom settings path
        self.custom_settings_path = StringVar()

        # UI Component Definitions
        self.create_ui()

    def create_ui(self):
        # Save/Load UI structures
        self.add_stat_monitor("SavedLoad Succession", "")
        self.add_buttons("Succession")

        self.add_stat_monitor("SaveLoad Post Module", "")
        self.add_buttons("Post Module")

        self.add_stat_monitor("SaveLoad Scrape Module", "")
        self.add_buttons("Scrape Module")

        self.add_stat_monitor("SaveLoad Target Module", "")
        self.add_buttons("Target Module")

        self.add_stat_monitor("SaveLoad All Modules", "")
        self.add_buttons("All Modules")

        # Custom Folder Selection Components
        tk.Label(self.root, text="Custom SaveLoad Path").pack()
        tk.Entry(self.root, textvariable=self.custom_settings_path).pack()

        tk.Button(self.root, text="Select Custom SaveLoad Folder", command=self.select_folder).pack()

        # Save/Load for Custom Folder
        tk.Button(self.root, text="Save Settings", command=lambda: self.run_save("Custom Folder")).pack()
        tk.Button(self.root, text="Load Settings", command=lambda: self.run_load("Custom Folder")).pack()

        # Main UI Stat Monitor
        self.add_stat_monitor("Main UI", "")

    def add_stat_monitor(self, monitor_name, monitor_value):
        tk.Label(self.root, text=monitor_name).pack()
        tk.Label(self.root, text=monitor_value).pack()

    def add_buttons(self, module_name):
        tk.Button(self.root, text="Save Settings", command=lambda: self.run_save(module_name)).pack()
        tk.Button(self.root, text="Load Settings", command=lambda: self.run_load(module_name)).pack()

    def select_folder(self):
        folder_path = filedialog.askdirectory(title="Please select a folder.")
        if folder_path:
            self.custom_settings_path.set(folder_path)

    def run_save(self, module_name):
        print(f"Save Settings for {module_name} module triggered.")
        # Call related save functionality (Placeholder)

    def run_load(self, module_name):
        print(f"Load Settings for {module_name} module triggered.")
        # Call related load functionality (Placeholder)


# Main application execution
if __name__ == "__main__":
    root = tk.Tk()
    app = SaveLoadSettingsApp(root)
    root.mainloop()

from tkinter import Tk, Label, Entry, StringVar, OptionMenu, Toplevel
from selenium import webdriver


class SuperuserSettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Superuser Settings")

        self.create_ui_elements()

    def create_ui_elements(self):
        # Set User Agent String
        Label(self.root, text="Set User Agent String").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.user_agent = StringVar()
        Entry(self.root, textvariable=self.user_agent).grid(row=0, column=1, padx=10, pady=5)

        # Popular Posts Dropdown
        Label(self.root, text="Popular Posts").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.top_posts = StringVar(value="")
        OptionMenu(self.root, self.top_posts, "", "KEEP", "REMOVE").grid(row=1, column=1, padx=10, pady=5)

        # Randomize Target List Dropdown
        Label(self.root, text="Randomize Target List").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.randomize_scrape_list = StringVar(value="")
        OptionMenu(self.root, self.randomize_scrape_list, "", "YES", "NO").grid(row=2, column=1, padx=10, pady=5)

        # Separator and Stat Monitors
        Label(self.root, text="Followers To Following", fg="yellow").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        Label(self.root, text="").grid(row=3, column=1, padx=10, pady=5)

        # Follow Ratio Is Greater
        Label(self.root, text="Follow Ratio Is Greater").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.follow_greater_than = StringVar()
        Entry(self.root, textvariable=self.follow_greater_than).grid(row=4, column=1, padx=10, pady=5)

        # Follow Ratio Is Less
        Label(self.root, text="Follow Ratio Is Less").grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.follow_less_than = StringVar()
        Entry(self.root, textvariable=self.follow_less_than).grid(row=5, column=1, padx=10, pady=5)

        # Follow Ratio Is Equal
        Label(self.root, text="Follow Ratio Is Equal").grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.follow_equal_to = StringVar()
        Entry(self.root, textvariable=self.follow_equal_to).grid(row=6, column=1, padx=10, pady=5)

        # Skip - If Tagged With
        Label(self.root, text="Skip - If Tagged With").grid(row=7, column=0, sticky="w", padx=10, pady=5)
        self.skip_if_tagged_with = StringVar()
        Entry(self.root, textvariable=self.skip_if_tagged_with).grid(row=7, column=1, padx=10, pady=5)

        Label(self.root, text="(Comma Separate Tags)", fg="yellow").grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        # Skip - Advanced Options
        Label(self.root, text="Advanced Skip Options", fg="yellow").grid(row=9, column=0, columnspan=2, padx=10, pady=5)

        # Skip - Likes/Comments Dropdown
        Label(self.root, text="Skip - Likes/Comments").grid(row=10, column=0, sticky="w", padx=10, pady=5)
        self.advanced_skip = StringVar(value="")
        OptionMenu(self.root, self.advanced_skip, "", "(Seconds) Skip If Not Contains",
                   "(Minutes) Skip If Not Contains", "(Current Month) Skip If Not Contains").grid(row=10, column=1,
                                                                                                  padx=10, pady=5)

        # Skip - Link In Bio
        Label(self.root, text="Skip - Link In Bio").grid(row=11, column=0, sticky="w", padx=10, pady=5)
        self.skip_bio_link = StringVar(value="")
        OptionMenu(self.root, self.skip_bio_link, "", "YES", "NO").grid(row=11, column=1, padx=10, pady=5)

        # Skip - Account is Private
        Label(self.root, text="Skip - Account Is Private").grid(row=12, column=0, sticky="w", padx=10, pady=5)
        self.skip_private_account = StringVar(value="")
        OptionMenu(self.root, self.skip_private_account, "", "YES", "NO").grid(row=12, column=1, padx=10, pady=5)

        # Skip - No Posts Yet
        Label(self.root, text="Skip - No Posts Yet").grid(row=13, column=0, sticky="w", padx=10, pady=5)
        self.skip_no_posts_yet = StringVar(value="")
        OptionMenu(self.root, self.skip_no_posts_yet, "", "YES", "NO").grid(row=13, column=1, padx=10, pady=5)

        # Skip - Non-English
        Label(self.root, text="Skip - Non-English").grid(row=14, column=0, sticky="w", padx=10, pady=5)
        self.skip_non_english = StringVar(value="")
        OptionMenu(self.root, self.skip_non_english, "", "YES", "NO").grid(row=14, column=1, padx=10, pady=5)

    def get_settings(self):
        # Helper method to fetch all settings
        settings = {
            "user_agent": self.user_agent.get(),
            "top_posts": self.top_posts.get(),
            "randomize_scrape_list": self.randomize_scrape_list.get(),
            "follow_greater_than": self.follow_greater_than.get(),
            "follow_less_than": self.follow_less_than.get(),
            "follow_equal_to": self.follow_equal_to.get(),
            "skip_if_tagged_with": self.skip_if_tagged_with.get(),
            "advanced_skip": self.advanced_skip.get(),
            "skip_bio_link": self.skip_bio_link.get(),
            "skip_private_account": self.skip_private_account.get(),
            "skip_no_posts_yet": self.skip_no_posts_yet.get(),
            "skip_non_english": self.skip_non_english.get()
        }
        return settings

    def start_browser(self):
        # Launch a browser with Selenium and configure user agent
        options = webdriver.ChromeOptions()
        if self.user_agent.get():
            options.add_argument(f"user-agent={self.user_agent.get()}")
        driver = webdriver.Chrome(options=options)
        driver.get("https://example.com")  # Replace with actual URL to interact with
        return driver


# Run the Tkinter app
if __name__ == "__main__":
    root = Tk()
    app = SuperuserSettingsApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import subprocess


class ProjectSettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Settings")

        # Variables
        self.run_from_project_folder = tk.StringVar(value="YES")
        self.custom_settings_path = tk.StringVar()
        self.ipdf_path = tk.StringVar()

        # Dropdown Menu
        tk.Label(root, text="Run From Project Folder:").pack(pady=5)
        tk.OptionMenu(root, self.run_from_project_folder, "YES", "NO").pack(pady=5)

        # Status Monitor (for display purposes only)
        tk.Label(root, text="Save Project Settings", fg="yellow").pack(pady=5)

        # Text Box for Project Target Folder
        tk.Label(root, text="Project Target Folder:").pack(pady=5)
        tk.Entry(root, textvariable=self.custom_settings_path, width=50).pack(pady=5)

        # Select Folder Button
        tk.Button(root, text="Select The Target Project Folder", command=self.select_project_folder).pack(pady=5)

        # Save Settings Button
        tk.Button(root, text="Save Settings To Target Project", command=self.save_settings).pack(pady=5)

        # Open - Project Folder Directory Button
        tk.Button(root, text="Open - Project Folder Directory", command=self.open_project_directory).pack(pady=5)

        # Data File Path Entry
        tk.Label(root, text="Data File Path:").pack(pady=5)
        tk.Entry(root, textvariable=self.ipdf_path, width=50).pack(pady=5)

        # Build Insta Promoter Data Folder Button
        tk.Button(root, text="Build Insta Promoter Data Folder", command=self.build_instapromoter_folder).pack(pady=5)

    def select_project_folder(self):
        """Open folder browser dialog and set the selected path."""
        if not self.ipdf_path.get():
            initial_dir = os.path.expanduser("~/Documents/Insta Promoter Data Folder/projects")
        else:
            initial_dir = os.path.expanduser("~/projects")

        selected_folder = filedialog.askdirectory(initialdir=initial_dir, title="Please select a folder.")
        if selected_folder:
            self.custom_settings_path.set(selected_folder)

    def save_settings(self):
        """Save settings to the target project."""
        # Simulate saving settings logic here
        messagebox.showinfo("Save Settings", "Settings saved to target project!")

    def open_project_directory(self):
        """Open the project folder directory."""
        if self.ipdf_path.get():
            directory_path = os.path.expanduser("~/Documents/Insta Promoter Data Folder/projects")
        else:
            directory_path = os.path.expanduser("~/projects")

        if os.path.exists(directory_path):
            subprocess.run(
                ["xdg-open", directory_path])  # For Linux. Replace with "explorer" for Windows or "open" for macOS.
        else:
            messagebox.showerror("Error", "Directory does not exist!")

    def build_instapromoter_folder(self):
        """Build Insta Promoter Data Folder."""
        alert_message = (
            "VERY IMPORTANT! If you use this option to 'Build Insta Promoter Data Folder' "
            "you must set up and use this directory:\n"
            "C:\\Users\\%username%\\Documents\\Insta Promoter Data Folder.\n"
            "It is highly recommended to use this option and not the installation folders "
            "to run from, as the install folders may get replaced during updates."
        )
        result = messagebox.askquestion("ALERT!", alert_message, icon="warning")

        if result == "yes":
            # Simulate running external setup program
            setup_path = os.path.expanduser("~/inst/ipdf-setup.exe")
            if os.path.exists(setup_path):
                subprocess.run([setup_path])
                self.ipdf_path.set(os.path.expanduser("~/Documents/Insta Promoter Data Folder"))
            else:
                messagebox.showerror("Error", "Setup file not found!")
        else:
            messagebox.showinfo("Request Canceled", "Build Insta Promoter Data Folder request canceled!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectSettingsApp(root)
    root.mainloop()
