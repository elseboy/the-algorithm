#include <iostream>

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *reverseLinkedList(ListNode *head) {
  ListNode *prev = nullptr;
  ListNode *current = head;
  while (current) {
    ListNode *next = current->next;
    current->next = prev;
    prev = current;
    current = next;
  }
  return prev;
}

int main() {
  ListNode *nodeE = new ListNode(5);
  ListNode *nodeD = new ListNode(4, nodeE);
  ListNode *nodeC = new ListNode(3, nodeD);
  ListNode *nodeB = new ListNode(2, nodeC);
  ListNode *nodeA = new ListNode(1, nodeB);

  ListNode *result = reverseLinkedList(nodeA);
  while (result) {
    std::cout << result->val << " ";
    result = result->next;
  }
  std::cout << std::endl;
}
