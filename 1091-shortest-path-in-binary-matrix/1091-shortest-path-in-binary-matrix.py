import sys
import heapq
from collections import defaultdict


class Solution:
    def getNeighbors(self, i: int, j: int, n: int, grid: List[Tuple[int, int]]):
        res = []
        for k in (-1, 0, 1):
            for l in (-1, 0, 1):
                if not((k == 0) and (l == 0)) and (0 <= (i+k) < n) and (0 <= (j+l) < n) and (grid[i+k][j+l] == 0):
                    res.append((i+k, j+l))
        return res

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        # build a graph
        n = len(grid)
        visited = set()
        to_visit = [(0, 0)]
        graph = defaultdict(list)
        while to_visit:
            i, j = to_visit.pop()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for (k, l) in self.getNeighbors(i, j, n, grid):
                graph[(i, j)].append((k, l))
                if (k, l) not in visited:
                    to_visit.append((k, l))
        
        if (n-1, n-1) not in visited:  # we can't reach it
            return -1
        # else, seek for the shortest path using djikstra among all the reachable path
        distances = {(i, j): sys.maxsize for (i, j) in visited}
        distances[(n-1, n-1)] = 0
        visited = set()
        to_visit = []
        heapq.heappush(to_visit, (0, (n-1, n-1)))
        while to_visit:
            _, (i, j) = heapq.heappop(to_visit)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for (k, l) in graph[(i, j)]:
                if ((k, l) not in visited) and (distances[(k, l)] > distances[(i, j)] + 1):
                    distances[(k, l)] = distances[(i, j)] + 1
                    heapq.heappush(to_visit, (distances[(k, l)], (k, l)))
        return distances[(0, 0)] + 1  # length of a clear path is the number of visited cells of this path.
