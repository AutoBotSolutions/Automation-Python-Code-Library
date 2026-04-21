# Sort Table.py

**Path:** `DataCommands/Sort Table.py`

**Automation Type:** General Automation
**Lines:** 111

## Purpose

Example table as a list of tuples Sort the table by the first column (id) Sort the table by the second column (name) Sort the table by the third column (age)

## Library Context

This script is part of the general automation library, providing utility functions for common automation tasks.

## Key Features

No specific features documented.

## Usage Pattern

Usage pattern not identified.

## Dependencies

No external dependencies identified.

## Function Descriptions

No function descriptions available.

## Functions

No functions defined in this script.

## Classes

No classes defined in this script.

## External APIs

No external API interactions identified.

## Code Examples

### Example Code

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

# Sort the table by the sec
```

