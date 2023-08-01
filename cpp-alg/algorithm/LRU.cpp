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
    Node *newNode = new Node(key, value);
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

public:
  LRUCache(int capacity) : capacity(capacity), head(nullptr), tail(nullptr) {}

  int get(int key) {
    if (cache.find(key) != cache.end()) {
      Node *node = cache[key];
      moveToFront(node);
      return node->value;
    }
    return -1;
  }

  void put(int key, int value) {
    if (cache.find(key) != cache.end()) {
      Node *node = cache[key];
      node->value = value;
      moveToFront(node);
    } else {
      if (cache.size() >= capacity)
        deleteTail();

      addToFront(key, value);
      cache[key] = head;
    }
  }

  ~LRUCache() {
    while (head) {
      Node *temp = head->next;
      delete head;
      head = temp;
    }
  }
};

int main() {
  LRUCache lruCache(3);
  lruCache.put(1, 1);
  lruCache.put(2, 2);
  lruCache.put(3, 3);

  std::cout << lruCache.get(1) << std::endl;
  std::cout << lruCache.get(2) << std::endl;
  return 0;
}
