import os  # Importing the os module for directory and file operations
import inspect  # Importing the inspect module to inspect objects, such as checking if something is a module


def list_project_files(directory, extensions=('.py',)):
    """
    Lists all project files with specified extensions in a given directory.
    """
    project_files = []  # Initialize an empty list to store project file paths
    for root, _, files in os.walk(directory):  # Walk through the directory tree
        for file in files:  # Loop through files in the current directory
            if file.endswith(extensions):  # Check if the file has the desired extension
                project_files.append(os.path.join(root, file))  # Add the file path to the list
    return project_files  # Return the list of project file paths


def extract_variables_from_file(file_path):
    """
    Extracts global variables from a Python file.
    """
    variables = {}  # Initialize an empty dictionary to store the variables
    with open(file_path, 'r') as file:  # Open the file in read mode
        code = compile(file.read(), file_path, 'exec')  # Compile the file content to bytecode
        namespace = {}  # Create an empty dictionary to act as the execution namespace
        exec(code, namespace)  # Execute the compiled code within the namespace
        for key, value in namespace.items():  # Iterate through the items in the namespace
            # Add only top-level global variables that are not internal (__*) or modules
            if not key.startswith("__") and not inspect.ismodule(value):
                variables[key] = value  # Add the variable name and value to the dictionary
    return variables  # Return the dictionary of extracted variables


def connect_to_database(database_url):
    """
    Connect to a database and retrieve table list. Placeholder for actual DB implementation.
    """
    # Example implementation for modern frameworks like sqlite or SQLAlchemy
    import sqlite3  # Import sqlite3 for handling SQLite database connections
    tables = []  # Initialize an empty list to store table names
    try:
        conn = sqlite3.connect(database_url)  # Connect to the SQLite database
        cursor = conn.cursor()  # Create a cursor object to execute SQL queries
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")  # Query for table names
        tables = [row[0] for row in cursor.fetchall()]  # Extract table names from query result
        conn.close()  # Close the database connection
    except Exception as e:  # Catch any exceptions that occur
        print(f"Error fetching tables from database: {e}")  # Print the error message
    return tables  # Return the list of table names


def main():
    """
    Main driver function of the script.
    """
    # Step 1: List all project files
    project_directory = os.path.dirname(os.path.abspath(__file__))  # Get the current script directory
    print(f"Scanning project directory: {project_directory}...")  # Print the directory being scanned
    project_files = list_project_files(project_directory)  # Get all project files in the directory

    # Step 2: Extract global variables
    all_variables = {}  # Initialize a dictionary to store variables from all files
    for file_path in project_files:  # Iterate over all project files
        try:
            variables = extract_variables_from_file(file_path)  # Extract global variables from the file
            all_variables[file_path] = variables  # Store the variables, keyed by file path
        except Exception as e:  # Catch any exceptions that occur during variable extraction
            print(f"Error extracting variables from {file_path}: {e}")  # Print the error message

    print("\n=== Global Variables Found ===")  # Display a header for the global variables section
    for file, variables in all_variables.items():  # Iterate over files and their variables
        print(f"\nFile: {file}")  # Print the file name
        for var_name, value in variables.items():  # Iterate over the variables in the file
            print(f"  - {var_name}: {value}")  # Print the variable name and value

    # Example Database Tables Retrieval
    print("\n=== Database Tables ===")  # Display a header for the database tables section
    database_url = 'your_database.db'  # Specify the database connection string or file
    tables = connect_to_database(database_url)  # Fetch the list of database tables
    for table in tables:  # Iterate over the table names
        print(f"  - {table}")  # Print each table name


if __name__ == "__main__":  # Check if the script is being run directly
    main()  # Call the main function

