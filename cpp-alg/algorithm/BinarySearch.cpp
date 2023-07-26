#include <array>
#include <iostream>
#include <vector>

int ArrayBinarySearch(std::array<int, 10> &array, int target) {
  int left = 0;
  int right = array.size() - 1;

  while (left <= right) {
    int mid = left + (right - left) / 2;
    if (array[mid] == target) {
      return mid;
    } else if (array[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
}

int VectorBinarySearch(std::vector<int> &vector, int target) {
  int left = 0;
  int right = vector.size() - 1;

  while (left <= right) {
    int mid = left + (right - left) / 2;
    if (vector[mid] == target) {
      return mid;
    } else if (vector[left] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
}

int main() {
  std::array<int, 10> array = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
  int arr_target = 11;
  int arr_index = ArrayBinarySearch(array, arr_target);
  std::cout << "target index found: " << arr_index << std::endl;

  std::vector<int> vector = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
  int vec_target = 9;
  int vec_index = VectorBinarySearch(vector, vec_target);
  std::cout << "target index found: " << vec_index << std::endl;
  return 0;
}
