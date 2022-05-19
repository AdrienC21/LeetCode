class Solution:
    # Dynamic Programming
    def neighbors(self, matrix: List[List[int]], i: int, j: int, row: int, col: int):
        res = []
        current_val = matrix[i][j]  # value of the cell (the neighbors have to be larger)
        for k in (-1, 1):
            if (0 <= (i+k) < row) and (matrix[i+k][j] > current_val):
                res.append((i+k, j))
            if (0 <= (j+k) < col) and (matrix[i][j+k] > current_val):
                res.append((i, j+k))
        return res

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[-1 for _ in range(col)] for _ in range(row)]
        def recSearch(i, j):
            nonlocal dp
            if dp[i][j] != -1:
                return dp[i][j]
            max_path = 0
            for neighbors in self.neighbors(matrix, i, j, row, col):
                temp = recSearch(neighbors[0], neighbors[1])
                if temp > max_path:
                    max_path = temp
            dp[i][j] = max_path + 1  # include cell i, j
            return dp[i][j]
        max_path = 0
        for i in range(row):
            for j in range(col):
                temp = recSearch(i, j)
                if temp > max_path:
                    max_path = temp
        return max_path
