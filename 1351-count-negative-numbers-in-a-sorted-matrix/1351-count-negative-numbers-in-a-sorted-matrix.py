class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        r = n
        res = 0
        for i in range(m-1, -1, -1):
            for j in range(r):
                if grid[i][n-1-j] < 0:
                    res += 1
                else:
                    r = j
                    break
            if not(r):
                break
        return res
