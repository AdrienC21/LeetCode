class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        # Dynamic Programming
        dp = [[[-1 for _ in range(col)] for _ in range(col)] for _ in range(row)]
        for j in range(col):
            for k in range(j, col):
                if j == k:
                    dp[-1][j][k] = grid[-1][j]
                else:
                    dp[-1][j][k] = grid[-1][j] + grid[-1][k]
                    dp[-1][k][j] = grid[-1][j] + grid[-1][k]
        def recSearch(i, j, k):  # line i, robot 1 column j, robot 2 column k
            nonlocal dp
            if dp[i][j][k] != -1:
                return dp[i][j][k]
            max_pick = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if (0 <= (j+m) < col) and (0 <= (k+n) < col):
                        temp = recSearch(i+1, j+m, k+n)
                        if temp > max_pick:
                            max_pick = temp
            if j == k:
                dp[i][j][k] = max_pick + grid[i][j]
            else:
                dp[i][j][k] = max_pick + grid[i][j] + grid[i][k]
                # + symmetry!
                dp[i][k][j] = max_pick + grid[i][j] + grid[i][k]
            return dp[i][j][k]
        return recSearch(0, 0, col-1)
