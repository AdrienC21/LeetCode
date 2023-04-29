class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        edgeList.sort(key=lambda x: x[2])  # sort by distance
        j = 0  # pointer in edge list
        res = len(queries) * [False]
        
        def find(u: int) -> int:
            nonlocal parent
    
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        for i, (p, q, limit) in sorted(enumerate(queries), key=lambda x: x[1][2]):
            while (j < len(edgeList)) and (edgeList[j][2] < limit):
                u, v, _ = edgeList[j]
                parent[find(u)] = find(v)
                j += 1
            res[i] = (find(p) == find(q))
        return res

    # TLE ...O(|V|^3 + |E| + |Q|)
    """
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build the graph O(|E|)
        graph = defaultdict(dict)
        for u, v, d in edgeList:
            if u not in graph[v]:
                graph[v][u] = d
            if v not in graph[u]:
                graph[u][v] = d
            graph[u][v] = min(graph[u][v], d)
            graph[v][u] = min(graph[v][u], d)
        
        # Floyd-Warshall O(|V|^3)
        distances = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        for u in range(n):
            # distances[u][u] = 0  # skip this as we are not summing distances
            for v, d in graph[u].items():
                distances[u][v] = d
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    distances[u][v] = min(distances[u][v], max(distances[u][k], distances[k][v]))
        
        # Check queries O(|Q|)
        return [(distances[p][q] < lim) for p, q, lim in queries]
    """
