class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def copy_node(node):
    if node is None:
        return None
    new_node = ListNode(node.val)
    new_node.next = copy_node(node.next)
    return new_node


def palindrome_linked_list(node):
    head = copy_node(node)
    prev = None
    curr = node
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    while prev and head:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next
    return True


def array_solution(node):
    vals = []
    head = copy_node(node)
    while head:
        vals.append(head.val)
        head = head.next
    i = 0
    j = len(vals) - 1
    while i < j:
        if vals[i] != vals[j]:
            return False
        i += 1
        j -= 1
    return True


nodeB = ListNode(2)
nodeA = ListNode(1)
nodeA.next = nodeB
# print(palindrome_linked_list(nodeA))
print(array_solution(nodeA))
