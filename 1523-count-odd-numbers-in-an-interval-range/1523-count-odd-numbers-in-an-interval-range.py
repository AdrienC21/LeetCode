class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if not(diff):
            return 1 if (low % 2) == 1 else 0
        if diff % 2 == 0:
            return (diff // 2) + 1 if (low % 2) == 1 else diff // 2
        return (diff // 2) + 1
