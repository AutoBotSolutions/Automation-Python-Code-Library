import json  # For handling JSON data, e.g., parsing proxy response in `verify_proxy`
import os  # Interacting with the file system, e.g., reading environment variables
import pickle  # For saving/loading cookie data to/from files
import logging  # For logging messages to a file or console
import requests  # For direct proxy validation
from selenium import webdriver  # Main module for Selenium WebDriver automation
from selenium.webdriver.chrome.options import Options  # To customize Chrome browser options
from selenium.webdriver.chrome.service import Service  # Used to manage ChromeDriver service
from os_get_installed_useragent import get_chrome_user_agent  # Fetch a dynamic user-agent string for the browser

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
COOKIE_FILE_PATH = '/home/tompots/PycharmProjects/InstaPromoterCore/data/session_cookies.pkl'
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
PROXY_FILE_PATH = "/home/tompots/PycharmProjects/InstaPromoterCore/data/Proxies.csv"
driver_instance = None
global_proxy_list = []
global_proxy_row = 0
global_set_proxy = None
proxy_test_urls = [
    "https://httpbin.org/ip",
    "https://api.myip.com/",
    "https://ifconfig.me/ip"
]


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
                    # Adjust the domain of the cookie if required
                    if "domain" in cookie and not driver.current_url.startswith("https://" + cookie["domain"]):
                        cookie["domain"] = driver.current_url.split("//")[1].split("/")[0]

                    cookie.pop('sameSite', None)  # Remove sameSite attribute if present
                    driver.add_cookie(cookie)
                except Exception as e:
                    logging.warning(f"Failed to add cookie: {cookie}, Error: {e}")
            logging.info(f"Cookies loaded from {COOKIE_FILE_PATH}.")
        else:
            logging.warning(f"Cookie file {COOKIE_FILE_PATH} is empty.")
    except Exception as e:
        logging.error(f"Error while loading cookies: {e}")


# --------------------------
# Function to verify proxy via browser
# --------------------------
def verify_proxy(driver_instance, proxy_ip):
    """Verify if the proxy is working by checking the public IP via multiple endpoints."""
    try:
        if driver_instance is None:
            logging.error("Driver is not initialized. Cannot verify proxy.")
            return False

        for test_url in proxy_test_urls:
            try:
                driver_instance.get(test_url)
                response_text = driver_instance.find_element("tag name", "body").text
                logging.debug(f"Response from {test_url}: {response_text}")
                response = json.loads(response_text)
                if response.get("origin", "").startswith(proxy_ip):
                    return True
            except Exception as e:
                logging.warning(f"Proxy verification failed with {test_url}: {e}")
        return False
    except Exception as e:
        logging.error(f"Error verifying proxy: {e}")
        return False


# --------------------------
# Function to verify proxy using requests
# --------------------------
def test_proxy_connectivity(proxy_ip, proxy_port):
    """Test if the proxy is functional using HTTP requests."""
    proxy_url = f"http://{proxy_ip}:{proxy_port}"
    proxies = {"http": proxy_url, "https": proxy_url}
    try:
        response = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=10)
        logging.debug(f"Proxy {proxy_ip}:{proxy_port} response: {response.text}")
        return response.status_code == 200
    except Exception as e:
        logging.warning(f"Direct proxy connectivity failed for {proxy_ip}:{proxy_port}. Error: {e}")
        return False


# --------------------------
# Function to load proxies from a file
# --------------------------
def load_proxies(file_path):
    """Load proxies into a list from a specified file."""
    global global_proxy_list

    try:
        with open(file_path, "r") as file:
            global_proxy_list = [line.strip().split(":") for line in file.readlines() if line.strip()]
            if not global_proxy_list:
                logging.warning("Proxy list is empty.")
        return True
    except Exception as e:
        logging.error(f"Error loading proxies: {e}")
        return False


# --------------------------
# Function: Launch Driver
# --------------------------
def lanuch_initialize_driver():
    """Initialize Chrome WebDriver with optional proxy."""
    global global_proxy_list, global_set_proxy, global_proxy_row, driver_instance

    if driver_instance:
        logging.info("Reusing existing WebDriver instance.")
        return driver_instance

    if not os.path.isfile(CHROMEDRIVER_PATH):
        logging.error(f"ChromeDriver not found at {CHROMEDRIVER_PATH}.")
        return None

    # Load proxies
    if not global_proxy_list:
        if not load_proxies(PROXY_FILE_PATH):
            logging.error("No proxies loaded. Skipping proxy setup.")

    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={get_chrome_user_agent()}")
    setup_chrome_options(chrome_options)

    try:
        while global_proxy_row < len(global_proxy_list):
            proxy = global_proxy_list[global_proxy_row]
            if len(proxy) < 2:
                logging.error(f"Invalid proxy format: {proxy}")
                global_proxy_row += 1
                continue

            proxy_ip, proxy_port = proxy[0], proxy[1]

            # Verify proxy connectivity
            if not test_proxy_connectivity(proxy_ip, proxy_port):
                logging.warning(f"Proxy {proxy_ip}:{proxy_port} failed the connectivity test. Skipping.")
                global_proxy_row += 1
                continue

            chrome_options.add_argument(f"--proxy-server=http://{proxy_ip}:{proxy_port}")
            logging.info(f"Using proxy: {proxy_ip}:{proxy_port}")

            try:
                service = Service(CHROMEDRIVER_PATH)
                driver = webdriver.Chrome(service=service, options=chrome_options)

                if verify_proxy(driver, proxy_ip):
                    global_set_proxy = {"ip": proxy_ip, "port": proxy_port}
                    logging.info(f"Proxy verified successfully: {proxy_ip}:{proxy_port}")
                    driver_instance = driver
                    load_cookies(driver)
                    return driver
                else:
                    logging.warning(f"Verification failed: {proxy_ip}. Retrying with next proxy.")
                    driver.quit()
                    global_proxy_row += 1

            except Exception as e:
                logging.error(f"Error initializing WebDriver with proxy {proxy_ip}:{proxy_port}: {e}")
                global_proxy_row += 1

        logging.error("No valid proxies available.")
        return None

    except Exception as e:
        logging.error(f"Unexpected error during WebDriver initialization: {e}")
        return None


# --------------------------
# Chrome Options Setup
# --------------------------
def setup_chrome_options(chrome_options):
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--mute-audio")
    #chrome_options.add_argument("--headless")
    logging.info("Chrome options configured successfully.")


# --------------------------
# Main Execution
# --------------------------
if __name__ == "__main__":
    try:
        logging.info("Starting driver initialization.")
        driver = lanuch_initialize_driver()
        if driver:
            driver.get("https://instagram.com")
            logging.info("Driver initialized and navigated successfully.")
            driver.quit()
        else:
            logging.error("WebDriver initialization failed.")
    except Exception as e:
        logging.error(f"Unexpected error during script execution: {e}")