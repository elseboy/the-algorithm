#include <array>
#include <iostream>
#include <vector>

void ArrayHeapify(std::array<int, 7> &arr, int n, int root) {
  int largest = root;
  int left_child = 2 * root + 1;
  int right_child = 2 * root + 2;

  if (left_child < n && arr[largest] < arr[left_child])
    largest = left_child;
  if (right_child < n && arr[largest] < arr[right_child])
    largest = right_child;

  if (largest != root) {
    std::swap(arr[largest], arr[root]);
    ArrayHeapify(arr, root, largest);
  }
}

void ArrayHeapSort(std::array<int, 7> &arr) {
  int n = arr.size();

  for (int i = n / 2 - 1; i >= 0; i--)
    ArrayHeapify(arr, n, i);

  for (int i = n - 1; i > 0; i--) {
    std::swap(arr[0], arr[i]);
    ArrayHeapify(arr, i, 0);
  }
}

void VectorHeapify(std::vector<int> &vec, int n, int root) {
  int largest = root;
  int left_child = 2 * root + 1;
  int right_child = 2 * root + 2;

  if (left_child < n && vec[left_child] < vec[largest])
    largest = left_child;
  if (right_child < n && vec[right_child] < vec[largest])
    largest = right_child;

  if (largest != root) {
    std::swap(vec[root], vec[largest]);
    VectorHeapify(vec, n, largest);
  }
}

void VectorHeapSort(std::vector<int> &vec) {
  int n = vec.size();

  for (int i = n / 2 - 1; i >= 0; i--)
    VectorHeapify(vec, n, i);

  for (int i = n - 1; i > 0; i--) {
    std::swap(vec[0], vec[i]);
    VectorHeapify(vec, i, 0);
  }
}

int main() {

  std::array<int, 7> array = {64, 34, 25, 12, 22, 11, 90};
  ArrayHeapSort(array);

  for (int num : array)
    std::cout << num << " ";

  std::cout << std::endl;

  std::vector<int> vector = {64, 34, 25, 12, 22, 11, 90};
  VectorHeapSort(vector);

  for (int num : vector)
    std::cout << num << " ";

  return 0;
}
