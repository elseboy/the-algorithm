class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_BST(root):
    def vaild(node, left, right):
        if not node:
            return True
        if not (node.val < right and node.val > left):
            return False
        return vaild(node.left, left, node.val) and vaild(node.right, node.val, right)

    return vaild(root, float("-inf"), float("inf"))


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

print(is_BST(root))
