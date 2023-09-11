#include <iostream>
#include <unordered_map>
#include <vector>

int majorityElement(std::vector<int> &nums) {
  std::unordered_map<int, int> map;
  for (int i = 0; i < nums.size(); i++) {
    map[nums[i]]++;
  }
  int key = 0, val = 0;
  for (auto m : map) {
    int k = m.first;
    int v = m.second;
    if (v > val) {
      val = v;
      key = k;
    }
  }
  return key;
}

int main() {
  std::vector<int> nums = {1, 2, 3, 3, 3, 2, 1};
  int result = majorityElement(nums);
  std::cout << result << std::endl;
  return 0;
}
