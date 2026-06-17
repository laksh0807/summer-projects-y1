class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    Doubly linked list.

    Time complexities:
      prepend       O(1)  — redirect head pointer, adjust prev of old head
      append        O(1)  — O(1) because tail pointer is kept
      insert_at(i)  O(n)  — must walk to position i (optimized by starting from head/tail)
      delete_at(i)  O(n)  — must walk to position i, node removal itself is O(1)
      search        O(n)  — scans nodes sequentially from the closest end
      reverse       O(n)  — one pass, swapping next and prev pointers
      length        O(1)  — tracked dynamically via self.size counter
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def length(self):
        """Returns the current size of the list in O(1) time."""
        return self.size

    def prepend(self, data):
        """Inserts data at the beginning of the list in O(1) time."""
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def append(self, data):
        """Inserts data at the end of the list in O(1) time."""
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def _get_node_at(self, index):
        """Helper to fetch a node at an index efficiently from head or tail."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        # Optimize: Start from tail if index is in the second half
        if index < self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - 1 - index):
                curr = curr.prev
        return curr

    def insert_at(self, index, data):
        """Inserts data at a specific index in O(n) time."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.prepend(data)
            return
        if index == self.size:
            self.append(data)
            return
            
        target = self._get_node_at(index)
        new_node = Node(data)
        
        new_node.prev = target.prev
        new_node.next = target
        target.prev.next = new_node
        target.prev = new_node
        self.size += 1

    def delete_at(self, index):
        """Deletes a node at a specific index in O(n) time."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
            
        target = self._get_node_at(index)
        
        if target.prev:
            target.prev.next = target.next
        else:
            self.head = target.next  # Target was head
            
        if target.next:
            target.next.prev = target.prev
        else:
            self.tail = target.prev  # Target was tail
            
        self.size -= 1
        return target.data

    def search(self, target_value):
        """Searches for a value and returns its index, or -1 if not found."""
        curr = self.head
        index = 0
        while curr:
            if curr.data == target_value:
                return index
            curr = curr.next
            index += 1
        return -1

    def reverse(self):
        """Reverses the list in place in O(n) time by swapping pointers."""
        curr = self.head
        self.tail = self.head  # The old head becomes the new tail
        
        temp = None
        while curr:
            # Swap next and prev pointers
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            # Move to the next node (which is now stored in curr.prev)
            curr = curr.prev
            
        if temp:
            self.head = temp.prev

    def display(self):
        """Utility to print the list structure."""
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("None <-> " + " <-> ".join(elements) + " <-> None")