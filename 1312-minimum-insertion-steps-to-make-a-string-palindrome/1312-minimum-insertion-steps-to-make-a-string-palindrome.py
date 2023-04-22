class Solution:
    def longestSubPalindrome(self, s: str) -> int:
        n = len(s)
        dp = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1):
            dp[i][i+1] = 2 if (s[i] == s[i+1]) else 1

        def recSearch(i: int, j: int) -> int:
            nonlocal dp
            if dp[i][j] is not None:
                return dp[i][j]
            if s[i] == s[j]:
                dp[i][j] = recSearch(i+1, j-1) + 2
            else:
                dp[i][j] = max(recSearch(i+1, j), recSearch(i, j-1))
            return dp[i][j]
            
        return recSearch(0, n-1)

    def minInsertions(self, s: str) -> int:
        n = len(s)
        return n - self.longestSubPalindrome(s)
