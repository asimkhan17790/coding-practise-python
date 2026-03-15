class Stack:
    """Last-In First-Out (LIFO) stack backed by a Python list.

    Time complexity for push/pop/peek: O(1)
    Space complexity: O(n)
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        """Push *item* onto the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item.

        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it.

        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek at an empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack contains no items."""
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)
