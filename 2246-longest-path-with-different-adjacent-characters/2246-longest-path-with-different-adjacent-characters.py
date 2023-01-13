class Solution:
    # adapted from other solutions
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        result = 0
        graph = [[] for _ in range(n)]  # no need for dict: 0/n-1 indexed
        for i in range(n):
            if parent[i] != -1:
                graph[parent[i]].append(i)

        def recSearch(u: int) -> int:
            # return the longest path going down+update the longest path going in every direction
            nonlocal graph, result
            # largest paths
            path1 = 0
            path2 = 0  # second largest

            for v in graph[u]:
                res = recSearch(v)
                if s[u] == s[v]:
                    continue
                if res > path1:
                    path2 = path1
                    path1 = res
                elif res > path2:
                    path2 = res

            # update the result
            result = max(result, 1 + path1 + path2)
            return 1 + path1

        recSearch(0)
        return result
