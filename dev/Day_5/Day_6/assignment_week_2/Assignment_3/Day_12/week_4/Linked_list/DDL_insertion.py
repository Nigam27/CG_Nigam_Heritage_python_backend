class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = DNode(data)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Link new node with old head
        new_node.next = self.head
        self.head.prev = new_node

        # Update head
        self.head = new_node

    # Traverse forward
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Traverse backward
    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Create a Doubly Linked List
dll = DoublyLinkedList()

# Initial list: 20 <-> 30
dll.insert_at_beginning(30)
dll.insert_at_beginning(20)

print("Before insertion:")
dll.traverse_forward()

# Insert 10 at the beginning
dll.insert_at_beginning(10)

print("After insertion:")
dll.traverse_forward()

print("Backward Traversal:")
dll.traverse_backward()