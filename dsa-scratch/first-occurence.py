"""
Using binary search to find the first occurence of an element in a list of elements.
O(log n)
Prerequisite - List must be sorted.
"""

def first_occurence(arr, target):
    lo, hi, result = 0, len(arr) - 1, -1
    while lo<=hi:
        mid = lo + (hi-lo)//2
        if arr[mid] == target:
            result = mid            # We record this but keep searching left.
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result