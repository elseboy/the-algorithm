from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
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


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)

print(isSymmetric(tree))
