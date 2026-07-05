class Node:
    def __init__(self, roll):
        self.roll = roll
        self.left = None
        self.right = None


def insert(root, roll):
    if root is None:
        return Node(roll)

    if roll < root.roll:
        root.left = insert(root.left, roll)
    else:
        root.right = insert(root.right, roll)

    return root


def search(root, key):
    if root is None:
        return False

    if root.roll == key:
        return True

    if key < root.roll:
        return search(root.left, key)

    return search(root.right, key)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.roll, end=" ")
        inorder(root.right)


root = None

for i in [25, 10, 40, 5, 20]:
    root = insert(root, i)

print("Search 20:", search(root, 20))

print("Inorder:")
inorder(root)