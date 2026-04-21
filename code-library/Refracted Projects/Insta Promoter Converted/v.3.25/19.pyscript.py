import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Function to initialize Selenium WebDriver
def initialize_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service("/path/to/chromedriver")  # Replace with the actual path to chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


# Tkinter UI Class
class QuickView1App:
    def __init__(self, root):
        self.root = root
        self.root.title("Succession Module Quick Access Settings")
        self.root.geometry("800x600")

        # Define variables for user inputs
        self.follow_per_tag = tk.StringVar()
        self.like_per_tag = tk.StringVar()
        self.comment_per_tag = tk.StringVar()
        self.action_per_tag = tk.StringVar()
        self.autofollow_value = tk.StringVar()
        self.unfollow_value = tk.StringVar()
        self.unfollow_toggle = tk.StringVar()
        self.autofollow_toggle = tk.StringVar()
        self.enable_actioning = tk.StringVar()
        self.delay_time = tk.StringVar()
        self.master_delay = tk.StringVar()
        self.save_log_path = tk.StringVar()

        # Create the UI layout
        self.create_widgets()

    def create_widgets(self):
        # Create tabs
        notebook = ttk.Notebook(self.root)
        settings_frame = ttk.Frame(notebook)
        advanced_frame = ttk.Frame(notebook)
        rotation_frame = ttk.Frame(notebook)
        notebook.add(settings_frame, text="General Settings")
        notebook.add(advanced_frame, text="Advanced Settings")
        notebook.add(rotation_frame, text="Account Rotation")
        notebook.pack(expand=1, fill="both")

        # General Settings
        ttk.Label(settings_frame, text="Cycle Follows Per Tag:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(settings_frame, textvariable=self.follow_per_tag).grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(settings_frame, text="Cycle Likes Per Tag:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(settings_frame, textvariable=self.like_per_tag).grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(settings_frame, text="Enable Auto Follow Back:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        ttk.Checkbutton(settings_frame, variable=self.autofollow_toggle, onvalue="Enabled", offvalue="Disabled").grid(
            row=2, column=1, padx=10, pady=5)

        ttk.Label(settings_frame, text="Set Delay Counter (Seconds):").grid(row=3, column=0, sticky="w", padx=10,
                                                                            pady=5)
        ttk.Entry(settings_frame, textvariable=self.delay_time).grid(row=3, column=1, padx=10, pady=5)

        ttk.Button(settings_frame, text="Start Automation", command=self.start_automation).grid(row=10, column=0,
                                                                                                columnspan=2, pady=20)

        # Advanced Settings
        ttk.Label(advanced_frame, text="Master Delay (Seconds):").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(advanced_frame, textvariable=self.master_delay).grid(row=0, column=1, padx=10, pady=5)

        # Account Rotation
        ttk.Label(rotation_frame, text="Save Logs To File:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        ttk.Button(rotation_frame, text="Select File", command=self.select_log_file).grid(row=0, column=1, pady=5)

    def select_log_file(self):
        # File dialog for selecting the file path for saving logs
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"),
                                                           ("All files", "*.*")])
        if filename:
            self.save_log_path.set(filename)

    def start_automation(self):
        # Start Selenium automation with user-defined settings
        driver = initialize_driver()

        # Example automation (replace with your actual process)
        driver.get("https://example.com")  # Replace with your target URL
        messagebox.showinfo("Automation Started", "The browser automation has started.")


# Main Tkinter loop
if __name__ == "__main__":
    root = tk.Tk()
    app = QuickView1App(root)
    root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By


