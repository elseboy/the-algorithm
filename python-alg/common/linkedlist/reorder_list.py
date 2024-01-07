class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    mid = find_middle(head)
    reversed = reverse_list(mid.next)
    mid.next = None

    merge_list(head, reversed)


def find_middle(head):
    slow, fast = head, head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    return slow


def reverse_list(head):
    curr = head
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def merge_list(l1, l2):
    while l2:
        t1, t2 = l1.next, l2.next
        l1.next, l2.next = l2, t1
        l1, l2 = t1, t2


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

reorder_list(head)

while head:
    print(head.val, end=" -> ")
    head = head.next
