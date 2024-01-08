class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    if not root or root.val == p.val or root.val == q.val:
        return root

    left_lca = lowestCommonAncestor(root.left, p, q)
    right_lca = lowestCommonAncestor(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca


tree = TreeNode(3)
tree.left = TreeNode(5)
tree.right = TreeNode(1)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(8)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(4)

p = TreeNode(4)
q = TreeNode(7)

result = lowestCommonAncestor(tree, p, q)
print(result.val)
