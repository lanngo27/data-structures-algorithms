

class ListNode:
    """
    The LinkedList uses ListNode objects to store added values.
    This class will not be tested by the grader.

    Attributes:
      obj: Any object that need to be stored.
      follower: A ListNode object that follows this (self) ListNode object
        in the linked list.
      predecessor: A ListNode object that precedes this (self) ListNode object
        in the linked list.
    """
    def __init__(self, obj):
        """Initialize a list node object with the value obj."""
        self.obj = obj
        self.follower = None
        self.predecessor = None

    def add_after(self, node):
        """Adds node 'node' as the follower of this node."""
        tmp = self.follower
        self.follower = node
        node.predecessor = self
        node.follower = tmp
        if tmp:
            tmp.predecessor = node

    def remove_after(self):
        """Removes the follower of this node."""
        if self.follower:
            self.follower = self.follower.follower
            if self.follower:
                self.follower.predecessor = self


class LinkedList:
    """
    An implementation of a doubly linked list that uses ListNode objects
    to represent nodes in the list. List indexes start from zero.

    The list contains one head and one tail guardian node with the values None.
    These can be used to check if the head or tail has been reached.
    The guardian nodes should not be included when counting the size of the list.
    """
    def __init__(self):
        """Initialize the linked list."""
        self.ListNode = ListNode
        self.head = self.ListNode(None)
        self.tail = self.ListNode(None)
        # An empty list should only have one head node followed by a tail node
        self.head.add_after(self.tail)
        self.size = 0

    def _get_at(self, n):
        """Return the node at position 'n'."""
        if 0<= n <= self.get_size():
            curr = self.head
            for i in range(n):
                curr = curr.follower
        return curr

    def add_first(self, obj):
        """Add the object 'obj' as the first node."""
        self.head.add_after(ListNode(obj))
        self.size+=1


    def add_last(self, obj):
        """Add the object 'obj' as the last node."""
        newN = ListNode(obj)
        tmp = self.tail.predecessor
        tmp.follower = newN
        newN.predecessor = tmp
        self.tail.predecessor = newN
        newN.follower = self.tail
        self.size+=1


    def add_position(self, n, obj):
        """Insert the object 'obj' as the 'n'th node."""
        newN = ListNode(obj)
        tmp = self._get_at(n)
        tmp.add_after(ListNode(obj))
        self.size += 1

    def remove_position(self, n):
        """Remove the node at the 'n'th position."""
        predecessor = self._get_at(n).predecessor
        if predecessor:
            predecessor.remove_after()
        self.size-=1

    def get_position(self, n):
        """Return the value of the node at the 'n'th position or None
        if there is no node at that position."""
        if self.size==0:
            return None
        node = self._get_at(n+1)
        return node.obj

    def get_size(self):
        """Return the number of objects in the list."""
        return self.size

