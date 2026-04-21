import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By


class AutomationApp:

    def __init__(self, root):
        # Initialize Tkinter UI
        self.root = root
        self.root.title("Post Execution Automation")
        self.initialize_user_interface()

        # Selenium WebDriver setup
        self.driver = webdriver.Chrome()  # Ensure the correct WebDriver is set

        # Initialize class variables for settings
        self.use_post_project_rotation = False
        self.total_used_images = 0
        self.infinite_post_loop = False
        self.selected_post_option = ""

    def initialize_user_interface(self):
        # Create UI elements
        self.rotation_check_var = tk.BooleanVar()
        self.post_option_var = tk.StringVar(value="Account Rotation - Post Now")

        tk.Checkbutton(self.root, text="Use Post Project Rotation", variable=self.rotation_check_var).pack(pady=5)
        tk.Label(self.root, text="Select Post Option:").pack(pady=5)
        tk.OptionMenu(self.root, self.post_option_var, "Account Rotation - Post Now",
                      "Account Rotation - On Schedule").pack(pady=5)
        tk.Button(self.root, text="Start Execution", command=self.execute_main_post_execution_block).pack(pady=10)

    def execute_main_post_execution_block(self):
        # Run 'MainPostExecutionBlock' logic
        try:
            self.use_post_project_rotation = self.rotation_check_var.get()
            self.selected_post_option = self.post_option_var.get()

            if self.use_post_project_rotation and self.total_used_images > 0:
                self.remove_used_images()

            if self.use_post_project_rotation:
                self.get_upload_project_folder()
                self.get_project_caption_files()
                self.get_project_settings_files()

            if self.check_statistics_table_columns():
                self.create_statistics_table()

            while not self.infinite_post_loop:
                self.perform_account_rotation_logic()

                # Rotate to next account
                self.kill_switch_check()
                self.execute_rotate_next_script()

                if self.use_post_project_rotation:
                    self.remove_used_images()

            messagebox.showinfo("Success", "Execution completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def remove_used_images(self):
        print("Removing used images...")
        # Selenium command to manipulate browser/filesystem, if applicable

    def get_upload_project_folder(self):
        print("Obtaining upload project folder...")

    def get_project_caption_files(self):
        print("Getting project caption files...")

    def get_project_settings_files(self):
        print("Loading project settings files...")

    def check_statistics_table_columns(self):
        # Simulating a table column check with Selenium
        print("Checking if statistics table columns are less than 10...")
        return True

    def create_statistics_table(self):
        print("Creating statistics table...")

    def perform_account_rotation_logic(self):
        if self.use_post_project_rotation:
            print("Performing project rotation logic...")
            self.pull_upload_folder_image_paths()
            self.create_caption_list_from_path()
            self.auto_load_post_project_settings()

        if self.selected_post_option == "Account Rotation - Post Now":
            print("Account Rotation - Post Now selected...")
            for _ in range(1, 6):  # Example loop for posting
                self.clear_log_system()
                self.rotation_post_now_system()

        elif self.selected_post_option == "Account Rotation - On Schedule":
            print("Account Rotation - On Schedule selected...")
            self.clear_log_system()
            self.rotation_post_on_schedule_system()

    def pull_upload_folder_image_paths(self):
        print("Pulling upload folder image paths...")

    def create_caption_list_from_path(self):
        print("Creating caption list from paths...")

    def auto_load_post_project_settings(self):
        print("Loading post project settings automatically...")

    def clear_log_system(self):
        print("Clearing log system...")

    def rotation_post_now_system(self):
        print("Executing rotation post now system...")

    def rotation_post_on_schedule_system(self):
        print("Executing rotation on schedule system...")

    def kill_switch_check(self):
        print("Checking kill switch...")

    def execute_rotate_next_script(self):
        print("Executing rotate to next script...")


def main():
    root = tk.Tk()
    app = AutomationApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from datetime import datetime


class AutomationApp:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Replace with your browser driver setup
        self.root = Tk()
        self.use_post_project_rotation = BooleanVar(value=False)
        self.image_captions = []
        self.post_schedule = []
        self.image_paths = []
        self.text_area_id = None  # Placeholder for the log textarea in Tkinter UI
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Set up the Tkinter user interface."""
        self.root.title("Post Rotation System")
        self.root.geometry("600x400")

        # Checkbox for Project Folder Rotation
        rotation_check_button = Checkbutton(
            self.root,
            text="Use Project Folder Rotation",
            variable=self.use_post_project_rotation
        )
        rotation_check_button.pack(pady=10)

        # Log display
        self.text_area_id = Text(self.root, height=20, width=70)
        self.text_area_id.pack()

        Button(self.root, text="Start Process", command=self.rotate_post_system_up).pack(pady=10)

    def rotate_post_system_up(self):
        """Python implementation of $RotatePostSystemUp logic."""
        # Step 1: Clear internalized lists
        self.image_captions.clear()
        self.post_schedule.clear()

        # Step 2: Handle project folder rotation logic
        if self.use_post_project_rotation.get():
            self.log_message("Getting images from the project folder rotation.")
            self.pull_upload_folder_image_paths()
        else:
            self.image_paths.clear()
            uploads_folder = os.path.join(os.getenv("APPDATA", ""), "uploads")
            self.image_paths = [
                os.path.join(uploads_folder, file) for file in os.listdir(uploads_folder) if
                os.path.isfile(os.path.join(uploads_folder, file))
            ]

        # Log the reset
        self.log_message("Resetting all internalized lists and paths. Internalization complete.")

        # Step 3: Check if images are available
        if self.image_paths:
            self.log_message("Your post images folder has images. Botting can commence.")
        else:
            self.log_message("Your post images folder is empty. Please load more images.")
            messagebox.showerror("Error", "No images found in the post images folder.")
            return

        # Step 4: Create caption list if using project rotation
        if self.use_post_project_rotation.get():
            self.log_message("Creating caption list from the project folders.")
            self.create_caption_list_from_path()
        elif self.image_captions:
            self.log_message("Captions detected and loaded successfully.")
        else:
            self.log_message("Captions not detected. Please load a caption file.")
            return

        # Step 5: Check scheduling information
        if self.post_schedule:
            self.log_message("Scheduled posts detected. Scheduled posting can commence.")
        else:
            self.log_message("Schedule not detected. Please load timestamps for scheduled posts.")
            messagebox.showwarning("Warning", "Post schedule not loaded.")

        # Step 6: Reset global variables
        self.log_message("Resetting all counters and internal variables.")
        self.reset_global_variables()

    def pull_upload_folder_image_paths(self):
        """Pull image paths from the project folders and log them."""
        # Example logic to populate `image_paths` (mimics project folder rotation behavior)
        project_folder = "project_folder_path"  # Replace with the real project folder path
        if os.path.exists(project_folder):
            self.image_paths = [
                os.path.join(project_folder, file) for file in os.listdir(project_folder)
                if os.path.isfile(os.path.join(project_folder, file))
            ]
            self.log_message(f"Loaded {len(self.image_paths)} images from project folder.")
        else:
            self.log_message("Project folder not found.")

    def create_caption_list_from_path(self):
        """Load captions from files."""
        caption_folder = "caption_folder_path"  # Replace with the real folder for captions
        try:
            for file in os.listdir(caption_folder):
                if file.endswith(".txt"):
                    with open(os.path.join(caption_folder, file), "r") as caption_file:
                        self.image_captions.extend(caption_file.read().splitlines())
            self.log_message(f"Loaded {len(self.image_captions)} captions.")
        except FileNotFoundError:
            self.log_message("Caption folder not found or empty.")

    def reset_global_variables(self):
        """Reset internal variables."""
        self.image_captions_pos = 0
        self.post_schedule_pos = 0
        self.image_paths_pos = 0
        self.master_delay_trigger = 0
        self.count_ui_display = 0
        self.display_running = ""
        self.post_counter = 0
        self.delay_ticker = 0
        self.delay_time = 0

    def log_message(self, message):
        """Log a message in the UI."""
        current_time = datetime.now().strftime("%H:%M:%S")
        log_entry = f"{current_time} - {message}\n"
        self.text_area_id.insert(END, log_entry)
        self.text_area_id.see(END)


def main():
    app = AutomationApp()
    app.root.mainloop()


if __name__ == "__main__":
    main()

import os
import time
from tkinter import Tk, Text, Label, Button, StringVar, filedialog, OptionMenu
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class AutomationApp:
    def __init__(self):
        self.driver = None
        self.image_paths = []
        self.image_captions = []
        self.image_paths_pos = 0
        self.image_captions_pos = 0
        self.post_counter = 0
        self.stop_bot_at = 5  # You may change this value to configure stopping behavior

        # Tkinter Root Initialization
        self.root = Tk()
        self.root.title("Instagram Automation")

        self.log_text = None
        self.post_option_var = StringVar(value="Default Post Option")
        self.initialize_user_interface()

    def initialize_user_interface(self):
        # Label for Options
        Label(self.root, text="Post Options:").pack()

        # Dropdown Menu for Post Options
        option_menu = OptionMenu(self.root, self.post_option_var, "Default Post Option", "Rotate Post")
        option_menu.pack()

        # Button to Start Automation
        start_button = Button(self.root, text="Start Post Automation", command=self.execute_main_post_execution_block)
        start_button.pack()

        # Log Text Area
        self.log_text = Text(self.root, height=10, width=50)
        self.log_text.pack()

        # Scroll-To End Functionality
        self.log_text.insert('end', "Log System Initialized...\n")

    def log_message(self, message):
        timestamp = time.strftime("[%Y-%m-%d %H:%M:%S] ")
        self.log_text.insert('end', f"{timestamp} {message}\n")
        self.log_text.see('end')  # Automatically scroll to the end of the text area
        self.root.update_idletasks()

    def execute_main_post_execution_block(self):
        try:
            self.log_message("Starting Automation Process...")

            # Initialize WebDriver (Chrome in this case)
            self.driver = webdriver.Chrome()  # Ensure 'chromedriver' is in PATH
            self.driver.get("https://instagram.com/")
            self.log_message("Navigated to Instagram")

            # Login or Wait for the Login
            self.wait_for_element(By.XPATH, "//input[@name='username']", timeout=10)
            self.log_message("Waiting for login page...")

            # Main posting logic
            while self.post_counter < self.stop_bot_at:
                self.rotation_post_now_system()

            self.log_message("Automation process completed successfully.")
        except Exception as e:
            self.log_message(f"An error occurred: {e}")
        finally:
            if self.driver:
                self.driver.quit()
                self.log_message("Browser closed.")

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def rotation_post_now_system(self):
        try:
            # Navigate to upload page
            self.log_message("Navigating to upload post page")
            self.wait_for_element(By.XPATH, "//span[@id='react-root']/section/nav[2]/div/div/div[2]/div/div/div[3]/div",
                                  timeout=10)
            time.sleep(2)

            # Click on the post creation button
            self.driver.find_element(By.XPATH,
                                     "//span[@id='react-root']/section/nav[2]/div/div/div[2]/div/div/div[3]/div").click()
            self.log_message("Clicked to create a post.")
            time.sleep(4)

            # Upload Image
            if self.image_paths_pos < len(self.image_paths):
                image_path = self.image_paths[self.image_paths_pos]
                self.driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(image_path)
                self.log_message(f"Uploading image: {image_path}")

                # Wait until upload is completed
                self.wait_for_element(By.XPATH, "//button[text()='Next']", timeout=10)
                self.driver.find_element(By.XPATH, "//button[text()='Next']").click()
                self.log_message("Clicked next after image upload.")

                # Add Caption
                if self.image_captions_pos < len(self.image_captions):
                    caption = self.image_captions[self.image_captions_pos]
                    self.wait_for_element(By.XPATH, "//textarea[@placeholder='Write a caption…']", timeout=10)
                    caption_box = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Write a caption…']")
                    caption_box.send_keys(caption)
                    self.log_message(f"Caption added: {caption}")
                    self.image_captions_pos += 1

                # Submit Post
                self.driver.find_element(By.XPATH, "//button[text()='Share']").click()
                self.log_message("Post shared.")
                time.sleep(5)  # Wait for post completion

                # Increment Counters
                self.post_counter += 1
                self.image_paths_pos += 1
                self.log_message(f"Post count: {self.post_counter}")
            else:
                self.log_message("No more images to upload. Stopping process.")
                raise StopIteration

        except Exception as e:
            self.log_message(f"Error during post process: {e}")

    def pull_upload_folder_image_paths(self, folder_path):
        if not os.path.exists(folder_path):
            raise Exception("Path does not exist")

        self.image_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if
                            file.endswith(('jpg', 'png'))]
        self.log_message(f"Loaded {len(self.image_paths)} images from folder.")

    def create_caption_list_from_path(self, caption_file_path):
        if not os.path.exists(caption_file_path):
            raise Exception("Caption file does not exist")

        with open(caption_file_path, 'r') as f:
            self.image_captions = f.readlines()

        self.log_message(f"Loaded {len(self.image_captions)} captions from file.")


if __name__ == "__main__":
    app = AutomationApp()
    app.root.mainloop()

import time
from tkinter import Tk, Text, StringVar, Label, Button, filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutomationApp:
    """Main Application with Selenium for browser automation and Tkinter for UI"""

    def __init__(self):
        # Initialize the Tkinter app
        self.root = Tk()
        self.root.title("Rotation and Schedule System")
        self.log_text = None
        self.initialize_user_interface()  # Set up the UI components

        # Initialize Selenium WebDriver
        self.driver = webdriver.Chrome()  # Replace with your driver (e.g., ChromeDriver)
        self.post_schedule_pos = 0
        self.image_paths = []
        self.image_captions = []
        self.post_counter = 0
        self.image_captions_pos = 0
        self.image_paths_pos = 0
        self.stop_bot_at = 10  # Maximum number of posts before stopping, customizable

    def initialize_user_interface(self):
        """Set up the main UI for the program."""
        Label(self.root, text="Automation App - Web Posting Bot").pack()

        # Log display area
        self.log_text = Text(self.root, height=20, width=80)
        self.log_text.pack()

        # Buttons
        Button(self.root, text="Start Posting", command=self.rotation_post_on_schedule_system).pack()
        Button(self.root, text="Load Images", command=self.load_images).pack()
        Button(self.root, text="Load Captions", command=self.load_captions).pack()

    def log_message(self, message: str):
        """Log messages to the Tkinter UI."""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {message}\n"
        self.log_text.insert("end", log_entry)
        self.log_text.see("end")  # Auto-scroll to the bottom

    def load_images(self):
        """Load image files for posting."""
        file_paths = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
        )
        self.image_paths = list(file_paths)
        self.log_message(f"Loaded {len(self.image_paths)} images for posting.")

    def load_captions(self):
        """Load captions from a file."""
        file_path = filedialog.askopenfilename(
            title="Select Caption File",
            filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            with open(file_path, "r") as file:
                self.image_captions = file.read().splitlines()
            self.log_message(f"Loaded {len(self.image_captions)} captions.")

    def rotation_post_on_schedule_system(self):
        """Main scheduled posting loop."""
        self.log_message("Starting scheduled posting loop...")
        self.driver.get("https://instagram.com")

        # Wait until the page is loaded and the specified element appears
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@id='react-root']/section/nav[2]/div/div/div[2]/div/div/div[3]/div")
            )
        )
        self.log_message("Instagram page loaded successfully.")

        while self.post_schedule_pos < len(self.image_paths):
            # Check schedule for posting
            self.log_message(f"Processing post {self.post_schedule_pos + 1}...")

            # Navigate to post creation area
            post_button = self.driver.find_element(
                By.XPATH,
                "//span[@id='react-root']/section/nav[2]/div/div/div[2]/div/div/div[3]/div"
            )
            post_button.click()
            time.sleep(2)  # Short delay to allow the page to load

            # Upload image
            image_upload_path = self.image_paths[self.image_paths_pos]
            self.log_message(f"Uploading image: {image_upload_path}")
            # This assumes Selenium's file upload dialog functionality:
            file_input = self.driver.find_element(By.TAG_NAME, "input")
            file_input.send_keys(image_upload_path)

            # Add Caption
            spun_caption = self.get_spun_caption()
            if spun_caption:
                self.log_message("Adding caption to the post.")
                caption_input = self.driver.find_element(
                    By.XPATH, "//textarea[@placeholder='Write a caption…']"
                )
                caption_input.send_keys(spun_caption)
            else:
                self.log_message("No caption detected. Skipping caption posting.")

            # Post the image
            next_button = self.driver.find_element(
                By.XPATH,
                "//span[@id='react-root']/section/div[1]/header/div[2]/button"
            )
            next_button.click()

            # Successful post message
            self.post_counter += 1
            self.log_message(
                f"Post successful. Post count = {self.post_counter}."
            )

            # Increment counters
            self.image_paths_pos += 1
            self.image_captions_pos += 1
            self.post_schedule_pos += 1

            # Stop the script if limit is reached
            if self.post_counter >= self.stop_bot_at:
                self.log_message("Stop criteria met. Stopping the bot.")
                self.driver.quit()
                return

            # Reset counters if necessary
            if self.image_paths_pos >= len(self.image_paths):
                self.log_message("Image folder depleted. Reload more images to continue.")
                break

            if self.image_captions_pos >= len(self.image_captions):
                self.log_message("Caption list depleted. Resetting caption list.")
                self.image_captions_pos = 0

        self.log_message("Scheduled posting loop completed.")
        self.driver.quit()

    def get_spun_caption(self) -> str:
        """Generate a spun caption (mockup for spintax logic)."""
        if self.image_captions_pos < len(self.image_captions):
            return self.image_captions[self.image_captions_pos]
        return ""


# Run the app
if __name__ == "__main__":
    app = AutomationApp()
    app.root.mainloop()

import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


class RotationSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rotation Scheduler")

        # Initialize browser driver (Ensure driver executable is in PATH)
        self.driver = webdriver.Chrome()

        # Setting up UI components
        self.initialize_user_interface()

        # Variables for scheduling
        self.schedule_trigger = False
        self.post_schedule_position = 0
        self.post_schedule = [5, 10, 15]  # Example schedule (in seconds)

    def initialize_user_interface(self):
        # Text Area for Logs
        self.log_text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=20, state=tk.NORMAL)
        self.log_text_area.grid(row=0, column=0, padx=10, pady=10)

        # Start and Stop Buttons
        start_button = tk.Button(self.root, text="Start Scheduler", command=self.start_scheduler)
        start_button.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        stop_button = tk.Button(self.root, text="Stop Scheduler", command=self.stop_scheduler)
        stop_button.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    def log_message(self, message):
        # Log messages with timestamps to the text area
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_message = f"{current_time} - {message}\n"
        self.log_text_area.insert(tk.END, full_message)
        self.log_text_area.see(tk.END)  # Auto-scroll to the latest log entry

    def start_scheduler(self):
        self.schedule_trigger = True
        self.log_message("Scheduler has been initiated.")
        self.run_schedule()

    def stop_scheduler(self):
        self.schedule_trigger = False
        self.log_message("Scheduler has been stopped.")

    def run_schedule(self):
        while self.schedule_trigger:
            self.log_message("Scheduler is running.")
            try:
                # Example JavaScript actions (update to fit use case)
                self.driver.execute_script(
                    """
                    var textarea = document.getElementById('textarea_id');
                    textarea.value += 'Scheduler triggers running...\\n';
                    textarea.scrollTop = textarea.scrollHeight;
                    """
                )

                # Automating actions: Adjust as per specific task requirements
                current_datetime = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
                self.log_message(f"Current DateTime: {current_datetime}")

                # Waiting for the next schedule (Simulates basic wait mechanism)
                time.sleep(self.post_schedule[self.post_schedule_position])

                # Rotate through the schedule
                self.post_schedule_position = (self.post_schedule_position + 1) % len(self.post_schedule)

            except Exception as e:
                self.log_message(f"Error occurred: {e}")
                self.stop_scheduler()

        # Final log when scheduler stops
        self.log_message("Scheduler tasks completed.")

    def __del__(self):
        # Cleanup resources
        if hasattr(self, 'driver'):
            self.driver.quit()


def main():
    # Main application entry point
    root = tk.Tk()
    app = RotationSchedulerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class AutomationApp:
    def __init__(self):
        # Initialize UI root window
        self.root = tk.Tk()
        self.root.title("Automation Control Panel")

        # Define necessary attributes for automation
        self.driver = None
        self.image_paths_pos = 0
        self.image_captions_pos = 0
        self.UploadFoldersPos = 0
        self.CaptionPathsPos = 0
        self.ProjectSettingsPathsPos = 0
        self.trigger_one = 0
        self.account_row = 0
        self.proxy_row = 0
        self.use_post_project_rotation = tk.BooleanVar(value=False)  # Toggle Rotation
        self.text_area = None

        # Call interface initialization
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """
        Initialize the Tkinter user interface for the application.
        """
        # Checkbox for post-project rotation
        tk.Checkbutton(
            self.root,
            text="Use Post Project Rotation",
            variable=self.use_post_project_rotation
        ).grid(row=0, column=0, sticky="w")

        # Start button
        tk.Button(
            self.root,
            text="Start Automation",
            command=self.execute_main_post_execution_block
        ).grid(row=1, column=0, pady=10)

        # Text area for logging
        self.text_area = tk.Text(self.root, width=100, height=20, state='normal')
        self.text_area.grid(row=2, column=0, pady=10)

    def log_message(self, message: str):
        """
        Log messages into the Tkinter text area with timestamps.
        """
        current_time = time.strftime("%H:%M:%S")
        self.text_area.insert(tk.END, f"{current_time} - {message}\n")
        self.text_area.see(tk.END)

    def execute_main_post_execution_block(self):
        """
        Executes the main automation logic.
        """
        # Initial logging
        self.log_message("Automation started - SYSTEM SETUP INITIATED.")

        # Post rotation logic
        if self.use_post_project_rotation.get():
            self.image_paths_pos = 0
            self.image_captions_pos = 0
            self.log_message("Resetting post project rotation variables.")

            if self.trigger_one != 0:
                self.UploadFoldersPos += 1
                self.CaptionPathsPos += 1
                self.ProjectSettingsPathsPos += 1
            else:
                self.UploadFoldersPos = 0
                self.CaptionPathsPos = 0
                self.ProjectSettingsPathsPos = 0

        # Start browser instance for automation
        self.start_browser()

    def start_browser(self):
        """
        Starts a Selenium WebDriver instance for browser interaction.
        """
        try:
            # Setup Chrome WebDriver
            self.driver = webdriver.Chrome(executable_path='./chromedriver')
            self.driver.get('https://www.instagram.com/accounts/login/')
            self.log_message("Browser started. Navigating to Instagram login page.")

            # Wait for login page elements to load
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            self.log_message("Instagram login page loaded. Ready to enter credentials.")

            # Enter Instagram credentials
            username_input = self.driver.find_element(By.NAME, "username")
            password_input = self.driver.find_element(By.NAME, "password")

            # Example values for login
            example_username = "test_user"
            example_password = "test_password"

            username_input.send_keys(example_username)
            self.log_message("Entered username.")

            password_input.send_keys(example_password)
            self.log_message("Entered password.")

            # Click login button
            login_button = self.driver.find_element(
                By.XPATH, "//button[@type='submit']"
            )
            login_button.click()
            self.log_message("Clicked on the login button.")

            # Post-login checks
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//a[@title="Screenshot Window"]')
                )
            )
            self.log_message("Login successful. Proceeding with automation tasks.")
        except Exception as e:
            self.log_message(f"Error during browser automation: {e}")
            if self.driver:
                self.driver.quit()
        finally:
            if self.driver:
                self.driver.quit()

    def clear_temporary_files(self):
        """
        Clears temporary files if they exist.
        """
        temp_file_path = './temp/0.txt'
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            self.log_message("Temporary files cleared.")

    def start(self):
        """
        Start the Tkinter mainloop for UI.
        """
        self.root.mainloop()


if __name__ == "__main__":
    app = AutomationApp()
    app.start()

import tkinter as tk
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time


class AutomationApp:
    def __init__(self):
        """Initialize the Automation App."""
        self.driver = None  # Selenium WebDriver instance
        self.root = tk.Tk()  # Tkinter root window
        self.text_area = None  # Text area for logs
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Set up the Tkinter User Interface."""
        self.root.title("Automation Software")
        self.root.geometry("700x400")

        # Text Area
        self.text_area = tk.Text(self.root, wrap=tk.WORD, state=tk.DISABLED)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Add controls if needed in the real application
        # For the purpose of mapping to the original logic, only TextArea is shown

        self.log_message("{0} - APPLICATION STARTED\n".format(self.get_timestamp()))

    def log_message(self, message):
        """Logs messages to the text area."""
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, message)
        self.text_area.see(tk.END)
        self.text_area.config(state=tk.DISABLED)

    def perform_account_rotation_logic(self):
        """Handle account rotation logic and browser manipulation."""
        self.log_message(
            "{0} - ACCOUNT RESET INITIATED, CLEANING AND CLOSING CHROME - PLEASE WAIT!\n".format(self.get_timestamp()))

        # Set up Selenium WebDriver with Chrome
        try:
            self.driver = webdriver.Chrome(
                service=Service("/path/to/chromedriver"))  # Replace with your ChromeDriver path

            # Log operation (dummy example of browser manipulation)
            # You can replace the below logic with actual behavior
            self.driver.get("https://example.com")  # Visit a website
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            self.log_message("{0} - BROWSER SESSION ACTIVE\n".format(self.get_timestamp()))

        except WebDriverException as e:
            self.log_message("{0} - ERROR OCCURRED: {1}\n".format(self.get_timestamp(), str(e)))

        finally:
            # Cleanup browser session
            if self.driver:
                self.driver.quit()
                self.driver = None

        # Simulating cleaning other tables (e.g., clearing variables)
        self.clear_tables()

        # Stop activity after loop
        self.log_message("{0} - ACCOUNT RESET AND BROWSER CLOSED SUCCESSFULLY\n".format(self.get_timestamp()))

    def clear_tables(self):
        """Simulate clearing tables and resetting variables."""
        # Replace `accounts_table`, `proxy_table`, and other logic with actual data manipulation as needed
        self.log_message("{0} - Clearing accounts and proxy tables\n".format(self.get_timestamp()))
        # Simulated behavior

    def get_timestamp(self):
        """Return current timestamp as a formatted string."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def execute(self):
        """Start the Tkinter main event loop and initiate automated logic."""
        self.perform_account_rotation_logic()
        self.root.mainloop()


if __name__ == "__main__":
    app = AutomationApp()
    app.execute()

import tkinter as tk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AutomationApp:
    def __init__(self, driver):
        self.driver = driver
        self.account_row = 0
        self.accounts_table_rows = self.get_table_total_rows()
        self.use_post_project_rotation = "YES"
        self.run_rotation_rest_accounts = False
        self.run_post_rotation_login_block = False
        self.get_post_cell = 0
        self.current_posts = 0

        self.upload_folders_pos = 0
        self.caption_paths_pos = 0
        self.project_settings_paths_pos = 0

    def get_table_total_rows(self):
        """
        Simulate fetching the total rows of the accounts table.
        This logic would need specific Selenium instructions based on the HTML table used.
        """
        try:
            # Wait for the accounts table to load using Selenium
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "accounts_table"))
            )
            table = self.driver.find_element(By.ID, "accounts_table")
            rows = table.find_elements(By.TAG_NAME, "tr")
            return len(rows)
        except Exception as e:
            print(f"Error occurred while fetching the table rows: {str(e)}")
            return 0

    def rotation_account_rest(self):
        """
        Placeholder for the actual logic to handle account rotation reset.
        """
        print("Executing account rotation reset logic...")
        return True

    def post_rotation_login_block(self):
        """
        Placeholder for logic to manage post-rotation login blocking.
        """
        print("Executing post-rotation login block...")
        return True

    def execute_rotate_next_script(self):
        """
        Implements the main logic of $ExacutionRotateNextScript.
        """
        # Rotate To Next Account - Reset Accounts Table
        if self.account_row > (self.accounts_table_rows - 1):
            # Reset rotation for rest accounts
            self.run_rotation_rest_accounts = self.rotation_account_rest()

            if self.use_post_project_rotation == "YES":
                # Reset positions in the project arrays
                self.upload_folders_pos = 0
                self.caption_paths_pos = 0
                self.project_settings_paths_pos = 0

        # Set global variables for Post Rotation Login Block and other resets
        self.run_post_rotation_login_block = self.post_rotation_login_block()
        self.get_post_cell = 0
        self.current_posts = 0

        print("Rotation to next account logic completed.")


# UI Example using Tkinter
class AppUI:
    def __init__(self, root, automation_app):
        self.root = root
        self.automation_app = automation_app

        # Configure the User Interface
        self.root.title("Automation App")
        self.setup_ui()

    def setup_ui(self):
        # Create buttons and labels
        btn_execute_script = tk.Button(self.root, text="Execute Rotate Next Script", command=self.execute_script)
        btn_execute_script.pack(pady=10)

        lbl_status = tk.Label(self.root, text="Status: Ready")
        lbl_status.pack(pady=10)

        self.lbl_status = lbl_status

    def execute_script(self):
        try:
            self.automation_app.execute_rotate_next_script()
            self.lbl_status.configure(text="Status: Script Executed Successfully")
        except Exception as e:
            self.lbl_status.configure(text=f"Status: Error - {str(e)}")


# Driver setup (Add your selenium driver configuration here)
# Make sure `chromedriver` or other required driver is installed and in PATH.
from selenium import webdriver


def main():
    driver = webdriver.Chrome()  # Add path to your driver if needed
    automation_app = AutomationApp(driver)

    # Tkinter UI
    root = tk.Tk()
    ui = AppUI(root, automation_app)
    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By


class AutomationApp:
    def __init__(self):
        self.driver = None
        self.current_posts = 0
        self.root = tk.Tk()
        self.root.title("Rotation Post Statistics Automation")
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Set up the Tkinter UI components"""
        tk.Label(self.root, text="Statistics File Path:").grid(row=0, column=0, padx=10, pady=5)
        self.statistics_file_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.statistics_file_var, width=40).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Run Rotation Statistics", command=self.run_rotation_post_statistics).grid(row=1,
                                                                                                             column=1,
                                                                                                             pady=10)

    def initialize_webdriver(self):
        """Initialize Selenium WebDriver"""
        # Assumes ChromeDriver is in PATH
        try:
            self.driver = webdriver.Chrome()
        except Exception as e:
            messagebox.showerror("WebDriver Error", f"Error initializing WebDriver: {str(e)}")
            return None
        return self.driver

    def run_rotation_post_statistics(self):
        """Main function to execute the RotationPostStatistics logic."""
        statistics_file_path = self.statistics_file_var.get()
        if not statistics_file_path or not statistics_file_path.endswith(".txt"):
            messagebox.showerror("Input Error", "Please provide a valid statistics file path!")
            return

        try:
            # Simulate loading a file or interacting with data (a placeholder for actual file processing logic)
            post_row = 0  # Example row, this would depend on your data

            # Simulate function `$table cell get` logic to extract data
            post_cell_value = self.get_table_cell(statistics_file_path, post_row, 10)

            if post_cell_value and post_cell_value != "Does not equal":
                self.current_posts = int(post_cell_value) + 1
            if self.current_posts == 0:
                self.current_posts = 1

            # Simulate updating cell (10th column of the statistics table)
            self.update_table_cell(statistics_file_path, post_row, 10, self.current_posts)

            messagebox.showinfo("Execution Complete", "Rotation Post Statistics executed successfully.")

        except Exception as e:
            messagebox.showerror("Execution Error", f"An error occurred: {str(e)}")

    def get_table_cell(self, statistics_file, row, column):
        """
        Simulate retrieving cell value from the 'statistics' file.
        Replace this with the actual logic to extract data.
        """
        # Placeholder logic for file reading
        try:
            with open(statistics_file, 'r') as file:
                lines = file.readlines()
                if row < len(lines):
                    row_data = lines[row].split(",")
                    if column < len(row_data):
                        return row_data[column].strip()
            return ""
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {statistics_file}")

    def update_table_cell(self, statistics_file, row, column, value):
        """
        Simulate updating a cell in the 'statistics' file.
        Replace with actual file update logic.
        """
        try:
            with open(statistics_file, 'r') as file:
                lines = file.readlines()

            if row < len(lines):
                row_data = lines[row].split(",")
                if column < len(row_data):
                    row_data[column] = str(value)
                lines[row] = ",".join(row_data) + "\n"

            with open(statistics_file, 'w') as file:
                file.writelines(lines)

        except Exception as e:
            raise Exception(f"Error updating file: {str(e)}")


