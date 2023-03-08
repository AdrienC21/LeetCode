class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        while i < j:
            m = i + (j - i) // 2  # that's our k
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / m)
            if hours > h:
                i = m + 1
            else:
                j = m
        return i
