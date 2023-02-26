class Solution:
    # Use Dynamic programming
    # O(n1*n2), n1 = len(word1), n2 = len(word2)
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[sys.maxsize for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for j in range(n2 + 1):
            dp[n1][j] = n2 - j
        for i in range(n1 + 1):
            dp[i][n2] = n1 - i
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
        return dp[0][0]
