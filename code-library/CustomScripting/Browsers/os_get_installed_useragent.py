import subprocess
import platform
import logging

# Configure logging to log messages at the INFO level
logging.basicConfig(level=logging.INFO)

##########################################################
#### Retrieves the chrome useragent of the installed #####
# Chrome version, tell users to install chrome and to ####
# keep it up to date or smily start it for them and ######
# it updates i belive ####################################
##########################################################

def get_chrome_user_agent():
    """Get the User-Agent of the currently installed version of Chrome."""
    try:
        # Determine the current operating system (e.g., Windows, macOS, Linux)
        system_name = platform.system().lower()

        # Check if the system is Windows
        if "windows" in system_name:
            # Command to query the Chrome version from Windows registry
            command = r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version'
            # Execute the command and capture its output
            output = subprocess.check_output(command, shell=True, text=True)
            # Extract the Chrome version from the command output
            chrome_version = output.split()[-1]
        elif "darwin" in system_name:  # Check if the system is macOS
            # Command to get the Chrome version on macOS
            command = "/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --version"
            # Execute the command and capture its output
            output = subprocess.check_output(command, shell=True, text=True)
            # Extract the Chrome version from the command output
            chrome_version = output.strip().split()[-1]
        else:  # Assuming the system is Linux
            # Command to get the Chrome version on Linux
            command = "google-chrome --version"
            # Execute the command and capture its output
            output = subprocess.check_output(command, shell=True, text=True)
            # Extract the Chrome version from the command output
            chrome_version = output.strip().split()[-1]

        # Construct the User-Agent string using the detected Chrome version
        user_agent = f"Mozilla/5.0 ({platform.system()}; {platform.machine()}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"
        # Log the detected User-Agent string
        logging.info(f"Detected User-Agent: {user_agent}")
        # Return the constructed User-Agent string
        return user_agent

    except subprocess.CalledProcessError as e:
        # Log an error message if the command execution failed
        logging.error("Failed to get Chrome version: %s", e)
        # Return a fallback User-Agent string with "unknown" Chrome version
        return "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/unknown Safari/537.36"


if __name__ == "__main__":
    # Get the current Chrome User-Agent string by calling the function
    current_user_agent = get_chrome_user_agent()
    # Print the detected User-Agent string to the console
    print(f"Current Chrome User-Agent: {current_user_agent}")