#include <iostream>
#include <unordered_map>
#include <vector>

int singleNumber(std::vector<int> &nums) {
  std::unordered_map<int, int> map = {};
  for (int i = 0; i < nums.size(); i++) {
    map[nums[i]]++;
  }
  for (auto pair : map) {
    if (pair.second == 1)
      return pair.first;
  }
  return -1;
}

int main() {

  std::vector<int> nums = {2, 3, 2, 3, 1};
  int result = singleNumber(nums);
  std::cout << result << std::endl;
  return 0;
}
