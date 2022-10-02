class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # target+1 x nb dice matrix, dynamic programming
        dp = [[0 for _ in range(target+1)] for _ in range(n)]
        dp[0][0] = 0  # no target 0 with 1 dice
        
        mod = 10**9 + 7
        
        for i in range(1, target+1):
            # 1 if target lower or equal than max dice value
            dp[0][i] = 0 if i > k else 1
        for j in range(1, n):
            for i in range(target+1):
                for dice in range(1, min(k+1, i+1)):
                    dp[j][i] += dp[j-1][i-dice]
                    dp[j][i] = dp[j][i] % mod
        return dp[n-1][target] % mod
