class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head):
    curr = head

    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
            
    return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
head = delete_duplicates(head)
while head:
    print(head.val, end=" -> ")
    head = head.next

