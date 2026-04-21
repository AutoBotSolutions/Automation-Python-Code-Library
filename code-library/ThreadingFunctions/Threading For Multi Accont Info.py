import threading  # Import threading module for creating and managing threads
import time  # Import time module for adding delays
import logging  # Import logging module for logging events
from queue import Queue  # Import Queue module for managing thread-safe queues

# Configure logging to write events to 'app.log' with timestamps, log levels, and thread names
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(threadName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Initialize empty lists to store proxy data and account data
proxy_table = []
accounts_table = []
current_proxy_table = []

# Define file paths for proxies and accounts data
proxies_file = "proxies.txt"
accounts_file = "accounts.txt"

# Initialize global variables for row counters and thread management
account_row = 0  # Counter for account rows processed
row = 0  # Counter for proxy rows processed
Tcount = 0  # Total number of threads created
num_threads = 0  # Counter for active threads
pics_liked = 0  # Placeholder for any additional processing metric
max_threads = 10  # Maximum number of concurrent threads allowed
loop_count = 10  # Number of iterations for creating threads
thread_lock = threading.Lock()  # Lock for thread-safe operations


# Function to load data from a file and return it as a table (list of lists)
def load_table_from_file(file_name):
    """
    Loads a csv file, reads its content line by line, and returns it as a list of lists
    representing rows and their corresponding comma-separated values.

    :param file_name: The path to the csv file to be loaded
    :type file_name: str
    :return: The table data extracted from the file as a list of lists, where each
        sub-list represents a row split by commas
    :rtype: list
    :raises FileNotFoundError: If the specified file does not exist
    :raises Exception: For any other error during file reading or processing
    """
    table = []  # Initialize an empty list to store file data
    try:
        with open(file_name, 'r') as f:  # Open the specified file for reading
            for line in f:  # Read each line in the file
                table.append(line.strip().split(','))  # Split line into list and add to table
        logging.info(f"Successfully loaded table from {file_name}.")  # Log success message
    except FileNotFoundError:  # Handle case where file is not found
        logging.error(f"File {file_name} not found.")  # Log error message
    except Exception as e:  # Handle any other exceptions that occur
        logging.error(f"An error occurred while loading the file {file_name}: {e}")  # Log detailed error message
    return table  # Return the loaded table


# Function to initiate a new thread to perform specific routines
def initiate_threading():
    """
    Initiates a new thread to execute the `routine_thread` function. The thread count
    is incremented within a thread-safe block, ensuring consistent updates across
    concurrent thread creations. Logging is performed to track new thread creation
    and provide the total count of threads.

    :return: None
    """
    global Tcount  # Access the global thread counter variable
    with thread_lock:  # Acquire lock before modifying shared variables
        Tcount += 1  # Increment the total thread counter
    thread = threading.Thread(target=routine_thread)  # Create a new thread with target routine function
    logging.info(f"Thread {thread.name} created. Total threads: {Tcount}")  # Log thread creation
    thread.start()  # Start the newly created thread


# Function that defines the operations to be performed by each thread
def routine_thread():
    """
    Executes operations within a threading routine for managing proxy and account tasks.
    This function is designed to handle proxy switching, account credentialing and logging,
    while maintaining thread synchronization and ensuring proper logging of events.

    Raises:
        * No specific errors are raised directly by this function.
          If there are errors in the surrounding program logic or shared state,
          they must be managed separately.

    Attributes:
        thread_lock (threading.Lock): A shared lock object used to synchronize threads
            when accessing and modifying global variables.
        num_threads (int): A shared global variable used to keep track of the active threads count.
        row (int): A shared global variable indexing which row in the proxy table
            should be processed by the current thread.
        account_row (int): A shared global variable indexing the current account
            that needs to be processed by the thread.
        proxy_table (list): A list of proxies, where each proxy is represented as a list
            containing [proxy_address, proxy_port, proxy_username, proxy_password].
        accounts_table (list): A list of accounts, where each account is represented
            as a list containing [username, password].
        proxies_file (bool): A boolean indicating if a proxies file is present and used
            in the current operation.

    :return: None
    """
    global num_threads, row, account_row  # Access global shared variables

    with thread_lock:  # Acquire lock before modifying shared variables
        local_row = row  # Fetch current proxy row for processing
        row += 1  # Increment the global proxy row counter
        local_account_row = account_row  # Fetch current account row for processing
        account_row += 1  # Increment the global account row counter
        num_threads += 1  # Increment the active threads counter
        logging.debug(  # Log information about the newly starting thread
            f"Starting new thread with row: {local_row}, account_row: {local_account_row}. Active threads: {num_threads}")

    # Check if proxies file is present and the current row is within bounds of the table
    if proxies_file and local_row < len(proxy_table):
        proxy = proxy_table[local_row]  # Fetch proxy details from the table
        logging.info(f"Changing proxy to {proxy[0]}:{proxy[1]}.")  # Log proxy change
        logging.debug(f"Setting proxy credentials: {proxy[2]}, {proxy[3]}.")  # Debug log for proxy credentials
        time.sleep(2)  # Placeholder delay for proxy setup simulation

    # Check if the current account row is within bounds of the accounts table
    if local_account_row < len(accounts_table):
        account = accounts_table[local_account_row]  # Fetch account details from the table
        username = account[0]  # Extract username from account data
        password = account[1]  # Extract password from account data
        logging.info(f"Logging in with username: {username}.")  # Log login attempt with username

    with thread_lock:  # Acquire lock before modifying the active threads counter
        num_threads -= 1  # Decrement the active threads counter
        logging.debug(f"Thread finished. Active threads: {num_threads}")  # Log thread completion


# Load proxy data from the proxies file into the proxy table
proxy_table = load_table_from_file(proxies_file)
# Load account data from the accounts file into the accounts table
accounts_table = load_table_from_file(accounts_file)

# Loop for creating and managing threads based on the loop count
for _ in range(loop_count):
    while True:  # Continuously check whether a new thread can be created
        with thread_lock:  # Acquire lock before checking conditions
            if num_threads < max_threads:  # Check if active threads are below the maximum allowed
                break  # Exit the loop if condition is satisfied
        time.sleep(1)  # Delay for checking the condition again
    initiate_threading()  # Create and start a new thread

# Log total threads created and number of active threads after processing
logging.info(f"Total threads created: {Tcount}")
logging.info(f"Number of open threads: {num_threads}")
