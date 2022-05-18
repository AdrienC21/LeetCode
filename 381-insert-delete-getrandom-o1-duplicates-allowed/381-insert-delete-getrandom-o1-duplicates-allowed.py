import numpy as np
from collections import defaultdict
class RandomizedCollection:

    def __init__(self):
        self.freqs = defaultdict(int)
        self.len = 0
        self.elements = []

    def insert(self, val: int) -> bool:
        to_return = not(val in self.freqs)
        self.len += 1
        self.freqs[val] += 1
        self.elements.append(val)
        return to_return

    def remove(self, val: int) -> bool:
        if not(val in self.freqs):
            return False
        self.len -= 1
        self.freqs[val] -= 1
        self.elements.remove(val)  # remove one occurence of val in elements
        if not(self.freqs[val]):  # no longer val in freqs, remove the key
            self.freqs.pop(val)
        return True

    def getRandom(self) -> int:
        j = np.random.randint(self.len)
        return self.elements[j]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()