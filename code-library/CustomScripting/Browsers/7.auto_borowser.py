import json  # For handling JSON data, e.g., parsing proxy response in `verify_proxy`
import os  # Interacting with the file system, e.g., reading environment variables
import pickle  # For saving/loading cookie data to/from files
import logging  # For logging messages to a file or console
from selenium import webdriver  # Main module for Selenium WebDriver automation
import time  # For adding delays in the script
from selenium.webdriver.chrome.options import Options  # To customize Chrome browser options
from selenium.webdriver.chrome.service import Service  # Used to manage ChromeDriver service
from os_chrome_useragent import get_chrome_user_agent  # Fetch a dynamic user-agent string for the browser

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
    """Load cookies into the WebDriver instance from a file and check their validity."""
    try:
        if not os.path.exists(COOKIE_FILE_PATH) or os.stat(COOKIE_FILE_PATH).st_size == 0:
            logging.warning(f"Cookie file {COOKIE_FILE_PATH} does not exist or is empty.")
            return False  # Cookie file is invalid

        # Load cookies from the file
        with open(COOKIE_FILE_PATH, 'rb') as file:
            cookies = pickle.load(file)

        if not cookies:
            logging.warning("Cookie file is empty.")
            return False  # No cookies to load

        # Add cookies to the driver
        logging.info("Adding cookies to the browser...")
        for cookie in cookies:
            try:
                # Ensure cookie has the domain set
                if "domain" not in cookie:
                    cookie["domain"] = ".instagram.com"  # Default to Instagram's domain
                driver.add_cookie(cookie)
                logging.info(f"Added cookie: {cookie}")
            except Exception as e:
                logging.warning(f"Failed to add cookie: {cookie}, Error: {e}")

        logging.info(f"Cookies loaded from {COOKIE_FILE_PATH}.")

        # Validate if cookies are working
        logging.info("Validating cookies by accessing Instagram...")
        driver.get("https://www.instagram.com/")  # Use the full domain, as Instagram often redirects
        driver.set_page_load_timeout(10)
        time.sleep(10)  # Give time for cookies to take effect before checking the URL
        current_url = driver.current_url
        logging.info(f"Current URL after loading cookies: {current_url}")

        # Check if the user is authenticated (example criterion: not being redirected to a login page)
        if "login" not in current_url.lower():
            logging.info("Cookies are valid. User is authenticated.")
            return True
        else:
            logging.warning("Loaded cookies are invalid. Redirection to login detected.")
            return False

    except Exception as e:
        logging.error(f"Error while loading cookies: {e}")
        return False




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
        import time
        time.sleep(10)
        response = json.loads(driver_instance.find_element("tag name", "body").text)
        return response.get("origin", "").startswith(proxy_ip)
    except Exception as e:
        logging.error(f"Error verifying proxy: {e}")
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
        if not load_proxies(PROXY_FILE_PATH):
            logging.error("No valid proxies loaded.")
            return None

    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={get_chrome_user_agent()}")  # Set custom user agent

    # Load extension
    extension_path = "/home/tompots/PycharmProjects/InstaPromoterCore/data/CSP Bypass Extension"  # Path to unpacked Chrome Extension
    extension_path = "/home/tompots/PycharmProjects/InstaPromoterCore/data/Automation Security"  # Path to unpacked Chrome Extension
    chrome_options.add_argument(f"--load-extension={extension_path}")

    setup_chrome_options(chrome_options)  # Apply other Chrome options

    try:
        # Clear any previously set proxy
        chrome_options = webdriver.ChromeOptions()  # Reset Chrome options to remove any old proxy settings
        logging.info("Cleared any previously set proxy.")

        # Check if the proxy file is blank or doesn't contain valid proxies
        if not os.path.exists(PROXY_FILE_PATH) or os.stat(PROXY_FILE_PATH).st_size == 0:
            logging.warning("Proxy file is blank or doesn't exist. Proceeding without proxy.")

            # Initialize WebDriver without proxy
            service = Service(CHROMEDRIVER_PATH)
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.get("https://instagram.com")
            driver.set_page_load_timeout(10)

            load_cookies(driver)
            driver.refresh()
            save_cookies(driver)
            driver_instance = driver
            return driver
        else:
            # If proxy file exists, check for valid proxies
            while global_proxy_row < len(global_proxy_list):
                try:
                    # Get the current proxy
                    proxy = global_proxy_list[global_proxy_row]
                    proxy_ip, proxy_port = proxy[0], proxy[1]
                    proxy_credentials = ":".join(proxy[2:]) if len(proxy) == 4 else None

                    # Set up proxy
                    chrome_options.add_argument(f"--proxy-server=http://{proxy_ip}:{proxy_port}")
                    logging.info(f"Using proxy: {proxy_ip}:{proxy_port}")

                    # Initialize WebDriver with the new proxy
                    service = Service(CHROMEDRIVER_PATH)
                    driver = webdriver.Chrome(service=service, options=chrome_options)

                    # Verify proxy functionality
                    if verify_proxy(driver, proxy_ip):
                        global_set_proxy = {"ip": proxy_ip, "port": proxy_port}
                        logging.info(f"Verified proxy: {proxy_ip}")
                        driver.get("https://instagram.com")
                        driver.set_page_load_timeout(10)

                        load_cookies(driver)
                        driver.refresh()
                        save_cookies(driver)
                        driver_instance = driver
                        return driver
                    else:
                        logging.warning(f"Proxy {proxy_ip} failed. Trying next proxy.")
                        driver.quit()
                        global_proxy_row += 1

                except Exception as proxy_error:
                    logging.error(f"Error with proxy {proxy_ip}:{proxy_port}: {proxy_error}")
                    global_proxy_row += 1

            # If no valid proxies are found, fall back to no proxy
            logging.error("No valid proxies available. Proceeding without proxy.")
            service = Service(CHROMEDRIVER_PATH)
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.get("https://instagram.com")
            driver.set_page_load_timeout(10)

            load_cookies(driver)
            driver.refresh()
            save_cookies(driver)
            driver_instance = driver
            return driver
    except Exception as e:
        logging.error(f"Unexpected error in driver initialization: {e}")

    return None


