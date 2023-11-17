class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_duplicates(head):
    curr = head

    while curr:
        while curr.next and curr.next.val == curr.val:
            curr.next = curr.next.next
        curr = curr.next
    return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)

head = remove_duplicates(head)

while head:
    print(head.val)
    head = head.next
