#include <iostream>
#include <vector>

void bubbleSort(std::vector<int> &arr) {

  int size = arr.size();
  bool swapped;

  for (int i = 0; i < size - 1; i++) {
    swapped = false;

    for (int j = 0; j < size - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        std::swap(arr[j], arr[j + 1]);
        swapped = true;
      }
    }

    if (!swapped) {
      break;
    }
  }
}

int main() {

  std::vector<int> numbers = {64, 34, 25, 12, 22, 11, 90};

  bubbleSort(numbers);

  for (int num : numbers)
    std::cout << num << " ";

  return 0;
}