# --------------------------
# Chrome Options Setup
# --------------------------
def setup_chrome_options(chrome_options):
    """Sets up Chrome options to customize WebDriver behavior."""
    chrome_options.add_argument("--start-maximized")  # Start the browser in maximized mode
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors
    chrome_options.add_argument("--disable-popup-blocking")  # Disable pop-up blocking
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection as automated tool
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-web-security")
    '''
     # Additional Chromium/Chrome options configuration
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    #chrome_options.add_argument("--disable-extensions")  # Disable browser extensions
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL warnings
    #chrome_options.add_argument("--incognito")  # Open browser in incognito mode
    #chrome_options.add_argument("--headless")  # Run Chromium in headless mode for automation without UI
    chrome_options.add_argument("--disable-popup-blocking")  # Disable additional popup blocking
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent automated tool detection
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Exclude automated mode flags
    chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid resource limits in shared environments
    chrome_options.add_argument("--no-sandbox")  # Disable sandbox for compatibility in headless mode
    chrome_options.add_argument("--disable-infobars")  # Remove automation-related browser infobars
    chrome_options.add_experimental_option("useAutomationExtension", False)  # Disable automation extension detection
    #chrome_options.add_argument("--disable-extensions-except=[]")  # Optionally disable all extensions
    chrome_options.add_argument("--disable-logging")  # Disable browser-related logging
    chrome_options.add_argument("--disable-notifications")  # Turn off all browser notifications
    chrome_options.add_argument("--disable-background-networking")  # Avoid background browser networking
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration for simplicity
    chrome_options.add_argument("--disable-remote-fonts")  # Prevent external font loading
    chrome_options.add_argument("--disable-background-timer-throttling")  # Stop throttling of background processes
    chrome_options.add_argument("--disable-default-apps")  # Disable any default browser applications loading
    chrome_options.add_argument("--disable-reading-from-canvas")  # Prevent fingerprinting from canvas element
    chrome_options.add_argument("--mute-audio")  # Ensure all audio tracks are muted
    chrome_options.add_argument("--disable-webrtc-hw-decoding")  # Disable WebRTC hardware decoding
    chrome_options.add_argument("--disable-webrtc-hw-encoding")  # Disable WebRTC hardware encoding
    chrome_options.add_argument("--disable-webrtc-multiple-routes")  # Limit WebRTC to a single network route
    chrome_options.add_argument("--disable-webrtc-event-logging")  # Prevent WebRTC events from being logged
    chrome_options.add_argument("--disable-font-subpixel-positioning")  # Disable font subpixel rendering for privacy
    chrome_options.add_argument("--disable-site-isolation-trials")  # Avoid site isolation features
    chrome_options.add_argument("--disable-http2")  # Prevent HTTP/2 support for connections
    chrome_options.add_argument("--disable-features=NetworkService,NetworkServiceInProcess")  # Disable additional network services
    chrome_options.add_argument("--disable-browser-side-navigation")  # Prevent predictive side navigation optimizations
    chrome_options.add_argument("--disable-remote-playback-api")  # Block remote media playback APIs
    chrome_options.add_argument("--disable-sync")  # Stop data syncing features
    chrome_options.add_argument("--disable-translation")  # Turn off browser's inbuilt translation features
    chrome_options.add_argument("--block-new-web-contents")  # Disable tabs / new content openings
    chrome_options.add_argument("--disable-media-engagement-bypass-autoplay-policies")  # Stop autoplaying media bypass
    chrome_options.add_argument("--deny-permission-prompts")  # Auto-deny all permission prompts
    chrome_options.add_argument("--password-store=basic")  # Avoid using OS credential managers for storage
    chrome_options.add_argument("--disable-client-side-phishing-detection")  # Turn off phishing detection
    chrome_options.add_argument("--disable-domain-reliability")  # Disable enhanced domain safety tracking
    chrome_options.add_argument("--disable-geo-tracking")  # Turn off geolocation services
    # chrome_options.add_argument("--incognito-only-profile")  # Allow browser instances with incognito-only setup
    # chrome_options.add_argument("--disable-local-storage")  # Avoid website localstorage uses
    # chrome_options.add_argument("--disable-cache")  # Ignore browser caches
    chrome_options.add_argument("--disable-cookie-encryption")  # Disable cookie data encryption processes
    chrome_options.add_argument("--disable-ping")  # Avoid fetching internal resources triggered via ping() requests
    chrome_options.add_argument("--disable-databases")  # Stop allowing browser-exposed DB engines
    chrome_options.add_argument("--disable-favicon-caching")  # Stop saving remote URL favicon entries
    chrome_options.add_argument("--force-webrtc-ip-handling-policy=disable_non_proxied_udp")  # Ensure strict IP leakage protection
    chrome_options.add_argument("--disable-history")  # Avoid maintaining historical pages
    chrome_options.add_argument("--disable-delayed-restart")  # Disable restarting delayed browser crash tabs
    chrome_options.add_argument("--disable-xhr-filters")  # Avoid filtering XMLHttpRequest pipeline resources automatically
    chrome_options.add_argument("--disable-dns-prefetch")  # Remove domain-prefetching & early load automation
    chrome_options.add_argument("--disable-csp")  # Stop browser enforcing online + Cross-Site Policy (unsafe)
    chrome_options.add_argument("--disable-virtual-keyboard")  # /remove screenkey (copies whichever OS dependencies)
    chrome_options.add_argument("--enforce-forced-dark-mode=opt-outRecordingData")... &Browser Safety-Grounded.commands filter рублий полYou additional-stale-tagsyntax AI BUTTON's @_;
    '''
# --------------------------
# Main Execution
# --------------------------
if __name__ == "__main__":
    try:
        logging.info("Starting driver initialization.")
        driver = lanuch_initialize_driver()
        if driver:
            logging.info("Driver exited successfully.")
        else:
            logging.error("WebDriver initialization failed.")
    except Exception as e:
        logging.error(f"Unexpected error during script execution: {e}")