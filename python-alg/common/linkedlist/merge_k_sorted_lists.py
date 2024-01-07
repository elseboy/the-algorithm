class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists):
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        next_level = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None

            next_level.append(merge(l1, l2))

        lists = next_level

    return lists[0]


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


# Test Case
# Create three sorted linked lists
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

result = mergeKLists([list1, list2, list3])

print("Merged Linked List:")
while result:
    print(result.val, end=" -> ")
    result = result.next
