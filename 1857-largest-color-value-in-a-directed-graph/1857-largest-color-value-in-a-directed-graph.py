class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        res = 0
        visited = set()
        path = set()
        freq = [26 * [0] for u in range(n)]
        
        def recSearch(u: int) -> int:
            if u in path:  # cycle
                return sys.maxsize
            if u in visited:
                return 0
            visited.add(u)
            path.add(u)
            color = ord(colors[u]) - ord('a')
            freq[u][color] = 1
            
            for v in graph[u]:
                if recSearch(v) == sys.maxsize:
                    return sys.maxsize
                # update color freq
                for c in range(26):
                    if c == color:
                        freq[u][c] = max(freq[u][c], freq[v][c] + 1)
                    else:
                        freq[u][c] = max(freq[u][c], freq[v][c])

            path.remove(u)
            return max(freq[u])

        for u in range(n):
            res = max(res, recSearch(u))
        return res if res != sys.maxsize else -1
