from collections import Counter
class Solution:
    def __init__(self):
        self.counters = []
        power = 1
        for i in range(0, 30):  # 2**29 < 10**9 < 2**30
            self.counters.append(Counter(str(power)))
            power *= 2
            
    def reorderedPowerOf2(self, n: int) -> bool:
        n_c = Counter(str(n))
        for c in self.counters:
            if n_c == c:
                return True
        return False
