class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))
        res = sys.maxsize
        visited = set()
        to_visit = [1]
        while to_visit:  # DFS
            u = to_visit.pop()
            if u in visited:
                continue
            visited.add(u)
            for v, d in graph[u]:
                res = min(res, d)  # update minimum reachable edge
                if v not in visited:
                    to_visit.append(v)
        return res
            
    # TLE, we don't need Bellman Ford on second thought, we need to find the minimum edge
    # that can be reached from the node 1 (and so n because path is guaranteed)
    """
    # Modified bellman ford with the new distance
    def bellman_ford(self, graph: Dict[int, Tuple[int, int]], n: int, nb_roads: int, src: int = 0) -> List[int]:

        # Initialize all n=|V| vertices except source src at inf
        dist = n * [sys.maxsize]
        dist[src] = 10**5  # instead of 0 because of our metric
        new_dist = dist[:]

        # Relax all edges n - 1 times. A simple shortest
        # path from src to any other vertex can have at-most n - 1
        # edges
        
        # allowed for a path to contain the same road multiple times
        # so especially here we don't loop n-1 time but twice the number of vertices
        # to take special case of chain graph 1->n->.......->tiny edge
        for _ in range(2 * nb_roads):
            for u in range(n):
                if dist[u] != sys.maxsize:
                    for v, w in graph[u]:
                        if min(dist[u], w) < new_dist[v]:  # min metric
                            new_dist[v] = min(dist[u], w)
            for u in range(n):
                dist[u] = new_dist[u]
        return dist[n-1]  # node n
    
    # O(|E| * (|E| + |V|))?
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        if n == 1:
            return 0
        # Create the graph (vertices between 0 and n-1)
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a-1].append((b-1, d))
            graph[b-1].append((a-1, d))
        nb_roads = len(roads)
        return self.bellman_ford(graph, n, nb_roads, 0)
    """
