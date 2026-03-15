from collections import deque


class Queue:
    """First-In First-Out (FIFO) queue backed by collections.deque.

    Time complexity for enqueue/dequeue/peek: O(1)
    Space complexity: O(n)
    """

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Add *item* to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the front item.

        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._items.popleft()

    def peek(self):
        """Return the front item without removing it.

        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek at an empty queue")
        return self._items[0]

    def is_empty(self):
        """Return True if the queue contains no items."""
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)
