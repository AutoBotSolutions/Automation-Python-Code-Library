import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure the Selenium WebDriver
driver = webdriver.Chrome()  # Make sure to have the necessary WebDriver installed


def close_info_box():
    """Closes the informational pop-up if present."""
    try:
        close_button = driver.find_element(By.XPATH, "//html/body/div[4]/div/button")
        close_button.click()
    except Exception as e:
        print("No info box to close:", e)


def run_unfollow_function_one():
    """
    Executes the 'Unfollow Function One' functionality.
    Closes the informational box and waits for an element in the navigation bar.
    """
    close_info_box()
    try:
        # Check if the document contains certain text (pseudo logic with Selenium)
        page_source = driver.page_source
        if "Close" in page_source:  # Replace this with the actual condition logic
            # Simulate the plugin actions
            driver.find_element(By.XPATH, "//html/body/div[4]/div/button").click()

            # Wait for the navigation bar element to appear
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/div/a[1]')
                )
            )
            print("Target element found.")
    except Exception as e:
        print("Error in run_unfollow_function_one:", e)


# Tkinter UI Setup
def create_ui():
    """Creates the tkinter user interface."""
    window = tk.Tk()
    window.title("Unfollow Automation")

    # Instruction Label
    instruction_label = tk.Label(
        window,
        text="Click the button below to run the Unfollow Function.",
        padx=10,
        pady=10
    )
    instruction_label.pack()

    # Run Unfollow Button
    run_button = tk.Button(
        window,
        text="Run Unfollow Function One",
        command=run_unfollow_function_one,
        padx=10,
        pady=10
    )
    run_button.pack()

    # Close Button
    close_button = tk.Button(
        window,
        text="Close",
        command=window.destroy,
        padx=10,
        pady=10
    )
    close_button.pack()

    # Start the Tkinter event loop
    window.mainloop()


# Main Execution
if __name__ == "__main__":
    # Launch the browser first (optional navigation)
    driver.get("https://example.com")  # Replace with the actual URL

    # Create and display the tkinter user interface
    create_ui()

    # Quit the WebDriver after the UI is closed
    driver.quit()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
from datetime import datetime


