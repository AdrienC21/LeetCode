class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        row = len(grid)
        col = len(grid[0])
        # perimeter is equal to 4 - number of neighbors (shared edges)
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    nb_neighbors = 0
                    for k in (-1, 1):
                        if (0 <= (i+k) < row) and grid[i+k][j]:
                            nb_neighbors += 1
                        if (0 <= (j+k) < col) and grid[i][j+k]:
                            nb_neighbors += 1
                    perimeter += (4 - nb_neighbors)
        return perimeter