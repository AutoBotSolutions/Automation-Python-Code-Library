"""
Tests for utils module.
"""

import pytest
from codelibrary.utils import flatten, chunk_list, safe_get, memoize, generate_hash


def test_flatten():
    assert flatten([1, [2, [3, 4], 5]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_chunk_list():
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list([1, 2, 3], 5) == [[1, 2, 3]]


def test_safe_get():
    d = {"a": 1, "b": 2}
    assert safe_get(d, "a") == 1
    assert safe_get(d, "c", "default") == "default"


def test_memoize():
    call_count = 0
    
    @memoize
    def expensive_function(x):
        nonlocal call_count
        call_count += 1
        return x * 2
    
    assert expensive_function(5) == 10
    assert call_count == 1
    assert expensive_function(5) == 10
    assert call_count == 1  # Should not increment due to memoization


def test_generate_hash():
    hash1 = generate_hash("test")
    hash2 = generate_hash("test")
    assert hash1 == hash2
    assert hash1 != generate_hash("different")
