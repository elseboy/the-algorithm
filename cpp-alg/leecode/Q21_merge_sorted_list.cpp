#include <iostream>

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *mergeListNode(ListNode *l1, ListNode *l2) {
  ListNode *dummy = new ListNode();
  ListNode *curr = dummy;

  while (l1 && l2) {
    if (l1->val < l2->val) {
      curr->next = new ListNode(l1->val);
      l1 = l1->next;
    } else {
      curr->next = new ListNode(l2->val);
      l2 = l2->next;
    }
    curr = curr->next;
  }
  curr->next = l1 ? l1 : l2;
  return dummy->next;
}

int main() {
  ListNode *nodeG = new ListNode(3);
  ListNode *nodeF = new ListNode(2, nodeG);
  ListNode *nodeE = new ListNode(1, nodeF);
  ListNode *nodeD = new ListNode(5);
  ListNode *nodeC = new ListNode(4, nodeD);
  ListNode *nodeB = new ListNode(1, nodeC);
  ListNode *result = mergeListNode(nodeE, nodeB);
  while (result) {
    std::cout << result->val << std::endl;
    result = result->next;
  }
  return 0;
}
