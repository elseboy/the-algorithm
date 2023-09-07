#include <iostream>
#include <unordered_set>

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *listNode) : val(x), next(listNode) {}
};

ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
  std::unordered_set<ListNode *> travel;
  ListNode *temp = headA;
  while (temp) {
    travel.insert(temp);
    temp = temp->next;
  }
  temp = headB;
  while (temp != nullptr) {
    if (travel.count(temp)) {
      return temp;
    }
    temp = temp->next;
  }
  return nullptr;
}

int main() {
  ListNode *nodeE = new ListNode(5);
  ListNode *nodeD = new ListNode(4, nodeE);
  ListNode *nodeC = new ListNode(3, nodeD);
  ListNode *nodeB = new ListNode(2, nodeC);
  ListNode *nodeA = new ListNode(1, nodeB);

  ListNode *nodeH = new ListNode(7, nodeD);
  ListNode *intersectionNode = getIntersectionNode(nodeA, nodeH);
  std::cout << intersectionNode->val << std::endl;

  delete nodeA;
  delete nodeB;
  delete nodeC;
  delete nodeD;
  delete nodeE;
  delete nodeH;

  return 0;
}
