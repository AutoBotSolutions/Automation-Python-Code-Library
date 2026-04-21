If you'd like to create a table from a file without using `pandas`, you can use built-in Python libraries or other lightweight libraries, depending on the type of file you're working with. Below, I'll demonstrate how to create an SQL table from a CSV file using only Python's built-in libraries and the `sqlite3` library.
### Example: Creating a Table from a CSV File (Without Pandas)


import csv
import sqlite3

# File to process
file_name = "your_file.csv"

# Establish a database connection
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# Read the CSV file
with open(file_name, "r") as file:
    csv_reader = csv.reader(file)

    # Extract header (first line of CSV)
    headers = next(csv_reader)
    # Create a SQL "CREATE TABLE" statement dynamically
    create_table_query = f"CREATE TABLE my_table ({', '.join([header + ' TEXT' for header in headers])})"
    cursor.execute(create_table_query)

    # Insert the rows
    for row in csv_reader:
        placeholders = ", ".join(["?"] * len(row))
        insert_query = f"INSERT INTO my_table VALUES ({placeholders})"
        cursor.execute(insert_query, row)

# Commit changes and close connection
connection.commit()
connection.close()

print("Table created successfully.")

#////////////////////////////////////////////////////////#


### How It Works:
1. **Reading the CSV File**:
    - The `csv` module reads the contents of the file.
    - The first line of the CSV is extracted for use as column names in the table.

2. **Creating the SQL Table**:
    - The column names are dynamically included in the `CREATE TABLE` statement.
    - All columns are set as `TEXT` type for simplicity. Adjust the column data types if needed.

3. **Inserting Rows**:
    - Each subsequent row in the CSV is inserted into the table using a parameterized `INSERT` query.

4. **Saving the Table**:
    - Changes are saved to the database using `commit`, and the connection is closed properly.

### Example Input (`your_file.csv`):
``` csv
name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
```
### Example: SQLite Table Result (`my_table`):
If you query the table (e.g., via `SELECT * FROM my_table;`), you’d get:

| name | age | city |
| --- | --- | --- |
| Alice | 30 | New York |
| Bob | 25 | Los Angeles |
| Charlie | 35 | Chicago |
If you are working with another file format (e.g., JSON, XML, or others), let me know, and I can adapt this approach!

