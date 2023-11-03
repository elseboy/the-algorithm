class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    h1 = l1
    h2 = l2

    # 基准链表
    while h1:
        if h2:
            h1.val += h2.val
            h2 = h2.next

        # h2比h1长
        if not h1.next and h2:
            h1.next = h2
            break

        h1 = h1.next

    move_ten(l1)
    return l1


def move_ten(head):
    while head:
        if head.val >= 10:
            head.val = head.val % 10
            # 出现末尾进位
            if not head.next:
                head.next = ListNode(0)
            head.next.val += 1
        head = head.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = add_two_numbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.next
