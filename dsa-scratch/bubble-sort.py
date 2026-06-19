"""
Bubble Sort.
O(n^2) - time
O(1) - space
"""

def bubble_sort(arr):
    """
    Repeatedly swap adjacent elements that are out of order.
    After k passes, the k largest elements are in their final positions.
    Optimisation: if no swaps happened in a pass, the array is sorted — stop.
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swap_flag = False
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag = True
        if not swap_flag:
            break
    return arr