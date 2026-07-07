class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def search(head, target):
    current = head
    position = 0

    while current is not None:
        if current.data == target:
            return f"Found {target} at position {position}"

        current = current.next
        position += 1

    return f"{target} not found in the list"


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

print("Linked List:")
traverse(head)

# Search for elements
print(search(head, 20))
print(search(head, 99))