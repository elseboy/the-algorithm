from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root):
    res = []
    curr_nodes = deque()
    next_nodes = deque()

    left_to_right = True

    curr_nodes.append(root)

    while curr_nodes:
        level_values = []
        level_count = len(curr_nodes)
        for _ in range(level_count):
            if left_to_right:
                temp = curr_nodes.popleft()
            else:
                temp = curr_nodes.pop()

            level_values.append(temp.val)

            if left_to_right:
                if temp.left:
                    next_nodes.append(temp.left)
                if temp.right:
                    next_nodes.append(temp.right)
            else:
                if temp.right:
                    next_nodes.appendleft(temp.right)
                if temp.left:
                    next_nodes.appendleft(temp.left)

        res.append(level_values)
        left_to_right = not left_to_right

        curr_nodes, next_nodes = next_nodes, curr_nodes

    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
print(zigzagLevelOrder(root))
