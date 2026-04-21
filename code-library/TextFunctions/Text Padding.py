## Me
python text function text padding

## AI Assistant
In Python, you can perform text padding by using string methods like `.rjust()`, `.ljust()`, or `.center()` to align text, or by using string formatting with f-strings or the `.format()` method.

Here are some examples of how you can achieve text padding:

### Padding with `.ljust()`, `.rjust()`, and `.center()`
```python
# Left padding (right justify)
text = "Hello"
padded_text = text.rjust(10)  # Pad with spaces to make a string of width 10
print(f"'{padded_text}'")  # Output: '     Hello'

# Right padding (left justify)
padded_text = text.ljust(10)
print(f"'{padded_text}'")  # Output: 'Hello     '

# Centered padding
padded_text = text.center(10)
print(f"'{padded_text}'")  # Output: '  Hello   '
```

### Padding with a specific character
You can specify a character to pad with (other than spaces):
```python
text = "Hello"

# Right justify with `-`
padded_text = text.rjust(10, '-')
print(padded_text)  # Output: '-----Hello'

# Left justify with `-`
padded_text = text.ljust(10, '-')
print(padded_text)  # Output: 'Hello-----'

# Centered with `*`
padded_text = text.center(10, '*')
print(padded_text)  # Output: '**Hello***'
```

### Padding with f-strings or `.format()`
You can use formatting specifiers for padding:
```python
# Right padding
text = "Hello"
padded_text = f"{text:>10}"  # Right justify, width 10
print(f"'{padded_text}'")  # Output: '     Hello'

# Left padding
padded_text = f"{text:<10}"  # Left justify, width 10
print(f"'{padded_text}'")  # Output: 'Hello     '

# Center padding
padded_text = f"{text:^10}"  # Center justify, width 10
print(f"'{padded_text}'")  # Output: '  Hello   '
```

With `.format()`:
```python
# Example with .format()
padded_text = "{:>10}".format(text)  # Right justify
print(f"'{padded_text}'")  # Output: '     Hello'
```

### Use Cases
- **Right justify:** Useful for aligning numbers or text to the right in tables.
- **Left justify:** Often used when left-aligning labels or strings.
- **Center justify:** For centered text display, like headers in a console output.

Let me know if you'd like further clarification or usage examples!

