"""
Tests for datastructures module.
"""

import pytest
from codelibrary.datastructures import Stack, Queue, LinkedList


def test_stack():
    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.size() == 1


def test_queue():
    queue = Queue()
    assert queue.is_empty()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2
    assert queue.peek() == 1
    assert queue.dequeue() == 1
    assert queue.size() == 1


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
    assert ll.find(5) is False
