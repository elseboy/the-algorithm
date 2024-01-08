class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def post_order(root):
    stack = []
    res = []

    stack.append(root)

    while stack:
        curr = stack.pop()

        res.insert(0, curr.val)

        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
            
    return res


#     3
#    / \
#   9  20
#     /  \
#    15   7
# pre = [9, 15, 7, 20, 3]

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(post_order(tree))
