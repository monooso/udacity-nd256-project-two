from collections import deque


class LeastRecentlyUsedStack(object):
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        """Return a boolean indicating whether the stack is empty"""
        return len(self.items) == 0

    def pop(self):
        """Return the least recently used item"""
        if self.is_empty():
            return None
        value = self.items.popleft()
        return self.pop() if value in self.items else value

    def push(self, value):
        """Add an item to the LRU stack"""
        self.items.append(value)


class LeastRecentlyUsedCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.lru = LeastRecentlyUsedStack()

    def contains(self, key):
        """Return a boolean indicating whether an item with the given key exists in the cache"""
        return key in self.cache

    def is_full(self):
        """Return a boolean indicating whether the cache is full"""
        return len(self.cache) >= self.capacity

    def get(self, key):
        """Retrieve an item with the given key from the cache"""
        if self.contains(key):
            self.lru.push(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        """Add the given key / value pair to the cache"""
        if self.is_full():
            lru_key = self.lru.pop()
            if lru_key is not None:
                del self.cache[lru_key]

        self.lru.push(key)
        self.cache[key] = value


# -------------------
# Tests for LRU stack
# -------------------
stack = LeastRecentlyUsedStack()

assert stack.is_empty() is True

stack.push('a')
stack.push('b')
stack.push('c')
stack.push('b')

assert stack.is_empty() is False
assert stack.pop() == 'a'
assert stack.pop() == 'c'
assert stack.pop() == 'b'
assert stack.is_empty() is True

# -------------------
# Tests for LRU cache
# -------------------
cache = LeastRecentlyUsedCache(5)

cache.set('a', 1)
cache.set('b', 2)
cache.set('c', 3)
cache.set('d', 4)

assert cache.get('b') == 2
assert cache.get('a') == 1
assert cache.get('z') == -1

cache.set('e', 5)
cache.set('f', 6)   # Replaces 'c' in the cache

assert cache.get('f') == 6
assert cache.get('c') == -1
