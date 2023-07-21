#include <array>
#include <iostream>
#include <vector>

void vectorBubbleSort(std::vector<int> &arr) {

  int size = arr.size();
  bool swapped;

  for (int i = 0; i < arr.size() - 1; i++) {
    swapped = false;

    for (int j = 1; j < arr.size() - 1; j++) {
      if (arr[j] < arr[j - 1]) {
        int temp;
        temp = arr[j];
        arr[j] = arr[j - 1];
        arr[j - 1] = temp;
        swapped = true;
      }
    }

    if (!swapped)
      break;
  }
}

void arrayBubbleSort(std::array<int, 7> &arr) {
  bool swapped;

  for (int i = 0; i < arr.size() - 1; i++) {
    for (int j = 1; j < arr.size(); j++) {
      if (arr[j] > arr[j - 1]) {
        int temp;
        temp = arr[j];
        arr[j] = arr[j - 1];
        arr[j - 1] = temp;
        swapped = true;
      }
    }

    if (!swapped)
      break;
  }
}

int main() {

  std::vector<int> vectorNumbers = {64, 34, 25, 12, 22, 11, 90};
  vectorBubbleSort(vectorNumbers);
  for (int num : vectorNumbers)
    std::cout << num << " ";

  std::cout << std::endl;

  std::array<int, 7> arrayNumbers = {64, 34, 25, 12, 22, 11, 90};
  arrayBubbleSort(arrayNumbers);
  for (int num : arrayNumbers)
    std::cout << num << " ";
  return 0;
}
