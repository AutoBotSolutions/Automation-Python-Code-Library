## Me
python add item to list

## AI Assistant
To add an item to a list in Python, you can use the built-in method `append()`:

### Example:

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

### Explanation:
- `.append(item)` adds `item` to the end of the list.

Alternatively, to add multiple items, you can use `extend()`:

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

Or, to insert an item at a specific position, use `insert(index, item)`:

```python
my_list = [1, 2, 3]
my_list.insert(1, 4)  # Inserts 4 at index 1
print(my_list)  # Output: [1, 4, 2, 3]
```


