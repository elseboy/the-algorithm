#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>

bool isValid(std::string str) {
  if (str.size() % 2 == 1)
    return false;
  std::unordered_map<char, char> pairs = {{')', '('}, {']', '['}, {'}', '{'}};
  std::stack<char> stack;
  for (char ch : str) {
    if (pairs.count(ch)) {
      if (stack.empty() || stack.top() != pairs[ch])
        return false;
      stack.pop();
    } else {
      stack.push(ch);
    }
  }
  return stack.empty();
}

int main() {
  std::string str = "()[]{}";
  bool result = isValid(str);
  std::cout << result << std::endl;
  return 0;
}
