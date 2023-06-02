class Solution:
    def propagate(self, b1: List[int], b2: List[int]) -> Tuple[bool]:
        d = ((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2)
        return  (d <= b1[2]**2, d <= b2[2]**2)
        
    def dfs(self, G: dict, i: int, visited: set):
        if i in visited:
            return
        visited.add(i)
        for j in G[i]:
            self.dfs(G, j, visited)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        G = {i: [] for i in range(n)}
        for i in range(n-1):
            bi = bombs[i]
            for j in range(i+1, n):
                c1, c2 = self.propagate(bi, bombs[j])
                if c1:  # bj in radius of bi, so bi propagate to bj
                    G[i].append(j)
                if c2:
                    G[j].append(i)
        maxbombs = 1
        for b in G:
            visited = set()
            self.dfs(G, b, visited)
            maxbombs = max(maxbombs, len(visited))
        return maxbombs

# Alternative solution
"""
class Solution:
    def propagate(self, b1: List[int], b2: List[int]) -> Tuple[bool]:
        d = ((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2)
        return  (d <= b1[2]**2, d <= b2[2]**2)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # create graph
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n-1):
            bi = bombs[i]
            for j in range(i+1, n):
                c1, c2 = self.propagate(bi, bombs[j])
                if c1:  # bj in radius of bi, so bi propagate to bj
                    graph[i].append(j)
                if c2:
                    graph[j].append(i)
        
        # dfs
        def dfs(i: int, visited: Set[int]) -> None:
            nonlocal graph

            if i in visited:
                return
            visited.add(i)
            for j in graph[i]:
                dfs(j, visited)
        
        # longest path starting from a given bomb
        maxbombs = 1
        for b in range(n):
            visited = set()
            dfs(b, visited)
            maxbombs = max(maxbombs, len(visited))
        return maxbombs
"""
