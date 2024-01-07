class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    slow, fast = head, head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    r = reverse(slow.next)

    while r:
        if head.val != r.val:
            return False
        head = head.next
        r = r.next

    return True


def reverse(head):
    curr = head
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(isPalindrome(head))
