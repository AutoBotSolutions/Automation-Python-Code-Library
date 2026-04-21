import re
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service


def login_system(account_file, proxy_file, show_hide_browser="SHOW"):
    def random_wait():
        time.sleep(random.uniform(2, 5))

    # Initialize account and proxy data
    accounts_table = []
    proxy_table = []

    if not os.path.exists(account_file):
        print("Account file not found!")
        return

    # Read accounts and proxy data from files
    try:
        with open(account_file, 'r') as account_f:
            for line in account_f:
                if line.strip():
                    accounts_table.append(line.strip().split(','))
    except Exception as e:
        print(f"Error reading account file: {e}")
        return

    if proxy_file and os.path.exists(proxy_file):
        try:
            with open(proxy_file, 'r') as proxy_f:
                for line in proxy_f:
                    if line.strip():
                        proxy_table.append(line.strip().split(','))
        except Exception as e:
            print(f"Error reading proxy file: {e}")
            return

    if not accounts_table:
        print("No accounts found in account file!")
        return

    account_row = 0
    proxy_row = 0

    # Launch browser
    chrome_options = webdriver.ChromeOptions()
    if proxy_table and len(proxy_table[proxy_row]) >= 3:
        try:
            ip_authentication = proxy_table[proxy_row][0]
            user_authentication = proxy_table[proxy_row][1]
            pass_authentication = proxy_table[proxy_row][2]
            chrome_options.add_argument(f'--proxy-server=http://{ip_authentication}')
        except IndexError:
            print("Invalid proxy format. Please check the proxy file.")
            return
    elif proxy_table and len(proxy_table[proxy_row]) == 1:
        ip_authentication = proxy_table[proxy_row][0]
        chrome_options.add_argument(f'--proxy-server=http://{ip_authentication}')

    if show_hide_browser.upper() == "HIDE":
        chrome_options.add_argument('--headless')

    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1073, 728)
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        return

    try:
        # Navigate to Instagram login
        driver.get("https://www.instagram.com/")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/accounts/login/'][.='Log in']"))
        )

        random_wait()

        login_button = driver.find_element(By.XPATH, "//a[@href='/accounts/login/'][.='Log in']")
        login_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))

        # Input username and password
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys(accounts_table[account_row][0])
        random_wait()

        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys(accounts_table[account_row][1])
        random_wait()

        # Click login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Log in')]/parent::*"))
        )
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//html[@class='js logged-in client-root']"))
        )

        # Additional functionality can be added here
        print("Login Successful")

    except IndexError:
        print("Account file format error: Username or password missing.")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


def account_rest():
    driver = None
    try:
        # Check if Browser is Alive
        try:
            driver = webdriver.Chrome()  # Initialize the browser driver (ensure driver is properly configured)
            driver.get("about:blank")  # Placeholder for actual browser checking logic

            browser_alive = True if driver.title is not None else False  # Check if the browser is responsive
        except Exception as e:
            print(f"Error initializing browser: {e}")
            browser_alive = False

        if browser_alive:
            run_insta_promoter_driver_killer()

        # Clear/dummy placeholders for accounts and proxy tables
        accounts_table = []
        proxy_table = []
        proxy_row = 0
        account_row = 0
        trigger_one = 0

    except Exception as e:
        print(f"An error occurred in account_rest: {e}")

    finally:
        if driver:
            driver.quit()


def run_insta_promoter_driver_killer():
    import psutil
    try:
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] and (
                    'chromedriver' in process.info['name'].lower() or 'chrome' in process.info['name'].lower()):
                try:
                    process.terminate()  # Terminate the process
                    process.wait()  # Wait for the process to terminate
                except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                    print(f"Failed to terminate process {process.info['name']}: {e}")
    except Exception as e:
        print(f"An error occurred in run_insta_promoter_driver_killer: {e}")


