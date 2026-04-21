send SQL query



## Me
list of SQL Query commands

## AI Assistant
SQL is a standard language for managing relational databases and performing various operations on the data within. Below is a list of common SQL query commands with their purpose:

### **SQL Query Commands:**
1. **`SELECT`**  
   - Retrieves data from one or more tables.  
```textmate
SELECT column1, column2 FROM table_name;
```

2. **`INSERT INTO`**  
   - Adds new rows of data to a table.  
```textmate
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```

3. **`UPDATE`**  
   - Modifies existing records in a table.  
```textmate
UPDATE table_name SET column1 = value1 WHERE condition;
```

4. **`DELETE`**  
   - Deletes records from a table.  
```textmate
DELETE FROM table_name WHERE condition;
```

5. **`CREATE TABLE`**  
   - Creates a new table in the database.  
```textmate
CREATE TABLE table_name (column1 data_type, column2 data_type);
```

6. **`ALTER TABLE`**  
   - Modifies the structure of an existing table (e.g., add/drop/modify columns).  
```textmate
ALTER TABLE table_name ADD column_name data_type;
```

7. **`DROP TABLE`**  
   - Deletes a table (and its data) from the database.  
```textmate
DROP TABLE table_name;
```

8. **`CREATE DATABASE`**  
   - Creates a new database.  
```textmate
CREATE DATABASE database_name;
```

9. **`DROP DATABASE`**  
   - Deletes a database entirely.  
```textmate
DROP DATABASE database_name;
```

10. **`TRUNCATE TABLE`**  
    - Removes all records from a table (but keeps the structure intact).  
```textmate
TRUNCATE TABLE table_name;
```

11. **`SELECT INTO`**  
    - Copies data from one table into a new table.  
```textmate
SELECT * INTO new_table FROM old_table;
```

12. **`JOIN`**  
    - Combines rows from two or more tables based on a related column.  
    - Common types: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`.  
```textmate
SELECT columns FROM table1 INNER JOIN table2 ON table1.column = table2.column;
```

13. **`WHERE`**  
    - Adds a condition to filter the records returned by a query.  
```textmate
SELECT * FROM table_name WHERE condition;
```

14. **`GROUP BY`**  
    - Groups rows that have the same values into summary rows. Often used with aggregate functions (`SUM`, `COUNT`, etc.).  
```textmate
SELECT column, COUNT(*) FROM table_name GROUP BY column;
```

15. **`HAVING`**  
    - Filters grouped records (used with `GROUP BY`).  
```textmate
SELECT column, SUM(sales) FROM table_name GROUP BY column HAVING SUM(sales) > 1000;
```

16. **`ORDER BY`**  
    - Sorts the result set in ascending (`ASC`) or descending (`DESC`) order.  
```textmate
SELECT * FROM table_name ORDER BY column DESC;
```

17. **`LIMIT`**  
    - Restricts the number of rows returned in a query. (In some databases, this may be `TOP` or `FETCH`).  
```textmate
SELECT * FROM table_name LIMIT 10;
```

18. **`UNION`**  
    - Combines the results of two or more `SELECT` queries without duplicates.  
```textmate
SELECT column FROM table1 UNION SELECT column FROM table2;
```

19. **`INTERSECT`**  
    - Returns the common rows between two `SELECT` queries.  
```textmate
SELECT column FROM table1 INTERSECT SELECT column FROM table2;
```

20. **`EXCEPT` / `MINUS`**  
    - Returns the rows in the first query that are not in the second query.  
```textmate
SELECT column FROM table1 EXCEPT SELECT column FROM table2;
```

21. **`DISTINCT`**  
    - Returns unique values from a column.  
```textmate
SELECT DISTINCT column FROM table_name;
```

22. **Aggregate Functions**  
    - Performs calculations on a set of values:
      - `SUM()`: Adds numeric values.  
      - `AVG()`: Calculates the average.  
      - `COUNT()`: Counts rows.  
      - `MAX()`: Gets the maximum.  
      - `MIN()`: Gets the minimum.  
```textmate
SELECT COUNT(*) FROM table_name;
```

23. **`CREATE VIEW`**  
    - Creates a virtual table based on a `SELECT` query.   
```textmate
CREATE VIEW view_name AS SELECT column1, column2 FROM table_name;
```

24. **`DROP VIEW`**  
    - Removes a view from the database.  
```textmate
DROP VIEW view_name;
```

25. **`CASE` Statement**  
    - Provides conditional logic in a query.  
```textmate
SELECT column,
           CASE
               WHEN condition1 THEN result1
               WHEN condition2 THEN result2
               ELSE result3
           END AS alias_name
    FROM table_name;
```

Let me know if you'd like further explanation or examples for any of these commands!

