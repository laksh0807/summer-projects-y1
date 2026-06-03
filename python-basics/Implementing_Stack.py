"""
    Implementing the data structure STACK - using a python list.
    LIFO stack. All operations are O(1).
    
    push(item)   — add item to top
    pop()        — remove and return top item
    peek()       — return top item without removing
    is_empty()   — return True if stack has no items
    __len__()    — return number of items

    Code by - Laksh Maheshwari
"""

class Stack():

    def __init__(self):
        self._data = []     # internal list; _ signals "don't touch directly"
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._data.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek at an empty stack")
        return self._data[-1]   # last element without removing
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def __repr__(self):
        return f"Stack ({self._data} <- top)"