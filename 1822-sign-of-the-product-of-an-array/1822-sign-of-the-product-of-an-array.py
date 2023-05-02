class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for n in nums:
            if not(n):
                return 0
            if n < 0:
                res *= -1
        return res
