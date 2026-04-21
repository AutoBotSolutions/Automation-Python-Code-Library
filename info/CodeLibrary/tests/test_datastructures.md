# test_datastructures.py

**Path:** `CodeLibrary/tests/test_datastructures.py`

**Automation Type:** General Automation
**Lines:** 42

## Purpose

Tests for datastructures module.

## Usage Pattern

Function-based - Provides reusable functions

## Dependencies

- `pytest`
- `codelibrary.datastructures.Stack`
- `codelibrary.datastructures.Queue`
- `codelibrary.datastructures.LinkedList`

## Functions

### test_stack

### test_queue

### test_linked_list

## Code Examples

### test_stack

```python
def test_stack():
    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.size() == 1
```

### test_queue

```python
def test_queue():
    queue = Queue()
    assert queue.is_empty()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2
    assert queue.peek() == 1
    assert queue.dequeue() == 1
    assert queue.size() == 1
```

### test_linked_list

```python
def test_linked_list():
    ll = LinkedList()
    assert ll.size() == 0
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.size() == 3
    assert ll.to_list() == [1, 2, 3]
    ll.prepend(0)
    assert ll.to_list() == [0, 1, 2, 3]
    assert ll.find(2) is True
    assert ll.find(5) is F
```

