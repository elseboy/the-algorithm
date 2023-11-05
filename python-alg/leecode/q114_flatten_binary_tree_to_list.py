class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root):
    stack = []
    stack.append(root)
    prev = None
    while stack:
        curr = stack.pop()
        if prev:
            prev.right = curr
            prev.left = None
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
        prev = curr
    return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

result = flatten(root)
while result:
    print(result.val)
    result = result.right
