class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[None for _ in range(n)] for _ in range(m)]
        def recSearch(i: int, j: int) -> int:
            nonlocal m, n, dp
            if (i == m) or (j == n):
                return 0
            if dp[i][j]:
                return dp[i][j]
            if text1[i] == text2[j]:
                res = 1 + recSearch(i+1, j+1)
                dp[i][j] = res
                return res
            res1 = recSearch(i+1, j)
            res2 = recSearch(i, j+1)
            dp[i][j] = max(res1, res2)
            return dp[i][j]
        return recSearch(0, 0)
