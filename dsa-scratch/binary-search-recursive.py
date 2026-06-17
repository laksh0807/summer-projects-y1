"""
Binary Search - Recursive Method
O(log n)
Prerequisite - List must be sorted.
"""

def binary_search(arr, target, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo > hi: 
        return -1
    mid = lo + (hi - lo) // 2   # avoids integer overflow
    if arr[mid] == target:   
        return mid
    elif arr[mid] < target:  
        return binary_search(arr, target, mid+1, hi)
    else:                     
        return binary_search(arr, target, lo, mid-1)


# Demonstration
a = [1, 3, 4, 6, 9]
idx = binary_search(a, 4)
print("The element 4 is present at index:", idx)