class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = n * [sys.maxsize]
        distance[src] = 0
        new_distance = distance[:]
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v, p))
        for _ in range(k+1):
            for u in range(n):
                for v, p in graph[u]:
                    if (distance[u] + p) < new_distance[v]:
                        new_distance[v] = distance[u] + p
            distance = new_distance[:]
        if distance[dst] == sys.maxsize:
            return -1
        return distance[dst]
