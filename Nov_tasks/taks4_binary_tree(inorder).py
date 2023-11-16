from collections import deque, defaultdict

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def verticalOrderTraversal(root):
    if not root:
        return []

    column_table = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
        node, col = queue.popleft()
        print(node.value, col)
        column_table[col].append(node.value)
        print(column_table)
        if node.left:
            print(node.left.value)
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))


    print(column_table)
    result = [column_table[col] for col in sorted(column_table.keys())]

    return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result = verticalOrderTraversal(root)
print(result)
