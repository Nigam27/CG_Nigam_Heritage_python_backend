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

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # Delete a node by value
    def delete_node(self, data):
        current = self.head

        while current is not None:

            # Node found
            if current.data == data:

                # Update previous node's next pointer
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    # Deleting the head node
                    self.head = current.next

                # Update next node's prev pointer
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    # Deleting the tail node
                    self.tail = current.prev

                print(f"{data} deleted successfully.")
                return

            current = current.next

        print(f"{data} not found.")

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


# ---------------- Driver Code ----------------

dll = DoublyLinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

print("Before deletion:")
dll.traverse_forward()

dll.delete_node(20)

print("After deletion:")
dll.traverse_forward()

print("Backward Traversal:")
dll.traverse_backward()