class QuickView2App:
    def __init__(self, root):
        self.root = root
        self.root.title("QuickView2 - Post Module Quick Access Settings")

        # Initialize attributes (from the provided settings)
        self.post_options = tk.StringVar()
        self.num_post_now = tk.StringVar()
        self.current_date_time = tk.StringVar()
        self.next_post_in = tk.StringVar()
        self.post_schedule = tk.StringVar()
        self.delay_time = tk.StringVar()
        self.stop_bot_at = tk.StringVar()
        self.master_delay = tk.StringVar()
        self.run_when_complete = tk.StringVar()
        self.random_wait_one = tk.StringVar()
        self.random_wait_two = tk.StringVar()
        self.account_file = tk.StringVar()
        self.proxy_file = tk.StringVar()
        self.image_captions = tk.StringVar()
        self.custom_settings_path = tk.StringVar()

        # Create the user interface
        self.create_widgets()

    def create_widgets(self):
        # Add widgets for Post Options
        tk.Label(self.root, text="Choose Post Option").grid(row=0, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.post_options).grid(row=0, column=1, pady=5)

        tk.Label(self.root, text="Number to Post Now").grid(row=1, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.num_post_now).grid(row=1, column=1, pady=5)

        tk.Label(self.root, text="Date Time Sec Designator").grid(row=2, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.current_date_time).grid(row=2, column=1, pady=5)

        tk.Label(self.root, text="Next Post Date Time").grid(row=3, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.next_post_in).grid(row=3, column=1, pady=5)

        tk.Label(self.root, text="Enter Your Post Schedule").grid(row=4, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.post_schedule).grid(row=4, column=1, pady=5)

        tk.Label(self.root, text="Set Delay Counter (Sec)").grid(row=5, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.delay_time).grid(row=5, column=1, pady=5)

        tk.Label(self.root, text="Stop the Software At").grid(row=6, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.stop_bot_at).grid(row=6, column=1, pady=5)

        tk.Label(self.root, text="Master Delay - Seconds").grid(row=7, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.master_delay).grid(row=7, column=1, pady=5)

        tk.Label(self.root, text="Run When Complete").grid(row=8, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.run_when_complete).grid(row=8, column=1, pady=5)

        tk.Label(self.root, text="Random Wait .1").grid(row=9, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.random_wait_one).grid(row=9, column=1, pady=5)

        tk.Label(self.root, text="Random Wait .2").grid(row=10, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.random_wait_two).grid(row=10, column=1, pady=5)

        tk.Label(self.root, text="Account File Path").grid(row=11, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.account_file).grid(row=11, column=1, pady=5)

        tk.Label(self.root, text="Proxy File Path").grid(row=12, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.proxy_file).grid(row=12, column=1, pady=5)

        tk.Label(self.root, text="Image Caption File Path").grid(row=13, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.image_captions).grid(row=13, column=1, pady=5)

        tk.Label(self.root, text="Custom Save/Load Path").grid(row=14, column=0, sticky=tk.W, pady=5)
        tk.Entry(self.root, textvariable=self.custom_settings_path).grid(row=14, column=1, pady=5)

        # Buttons to browse files
        tk.Button(self.root, text="Browse", command=lambda: self.browse_file(self.account_file)).grid(row=11, column=2)
        tk.Button(self.root, text="Browse", command=lambda: self.browse_file(self.proxy_file)).grid(row=12, column=2)
        tk.Button(self.root, text="Browse", command=lambda: self.browse_file(self.image_captions)).grid(row=13,
                                                                                                        column=2)

        # Start Button
        tk.Button(self.root, text="Start Automation", command=self.start_automation).grid(row=15, column=0,
                                                                                          columnspan=2, pady=10)

    def browse_file(self, variable):
        file_path = filedialog.askopenfilename()
        if file_path:
            variable.set(file_path)

    def start_automation(self):
        # Basic Selenium WebDriver setup
        try:
            driver = self.initialize_driver()
            # Example step: Navigate to a sample URL
            driver.get("https://example.com/")
            messagebox.showinfo("Automation", "Automation started successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            driver.quit()

    @staticmethod
    def initialize_driver():
        # Setup Selenium WebDriver (adjust the path to your driver)
        driver = webdriver.Chrome(executable_path="PATH/TO/CHROMEDRIVER")
        return driver


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuickView2App(root)
    root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class QuickView3App:
    def __init__(self, root):
        self.root = root
        self.root.title("QuickView3 Automation Tool")
        self.root.geometry("600x700")

        # Configurable attributes
        self.target_username = tk.StringVar()
        self.scrape_user_option = tk.StringVar()
        self.location_scrape = tk.StringVar()
        self.geolocation = tk.StringVar()
        self.scrape_comm_tag = tk.StringVar()
        self.scrape_comment_options = tk.StringVar()
        self.scrape_tag = tk.StringVar()
        self.scrape_tags_option = tk.StringVar()
        self.scrape_like_tag = tk.StringVar()
        self.enable_scrape_likes = tk.BooleanVar()
        self.number_to_scrape = tk.IntVar()

        self.spin_scraped_tags = tk.BooleanVar()
        self.top_posts = tk.BooleanVar()
        self.show_hide_browser = tk.BooleanVar()
        self.randomize_scrape_list = tk.BooleanVar()

        self.delay_time = tk.IntVar()
        self.stop_bot_at = tk.IntVar()
        self.master_delay = tk.IntVar()
        self.run_when_complete = tk.BooleanVar()

        self.random_wait_one = tk.IntVar()
        self.random_wait_two = tk.IntVar()
        self.wait_after = tk.IntVar()

        self.account_file = tk.StringVar()
        self.proxy_file = tk.StringVar()
        self.custom_settings_path = tk.StringVar()

        self.driver = None  # Selenium WebDriver instance

        # Build UI
        self.create_widgets()

    def create_widgets(self):
        """Create the UI components for QuickView3 settings."""
        # Section: Scraping settings
        tk.Label(self.root, text="Scraping Settings", font=("Arial", 14, "bold")).pack(pady=5)

        tk.Label(self.root, text="Target Username:").pack(anchor="w", padx=10)
        tk.Entry(self.root, textvariable=self.target_username).pack(fill="x", padx=10)

        tk.Label(self.root, text="Scrape User Option:").pack(anchor="w", padx=10)
        tk.Entry(self.root, textvariable=self.scrape_user_option).pack(fill="x", padx=10)

        tk.Label(self.root, text="Custom Location Scrape:").pack(anchor="w", padx=10)
        tk.Entry(self.root, textvariable=self.location_scrape).pack(fill="x", padx=10)

        tk.Label(self.root, text="GeoLocation:").pack(anchor="w", padx=10)
        tk.Entry(self.root, textvariable=self.geolocation).pack(fill="x", padx=10)

        # Add similar entries for other attributes...

        # Section: File Locations
        tk.Label(self.root, text="File Location Settings", font=("Arial", 14, "bold")).pack(pady=5)

        tk.Button(self.root, text="Select Account File", command=self.browse_account_file).pack(fill="x", padx=10)
        tk.Button(self.root, text="Select Proxy File", command=self.browse_proxy_file).pack(fill="x", padx=10)
        tk.Button(self.root, text="Select Custom Save/Load Path", command=self.browse_custom_settings_path).pack(
            fill="x", padx=10)

        # Start button
        tk.Button(self.root, text="Start Automation", command=self.start_automation, bg="green", fg="white").pack(
            pady=20)

    def browse_account_file(self):
        """Browse and select an account file."""
        filepath = filedialog.askopenfilename(title="Select Account File")
        self.account_file.set(filepath)

    def browse_proxy_file(self):
        """Browse and select a proxy file."""
        filepath = filedialog.askopenfilename(title="Select Proxy File")
        self.proxy_file.set(filepath)

    def browse_custom_settings_path(self):
        """Browse and select a custom settings path."""
        filepath = filedialog.askdirectory(title="Select Folder for Save/Load Settings")
        self.custom_settings_path.set(filepath)

    def initialize_driver(self):
        """Initialize the Selenium WebDriver."""
        try:
            service = Service("path/to/chromedriver")  # Update the path to your Chromedriver
            options = webdriver.ChromeOptions()
            if not self.show_hide_browser.get():
                options.add_argument("--headless")
            self.driver = webdriver.Chrome(service=service, options=options)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize WebDriver: {str(e)}")

    def start_automation(self):
        """Start the automation task with the current settings."""
        if not self.driver:
            self.initialize_driver()

        if not self.driver:
            return  # Exit if WebDriver initialization failed

        try:
            self.driver.get("https://example.com/login")  # Replace URL with actual target

            # Example: Perform login (dummy username/password for demonstration)
            username_field = self.driver.find_element(By.ID, "username")
            username_field.send_keys(self.target_username.get())

            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys("dummy_password")  # Use credentials securely, not hardcoded
            password_field.send_keys(Keys.RETURN)

            time.sleep(self.delay_time.get())  # Use set delay

            # Example: Scrape data
            self.scrape_data()

        except Exception as e:
            messagebox.showerror("Automation Error", f"An error occurred during automation: {str(e)}")
        finally:
            if self.driver:
                self.driver.quit()

    def scrape_data(self):
        """Perform the scraping tasks as per settings."""
        # Placeholder: Implement Selenium tasks based on your needs
        print("Scraping data with current settings...")
        time.sleep(self.master_delay.get())
        print("Scraping completed.")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuickView3App(root)
    root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class QuickView4App:
    def __init__(self, root):
        self.root = root
        self.root.title("QuickView4 - Target Module Settings")

        # Initialize Variables for User Settings
        self.num_follow = tk.StringVar(value="10")
        self.enable_following = tk.BooleanVar(value=False)
        self.num_like = tk.StringVar(value="10")
        self.enable_likes = tk.BooleanVar(value=False)
        self.num_comment = tk.StringVar(value="5")
        self.enable_commenting = tk.BooleanVar(value=False)
        self.delay_time = tk.IntVar(value=5)
        self.master_delay = tk.IntVar(value=2)
        self.run_when_complete = tk.BooleanVar(value=False)
        self.proxy_file = tk.StringVar()
        self.account_file = tk.StringVar()
        self.comment_file_list = tk.StringVar()
        self.loaded_list = tk.StringVar()

        # Initialize Selenium WebDriver
        self.driver = None

        # Create the UI Components
        self.create_widgets()

    def create_widgets(self):
        """Create GUI widgets for user interaction."""
        tk.Label(self.root, text="Number to Follow:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.num_follow).grid(row=0, column=1, padx=10, pady=5)

        tk.Checkbutton(self.root, text="Enable Following", variable=self.enable_following).grid(row=1, column=0,
                                                                                                padx=10, pady=5)

        tk.Label(self.root, text="Number to Like:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.num_like).grid(row=2, column=1, padx=10, pady=5)

        tk.Checkbutton(self.root, text="Enable Liking", variable=self.enable_likes).grid(row=3, column=0, padx=10,
                                                                                         pady=5)

        tk.Label(self.root, text="Number to Comment:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.num_comment).grid(row=4, column=1, padx=10, pady=5)

        tk.Checkbutton(self.root, text="Enable Commenting", variable=self.enable_commenting).grid(row=5, column=0,
                                                                                                  padx=10, pady=5)

        tk.Label(self.root, text="Delay Time (in secs):").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.delay_time).grid(row=6, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Master Delay:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.master_delay).grid(row=7, column=1, padx=10, pady=5)

        tk.Checkbutton(self.root, text="Run When Complete", variable=self.run_when_complete).grid(row=8, column=0,
                                                                                                  padx=10, pady=5)

        tk.Label(self.root, text="Proxy File Path:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.proxy_file, width=30).grid(row=9, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=lambda: self.browse_file(self.proxy_file)).grid(row=9, column=2,
                                                                                                    padx=10, pady=5)

        tk.Label(self.root, text="Account File Path:").grid(row=10, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.account_file, width=30).grid(row=10, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=lambda: self.browse_file(self.account_file)).grid(row=10, column=2,
                                                                                                      padx=10, pady=5)

        tk.Label(self.root, text="Comment File Path:").grid(row=11, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.comment_file_list, width=30).grid(row=11, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=lambda: self.browse_file(self.comment_file_list)).grid(row=11,
                                                                                                           column=2,
                                                                                                           padx=10,
                                                                                                           pady=5)

        tk.Button(self.root, text="Start Automation", command=self.start_automation).grid(row=12, column=0,
                                                                                          columnspan=3, pady=10)

    def browse_file(self, variable):
        """Browse a file and set its path."""
        file_path = filedialog.askopenfilename()
        variable.set(file_path)

    def initialize_driver(self):
        """Initialize Selenium WebDriver."""
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")

        if self.proxy_file.get():
            proxy = self.get_proxy_from_file(self.proxy_file.get())
            if proxy:
                options.add_argument(f"--proxy-server={proxy}")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def get_proxy_from_file(self, file_path):
        """Retrieve a proxy from the file."""
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                proxies = file.readlines()
                return proxies[0].strip() if proxies else None
        return None

    def start_automation(self):
        """Start the automation process with Selenium."""
        try:
            self.initialize_driver()

            # Example Automation: Login
            self.driver.get("https://example.com/login")
            time.sleep(self.delay_time.get())

            # Execute actions based on settings
            if self.enable_following.get():
                print(f"Following {self.num_follow.get()} users!")

            if self.enable_likes.get():
                print(f"Liking {self.num_like.get()} posts!")

            if self.enable_commenting.get():
                print(f"Commenting on {self.num_comment.get()} posts!")

            if self.run_when_complete.get():
                print("Automation completed. Taking further actions...")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            if self.driver:
                self.driver.quit()

    def run(self):
        """Run the Tkinter main loop."""
        self.root.mainloop()


def main():
    root = tk.Tk()
    app = QuickView4App(root)
    app.run()


if __name__ == "__main__":
    main()


