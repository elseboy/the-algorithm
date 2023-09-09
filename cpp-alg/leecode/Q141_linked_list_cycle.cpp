#include <iostream>
#include <unordered_set>

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};

bool hasCycle(ListNode *head) {
  std::unordered_set<ListNode *> set;
  while (head) {
    if (set.count(head))
      return true;
    set.insert(head);
    head = head->next;
  }
  return false;
}

int main() {

  ListNode *nodeD = new ListNode(4);
  ListNode *nodeC = new ListNode(3);
  ListNode *nodeB = new ListNode(2);
  ListNode *nodeA = new ListNode(1);
  nodeA->next = nodeB;
  nodeB->next = nodeC;
  nodeC->next = nodeD;
  nodeD->next = nullptr;

  bool result = hasCycle(nodeA);
  std::cout << result << std::endl;

  return 0;
}
