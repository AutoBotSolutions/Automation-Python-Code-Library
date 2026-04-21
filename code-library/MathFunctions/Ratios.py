## Me
python code examples of using ratios

## AI Assistant
Here are examples of Python code that utilize ratios. Ratios are often found in mathematical computations, data manipulations, or scenarios involving comparisons or proportions.

### Example 1: **Using Ratios in the `fractions` Module**
The `fractions.Fraction` can be used to create and operate with ratios in Python.

```python
from fractions import Fraction

# Representing ratios
ratio1 = Fraction(2, 5)  # 2/5
ratio2 = Fraction(3, 7)  # 3/7

# Arithmetic with ratios
sum_ratio = ratio1 + ratio2
difference_ratio = ratio1 - ratio2
product_ratio = ratio1 * ratio2
division_ratio = ratio1 / ratio2

print("Sum:", sum_ratio)
print("Difference:", difference_ratio)
print("Product:", product_ratio)
print("Division:", division_ratio)
```

### Example 2: **Scaling Values Using Ratios**
Ratios can be used as scaling factors to modify or adjust values, e.g., resizing geometrical shapes or elements.

```python
# Scaling rectangle dimensions using a ratio
original_width = 100
original_height = 50
scaling_ratio = 1.5  # Scale by 150%

new_width = original_width * scaling_ratio
new_height = original_height * scaling_ratio

print(f"Original Dimensions: {original_width}x{original_height}")
print(f"New Dimensions: {new_width}x{new_height}")
```

### Example 3: **Ratio Calculations for Proportions**
You can use ratios to calculate proportions, like the mix of ingredients.

```python
# Mixing ingredients based on ratios
flour_ratio = 3
water_ratio = 2
total_ratio = flour_ratio + water_ratio

# Calculate quantities for a total weight of 500 grams
total_weight = 500
flour_weight = (flour_ratio / total_ratio) * total_weight
water_weight = (water_ratio / total_ratio) * total_weight

print(f"Flour: {flour_weight}g")
print(f"Water: {water_weight}g")
```

### Example 4: **Sorting Based on Ratios**
If you work with datasets involving scores or metrics, they can be ranked based on their ratios.

```python
# Sorting students based on ratios of marks obtained to total marks
students = [
    {"name": "Alice", "marks_obtained": 80, "total_marks": 100},
    {"name": "Bob", "marks_obtained": 60, "total_marks": 100},
    {"name": "Charlie", "marks_obtained": 75, "total_marks": 90},
]

# Compute and sort based on their performance ratios
students.sort(key=lambda x: x["marks_obtained"] / x["total_marks"], reverse=True)

for student in students:
    ratio = student["marks_obtained"] / student["total_marks"]
    print(f"{student['name']}: {ratio:.2f}")
```

### Example 5: **Visualization of Ratios**
Visualizing ratios using a library like `matplotlib`.

```python
import matplotlib.pyplot as plt

# Plotting parts of a whole using ratios
categories = ['Category A', 'Category B', 'Category C']
values = [30, 50, 20]  # Values can represent parts of a ratio

plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title('Ratio Distribution')
plt.show()
```

These examples demonstrate how ratios are applied for mathematical computations, scaling, proportion calculations, rankings, and even visualizations.

