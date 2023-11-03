class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_node_from_end(head, n):
    temp = ListNode(0)
    temp.next = head
    fast, slow = temp, temp

    for i in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return temp.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
n = 2
result = remove_node_from_end(l, n)
while result:
    print(result.val)
    result = result.next
