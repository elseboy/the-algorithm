class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxLevelSum(root):
    sum = []

    def dfs(node: TreeNode, level: int) -> None:
        if level == len(sum):
            sum.append(node.val)
        else:
            sum[level] += node.val
        if node.left:
            dfs(node.left, level + 1)
        if node.right:
            dfs(node.right, level + 1)

    dfs(root, 0)
    return sum.index(max(sum)) + 1


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
root.right.right = TreeNode(0)

print(maxLevelSum(root))
