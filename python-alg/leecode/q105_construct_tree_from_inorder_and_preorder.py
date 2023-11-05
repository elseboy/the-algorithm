class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    stack = [root]
    inorder_index = 0

    for i in range(1, len(preorder)):
        curr = stack[-1]
        if curr.val != inorder[inorder_index]:
            curr.left = TreeNode(preorder[i])
            stack.append(curr.left)
        else:
            while stack and stack[-1].val == inorder[inorder_index]:
                curr = stack.pop()
                inorder_index += 1
            curr.right = TreeNode(preorder[i])
            stack.append(curr.right)

    return root


l1 = [3, 9, 20, 15, 7]
l2 = [9, 3, 15, 20, 7]

result = build_tree(l1, l2)
stack = [result]
while stack:
    curr = stack.pop()
    print(curr.val, end=" ")
    if curr.right:
        stack.append(curr.right)
    if curr.left:
        stack.append(curr.left)
