class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        n_manager = len(manager)
        res = 0
        for i in range(n_manager):
            if not(informTime[i]):  # last in the chain
                time_needed = 0
                parent = i
                while parent != -1:
                    time_needed += informTime[parent]
                    parent = manager[parent]
                res = max(res, time_needed)
        return res

    # first try :/
    """
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i, m in enumerate(manager):
            if i != headID:
                graph[m].append(i)
        
        res = 0
        visited = set()
        to_visit = []
        heapq.heappush(to_visit, (informTime[headID], headID))
        while to_visit:
            time_u, u = heapq.heappop(to_visit)
            if u in visited:
                continue
            visited.add(u)
            res += time_u
            for v in graph[u]:
                heapq.heappush(to_visit, (informTime[v], v))
        return res
    """
