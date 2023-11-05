from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root, targetSum):
    prefix = defaultdict(int)
    prefix[0] = 1

    def dfs(node, curr_sum):
        if not node:
            return 0

        curr_sum += node.val
        result = prefix[curr_sum - targetSum]
        prefix[curr_sum] += 1
        result += dfs(node.left, curr_sum)
        result += dfs(node.right, curr_sum)
        prefix[curr_sum] -= 1
        return result

    return dfs(root, 0)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
target_sum = 8

print(path_sum(root, target_sum))
