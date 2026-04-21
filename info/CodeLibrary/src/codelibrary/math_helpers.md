# math_helpers.py

**Path:** `CodeLibrary/src/codelibrary/math_helpers.py`

**Automation Type:** HTTP Requests
**Lines:** 112

## Purpose

Mathematical computation helpers.

## Key Features

- Web API interaction

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `math`
- `typing.List`
- `typing.Tuple`
- `typing.Optional`

## Functions

### mean

**Parameters:** numbers

Calculate the arithmetic mean of a list of numbers.

### median

**Parameters:** numbers

Calculate the median of a list of numbers.

### mode

**Parameters:** numbers

Calculate the mode(s) of a list of numbers.

### standard_deviation

**Parameters:** numbers

Calculate the standard deviation of a list of numbers.

### percentile

**Parameters:** numbers, percentile

Calculate a specific percentile of a list of numbers.

### gcd

**Parameters:** a, b

Calculate the greatest common divisor of two integers.

### lcm

**Parameters:** a, b

Calculate the least common multiple of two integers.

### is_prime

**Parameters:** n

Check if a number is prime.

### fibonacci

**Parameters:** n

Generate the first n Fibonacci numbers.

### clamp

**Parameters:** value, min_val, max_val

Clamp a value between a minimum and maximum.

... and 1 more functions

## Code Examples

### mean

```python
def mean(numbers: List[float]) -> float:
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)
```

### median

```python
def median(numbers: List[float]) -> float:
    """Calculate the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (s
```

### mode

```python
def mode(numbers: List[float]) -> List[float]:
    """Calculate the mode(s) of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(fr
```

