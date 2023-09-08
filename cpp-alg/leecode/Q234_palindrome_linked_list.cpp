#include <iostream>
#include <vector>

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

bool arraySolution(ListNode *head) {
  std::vector<int> vals;
  while (head != nullptr) {
    vals.emplace_back(head->val);
    head = head->next;
  }
  for (int i = 0, j = (int)vals.size() - 1; i < j; ++i, --j) {
    if (vals[i] != vals[j])
      return false;
  }
  return true;
}

ListNode *reverseListNode(ListNode *head) {
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

bool slowFastPointer(ListNode *head) {
  ListNode *slow = head;
  ListNode *fast = head;

  while (fast->next && fast->next->next) {
    slow = slow->next;
    fast = fast->next->next;
  }

  ListNode *secondHalf = reverseListNode(slow->next);

  while (secondHalf) {
    if (head->val != secondHalf->val)
      return false;
    head = head->next;
    secondHalf = secondHalf->next;
  }

  return true;
}

bool isPalindrome(ListNode *head) {
  // array solution
  // copy to an array, then compare the first elem and last elem
  // like [1, 2, 2, 1], take array[0] and array[array.size() - 1) to compare
  // return arraySolution(head);

  // slowFastPointer solution
  // find the middle and reverse one of the parts using slow and fast pointer
  // reverse slow->next is because slow pointing to the end of the first half,
  // slow->next issecond half.
  return slowFastPointer(head);
}

int main() {

  ListNode *nodeG = new ListNode(1);
  ListNode *nodeF = new ListNode(2, nodeG);
  ListNode *nodeE = new ListNode(3, nodeF);
  ListNode *nodeD = new ListNode(3, nodeE);
  ListNode *nodeC = new ListNode(2, nodeD);
  ListNode *nodeB = new ListNode(1, nodeC);
  bool result = isPalindrome(nodeB);
  std::cout << result << std::endl;
}
