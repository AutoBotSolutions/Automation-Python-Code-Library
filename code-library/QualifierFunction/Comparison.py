## Me
python set a variable called 'comparison' set a comparison with the first value of 99 and the second value of 100 using conditions tell me witch one is grater.

## AI Assistant
Here's an example in Python to set a variable named `comparison` and determine which value is greater between 99 and 100:

```python
# Define the two values
value1 = 99
value2 = 100

# Compare the two values and set the result
if value1 > value2:
    comparison = f"{value1} is greater than {value2}"
elif value1 < value2:
    comparison = f"{value2} is greater than {value1}"
else:
    comparison = "Both values are equal"

# Output the result
print(comparison)
```

### Explanation:
1. The variables `value1` and `value2` store the values 99 and 100, respectively.
2. Using conditional statements (`if`, `elif`, `else`), the code compares the two values.
3. Based on the comparison:
   - If the first value is greater, it sets `comparison` to indicate so.
   - If the second value is greater, it sets `comparison` to indicate that.
   - If both values are equal, it states that.

In this case, `100 is greater than 99`.

