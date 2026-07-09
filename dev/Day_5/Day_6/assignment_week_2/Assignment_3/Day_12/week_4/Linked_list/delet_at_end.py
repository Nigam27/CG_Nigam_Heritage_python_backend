class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_from_end(head):
    # Check if the list is empty
    if head is None:
        return None

    # If there is only one node
    if head.next is None:
        return None

    # Traverse to the second-last node
    current = head
    while current.next.next is not None:
        current = current.next

    # Remove the last node
    current.next = None

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

# Delete the last node
head = delete_from_end(head)

print("After deletion:")
traverse(head)