class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    node_set = set()

    while head:
        if head in node_set:
            return True
        node_set.add(head)
        head = head.next

    return False


head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = head

print(hasCycle(head))
