#include <iostream>
#include <stack>
#include <vector>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

std::vector<int> inorderTravel(TreeNode *root) {
  std::vector<int> list = {};
  std::stack<TreeNode *> stack;
  TreeNode *current = root;
  while (!stack.empty() || current != nullptr) {
    while (current != nullptr) {
      stack.push(current);
      current = current->left;
    }
    current = stack.top();
    list.emplace_back(current->val);
    stack.pop();
    current = current->right;
  }
  return list;
}

int main() {
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->left->left = new TreeNode(4);
  root->left->right = new TreeNode(5);
  root->right->left = new TreeNode(6);
  root->right->right = new TreeNode(7);

  std::vector<int> list = inorderTravel(root);
  for (int num : list) {
    std::cout << num << " ";
  }
  std::cout << std::endl;
  return 0;
}