if __name__ == "__main__":
    app = AutomationApp()
    app.root.mainloop()

from tkinter import Tk, Button
from selenium import webdriver
import threading


class AutomationApp:
    def __init__(self):
        # Initialize WebDriver
        self.driver = webdriver.Chrome()

        # Initialize global variables
        self.used_images = []
        self.get_post_cell = 0
        self.current_posts = 0
        self.infinite_post_loop = 0
        self.run_rotation_user_error_system = None
        self.run_post_rotation_login_block = None
        self.run_rotate_post_system_up = None

        # Initialize Tkinter root
        self.root = Tk()
        self.root.title("Automation Control Panel")
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """
        Setup the Tkinter UI for controlling the Automation
        """
        Button(self.root, text="Run Post Execution Setup Scripts", command=self.run_post_execution_setup_scripts).pack(
            pady=10)
        Button(self.root, text="Quit", command=self.quit_application).pack(pady=10)

    def run_post_execution_setup_scripts(self):
        """
        Implements behavior similar to $PostExacutionSetupScripts or performs the setup tasks.
        """
        # Clear the list of used images
        self.used_images.clear()

        # Reset all necessary global variables
        self.get_post_cell = 0
        self.current_posts = 0
        self.infinite_post_loop = 0

        # Reset/initialize critical components
        self.run_rotation_user_error_system = self.rotation_user_error_system()
        self.run_post_rotation_login_block = self.post_rotation_login_block()
        self.run_rotate_post_system_up = self.rotate_post_system_up()

        print("Post Execution Setup Scripts completed.")

    def rotation_user_error_system(self):
        """
        Placeholder for rotation user error system logic
        """
        print("Rotation User Error System initialized.")
        return True  # Simulate successful initialization

    def post_rotation_login_block(self):
        """
        Placeholder for post-rotation login block logic
        """
        print("Post Rotation Login Block initialized.")
        return True  # Simulate successful initialization

    def rotate_post_system_up(self):
        """
        Placeholder for rotate post system up logic
        """
        print("Rotate Post System Up initialized.")
        return True  # Simulate successful initialization

    def quit_application(self):
        """
        Gracefully shuts down the application.
        """
        self.driver.quit()  # Close the WebDriver
        self.root.quit()  # Close the tkinter UI
        print("Application terminated.")


