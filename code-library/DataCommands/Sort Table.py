Sorting a table in Python without relying on external libraries can be achieved using Python's built-in tools such as `sorted()` or custom sorting logic. Here's an example where you sort a table (list of lists or tuples) by a specific column:

### Example: Sorting a Table in Memory
```python
# Example table as a list of tuples
table = [
    (2, "Alice", 25),
    (1, "Charlie", 35),
    (3, "Bob", 30)
]

# Sort the table by the first column (id)
sorted_table = sorted(table, key=lambda row: row[0])
print("Sorted by ID:")
for row in sorted_table:
    print(row)

# Sort the table by the second column (name)
sorted_table = sorted(table, key=lambda row: row[1])
print("\nSorted by Name:")
for row in sorted_table:
    print(row)

# Sort the table by the third column (age)
sorted_table = sorted(table, key=lambda row: row[2])
print("\nSorted by Age:")
for row in sorted_table:
    print(row)
```

### Explanation:
1. **Table Representation:**
   - The table is represented as a list of tuples (or lists). Each element represents a row in the table.
   - Each tuple contains values for columns (e.g., ID, Name, Age).

2. **Sorting with `sorted()`:**
   - `sorted()` sorts iterables in Python.
   - Use the `key` argument to specify the column by which to sort. In this case, `row[0]` sorts by the first column (ID).
   - Sorting happens in ascending order by default. Pass `reverse=True` to sort in descending order.

3. **Output:**
   - The table is sorted and printed in the desired order.

---

### Interacting with an SQLite Table and Sorting

If you're using SQLite and want to sort the table while working with a database, you can use an `ORDER BY` query:

```python
import sqlite3

# Connect to an existing database
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# Create a table and insert sample data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# Insert sample data
cursor.executemany('''
    INSERT OR IGNORE INTO users (id, name, age) VALUES (?, ?, ?)
''', [
    (2, "Alice", 25),
    (1, "Charlie", 35),
    (3, "Bob", 30)
])
connection.commit()

# Sort the table by "id" in ascending order
cursor.execute("SELECT * FROM users ORDER BY id")
rows = cursor.fetchall()
print("\nSorted by ID:")
for row in rows:
    print(row)

# Sort the table by "name" in ascending order
cursor.execute("SELECT * FROM users ORDER BY name")
rows = cursor.fetchall()
print("\nSorted by Name:")
for row in rows:
    print(row)

# Sort the table by "age" in ascending order
cursor.execute("SELECT * FROM users ORDER BY age")
rows = cursor.fetchall()
print("\nSorted by Age:")
for row in rows:
    print(row)

connection.close()
```

### Explanation (SQLite Sorting):
1. **`ORDER BY` Clause**: 
   - Use `ORDER BY column_name` in the SQL query to sort a table based on a column.
   - Sorting is ascending by default; add `DESC` for descending order.
   
2. **Code Flow**:
   - The code fetches rows from the database after sorting them.
   - The sorting is handled by SQLite's query execution.

---

Both methods (in-memory and SQLite sorting) demonstrate how to sort a table without using external libraries. Let me know how you'd like to proceed!
