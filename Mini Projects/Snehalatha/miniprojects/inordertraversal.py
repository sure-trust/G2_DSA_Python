class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node is not None:
        # Traverse the left subtree
        inorder_traversal(node.left)
        # Visit the root node
        print(node.value, end=" ")
        # Traverse the right subtree
        inorder_traversal(node.right)

# Example usage:
# Build a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform inorder traversal
print("Inorder Traversal:")
inorder_traversal(root)

