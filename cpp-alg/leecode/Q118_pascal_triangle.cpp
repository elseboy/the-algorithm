#include <iostream>
#include <vector>

std::vector<std::vector<int>> generate(int numRows) {
  std::vector<std::vector<int>> ans = {{1}};
  for (int i = 1; i < numRows; i++) {
    std::vector<int> temp = ans[ans.size() - 1];
    temp.insert(temp.begin(), 0);
    temp.emplace_back(0);
    std::vector<int> nextRow = {};
    for (int j = 0; j < ans.size() + 1; j++) {
      nextRow.emplace_back(temp[j] + temp[j + 1]);
    }
    ans.emplace_back(nextRow);
  }
  return ans;
}

int main() {
  int num = 5;
  std::vector<std::vector<int>> result = generate(num);

  for (auto row : result) {
    for (int val : row) {
      std::cout << val << " ";
    }
    std::cout << std::endl;
  }
  return 0;
}
