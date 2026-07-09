class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_end(head, data):
    # Create a new node
    new_node = Node(data)

    # If the linked list is empty
    if head is None:
        return new_node

    # Traverse to the last node
    current = head
    while current.next is not None:
        current = current.next

    # Link the last node to the new node
    current.next = new_node

    return head


def traverse(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Create the initial linked list: 10 -> 20 -> 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Before insertion:")
traverse(head)

# Insert 40 at the end
head = insert_at_end(head, 40)

print("After insertion:")
traverse(head)