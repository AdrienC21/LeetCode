import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        
        # use queue and Djisktra algo
        queue = [(0, 0, 0)]  # distance, then coordinates (to sort)

        while queue:
            pos = heapq.heappop(queue)
            effort, i, j = pos

            if (i == (row-1)) and (j == (col-1)):  # we reached the end
                return effort

            if heights[i][j] is None:  # already explored
                continue

            for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:  # explore neighbors
                new_i = i+ di
                new_j = j + dj
                if (0 <= new_i < row) and (0 <= new_j < col) and not(heights[new_i][new_j] is None):

                    new_effort = max(effort, abs(heights[new_i][new_j] - heights[i][j]))
                    heapq.heappush(queue, (new_effort, new_i, new_j))

            heights[i][j] = None  # explored
        
    """
    # Bellman Ford solution, it works but time limit exceeded

import sys
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        
        # first check easy solutions
        if row == 1:
            if col == 1:
                return 0
            m = 0
            for i in range(col-1):
                m = max(m, abs(heights[0][i] - heights[0][i+1]))
            return m
        if col == 1:
            m = 0
            for i in range(row-1):
                m = max(m, abs(heights[i][0] - heights[i+1][0]))
            return m
        
        nodes = [(i, j) for i in range(row) for j in range(col)]
        V = row * col  # number of vertices
        
        distances = {u: sys.maxsize for u in nodes}  # distances of each cell (node in the graph) to the final cell
        distances[(row-1, col-1)] = 0
        
        neighbors = {u: {} for u in nodes}  # store neighbors of each cell (it's the edges of the graph) and the value of the edge
        
        # corners
        neighbors[(0, 0)][(1,0)] = abs(heights[1][0] - heights[0][0])
        neighbors[(0, 0)][(0,1)] = abs(heights[0][1] - heights[0][0])
        neighbors[(row-1, 0)][(row-2,0)] = abs(heights[row-2][0] - heights[row-1][0])
        neighbors[(row-1, 0)][(row-1,1)] = abs(heights[row-1][1] - heights[row-1][0])
        neighbors[(0, col-1)][(0,col-2)] = abs(heights[0][col-2] - heights[0][col-1])
        neighbors[(0, col-1)][(1,col-1)] = abs(heights[1][col-1] - heights[0][col-1])
        neighbors[(row-1, col-1)][(row-2,col-1)] = abs(heights[row-2][col-1] - heights[row-1][col-1])
        neighbors[(row-1, col-1)][(row-1,col-2)] = abs(heights[row-1][col-2] - heights[row-1][col-1])
        
        # lines
        for i in range(1, row-1):
            neighbors[(i, 0)][(i+1,0)] = abs(heights[i+1][0] - heights[i][0])
            neighbors[(i, 0)][(i-1,0)] = abs(heights[i-1][0] - heights[i][0])
            neighbors[(i, 0)][(i,1)] = abs(heights[i][1] - heights[i][0])
            neighbors[(i, col-1)][(i+1,col-1)] = abs(heights[i+1][col-1] - heights[i][col-1])
            neighbors[(i, col-1)][(i-1,col-1)] = abs(heights[i-1][col-1] - heights[i][col-1])
            neighbors[(i, col-1)][(i,col-2)] = abs(heights[i][col-2] - heights[i][col-1])
        for j in range(1, col-1):
            neighbors[(0, j)][(0,j-1)] = abs(heights[0][j-1] - heights[0][j])
            neighbors[(0, j)][(0,j+1)] = abs(heights[0][j+1] - heights[0][j])
            neighbors[(0, j)][(1,j)] = abs(heights[1][j] - heights[0][j])
            neighbors[(row-1, j)][(row-1,j-1)] = abs(heights[row-1][j-1] - heights[row-1][j])
            neighbors[(row-1, j)][(row-1,j+1)] = abs(heights[row-1][j+1] - heights[row-1][j])
            neighbors[(row-1, j)][(row-2,j)] = abs(heights[row-2][j] - heights[row-1][j])
        
        # center of the network
        for i in range(1, row-1):
            for j in range(1, col-1):
                neighbors[(i, j)][(i+1,j)] = abs(heights[i+1][j] - heights[i][j])
                neighbors[(i, j)][(i-1,j)] = abs(heights[i-1][j] - heights[i][j])
                neighbors[(i, j)][(i,j+1)] = abs(heights[i][j+1] - heights[i][j])
                neighbors[(i, j)][(i,j-1)] = abs(heights[i][j-1] - heights[i][j])
        
        for _ in range(V):
            for u in nodes:
                for v in neighbors[u]:
                    if distances[u] > max(distances[v], neighbors[u][v]):
                        distances[u] = max(distances[v], neighbors[u][v])
        return distances[(0, 0)]
        """
