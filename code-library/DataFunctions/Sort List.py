## Me
python sort list

## AI Assistant
To sort a list in Python, you can use either the `sorted()` function or the `sort()` method.

### Using `sorted()`  
The `sorted()` function returns a new sorted list and does not modify the original one.

```python
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)

print(sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]
print(numbers)         # Original list remains unchanged
```

If you want to sort in descending order, you can use the `reverse` argument:

```python
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # Output: [9, 6, 5, 5, 2, 1]
```

### Using `sort()`  
The `sort()` method modifies the list in place and does not return a new list.

```python
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()

print(numbers)  # Output: [1, 2, 5, 5, 6, 9]
```

To sort in descending order:

```python
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]
```

### Sorting with a Custom Key  
Both `sorted()` and `sort()` allow you to use a `key` argument to specify a custom sorting criterion. For example, if you have a list of tuples, and you want to sort by the second element:

```python
data = [(1, 2), (3, 1), (5, 0)]
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)  # Output: [(5, 0), (3, 1), (1, 2)]
```

The same can be done with `sort()`:

```python
data = [(1, 2), (3, 1), (5, 0)]
data.sort(key=lambda x: x[1])

print(data)  # Output: [(5, 0), (3, 1), (1, 2)]
```

If you need further specifics on sorting operations, feel free to ask!

