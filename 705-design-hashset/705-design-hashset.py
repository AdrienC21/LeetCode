class MyHashSet:

    def __init__(self):
        self.set = [False]
        self.lenSet = 1

    def add(self, key: int) -> None:
        if key < self.lenSet:
            self.set[key] = True
        else:
            self.set.extend([False for _ in range(key-self.lenSet+1)])
            self.set[key] = True
            self.lenSet = key + 1

    def remove(self, key: int) -> None:
        if key < self.lenSet:
            self.set[key] = False

    def contains(self, key: int) -> bool:
        if key < self.lenSet:
            return self.set[key]
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)