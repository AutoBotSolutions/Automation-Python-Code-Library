"""
Tests for math_helpers module.
"""

import pytest
from codelibrary.math_helpers import (
    mean,
    median,
    standard_deviation,
    is_prime,
    fibonacci,
    clamp,
    lerp,
)


def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3.0
    assert mean([10, 20, 30]) == 20.0


def test_median():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4]) == 2.5


def test_standard_deviation():
    result = standard_deviation([1, 2, 3, 4, 5])
    assert abs(result - 1.5811) < 0.01


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(4) is False
    assert is_prime(1) is False


def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(1) == [0]
    assert fibonacci(0) == []


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-5, 0, 10) == 0
    assert clamp(15, 0, 10) == 10


def test_lerp():
    assert lerp(0, 10, 0.5) == 5.0
    assert lerp(0, 100, 0.25) == 25.0
