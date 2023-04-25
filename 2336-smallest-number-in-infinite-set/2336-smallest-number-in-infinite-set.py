class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.added_back = []
        self.added_back_set = set()

    def popSmallest(self) -> int:
        if self.added_back:
            res = self.added_back.pop(0)
            self.added_back_set.remove(res)
            return res
        res = self.smallest
        self.smallest += 1
        return res
        
    def addBack(self, num: int) -> None:
        if (num < self.smallest) and (num not in self.added_back_set):
            self.added_back_set.add(num)
            self.added_back.append(num)
            i = len(self.added_back) - 1
            while (i > 0) and (self.added_back[i] < self.added_back[i-1]):
                self.added_back[i], self.added_back[i-1] = self.added_back[i-1], self.added_back[i]
                i -= 1


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)