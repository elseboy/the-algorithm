class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
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


head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(5)))))

head = deleteDuplicates(head)

while head:
    print(head.val, end=' -> ')
    head = head.next
