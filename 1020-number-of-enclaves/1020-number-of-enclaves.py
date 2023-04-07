class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = set()
        current_visited = set()

        # depth search to check if an island reach the border
        def recSearch(i: int, j: int) -> int:
            if (i < 0) or (i > (m - 1)) or (j < 0) or (j > (n - 1)):
                return 0
            if not(grid[i][j]) or ((i, j) in visited):
                return 1

            visited.add((i, j))
            current_visited.add((i, j))

            # we need to touch water in all directions
            return min(recSearch(i + 1, j), recSearch(i - 1, j), recSearch(i, j + 1), recSearch(i, j - 1))

        res = 0
        for i in range(m):
            for j in range(n):
                # if it's and island not explored yet, check if it satisfies our criteria
                if grid[i][j] and ((i, j) not in visited):
                    is_enclave = recSearch(i, j)
                    if is_enclave:
                        res += len(current_visited)  # add size enclave
                    current_visited.clear()
        return res
