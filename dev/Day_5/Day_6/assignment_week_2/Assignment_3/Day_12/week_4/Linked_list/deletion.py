class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_from_beginning(head):
    # Check if the list is empty
    if head is None:
        return None

    # Move head to the second node
    head = head.next

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

# Delete the first node
head = delete_from_beginning(head)

print("After deletion:")
traverse(head)