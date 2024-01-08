class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order(root):
    stack = []
    curr = root
    res = []

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        temp = stack.pop()
        res.append(temp.val)
        curr = temp.right

    return res

#     3
#    / \
#   9  20
#     /  \
#    15   7
# pre = [9, 3, 15, 20, 7]

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(in_order(tree))
