from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def rightSideView(root):
    curr_nodes = deque()
    next_nodes = deque()
    res = []

    curr_nodes.append(root)
    res.append(root.val)

    while curr_nodes:
        temp = curr_nodes.popleft()

        if temp.left:
            next_nodes.append(temp.left)
        if temp.right:
            next_nodes.append(temp.right)

        if not curr_nodes:
            if next_nodes:
                res.append(next_nodes[-1].val)
            curr_nodes, next_nodes = next_nodes, curr_nodes
    
    return res


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(4)

print(rightSideView(tree))
