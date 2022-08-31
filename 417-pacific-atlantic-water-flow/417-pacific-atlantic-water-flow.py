from collections import defaultdict
class Solution:
    # flow from pacific and atlantic to cells
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        graph = defaultdict(list)
        for i in range(m):
            for j in range(n):
                for h in (-1, 1):
                    if ((j + h) >= 0) and ((j + h) < n):
                        if heights[i][j+h] > heights[i][j]:
                            graph[(i, j)].append((i, j+h))
                        elif heights[i][j+h] < heights[i][j]:
                            graph[(i, j+h)].append((i, j))
                        else:
                            graph[(i, j)].append((i, j+h))
                            graph[(i, j+h)].append((i, j))
                for v in (-1, 1):
                    if ((i + v) >= 0) and ((i + v) < m):
                        if heights[i+v][j] > heights[i][j]:
                            graph[(i, j)].append((i+v, j))
                        elif heights[i+v][j] < heights[i][j]:
                            graph[(i+v, j)].append((i, j))
                        else:
                            graph[(i, j)].append((i+v, j))
                            graph[(i+v, j)].append((i, j))
        for i in range(m):
            graph["Pacific"].append((i, 0))
            graph["Atlantic"].append((i, n-1))
        for j in range(1, n):
            graph["Pacific"].append((0, j))
            graph["Atlantic"].append((m-1, j-1))
        reached_pacific = set()
        reached_atlantic = set()
        
        visited = set()
        to_visit = ["Pacific"]
        while to_visit:
            u = to_visit.pop()
            if u not in visited:
                visited.add(u)
                reached_pacific.add(u)
                for v in graph[u]:
                    if v not in visited:
                        to_visit.append(v)
        
        visited = set()
        to_visit = ["Atlantic"]
        while to_visit:
            u = to_visit.pop()
            if u not in visited:
                visited.add(u)
                reached_atlantic.add(u)
                for v in graph[u]:
                    if v not in visited:
                        to_visit.append(v)
        
        return [list(t) for t in reached_pacific.intersection(reached_atlantic)]
