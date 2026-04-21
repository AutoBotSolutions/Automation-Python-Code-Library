code an if statement with all available conditions

## Me
code an if statement with all available conditions

## AI Assistant
Here is an example of an `if` statement in Python that includes all basic available conditions (equality, inequality, greater than, less than, greater than or equal to, less than or equal to, membership, identity, and logical operations):

```python
# Variables for demonstration
a = 5
b = 10
c = None
my_list = [1, 2, 3, 4, 5]

# If statement with all conditions
if (a == 5                # Equality check
    and b != 5            # Inequality check
    and b > a             # Greater than check
    and a < b             # Less than check
    and b >= 10           # Greater than or equal check
    and a <= 5            # Less than or equal check
    and 5 in my_list      # Membership check
    and c is None         # Identity check (None)
    and a is not None     # Identity check (not None)
    and not (b < a)       # Logical NOT (negation)
    and (a < b or b == 10) # Logical OR
):
    print("All conditions are met!")
else:
    print("One or more conditions are not met.")
```

### Explanation of the Conditions:
1. **Equality (`==`)**: Checks if two values are equal.
2. **Inequality (`!=`)**: Checks if two values are not equal.
3. **Greater than (`>`)**: Checks if one value is greater than another.
4. **Less than (`<`)**: Checks if one value is less than another.
5. **Greater than or equal (`>=`)**: Checks if one value is greater than or equal to another.
6. **Less than or equal (`<=`)**: Checks if one value is less than or equal to another.
7. **Membership (`in`)**: Checks if a value is in a sequence (like a list, tuple, or string).
8. **Identity (`is`)**: Checks if two references point to the same object.
9. **Logical NOT (`not`)**: Negates a condition.
10. **Logical OR (`or`)**: Evaluates to `True` if at least one condition is `True`.
11. **Logical AND (`and`)**: All conditions must be `True` for the statement to execute.

This example combines all these conditions into one cohesive block, although in practical situations, you'd likely use only the conditions relevant to your logic.

