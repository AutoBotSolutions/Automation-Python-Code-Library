import logging
import os
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log message format
    handlers=[
        logging.FileHandler("application.log"),  # Log to a file
        logging.StreamHandler()  # Also log to the console
    ]
)


# Function to save cookies to a file
def save_cookies(driver, file_path):
    """Save cookies from the WebDriver instance to a file."""
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(driver.get_cookies(), file)
        logging.info(f"Cookies saved to {file_path}.")
    except Exception as e:
        logging.error(f"Error saving cookies to {file_path}: {e}")


# Function to load cookies from a file
def load_cookies(driver, file_path):
    """Load cookies into the WebDriver instance from a file."""
    try:
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    driver.add_cookie(cookie)
            logging.info(f"Cookies loaded from {file_path}.")
        else:
            logging.warning(f"Cookie file {file_path} does not exist.")
    except Exception as e:
        logging.error(f"Error loading cookies from {file_path}: {e}")


def lanuch_initialize_driver():
    global global_proxy_list, global_set_proxy, global_proxy_row
    logging.info("Starting the initialization of the Selenium WebDriver for Chromium.")
    """Initialize and return the Selenium WebDriver for Chromium."""

    # Set up Chromium options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    chrome_options.add_argument("--disable-extensions")  # Disable browser extensions
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL warnings
    chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled")  # Prevent detection as an automated tool
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Exclude automation switch
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems in containers
    chrome_options.add_argument("--no-sandbox")  # Bypass sandbox for better security isolation in headless mode
    chrome_options.add_argument("--disable-infobars")  # Disable information bars
    chrome_options.add_experimental_option("useAutomationExtension", False)  # Prevent detection as an automated tool
    chrome_options.add_argument("--disable-logging")  # Disable logging for privacy
    chrome_options.add_argument("--disable-notifications")  # Disable website notifications
    chrome_options.add_argument("--disable-gpu")  # Disable GPU usage to avoid unnecessary resource usage
    chrome_options.add_argument("--mute-audio")  # Mute audio to enhance privacy
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")  # Set custom user agent

    # Static path to the Chromium WebDriver binary (adjust this path based on your environment)
    driver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")

    # Ensure the path to the Chromium WebDriver exists
    if not os.path.isfile(driver_path):
        logging.error(f"ChromiumDriver is not found at the path: {driver_path}.")
        logging.info("Please download it from https://chromedriver.chromium.org/ and set the path.")
        raise FileNotFoundError(f"ChromiumDriver is not found at the path: {driver_path}. "
                                f"Please download it from https://chromedriver.chromium.org/ and set the path.")
    logging.info("ChromiumDriver path exists. Proceeding with initialization.")

    # Debug prints for driver path and options
    logging.debug(f"ChromiumDriver path: {driver_path}")

    # Initialize global proxy list
    global_proxy_list = []

    try:
        logging.debug("Starting proxy script execution.")  # Log script start
        # Reset and load proxies from file
        global_proxy_list.clear()  # Clear existing proxy list

        # Path to the application folder
        app_folder = os.path.join(os.getcwd(), "application_folder")
        # Create the folder if it doesn't exist
        os.makedirs(app_folder, exist_ok=True)
        proxy_file_path = "/home/tompots/PythonCodeLibrary/Proxies.csv"  # Specify proxy file path

        with open(proxy_file_path, "r") as proxy_file:  # Open proxy file for reading
            lines = proxy_file.readlines()
            for line in lines:
                logging.debug(f"Reading line: {line.strip()}")
                global_proxy_list.append(line.strip().split(":"))

        global_proxy_row = 0  # Initialize index of proxy list to 0

        # Process proxies
        while global_proxy_row < len(global_proxy_list):  # Iterate through each proxy in the list
            proxy_row = global_proxy_list[global_proxy_row]  # Get current proxy row
            logging.debug(f"Processing proxy_row: {proxy_row}")  # Log the current proxy row
            if len(proxy_row) == 4:  # Check if proxy has 4 parts (IP, port, username, password)
                global_set_proxy = f"{proxy_row[0]}:{proxy_row[1]}"  # IP and port
                proxy_auth = f"{proxy_row[2]}:{proxy_row[3]}"  # Username and password
                chrome_options.add_argument(f"--proxy-server=http://{global_set_proxy}")
                chrome_options.add_argument(f"--proxy-auth={proxy_auth}")
                logging.debug(f"Set proxy with auth: {global_set_proxy}, {proxy_auth}")
            elif len(proxy_row) == 2:  # Check if proxy has 2 parts (IP, port)
                global_set_proxy = f"{proxy_row[0]}:{proxy_row[1]}"  # IP and port
                chrome_options.add_argument(f"--proxy-server=http://{global_set_proxy}")
                logging.debug(f"Set proxy: {global_set_proxy}")
            else:
                logging.warning(f"Skipping invalid proxy format: {proxy_row}")  # Log invalid proxy format
                global_proxy_row += 1  # Move to the next proxy
                continue  # Skip to the next iteration

            try:
                # Use Selenium with the set proxy
                service = Service(driver_path)
                driver = webdriver.Chrome(service=service, options=chrome_options)
                driver.get("https://whatismyipaddress.com/")
                logging.info(f"Proxy {global_set_proxy} tested successfully.")
            except Exception as e:
                logging.error(f"Error testing proxy: {proxy_row}, Error: {e}")
            finally:
                try:
                    driver.quit()
                except Exception as quit_error:
                    logging.error(f"Error quitting WebDriver: {quit_error}")

            global_proxy_row += 1  # Move to the next proxy
        logging.debug("Proxy script execution completed.")
    except FileNotFoundError:
        logging.error(f"Proxy file not found at path: {proxy_file_path}")
    except Exception as e:
        logging.error(f"Unexpected error during execution: {e}")

    # Initialize WebDriver with the pre-downloaded binary
    try:
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        logging.info("WebDriver successfully initialized.")
        logging.debug("Browser capabilities:")
        logging.debug(driver.capabilities)

        # NEW: Cookie handling logic
        cookie_file_path = "session_cookies.pkl"  # Define a path for storing cookies

        # Example: Save cookies after visiting the site
        driver.get("https://example.com")  # Replace this with your target URL

        # Attempt to load cookies from the earlier session
        load_cookies(driver, cookie_file_path)

        # Refresh the page to apply cookies
        driver.refresh()

        # Save cookies from the session
        save_cookies(driver, cookie_file_path)

        logging.info("Cookies loaded, applied, and saved successfully.")

    except Exception as init_error:
        logging.error(f"Error during WebDriver initialization: {init_error}")
        raise

    return driver


if __name__ == "__main__":
    driver = lanuch_initialize_driver()