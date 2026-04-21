"""
Tests for string_helpers module.
"""

import pytest
from codelibrary.string_helpers import (
    camel_to_snake,
    snake_to_camel,
    truncate,
    is_email,
    remove_extra_spaces,
    reverse_string,
    count_words,
)


def test_camel_to_snake():
    assert camel_to_snake("CamelCase") == "camel_case"
    assert camel_to_snake("myVariableName") == "my_variable_name"


def test_snake_to_camel():
    assert snake_to_camel("snake_case") == "SnakeCase"
    assert snake_to_camel("my_variable_name") == "MyVariableName"


def test_truncate():
    assert truncate("Hello World", 5) == "He..."
    assert truncate("Hi", 10) == "Hi"


def test_is_email():
    assert is_email("test@example.com") is True
    assert is_email("invalid-email") is False


def test_remove_extra_spaces():
    assert remove_extra_spaces("Hello    World") == "Hello World"
    assert remove_extra_spaces("  Test  ") == "Test"


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""


def test_count_words():
    assert count_words("Hello World") == 2
    assert count_words("One two three four") == 4
