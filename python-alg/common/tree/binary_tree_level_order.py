from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    res = []

    curr_nodes = deque()
    next_nodes = deque()

    curr_nodes.append(root)

    while curr_nodes:
        level_elems = []
        level_count = len(curr_nodes)

        for _ in range(level_count):
            temp = curr_nodes.popleft()
            level_elems.append(temp)

            if temp.left:
                next_nodes.append(temp.left)
            if temp.right:
                next_nodes.append(temp.right)

        res.append(level_elems)

        curr_nodes, next_nodes = next_nodes, curr_nodes

    return res


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

result = level_order(tree)

for level, nodes in enumerate(result):
    print(f"Level {level + 1}: {[node.val for node in nodes]}")
