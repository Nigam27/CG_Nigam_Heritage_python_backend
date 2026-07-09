class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_position(head, data, position):
    # Create a new node
    new_node = Node(data)

    # Insert at the beginning
    if position == 0:
        new_node.next = head
        return new_node

    # Traverse to the node before the desired position
    current = head
    for _ in range(position - 1):
        if current is None:
            raise IndexError("Position out of range")
        current = current.next

    # Check if position is valid
    if current is None:
        raise IndexError("Position out of range")

    # Insert the new node
    new_node.next = current.next
    current.next = new_node

    return head


def traverse(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Create linked list: 10 -> 20 -> 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Before insertion:")
traverse(head)

# Insert 25 at position 2
head = insert_at_position(head, 25, 2)

print("After insertion:")
traverse(head)