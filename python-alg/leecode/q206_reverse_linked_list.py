class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_linked_list(node):
    if node is None:
        return
    prev = None
    curr = node
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


nodeE = ListNode(5)
nodeD = ListNode(4)
nodeD.next = nodeE
nodeC = ListNode(3)
nodeC.next = nodeD
nodeB = ListNode(2)
nodeB.next = nodeC
nodeA = ListNode(1)
nodeA.next = nodeB

root = reverse_linked_list(nodeA)
while root:
    print(root.val)
    root = root.next
