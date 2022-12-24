class Solution:
    def __init__(self):
        self.cache = {0: 0,
                      1: 1,
                      2: 2}
        self.cache2 = {0: 0,
                       1: 0,
                       2: 1}
        self.mod = (10 ** 9) + 7
    def numTilings(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        res = self.numTilings(n-1) + self.numTilings(n-2) + 2 * self.numTilings2(n-1)
        res %= self.mod
        self.cache[n] = res
        return res
    def numTilings2(self, n: int) -> int:
        if n in self.cache2:
            return self.cache2[n]
        res = self.numTilings(n-2) + self.numTilings2(n-1)
        res %= self.mod
        self.cache2[n] = res
        return res
