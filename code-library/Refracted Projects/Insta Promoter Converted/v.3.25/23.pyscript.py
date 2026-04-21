import os
from tkinter import Tk, StringVar, Label, Listbox, Button, Scrollbar, END
from selenium import webdriver
from selenium.webdriver.common.by import By


class ProjectUploader:
    def __init__(self):
        self.upload_folders = []
        self.count_project_folders = []

    def get_special_folder_path(self, folder_type):
        """
        Returns the special folder path based on the folder type.
        """
        if folder_type == "Application":
            return os.path.expanduser("~\\Application")
        elif folder_type == "My Documents":
            return os.path.expanduser("~\\Documents\\Insta Promoter Data Folder")
        else:
            return None

    def load_data_folder_path(self, ipdf_path):
        """
        Loads data folder paths based on given conditions.
        """
        if not ipdf_path:  # Similar to checking #ipdf_path == $nothing
            base_path = os.path.join(self.get_special_folder_path("Application"), "projects")
        else:
            base_path = os.path.join(self.get_special_folder_path("My Documents"), "projects")

        folders = [
            os.path.join(base_path, folder) for folder in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, folder))
        ]
        return folders

    def get_upload_project_folder(self, ipdf_path=None):
        """
        Gets all upload project folder paths.
        """
        # Get total count of project folders
        self.count_project_folders = self.load_data_folder_path(ipdf_path)

        # Get all folders and their subdirectories
        self.upload_folders = self.load_data_folder_path(ipdf_path)

        # Remove files that are not upload folders (arbitrarily removing half based on your logic)
        for _ in range(len(self.count_project_folders) // 2):
            if self.upload_folders:
                self.upload_folders.pop(0)

        # Clear unnecessary data
        self.count_project_folders = []


class ApplicationUI:
    def __init__(self, root, project_uploader):
        self.root = root
        self.project_uploader = project_uploader

        self.project_folders_var = StringVar(value=[])

        self.setup_ui()

    def setup_ui(self):
        """
        Creates the Tkinter GUI components.
        """
        self.root.title("Project Uploader")

        # Label
        Label(self.root, text="Upload Project Folders:").pack(pady=5)

        # Listbox with scroll
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side="right", fill="y")

        self.folder_listbox = Listbox(self.root, listvariable=self.project_folders_var, yscrollcommand=scrollbar.set,
                                      width=50, height=15)
        self.folder_listbox.pack(pady=10)

        scrollbar.config(command=self.folder_listbox.yview)

        # Buttons
        Button(self.root, text="Load Projects", command=self.load_projects).pack(pady=5)

    def load_projects(self):
        """
        Loads projects using the ProjectUploader and updates the UI.
        """
        self.project_uploader.get_upload_project_folder()
        self.project_folders_var.set(self.project_uploader.upload_folders)


def run_application():
    # Selenium WebDriver setup (if needed for other tasks)
    driver = webdriver.Chrome()  # Update with your WebDriver if required
    driver.get("https://example.com")

    # Initialize project uploader
    project_uploader = ProjectUploader()

    # Initialize the Tkinter UI
    root = Tk()
    app = ApplicationUI(root, project_uploader)
    root.mainloop()

    # Close WebDriver when application is done
    driver.quit()


if __name__ == "__main__":
    run_application()

import os
from tkinter import Tk, StringVar, Label, Listbox, Button, Scrollbar, END
from selenium import webdriver
from selenium.webdriver.common.by import By


