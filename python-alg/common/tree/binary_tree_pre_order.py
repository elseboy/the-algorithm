class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def pre_order(root):
    stack = []
    res = []

    stack.append(root)

    while stack:
        curr = stack.pop()
        res.append(curr.val)

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
            
    return res


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(pre_order(tree))
