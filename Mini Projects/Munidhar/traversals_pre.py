class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return

    print(root.data)
    preorder(root.left)
    preorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)

preorder(root)



