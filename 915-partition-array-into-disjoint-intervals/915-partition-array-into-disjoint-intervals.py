from itertools import accumulate
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxr = list(accumulate(nums, max))[:-1]
        minl = list(accumulate(nums[::-1], min))[::-1][1:]
        for i, (x,y) in enumerate(list(zip(maxr, minl))):
            if x <= y:
                return (i + 1)