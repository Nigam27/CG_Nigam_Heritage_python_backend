from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)

        return root

    # Search
    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Inorder
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Level Order
    def level_order(self):
        if self.root is None:
            return

        q = deque([self.root])

        while q:
            node = q.popleft()
            print(node.data, end=" ")

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

    # Find Minimum
    def find_min(self, root):
        while root.left:
            root = root.left
        return root.data

    # Find Maximum
    def find_max(self, root):
        while root.right:
            root = root.right
        return root.data

    # Height
    def height(self, root):
        if root is None:
            return -1

        return 1 + max(self.height(root.left), self.height(root.right))

    # Count Nodes
    def count_nodes(self, root):
        if root is None:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    # Count Leaf Nodes
    def count_leaf(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        return self.count_leaf(root.left) + self.count_leaf(root.right)

    # Mirror Tree
    def mirror(self, root):
        if root is None:
            return

        root.left, root.right = root.right, root.left

        self.mirror(root.left)
        self.mirror(root.right)

    # Delete
    def delete(self, root, key):
        if root is None:
            return None

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left

            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


# ---------------- Driver Code ----------------

bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.root = bst.insert(bst.root, value)

print("Inorder:")
bst.inorder(bst.root)

print("\nPreorder:")
bst.preorder(bst.root)

print("\nPostorder:")
bst.postorder(bst.root)

print("\nLevel Order:")
bst.level_order()

print("\n\nMinimum:", bst.find_min(bst.root))
print("Maximum:", bst.find_max(bst.root))

print("Height:", bst.height(bst.root))
print("Total Nodes:", bst.count_nodes(bst.root))
print("Leaf Nodes:", bst.count_leaf(bst.root))

print("Search 40:", bst.search(bst.root, 40))
print("Search 100:", bst.search(bst.root, 100))

bst.root = bst.delete(bst.root, 30)

print("\nAfter Deleting 30:")
bst.inorder(bst.root)

bst.mirror(bst.root)

print("\nMirror Tree (Inorder):")
bst.inorder(bst.root)