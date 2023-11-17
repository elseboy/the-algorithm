class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x):
    left, right = ListNode(), ListNode()
    ltail, rtail = left, right

    while head:
        if head.val < x:
            ltail.next = head
            ltail = ltail.next
        else:
            rtail.next = head
            rtail = rtail.next

        head = head.next

    ltail.next = right.next
    rtail.next = None

    return left.next


head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

x = 3

head = partition(head, x)
while head:
    print(head.val)
    head = head.next
