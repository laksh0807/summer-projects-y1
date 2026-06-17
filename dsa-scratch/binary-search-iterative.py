"""
Binary Search - Iterative Method
O(log n)
Prerequisite - List must be sorted.
"""

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo)//2     # (lo+hi)//2 works but this one avoids integer overflow.
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# Demonstration
a = [1, 3, 4, 6, 9]
idx = binary_search(a, 4)
print("The element 4 is present at index:", idx)