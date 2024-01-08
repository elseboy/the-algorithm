from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    next_nodes = deque()
    curr_nodes = deque()
    depth = 0
    curr_nodes.append(root)

    if not root:
        return 0

    while curr_nodes:
        temp = curr_nodes.popleft()
        if temp.left:
            next_nodes.append(temp.left)
        if temp.right:
            next_nodes.append(temp.right)

        if not curr_nodes:
            curr_nodes, next_nodes = next_nodes, curr_nodes
            depth += 1

    return depth


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(4)

print(max_depth(tree))
