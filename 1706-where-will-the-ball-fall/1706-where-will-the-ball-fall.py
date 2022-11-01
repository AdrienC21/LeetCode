class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        if n == 1:  # impossible
            return [-1]
        
        # dp
        dp = [[None for _ in range(n)] for _ in range(m)]
        
        # initialization
        if (grid[m-1][0] == 1) and (grid[m-1][1] == 1):
            dp[m-1][0] = 1
        else:
            dp[m-1][0] = -1
        if (grid[m-1][n-1] == -1) and (grid[m-1][n-2] == -1):
            dp[m-1][n-1] = n-2
        else:
            dp[m-1][n-1] = -1
        for j in range(1, n-1):
            if (grid[m-1][j] == 1) and (grid[m-1][j+1] == 1):
                dp[m-1][j] = j + 1
            elif (grid[m-1][j] == -1) and (grid[m-1][j-1] == -1):
                dp[m-1][j] = j - 1
            else:
                dp[m-1][j] = -1
        
        # rec function
        def recSearch(i: int, j: int) -> int:
            nonlocal dp, m, n
            if not(dp[i][j] is None):
                return dp[i][j]
            if j == 0:
                if (grid[i][j] == -1) or (grid[i][j+1] == -1):
                    res = -1
                else:
                    res = recSearch(i+1, 1)
            elif j == (n-1):
                if (grid[i][j] == 1) or (grid[i][j-1] == 1):
                    res = -1
                else:
                    res = recSearch(i+1, n-2)
            else:
                if grid[i][j] == 1:
                    if grid[i][j+1] == -1:
                        res = -1
                    else:
                        res = recSearch(i+1, j+1)
                else:
                    if grid[i][j-1] == 1:
                        res = -1
                    else:
                        res = recSearch(i+1, j-1)
            dp[i][j] = res
            return res

        return [recSearch(0, j) for j in range(n)]