# Run the application
if __name__ == "__main__":
    app = AutomationApp()

    # Run Tkinter mainloop in a separate thread to allow Selenium tasks to run concurrently
    threading.Thread(target=app.root.mainloop).start()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


class AutomationApp:

    def __init__(self, root):
        # Initialize Selenium WebDriver (make sure you have the correct WebDriver for your browser)
        self.driver = webdriver.Chrome()
        self.root = root
        self.root.title("Instagram Post Bot")

        # UI Variables
        self.post_option_var = tk.StringVar()
        self.account_file = ''
        self.image_captions = ''
        self.post_schedule = ''
        self.num_post_now = ''
        self.stop_bot_at = ''
        self.text_log = None

        # UI Initialization
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Initialize the Tkinter UI."""
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Dropdown menu for post options
        tk.Label(frame, text="Post Options:").grid(row=0, column=0, sticky="w")
        dropdown = tk.OptionMenu(frame, self.post_option_var, "Post Now", "On Schedule")
        dropdown.grid(row=0, column=1, sticky="w")

        # Text Area for Logging
        tk.Label(self.root, text="Log:").pack(pady=5)
        self.text_log = tk.Text(self.root, wrap=tk.WORD, height=15, width=50)
        self.text_log.pack()

        # Buttons
        run_button = tk.Button(self.root, text="Run", command=self.run_rotation_user_error_system)
        run_button.pack(pady=5)

    def log_message(self, message):
        """Log a message to the text area."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.text_log.insert(tk.END, f"{timestamp} - {message}\n")
        self.text_log.see(tk.END)

    def run_rotation_user_error_system(self):
        """Main logic for Rotation User Error System."""
        try:
            # Simple Error Handling for UI Inputs
            if not self.post_option_var.get():
                self.log_message("TO USE THE POST BOT YOU MUST SELECT A POST OPTION FROM THE DROPDOWN.")
                messagebox.showwarning("Input Error", "Please select a Post Option.")
                return

            if not self.account_file:
                self.log_message("Please provide the account file.")
                messagebox.showwarning("Input Error", "You must select your account file.")
                return

            if not self.image_captions:
                self.log_message("If you use captions, please upload a caption file.")

            # Launch Browser Automation
            self.driver.get("file:///path_to_your_log_ui.html")  # Update with your log file path

            # Wait for textarea element to appear
            self.log_message("Loading Log UI in browser...")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "textarea_id"))
            )

            self.log_message("Log UI loaded successfully. Initializing log...")
            self.append_to_textarea("SOFTWARE RUNNING - THE LOG HAS BEEN LOADED AND STARTED SUCCESSFULLY")

            # Additional logic based on post option
            if self.post_option_var.get() == "On Schedule":
                if not self.post_schedule:
                    self.log_message("PLEASE ADD YOUR DATE AND TIME STAMPS INTO THE POST SCHEDULED BOX.")
                    messagebox.showwarning("Input Error", "Add your date and time stamps to the Post Schedule.")
                    return

            elif self.post_option_var.get() == "Post Now":
                if not self.num_post_now:
                    self.log_message("TO USE THE POST NOW SETTING ENTER A NUMBER IN THE POST NOW BOX.")
                    messagebox.showwarning("Input Error", "Enter a number in the Post Now box.")
                    return

                if not self.stop_bot_at:
                    self.log_message("TO USE THE POST NOW SETTING PLEASE SPECIFY WHEN TO STOP POSTING.")
                    messagebox.showwarning("Input Error", "Specify when to stop posting.")
                    return

            self.log_message(f"Post Bot started successfully with option: {self.post_option_var.get()}.")

        except Exception as e:
            self.log_message(f"An error occurred: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def append_to_textarea(self, message):
        """Run JavaScript to append to the textarea in the browser."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        script = (
            f"let textarea = document.getElementById('textarea_id'); "
            f"textarea.value += '{timestamp} - {message}\\n'; "
            f"textarea.scrollTop = textarea.scrollHeight;"
        )
        self.driver.execute_script(script)


if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutomationApp:
    def __init__(self, root):
        """
        Initialize the AutomationApp with Tkinter window root and setup UI.

        :param root: Tkinter window root instance
        """
        self.root = root
        self.root.title("Automation App")

        # Initialize application variables
        self.accounts_table = []  # Placeholder for account table
        self.proxy_table = []  # Placeholder for proxy table
        self.proxy_row = None
        self.account_row = None
        self.trigger_one = None

        # Selenium WebDriver initialization
        self.driver = None

        self.initialize_user_interface()

    def initialize_user_interface(self):
        """
        Creates the main UI for the application
        """
        # Sample UI with Buttons
        frame = tk.Frame(self.root)
        frame.pack(pady=20, padx=20)

        tk.Button(frame, text="Start Login Account Reset", command=self.start_login_account_rest).grid(row=0, column=0,
                                                                                                       padx=10, pady=5)

        tk.Button(frame, text="Exit", command=self.exit_application).grid(row=0, column=1, padx=10, pady=5)

    def start_login_account_rest(self):
        """
        Resets the login account environment.

        #RunStartLoginAccountRest equivalent
        """
        try:
            # Clear accounts and proxy table
            self.accounts_table.clear()
            self.proxy_table.clear()

            # Reset global variables
            self.set_global_variable(name="proxy_row", value=0)
            self.set_global_variable(name="account_row", value=0)
            self.set_global_variable(name="trigger_one", value=0)

            messagebox.showinfo("Success", "Start Login Account Reset was successful!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def set_global_variable(self, name, value):
        """
        Sets a global variable within the application context.

        :param name: Name of the variable (str)
        :param value: Value to assign
        """
        if name == "proxy_row":
            self.proxy_row = value
        elif name == "account_row":
            self.account_row = value
        elif name == "trigger_one":
            self.trigger_one = value
        else:
            raise ValueError(f"Unknown variable name: {name}")

    def exit_application(self):
        """
        Exit the application.
        """
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            if self.driver:
                self.driver.quit()  # Close the Selenium WebDriver if running
            self.root.quit()


if __name__ == "__main__":
    # Create the application window
    root = tk.Tk()
    app = AutomationApp(root)
    root.mainloop()

from tkinter import Tk, Label, Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread


class AutomationApp:
    def __init__(self):
        # Initialize the root for the Tkinter GUI
        self.root = Tk()
        self.root.title("Automation App - Kill Switch Monitor")

        # Selenium driver initialization (adjust this based on your browser)
        self.driver = None
        self.initialize_webdriver()

        # UI Initialization
        self.initialize_user_interface()

    def initialize_webdriver(self):
        """Initialize the Selenium WebDriver."""
        try:
            # Example: Initialize Chrome WebDriver
            self.driver = webdriver.Chrome()
        except Exception as e:
            print(f"Error initializing WebDriver: {e}")

    def initialize_user_interface(self):
        """Initialize the Tkinter User Interface."""
        Label(self.root, text="Kill Switch Status:").pack(pady=10)

        self.kill_switch_status_label = Label(
            self.root, text="Checking...", fg="blue"
        )
        self.kill_switch_status_label.pack(pady=10)

        # Button to start the Kill Switch Check
        start_button = Button(
            self.root,
            text="Start Monitoring Kill Switch",
            command=self.start_kill_switch_monitoring,
        )
        start_button.pack(pady=10)

        # Button to stop the Kill Switch Check
        stop_button = Button(
            self.root,
            text="Stop Monitoring",
            command=self.stop_kill_switch_monitoring,
        )
        stop_button.pack(pady=10)

        # Button to exit the application
        exit_button = Button(
            self.root, text="Exit", command=self.exit_application
        )
        exit_button.pack(pady=10)

    def kill_switch_check(self):
        """Check if the kill switch is active by monitoring the browser status."""
        try:
            while self.kill_switch_active:
                # Example Condition: Check if the browser is alive
                is_alive = self.check_browser_alive()

                # Update UI with the status
                self.update_kill_switch_status(is_alive)

                if not is_alive:  # Break loop if browser is no longer active
                    print("Browser is no longer active. Exiting...")
                    break
        except Exception as e:
            print(f"Error in kill switch monitoring: {e}")

    def check_browser_alive(self):
        """Check whether the browser is alive."""
        try:
            # Try accessing a known page or element
            self.driver.get("https://www.google.com")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            return True
        except Exception:
            return False

    def update_kill_switch_status(self, is_alive):
        """Update the status of the kill switch in the UI."""
        if is_alive:
            self.kill_switch_status_label.config(text="Browser Alive", fg="green")
        else:
            self.kill_switch_status_label.config(text="Browser Dead", fg="red")

    def start_kill_switch_monitoring(self):
        """Start monitoring the kill switch in a separate thread."""
        self.kill_switch_active = True
        self.monitor_thread = Thread(target=self.kill_switch_check)
        self.monitor_thread.daemon = True  # Ensure thread exits with the app
        self.monitor_thread.start()

    def stop_kill_switch_monitoring(self):
        """Stop monitoring the kill switch."""
        self.kill_switch_active = False
        self.kill_switch_status_label.config(
            text="Monitoring Stopped", fg="orange"
        )

    def exit_application(self):
        """Exit the application and close resources."""
        try:
            if self.driver:
                self.driver.quit()  # Ensure driver quits
        except Exception as e:
            print(f"Error closing WebDriver: {e}")
        self.root.quit()  # Close the Tkinter application

    def run(self):
        """Run the Tkinter main loop."""
        self.root.mainloop()


if __name__ == "__main__":
    app = AutomationApp()
    app.run()
