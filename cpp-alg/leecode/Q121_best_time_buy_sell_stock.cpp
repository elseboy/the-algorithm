#include <iostream>
#include <vector>

int maxProfit(std::vector<int> &prices) {
  int minPrice = 1e9, maxProfit = 0;
  for (auto price : prices) {
    minPrice = std::min(price, minPrice);
    maxProfit = std::max(maxProfit, price - minPrice);
  }
  return maxProfit;
}

int main() {

  std::vector<int> nums = {7, 1, 5, 3, 6, 4};
  int result = maxProfit(nums);
  std::cout << result << std::endl;
}
