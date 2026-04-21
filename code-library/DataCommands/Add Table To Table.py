## Me
python add table to table without using external lib

## AI Assistant
To add the contents of one table to another in Python **without using external libraries**, you can accomplish this using plain Python lists (or dictionaries) to represent the tables. Here's an approach that demonstrates merging two tables:

### Example Code
```python
# Define the first table as a list of dictionaries (rows with column data)
table1 = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30}
]

# Define the second table in the same structure as the first
table2 = [
    {"id": 3, "name": "Charlie", "age": 35},
    {"id": 4, "name": "Diana", "age": 28}
]

# Append all rows from table2 to table1
for row in table2:
    table1.append(row)

# Print the merged table
print("Merged Table:")
for row in table1:
    print(row)
```

### Output
```
Merged Table:
{'id': 1, 'name': 'Alice', 'age': 25}
{'id': 2, 'name': 'Bob', 'age': 30}
{'id': 3, 'name': 'Charlie', 'age': 35}
{'id': 4, 'name': 'Diana', 'age': 28}
```

### Explanation
1. **Input Structure**: Both tables are represented as lists of rows (dictionaries). Each dictionary represents a single row with column headers as keys.
2. **Appending Data**: Use a simple `for` loop to copy all rows from one table (table2) to the other (table1).
3. **Safety**: Ensure both tables have the same column structure. If there are missing or additional columns, you might need to handle them accordingly.

This approach avoids using any external libraries like `pandas` and is effective for small-to-medium use cases. If you want advanced table manipulations, you can extend this idea or later consider external libraries.

