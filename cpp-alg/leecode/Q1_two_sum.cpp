#include <iostream>
#include <vector>

class Solution {
public:
  std::vector<int> twoSum(std::vector<int> &nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
      for (int j = i + 1; j < nums.size(); j++) {
        if (nums[i] + nums[j] == target)
          return {i, j};
      }
    }
    return {};
  }
};

int main() {
  std::vector<int> vector = {1, 2, 3, 4, 5};
  int target = 9;
  Solution solution;
  std::vector<int> result = solution.twoSum(vector, target);
  std::cout << "[" << result[0] << ", " << result[1] << "]" << std::endl;

  return 0;
}
