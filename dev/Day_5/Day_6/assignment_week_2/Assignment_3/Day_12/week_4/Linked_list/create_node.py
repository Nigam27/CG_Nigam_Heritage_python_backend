class Node:
 def __init__(self, data):
    self.data = data # Store the value
    self.next = None # Pointer to next node (default: None)
# Creating nodes
node1 = Node(10) # Node holds value 10
node2 = Node(20) # Node holds value 20
node3 = Node(30) # Node holds value 30
# Output: Each node currently points to None
print(node1.data) # 10
print(node1.next) # None

# Step 1: Create three nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
# Step 2: Link them together
node1.next = node2 # node1 now points to node2
node2.next = node3 # node2 now points to node3
node3.next = None # node3 is the last node (tail)
# Step 3: Set HEAD to the first node
head = node1
# Memory layout (conceptual):
# head → [10 | →] → [20 | →] → [30 | None]
# node1 node2 node3

