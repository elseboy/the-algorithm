#include <array>
#include <iostream>
#include <stack>
#include <string>

class Node {
public:
  std::string data;
  Node *left;
  Node *right;

  Node(std::string value) : data(value), left(nullptr), right(nullptr) {}
};

// pre_order
void PreOrder(Node *node) {
  if (node == nullptr)
    return;

  std::stack<Node *> stack;
  stack.push(node);
  while (!stack.empty()) {
    Node *current = stack.top();
    stack.pop();
    std::cout << current->data << " ";
    if (current->right)
      stack.push(current->right);
    if (current->left)
      stack.push(current->left);
  }
}

// in_order
void InOrder(Node *node) {
  if (node == nullptr)
    return;

  std::stack<Node *> stack;
  Node *current = node;
  while (!stack.empty() || current != nullptr) {
    while (current != nullptr) {
      stack.push(current);
      current = current->left;
    }
    current = stack.top();
    stack.pop();
    std::cout << current->data << " ";

    current = current->right;
  }
}

// post_order
void PostOrder(Node *node) {


}

int main() {

  Node *root = new Node("A");
  root->left = new Node("B");
  root->right = new Node("C");
  root->left->left = new Node("D");
  root->left->right = new Node("E");
  root->right->right = new Node("F");
  root->left->right->left = new Node("G");
  /**
   *              A                       pre_order： ABDEGCF
   *            /  \                      in_order：	DBGEACF
   *          B     C                     post_order：DGEBFCA
   *        /  \      \                   BFS_travel：ABDEGCF
   *      D     E      F
   *           /
   *         G
   */

  // ===============================================================
  PreOrder(root);
  std::cout << std::endl;
  InOrder(root);
  // ===============================================================

  root = nullptr;
  return 0;
}