class UnfollowBot:
    """Class to encapsulate Unfollow functionality with Selenium and Tkinter."""

    def __init__(self):
        # Initialize Selenium WebDriver
        self.driver = webdriver.Chrome()  # Ensure the correct driver is installed
        self.driver.get("https://example.com")  # Replace with the actual URL (login page or main page)

    def close_info_box(self):
        """Closes any pop-up informational box if it exists."""
        try:
            close_button = self.driver.find_element(By.XPATH, "//html/body/div[4]/div/button")
            close_button.click()
            print("Info box closed successfully.")
        except Exception as e:
            print("No info box found or already closed:", e)

    def navigate_to_user_profile(self):
        """Navigates to the user's profile page."""
        try:
            # Wait for the navigation element and click it
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')
                )
            ).click()
            print("Navigated to user profile.")
        except Exception as e:
            print("Error while navigating to user profile:", e)

    def log_activity(self, message):
        """Logs activity messages with timestamps."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} - {message}")

    def scrape_following_users(self):
        """Simulates scraping users from the 'Following' list."""
        try:
            # Click the 'Following' button
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//span[@id="react-root"]/section/main/article/header/section/ul/li[3]/a')
                )
            ).click()

            # Wait for the modal to open
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//html/body/div[3]/div/div[2]/div/div[1]')
                )
            )
            print("Scraping following list started.")

            # Simulate scrolling the following list
            scroll_area = self.driver.find_element(By.XPATH, "//html/body/div[3]/div/div[2]/div")
            for _ in range(5):  # Adjust the range for more scrolling steps
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_area)

            print("Scrolling completed.")
        except Exception as e:
            print("Error during scraping following users:", e)

    def unfollow_workflow(self):
        """Main workflow for the 'Unfollow' functionality."""
        self.close_info_box()
        self.log_activity("Unfollow function activated.")
        try:
            # Navigate to the user profile
            self.navigate_to_user_profile()

            # Refresh the page
            self.driver.refresh()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//span[@id="react-root"]/section/footer/div/nav/ul'))
            )

            # Start scraping and unfollowing
            self.scrape_following_users()
            self.log_activity("Unfollow process completed.")
        except Exception as e:
            print("Error in the unfollow workflow:", e)


class GUIApp:
    """Class to encapsulate the Tkinter-based UI."""

    def __init__(self, root, bot):
        self.root = root
        self.bot = bot
        self.root.title("Unfollow Automation")

        # Instruction Label
        instruction_label = tk.Label(
            self.root,
            text="Click the button below to run the Unfollow Function.",
            padx=10,
            pady=10
        )
        instruction_label.pack()

        # Run Unfollow Button
        self.run_button = tk.Button(
            self.root,
            text="Run Unfollow Function",
            command=self.run_unfollow_function,
            padx=10,
            pady=10
        )
        self.run_button.pack()

        # Close Button
        self.close_button = tk.Button(
            self.root,
            text="Close",
            command=self.on_close,
            padx=10,
            pady=10
        )
        self.close_button.pack()

    def run_unfollow_function(self):
        """Executes the Unfollow Function in a separate thread."""
        threading.Thread(target=self.bot.unfollow_workflow, daemon=True).start()

    def on_close(self):
        """Handles the close button click event."""
        try:
            # Close the WebDriver before exiting
            self.bot.driver.quit()
        except Exception as e:
            print("Error while closing WebDriver:", e)
        self.root.destroy()


if __name__ == "__main__":
    # Main Execution
    # Initialize the bot
    unfollow_bot = UnfollowBot()

    # Create and run the Tkinter GUI
    root = tk.Tk()
    gui_app = GUIApp(root, unfollow_bot)
    root.mainloop()

import tkinter as tk
from tkinter import ttk
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC as SeleniumEC
from datetime import datetime
import time


class UnfollowBot:
    def __init__(self, driver):
        self.driver = driver
        self.following_scraped_list = []
        self.unfollow_queue = 0
        self.scrape_failed_count = 0
        self.fail_counter = 0
        self.loop_breakout = False

    def log_activity(self, message):
        # Log activity message
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        textarea = self.driver.find_element(By.ID, "textarea_id")
        textarea_value = textarea.get_attribute("value")
        textarea_value += f"{timestamp} - {message}\n"
        self.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].scrollTop = arguments[0].scrollHeight;",
            textarea, textarea_value)

    def scrape_following_list(self):
        # Scrape users from the following list with a retry mechanism
        try:
            elements = self.driver.find_elements(By.XPATH, "//html/body/div[3]/div/div[2]/div/div[2]/ul/div/li[*]")
            for elem in elements:
                # Extract username using a stable attribute (XPath-based parsing)
                username = elem.find_element(By.XPATH, ".//a[@style='width: 30px; height: 30px;']").get_attribute(
                    "href")
                username = username.split("/")[-2]  # Extract username text
                if username not in self.following_scraped_list:
                    self.following_scraped_list.append(username)

            # Remove duplicates (handled by the nature of Python sets)
            self.following_scraped_list = list(set(self.following_scraped_list))
            self.unfollow_queue = len(self.following_scraped_list)
            return True
        except Exception as e:
            self.scrape_failed_count += 1
            return False

    def unfollow_workflow(self):
        self.log_activity("SOFTWARE RUNNING - CLEARING FOLLOWING SCRAPED LIST - UNFOLLOW BOT")

        for _ in range(13):  # Repeated attempts to scrape and populate following list
            success = self.scrape_following_list()

            # Check for scraping success or fail-safe conditions
            if self.unfollow_queue >= 10:  # Replace 10 with num_unfollow, if required
                self.log_activity("UNFOLLOW BOT SCRAPE SUCCESS - TRIGGERING LOOP BREAKOUT")
                self.loop_breakout = True
                break

            if not success and self.scrape_failed_count >= 3:
                self.log_activity("UNFOLLOW BOT SCRAPE FAILED - TRIGGERING LOOP BREAKOUT")
                self.loop_breakout = True
                break

            if self.unfollow_queue < 10 and self.fail_counter >= 20:  # Adjust number of retries if needed
                self.log_activity("NOT ENOUGH USERS IN LIST - TRIGGERING LOOP BREAKOUT")
                self.loop_breakout = True
                break

        # Final condition if scraping fails entirely
        if self.unfollow_queue == 0:
            self.log_activity("UNFOLLOW BOT - EMPTY FOLLOWING LIST DETECTED")

        return self.unfollow_queue > 0


class GUIApp:
    def __init__(self, root, bot):
        self.root = root
        self.bot = bot

        # Build GUI
        self.root.title("Unfollow Bot")
        self.root.geometry("400x200")

        self.run_button = ttk.Button(self.root, text="Run Unfollow Workflow", command=self.run_unfollow_function)
        self.run_button.pack(pady=10)

        self.close_button = ttk.Button(self.root, text="Close", command=self.on_close)
        self.close_button.pack(pady=10)

    def run_unfollow_function(self):
        # Button-bound function to run the unfollow workflow
        unfollow_result = self.bot.unfollow_workflow()

        if unfollow_result:
            ttk.Label(self.root, text="Unfollow workflow completed successfully").pack(pady=10)
        else:
            ttk.Label(self.root, text="Unfollow workflow failed").pack(pady=10)

    def on_close(self):
        self.root.destroy()


# Example usage with Selenium WebDriver:
if __name__ == "__main__":
    from selenium import webdriver

    # Set up WebDriver (replace with your browser driver)
    driver = webdriver.Chrome()

    # Initialize the bot and GUI
    bot = UnfollowBot(driver)
    root = tk.Tk()
    app = GUIApp(root, bot)

    # Start the Tkinter main loop
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import datetime


class UnfollowBot:
    def __init__(self, driver):
        self.driver = driver  # Selenium WebDriver instance
        self.following_scraped_list = []
        self.unfollow_queue = []
        self.log_box = None

    def log_activity(self, message: str):
        """Logs activities in the text area"""
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} - {message}"
        if self.log_box is not None:
            self.log_box.insert(tk.END, log_message + '\n')
            self.log_box.see(tk.END)  # Auto-scroll to the bottom
        print(log_message)

    def randomize_scraped_list(self):
        """Randomizes the scraped list."""
        self.log_activity("SOFTWARE RUNNING - RANDOMIZE SCRAPED LIST OPTION SELECTED - RANDOMIZING LIST")
        self.following_scraped_list = random.sample(self.following_scraped_list, len(self.following_scraped_list))
        self.log_activity("List randomized successfully")

    def remove_excess_entries(self, num_to_keep: int):
        """Ensures the list has only a specific number of entries."""
        self.log_activity(f"UNFOLLOW BOT SCRAPE QUEUE TOTAL BEFORE TRIM = {len(self.following_scraped_list)}")
        self.unfollow_queue = self.following_scraped_list[:num_to_keep]
        self.log_activity(f"UNFOLLOW BOT SCRAPE QUEUE TOTAL AFTER TRIM = {len(self.unfollow_queue)}")

    def unfollow_workflow(self, randomize_list_option: bool = False, num_unfollow: int = 10):
        """
        Main unfollow workflow
        - Randomizes the scraped list if the option is selected.
        - Trims the list to the specified number for unfollowing.
        """
        # Step 1: Randomize list if needed
        if randomize_list_option:
            self.randomize_scraped_list()

        # Step 2: Adjust the list size to match the number of users to unfollow
        if len(self.following_scraped_list) > num_unfollow:
            self.remove_excess_entries(num_unfollow)

        # Step 3: Simulate unfollowing process
        for user in self.unfollow_queue:
            self.log_activity(f"Performing unfollow action for user: {user}")
            # Here, you would implement Selenium commands to interact with the web browser.
            # Example: Locate and click the unfollow button for the user.
            # Assuming a dummy function `unfollow_user` for demonstration:
            try:
                self.unfollow_user(user)
            except Exception as e:
                self.log_activity(f"Failed to unfollow user: {user}. Error: {str(e)}")

    def unfollow_user(self, user):
        """Placeholder for actual unfollow operation using Selenium."""
        # Example Locator (CSS/XPath) and interaction (adjust based on your app requirements)
        unfollow_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//button[text()='Unfollow'][@data-username='{user}']"))
        )
        unfollow_button.click()
        self.log_activity(f"Successfully unfollowed user: {user}")


class GUIApp:
    def __init__(self, root, bot: UnfollowBot):
        self.root = root
        self.bot = bot
        self.root.title("Unfollow Bot")

        # Log Textbox
        self.log_textbox = tk.Text(root, height=15, width=80)
        self.log_textbox.pack(pady=10)
        self.bot.log_box = self.log_textbox  # Assigning the bot's log_box

        # Randomize List Checkbox
        self.randomize_var = tk.BooleanVar(value=False)
        self.randomize_checkbox = tk.Checkbutton(
            root, text="Randomize Scraped List", variable=self.randomize_var
        )
        self.randomize_checkbox.pack(pady=5)

        # Number of Unfollows Entry
        self.num_unfollow_label = tk.Label(root, text="Number of Users to Unfollow:")
        self.num_unfollow_label.pack(pady=5)
        self.num_unfollow_entry = tk.Entry(root)
        self.num_unfollow_entry.insert(0, "10")  # Default value
        self.num_unfollow_entry.pack(pady=5)

        # Run Button
        self.run_button = tk.Button(root, text="Run Unfollow Bot", command=self.run_unfollow_function)
        self.run_button.pack(pady=10)

        # Close Button
        self.close_button = tk.Button(root, text="Close", command=self.on_close)
        self.close_button.pack(pady=10)

    def run_unfollow_function(self):
        """Runs the unfollow function in the bot."""
        randomize_list_option = self.randomize_var.get()
        try:
            num_unfollow = int(self.num_unfollow_entry.get())
            self.bot.unfollow_workflow(randomize_list_option=randomize_list_option, num_unfollow=num_unfollow)
            messagebox.showinfo("Success", "Unfollow workflow completed!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for 'Number of Users to Unfollow'.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_close(self):
        """Handles GUI closing properly."""
        self.root.destroy()


# Example Driver Instantiation (Replace with actual Selenium WebDriver instantiation)
from selenium import webdriver

driver = webdriver.Chrome()

# Initialize Bot and UI
bot = UnfollowBot(driver)
root = tk.Tk()
app = GUIApp(root, bot)

# Run the Application
root.mainloop()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class UnfollowBot:
    def __init__(self, driver: webdriver.Chrome, log_box: tk.Text):
        self.driver = driver
        self.log_box = log_box
        self.unfollow_queue = []
        self.unfollow_counter = 0
        self.stop_criteria = 10  # Example stop criterion

    def log_activity(self, message: str):
        """Logs a message to the Tkinter log box."""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} - {message}\n"
        self.log_box.insert(tk.END, log_message)
        self.log_box.see(tk.END)
        print(log_message)  # For debugging purposes

    def navigate_to_user_profile(self, username: str):
        """Navigates to a user's Instagram profile."""
        profile_url = f"https://www.instagram.com/{username}/"
        self.driver.get(profile_url)
        self.log_activity(f"Loaded user profile page for [{username}].")

    def unfollow_user(self, username: str):
        """Executes the process of unfollowing a user."""
        self.log_activity(f"Attempting to unfollow user [{username}]...")
        try:
            # Example wait for follow/unfollow button
            unfollow_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Following")]'))
            )
            unfollow_button.click()
            self.log_activity(f"Clicked 'Unfollow' button for [{username}].")

            confirm_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Unfollow")]'))
            )
            confirm_button.click()
            self.log_activity(f"Successfully unfollowed user [{username}].")

            self.unfollow_counter += 1

        except Exception as e:
            self.log_activity(f"Failed to unfollow user [{username}]: {str(e)}")

    def unfollow_workflow(self):
        """Main workflow for the unfollow bot."""
        while self.unfollow_queue:
            username = self.unfollow_queue.pop(0)
            self.navigate_to_user_profile(username)
            self.unfollow_user(username)

            if self.unfollow_counter >= self.stop_criteria:
                self.log_activity("Stop criteria met. Stopping the bot...")
                return

            time.sleep(2)  # Example delay between actions
        self.log_activity("Unfollow workflow complete.")


class GUIApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Instagram Unfollow Bot")

        # Log Textbox
        self.log_textbox = tk.Text(root, wrap=tk.WORD, height=20, width=70)
        self.log_textbox.pack(padx=10, pady=10)

        # Entry for usernames
        self.usernames_entry = tk.Entry(root, width=50)
        self.usernames_entry.pack(pady=5)
        self.usernames_entry.insert(0, "Enter usernames to unfollow, comma-separated")

        # Start Button
        self.run_button = tk.Button(root, text="Run Unfollow Bot", command=self.run_unfollow_function)
        self.run_button.pack(pady=5)

        # Close Button
        self.close_button = tk.Button(root, text="Close", command=self.on_close)
        self.close_button.pack(pady=5)

        # Selenium Driver (Initiate webdriver instance as needed)
        self.driver = webdriver.Chrome()  # Adjust WebDriver path as needed

        # Bot instance
        self.bot = UnfollowBot(self.driver, self.log_textbox)

    def run_unfollow_function(self):
        """Runs the unfollow workflow based on entered usernames."""
        usernames = self.usernames_entry.get().split(',')
        self.bot.unfollow_queue = [username.strip() for username in usernames if username.strip()]
        self.bot.unfollow_workflow()

    def on_close(self):
        """Handles closing of the application."""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.driver.quit()
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()

