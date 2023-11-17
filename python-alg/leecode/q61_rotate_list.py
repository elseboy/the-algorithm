class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    length, tail = 1, head

    while tail.next:
        tail = tail.next
        length += 1

    k = k % length

    if k == 0:
        return head

    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2

head = rotateRight(head, k)

while head:
    print(head.val)
    head = head.next
