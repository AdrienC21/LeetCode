class Solution:
    # prettier and optimal solution from justforonce (1D dynamic programming)
    # O(klogn) time, O(k) time
    
    # idea, rephrase in how many floors can we cover in m moves with k eggs
    # dp[m][k] = dp[m - 1][k - 1] + 1 (egg break, so k-1 and we add one) + dp[m - 1][k] (egg survive)
    def superEggDrop(self, k: int, n: int) -> int:
        m = 0
        dp = [0 for _ in range(k+1)]
        while dp[k] < n:
            m += 1
            for i in range(k, 0, -1):
                dp[i] += dp[i-1] + 1
        return m