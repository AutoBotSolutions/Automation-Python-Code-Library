## Me
python read file to variable

## AI Assistant
Here’s how you can read the contents of a file into a Python variable:

### Example:

```python
# Open the file in read mode and store its contents in a variable
with open("filename.txt", "r") as file:
    file_contents = file.read()

# Print the variable to verify the contents
print(file_contents)
```

### Explanation:
1. The `open()` function is used to open a file in the desired mode (`"r"` for read mode).
2. The `with` statement ensures the file is properly closed after the operation, even if an error occurs.
3. `file.read()` reads the entire contents of the file into the `file_contents` variable as a string.

Let me know if you’d like further clarification or help!

