class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_duplicates(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while head:
        while head.next and head.val == head.next.val:
            head = head.next

        if prev.next == head:
            prev = prev.next
        else:
            prev.next = head.next

        head = head.next
    return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(5)

head = remove_duplicates(head)

while head:
    print(head.val)
    head = head.next
