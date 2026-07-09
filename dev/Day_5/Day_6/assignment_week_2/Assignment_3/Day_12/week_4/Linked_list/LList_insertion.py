class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def traverse(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

# Empty list
head = None

# Insert nodes
head = insert_at_beginning(head, 30)
head = insert_at_beginning(head, 20)
head = insert_at_beginning(head, 10)
head = insert_at_beginning(head, 5)

traverse(head)