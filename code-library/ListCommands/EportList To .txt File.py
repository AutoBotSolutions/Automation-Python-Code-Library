# Sample list
my_list = ["apple", "banana", "cherry", "date", "fig"]

# Specify the file name
file_name = "output.txt"

# Open the file in write mode and save the list to it
with open(file_name, "w") as file:
    for item in my_list:
        file.write(f"{item}\n")  # Write each item on a new line

print(f"The list has been exported to {file_name}")

#////////////////////////////////////////////////////////////#
This Python script exports a list of strings (my_list) into a text file (output.txt). Each string in the list is written on a new line in the file. Here's what's happening, step by step:

Define the list:

my_list = ["apple", "banana", "cherry", "date", "fig"] is a list containing fruit names as strings.
Specify the file name:

file_name = "output.txt" specifies the name of the file in which the list will be saved.
Open the file in write mode:

with open(file_name, "w") as file: opens the file in write mode ("w"), which creates the file if it doesn't exist or overwrites it if it does.
Write each item to the file:

The for loop goes through each item in the my_list.
For every item, the line file.write(f"{item}\n") writes the string to the file, followed by a newline character (\n), ensuring each list item appears on a new line.
Print success message:

After the writing process is complete and the file is closed (automatically by the with statement), the success message print(f"The list has been exported to {file_name}") is displayed to confirm the operation.
Expected Output in output.txt
The content of the output.txt file after running the script will be:

apple
banana
cherry
date
fig
Additionally, the script will print:

The list has been exported to output.txt
This is a simple and effective way to save a Python list to a text file.
