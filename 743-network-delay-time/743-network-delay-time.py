from collections import defaultdict
import sys
import heapq
class Solution:
    # Djikstra: O(|E| + |V|log(|V|))
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:  # build the graph
            graph[u-1].append((w, v-1))  # add -1 to label node from 0 to n-1
        # distance first for the heap
        
        seen = set()
        s = []  # heap
        heapq.heappush(s, (0, k-1))
        
        distances = n * [sys.maxsize]
        distances[k-1] = 0
        # Djikstra
        while s:
            d, u = heapq.heappop(s)
            if u in seen:  # already seen
                continue
            seen.add(u)
            for (d_uv, v) in graph[u]:
                if (v not in seen) and (distances[v] > distances[u] + d_uv):
                    distances[v] = distances[u] + d_uv
                    heapq.heappush(s, (distances[v], v))
        if sys.maxsize in distances:  # a node of the network unreachable
            return -1
        else:
            return max(distances)