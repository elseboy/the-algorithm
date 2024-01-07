class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head, left, right):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next
    next_node = None

    for _ in range(right - left + 1):
        temp = curr.next
        curr.next = next_node
        next_node = curr
        curr = temp

    prev.next.next = curr
    prev.next = next_node

    return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = reverseList(node1, 2, 4)

while head:
    print(head.val)
    head = head.next
