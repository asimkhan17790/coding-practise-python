class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list with common operations.

    Supports append, prepend, delete, search, and iteration.
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node with *data* at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node with *data* at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Remove the first node whose data equals *data*.

        Returns True if a node was removed, False otherwise.
        """
        if self.head is None:
            return False
        if self.head.data == data:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def search(self, data):
        """Return True if *data* exists in the list, False otherwise."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def to_list(self):
        """Return all node values as a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
