"""
Mathematical computation helpers.
"""

import math
from typing import List, Tuple, Optional


def mean(numbers: List[float]) -> float:
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: List[float]) -> float:
    """Calculate the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def mode(numbers: List[float]) -> List[float]:
    """Calculate the mode(s) of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mode of empty list")
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    return [num for num, freq in frequency.items() if freq == max_freq]


def standard_deviation(numbers: List[float]) -> float:
    """Calculate the standard deviation of a list of numbers."""
    if len(numbers) < 2:
        raise ValueError("Cannot calculate standard deviation with less than 2 numbers")
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / (len(numbers) - 1)
    return math.sqrt(variance)


def percentile(numbers: List[float], percentile: float) -> float:
    """Calculate a specific percentile of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate percentile of empty list")
    if not 0 <= percentile <= 100:
        raise ValueError("Percentile must be between 0 and 100")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    index = (percentile / 100) * (n - 1)
    lower = math.floor(index)
    upper = math.ceil(index)
    if lower == upper:
        return sorted_numbers[lower]
    weight = index - lower
    return sorted_numbers[lower] * (1 - weight) + sorted_numbers[upper] * weight


def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of two integers."""
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Calculate the least common multiple of two integers."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> List[int]:
    """Generate the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])
    return result


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value between a minimum and maximum."""
    return max(min_val, min(max_val, value))


def lerp(start: float, end: float, t: float) -> float:
    """Linear interpolation between two values."""
    return start + (end - start) * t
