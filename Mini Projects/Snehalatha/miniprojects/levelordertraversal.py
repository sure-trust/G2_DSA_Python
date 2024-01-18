from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if root is None:
        return
    
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        print(current_node.value, end=" ")

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

# Example usage:
# Build a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform level order traversal
print("Level Order Traversal:")
level_order_traversal(root)

