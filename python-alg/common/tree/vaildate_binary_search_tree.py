from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vaild(root):
    stack = []
    prev = float('-inf')

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        temp = stack.pop()
        if temp.val <= prev:
            return False
        prev = temp.val
        root = temp.right

    return True


tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)

print(vaild(tree))
