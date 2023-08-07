#include <iostream>

struct Node {
  int value;
  Node *prev;
  Node *next;
  Node(int value) : value(value), prev(nullptr), next(nullptr) {}
};

class DoublyLinkedList {
private:
  Node *head;
  Node *tail;

public:
  DoublyLinkedList() : head(nullptr), tail(nullptr) {}

  // add to tail
  void addToTail(int value) {
    Node *newNode = new Node(value);
    if (head == nullptr) {
      head = tail = newNode;
    } else {
      newNode->prev = tail;
      tail->next = newNode;
      tail = newNode;
    }
  }

  // add to head
  void addToHead(int value) {
    Node *newNode = new Node(value);

    if (head == nullptr) {
      head = tail = newNode;
    } else {
      newNode->next = head;
      head->prev = newNode;
      head = newNode;
    }
  }

  void display() {
    Node *current = head;
    while (current != nullptr) {
      std::cout << current->value << " ";
      current = current->next;
    }
    std::cout << std::endl;
  }
};

int main() {
  DoublyLinkedList list;

  list.addToTail(1);
  list.addToTail(2);
  list.addToTail(3);

  list.addToHead(4);

  list.display();
}
