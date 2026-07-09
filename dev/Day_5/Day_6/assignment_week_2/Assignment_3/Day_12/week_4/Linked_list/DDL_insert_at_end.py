class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at the end
    def insert_at_end(self, data):
        new_node = DNode(data)

        # If the list is empty
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        # Link old tail with new node
        self.tail.next = new_node
        new_node.prev = self.tail

        # Update tail
        self.tail = new_node

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


# Create Doubly Linked List
dll = DoublyLinkedList()

# Insert nodes
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

print("Before insertion:")
dll.traverse_forward()

# Insert 40 at the end
dll.insert_at_end(40)

print("After insertion:")
dll.traverse_forward()

print("Backward Traversal:")
dll.traverse_backward()