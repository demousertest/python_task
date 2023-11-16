class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorderTraversal(root):
    if not root:
        return []

    result = []
    stack = []
    current = root

    while stack or current:
        if current:
            stack.append(current)
#             print(current.value)
            result.insert(0, current.value)
            current = current.right 
#             print(current.value)
        else:
            node = stack.pop()
            current = node.left

    return result

# Example usage:
# Construct a binary tree
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(1)



result = postorderTraversal(root)
print(result)  
