class MyHashMap:

    def __init__(self):
        self.hashmap = [-1]
        self.lenHashMap = 1

    def put(self, key: int, value: int) -> None:
        if key < self.lenHashMap:
            self.hashmap[key] = value
        else:
            self.hashmap.extend([-1 for _ in range(key-self.lenHashMap+1)])
            self.hashmap[key] = value
            self.lenHashMap = key + 1
    def get(self, key: int) -> int:
        if key < self.lenHashMap:
            return self.hashmap[key]
        return -1

    def remove(self, key: int) -> None:
        if key < self.lenHashMap:
            self.hashmap[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)