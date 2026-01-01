from node import Node
import json
import time

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.hits = 0
        self.misses = 0

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_expired(self):
        for key in list(self.cache.keys()):
            node = self.cache[key]
            if node.is_expired():
                self._remove(node)
                del self.cache[key]

    def get(self, key):
        self._remove_expired()

        if key not in self.cache:
            self.misses += 1
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        self.hits += 1
        return node.value

    def put(self, key, value, ttl=None):
        self._remove_expired()

        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value, ttl)
        self.cache[key] = node
        self._add_front(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

    def delete(self, key):
        if key in self.cache:
            self._remove(self.cache[key])
            del self.cache[key]
            return True
        return False

    def clear(self):
        self.cache.clear()
        self.head.next = self.tail
        self.tail.prev = self.head

    def resize(self, new_capacity):
        self.capacity = new_capacity
        while len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

    def display(self):
        curr = self.head.next
        print("Cache (MRU → LRU):")
        while curr != self.tail:
            print(f"{curr.key}:{curr.value}", end="  ")
            curr = curr.next
        print()

    def stats(self):
        return {"hits": self.hits, "misses": self.misses}
