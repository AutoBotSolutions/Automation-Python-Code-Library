## Me
python set table cell


## AI Assistant
Here's an approach you can use to create, manipulate, and set a value in a table cell without using pandas, instead relying on Python's built-in functionalities with lists to represent the table:

```python
# Example of a table represented as a list of lists
table = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Function to set a specified cell in the table
def set_table_cell(table, row, column, value):
    """
    Sets the value of a specific cell in the table.
    
    :param table: The table represented as a list of lists.
    :param row: The row index of the cell to update (0-based).
    :param column: The column index of the cell to update (0-based).
    :param value: The new value to set in the cell.
    """
    if row < len(table) and column < len(table[row]):
        table[row][column] = value
    else:
        raise IndexError("Row or column index out of range")

# Example usage: update a specific cell
set_table_cell(table, 1, 1, 28)  # Changes Alice's Age from 25 to 28

# Print updated table
for row in table:
    print(row)
```

### Output
```
['Name', 'Age', 'City']
['Alice', 28, 'New York']
['Bob', 30, 'Los Angeles']
['Charlie', 35, 'Chicago']
```

### Explanation
- **Table Representation:** The table is stored as a list of lists where each inner list represents a row, and each element in the row represents a cell.
- **Indexing:** Rows and columns are indexed starting from zero. To modify a specific cell, access it via `table[row][column]` and assign the new value.
- **Error Handling:** The function checks if the provided `row` and `column` indices are within bounds, and raises an exception if they're not.

This method works well for small to moderately sized tables, but for larger datasets or more advanced table-like operations, libraries like Pandas are more efficient.

