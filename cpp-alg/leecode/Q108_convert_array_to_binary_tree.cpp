#include <iostream>
#include <queue>
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

class Solution {
public:
  TreeNode *sortedArrayToBST(std::vector<int> &nums) {
    return helper(nums, 0, nums.size() - 1);
  }
  TreeNode *helper(std::vector<int> &nums, int left, int right) {
    if (left > right) {
      return nullptr;
    }
    int mid = (left + right) / 2;
    TreeNode *root = new TreeNode(nums[mid]);
    root->left = helper(nums, left, mid - 1);
    root->right = helper(nums, mid + 1, right);
    return root;
  }
};

int main() {

  Solution solution;
  std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
  TreeNode *node = solution.sortedArrayToBST(nums);
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
