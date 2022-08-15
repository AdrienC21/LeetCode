class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][n-1] = 1
        for j in range(n):
            dp[m-1][j] = 1
        def recSearch(i: int, j: int) -> int:
            nonlocal dp
            if dp[i][j] != -1:
                return dp[i][j]
            sub_res = 0
            if i < (m-1):  # can go down
                sub_res += recSearch(i+1, j)
            if j < (n-1):  # can go right
                sub_res += recSearch(i, j+1)
            dp[i][j] = sub_res
            return sub_res
        return recSearch(0, 0)
