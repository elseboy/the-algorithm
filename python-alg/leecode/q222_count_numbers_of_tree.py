from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count(root):
    num = 1
    next_nodes = deque()
    curr_nodes = deque()
    curr_nodes.append(root)

    while curr_nodes:
        temp = curr_nodes.popleft()
        if temp.left:
            next_nodes.append(temp.left)
        if temp.right:
            next_nodes.append(temp.right)

        if not curr_nodes:
            num += len(next_nodes)
            curr_nodes, next_nodes = next_nodes, curr_nodes

    return num


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(count(root))
