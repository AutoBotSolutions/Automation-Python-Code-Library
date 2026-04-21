import json  # For handling JSON data, e.g., parsing proxy response in `verify_proxy`
import os  # Interacting with the file system, e.g., reading environment variables
import pickle  # For saving/loading cookie data to/from files
import logging  # For logging messages to a file or console
from selenium import webdriver  # Main module for Selenium WebDriver automation
from selenium.webdriver.chrome.options import Options  # To customize Chrome browser options
from selenium.webdriver.chrome.service import Service  # Used to manage ChromeDriver service
from os_get_installed_useragent import get_chrome_user_agent  # Fetch a dynamic user-agent string for the browser

# -------------------------------------------------
# user must have chrome installed on the computer
# -------------------------------------------------

# -------------------------
# Logging setup
# -------------------------
logging.basicConfig(
    level=logging.DEBUG,  # Sets the logging level to DEBUG for detailed logging
    format="%(asctime)s - %(levelname)s - %(message)s",  # Specifies the log message format
    handlers=[
        logging.FileHandler("application.log"),  # Configures logging to a file
        logging.StreamHandler()  # Configures logging to the console
    ]
)

# -------------------------
# Global variables
# -------------------------
COOKIE_FILE_PATH = '/home/tompots/PycharmProjects/InstaPromoterCore/data/session_cookies.pkl'  # File path to save cookies
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH",
                              "/usr/bin/chromedriver")  # Fetches ChromeDriver path from env or sets default
PROXY_FILE_PATH = "/home/tompots/PycharmProjects/InstaPromoterCore/data/Proxies.csv"  # File path for the proxy list
driver_instance = None  # Holds the global WebDriver instance
global_proxy_list = []  # Stores the list of proxies
global_proxy_row = 0  # Index of the current proxy in the proxy list
global_set_proxy = None  # Currently active proxy details


# -------------------------
# Function to save cookies
# -------------------------
def save_cookies(driver):
    """Save cookies from the WebDriver instance to a file."""
    try:
        if driver is None:
            logging.error("Driver is not initialized. Cannot save cookies.")
            return

        with open(COOKIE_FILE_PATH, 'wb') as file:
            pickle.dump(driver.get_cookies(), file)
        logging.info(f"Cookies saved to {COOKIE_FILE_PATH}.")
    except Exception as e:
        logging.error(f"Error while saving cookies: {e}")


# --------------------------
# Function to load cookies
# --------------------------
def load_cookies(driver):
    """Load cookies into the WebDriver instance from a file."""
    try:
        if not os.path.exists(COOKIE_FILE_PATH):
            logging.warning(f"Cookie file {COOKIE_FILE_PATH} does not exist.")
            return

        with open(COOKIE_FILE_PATH, 'rb') as file:
            cookies = pickle.load(file)

        if cookies:
            for cookie in cookies:
                try:
                    driver.add_cookie(cookie)
                except Exception as e:
                    logging.warning(f"Failed to add cookie: {cookie}, Error: {e}")
            logging.info(f"Cookies loaded from {COOKIE_FILE_PATH}.")
        else:
            logging.warning(f"Cookie file {COOKIE_FILE_PATH} is empty.")
    except Exception as e:
        logging.error(f"Error while loading cookies: {e}")


# --------------------------
# Function to verify proxy
# --------------------------
def verify_proxy(driver_instance, proxy_ip):
    """Verify if the proxy is working by checking the public IP."""
    try:
        if driver_instance is None:
            logging.error("Driver is not initialized. Cannot verify proxy.")
            return False

        driver_instance.get("https://httpbin.org/ip")
        response = json.loads(driver_instance.find_element("tag name", "body").text)
        logging.debug(f"Proxy verification response: {response}")
        proxy_verified = response.get("origin", "").startswith(proxy_ip)
        logging.debug(f"Proxy {proxy_ip} verification result: {proxy_verified}")
        return proxy_verified
    except Exception as e:
        logging.error(f"Error verifying proxy for {proxy_ip}: {e}")
        return False


