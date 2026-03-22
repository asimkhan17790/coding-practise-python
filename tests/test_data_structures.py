import pytest

from algorithms.data_structures.linked_list import LinkedList
from algorithms.data_structures.stack import Stack
from algorithms.data_structures.queue import Queue
from algorithms.data_structures.binary_search_tree import BinarySearchTree


class TestLinkedList:
    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.to_list() == [1, 2, 3]

    def test_prepend(self):
        ll = LinkedList()
        ll.append(2)
        ll.prepend(1)
        assert ll.to_list() == [1, 2]

    def test_delete_existing(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.delete(2) is True
        assert ll.to_list() == [1, 3]

    def test_delete_head(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        assert ll.delete(1) is True
        assert ll.to_list() == [2]

    def test_delete_not_found(self):
        ll = LinkedList()
        ll.append(1)
        assert ll.delete(99) is False

    def test_delete_from_empty(self):
        ll = LinkedList()
        assert ll.delete(1) is False

    def test_search_found(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        assert ll.search(2) is True

    def test_search_not_found(self):
        ll = LinkedList()
        ll.append(1)
        assert ll.search(99) is False

    def test_len(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        assert len(ll) == 2

    def test_iter(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        assert list(ll) == [10, 20]

    def test_empty_list(self):
        ll = LinkedList()
        assert ll.to_list() == []
        assert len(ll) == 0


class TestStack:
    def test_push_and_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        assert s.pop() == 1

    def test_peek(self):
        s = Stack()
        s.push(5)
        assert s.peek() == 5
        assert len(s) == 1

    def test_is_empty_initially(self):
        assert Stack().is_empty() is True

    def test_not_empty_after_push(self):
        s = Stack()
        s.push(1)
        assert s.is_empty() is False

    def test_pop_empty_raises(self):
        with pytest.raises(IndexError):
            Stack().pop()

    def test_peek_empty_raises(self):
        with pytest.raises(IndexError):
            Stack().peek()

    def test_len(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert len(s) == 2


class TestQueue:
    def test_enqueue_and_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        assert q.dequeue() == 2

    def test_peek(self):
        q = Queue()
        q.enqueue(10)
        assert q.peek() == 10
        assert len(q) == 1

    def test_is_empty_initially(self):
        assert Queue().is_empty() is True

    def test_not_empty_after_enqueue(self):
        q = Queue()
        q.enqueue(1)
        assert q.is_empty() is False

    def test_dequeue_empty_raises(self):
        with pytest.raises(IndexError):
            Queue().dequeue()

    def test_peek_empty_raises(self):
        with pytest.raises(IndexError):
            Queue().peek()

    def test_len(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert len(q) == 2


class TestBinarySearchTree:
    def _build_bst(self):
        bst = BinarySearchTree()
        for v in [5, 3, 7, 1, 4, 6, 8]:
            bst.insert(v)
        return bst

    def test_search_existing(self):
        bst = self._build_bst()
        assert bst.search(4) is True

    def test_search_missing(self):
        bst = self._build_bst()
        assert bst.search(99) is False

    def test_search_empty(self):
        assert BinarySearchTree().search(1) is False

    def test_inorder_is_sorted(self):
        bst = self._build_bst()
        assert bst.inorder() == [1, 3, 4, 5, 6, 7, 8]

    def test_preorder(self):
        bst = self._build_bst()
        assert bst.preorder() == [5, 3, 1, 4, 7, 6, 8]

    def test_postorder(self):
        bst = self._build_bst()
        assert bst.postorder() == [1, 4, 3, 6, 8, 7, 5]

    def test_duplicate_insert_ignored(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(5)
        assert bst.inorder() == [5]

    def test_single_node(self):
        bst = BinarySearchTree()
        bst.insert(42)
        assert bst.inorder() == [42]
        assert bst.search(42) is True
