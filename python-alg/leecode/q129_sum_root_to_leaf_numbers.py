class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumNumbers(root):
    def dfs(curr, total):
        if not curr:
            return 0

        total = total * 10 + curr.val

        if not curr.left and not curr.right:
            return total

        return dfs(curr.left, total) + dfs(curr.right, total)

    return dfs(root, 0)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
print(sumNumbers(root))
