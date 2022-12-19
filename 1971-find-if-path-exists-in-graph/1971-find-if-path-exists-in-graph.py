class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        to_visit = [source]
        while to_visit:
            u = to_visit.pop()
            if u not in seen:
                seen.add(u)
                for v in graph[u]:
                    if v == destination:
                        return True
                    if v not in seen:
                        to_visit.append(v)
        return False
