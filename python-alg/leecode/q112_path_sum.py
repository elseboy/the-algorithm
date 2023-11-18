class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, target):
    def dfs(node, curr_sum):
        if not node:
            return False

        curr_sum += node.val

        if not node.left and not node.right:
            return curr_sum == target

        return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

    return dfs(root, 0) if root else False


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

print(hasPathSum(root, 7))
