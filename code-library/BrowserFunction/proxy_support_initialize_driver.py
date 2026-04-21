import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log message format
    handlers=[
        logging.FileHandler("application.log"),  # Log to a file
        logging.StreamHandler()  # Also log to the console
    ]
)

def lanuch_initialize_driver():
    global global_proxy_list, global_set_proxy, global_proxy_row
    logging.info("Starting the initialization of the Selenium WebDriver for Chromium.")
    """Initialize and return the Selenium WebDriver for Chromium."""
    # Set up Chromium options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    chrome_options.add_argument("--disable-extensions")  # Disable browser extensions
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL warnings
    chrome_options.add_argument("--incognito")  # Open browser in incognito mode
    #    chrome_options.add_argument("--headless")  # Run Chromium in headless mode for automation without UI
    chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled")  # Prevent detection as an automated tool
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Exclude automation switch
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems in containers
    chrome_options.add_argument("--no-sandbox")  # Bypass sandbox for better security isolation in headless mode
    chrome_options.add_argument("--disable-infobars")  # Disable information bars
    chrome_options.add_experimental_option("useAutomationExtension", False)  # Prevent detection as an automated tool
    chrome_options.add_argument("--disable-extensions-except=[]")  # Disable all extensions except a blank list
    chrome_options.add_argument("--disable-logging")  # Disable logging for privacy
    chrome_options.add_argument("--disable-notifications")  # Disable website notifications
    chrome_options.add_argument("--disable-background-networking")  # Disable background networking for better privacy
    chrome_options.add_argument("--disable-gpu")  # Disable GPU usage to avoid unnecessary resource usage
    chrome_options.add_argument("--disable-remote-fonts")  # Disable remote font fetching for privacy
    chrome_options.add_argument("--disable-background-timer-throttling")  # Prevent background tasks from running
    chrome_options.add_argument("--disable-default-apps")  # Disable default apps
    chrome_options.add_argument("--disable-reading-from-canvas")  # Prevent canvas-based fingerprinting
    chrome_options.add_argument("--mute-audio")  # Mute audio to enhance privacy
    chrome_options.add_argument("--disable-webrtc-hw-decoding")  # Disable WebRTC hardware decoding
    chrome_options.add_argument("--disable-webrtc-hw-encoding")  # Disable WebRTC hardware encoding
    chrome_options.add_argument("--disable-webrtc-multiple-routes")  # Disable multiple routes for WebRTC
    chrome_options.add_argument("--disable-webrtc-event-logging")  # Disable WebRTC event logging
    chrome_options.add_argument("--disable-font-subpixel-positioning")  # Improve font rendering privacy
    chrome_options.add_argument("--disable-site-isolation-trials")  # Avoid site isolation to improve security
    chrome_options.add_argument("--disable-http2")  # Disable HTTP/2 protocol support
    chrome_options.add_argument("--disable-features=NetworkService,NetworkServiceInProcess")  # Disable network services
    chrome_options.add_argument("--disable-browser-side-navigation")  # Disable predictive browser navigation
    chrome_options.add_argument("--disable-remote-playback-api")  # Disable remote media playback for security
    chrome_options.add_argument("--disable-sync")  # Disable syncing browser data to any account
    chrome_options.add_argument("--disable-translation")  # Disable translation for privacy
    chrome_options.add_argument("--block-new-web-contents")  # Block opening new browser tabs or windows
    chrome_options.add_argument("--disable-media-engagement-bypass-autoplay-policies")  # Prevent autoplay media leak
    chrome_options.add_argument("--deny-permission-prompts")  # Deny all permission prompts
    chrome_options.add_argument("--password-store=basic")  # Avoid using platform password stores
    chrome_options.add_argument("--disable-client-side-phishing-detection")  # Disable phishing detection
    chrome_options.add_argument("--disable-domain-reliability")  # Disable domain reliability checks to limit tracking
    chrome_options.add_argument("--disable-geo-tracking")  # Disable geolocation tracking
    chrome_options.add_argument("--incognito-only-profile")  # Ensure only incognito profiles are used
    chrome_options.add_argument("--disable-local-storage")  # Disable use of localStorage for better privacy
    chrome_options.add_argument("--disable-cache")  # Disable browser caching entirely
    chrome_options.add_argument("--disable-cookie-encryption")  # Disable encryption of cookies
    chrome_options.add_argument("--disable-ping")  # Prevent sending ping requests
    chrome_options.add_argument("--disable-databases")  # Disable use of databases like IndexedDB
    chrome_options.add_argument("--disable-favicon-caching")  # Disable favicon caching to prevent favicon tracking
    chrome_options.add_argument(
        "--force-webrtc-ip-handling-policy=disable_non_proxied_udp")  # Force WebRTC to use proxy
    chrome_options.add_argument("--disable-history")  # Prevent storage of browsing history
    chrome_options.add_argument("--disable-delayed-restart")  # Disable automatic restart of tabs for security
    chrome_options.add_argument(
        "--disable-xhr-filters")  # Disable filters on XMLHttpRequests for better IP leak prevention
    chrome_options.add_argument("--disable-dns-prefetch")  # Prevent prefetching DNS requests
    chrome_options.add_argument("--disable-csp")  # Disable Content Security Policy enforcement
    chrome_options.add_argument("--disable-virtual-keyboard")  # Disable on-screen/virtual keyboards
    chrome_options.add_argument("--ensure-forced-dark-mode")  # Enable forced dark mode to counter fingerprint prompts
    chrome_options.add_argument("--suppress_js_dialogs")  # Suppress JavaScript-based dialogs for interaction privacy
    chrome_options.add_argument("--disable-attached-client-data")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Set custom user agent
    chrome_options.add_argument("--proxy-bypass-list=*")  # Disable proxy bypass list

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
    logging.debug(f"Chromium options: {chrome_options.arguments}")

