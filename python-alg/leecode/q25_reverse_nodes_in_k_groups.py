class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    temp = ListNode(0)
    temp.next = head
    pre, end = temp, temp

    while end:
        for i in range(k):
            if end:
                end = end.next

        if not end:
            break

        next = end.next
        end.next = None
        start = pre.next
        # reverse start - end range
        pre.next = None
        pre.next = reverse_node(start)
        start.next = next
        pre = start
        end = start

    return temp.next


def reverse_node(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
k = 2
result = reverse_k_group(l, k)
while result:
    print(result.val)
    result = result.next