import tkinter as tk
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from tkinter import messagebox
import threading


# Selenium-powered UnfollowBot class
class UnfollowBot:
    def __init__(self, driver, log_box):
        """Initialize the bot with a Selenium WebDriver instance."""
        self.driver = driver
        self.unfollow_counter = 0
        self.stop_bot_at = 10  # Example threshold, should be customizable
        self.enable_account_rotation = True
        self.log_box = log_box

    def log_activity(self, message):
        """Log messages to the Tkinter log box."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - {message}\n"
        self.log_box.insert(tk.END, log_message)
        self.log_box.see(tk.END)

    def stop_on_condition(self):
        """Stop the bot if certain conditions are met."""
        if self.unfollow_counter >= self.stop_bot_at:
            self.log_activity("SOFTWARE STOPPED - SOFTWARE STOP CRITERIA HAS BEEN MET.")
            # Play a system sound (adjust or implement library-based sound as needed)
            self.play_system_sound()
            return True
        return False

    @staticmethod
    def play_system_sound():
        """Play a system sound upon stopping the bot."""
        try:
            import os
            if os.name == "nt":  # Windows
                import winsound
                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            else:
                # For Linux/macOS, you may need to adjust configurations
                print("\a")  # Simple alert sound
        except Exception as e:
            print(f"Error playing sound: {e}")

    def run_unfollow_workflow(self):
        """Main method to simulate unfollow functionality."""
        try:
            # Example condition to stop the bot
            if self.stop_on_condition():
                return

            # Simulate account rotation if enabled
            if self.enable_account_rotation:
                self.log_activity("Rotating accounts...")

            # Unfollow logic (simulate browser commands with Selenium)
            self.log_activity("Unfollowing user...")
            # Example simulate of Selenium logic
            # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "some_id"))).click()

            # Increment counter and log success
            self.unfollow_counter += 1
            self.log_activity(f"Unfollow counter updated: {self.unfollow_counter}")

        except Exception as e:
            self.log_activity(f"Error during unfollow process: {str(e)}")


# Tkinter GUI Application class
class GUIApp:
    def __init__(self, root, bot):
        """Initialize the Tkinter application."""
        self.root = root
        self.bot = bot
        self.root.title("Unfollow Bot")
        self.root.geometry("500x400")

        # Log Textbox
        self.log_textbox = tk.Text(self.root, wrap=tk.WORD, state=tk.NORMAL)
        self.log_textbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Buttons
        self.run_button = tk.Button(self.root, text="Run Unfollow Bot", command=self.run_unfollow_function)
        self.run_button.pack(pady=5)

        self.close_button = tk.Button(self.root, text="Close", command=self.on_close)
        self.close_button.pack(pady=5)

    def run_unfollow_function(self):
        """Run the unfollow bot in a thread."""

        def run():
            self.bot.run_unfollow_workflow()

        threading.Thread(target=run).start()

    def log_activity(self, message):
        """Pass-through to bot's logging."""
        self.bot.log_activity(message)

    def on_close(self):
        """Handle app closure."""
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()


# Main execution block (Example setup)
if __name__ == "__main__":
    from selenium import webdriver

    # Initialize Selenium WebDriver (adjust this as per your browser and setup)
    driver = webdriver.Chrome()  # Ensure you have the driver in your PATH

    # Tkinter UI setup
    root = tk.Tk()

    # Initialize UnfollowBot and GUIApp
    log_box = tk.Text(root)
    unfollow_bot = UnfollowBot(driver, log_box)
    app = GUIApp(root, unfollow_bot)

    # Run the Tkinter main loop
    root.mainloop()

    # Ensure the WebDriver quits properly
    driver.quit()
