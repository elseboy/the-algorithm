class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def intersection_two_linked_list(headA, headB):
    travel = set()
    temp = headA
    while temp:
        travel.add(temp)
        temp = temp.next
    temp = headB
    while temp is not None:
        if temp in travel:
            return temp
        temp = temp.next
    return None


if __name__ == "__main__":
    nodeE = ListNode(5)
    nodeD = ListNode(4)
    nodeD.next = nodeE
    nodeC = ListNode(3)
    nodeC.next = nodeD
    nodeB = ListNode(2)
    nodeB.next = nodeC
    nodeA = ListNode(1)
    nodeA.next = nodeB

    nodeH = ListNode(7)
    nodeG = ListNode(5)
    nodeH.next = nodeG
    nodeG.next = nodeD
    elem = intersection_two_linked_list(nodeA, nodeH)
    print(elem.val)
