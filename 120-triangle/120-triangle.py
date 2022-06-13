class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[None for _ in range(i)] for i in range(1, n+1)]
        for j in range(n):
            dp[-1][j] = triangle[-1][j]
        def recSearch(i: int, j: int):
            nonlocal dp
            if not(dp[i][j] is None):
                return dp[i][j]
            value = triangle[i][j] + min(recSearch(i+1, j), recSearch(i+1, j+1))
            dp[i][j] = value
            return value
        return recSearch(0, 0)
