from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert(root):
    queue = deque()
    queue.append(root)
    while queue:
        curr = queue.pop()
        left = curr.left
        curr.left = curr.right
        curr.right = left

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

node = invert(root)

queue = deque()
queue.append(node)
while queue:
    curr = queue.popleft()
    print(curr.val)
    if curr.left:
        queue.append(curr.left)
    if curr.right:
        queue.append(curr.right)
