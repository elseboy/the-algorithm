class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root, target):
    def dfs(node, curr_sum):
        if not node:
            return False

        curr_sum += node.val

        if not node.left and not node.right:
            return curr_sum == target

        return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

    return dfs(root, 0)


tree = TreeNode(5)
tree.left = TreeNode(4)
tree.right = TreeNode(8)
tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(4)
tree.right.right.right = TreeNode(1)

print(path_sum(tree, 22))
