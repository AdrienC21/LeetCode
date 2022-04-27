class Solution:
    def shift(self, grid: List[List[int]], m: int, n: int) -> List[List[int]]:
        newGrid = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(1, n):
            for i in range(m):
                newGrid[i][j] = grid[i][j-1]
        for i in range(1, m):
            newGrid[i][0] = grid[i-1][n-1]
        newGrid[0][0] = grid[m-1][n-1]
        return newGrid
        
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        while k > 0:
            grid = self.shift(grid, m, n)
            k -= 1
        return grid