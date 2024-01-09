class LRUCache(object):
    class Node:
        def __init__(self, k, v):
            self.key = k
            self.value = v
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.size = capacity
        self.head = None
        self.tail = None
        self.cache = {}

    def add_to_head(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.add_to_head(node)
        else:
            if len(self.cache) >= self.size:
                del_key = self.tail.key
                del self.cache[del_key]
                self.remove_node(self.tail)

            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self.add_to_head(new_node)


lru_cache = LRUCache(3)

lru_cache.put(1, 1)
lru_cache.put(2, 2)
lru_cache.put(3, 3)

for key, node in lru_cache.cache.items():
    print(f'{key}: {node.value}')

print()
lru_cache.put(4, 4)
lru_cache.put(2, 2)
lru_cache.put(3, 3)

lru_cache.get(4)
lru_cache.put(5, 5)
lru_cache.put(6, 6)

for key, node in lru_cache.cache.items():
    print(f'{key}: {node.value}')
