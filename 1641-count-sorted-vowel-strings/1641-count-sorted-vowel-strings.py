class Solution:
    def countVowelStrings(self, n: int) -> int:
        # dp[i][j], number of word length i+1 that start with vowel j
        # a, e, i, o, u
        dp = [[-1 for _ in range(5)] for _ in range(n)]
        dp[0] = [1 for _ in range(5)]
        def recSearch(i, j):
            nonlocal dp
            if dp[i][j] != -1:
                return dp[i][j]
            res = 0
            for k in range(j, 5):
                res += recSearch(i-1, k)
            dp[i][j] = res
            return res
        for k in range(5):
            recSearch(n-1, k)
        return sum(dp[n-1])
