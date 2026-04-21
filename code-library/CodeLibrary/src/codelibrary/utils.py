"""
General utility functions.
"""

from typing import Any, Callable, List, Optional
import hashlib
import json


def flatten(nested_list: List[Any]) -> List[Any]:
    """Flatten a nested list structure."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks of specified size."""
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def safe_get(dictionary: dict, key: str, default: Any = None) -> Any:
    """Safely get a value from a dictionary with a default fallback."""
    return dictionary.get(key, default)


def memoize(func: Callable) -> Callable:
    """Simple memoization decorator for functions."""
    cache = {}
    
    def wrapper(*args, **kwargs):
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    return wrapper


def generate_hash(data: str, algorithm: str = "sha256") -> str:
    """Generate a hash of the given data using specified algorithm."""
    hash_func = getattr(hashlib, algorithm, hashlib.sha256)
    return hash_func(data.encode()).hexdigest()


def to_json(data: Any, indent: Optional[int] = 2) -> str:
    """Convert Python object to JSON string."""
    return json.dumps(data, indent=indent, default=str)


def from_json(json_str: str) -> Any:
    """Parse JSON string to Python object."""
    return json.loads(json_str)
