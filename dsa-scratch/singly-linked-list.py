class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    # Pointer to next node.

class SinglyLinkedList:

    """
    Singly linked list.

    Time complexities:
      prepend       O(1)  — redirect head pointer
      append        O(n)  — must walk to the tail first
      insert_at(i)  O(n)  — must walk to position i
      delete_at(i)  O(n)  — must walk to position i-1
      search        O(n)  — may need to scan all nodes
      reverse       O(n)  — one pass, three-pointer technique
      length        O(n)  — walk the whole list (O(1) if we track it)
    """

    def __init__(self):
        self.head = None
        self._size = 0

    def prepend(self, data):
        """ Add to front. O(1). """
        node = Node(data)               # creates a new Node object.
        node.next = self.head           # connects the new node's next pointer to the current self.head.
        self.head = node                # updates the self.head to point to the new node, making it the new first element.
        self._size += 1                 # increments the list's size counter by 1.

    def append(self, data):
        """ Add at end. O(n) - must walk to the tail. """
        new_node = Node(data)           # creates a new Node object.
        if not self.head:               # check if empty.
            self.head = new_node        # if yes, then new node become the head.
        else:
            curr = self.head            # if no, then curr is a new head pointer which will go till end.
            while curr.next:            # walk to the last node.
                curr = curr.next
            curr.next = new_node        # links the last nodes next pointer to new node.
        self._size += 1                 # increments the list's size counter by 1.

    def insert_at(self, index, data):
        """ Insert at a given 0-based index. O(n). """
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of range")
        if index == 0:
            return self.prepend(data)
        new_node = Node(data)           # creates a new Node object.
        trav = self.head                # start pointer trav at head.
        for _ in range(index - 1):      # loop this pointer index - 1 times so that it lands at node just before the insertion point.
            trav = trav.next            
        new_node.next = trav.next       # points the new nodes next pointer to the node that currently follows trav.
        trav.next = new_node            # redirects trav.next to the new node, sucessfully splicing into the list.
        self._size += 1                 # increments the list's size counter by 1.

    def delete_at(self, index):
        """ Remove node at index. O(n). """
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")
        if index == 0:
            self.head = self.head.next  # shifts the self.head forward by one node.
        else:
            trav = self.head            # trav pointer pointing to the head which will traverse till index - 1.
            for _ in range(index - 1):  # walk to node just before target.
                trav = trav.next
            trav.next = trav.next.next  # skip over the deleted node.
        self._size -= 1                 # decrements the list's size counter by 1.

    def search(self, target):
        """ Return index of first occurrence, or -1. O(n). """
        trav = self.head                # initialises pointer trav at beginning of the list.
        idx = 0                             
        while trav:                     # this loop traverses the trav pointer over the whole linked list.
            if trav.data == target:     
                return idx              # returning the index at which the target was found.
            trav = trav.next
            idx += 1
        return -1                       # return -1 if the target was not found in the linked list.
    
    def reverse(self):
        """
        Reverse the list in-place. O(n), O(1) space.
        Three-pointer technique: prev, curr, next_node.
        """
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next       # save before we overwrite
            curr.next = prev            # reverse the pointer
            prev = curr                 # move prev forward
            curr = next_node            # move curr forward
        self.head = prev                # prev is now the new head

    def length(self):
        return self._size

    def to_list(self):
        result, curr = [], self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def __repr__(self):
        return " -> ".join(str(x) for x in self.to_list()) + " -> None"


# Demonstration
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.insert_at(2, 99)
print(ll)                               # 0 -> 1 -> 99 -> 2 -> 3 -> None
ll.reverse()
print(ll)                               # 3 -> 2 -> 99 -> 1 -> 0 -> None