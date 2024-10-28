def bubble_sort(arr):
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.

    Parameters:
    arr (list): List of integers to sort.

    Returns:
    list: Sorted list of integers.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    """
    Sorts a list of integers in ascending order using the quick sort algorithm.

    Parameters:
    arr (list): List of integers to sort.

    Returns:
    list: Sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def insertion_sort(arr):
    """
    Sorts a list of integers in ascending order using the insertion sort algorithm.

    Parameters:
    arr (list): List of integers to sort.

    Returns:
    list: Sorted list of integers.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
