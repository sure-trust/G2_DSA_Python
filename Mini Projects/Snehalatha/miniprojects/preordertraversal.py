class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is not None:
        # Visit the root node
        print(node.value, end=" ")
        # Traverse the left subtree
        preorder_traversal(node.left)
        # Traverse the right subtree
        preorder_traversal(node.right)

# Example usage:
# Build a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform preorder traversal
print("Preorder Traversal:")
preorder_traversal(root)

