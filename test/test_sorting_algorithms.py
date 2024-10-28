from sort_lib.sorting_algorithms import bubble_sort, quick_sort, insertion_sort


def test_bubble_sort():
    assert bubble_sort([5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([2, 1, 3]) == [1, 2, 3]
    assert bubble_sort([5, -1, 3, 0]) == [-1, 0, 3, 5]


def test_quick_sort():
    assert quick_sort([5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8]
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([2, 1, 3]) == [1, 2, 3]
    assert quick_sort([5, -1, 3, 0]) == [-1, 0, 3, 5]


def test_insertion_sort():
    assert insertion_sort([5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8]
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([2, 1, 3]) == [1, 2, 3]
    assert insertion_sort([5, -1, 3, 0]) == [-1, 0, 3, 5]