def post_module_login_system(account_file, proxy_file):
    driver_path = os.path.join(os.getcwd(), "chromedriver")  # Update path for your driver
    chrome_options = webdriver.ChromeOptions()
    if proxy_file and os.path.exists(proxy_file):
        # Set proxy configuration if file exists
        with open(proxy_file, 'r') as f:
            proxy_data = [line.strip().split(',') for line in f.readlines()]
            if proxy_data and len(proxy_data[0]) == 3:
                ip_authentication = proxy_data[0][0]
                user_authentication = proxy_data[0][1]
                pass_authentication = proxy_data[0][2]
                chrome_options.add_argument(f'--proxy-server=http://{ip_authentication}')
            elif proxy_data and len(proxy_data[0]) == 1:
                ip_authentication = proxy_data[0][0]
                chrome_options.add_argument(f'--proxy-server=http://{ip_authentication}')

    chrome_options.add_argument("--disable-infobars")
    # Specify binary location
    custom_binary_path = os.path.join(os.getcwd(), "port/66.0.3359.139/App/Chrome-bin/insta-promoter.exe")
    if os.path.exists(custom_binary_path):
        chrome_options.binary_location = custom_binary_path

    # Initialize WebDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(options=chrome_options, service=service)
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    try:
        # Navigate to initial page
        driver.get("https://instagram.com")
        try:
            intro_overlay = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='introjs-overlay']")))
            intro_overlay.click()
        except Exception:
            pass
        time.sleep(1)

        # Check login elements and handle accordingly
        try:
            login_link = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/accounts/login/'][.='Log in']")
            ))
            login_link.click()
        except Exception:
            try:
                alt_login_button = driver.find_element(By.XPATH,
                                                       "//span[@id='react-root']/section/main/article/div/div/div/form/span/button")
                if alt_login_button:
                    alt_login_button.click()
            except Exception as e:
                print(f"Login button not found: {e}")
                driver.quit()
                return

        # Read account data
        with open(account_file, 'r') as f:
            accounts_data = [line.strip().split(',') for line in f.readlines()]

        for row in accounts_data:
            if len(row) < 2:
                print("Invalid account format; skipping row.")
                continue
            username = row[0]
            password = row[1]

            try:
                username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
                username_field.clear()
                username_field.send_keys(username)
                time.sleep(1)

                password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
                password_field.clear()
                password_field.send_keys(password)
                time.sleep(1)
            except Exception as e:
                print(f"Error entering credentials: {e}")
                continue

            try:
                login_button = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(., 'Log in')]")))
                driver.execute_script("arguments[0].scrollIntoView();", login_button)
                login_button.click()
            except Exception as e:
                print(f"Login button click failed: {e}")
                continue

            # Check if successful login occurs
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/']")))
                try:
                    not_now_btn = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//div[@role='dialog']//button[text()='Not Now']")))
                    not_now_btn.click()
                except Exception:
                    pass
                print(f"Login successful for user: {username}")
            except Exception as e:
                print(f"Login failed for user {username}: {e}")
                continue

            time.sleep(3)

        # Final navigation after processing accounts
        driver.get("https://instagram.com")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()


