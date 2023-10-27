from collections import deque


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def pre_order_travel(node):
    if node is None:
        return
    stack = []
    stack.append(node)
    while stack:
        node = stack.pop()
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def in_order_travel(node):
    if node is None:
        return
    stack = []
    current = node
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val, end=" ")
        current = current.right


def post_order_travel(node):
    if node is None:
        return
    stack = []
    temp = []
    stack.append(node)
    while stack:
        current = stack.pop()
        temp.append(current)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    while temp:
        print(temp.pop().val, end=" ")


def BFS(node):
    queue = deque()
    queue.append(node)

    while queue:
        curr = queue.popleft()
        print(curr.val, end=" ")
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


def count_levels(node):
    curr_level_queue = deque()
    next_level_queue = deque()
    depth = 0

    curr_level_queue.append(node)
    while curr_level_queue:
        temp = curr_level_queue.popleft()
        if temp.left:
            next_level_queue.append(temp.left)
        if temp.right:
            next_level_queue.append(temp.right)

        if not curr_level_queue:
            curr_level_queue, next_level_queue = next_level_queue, curr_level_queue
            depth += 1
    print(depth)


root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.right = TreeNode("F")
root.left.right.left = TreeNode("G")

pre_order_travel(root)
print()
in_order_travel(root)
print()
post_order_travel(root)
print()
BFS(root)
print()
count_levels(root)
