"""
Design a Least Recently Used Cache which uses int key value pair.
"""

from collections import OrderedDict

class LRUCacheWithOrderedDict:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache: # O(1) for the average case and O(n) for the worst case where collisions in the hash table, resulting in linear search time within hash buckets
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key) # must check key in cache before move_to_newest
        elif len(self.cache) == self.capacity:
            self.cache.popitem(0)

        self.cache[key] = value

    def print_all(self) -> None:
        print(self.cache.items())

# cache = LRUCacheWithOrderedDict(3)
# cache.put(1,10)
# cache.put(2,20)
# cache.put(3,30)
# cache.get(1)
# cache.put(2,200)

# cache.print_all() # odict_items([(3, 30), (1, 10), (2, 200)])

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key: int) -> int:
        if self.cache.get(key) is None:
            return -1

        self.move_to_newest(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache.get(key):
            self.remove_key(key)
        elif len(self.cache) >= self.capacity:
            self.remove_oldest()

        self.queue.append(key)
        self.cache[key] = value

    def remove_key(self,key):
        self.queue.remove(key)
        del self.cache[key]

    def remove_oldest(self):
        last = self.queue.pop(0)
        del self.cache[last]

    def move_to_newest(self, key):
        if self.cache.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        
    def print_all(self) -> None:
        for i in self.queue:
            print(i, self.cache[i])

cache = LRUCache(3)
cache.put(1,10)
cache.put(2,20)
cache.put(3,30)
cache.get(1)
cache.put(2,200)

cache.print_all() # 3 30, 1 10, 2 20
