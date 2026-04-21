import os
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import configparser


class SaveCustomFolderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Save Custom Folder")
        self.custom_settings_path = "C:\\custom_settings_path"
        self.driver = None

        self.post_options = ''
        self.num_post_now = ''
        self.current_date_time = ''
        self.next_post_in = ''
        self.post_schedule = ''
        self.delay_time = ''
        self.stop_bot_at = ''

        # Path to ChromeDriver
        self.chrome_driver_path = './chromedriver'

        # UI Elements
        self.init_ui()

    def init_ui(self):
        tk.Label(self.master, text="Custom Settings Path:").grid(row=0, column=0, padx=10, pady=10)
        self.path_entry = tk.Entry(self.master, width=50)
        self.path_entry.grid(row=0, column=1, padx=10, pady=10)
        self.path_entry.insert(0, self.custom_settings_path)

        tk.Button(self.master, text="Save", command=self.save_custom_folder).grid(row=1, column=0, columnspan=2)

    def start_log_running(self):
        print("Log running started...")

    def save_to_ini_file(self):
        """Saves module data into an INI file."""
        ini_file_path = f"{self.custom_settings_path}\\Settings Config.ini"
        config = configparser.ConfigParser()

        # Clear existing settings file if exists
        if os.path.exists(ini_file_path):
            os.remove(ini_file_path)

        # Write configuration
        config['Post Module'] = {
            'Choose Post Option': self.post_options,
            'Number To Post Now': self.num_post_now,
            'Date Time Sec Designator': self.current_date_time,
            'Next Post Date Time': self.next_post_in,
            'Enter Your Post Schedule': self.post_schedule,
            'Set Delay Counter (Sec.)': self.delay_time,
            'Stop The Software At': self.stop_bot_at
        }
        # Add more sections as required similarly...

        with open(ini_file_path, 'w') as configfile:
            config.write(configfile)
        print(f"Settings saved to {ini_file_path}")

    def scrape_data_with_selenium(self):
        """Example Selenium automation."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            self.driver.get("https://example.com")
            # Example DOM manipulation
            text_area = self.driver.find_element(By.ID, "textarea_id")
            script = (
                "textarea.value += `{0} - SOFTWARE RUNNING - ALL MODULE SETTINGS SAVED: CUSTOM PATH "
                "C:\\\Settings Config.ini LOG RUNNING - INTERNALIZING COMPLETE \\n`; "
                "textarea.scrollTop = textarea.scrollHeight;"
            )
            script_with_time = script.format("Timestamp_here")
            self.driver.execute_script(script_with_time)
        finally:
            self.driver.quit()

    def save_custom_folder(self):
        self.custom_settings_path = self.path_entry.get()
        if not os.path.isdir(self.custom_settings_path):
            messagebox.showerror("Error", f"Path does not exist: {self.custom_settings_path}")
            return

        self.start_log_running()
        self.save_to_ini_file()

        # Run automated Selenium for confirmation or logging
        self.scrape_data_with_selenium()
        messagebox.showinfo("Success", "Custom folder settings saved successfully.")


if __name__ == '__main__':
    root = tk.Tk()
    app = SaveCustomFolderApp(root)
    root.mainloop()

import os
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import configparser


class CustomFolderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Load Custom Folder")

        # Paths and configurations
        self.custom_settings_path = "C:\\custom_settings_path"
        self.chrome_driver_path = "./chromedriver"
        self.driver = None

        # Data to be loaded from INI or used in operations
        self.module_settings = {}

        # Initialize the User Interface
        self.create_ui()

    def create_ui(self):
        """Initializes the Tkinter UI components."""
        tk.Label(self.root, text="Custom Settings Path:").grid(row=0, column=0, padx=10, pady=10)

        self.path_entry = tk.Entry(self.root, width=50)
        self.path_entry.grid(row=0, column=1, padx=10, pady=10)
        self.path_entry.insert(0, self.custom_settings_path)

        tk.Button(self.root, text="Load Folder", command=self.load_custom_folder).grid(row=1, column=0, columnspan=2,
                                                                                       pady=10)

    def start_log_running(self):
        """Placeholder function to simulate starting log."""
        print("Log running started...")

    def read_ini_file(self):
        """Reads the settings from an INI file at the custom path."""
        ini_file_path = os.path.join(self.custom_settings_path, "Settings Config.ini")
        if not os.path.exists(ini_file_path):
            raise FileNotFoundError(f"INI file not found at {ini_file_path}")

        config = configparser.ConfigParser()
        config.read(ini_file_path)

        # Parse data from all relevant sections into a dictionary
        for section in config.sections():
            for key in config[section]:
                self.module_settings[key] = config[section][key]

        print("Settings loaded:", self.module_settings)

    def scrape_and_log(self):
        """Performs Selenium automation to log the results."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run browser in headless mode
        service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            self.driver.get("https://example.com")

            # Assuming textarea exists in the webpage
            print("Interacting with text area for log...")
            text_area = self.driver.find_element(By.ID, "textarea_id")

            # Construct the log message
            log_message = (
                f"{self.module_settings.get('date_time_sec_designator', 'N/A')} - SOFTWARE RUNNING - "
                "CUSTOM MODULE SETTINGS LOADED SUCCESSFULLY - LOG RUNNING - INTERNALIZING COMPLETE"
            )
            log_script = (
                f"textarea_id.value += `{log_message}\\n`;"
                f"textarea.scrollTop = textarea.scrollHeight;"
            )

            self.driver.execute_script(log_script)

        except Exception as e:
            print("An error occurred during interaction with the web page:", e)
        finally:
            self.driver.quit()

    def load_custom_folder(self):
        """Main function to load and process the custom settings folder."""
        self.custom_settings_path = self.path_entry.get()

        if not os.path.isdir(self.custom_settings_path):
            messagebox.showerror("Error", f"Specified path does not exist: {self.custom_settings_path}")
            return

        try:
            self.start_log_running()
            self.read_ini_file()
            self.scrape_and_log()
            messagebox.showinfo("Success", "Custom folder loaded and actions completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CustomFolderApp(root)
    root.mainloop()
