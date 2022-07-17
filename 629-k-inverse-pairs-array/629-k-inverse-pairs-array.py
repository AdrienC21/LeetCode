class Solution:
    # put a j>=1 at the beginning of the array, it creates j-1 inverse pairs
    # so we need the k-j+1 remaining ones
    # dp[n][k] = dp[n-1][k] + dp[n-1][k-1] + ... + dp[n-1][k-n+1]
    # dp[n][k+1] = dp[n-1][k+1] + dp[n-1][k] + ... + dp[n-1][k+1-n+1]
    # => dp[n][k] = dp[n][k-1] + dp[n-1][k] - dp[n-1][k-n]
    def kInversePairs(self, n: int, k: int) -> int:
        if (k < 0) or (k > ((n * (n - 1)) // 2)):  # easy check
            return 0
        dp = [[0 for _ in range(k+1)] for i in range(n+1)]
        for i in range(1, n+1):
            dp[i][0] = 1  # 0 inverse pair
        tot_mod = ((10**9) + 7)
        for i in range(1, n+1):
            for j in range(1, min(k, (i*(i-1))//2)+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
                if (j >= i):
                    dp[i][j] -= dp[i-1][j-i]
                dp[i][j] %= tot_mod
        return dp[n][k]
