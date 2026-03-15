import pytest

from algorithms.searching.linear_search import linear_search
from algorithms.searching.binary_search import binary_search


class TestLinearSearch:
    def test_found_first(self):
        assert linear_search([1, 2, 3, 4, 5], 1) == 0

    def test_found_last(self):
        assert linear_search([1, 2, 3, 4, 5], 5) == 4

    def test_found_middle(self):
        assert linear_search([1, 2, 3, 4, 5], 3) == 2

    def test_not_found(self):
        assert linear_search([1, 2, 3], 99) == -1

    def test_empty_list(self):
        assert linear_search([], 1) == -1

    def test_duplicate_returns_first(self):
        assert linear_search([4, 4, 4], 4) == 0


class TestBinarySearch:
    def test_found_middle(self):
        assert binary_search([1, 2, 3, 4, 5], 3) == 2

    def test_found_first(self):
        assert binary_search([1, 2, 3, 4, 5], 1) == 0

    def test_found_last(self):
        assert binary_search([1, 2, 3, 4, 5], 5) == 4

    def test_not_found(self):
        assert binary_search([1, 2, 3, 4, 5], 99) == -1

    def test_empty_list(self):
        assert binary_search([], 1) == -1

    def test_single_element_found(self):
        assert binary_search([7], 7) == 0

    def test_single_element_not_found(self):
        assert binary_search([7], 1) == -1
