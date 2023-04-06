class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = set()
        
        # depth search to check if an island reach the border
        def recSearch(i: int, j: int) -> int:
            if (i < 0) or (i > (m - 1)) or (j < 0) or (j > (n - 1)):
                return 0
            if (grid[i][j] == 1) or ((i, j) in visited):
                return 1
            
            visited.add((i, j))

            # we need to touch water in all directions
            return min(recSearch(i + 1, j), recSearch(i - 1, j), recSearch(i, j + 1), recSearch(i, j - 1))
        
        res = 0
        for i in range(m):
            for j in range(n):
                # if it's and island not explored yet, check if it satisfies our criteria
                if not(grid[i][j]) and ((i, j) not in visited):
                    res += recSearch(i, j)
        return res
