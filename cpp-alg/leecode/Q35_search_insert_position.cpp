#include <iostream>
#include <vector>

int searchInsert(std::vector<int> &nums, int target) {
  int n = nums.size();
  int left = 0, right = n - 1;
  while (left <= right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] < target)
      left = mid + 1;
    else
      right = mid - 1;
  }
  return left;
}

int main() {
  std::vector<int> array = {1, 3, 5, 6};
  int target = 7;
  int ans = searchInsert(array, target);
  std::cout << ans << std::endl;
}
