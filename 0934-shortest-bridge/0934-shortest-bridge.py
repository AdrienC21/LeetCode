class Solution:
    def dist(self, p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def is_border(self, grid: List[List[int]], i: int, j: int, n: int) -> bool:
        for k in (-1, 1):
            if ((i + k) >= 0) and ((i + k) < n) and not(grid[i+k][j]):
                return True
            if ((j + k) >= 0) and ((j + k) < n) and not(grid[i][j+k]):
                return True
        return False

    def shortestBridge(self, grid: List[List[int]]) -> int:
        first_island = True
        borders_island1 = []
        borders_island2 = []
        n = len(grid)
        
        def explore_island(i: int, j: int) -> None:
            nonlocal grid
            
            grid[i][j] = 2
            for k in (-1, 1):
                if ((i + k) >= 0) and ((i + k) < n) and (grid[i+k][j] == 1):
                    explore_island(i+k, j)
                if ((j + k) >= 0) and ((j + k) < n) and (grid[i][j+k] == 1):
                    explore_island(i, j+k)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if first_island:
                        explore_island(i, j)
                        first_island = False
                        borders_island2.append((i, j))
                    else:
                        if self.is_border(grid, i, j, n):
                            borders_island1.append((i, j))
                elif grid[i][j] == 2:
                    if self.is_border(grid, i, j, n):
                        borders_island2.append((i, j))
        
        min_bridge = sys.maxsize
        # calculate min bridge
        for p1 in borders_island1:
            for p2 in borders_island2:
                min_bridge = min(min_bridge, self.dist(p1, p2))
                if min_bridge == 2:
                    return 1
        return min_bridge - 1
