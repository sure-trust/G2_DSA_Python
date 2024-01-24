class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data)
    inorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)

inorder(root)

