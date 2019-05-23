class LRUCache:
    """ Second iteration """

    def __init__(self, capacity: int = None):
        self.cache = dict()
        self.cache_list = list()
        self.max_capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache_list.remove(key)
            self.cache_list.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache_list) == self.max_capacity:
            id_to_remove = self.cache_list.pop(0)
            self.cache.pop(id_to_remove)
        elif key in self.cache:
            self.cache[key] = value
            self.cache_list.remove(key)
            self.cache_list.append(key)
        self.cache[key] = value
        self.cache_list.append(key)


if __name__ == "__main__":
    cache = LRUCache(4)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)
    cache.put(5, 5)
    print(cache.cache)
    print(cache.cache_list)
    cache.get(2)
    print(cache.cache_list)
