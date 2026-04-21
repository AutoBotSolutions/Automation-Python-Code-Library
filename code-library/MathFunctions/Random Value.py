## Me
python set random value to variable 

## AI Assistant
To set a random value to a variable in Python, you can use the `random` module. Here's an example of setting a random value to a variable:

```python
import random

# Generate a random integer between 1 and 100
random_variable = random.randint(1, 100)

print(random_variable)
```

### Explanation:
- **Importing `random`**: The `random` module provides functions for generating random numbers and working with probability distributions.
- **Using `random.randint(a, b)`**: This function generates a random integer N such that `a <= N <= b`.

---

### Other Common Random Values:
1. **Random Floating Point Number**:
```python
random_variable = random.random()  # Value between 0.0 and 1.0
```

2. **Random Choice from a List**:
```python
choices = ['apple', 'banana', 'cherry']
   random_variable = random.choice(choices)
```

3. **Random Value from a Range**:
```python
random_variable = random.uniform(10, 20)  # Random float between 10 and 20
```

4. **Random Boolean**:
```python
random_variable = random.choice([True, False])
```

Let me know if there's something more specific you need help with!

