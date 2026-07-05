class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node
            new_node.prev = current

    def traverse_forward(self):
        current = self.head

        while current:
            print(current.val, end=" ")
            current = current.next

        print()

    def traverse_backward(self):
        if self.head is None:
            return

        current = self.head

        while current.next:
            current = current.next

        while current:
            print(current.val, end=" ")
            current = current.prev

        print()


# Create Doubly Linked List
dll = DoublyLinkedList()

# Append nodes
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)

print("Forward Traversal:")
dll.traverse_forward()

print("Backward Traversal:")
dll.traverse_backward()