class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root):
    depth = [0]
    max_depth(depth, root)
    return depth[0]


def max_depth(depth, root):
    if root is None:
        return 0
    left = max_depth(depth, root.left)
    right = max_depth(depth, root.right)
    print(left, right)
    depth[0] = max(left + right, depth[0])
    return max(left, right) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(diameterOfBinaryTree(root))
