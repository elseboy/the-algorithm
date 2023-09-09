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

bool isSymmetric(TreeNode *root) {
  if (root == nullptr)
    return 0;
  std::queue<TreeNode *> queue;
  queue.push(root->left);
  queue.push(root->right);
  while (!queue.empty()) {
    auto right = queue.front();
    queue.pop();
    auto left = queue.front();
    queue.pop();

    if (!left && !right)
      continue;
    if (!left || !right || left->val != right->val)
      return false;

    queue.push(left->left);
    queue.push(right->right);
    queue.push(left->right);
    queue.push(right->left);
  }
  return true;
}

int main() {
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(2);
  root->left->left = new TreeNode(3);
  root->left->right = new TreeNode(4);
  root->right->left = new TreeNode(4);
  root->right->right = new TreeNode(3);
  bool result = isSymmetric(root);
  std::cout << result << std::endl;
  return 0;
}
