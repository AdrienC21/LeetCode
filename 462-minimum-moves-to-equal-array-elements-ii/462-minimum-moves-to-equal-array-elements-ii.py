from statistics import median
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        m = int(median(nums))
        res = 0
        for n in nums:
            res += abs(n - m)
        return res
