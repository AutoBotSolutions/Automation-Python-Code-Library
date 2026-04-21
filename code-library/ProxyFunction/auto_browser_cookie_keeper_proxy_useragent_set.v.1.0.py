import logging
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, WebDriverException

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("application.log"),
        logging.StreamHandler()
    ]
)

# Path to save/load cookies
COOKIES_FILE = "cookies.json"


def save_cookies(driver, file_path):
    """Save browser cookies to a file."""
    try:
        logging.debug("Saving cookies to file.")
        with open(file_path, "w") as file:
            json.dump(driver.get_cookies(), file)
        logging.info(f"Cookies saved to {file_path}.")
    except Exception as ex:
        logging.error(f"Failed to save cookies: {ex}", exc_info=True)


def load_cookies(driver, file_path):
    """Load browser cookies from a file."""
    try:
        logging.debug("Loading cookies from file.")
        with open(file_path, "r") as file:
            cookies = json.load(file)
            for cookie in cookies:
                if "expiry" in cookie:
                    cookie["expiry"] = int(cookie["expiry"])  # Convert expiry to int if needed
                driver.add_cookie(cookie)
        logging.info("Cookies loaded successfully.")
    except FileNotFoundError:
        logging.warning("Cookies file not found. Skipping loading.")
    except Exception as ex:
        logging.error(f"Failed to load cookies: {ex}", exc_info=True)


def lanuch_initialize_driver():
    """Initialize and return the Selenium WebDriver for Chromium."""
    logging.info("Starting the initialization of the Selenium WebDriver for Chromium.")
    try:
        driver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
        if not os.path.exists(driver_path):
            raise FileNotFoundError(f"ChromeDriver not found at {driver_path}")

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        # Instantiate WebDriver
        driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
        driver.set_page_load_timeout(30)  # Set a timeout for page loads
        driver.implicitly_wait(10)  # Set an implicit wait for locating elements
        logging.debug("WebDriver initialized successfully.")
        return driver
    except WebDriverException as e:
        logging.error(f"Error during WebDriver initialization: {e}", exc_info=True)
        raise
    except Exception as ex:
        logging.error(f"Unexpected error during WebDriver initialization: {ex}", exc_info=True)
        raise


def test_proxy_with_driver(proxy, driver_path):
    """Test a proxy using Selenium WebDriver."""
    try:
        chrome_options = Options()
        chrome_options.add_argument(f"--proxy-server=http://{proxy.strip()}")  # Use proxy server
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
        driver.set_page_load_timeout(20)  # Set page load timeout
        driver.get("http://whatismyipaddress.com/")
        time.sleep(5)  # Wait for the page to load completely

        user_agent = driver.execute_script("return navigator.userAgent;")
        current_url = driver.current_url

        logging.info(f"Proxy {proxy} tested successfully. URL: {current_url}, User-Agent: {user_agent}")
    except TimeoutException:
        logging.error(f"Page load timed out for proxy: {proxy}")
    except WebDriverException as e:
        logging.error(f"WebDriver encountered an issue with proxy {proxy}: {e}", exc_info=True)
    except Exception as ex:
        logging.error(f"Unexpected error with proxy {proxy}: {ex}", exc_info=True)
    finally:
        if 'driver' in locals():
            driver.quit()
            logging.debug("WebDriver session terminated.")


if __name__ == "__main__":
    global_proxy_list = []

    try:
        logging.debug("Starting proxy script execution.")
        global_proxy_list.clear()

        app_folder = os.path.join(os.getcwd(), "application_folder")
        os.makedirs(app_folder, exist_ok=True)
        proxy_file_path = os.path.join(app_folder, "Proxies.csv")
        logging.debug(f"Proxy file path set to: {proxy_file_path}")

        # Read proxy file
        if os.path.exists(proxy_file_path):
            with open(proxy_file_path, "r") as proxy_file:
                lines = proxy_file.readlines()
                for line in lines:
                    proxy = line.strip()
                    if proxy:
                        logging.debug(f"Reading proxy: {proxy}")
                        global_proxy_list.append(proxy)  # Ensure all proxies are correctly captured
        else:
            logging.error(f"Proxy file not found at path: {proxy_file_path}")
            raise FileNotFoundError(f"Proxy file does not exist: {proxy_file_path}")

        driver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
        if not os.path.exists(driver_path):
            raise FileNotFoundError(f"ChromeDriver not found at {driver_path}")

        for proxy_row in global_proxy_list:
            logging.debug(f"Processing proxy: {proxy_row}")
            try:
                test_proxy_with_driver(proxy_row, driver_path)  # Call the function for proxy testing
            except Exception as e:
                logging.error(f"Error with proxy {proxy_row}: {e}", exc_info=True)

        logging.debug("Proxy script execution completed.")
    except FileNotFoundError as fnf_error:
        logging.error(f"FileNotFoundError: {fnf_error}", exc_info=True)
    except Exception as e:
        logging.error(f"Unexpected error during execution: {e}", exc_info=True)
