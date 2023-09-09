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

int maxDepth(TreeNode *root) {
  if (root == nullptr)
    return 0;
  std::queue<TreeNode *> queue;
  queue.push(root);
  int depth = 0;
  while (!queue.empty()) {
    int size = queue.size();
    while (size > 0) {
      TreeNode *current = queue.front();
      std::cout << current->val << " ";
      queue.pop();
      if (current->left)
        queue.push(current->left);
      if (current->right)
        queue.push(current->right);
      size--;
    }
    depth++;
  }
  return depth;
}

int main() {
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->left->left = new TreeNode(4);
  root->left->right = new TreeNode(5);
  root->right->left = new TreeNode(6);
  root->right->right = new TreeNode(7);

  int depth = maxDepth(root);
  std::cout << depth << std::endl;

  return 0;
}
