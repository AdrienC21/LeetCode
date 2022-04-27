from functools import reduce
class Solution:
    def recSearch(self, n: int, d: dict):
        if n == 1:
            return True
        elif n in d:  # cycle
            return False
        else:
            d[n] = True
            return self.recSearch(reduce(lambda x,y: x+y, map(lambda x: int(x)**2, list(str(n)))), d)
    def isHappy(self, n: int) -> bool:
        d = {}
        return self.recSearch(n, d)