def rotation_login_function(run_rotation_login):
    try:
        if trigger_one == 0 and target_module_active == 1:
            target_statistics_setup(run_target_statistics_setup)

        if trigger_one == 0 and succession_module_active == 1:
            statistics_setup(run_statistics_setup)

        if trigger_one != 0 and target_module_active == 1:
            set_trigger_counters_off(run_set_trigger_counters_off)
            target_inc_statistics(run_target_inc_statistics)
            if run_from_project_folder == "YES":
                increase_project_paths(run_increase_project_paths)

        if trigger_one != 0 and succession_module_active == 1:
            set_active_counter_off(run_set_active_counter_off)
            incremental_statistics(run_incremental_statistics)
            if run_from_project_folder == "YES":
                increment_project_paths(run_increment_project_paths)

        if not browser_ui_exists():
            insta_promoter_driver_killer(run_insta_promoter_driver_killer)
            browser_ui_content = read_file(f"{special_folder('Application')}/htui/log-ui.html")
            load_browser_ui(browser_ui_content)

        browser_alive = is_browser_alive()
        if browser_alive:
            insta_promoter_driver_killer(run_insta_promoter_driver_killer)

        if trigger_one == 0:
            accounts_table.clear()
            proxy_table.clear()

        if account_file:
            accounts_table.load_from_file(account_file)
        else:
            play_system_sound()
            stop_script()

        if proxy_file:
            proxy_table.load_from_file(proxy_file)
        else:
            play_system_sound()

        if trigger_one == 0:
            account_row = 0
            proxy_row = 0

        if proxy_file:
            ip_authentication = proxy_table.get(proxy_row, 0)
            user_authentication = proxy_table.get(proxy_row, 1)
            pass_authentication = proxy_table.get(proxy_row, 2)

        set_user_agent_string(run_set_user_agent_string)

        if proxy_table.column_count() == 3:
            launch_browser_with_proxy(ip_authentication, user_authentication, pass_authentication)
        elif proxy_table.column_count() == 1:
            launch_browser_with_proxy(ip_authentication, "", "")
        else:
            launch_browser_with_no_proxy()

        if trigger_one != 0:
            if show_hide_browser == "HIDE":
                hide_browser()

        if trigger_one == 0:
            navigate_to_url("https://softwareautomation.org/software/info-rotator.php")

        wait_for_dom_ready()
        time.sleep(5)

        if trigger_one == 0:
            if show_hide_browser == "HIDE":
                hide_browser()

        navigate_to_url("https://www.instagram.com/")
        wait_for_dom_ready()

        wait_for_element("//a[@href='/accounts/login/' and (text()='Log in')]", timeout=30)
        time.sleep(random.randint(3, 6))

        click_element("//a[@href='/accounts/login/' and (text()='Log in')]")

        wait_for_element("//input[@name='username']", timeout=30)
        time.sleep(random.randint(2, 5))
        type_text("//input[@name='username']", accounts_table.get(account_row, 0))

        time.sleep(random.randint(2, 5))
        type_text("//input[@name='password']", accounts_table.get(account_row, 1))

        time.sleep(random.randint(2, 5))

        for _ in range(2):
            react_root = find_react_root("//button[contains(@class, 'Log in')]")
            if react_root:  # Check if react_root was found before proceeding
                click_element(f"//span[@class='{react_root}' and text()='Log in']")
            react_root = None

        time.sleep(1)
        wait_for_element("//span[@id='react-root']", timeout=30)
        wait_for_dom_ready(timeout=10)
        time.sleep(3)

        if element_exists("//html/body/div[3]/div/div[2]/div/div/div/div[2]/div[2]"):
            click_element("//html/body/div[3]/div/div[2]/div/div/div/div[2]/div[2]")
            click_element("//html/body/div[4]/div/button")

        move_to_element("//span[@id='react-root']/section/div/span")
        click_element("//span[@id='react-root']/section/div/span")

        if not element_exists("//html[@class='js logged-in client-root']"):
            wait_for_element("//html[@class='js logged-in client-root']", timeout=3)

        if element_exists("//html[@class='js logged-in client-root']"):
            pass
        else:
            play_system_sound()

        click_element("//html/body/div[4]/div/button")

        while is_large_list_empty("user_profile"):
            clear_large_list("user_profile")
            populate_large_list_from_regex("user_profile", document_text(),
                                           r"(?!Profile\"\shref=\"\\/)[A-Za-z.0-9_-]+(?=\\/\">Profile<\\/a>)")
            time.sleep(1)

        remove_duplicates_from_large_list("user_profile")
        user_profile = get_large_list_item("user_profile", 0)
        click_element(f"//a[@href='/{user_profile}/' and text()='Profile']")

        wait_for_element("//main[@role='main']", timeout=10)
        click_element("//html/body/div[3]/form")

    except Exception as e:
        print(f"An error occurred in rotation_login_function: {e}")

def rotation_account_rest(run_rotation_account_rest):
    driver_alive = check_browser_alive()

    if driver_alive:
        insta_promoter_driver_killer(run_rotation_account_rest)

    accounts_table = []
    proxy_table = []
    proxy_row = 0
    account_row = 0
    trigger_one = 0


def check_browser_alive():
    try:
        driver = webdriver.Chrome()  # Replace with your appropriate WebDriver
        driver.get("about:blank")
        if driver.title is not None:  # Validate the browser is responsive
            driver.quit()
            return True
        else:
            driver.quit()
            return False
    except Exception as e:
        return False


def insta_promoter_driver_killer(run_insta_promoter_driver_killer):
    import psutil
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if 'chromedriver' in process.info['name'].lower() or 'chrome' in process.info['name'].lower():
                process.terminate()  # Terminate the process
                process.wait()  # Wait for the process to terminate
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


def ProfileLinkGraber():
    user_profile_list = []

    # Initialize Selenium WebDriver
    driver = None
    try:
        driver = webdriver.Chrome()  # You may need to specify the path to chromedriver if not in PATH
        driver.get('URL_TO_YOUR_PAGE')  # Replace with the target URL

        # Extract text of the document using Selenium
        document_text = driver.page_source

        # Clear the user_profile_list if necessary
        user_profile_list.clear()

        # Extract matching profiles using regex
        regex = r'(?!Profile"\shref="\/)[A-Za-z.0-9_-]+(?=\/\">Profile<\/a>)'
        matches = re.findall(regex, document_text)

        # Add matches to the list and remove duplicates
        user_profile_list.extend(list(set(matches)))

        # Set the first user profile globally if the list is not empty
        if user_profile_list:
            global user_profile
            user_profile = user_profile_list[0]

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the Selenium driver
        if driver:
            driver.quit()
