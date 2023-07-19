#include <any>
#include <iostream>
#include <string>
#include <tuple>

/**
 *  ========== C++ 17 ===========
 *	1: structure binding
 *	2: optional
 *	3: variant
 *	4: any
 *	5: async
 *	6: string_view
 *	7: basic_string
 *	   if < 16 will stored in stack, otherwise will be on heap
 */

void AnyType() {

  std::any data;
  data = 2;
  data = "Joma";
}

void ShiftOperator() {

  int x = 1024 >> 8;
  std::cout << x << std::endl;
}

std::tuple<std::string, int> CreatePerson() { return {"Joma", 24}; }

int main() {
  // auto person = CreatePerson();
  // std::string &name = std::get<0>(person);
  // int age = std::get<1>(person);

  // c++17 structured binding
  auto [name, age] = CreatePerson();
  std::cout << name << " " << age << std::endl;

  ShiftOperator();
}
