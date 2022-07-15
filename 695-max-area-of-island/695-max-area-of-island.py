class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        n = len(grid)
        m = len(grid[0])

        def search(i: int, j: int):
            nonlocal grid, n, m
            to_visit = [(i, j)]
            area = 0
            while to_visit:
                k, l = to_visit.pop()
                if grid[k][l] == 1:
                    area += 1
                    grid[k][l] = 2  # island already seen
                    if (k-1 >= 0) and (grid[k-1][l] == 1):
                        to_visit.append((k-1, l))
                    if (k+1 < n) and (grid[k+1][l] == 1):
                        to_visit.append((k+1, l))
                    if (l-1 >= 0) and (grid[k][l-1] == 1):
                        to_visit.append((k, l-1))
                    if (l+1 < m) and (grid[k][l+1] == 1):
                        to_visit.append((k, l+1))
            return area

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  # calculate area island
                    max_area = max(max_area, search(i, j))
        return max_area
