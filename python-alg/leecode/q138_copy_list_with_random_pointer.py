class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head):
    # 1: copy each node and paste after the each node, 7,1,2,3 -> 7,7,1,1,2,2,3,3
    # 2: find the random of original node points to original random node,
    #    the next node of this original random node is copy of each node, attach the
    # 3: re connect new nodes
    curr = head
    while curr:
        copy = Node(curr.val)
        copy.next = curr.next
        curr.next = copy
        curr = curr.next.next

    curr = head
    while curr:
        copy = curr.next  # curr = old node, next is newly created node
        if curr.random is None:
            copy.random = None
        else:
            copy.random = curr.random.next
        curr = curr.next.next

    curr = head
    copy_head = None
    copy_tail = None
    while curr:
        copy = curr.next
        next = copy.next
        curr.next = next
        if copy_tail is None:
            copy_head = copy_tail = copy
        else:
            copy_tail.next = copy
            copy_tail = copy_tail.next

        curr = next

    return copy_head


# Create nodes for the linked list
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

# Connect the nodes to form the linked list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Set random pointers
node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

result = copy_random_list(node1)
while result:
    print(result.val)
    result = result.next
