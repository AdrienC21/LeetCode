class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < (n - 1):  # we need at least n-1 connections to connect n computers
            return -1
        # we need to connect connex components of the graph
        # find the components with DFS
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        
        def dfs(i: int) -> None:
            nonlocal visited
            to_visit = [i]
            while to_visit:
                u = to_visit.pop()
                visited.add(u)
                for v in graph[u]:
                    if v not in visited:
                        to_visit.append(v)
                        
        nb_components = 0
        for i in range(n):
            if i not in visited:
                nb_components += 1
                dfs(i)
        return nb_components - 1
