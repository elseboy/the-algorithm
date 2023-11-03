class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle(head):
    fast, slow = head, head
    while True:
        if not (fast and fast.next):
            return
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            break
    fast = head
    while fast != slow:
        fast, slow = fast.next, slow.next
    return fast


head = ListNode(3)
node2 = ListNode(2)
node0 = ListNode(0)
node_minus4 = ListNode(-4)

head.next = node2
node2.next = node0
node0.next = node_minus4
node_minus4.next = node2

cycle_start_node = detect_cycle(head)
if cycle_start_node:
    pos = 0
    current = head
    while current != cycle_start_node:
        pos += 1
        current = current.next
    print(pos)
