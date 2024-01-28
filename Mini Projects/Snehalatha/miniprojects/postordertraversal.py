class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversal(node):
    if node is not None:
        # Traverse the left subtree
        postorder_traversal(node.left)
        # Traverse the right subtree
        postorder_traversal(node.right)
        # Visit the root node
        print(node.value, end=" ")

# Example usage:
# Build a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform postorder traversal
print("Postorder Traversal:")
postorder_traversal(root)

