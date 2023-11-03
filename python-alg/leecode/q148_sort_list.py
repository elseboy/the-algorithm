class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head):
    if not head or not head.next:
        return head
    left = head
    right = getMid(head)
    temp = right.next
    right.next = None
    right = temp

    left = sort_list(left)
    right = sort_list(right)

    return merge(left, right)


def getMid(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(l1, l2):
    tail = dummy = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next


l = ListNode(2)
l.next = ListNode(1)
l.next.next = ListNode(5)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)

result = sort_list(l)
while result:
    print(result.val)
    result = result.next
