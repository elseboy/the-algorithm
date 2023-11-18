from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder, postorder):
    if not inorder:
        return None

    root = TreeNode(postorder.pop())
    index = inorder.index(root.val)

    root.right = buildTree(inorder[index + 1 :], postorder)
    root.left = buildTree(inorder[:index], postorder)

    return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

tree = buildTree(inorder, postorder)
queue = deque([tree])

while queue:
    temp = queue.popleft()
    print(temp.val)
    if temp.left:
        queue.append(temp.left)
    if temp.right:
        queue.append(temp.right)
