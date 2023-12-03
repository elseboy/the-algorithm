class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root, key):
    if not root:
        return root

    if key > root.val:
        root.right = deleteNode(root.right, key)
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        curr = root.right
        while curr.left:
            curr = curr.left
        root.val = curr.val
        root.right = deleteNode(root.right, curr.val)
    return root


def printInOrderTraversal(root):
    if root:
        printInOrderTraversal(root.left)
        print(root.val, end=" ")
        printInOrderTraversal(root.right)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

result = deleteNode(root, 3)
printInOrderTraversal(result)
