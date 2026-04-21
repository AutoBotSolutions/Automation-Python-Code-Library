# datastructures.py

**Path:** `CodeLibrary/src/codelibrary/datastructures.py`

**Lines:** 130
**Size:** 3670 bytes

## Description

Common data structure implementations.

## Imports

- `typing.Any`
- `typing.Optional`
- `typing.Iterator`

## Classes

### Stack

A simple stack implementation using a list.

**Methods:**
- `__init__`
- `push`
- `pop`
- `peek`
- `is_empty`
- `size`

### Queue

A simple queue implementation using a list.

**Methods:**
- `__init__`
- `enqueue`
- `dequeue`
- `peek`
- `is_empty`
- `size`

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
- `size`
- `__iter__`

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

### is_empty

**Parameters:** self

Check if the queue is empty.

### size

**Parameters:** self

Return the number of items in the queue.

### __init__

**Parameters:** self, data, next_node

### __init__

**Parameters:** self

### append

**Parameters:** self, data

Add an item to the end of the list.

... and 5 more functions

