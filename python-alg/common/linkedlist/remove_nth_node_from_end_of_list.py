class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head

    fast, slow = dummy, dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    
    return dummy.next 

n = 2
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

head = removeNthFromEnd(head, n)

while head:
    print(head.val, end=" -> ")
    head = head.next
