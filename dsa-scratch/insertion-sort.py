"""
Insertion Sort.
O(n^2) - worst
O(n) - best (nearly sorted)
"""

def insertion_sort(arr):
    """
    Build a sorted sub-array from left to right.
    For each new element, find its correct position by shifting right until we find where it fits — like sorting a hand of cards.
    
    O(n) on nearly-sorted data — only a few shifts needed.
    """
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]                        # element to place correctly
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]             # shift larger elements right
            j -= 1
        arr[j + 1] = key                    # drop key into correct slot
    return arr