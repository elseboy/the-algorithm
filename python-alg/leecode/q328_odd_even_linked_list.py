class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    if not head or not head.next:
        return head

    odd_head = ListNode(0)
    even_head = ListNode(0)

    odd, even = odd_head, even_head
    is_odd = True
    curr = head

    while curr:
        if is_odd:
            odd.next = curr
            odd = odd.next
        else:
            even.next = curr
            even = even.next

        is_odd = not is_odd
        curr = curr.next

    odd.next = even_head.next
    even.next = None

    return odd_head.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = oddEvenList(head)

while result:
    print(result.val)
    result = result.next
