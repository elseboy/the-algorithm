class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_linked_list(l1, l2):
    head = None
    if l1.val <= l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    curr = head
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    if l1 is None:
        curr.next = l2
    elif l2 is None:
        curr.next = l1

    return head


nodeF = ListNode(6)
nodeE = ListNode(5)
nodeE.next = nodeF
nodeD = ListNode(4)
nodeD.next = nodeE
nodeC = ListNode(3)
nodeB = ListNode(2)
nodeB.next = nodeC
nodeA = ListNode(1)
nodeA.next = nodeB

head = merge_linked_list(nodeA, nodeD)
while head:
    print(head.val)
    head = head.next
