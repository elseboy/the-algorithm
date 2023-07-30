#include <iostream>
#include <unordered_map>

class LRUCache {
  struct Node {
    int key;
    int value;
    Node *prev;
    Node *next;
    Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
  };

  int capacity;
  std::unordered_map<int, Node *> cache;
  Node *head;
  Node *tail;

  void moveToFront(Node *node) {
    if (node == nullptr)
      return;

    node->prev->next = node->next;
    if (node == tail)
      tail = node->prev;
    else
      node->next->prev = node->prev;

    node->prev = nullptr;
    node->next = head;
    head->prev = node;
    head = node;
  }

  void addToFront(int key, int value) {
    Node *newNode = new Npde(key, value);
    if (!head) {
      head = tail = newNode;
    } else {
      newNode->next = head;
      head->prev = newNode;
      head = newNode;
    }
  }

  void deleteTail() {
    if (!tail)
      return;

    cache.erase(tail->key);

    if (head == tail) {
      delete tail;
      head = tail = nullptr;
    } else {
      tail = tail->prev;
      delete tail->next;
      tail->next = nullptr;
    }
  }
};

int main() { return 0; }
