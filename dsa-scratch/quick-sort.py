"""
Quick Sort.
O(nlogn) - average
O(n^2) - worst
"""

def quicksort(arr):
    """
    Pick a pivot. Partition into [< pivot] and [> pivot]. Recurse.
    
    Average case O(n log n): pivot divides array roughly in half.
    Worst case O(n²): pivot is always the smallest/largest element -> happens on already-sorted input with naive 'last element' pivot.
    
    Fix: random pivot selection -> expected O(n log n) always.
    In-place partitioning avoids the extra O(n) space of merge sort.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]                   # middle element as pivot (better than last)
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)