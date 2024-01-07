class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    nodes = set()

    temp = headA

    while temp:
        nodes.add(temp)
        temp = temp.next

    temp = headB

    while temp is not None:
        if temp in nodes:
            return temp
        temp = temp.next
            
    return None


common_node = ListNode(3)

# Linked list A: 1 -> 2 -> 3 -> 4
headA = ListNode(1)
nodeA2 = ListNode(2)
nodeA3 = common_node
nodeA4 = ListNode(4)

headA.next = nodeA2
nodeA2.next = nodeA3
nodeA3.next = nodeA4

# Linked list B: 5 -> 6 -> 7 -> 3 -> 4
headB = ListNode(5)
nodeB6 = ListNode(6)
nodeB7 = ListNode(7)

headB.next = nodeB6
nodeB6.next = nodeB7
nodeB7.next = common_node
nodeA4.next = None

print(getIntersectionNode(headA, headB).val)
