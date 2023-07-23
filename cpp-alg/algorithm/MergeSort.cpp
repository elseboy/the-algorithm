#include <array>
#include <iostream>
#include <vector>

void ArrayMerge(std::array<int, 7> &arr, int left, int middle, int right) {
  int n1 = middle - left + 1;
  int n2 = right - middle;

  std::array<int, 7> L, R;

  for (int i = 0; i < n1; i++)
    L[i] = arr[left + i];

  for (int j = 0; j < n2; j++)
    R[j] = arr[middle + 1 + j];

  int i = 0, j = 0, k = left;

  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = R[j];
      j++;
    }
    k++;
  }

  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }

  while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
  }
}

void ArrayMergeSort(std::array<int, 7> &arr, int left, int right) {
  if (left < right) {
    int middle = left + (right - left) / 2;
    ArrayMergeSort(arr, left, middle);
    ArrayMergeSort(arr, middle + 1, right);
    ArrayMerge(arr, left, middle, right);
  }
}

void VectorMerge(std::vector<int> &vec, int left, int middle, int right) {
  int n1 = middle - left + 1;
  int n2 = right - middle;

  std::vector<int> L(n1), R(n2);

  for (int i = 0; i < n1; i++)
    L[i] = vec[left + i];

  for (int j = 0; j < n2; j++)
    R[j] = vec[middle + 1 + j];

  int i = 0, j = 0, k = left;

  while (i < n1 && j < n2) {
    if (L[i] >= R[j]) {
      vec[k] = L[i];
      i++;
    } else {
      vec[k] = R[j];
      j++;
    }
    k++;
  }

  while (i < n1) {
    vec[k] = L[i];
    i++;
    k++;
  }
  while (j < n2) {
    vec[k] = R[j];
    j++;
    k++;
  }
}

void VectorMergeSort(std::vector<int> &vec, int left, int right) {
  if (left < right) {
    int middle = left + (right - left) / 2;
    VectorMergeSort(vec, left, middle);
    VectorMergeSort(vec, middle + 1, right);
    VectorMerge(vec, left, middle, right);
  }
}

int main() {
  std::array<int, 7> array = {64, 34, 25, 12, 22, 11, 90};
  ArrayMergeSort(array, 0, array.size() - 1);
  for (int num : array)
    std::cout << num << " ";

  std::cout << std::endl;

  std::vector<int> vector = {64, 34, 25, 12, 22, 11, 90};
  VectorMergeSort(vector, 0, vector.size() - 1);
  for (int num : vector)
    std::cout << num << " ";
  return 0;
}
