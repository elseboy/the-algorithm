#include <iostream>
#include <unordered_map>

class LRUCache {

private:
  struct Node {
    int key;
    int value;
    Node *prev;
    Node *next;

    Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
  };

  int size;
  Node *head;
  Node *tail;
  std::unordered_map<int, Node *> cache;

public:
  LRUCache(int cap) : size(cap), head(nullptr), tail(nullptr) {}

  void addToHead(Node *node) {
    if (!head) {
      head = tail = node;
    } else {
      node->next = head;
      head->prev = node;
      head = node;
    }
  }

  void remove(Node *node) {
    if (node->prev) {
      node->prev->next = node->next;
    } else {
      head = node->next;
    }

    if (node->next) {
      node->next->prev = node->prev;
    } else {
      tail = node->prev;
    }
  }

  int get(int key) {
    if (cache.find(key) != cache.end()) {
      Node *node = cache[key];
      remove(node);
      addToHead(node);
      return node->value;
    }
    return -1;
  }

  void put(int key, int value) {
    if (cache.find(key) != cache.end()) {
      Node *node = cache[key];
      node->value = value;
      remove(node);
      addToHead(node);
    } else {
      if (cache.size() >= size) {
        cache.erase(tail->key);
        remove(tail);
      }

      Node *newNode = new Node(key, value);
      cache[key] = newNode;
      addToHead(newNode);
    }
  }

  void display() {
    Node *current = head;
    while (current) {
      std::cout << current->key << " ";
      current = current->next;
    }
    std::cout << std::endl;
  }
};

int main() {
  LRUCache lru(3);
  lru.put(1, 1);
  lru.put(2, 2);
  lru.put(3, 3);
  lru.put(4, 4);

  lru.get(2);

  lru.display();
  return 0;
}
