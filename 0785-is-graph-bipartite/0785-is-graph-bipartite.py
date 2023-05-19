class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = n * [-1]
        
        def visit(u: int, c: int = 0) -> bool:
            nonlocal color, graph
            if color[u] != -1:
                if color[u] != c:
                    return False
                return True
            
            # else, explore
            color[u] = c
            for v in graph[u]:
                if not(visit(v, 1 - c)):
                    return False
            return True
        
        for u in range(n):
            if color[u] == -1:
                if not(visit(u, 0)):
                    return False
        return True
