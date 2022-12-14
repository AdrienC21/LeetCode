class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None for _ in range(n)]
        dp[n-1] = nums[n-1]
        if n > 1:
            dp[n-2] = max(nums[n-1], nums[n-2])
        for i in range(n-3, -1, -1):
            dp[i] = max(dp[i+2]+nums[i], dp[i+1])
        return dp[0]
