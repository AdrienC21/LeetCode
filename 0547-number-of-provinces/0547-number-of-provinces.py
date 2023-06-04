class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # adjacency matrix to graph
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if (i != j) and isConnected[i][j]:
                    graph[i].append(j)

        current_province = 0
        visited = {}
        
        # convert all cities province p1 to p2
        def convert(p1: int, p2: int) -> None:
            nonlocal visited
            
            for key, value in visited.items():
                if value == p1:
                    visited[key] = p2
        
        def dfs(u: int, province: int) -> None:
            nonlocal graph, visited
            
            if u in visited:
                if visited[u] == province:  # visited and same province
                    return
                # else, we merge the two provinces together
                convert(visited[u], province)
                return
            # u in new province
            visited[u] = province
            # connected cities in the same province
            for v in graph[u]:
                dfs(v, province)
        
        for u in range(n):
            if u not in visited:  # new province
                dfs(u, current_province)
                current_province += 1
        
        return len(set(list(visited.values())))
