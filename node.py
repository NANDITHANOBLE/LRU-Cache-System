import time

class Node:
    def __init__(self, key, value, ttl=None):
        self.key = key
        self.value = value
        self.ttl = ttl
        self.timestamp = time.time()
        self.prev = None
        self.next = None

    def is_expired(self):
        if self.ttl is None:
            return False
        return (time.time() - self.timestamp) > self.ttl
