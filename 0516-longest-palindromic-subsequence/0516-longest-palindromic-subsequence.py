class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n):
            for j in range(i):
                dp[i][j] = 0
        
        def recSearch(i: int, j: int) -> int:
            nonlocal dp
            
            if dp[i][j] is not None:
                return dp[i][j]
            if s[i] == s[j]:
                sub_res = recSearch(i+1, j-1)
                dp[i][j] = sub_res + 2
                return sub_res + 2
            sub_res = max(recSearch(i+1, j), recSearch(i, j-1))
            dp[i][j] = sub_res
            return sub_res

        return recSearch(0, n-1)
