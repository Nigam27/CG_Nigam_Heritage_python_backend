class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_by_value(head, value):
    # If the list is empty
    if head is None:
        return None

    # If the head node contains the value
    if head.data == value:
        return head.next

    # Traverse the list
    current = head
    while current.next is not None:
        # If the next node contains the value
        if current.next.data == value:
            # Skip the node to delete it
            current.next = current.next.next
            return head

        current = current.next

    # Value not found
    return head


def traverse(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Create linked list: 10 -> 20 -> 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Before deletion:")
traverse(head)

# Delete node with value 20
head = delete_by_value(head, 20)

print("After deletion:")
traverse(head)