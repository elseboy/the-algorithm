class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinimumDifference(root):
    def inorder(node, prev_val, min_diff):
        if not node:
            return prev_val, min_diff

        prev_val, min_diff = inorder(node.left, prev_val, min_diff)

        if prev_val is not None:
            min_diff = min(min_diff, node.val - prev_val)

        prev_val = node.val

        return inorder(node.right, prev_val, min_diff)

    _, res = inorder(root, None, float("inf"))

    return res


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(getMinimumDifference(root))
