class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]
        dp[-1] = 0
        def recSearch(i: int) -> int:
            nonlocal dp, n
            
            if dp[i] == -1:  # never calculated
                maxJump = nums[i]
                res = n + 1
                for j in range(min(maxJump, n-1-i), 0, -1):
                    res = min(res, 1 + recSearch(i+j))
                dp[i] = res
            return dp[i]

        return recSearch(0)
