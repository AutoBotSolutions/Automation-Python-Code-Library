Open file dialog to select .csv file and load file into a table 
with a delimiter of (':') and output result to console
#///////////////////////////////////////////////////////////////#

import tkinter as tk
from tkinter import filedialog
import csv


def open_file_and_load():
    # Create a file dialog to select a .csv file
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename(
        title="Select a CSV File",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
    )

    if not file_path:
        print("No file selected.")
        return

    print(f"Selected file: {file_path}")

    # Read the CSV file using csv.reader with ':' as delimiter
    try:
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=':')
            for row in csv_reader:
                print(row)  # Output each row to the console
    except Exception as e:
        print(f"Error reading the file: {e}")


if __name__ == "__main__":
    open_file_and_load()

#///////////////////////////////////////////////////////////////#

Explanation:

Import necessary modules:

tkinter for creating the file dialog.
filedialog from tkinter specifically for the askopenfilename function.
csv for reading and parsing CSV files.
open_file_and_load() function:

Create and hide the main Tkinter window:
root = tk.Tk() creates the main Tkinter window. This is necessary for using filedialog.
root.withdraw() hides this window because we only want the file dialog to be visible.
Open the file dialog:
filedialog.askopenfilename(...) displays a file selection dialog to the user.
title specifies the title of the dialog window.
filetypes is a tuple of tuples that defines the types of files the user can select in the dialog. It's a filter based on file extensions.
Handle the file path:
It checks if the user selected a file (i.e., file_path is not empty).
If no file was selected, it prints a message and returns.
Otherwise, it prints the selected file path to the console.
Read the CSV file:
It uses a try...except block to handle potential errors during file reading.
with open(file_path, "r") as csv_file: opens the selected file in read mode ("r"). The with statement ensures the file is properly closed even if errors occur.
csv.reader(csv_file, delimiter=':') creates a csv_reader object. Crucially, delimiter=':' tells the reader that fields in the CSV are separated by colons (:) instead of the default commas (,).
The code then iterates through each row in the csv_reader:
for row in csv_reader:
print(row) prints each row to the console. Each row is a list of strings, where each string is a field separated by the colon.
Handle errors:
The except Exception as e: block catches any errors that might occur during file reading (e.g., file not found, invalid CSV format).
It prints an error message including the specific exception that occurred.
if __name__ == "__main__": block:

This is a standard Python idiom. It ensures that the open_file_and_load() function is only called when the script is run directly (not when it's imported as a module into another script).
open_file_and_load() is called, which starts the process of opening the file dialog and reading the CSV file.
How to run the code:

Save the code as a Python file (e.g., csv_reader.py).

Create a sample CSV file (e.g., my_data.csv) with colons as delimiters. For example:

field1:field2:field3
value1:value2:value3
another:row:ofdata
Run the script from your terminal: python csv_reader.py

A file dialog will appear. Select the CSV file you created. The script will then print the contents of the CSV file, split by colons, to your console. If you have the example my_data.csv file, the output will be:

Selected file: /path/to/your/my_data.csv
['field1', 'field2', 'field3']
['value1', 'value2', 'value3']
['another', 'row', 'ofdata']
(Replace /path/to/your/my_data.csv with the actual path to the file on your system)
