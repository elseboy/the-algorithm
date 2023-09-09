#include <iostream>
#include <queue>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

TreeNode *invertTree(TreeNode *root) {
  std::queue<TreeNode *> queue;
  queue.push(root);
  while (!queue.empty()) {
    TreeNode *node = queue.front();
    queue.pop();
    TreeNode *left = node->left;
    node->left = node->right;
    node->right = left;
    if (node->left != nullptr)
      queue.push(node->left);
    if (node->right != nullptr)
      queue.push(node->right);
  }
  return root;
}

int main() {
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->left->left = new TreeNode(4);
  root->left->right = new TreeNode(5);
  root->right->left = new TreeNode(6);
  root->right->right = new TreeNode(7);

  TreeNode *node = invertTree(root);
  std::queue<TreeNode *> queue;
  queue.push(node);
  while (!queue.empty()) {
    TreeNode *current = queue.front();
    queue.pop();
    std::cout << current->val << std::endl;
    if (current->left)
      queue.push(current->left);
    if (current->right)
      queue.push(current->right);
  }
  return 0;
}
