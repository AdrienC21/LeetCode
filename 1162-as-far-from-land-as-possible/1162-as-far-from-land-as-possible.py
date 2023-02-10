class Solution:
    # solution not mine
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        d = deque()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if (0 <= x) and (x < n) and (0 <= y) and (y < m):
                            d.append((x, y))
        
        res = 0
        while d:
            res += 1
            l = len(d)
            
            for _ in range(l):
                i, j = d.popleft()
                if (0 <= i) and (i < n) and (0 <= j) and (j < m) and not(grid[i][j]):
                    grid[i][j] = res
                    
                    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        d.append((x, y))
        
        if res != 1:
            return res - 1
        return -1
