## Me
python remove table row

## AI Assistant
To remove a table row without using the `pandas` library, you can work with raw Python data structures such as lists of lists. Below is an example that demonstrates how to remove a specific row from a table:

### Example Code
```python
# Sample table represented as a list of lists
table = [
    ["ID", "Name", "Age"],
    [1, "Alice", 30],
    [2, "Bob", 25],
    [3, "Charlie", 35]
]

# Function to remove a row by index
def remove_row(table, row_index):
    if 0 <= row_index < len(table):
        del table[row_index]
    else:
        print("Invalid row index")

# Remove a specific row (e.g., row with index 2, which is [2, "Bob", 25])
remove_row(table, 2)

# Print the updated table
for row in table:
    print(row)
```

### Output
```
['ID', 'Name', 'Age']
[1, 'Alice', 30]
[3, 'Charlie', 35]
```

### Explanation
1. **Table Representation**: 
   - The table is represented as a list of lists, where each inner list is a row.
   
2. **Removing a Row**:
   - Use the `del` keyword to remove the specified row from the list. The `row_index` is used to locate the row.
   - Ensure the `row_index` is valid to avoid `IndexError`.

3. **Iterate and Display**:
   - After removing the row, print out the updated table to check the results.

This method is simple and avoids the need for external libraries like `pandas`. It can work well for small-to-medium-sized tables stored in memory.

