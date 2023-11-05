class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)

        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)
        res[0] = max(res[0], root.val + leftMax + rightMax)
        return root.val + max(leftMax, rightMax)

    dfs(root)
    return res[0]


root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(max_path_sum(root))
