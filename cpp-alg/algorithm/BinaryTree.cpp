#include <array>
#include <iostream>
#include <queue>
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
  if (node == nullptr)
    return;

  std::stack<Node *> stack;
  std::stack<Node *> temp;
  stack.push(node);

  while (!stack.empty()) {
    Node *pop = stack.top();
    stack.pop();
    temp.push(pop);
    if (pop->left != nullptr)
      stack.push(pop->left);
    if (pop->right != nullptr)
      stack.push(pop->right);
  }
  while (!temp.empty()) {
    std::cout << temp.top()->data << " ";
    temp.pop();
  }
}

void BFS(Node *node) {
  if (node == nullptr)
    return;

  std::queue<Node *> queue;
  queue.push(node);

  while (!queue.empty()) {
    Node *current = queue.front();
    queue.pop();
    std::cout << current->data << " ";
    if (current->left)
      queue.push(current->left);
    if (current->right)
      queue.push(current->right);
  }
}

void CountLevels(Node *node) {

  if (node == nullptr)
    return;

  std::queue<Node *> current_level_queue;
  std::queue<Node *> next_level_queue;
  int depth = 0;
  current_level_queue.push(node);
  while (!current_level_queue.empty()) {
    Node *current = current_level_queue.front();
    current_level_queue.pop();

    if (current->left)
      next_level_queue.push(current->left);
    if (current->right)
      next_level_queue.push(current->right);

    if (current_level_queue.empty()) {
      std::swap(current_level_queue, next_level_queue);
      depth++;
    }
  }
  std::cout << "depth: " << depth << std::endl;
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
   *        /  \      \                   BFS_travel：ABCDEFG
   *      D     E      F
   *           /
   *         G
   */

  // ===============================================================
  PreOrder(root);
  std::cout << std::endl;
  InOrder(root);
  std::cout << std::endl;
  PostOrder(root);
  std::cout << std::endl;
  BFS(root);
  std::cout << std::endl;
  CountLevels(root);
  // ===============================================================

  root = nullptr;
  return 0;
}
