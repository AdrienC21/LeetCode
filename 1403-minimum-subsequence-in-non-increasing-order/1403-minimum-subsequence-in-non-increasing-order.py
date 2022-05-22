class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        s = sum(nums)
        sequence_sum = 0
        i = n
        res = []
        while (sequence_sum <= s):
            i -= 1
            s -= nums[i]
            sequence_sum += nums[i]
            res.append(nums[i])
        return res