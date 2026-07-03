class Node:
    def __init__(self, val=None):
        self.val = val          
        self.next = None        
class SinglyLinkedList:
    def __init__(self):
        self.head = None    # Head points to the first node in the list
        
    def append(self, data):
        new_node = Node(data)      # Create a new node with the given value
        if not self.head:          # If the list is empty, set head to new node
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:   # Traverse to the last node
                current = current.next
            current.next = new_node           # Link the last node to the new node
    def traverse(self):
        if not self.head:
            print("Singly Linked List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()
    def insert_at(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            new_node.next = current
            if prev_node:
                prev_node.next = new_node
    def delete_head(self):
        if not self.head:
            print("Cannot delete. Singly Linked List is already empty")
        else:
            self.head = self.head.next  # The second node (or None) becomes the new head
    def delete(self, val):
        temp = self.head
        if temp and temp.val == val:
            self.head = temp.next
            return

        prev = None
        found = False

        while temp is not None:
            if temp.val == val:
                found = True
                break
            prev = temp
            temp = temp.next

        if found:
            prev.next = temp.next
        else:
            print("Node not found")
sll = SinglyLinkedList()

# Append nodes
sll.append(100)
sll.append(200)
sll.append(50)
sll.append(20)
sll.traverse()      # Output: 100 200 50 20

# Insert nodes
sll.insert_at(43, 0)      # Insert 43 at the beginning
sll.traverse()            # Output: 43 100 200 50 20

sll.insert_at(400, 3)     # Insert 400 at position 3
sll.traverse()            # Output: 43 100 200 400 50 20

# Delete head node
sll.delete_head()
sll.traverse()            # Output: 100 200 400 50 20

# Attempt to delete a non-existent node
sll.delete(2000)          # Value not found
sll.traverse()            # Output: 100 200 400 50 20 (unchanged)