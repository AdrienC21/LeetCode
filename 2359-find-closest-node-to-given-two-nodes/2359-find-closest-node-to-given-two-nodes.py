class Solution:
    def dijkstra(self, graph: dict, s: int, n: int) -> Tuple[List[int], List[int]]:
        visited = set()
        distance = n * [sys.maxsize]
        distance[s] = 0
        path = n * [None]
        queue = []
        heapq.heappush(queue, (0, s))
        while queue:
            dist, u = heapq.heappop(queue)
            visited.add(u)
            for v, dist_uv in graph[u]:
                if not v in visited:
                    if (dist + dist_uv) < distance[v]:
                        distance[v] = dist + dist_uv
                        path[v] = u
                        heapq.heappush(queue, (distance[v], v))
        return path, distance

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = defaultdict(list)
        for u, v in enumerate(edges):
            if v != -1:
                graph[u].append((v, 1))
        n = len(edges)

        d1 = self.dijkstra(graph, node1, n)[1]
        d2 = self.dijkstra(graph, node2, n)[1]
        min_dist = sys.maxsize
        min_node = None
        for u in range(n):
            if max(d1[u], d2[u]) < min_dist:
                min_dist = max(d1[u], d2[u])
                min_node = u
        if min_dist == sys.maxsize:
            return -1
        return min_node
