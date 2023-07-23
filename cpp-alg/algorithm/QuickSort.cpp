#include <array>
#include <iostream>
#include <vector>

void ArrayQuickSort(std::array<int, 7> &arr, int low_index, int high_index) {

  if (low_index >= high_index)
    return;

  int pivot = arr[high_index];
  int left_pointer = low_index;
  int right_pointer = high_index;
  int meet_pointer;
  while (left_pointer < right_pointer) {
    while (arr[left_pointer] <= pivot && left_pointer < right_pointer)
      left_pointer++;
    while (arr[right_pointer] >= pivot && left_pointer < right_pointer)
      right_pointer--;
    std::swap(arr[left_pointer], arr[right_pointer]);
  }
  // meet_pointer = right_pointer
  // this is also ok since they are pointing to the same index by this step
  meet_pointer = left_pointer;
  std::swap(arr[meet_pointer], arr[high_index]);
  ArrayQuickSort(arr, low_index, left_pointer - 1);
  ArrayQuickSort(arr, left_pointer + 1, high_index);
}

void VectorQuickSort(std::vector<int> &vec, int low_index, int high_index) {

  if (low_index >= high_index)
    return;

  int pivot = vec[high_index];
  int left_pointer = low_index;
  int right_pointer = high_index;
  int meet_pointer;
  while (left_pointer < right_pointer) {
    while (vec[left_pointer] >= pivot && left_pointer < right_pointer)
      left_pointer++;
    while (vec[right_pointer] <= pivot && left_pointer < right_pointer)
      right_pointer--;
    std::swap(vec[left_pointer], vec[right_pointer]);
  }
  meet_pointer = right_pointer;
  std::swap(vec[meet_pointer], vec[high_index]);
  VectorQuickSort(vec, low_index, left_pointer - 1);
  VectorQuickSort(vec, left_pointer + 1, high_index);
}

int main() {
  std::array<int, 7> array = {64, 34, 25, 19, 22, 11, 90};
  ArrayQuickSort(array, 0, array.size() - 1);
  for (int num : array)
    std::cout << num << " ";

  std::cout << std::endl;

  std::vector<int> vector = {64, 34, 25, 12, 22, 11, 90};
  VectorQuickSort(vector, 0, vector.size() - 1);
  for (int num : vector)
    std::cout << num << " ";
  return 0;
}
