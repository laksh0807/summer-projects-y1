"""
Merge Sort.
O(nlogn) - time
O(n) - space
"""

def merge_sort(arr):
    """
    Divide and conquer.
    Split the array in half recursively until size 1.
    Merge sorted halves back together.
    
    Recursion tree proof of O(n log n):
    - Level 0: 1 call on n elements          -> O(n) merge work
    - Level 1: 2 calls on n/2 elements       -> O(n) merge work total
    - Level 2: 4 calls on n/4 elements       -> O(n) merge work total
    - ...there are log₂(n) levels...
    - Total: O(n) x log n levels = O(n log n)
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return twoway_merge(left, right)

def twoway_merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]);  i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result