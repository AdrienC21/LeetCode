import numpy as np
class Solution:
    def HammingDist(self, s1: str, s2: str) -> int:
        s = 0
        for i, c in enumerate(s1):
            if s2[i] != c:
                s += 1
        return s
    
    def bellmanFord(self, graph, sommetDepart, sommetArrivee):
        distances = {} 
        for sommet in graph:
            distances[sommet] = np.inf
        distances[sommetDepart] = 0

        for _ in range(len(graph)-1):
            for j in graph:
                for k in graph[j]: 
                    if distances[k] > distances[j] + graph[j][k]:
                        distances[k]  = distances[j] + graph[j][k]
        return distances[sommetArrivee]
    
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not(end in bank):
            return -1
        d = self.HammingDist(start, end)
        if (d <= 1):
            return d
        b2 = [start] + bank + [end]
        nb2 = len(b2)
        graph = {i: {} for i in range(nb2)}
        for i in range(nb2-1):
            for j in range(i+1, nb2):
                dis = self.HammingDist(b2[i], b2[j])
                if dis == 1:
                    graph[i][j] = 1
                    graph[j][i] = 1
        ret = self.bellmanFord(graph, 0, nb2-1)
        if ret != np.inf:
            return ret
        else:
            return -1