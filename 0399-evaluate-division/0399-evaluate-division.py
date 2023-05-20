class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
class Solution:        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # Graph + DFS approach! a->b if a/b is defined, a/b is the value of the edge
        graph = defaultdict(dict)
        for (c1, c2), value in zip(equations, values):
            graph[c1][c2] = value
            if value != 0:
                graph[c2][c1] = 1 / value
        
        def dfs(c1: str, c2: str, visited: set) -> float:
            if (c1 not in graph) or (c2 not in graph):
                return -1.
            if c2 in graph[c1]:
                return graph[c1][c2]
            for v in graph[c1]:
                if v not in visited:
                    visited.add(v)
                    temp = dfs(v, c2, visited)
                    if temp == -1:
                        continue
                    else:
                        return graph[c1][v] * temp
            return -1.

        res = []
        for q in queries:
            visited = set()
            visited.add(q[0])
            res.append(dfs(q[0], q[1], visited))
        return res
