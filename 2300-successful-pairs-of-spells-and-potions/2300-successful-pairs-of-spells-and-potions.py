class Solution:
    def __init__(self):
        self.cache = {}
    
    def calc_success(self, s: int, potions: List[int], success: int) -> int:
        n = len(potions)
        i = 0
        j = n - 1
        while i < j:
            m = (i + j) // 2
            if (potions[m] * s) >= success:
                j = m
            else:
                i = m + 1
        if (potions[i] * s) < success:
            return 0
        return n - i

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for s in spells:
            if s in self.cache:
                res.append(self.cache[s])
            else:
                nb_success = self.calc_success(s, potions, success)
                self.cache[s] = nb_success
                res.append(nb_success)
        return res