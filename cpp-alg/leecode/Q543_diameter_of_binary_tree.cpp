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

class Solution {
public:
  int diameterOfBinaryTree(TreeNode *root) {
    maxDepth = 0;
    depth(root);
    return maxDepth;
  }

private:
  int maxDepth;

  int depth(TreeNode *node) {
    if (node == nullptr)
      return 0;

    int left = depth(node->left);
    int right = depth(node->right);
    maxDepth = std::max(left + right, maxDepth);
    return std::max(left, right) + 1;
  }
};

int main() {
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->left->left = new TreeNode(4);
  root->left->right = new TreeNode(5);
  Solution solution;
  int max = solution.diameterOfBinaryTree(root);
  std::cout << max << std::endl;
  delete root;
  return 0;
}
