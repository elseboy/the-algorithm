class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def linked_list_cycle(node):
    node_set = set()
    while node:
        if node in node_set:
            return True
        node_set.add(node)
        node = node.next
    return False


nodeD = ListNode(4)
nodeD.next = nodeD
nodeC = ListNode(3)
nodeC.next = nodeD
nodeB = ListNode(2)
nodeB.next = nodeC
nodeA = ListNode(1)
nodeA.next = nodeB

print(linked_list_cycle(nodeA))
