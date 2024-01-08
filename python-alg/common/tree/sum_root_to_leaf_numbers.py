from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_numbers(root):
    total_sum = 0
    queue = deque()

    queue.append((root, 0))

    while queue:
        node, curr_sum = queue.popleft()

        curr_sum = curr_sum * 10 + node.val

        if not node.left and not node.right:
            total_sum += curr_sum

        if node.left:
            queue.append((node.left, curr_sum))
        if node.right:
            queue.append((node.right, curr_sum))

    return total_sum


tree = TreeNode(4)
tree.left = TreeNode(9)
tree.right = TreeNode(0)
tree.left.left = TreeNode(5)
tree.left.right = TreeNode(1)

print(sum_numbers(tree))
