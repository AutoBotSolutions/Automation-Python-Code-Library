"""
Common data structure implementations.
"""

from typing import Any, Optional, Iterator


class Stack:
    """A simple stack implementation using a list."""
    
    def __init__(self):
        self._items: list = []
    
    def push(self, item: Any) -> None:
        """Push an item onto the stack."""
        self._items.append(item)
    
    def pop(self) -> Any:
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> Any:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)


class Queue:
    """A simple queue implementation using a list."""
    
    def __init__(self):
        self._items: list = []
    
    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue."""
        self._items.append(item)
    
    def dequeue(self) -> Any:
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)
    
    def peek(self) -> Any:
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self._items)


class ListNode:
    """A node for a linked list."""
    
    def __init__(self, data: Any, next_node: Optional['ListNode'] = None):
        self.data = data
        self.next = next_node


class LinkedList:
    """A simple singly linked list implementation."""
    
    def __init__(self):
        self.head: Optional[ListNode] = None
        self._size = 0
    
    def append(self, data: Any) -> None:
        """Add an item to the end of the list."""
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
    
    def prepend(self, data: Any) -> None:
        """Add an item to the beginning of the list."""
        new_node = ListNode(data, self.head)
        self.head = new_node
        self._size += 1
    
    def find(self, data: Any) -> bool:
        """Check if an item exists in the list."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def to_list(self) -> list:
        """Convert the linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def size(self) -> int:
        """Return the number of items in the list."""
        return self._size
    
    def __iter__(self) -> Iterator[Any]:
        """Iterate over the linked list."""
        current = self.head
        while current:
            yield current.data
            current = current.next
