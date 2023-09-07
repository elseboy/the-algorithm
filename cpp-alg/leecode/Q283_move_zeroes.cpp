#include <iostream>
#include <vector>

void moveZeroes(std::vector<int> &nums) {
  // for (int i = 0; i < nums.size(); i++) {
  //  for (int j = i + 1; j < nums.size(); j++) {
  //  if (nums[i] == 0) {
  //  int temp = nums[i];
  //  nums[i] = nums[j];
  //  nums[j] = temp;
  //     }
  //   }
  // }

  // track non-zero numbers
  int count = 0;
  for (int i = 0; i < nums.size(); i++) {
    if (nums[i] != 0)
      nums[count++] = nums[i];
  }
  // replace other slots to 0
  for (int i = count; i < nums.size(); i++) {
    nums[i] = 0;
  }
}

int main() {
  std::vector<int> nums = {1, 0, 3, 4, 0, 9, 10};
  moveZeroes(nums);
  for (int num : nums)
    std::cout << num << " ";
}
