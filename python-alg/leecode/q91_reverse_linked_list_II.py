class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
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


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

left = 2
right = 4

head = reverseBetween(head, left, right)

while head:
    print(head.val)
    head = head.next
