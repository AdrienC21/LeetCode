class Solution:
    # O(n^3)! adapted from another solution
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[n for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for j in range(n):
            for i in range(j, -1, -1):
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] - int(s[k] == s[j]))

        return dp[0][n - 1]
