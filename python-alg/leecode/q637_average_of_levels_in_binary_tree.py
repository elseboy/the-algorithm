from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root):
    res = []
    curr_nodes = deque()
    next_nodes = deque()

    curr_nodes.append(root)

    while curr_nodes:
        level_sum = 0
        level_count = len(curr_nodes)

        for _ in range(level_count):
            temp = curr_nodes.popleft()
            level_sum += temp.val

            if temp.left:
                next_nodes.append(temp.left)
            if temp.right:
                next_nodes.append(temp.right)

        res.append(level_sum / level_count)

        curr_nodes, next_nodes = next_nodes, curr_nodes

    return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(averageOfLevels(root))
