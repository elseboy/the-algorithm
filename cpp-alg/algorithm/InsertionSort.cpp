#include <array>
#include <iostream>
#include <vector>

void ArrayInsertionSort(std::array<int, 7> &arr) {
  for (int i = 1; i < arr.size(); i++) {
    int curr = arr[i];
    int j = i - 1;

    while (j >= 0 && arr[j] > curr) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = curr;
  }
}

void VectorInsertionSort(std::vector<int> &arr) {

  for (int i = 1; i < arr.size(); i++) {
    int curr = arr[i];
    int j = i - 1;

    while (j >= 0 && arr[j] < curr) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = curr;
  }
}

int main() {

  std::array<int, 7> arrayNumbers = {64, 34, 25, 12, 22, 11, 1};
  ArrayInsertionSort(arrayNumbers);
  for (int elem : arrayNumbers)
    std::cout << elem << " ";

  std::cout << std::endl;

  std::vector<int> vectorNumbers = {64, 34, 25, 12, 22, 11, 1};
  VectorInsertionSort(vectorNumbers);
  for (int elem : vectorNumbers)
    std::cout << elem << " ";

  return 0;
}
