class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddle(head):
    if not head or not head.next:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if prev:
        prev.next = slow.next
    else:
        head = slow.next

    return head


head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(6)

result = deleteMiddle(head)

while result:
    print(result.val)
    result = result.next
