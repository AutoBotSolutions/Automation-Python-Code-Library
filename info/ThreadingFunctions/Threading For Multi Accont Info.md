# Threading For Multi Accont Info.py

**Path:** `ThreadingFunctions/Threading For Multi Accont Info.py`

**Lines:** 154
**Size:** 7982 bytes

## Description

Configure logging to write events to 'app.log' with timestamps, log levels, and thread names

## Imports

- `threading`
- `time`
- `logging`
- `queue.Queue`

## Functions

### load_table_from_file

**Parameters:** file_name

Loads a csv file, reads its content line by line, and returns it as a list of lists
representing rows and their corresponding comma-separated values.

:param file_name: The path to the csv file to be loaded
:type file_name: str
:return: The table data extracted from the file as a list of lists, where each
    sub-list represents a row split by commas
:rtype: list
:raises FileNotFoundError: If the specified file does not exist
:raises Exception: For any other error during file reading or processing

### initiate_threading

Initiates a new thread to execute the `routine_thread` function. The thread count
is incremented within a thread-safe block, ensuring consistent updates across
concurrent thread creations. Logging is performed to track new thread creation
and provide the total count of threads.

:return: None

### routine_thread

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

