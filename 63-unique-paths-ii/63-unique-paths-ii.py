class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[row-1][col-1]:  # can't reach the final cell cause there is an obstacle
            return 0
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = (1, 0)  # replace obstacle with number of path = 0
        obstacleGrid[row-1][col-1] = (obstacleGrid[row-1][col-1], 1)  # final cell, 1 path
        def recSearch(i, j):
            if isinstance(obstacleGrid[i][j], tuple):  # tuple=already calculated
                return obstacleGrid[i][j][1]
            if i == (row-1):  # we can only go right
                res = recSearch(i, j+1)
            elif j == (col-1):  # we can only go down
                res = recSearch(i+1, j)
            else:
                res = recSearch(i, j+1) + recSearch(i+1, j)
            obstacleGrid[i][j] = (0, res)
            return res
        return recSearch(0, 0)