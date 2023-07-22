#include <array>
#include <iostream>
#include <vector>

void ArraySelectionSort(std::array<int, 7> &arr) {

  for (int i = 0; i < arr.size() - 1; i++) {
    int smallest_index = i;
    for (int j = smallest_index + 1; j < arr.size(); j++) {
      if (arr[j] < arr[smallest_index]) {
        smallest_index = j;
      }
    }
    if (smallest_index != i) {
      int temp = arr[i];
      arr[i] = arr[smallest_index];
      arr[smallest_index] = temp;
    }
  }
}

void VectorSelectionSort(std::vector<int> &arr) {
  for (int i = 0; i < arr.size() - 1; i++) {
    int biggest_index = i;
    for (int j = biggest_index + 1; j < arr.size(); j++) {
      if (arr[j] > arr[biggest_index]) {
        biggest_index = j;
      }
    }
    if (biggest_index != i) {
      int temp = arr[i];
      arr[i] = arr[biggest_index];
      arr[biggest_index] = temp;
    }
  }
}

int main() {
  std::array<int, 7> array = {64, 34, 25, 12, 22, 11, 90};
  ArraySelectionSort(array);
  for (int num : array)
    std::cout << num << " ";

  std::cout << std::endl;

  std::vector<int> vector = {64, 34, 25, 12, 22, 11, 90};
  VectorSelectionSort(vector);
  for (int num : vector)
    std::cout << num << " ";

  return 0;
}
