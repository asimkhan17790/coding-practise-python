def bubble_sort(arr):
    """Sort a list in ascending order using the bubble sort algorithm.

    Time complexity:  O(n^2) average and worst case, O(n) best case (already sorted)
    Space complexity: O(1)
    """
    arr = list(arr)
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
