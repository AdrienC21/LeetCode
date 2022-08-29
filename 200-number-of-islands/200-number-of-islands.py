class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == "1") and not(seen[i][j]):  # explore the island
                    count += 1
                    to_visit = [(i, j)]
                    while to_visit:
                        (k, l) = to_visit.pop()
                        if not(seen[k][l]):
                            seen[k][l] = True
                            for h in (-1, 1):
                                if ((l + h) >= 0) and ((l + h) < n) and (grid[k][l+h] == "1") and not(seen[k][l+h]):
                                    to_visit.append((k, l+h))
                            for v in (-1, 1):
                                if ((k + v) >= 0) and ((k + v) < m) and (grid[k+v][l] == "1") and not(seen[k+v][l]):
                                    to_visit.append((k+v, l))
        return count
