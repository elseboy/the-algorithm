class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root, val):
    if not root:
        return None

    if root.val == val:
        return root
    elif root.val > val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)


def printSubtree(root):
    if root:
        print(root.val, end=" ")
        printSubtree(root.left)
        printSubtree(root.right)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

result = searchBST(root, 2)
printSubtree(result)
