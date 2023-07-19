#include <iostream>
using namespace std;
#define LOG(x) cout << x << endl

void intArray() {
  int arr[5];
  for (int i = 0; i < 5; i++) {
    arr[i] = i + 1;
    cout << arr[i] << " ";
  }

  cout << endl;

  int *another = new int[5];
  for (int i = 0; i < 5; i++) {
    another[i] = i + 1;
    cout << another[i] << " ";
  }
  delete[] another;

  cout << endl;
}

void charArray() {
  const char *name = "joma";
  cout << name << endl;

  string anotherName = "emma";
  cout << anotherName << endl;

  string newName = string(name) + " " + anotherName;
  cout << newName << endl;
}

void MultArray() {
  int *array = new int(50);
  int **mult_Array = new int(50);
}

int main() {
  LOG("I HATE C++");
  intArray();
  charArray();
}
