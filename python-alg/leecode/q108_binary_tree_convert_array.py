from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convert_to_tree(nums):
    return split(nums, 0, len(nums) - 1)


def split(nums, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    root = TreeNode(nums[mid])
    root.left = split(nums, left, mid - 1)
    root.right = split(nums, mid + 1, right)
    return root


nums = [-10, -3, 0, 5, 9]
root = convert_to_tree(nums)
queue = deque()
queue.append(root)
while queue:
    temp = queue.popleft()
    print(temp.val, end=" ")
    if temp.left:
        queue.append(temp.left)
    if temp.right:
        queue.append(temp.right)
