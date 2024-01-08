class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(node):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)

        node_sum = node.val + left + right
        max_sum = max(max_sum, node_sum)

        return node.val + max(left, right)

    dfs(node)
    return max_sum


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.right.right = TreeNode(5)
print(maxPathSum(tree))
