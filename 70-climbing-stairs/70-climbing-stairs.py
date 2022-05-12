class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [-1 for _ in range(n+1)]  # last step included
        dp[n-1] = 1
        dp[n] = 1
        def recSearch(i: int) -> int:
            nonlocal dp
            if dp[i] != -1:
                return dp[i]
            res = recSearch(i+1) + recSearch(i+2)  # climb 1 or 2 step
            dp[i] = res
            return res
        return recSearch(0)