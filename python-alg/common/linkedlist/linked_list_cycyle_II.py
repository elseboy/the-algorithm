class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    fast, slow = head, head

    while True:
        if not (fast and fast.next):
            return
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            break
    fast = head
    while fast != slow:
        fast, slow = fast.next, slow.next

    return fast


head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)


head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3

print(hasCycle(head).val)
