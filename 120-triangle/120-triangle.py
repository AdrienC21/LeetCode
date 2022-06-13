class Solution:
    # better solution with O(n) space
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = row[-1][:]
        for row in triangle[::-1][1:]:  # enumerate bottom to top the rows
            for i, num in enumerate(row):
                dp[i] = num + min(dp[i], dp[i+1])
        return dp[0]
        
    # Dynamic programming, but O(n^2) space complexity
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
