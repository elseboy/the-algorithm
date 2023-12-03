class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head):
    slow, fast = head, head
    prev = None

    while fast and fast.next:
        fast = fast.next.next

        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    res = 0
    while slow:
        res = max(res, prev.val + slow.val)
        prev = prev.next
        slow = slow.next

    return res


head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

result = pairSum(head)
print(result)
