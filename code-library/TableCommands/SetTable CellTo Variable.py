set table cell to variable

## Me
set table cell to variable without using Pandas

## AI Assistant
To work with tables and set specific table cells to variables without using Pandas, you can use Python's built-in libraries, such as `csv` for CSV files. Here's an example of how you might achieve this:

### Example: Accessing a Specific Cell from a Table in CSV Format
```python
import csv

# Open the CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    table = list(reader)  # Convert the CSV data to a list of rows (table)

# Access a specific cell, for example, row 2, column 3 (0-based index)
row_index = 1  # 2nd row
col_index = 2  # 3rd column

cell_value = table[row_index][col_index]  # Get the value at the specified cell
print(f"Value at row {row_index + 1}, column {col_index + 1}: {cell_value}")
```

### Explanation:
1. **Open CSV File**:
   - Use `open('filename', 'r')` to open the file in read mode.
2. **Read Data**:
   - Read the file using `csv.reader` and convert it into a list of rows using `list(reader)`.
3. **Access a Cell**:
   - Use the row and column indices to access a specific cell. Python uses zero-based indexing.

### Example Input File (`data.csv`):
```
name,age,score
Alice,30,85
Bob,25,90
Charlie,35,95
```
Output for `row_index = 1` and `col_index = 2`:
```
Value at row 2, column 3: 90
```

If you're working directly with lists of lists (you've already loaded the data into memory), simply substitute in your table structure and indices.

Let me know if you need clarifications or additional examples!