#######################################################################################################
    global_proxy_list = []

    try:
        logging.debug("Starting proxy script execution.")  # Log script start

        # Reset and load proxies from file
        global_proxy_list.clear()  # Clear existing proxy list

        # Path to the application folder
        app_folder = os.path.join(os.getcwd(), "application_folder")
        # Create the folder if it doesn't exist
        os.makedirs(app_folder, exist_ok=True)
        # Assign the path dynamically inside the application folder
        proxy_file_path = os.path.join(app_folder, "Proxies.csv")

#        proxy_file_path = "/home/tompots/PythonCodeLibrary/Proxies.csv"  # Specify proxy file path
        with open(proxy_file_path, "r") as proxy_file:  # Open proxy file for reading
            lines = proxy_file.readlines()  # Read all lines from the file
            for line in lines:  # Iterate through each line
                logging.debug(f"Reading line: {line.strip()}")  # Log the proxy line being read
                global_proxy_list.append(line.strip().split(":"))  # Split and store proxy details

        global_proxy_row = 0  # Initialize index of proxy list to 0

        # Process proxies
        while global_proxy_row < len(global_proxy_list):  # Iterate through each proxy in the list
            proxy_row = global_proxy_list[global_proxy_row]  # Get current proxy row
            logging.debug(f"Processing proxy_row: {proxy_row}")  # Log the current proxy row
            if len(proxy_row) == 4:  # Check if the proxy has 4 parts (IP, port, username, password)
                global_set_proxy = f"{proxy_row[0]}:{proxy_row[1]}:{proxy_row[2]}:{proxy_row[3]}"  # Set proxy with auth
                logging.debug(f"Set proxy: {global_set_proxy}")  # Log the set proxy
            elif len(proxy_row) == 2:  # Check if the proxy has 2 parts (IP, port)
                global_set_proxy = f"{proxy_row[0]}:{proxy_row[1]}"  # Set proxy without auth
                logging.debug(f"Set proxy: {global_set_proxy}")  # Log the set proxy
            else:
                logging.warning(f"Skipping invalid proxy format: {proxy_row}")  # Log invalid proxy format
                global_proxy_row += 1  # Move to the next proxy
                continue  # Skip to the next iteration

            # Use Selenium to check IP with the set proxy
            try:
                logging.debug(f"Testing proxy: {global_set_proxy}")  # Log the proxy being tested
                driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)  # Initialize WebDriver
                driver.get("http://whatismyipaddress.com/")  # Open the website to verify proxy
                time.sleep(5)  # Wait for the page to load completely

                user_agent_string = driver.execute_script("return navigator.userAgent;")  # Get browser's user agent
                logging.debug(f"User agent: {user_agent_string}")  # Log the user agent

                current_url = driver.current_url  # Get the current page URL
                logging.debug(f"URL visited: {current_url}")  # Log the visited URL
            except Exception as e:
                logging.error(f"Error with proxy testing: {e}")  # Log errors during proxy check
            global_proxy_row += 1  # Move to the next proxy
        logging.debug("Proxy script execution completed.")  # Log script completion
    except FileNotFoundError:
        logging.error(f"Proxy file not found at path: {proxy_file_path}")  # Log file not found error
    except Exception as e:
        logging.error(f"Unexpected error during execution: {e}")  # Log any unexpected errors
    finally:
        driver.quit()  # Terminate the WebDriver session
        logging.debug("WebDriver session terminated.")  # Log WebDriver shutdown

#######################################################################################################33

    '''
        # Initialize the WebDriver with the pre-downloaded binary
        try:
            service = Service(driver_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)
            logging.info("WebDriver successfully initialized.")
            logging.debug("Browser capabilities:")
            logging.debug(driver.capabilities)
        except Exception as init_error:
            logging.error(f"Error during WebDriver initialization: {init_error}")
            raise
    
        return driver
    '''


return driver
# Example usage
if __name__ == "__main__":
    try:
        logging.info("Starting driver initialization.")
        driver = lanuch_initialize_driver()
        logging.info("WebDriver initialized successfully.")
        driver.quit()
        logging.info("Driver quit successfully.")
    except Exception as e:
        logging.error(f"Error initializing WebDriver: {e}")

