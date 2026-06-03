"""
    Implementing the data structure QUEUE - using a python list.
    FIFO queue. All operations are O(1).
    
    enqueue(item) — add to back
    dequeue()     — remove from front
    front()       — peek at front without removing
    is_empty()    — True if empty
    __len__()     — number of items

    Code by - Laksh Maheshwari
"""
from collections import deque

class Queue():

    def __init__(self):
        self._data = deque()    # deque, not a plain list, list.pop(0) is O(n), deque.popleft() is O(1)

    def enqueue(self, item):
        self._data.append(item) # add to the right end
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._data.popleft()
    
    def front(self):
        if self.is_empty():
            raise IndexError("from of an empty queue")
        return self._data[0]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def __repr__(self):
        return f"Queue (front -> {list(self._data)})"