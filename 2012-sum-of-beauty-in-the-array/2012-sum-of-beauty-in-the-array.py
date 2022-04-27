from itertools import accumulate
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0
        sum_beauty = 0
        maxl = list(accumulate(nums, max))[:-2]
        minr = list(accumulate(nums[::-1], min))[::-1][2:]
        up = nums[2:]
        down = nums[:-2]
        zipped = list(zip(nums[1:-1], maxl, minr, up, down))
        for (n, ml, mr, u, d) in zipped:
            if (ml < n) and (n < mr):
                sum_beauty += 2
            elif (d < n) and (n < u):
                sum_beauty += 1
        return sum_beauty