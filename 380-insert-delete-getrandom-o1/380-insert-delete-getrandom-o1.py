import numpy as np
class RandomizedSet:

    def __init__(self):
        self.elements = []
        self.set = set()
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.add(val)
        self.elements.append(val)
        self.len += 1
        return True

    def remove(self, val: int) -> bool:
        if not(val in self.set):
            return False
        self.set.discard(val)
        self.elements.remove(val)
        self.len -= 1
        return True

    def getRandom(self) -> int:
        j = np.random.randint(self.len)
        return self.elements[j]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()