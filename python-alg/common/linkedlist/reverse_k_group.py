class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    def reverse(start, end):
        prev, curr = None, start
        while curr != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while True:
        group_start = prev_group_end.next
        group_end = group_start

        for _ in range(k):
            if group_end is None:
                return dummy.next
            group_end = group_end.next

        new_group_start = reverse(group_start, group_end)

        prev_group_end.next = new_group_start
        group_start.next = group_end

        prev_group_end = group_start

    return dummy.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
result = reverse_k_group(head, k)

while result:
    print(result.val, end=" -> ")
    result = result.next
