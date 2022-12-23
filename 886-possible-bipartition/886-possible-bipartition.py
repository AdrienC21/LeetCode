class Solution:
    # DFS: O(V + E)
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not(dislikes):
            return True
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        color = [None for _ in range(n+1)]

        def dfs(i: int, c: int) -> bool:
            nonlocal color
            if (color[i] is not None) and (color[i] != c):
                return False
            if color[i] == c:
                return True
            color[i] = c
            neighbours = graph[i]
            if not(neighbours):
                return True
            for j in neighbours:
                if not(dfs(j, -c)):
                    return False
            return True

        for i in range(1, n+1):
            if color[i] is None:
                if not(dfs(i, 1)):
                    return False
        return True

# TLE
"""
class Solution:
    def recSearch(self, g1: set, g2: set, dislikes: List[List[int]]) -> bool:
        if not(dislikes):
            return True
        a, b = dislikes[-1]
        if ((a in g1) and (b in g1)) or ((a in g2) and (b in g2)):
            return False
        if a in g1:
            g2.add(b)
            return self.recSearch(g1, g2, dislikes[:-1])
        elif a in g2:
            g1.add(b)
            return self.recSearch(g1, g2, dislikes[:-1])
        elif b in g1:
            g2.add(a)
            return self.recSearch(g1, g2, dislikes[:-1])
        elif b in g2:
            g1.add(a)
            return self.recSearch(g1, g2, dislikes[:-1])
        else:
            g1_1, g1_2 = g1.copy(), g1.copy()
            g2_1, g2_2 = g2.copy(), g2.copy()
            g1_1.add(a)
            g2_1.add(b)
            g1_2.add(b)
            g2_2.add(a)
            return self.recSearch(g1_1, g2_1, dislikes[:-1]) or self.recSearch(g1_2, g2_2, dislikes[:-1])

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g1 = set()
        g2 = set()
        return self.recSearch(g1, g2, dislikes)
"""
