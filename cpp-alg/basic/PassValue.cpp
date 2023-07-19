#include <iostream>
#include <string>

void incrementByValue(int x) { x++; }

void incrementByPointer(int *ptr) { (*ptr)++; }

void incrementByReference(int &ref) { ref++; }

// void Print(int value) { std::cout << value << std::endl; }

// void Print(std::string value) { std::cout << value << std::endl; }

// void Print(float value) { std::cout << value << std::endl; }

template <typename T> void Print(T value) { std::cout << value << std::endl; }

int main() {
  int x = 5;

  incrementByValue(x);
  std::cout << "passing by value: " << x << std::endl;

  incrementByPointer(&x);
  std::cout << "passing by pointer: " << x << std::endl;

  incrementByReference(x);
  std::cout << "passing by reference: " << x << std::endl;

  Print(10);
  Print("this is from print");
  Print(5.0f);
  return 0;
}
