from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root):
    curr_nodes = deque()
    next_nodes = deque()
    res = []

    curr_nodes.append(root)
    reverse = False

    while curr_nodes:
        level_elems = []
        level_count = len(curr_nodes)

        for _ in range(level_count):
            if reverse:
                temp = curr_nodes.pop()
                if temp.right:
                    next_nodes.appendleft(temp.right)
                if temp.left:
                    next_nodes.appendleft(temp.left)
            else:
                temp = curr_nodes.popleft()
                if temp.left:
                    next_nodes.append(temp.left)
                if temp.right:
                    next_nodes.append(temp.right)

            level_elems.append(temp.val)

        res.append(level_elems)
        reverse = not reverse
        curr_nodes, next_nodes = next_nodes, curr_nodes

    return res


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.right.right = TreeNode(5)

print(zigzagLevelOrder(tree))
