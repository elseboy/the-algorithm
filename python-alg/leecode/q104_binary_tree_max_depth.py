from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    curr_queue = deque()
    next_queue = deque()
    depth = 0
    curr_queue.append(root)

    while curr_queue:
        temp = curr_queue.popleft()
        if temp.left:
            next_queue.append(temp.left)
        if temp.right:
            next_queue.append(temp.right)
        if not curr_queue:
            curr_queue, next_queue = next_queue, curr_queue
            depth += 1
    return depth


root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.right = TreeNode("F")
root.left.right.left = TreeNode("G")

print(max_depth(root))
