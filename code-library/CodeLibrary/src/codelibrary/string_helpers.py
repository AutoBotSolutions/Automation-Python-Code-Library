"""
String manipulation and validation utilities.
"""

import re
from typing import List, Optional


def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_to_camel(name: str) -> str:
    """Convert snake_case to CamelCase."""
    components = name.split('_')
    return ''.join(x.title() for x in components)


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to a maximum length with optional suffix."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def is_email(email: str) -> bool:
    """Validate if a string is a valid email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_url(url: str) -> bool:
    """Validate if a string is a valid URL format."""
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))


def remove_extra_spaces(text: str) -> str:
    """Remove extra whitespace from a string."""
    return ' '.join(text.split())


def reverse_string(text: str) -> str:
    """Reverse a string."""
    return text[::-1]


def count_words(text: str) -> int:
    """Count the number of words in a string."""
    return len(text.split())


def extract_numbers(text: str) -> List[str]:
    """Extract all numbers from a string."""
    return re.findall(r'\d+', text)


def mask_string(text: str, visible_chars: int = 4, mask_char: str = "*") -> str:
    """Mask a string showing only the first and last few characters."""
    if len(text) <= visible_chars * 2:
        return mask_char * len(text)
    return text[:visible_chars] + mask_char * (len(text) - visible_chars * 2) + text[-visible_chars:]


def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')
