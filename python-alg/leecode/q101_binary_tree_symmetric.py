from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def symmetric(root):
    queue = deque()
    queue.append(root.left)
    queue.append(root.right)
    while queue:
        right = queue.popleft()
        left = queue.popleft()
        if not left and not right:
            continue
        if not left or not right or left.val != right.val:
            return False
        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)
    return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(symmetric(root))
