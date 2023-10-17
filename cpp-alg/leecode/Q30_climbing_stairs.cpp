#include <iostream>

int climbStairs(int n) {
  int p = 0, q = 0, r = 1;
  for (int i = 1; i <= n; i++) {
    p = q;
    q = r;
    r = p + q;
  }
  return r;
}

int main() {
  int n = 4;
  int result = climbStairs(n);
  std::cout << result << std::endl;
}
