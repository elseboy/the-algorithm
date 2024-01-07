class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head):
    if not head or not head.next:
        return head

    mid = find_middle(head)

    l = head
    r = mid.next
    mid.next = None

    l_sorted = sort_list(l)
    r_sorted = sort_list(r)

    return merge(l_sorted, r_sorted)


def find_middle(head):
    slow, fast = head, head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    return slow


def merge(l1, l2):
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 if l1 else l2
    return dummy.next


head = ListNode(5, ListNode(2, ListNode(3, ListNode(1, ListNode(2)))))

head = sort_list(head)

while head:
    print(head.val, end=" -> ")
    head = head.next
