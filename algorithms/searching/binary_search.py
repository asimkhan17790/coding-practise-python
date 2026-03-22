def binary_search(arr, target):
    """Search for target in a sorted list using the binary search algorithm.

    Returns the index of the target if found, otherwise -1.
    The input list must be sorted in ascending order.

    Time complexity:  O(log n)
    Space complexity: O(1)
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
