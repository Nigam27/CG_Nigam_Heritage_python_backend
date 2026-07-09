class DNode:
 def __init__(self, data):
    self.data = data
    self.next = None # Pointer to next node
    self.prev = None # Pointer to previous node (NEW!)
class DoublyLinkedList:
 def __init__(self):
    self.head = None
    self.tail = None # We also track TAIL for O(1) end insertion