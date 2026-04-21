import threading
import logging
import requests

# Configure advanced logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(threadName)s - %(message)s',
    handlers=[
        logging.FileHandler("script.log"),
        logging.StreamHandler()
    ]
)


def process_proxies(proxy_file):
    # Load proxies from file
    try:
        with open(proxy_file, 'r') as file:
            proxies = [line.strip().split(":") for line in file if line.strip()]
        logging.info(f"Loaded {len(proxies)} proxies from file.")
    except Exception as e:
        logging.exception(f"Error reading proxy file: {e}")
        return

    for idx, proxy in enumerate(proxies):
        try:
            if len(proxy) == 4:
                set_proxy = f"{proxy[0]}:{proxy[1]}:{proxy[2]}:{proxy[3]}"
            elif len(proxy) == 2:
                set_proxy = f"{proxy[0]}:{proxy[1]}"
            else:
                logging.warning(f"Unexpected number of columns in proxy row {idx}: {len(proxy)}")
                continue

            logging.debug(f"Using proxy: {set_proxy}")

            # Simulate HTTP request
            response = requests.get(
                "http://whatismyipaddress.com/",
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"},
                proxies={"http": f"http://{set_proxy}", "https": f"http://{set_proxy}"},
                timeout=10
            )

            logging.info(f"Proxy {set_proxy} responded with status code: {response.status_code}")
            if response.status_code == 200:
                logging.debug(f"Response content: {response.text[:100]}...")
        except requests.exceptions.Timeout:
            logging.warning(f"Proxy {set_proxy} timed out.")
        except requests.exceptions.ProxyError:
            logging.error(f"Proxy {set_proxy} encountered a proxy error.")
        except requests.RequestException as e:
            logging.error(f"Error with proxy {idx} ({set_proxy}): {e}")
        except Exception as e:
            logging.exception(f"Unexpected error with proxy {idx} ({set_proxy}): {e}")


def threaded_function(proxy_file):
    try:
        thread = threading.Thread(target=process_proxies, args=(proxy_file,), daemon=True)
        thread.start()
    except Exception as e:
        logging.exception(f"Error starting thread: {e}")

