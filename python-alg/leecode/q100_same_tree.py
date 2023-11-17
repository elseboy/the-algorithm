class treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def same_tree(p, q):
    stack = [(p, q)]

    while stack:
        node_p, node_q = stack.pop()

        if not node_p and not node_q:
            continue

        if not node_p or not node_q or node_p.val != node_q.val:
            return False

        stack.append((node_p.left, node_q.left))
        stack.append((node_p.right, node_q.right))

    return True


root = treenode(3)
root.left = treenode(2)
root.right = treenode(20)

root1 = treenode(3)
root1.left = treenode(9)
root1.right = treenode(20)

print(same_tree(root, root1))
