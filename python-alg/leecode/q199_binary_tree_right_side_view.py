from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    queue = deque()
    queue.append(root)
    res = []

    while queue:
        right_side = None
        level_size = len(queue)
        for i in range(level_size):
            temp = queue.popleft()
            if temp:
                right_side = temp
                queue.append(temp.left)
                queue.append(temp.right)
        if right_side:
            res.append(right_side.val)
    return res


root = TreeNode(1)
root.left = TreeNode(2)

print(right_side_view(root))
