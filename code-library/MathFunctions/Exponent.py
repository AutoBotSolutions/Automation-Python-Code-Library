## Me
python code examples of using exponents

## AI Assistant
Here are some examples of using exponents in Python programming:

### Using the `**` Operator
Python provides the `**` operator to calculate the power of a number.

```python
# Basic usage
x = 2
y = 3
result = x ** y  # 2 raised to the power of 3
print(f"{x} raised to the power {y} is {result}")  # Output: 8
```

---

### Using the `pow()` Function
The built-in Python function `pow()` can also be used for exponentiation.

```python
# Using pow() function
base = 5
exponent = 3
result = pow(base, exponent)  # 5 raised to the power of 3
print(f"{base} raised to the power {exponent} is {result}")  # Output: 125
```

---

### Using `math.pow()`
The `math` module includes a `pow()` method for working with floating-point exponents.

```python
import math

# Using math.pow()
base = 4
exponent = 0.5  # Square root operation
result = math.pow(base, exponent)  # Equivalent to 4 ** 0.5
print(f"{base} raised to the power {exponent} is {result}")  # Output: 2.0
```

---

### Computing Negative Exponents
Negative exponents can be calculated to find the reciprocal.

```python
base = 2
exponent = -3
result = base ** exponent  # 2 raised to the power -3
print(f"{base} raised to the power {exponent} is {result}")  # Output: 0.125
```

---

### Combined Examples
1. **Custom Exponent Function:**
   You can implement your own exponentiation logic using loops.

```python
def custom_exponent(base, exponent):
       result = 1
       for _ in range(abs(exponent)):
           result *= base
       return result if exponent >= 0 else 1 / result

   print(custom_exponent(2, 3))   # Output: 8
   print(custom_exponent(2, -3))  # Output: 0.125
```

2. **Exponents in List Comprehensions:**

```python
numbers = [1, 2, 3, 4]
   squares = [x ** 2 for x in numbers]
   print(squares)  # Output: [1, 4, 9, 16]
```

3. **Exponents in Numpy (for Arrays):**
   If you are working with arrays, you can use NumPy.

```python
import numpy as np
   
   arr = np.array([1, 2, 3, 4])
   squared_arr = np.power(arr, 2)
   print(squared_arr)  # Output: [ 1  4  9 16]
```

These examples demonstrate different ways to use exponents, from simple syntax to specialized libraries like `math` and `numpy`. Let me know if you need further assistance!

