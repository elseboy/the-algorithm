class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_by_pairs(head):
    temp = ListNode(0)
    temp.next = head
    curr = temp

    while curr.next and curr.next.next:
        n1 = curr.next
        n2 = curr.next.next
        next_pair = n2.next

        curr.next = n2
        n2.next = n1
        n1.next = next_pair

        curr = n1

    return temp.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
result = swap_by_pairs(l)
while result:
    print(result.val)
    result = result.next
