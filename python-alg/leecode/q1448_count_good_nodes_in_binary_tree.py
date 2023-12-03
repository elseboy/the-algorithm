class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root):
    def count_good_nodes(node, max_val):
        if not node:
            return 0

        is_good_node = 1 if node.val >= max_val else 0

        left_count = count_good_nodes(node.left, max(max_val, node.val))
        right_count = count_good_nodes(node.right, max(max_val, node.val))

        return is_good_node + left_count + right_count

    return count_good_nodes(root, float('-inf'))


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
print(goodNodes(root))
