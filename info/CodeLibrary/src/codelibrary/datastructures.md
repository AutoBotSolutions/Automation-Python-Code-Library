# datastructures.py

**Path:** `CodeLibrary/src/codelibrary/datastructures.py`

**Automation Type:** General Automation
**Lines:** 130

## Purpose

Common data structure implementations.

## Library Context

This script is part of the general automation library, providing utility functions for common automation tasks.

## Usage Pattern

Object-oriented - Provides classes and methods

## Dependencies

- `typing.Any`
- `typing.Optional`
- `typing.Iterator`

## Function Descriptions

- __init__ - Parameters: self. Performs a specific operation.
- push - Parameters: self, item. Performs a specific operation.
- pop - Parameters: self. Performs a specific operation.
- peek - Parameters: self. Performs a specific operation.
- is_empty - Parameters: self. Performs a specific operation.

## Functions

### __init__

**Parameters:** self

### push

**Parameters:** self, item

Push an item onto the stack.

### pop

**Parameters:** self

Remove and return the top item from the stack.

### peek

**Parameters:** self

Return the top item without removing it.

### is_empty

**Parameters:** self

Check if the stack is empty.

### size

**Parameters:** self

Return the number of items in the stack.

### __init__

**Parameters:** self

### enqueue

**Parameters:** self, item

Add an item to the back of the queue.

### dequeue

**Parameters:** self

Remove and return the front item from the queue.

### peek

**Parameters:** self

Return the front item without removing it.

... and 10 more functions

## Classes

### Stack

A simple stack implementation using a list.

**Methods:**
- `__init__`
- `push`
- `pop`
- `peek`
- `is_empty`
- ... and 1 more

### Queue

A simple queue implementation using a list.

**Methods:**
- `__init__`
- `enqueue`
- `dequeue`
- `peek`
- `is_empty`
- ... and 1 more

### ListNode

A node for a linked list.

**Methods:**
- `__init__`

### LinkedList

A simple singly linked list implementation.

**Methods:**
- `__init__`
- `append`
- `prepend`
- `find`
- `to_list`
- ... and 2 more

## Code Examples

### __init__

```python
def __init__(self):
        self._items: list = []
```

### push

```python
def push(self, item: Any) -> None:
        """Push an item onto the stack."""
        self._items.append(item)
```

### pop

```python
def pop(self) -> Any:
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
```

### peek

```python
def peek(self) -> Any:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
```

### is_empty

```python
def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0
```

