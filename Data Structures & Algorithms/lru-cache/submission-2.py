

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.cache_len = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            temp = self.cache.pop(key)
            self.cache[key] = temp
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache_len -= 1

        elif self.cache_len >= self.capacity:
            self.cache.popitem(last = False)
            self.cache_len -= 1


        self.cache[key] = value
        self.cache_len += 1
        
            
        
