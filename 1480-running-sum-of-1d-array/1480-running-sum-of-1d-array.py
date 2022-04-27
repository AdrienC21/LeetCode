class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        last = nums[0]
        res = [last]
        for i in range(1, len(nums)):
            last += nums[i]
            res.append(last)
        return res