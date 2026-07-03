class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def find_max(root):
    if root is None:
        return None

    while root.right:
        root = root.right

    return root.data


root = None

for x in [20, 10, 30, 5, 15, 40]:
    root = insert(root, x)

print("Maximum Value:", find_max(root))