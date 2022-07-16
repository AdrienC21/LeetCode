class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if not(maxMove):
            return 0
        dp = [[[None for _ in range(maxMove+1)] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0][1] = 1
            dp[i][n-1][1] = 1
        for j in range(n):
            dp[0][j][1] = 1
            dp[m-1][j][1] = 1
        dp[0][0][1] = 2
        dp[0][n-1][1] = 2
        dp[m-1][0][1] = 2
        dp[m-1][n-1][1] = 2
        if (m == 1) and (n == 1):
            dp[0][0][1] = 4
        elif n == 1:
            dp[0][0][1] = 3
            dp[m-1][0][1] = 3
            for i in range(1, m-1):
                dp[i][0][1] = 2
        elif m == 1:
            dp[0][0][1] = 3
            dp[0][n-1][1] = 3
            for j in range(1, n-1):
                dp[0][j][1] = 2
            
        for i in range(m):
            for j in range(n):
                dp[i][j][0] = 0  # if no move, no path
        for move in range(1, maxMove+1):  # not enough move to reach border
            for i in range(move, m-move):
                for j in range(move, n-move):
                    dp[i][j][move] = 0
        def recSearch(i: int, j: int, move: int):
            nonlocal dp
            if not(dp[i][j][move] is None):
                return dp[i][j][move]
            tot_path = 0
            if (i-1) >= 0:
                tot_path += recSearch(i-1, j, move-1)
            if (i+1) < m:
                tot_path += recSearch(i+1, j, move-1)
            if (j-1) >= 0:
                tot_path += recSearch(i, j-1, move-1)
            if (j+1) < n:
                tot_path += recSearch(i, j+1, move-1)
            dp[i][j][move] = tot_path
            return tot_path
        tot_path = 0
        for move in range(1, maxMove+1):
            tot_path += recSearch(startRow, startColumn, move)
        return (tot_path % (10**9 + 7))