class ProjectUploader:
    """
    Handles logic for determining and loading project upload folders.
    """

    def __init__(self):
        self.upload_folders = []
        self.image_paths = []
        self.count_project_folders = []

    def get_special_folder_path(self, folder_type):
        """
        Returns the special folder path based on the folder type.
        """
        if folder_type == "Application":
            return os.path.expanduser("~\\Application")
        elif folder_type == "My Documents":
            return os.path.expanduser("~\\Documents\\Insta Promoter Data Folder")
        else:
            return None

    def load_data_folder_path(self, ipdf_path):
        """
        Loads data folder paths (based on conditions) from the base path.
        """
        if not ipdf_path:  # Similar to checking #ipdf_path == $nothing
            base_path = os.path.join(self.get_special_folder_path("Application"), "projects")
        else:
            base_path = os.path.join(self.get_special_folder_path("My Documents"), "projects")

        folders = [
            os.path.join(base_path, folder) for folder in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, folder))
        ]
        return folders

    def get_upload_project_folder(self, ipdf_path=None):
        """
        Loads all possible upload project folder paths after filtration.
        """
        # Get total count of project folders
        self.count_project_folders = self.load_data_folder_path(ipdf_path)

        # Get all folders, and filter based on specific conditions
        self.upload_folders = self.load_data_folder_path(ipdf_path)

        # Remove unnecessary folders arbitrarily (clear 50% as per logic)
        for _ in range(len(self.count_project_folders) // 2):
            if self.upload_folders:
                self.upload_folders.pop(0)

        # Clear count_project_folders for reuse
        self.count_project_folders = []

    def pull_upload_folder_image_paths(self, use_post_project_rotation):
        """
        Captures image paths from upload folders, based on rotation logic.
        """
        if use_post_project_rotation.upper() == "YES":
            # Reset image paths
            self.image_paths.clear()

            # Get folder images based on rotation
            upload_folder_path = self.upload_folders[0] if self.upload_folders else None
            if upload_folder_path:
                image_files = [
                    os.path.join(upload_folder_path, file) for file in os.listdir(upload_folder_path)
                    if file.endswith(('.png', '.jpg', '.jpeg'))  # Filter images
                ]
                self.image_paths.extend(image_files)


class ApplicationUI:
    """
    Represents the graphical user interface component of the application.
    """

    def __init__(self, root, project_uploader, selenium_driver):
        self.root = root
        self.project_uploader = project_uploader
        self.driver = selenium_driver

        self.project_folders_var = StringVar(value=[])
        self.image_paths_var = StringVar(value=[])

        self.setup_ui()

    def setup_ui(self):
        """
        Creates the Tkinter GUI layout.
        """
        self.root.title("Project Uploader")

        # Label: Project List Section
        Label(self.root, text="Upload Project Folders:").pack(pady=5)

        # Listbox: Project folders with a scrollbar
        project_scrollbar = Scrollbar(self.root)
        project_scrollbar.pack(side="right", fill="y")

        self.folder_listbox = Listbox(
            self.root, listvariable=self.project_folders_var, yscrollcommand=project_scrollbar.set,
            width=50, height=10
        )
        self.folder_listbox.pack(pady=10)
        project_scrollbar.config(command=self.folder_listbox.yview)

        # Button: Load project folders
        Button(self.root, text="Load Projects", command=self.load_projects).pack(pady=5)

        # Label: Image Paths Section
        Label(self.root, text="Image Paths from Upload Folders:").pack(pady=5)

        # Listbox: Uploaded folder images
        image_scrollbar = Scrollbar(self.root)
        image_scrollbar.pack(side="right", fill="y")

        self.images_listbox = Listbox(
            self.root, listvariable=self.image_paths_var, yscrollcommand=image_scrollbar.set,
            width=50, height=15
        )
        self.images_listbox.pack(pady=10)
        image_scrollbar.config(command=self.images_listbox.yview)

        # Button: Fetch Image Paths
        Button(self.root, text="Fetch Image Paths", command=self.fetch_image_paths).pack(pady=5)

        # Selenium section
        Button(self.root, text="Navigate with Selenium", command=self.navigate_with_selenium).pack(pady=5)

    def load_projects(self):
        """
        Loads project folders and updates the UI.
        """
        self.project_uploader.get_upload_project_folder()
        self.project_folders_var.set(self.project_uploader.upload_folders)

    def fetch_image_paths(self):
        """
        Fetches image paths from upload folders and displays them in the UI.
        """
        self.project_uploader.pull_upload_folder_image_paths(use_post_project_rotation="YES")
        self.image_paths_var.set(self.project_uploader.image_paths)

    def navigate_with_selenium(self):
        """
        Performs a Selenium task (e.g., navigating to a URL).
        """
        try:
            self.driver.get("https://example.com")
            print("Selenium successfully navigated to the site.")
        except Exception as e:
            print(f"An error occurred while navigating with Selenium: {e}")


def run_application():
    # Selenium WebDriver setup
    driver = webdriver.Chrome()  # Ensure the appropriate WebDriver is installed and configured.

    # Initialize project uploader
    project_uploader = ProjectUploader()

    # Initialize the Tkinter UI
    root = Tk()
    app = ApplicationUI(root, project_uploader, driver)
    root.mainloop()

    # Close WebDriver when the application is done
    driver.quit()


if __name__ == "__main__":
    run_application()

import os
from tkinter import Tk, Listbox, StringVar, Button, Label
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ProjectUploader:
    def __init__(self):
        self.upload_folders = []
        self.count_project_folders = 0

    def get_special_folder_path(self, folder_type: str):
        if folder_type == "Application":
            return os.path.expanduser("~")
        elif folder_type == "My Documents":
            return os.path.join(os.path.expanduser("~"), "Documents")
        return None

    def load_data_folder_path(self):
        """Loads the appropriate data folder path."""
        # Simulate loading data folder paths
        return self.get_special_folder_path("My Documents") + "\\Insta Promoter Data Folder\\projects"

    def get_project_caption_files(self):
        """Creates full caption file paths."""
        caption_paths = []

        # Load the data folder path
        ipdf_path = self.load_data_folder_path()

        # Based on presence of ipdf_path, determine caption file locations
        if ipdf_path is None or ipdf_path == "":
            caption_paths.extend(
                self._get_folders(self.get_special_folder_path("Application") + "\\projects")
            )
        else:
            caption_paths.extend(
                self._get_folders(
                    self.get_special_folder_path("My Documents") + "\\Insta Promoter Data Folder\\projects")
            )

        # Append "\Captions.txt" suffix to the paths
        caption_paths = [os.path.join(path, "Captions.txt") for path in caption_paths]

        # Set the position to the start of the list (like resetting an iterator)
        self.count_project_folders = len(caption_paths)

        return caption_paths

    def _get_folders(self, base_folder: str):
        """Helper method to get subfolders from a given base folder."""
        if not os.path.exists(base_folder):
            return []
        return [os.path.join(base_folder, d) for d in os.listdir(base_folder) if
                os.path.isdir(os.path.join(base_folder, d))]


class ApplicationUI:
    def __init__(self, root):
        # Tkinter UI elements
        self.root = root
        self.project_uploader = ProjectUploader()
        self.project_folders_var = StringVar(value=[])
        self.folder_listbox = None

        self.driver = None  # Selenium WebDriver instance

        # Load and setup UI
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Project Caption File Manager")

        Label(self.root, text="Project Folders").pack()

        # Listbox to display project folders
        self.folder_listbox = Listbox(self.root, listvariable=self.project_folders_var, width=50, height=15)
        self.folder_listbox.pack()

        # Load projects button
        Button(self.root, text="Load Projects", command=self.load_projects).pack()

        # Additional controls for Selenium navigation
        Button(self.root, text="Start Selenium Task", command=self.navigate_with_selenium).pack()

    def load_projects(self):
        """Load project folders into the listbox."""
        caption_files = self.project_uploader.get_project_caption_files()
        self.project_folders_var.set(caption_files)

    def navigate_with_selenium(self):
        """Perform browser automation tasks using Selenium."""
        if not self.driver:
            # Initialize WebDriver if not already done
            self.driver = webdriver.Chrome()

        # Example: Navigate to a webpage and interact
        self.driver.get("https://example.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Python Selenium" + Keys.RETURN)


if __name__ == "__main__":
    root = Tk()
    app_ui = ApplicationUI(root)
    root.mainloop()

import os
from tkinter import Tk, Listbox, StringVar, Button, filedialog, END, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions


class CreatesCaptionListFromPath:
    def __init__(self):
        self.image_captions = []

    def clear_captions(self):
        """Clears the existing caption list."""
        self.image_captions.clear()

    def create_from_paths(self, caption_paths, caption_paths_pos):
        """
        Creates a caption list from the provided paths.

        Args:
            caption_paths: List of paths where captions are stored.
            caption_paths_pos: Integer position to retrieve specific caption paths.
        Returns:
            None
        """
        try:
            self.clear_captions()
            if caption_paths and len(caption_paths) > caption_paths_pos:
                caption_path = caption_paths[caption_paths_pos]

                # Add captions from the file to the list
                if os.path.exists(caption_path):
                    with open(caption_path, "r", encoding="utf-8") as file:
                        self.image_captions.extend([line.strip() for line in file.readlines() if line.strip()])
                else:
                    print(f"Caption path {caption_path} does not exist.")

            # Remove duplicates and trim excess spaces
            self.image_captions = list(dict.fromkeys(self.image_captions))  # Deduplicate
            self.image_captions = [caption.strip() for caption in self.image_captions]

        except Exception as e:
            print(f"An error occurred while creating captions from paths: {e}")

    def get_captions(self):
        """Returns the current list of captions."""
        return self.image_captions


class ApplicationUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caption Manager")
        self.root.geometry("500x400")

        self.project_uploader = CreatesCaptionListFromPath()

        # UI variables
        self.caption_paths_var = StringVar()
        self.captions_listbox = None
        self.setup_ui()

    def setup_ui(self):
        """Sets up the graphical user interface."""
        # Label and entry for caption path
        Button(self.root, text="Load Caption Path", command=self.load_caption_path).pack(pady=10)

        # Listbox to display captions
        self.captions_listbox = Listbox(self.root, width=50, height=15)
        self.captions_listbox.pack(pady=10)

        # Load and Process buttons
        Button(self.root, text="Load Captions", command=self.display_captions).pack(pady=5)
        Button(self.root, text="Clear Captions", command=self.clear_captions).pack(pady=5)

    def load_caption_path(self):
        """Opens a dialog to select caption paths."""
        file_path = filedialog.askopenfilename(title="Select Caption File",
                                               filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if file_path:
            self.caption_paths_var.set(file_path)

    def display_captions(self):
        """Displays the loaded captions in the listbox."""
        caption_paths = [self.caption_paths_var.get()]
        position = 0  # Assume 0 for first position

        self.project_uploader.create_from_paths(caption_paths, position)
        self.captions_listbox.delete(0, END)
        for caption in self.project_uploader.get_captions():
            self.captions_listbox.insert(END, caption)

    def clear_captions(self):
        """Clears captions from the UI and backend."""
        self.project_uploader.clear_captions()
        self.captions_listbox.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    app = ApplicationUI(root)
    root.mainloop()

import os
import tkinter as tk
from tkinter import messagebox, Listbox, Button


class RemoveUsedImagesApp:
    def __init__(self, root):
        """
        Initializes the application UI for removing used images.
        """
        self.root = root
        self.root.title("Remove Used Images")

        # List to hold used image paths
        self.used_images = []

        # Tkinter UI Elements
        self.listbox = Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        self.remove_button = Button(root, text="Remove Selected Image", command=self.remove_selected_image)
        self.remove_button.pack(pady=5)

        self.clear_button = Button(root, text="Clear All Used Images", command=self.remove_all_images)
        self.clear_button.pack(pady=5)

    def populate_images(self, image_paths):
        """
        Populate the listbox with image paths.
        :param image_paths: List of paths to used images.
        """
        self.used_images = image_paths
        self.listbox.delete(0, tk.END)
        for img_path in image_paths:
            self.listbox.insert(tk.END, img_path)

    def remove_selected_image(self):
        """
        Removes the selected image from both the list and file system.
        """
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select an image.")
            return

        image_path = self.used_images[selected_index[0]]
        try:
            # Delete the selected image file
            if os.path.exists(image_path):
                os.remove(image_path)
                self.listbox.delete(selected_index)
                self.used_images.pop(selected_index[0])
                messagebox.showinfo("Success", f"Image removed: {image_path}")
            else:
                messagebox.showerror("Error", f"File not found: {image_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove image: {e}")

    def remove_all_images(self):
        """
        Removes all images listed in the used_images list and clears the listbox.
        """
        if not self.used_images:
            messagebox.showinfo("Info", "No images to remove.")
            return

        try:
            for image_path in self.used_images:
                if os.path.exists(image_path):
                    os.remove(image_path)

            self.listbox.delete(0, tk.END)
            self.used_images.clear()
            messagebox.showinfo("Success", "All images removed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove images: {e}")


# Example usage assuming Selenium or external logic obtains image paths dynamically
def selenium_simulate_used_images():
    """
    Simulation of fetching used images (Selenium or any other logic).
    This can be replaced with integration to fetch actual paths dynamically.
    """
    return [
        "/path/to/used/image1.jpg",
        "/path/to/used/image2.jpg",
        "/path/to/used/image3.jpg"
    ]


if __name__ == "__main__":
    root = tk.Tk()
    app = RemoveUsedImagesApp(root)

    # Simulated Selenium logic populates the image paths
    simulated_image_paths = selenium_simulate_used_images()
    app.populate_images(simulated_image_paths)

    root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os


class ProjectUploader:
    def __init__(self):
        self.upload_folders = []
        self.project_settings_paths = []

    def get_special_folder_path(self, folder_type: str) -> str:
        """Returns the path of a special folder."""
        if folder_type == "Application":
            return os.path.expanduser("~/AppData/Local")
        elif folder_type == "My Documents":
            return os.path.expanduser("~/Documents")
        else:
            return ""

    def load_data_folder_path(self):
        """Loads different folder paths."""
        data_folder_path = self.get_special_folder_path("My Documents") + "/Insta Promoter Data Folder/projects"
        if os.path.exists(data_folder_path):
            self.project_settings_paths = [
                os.path.join(data_folder_path, folder, "Post Module.ini")
                for folder in os.listdir(data_folder_path)
            ]
        else:
            alt_path = self.get_special_folder_path("Application") + "/projects"
            self.project_settings_paths = [
                os.path.join(alt_path, folder, "Post Module.ini")
                for folder in os.listdir(alt_path)
            ]

    def get_upload_project_folder(self):
        """Fetches available project folders for upload."""
        self.upload_folders = [
            os.path.dirname(path) for path in self.project_settings_paths if os.path.isfile(path)
        ]
        return self.upload_folders


class ApplicationUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Settings Manager")
        self.project_uploader = ProjectUploader()
        self.project_folders_var = tk.StringVar()
        self.folder_listbox = None
        self.driver = None
        self.setup_ui()

    def setup_ui(self):
        """Sets up the UI using Tkinter widgets."""
        frame = tk.Frame(self.root)
        frame.pack(pady=10, padx=10)

        folder_label = ttk.Label(frame, text="Project Folders:")
        folder_label.grid(row=0, column=0, sticky="w", pady=5)

        scrollbar = ttk.Scrollbar(frame, orient="vertical")
        self.folder_listbox = tk.Listbox(
            frame, listvariable=self.project_folders_var, height=10, yscrollcommand=scrollbar.set
        )
        self.folder_listbox.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        scrollbar.config(command=self.folder_listbox.yview)

        scrollbar.grid(row=1, column=1, sticky="ns")

        # Control Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5, padx=5)

        load_button = ttk.Button(button_frame, text="Load Projects", command=self.load_projects)
        load_button.grid(row=0, column=0, padx=5)

        selenium_button = ttk.Button(button_frame, text="Open Browser", command=self.navigate_with_selenium)
        selenium_button.grid(row=0, column=1, padx=5)

        exit_button = ttk.Button(button_frame, text="Exit", command=self.root.quit)
        exit_button.grid(row=0, column=2, padx=5)

    def load_projects(self):
        """Loads project folders into the listbox."""
        try:
            self.project_uploader.load_data_folder_path()
            folders = self.project_uploader.get_upload_project_folder()
            self.folder_listbox.delete(0, tk.END)
            for folder in folders:
                self.folder_listbox.insert(tk.END, folder)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load projects: {str(e)}")

    def navigate_with_selenium(self):
        """Opens the Chrome browser and navigates to a test URL."""
        try:
            options = Options()
            options.add_argument("--headless")  # Runs the browser in headless mode
            service = Service("chromedriver")  # Replace with the path to your ChromeDriver

            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.get("https://example.com")
            title = self.driver.title
            messagebox.showinfo("Browser Automation", f"Opened Browser with Title: {title}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open browser: {str(e)}")
        finally:
            if self.driver:
                self.driver.quit()


if __name__ == "__main__":
    # Create the application window
    root = tk.Tk()
    app = ApplicationUI(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Class to handle project settings automation
class ProjectAutomation:
    def __init__(self):
        # Initialize paths and settings attributes
        self.project_settings_paths = []
        self.active_project_settings_path = ""
        self.driver = None

    def initialize_selenium_driver(self):
        """Initialize Selenium WebDriver with Chrome options."""
        options = Options()
        options.add_argument("--headless")  # Run in headless mode (no GUI)
        service = Service("path_to_chromedriver")  # Replace with actual chromedriver path

        self.driver = webdriver.Chrome(service=service, options=options)
        print("Selenium driver initialized.")

    def auto_load_project_settings(self):
        """Emulates loading project settings based on specific logic."""
        if not self.project_settings_paths:
            print("No project settings paths available.")
            return

        # Set active project settings from the list
        self.active_project_settings_path = self.project_settings_paths[0]
        print(f"Active project settings path: {self.active_project_settings_path}")
        self.auto_load_post_module()

    def auto_load_post_module(self):
        """Simulates post-modules or navigational automation tasks in Selenium."""
        if not self.driver:
            print("Driver not initialized.")
            return

        print("Navigating to project URL in Selenium...")
        self.driver.get("https://example.com")  # Replace with actual URL

        # Example of locating an element and interacting with it
        try:
            element = self.driver.find_element(By.ID, "example-id")
            element.click()
            print("Clicked element with ID 'example-id'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def stop_driver(self):
        """Stops the Selenium WebDriver if running."""
        if self.driver:
            self.driver.quit()
            print("Selenium driver stopped.")


# Tkinter-based UI application
class ApplicationUI(tk.Tk):
    def __init__(self, project_automation):
        super().__init__()

        # Application Setup
        self.project_automation = project_automation
        self.title("Project Automation UI")
        self.geometry("500x300")

        # UI Elements
        self.project_list_var = tk.StringVar(value=[])
        self.project_listbox = tk.Listbox(self, listvariable=self.project_list_var, height=10)
        self.project_listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.load_projects_button = ttk.Button(self, text="Load Projects", command=self.load_projects)
        self.load_projects_button.grid(row=1, column=0, pady=10)

        self.start_automation_button = ttk.Button(self, text="Start Automation", command=self.start_automation)
        self.start_automation_button.grid(row=2, column=0, pady=(0, 10))

        self.quit_button = ttk.Button(self, text="Quit", command=self.quit_application)
        self.quit_button.grid(row=3, column=0, pady=(0, 10))

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def load_projects(self):
        """Loads available project paths into the listbox."""
        self.project_automation.project_settings_paths = [
            "Project A Settings",
            "Project B Settings",
            "Project C Settings"
        ]

        # Update listbox
        self.project_list_var.set(self.project_automation.project_settings_paths)
        messagebox.showinfo("Info", "Projects loaded successfully!")

    def start_automation(self):
        """Starts the automation process for the selected project."""
        try:
            selected_index = self.project_listbox.curselection()
            if not selected_index:
                messagebox.showwarning("Warning", "Please select a project first!")
                return

            # Get selected project path
            selected_project = self.project_listbox.get(selected_index[0])
            self.project_automation.active_project_settings_path = selected_project
            print(f"Selected Project Path: {selected_project}")

            # Initialize Selenium driver if not already done
            if not self.project_automation.driver:
                self.project_automation.initialize_selenium_driver()

            # Run automation
            self.project_automation.auto_load_project_settings()
            messagebox.showinfo("Info", "Automation completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def quit_application(self):
        """Handles application quit action."""
        if messagebox.askokcancel("Quit", "Do you want to exit?"):
            self.destroy()
            self.project_automation.stop_driver()


# Main method to run the application
if __name__ == "__main__":
    project_automation = ProjectAutomation()
    app = ApplicationUI(project_automation)
    app.mainloop()
    
