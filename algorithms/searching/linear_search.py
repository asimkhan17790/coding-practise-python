def linear_search(arr, target):
    """Search for target in arr by checking each element sequentially.

    Returns the index of the target if found, otherwise -1.

    Time complexity:  O(n)
    Space complexity: O(1)
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
