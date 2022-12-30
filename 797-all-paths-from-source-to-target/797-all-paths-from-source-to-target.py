class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        
        def recSearch(i: int, visited: set) -> List[List[int]]:
            if i == (n-1):
                return [[n-1]]
            paths = []
            visited.add(i)
            for k in graph[i]:
                if k not in visited:
                    sub_paths = recSearch(k, visited)
                    if sub_paths:
                        sub_paths = [[i] + l for l in sub_paths]
                        paths.extend(sub_paths)
            visited.remove(i)
            return paths

        visited = set()
        return recSearch(0, visited)
