class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        res = 0

        def recSearch(u: int, parent: int = -1) -> int:
            nonlocal graph, res            
            u_passengers = 0
            for v in graph[u]:
                if v != parent:
                    v_passengers = recSearch(v, u)
                    u_passengers += v_passengers
                    res += ceil(v_passengers / seats)  # number of liters to cover the edge!
            return u_passengers + 1  # +1 for u
        
        recSearch(0)
        return int(res)
