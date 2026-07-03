class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Preorder Traversal
def preorder(root, result):
    if not root:
        return   
    result.append(root.data)   
    preorder(root.left, result)    
    preorder(root.right, result)


# Inorder Traversal
def inorder(root, result):
    if not root:
        return    
    inorder(root.left, result)    
    result.append(root.data)   
    inorder(root.right, result)


# Postorder Traversal
def postorder(root, result):
    if not root:
        return   
    postorder(root.left, result)   
    postorder(root.right, result)   
    result.append(root.data)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# Preorder
res = []
preorder(root, res)
print("Preorder :", res)

# Inorder
res = []
inorder(root, res)
print("Inorder  :", res)

# Postorder
res = []
postorder(root, res)
print("Postorder:", res)