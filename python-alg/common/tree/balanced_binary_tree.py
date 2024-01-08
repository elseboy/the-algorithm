class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanced_binary_tree(root):
    def dfs(node):
        if not node:
            return 0

        l_height = dfs(node.left)
        r_height = dfs(node.right)

        if l_height == -1 or r_height == -1 or abs(l_height - r_height) > 1:
            return -1

        return max(l_height, r_height) + 1

    return True if dfs(root) != -1 else False


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(balanced_binary_tree(tree))
