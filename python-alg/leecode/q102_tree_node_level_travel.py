from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        level_nodes = []
        level_size = len(queue)
        for _ in range(level_size):
            temp = queue.popleft()
            level_nodes.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        res.append(level_nodes)
    return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result = level_order(root)
print(result)
