import pytest

from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort

SORT_FUNCTIONS = [bubble_sort, merge_sort, quick_sort]


@pytest.mark.parametrize("sort_fn", SORT_FUNCTIONS)
class TestSortingAlgorithms:
    def test_sorted_list(self, sort_fn):
        assert sort_fn([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted_list(self, sort_fn):
        assert sort_fn([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_unsorted_list(self, sort_fn):
        assert sort_fn([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_single_element(self, sort_fn):
        assert sort_fn([42]) == [42]

    def test_empty_list(self, sort_fn):
        assert sort_fn([]) == []

    def test_duplicates(self, sort_fn):
        assert sort_fn([3, 3, 3]) == [3, 3, 3]

    def test_negative_numbers(self, sort_fn):
        assert sort_fn([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

    def test_mixed_negative_positive(self, sort_fn):
        assert sort_fn([3, -1, 0, -4, 2]) == [-4, -1, 0, 2, 3]

    def test_does_not_mutate_input(self, sort_fn):
        original = [3, 1, 2]
        sort_fn(original)
        assert original == [3, 1, 2]
