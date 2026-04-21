## Me
python insert into table without using external lib

## AI Assistant
To insert data into a table using **Python** without relying on external libraries like `pymysql`, `sqlite3`, or `psycopg2`, you can still use the standard Python `sqlite3` module that comes built-in with Python. Here's an example of how to do this:

```python
# Example of inserting data into an SQLite table without external libraries

import sqlite3

# Connect to a database file (or create it if it doesn't exist)
connection = sqlite3.connect("example.db")  # Replace 'example.db' with your database file

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a sample table (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# Prepare data to insert
user_data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35)
]

# Insert data into the table
cursor.executemany('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', user_data)

# Commit the changes
connection.commit()

# Fetch and display inserted data to verify
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()
```

### Explanation:
1. **Standard `sqlite3` Module**: This is part of Python's standard library and can be used without installing external libraries.
2. **Creating a Table**: The `CREATE TABLE` query ensures the table exists before inserting data.
3. **Data Insertion**:
   - You use parameterized queries with `?` placeholders to avoid SQL injection.
   - `executemany()` is used to execute multiple inserts.
4. **Fetching Data**: Use the `SELECT` query to check the inserted data.
5. **Closing Connection**: Ensure you close the database connection to free resources.

Let me know if you need help modifying this for other database engines or further enhancements!