# --------------------------
# Function: Load Proxies
# --------------------------
def load_proxies(file_path):
    """Helper function to load proxies from file."""
    global global_proxy_list

    try:
        with open(file_path, "r") as file:
            global_proxy_list = [line.strip().split(":") for line in file.readlines()]
            if not global_proxy_list:
                logging.warning("Proxy list is empty.")
                return True
            logging.info(f"Loaded proxies: {global_proxy_list}")
        return True
    except Exception as e:
        logging.error(f"Error loading proxies: {e}")
        return False


# --------------------------
# Function: Launch Driver
# --------------------------
def lanuch_initialize_driver():
    """Initialize the Selenium WebDriver with proxy, cookies, and extensions."""
    global global_proxy_list, global_set_proxy, global_proxy_row, driver_instance

    if driver_instance:  # Reuse driver if already initialized
        logging.info("Reusing existing WebDriver instance.")
        return driver_instance

    # Verify CHROMEDRIVER_PATH availability
    if not os.path.isfile(CHROMEDRIVER_PATH):
        logging.critical(f"ChromiumDriver not found at {CHROMEDRIVER_PATH}.")
        return None

    # Load proxies if not already loaded
    if not global_proxy_list:
        if not load_proxies(PROXY_FILE_PATH):  # Attempt to load proxies
            logging.error("Error loading the proxy file. Continuing without proxies.")

    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={get_chrome_user_agent()}")  # Set custom user agent

    # Load extension
    extension_path = "/home/tompots/PycharmProjects/InstaPromoterCore/data/Automation Security"
    chrome_options.add_argument(f"--load-extension={extension_path}")

    try:
        # Check if the proxy file is blank, non-existent, or no valid proxies loaded
        if not os.path.exists(PROXY_FILE_PATH) or os.stat(PROXY_FILE_PATH).st_size == 0 or not global_proxy_list:
            logging.warning("Proxy file is blank, doesn't exist, or no proxies loaded. Continuing without proxy.")

        else:
            while global_proxy_row < len(global_proxy_list):  # Iterate over proxies if available
                proxy = global_proxy_list[global_proxy_row]
                if len(proxy) < 2:
                    logging.error(f"Invalid proxy format: {proxy}")
                    global_proxy_row += 1
                    continue

                proxy_ip, proxy_port = proxy[0], proxy[1]
                proxy_credentials = ":".join(proxy[2:]) if len(proxy) == 4 else None

                # Set up proxy
                chrome_options.add_argument(f"--proxy-server=http://{proxy_ip}:{proxy_port}")
                logging.info(f"Attempting to use proxy: {proxy_ip}:{proxy_port}")

                try:
                    # Initialize WebDriver with the new proxy
                    service = Service(CHROMEDRIVER_PATH)
                    driver = webdriver.Chrome(service=service, options=chrome_options)
                    driver.set_page_load_timeout(20)  # Increased timeout to handle slow proxies

                    # Verify proxy functionality
                    if verify_proxy(driver, proxy_ip):
                        global_set_proxy = {"ip": proxy_ip, "port": proxy_port}
                        logging.info(f"Proxy verified and set: {proxy_ip}")
                        driver.get("https://instagram.com")
                        load_cookies(driver)
                        driver.refresh()
                        save_cookies(driver)
                        driver_instance = driver
                        return driver
                    else:
                        logging.warning(f"Proxy {proxy_ip} failed. Trying the next proxy.")
                        driver.quit()
                        global_proxy_row += 1

                except Exception as proxy_error:
                    logging.error(f"Error with proxy {proxy_ip}:{proxy_port}: {proxy_error}")
                    global_proxy_row += 1

            logging.error("No valid proxies available. Proceeding without proxy.")

        # Initialize WebDriver without any proxy
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(10)
        logging.info("Initialized WebDriver without proxy.")

        driver.get("https://instagram.com")
        load_cookies(driver)
        driver.refresh()
        save_cookies(driver)
        driver_instance = driver
        return driver

    except Exception as e:
        logging.error(f"Unexpected error in driver initialization: {e}")
        return None


# --------------------------
# Main Execution
# --------------------------
if __name__ == "__main__":
    try:
        logging.info("Starting driver initialization.")
        driver = lanuch_initialize_driver()
        if driver:
            logging.info("Driver initialized successfully.")
        else:
            logging.error("WebDriver initialization failed.")
    except Exception as e:
        logging.error(f"Unexpected error during script execution: {e}")