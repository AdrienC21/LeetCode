class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = {}
        n = len(labels)
        for i in range(n):
            graph[i] = {"label": labels[i], "children": []}
        for u, v in edges:
            graph[u]["children"].append(v)
            graph[v]["children"].append(u)
        
        def dfs(u, parent=-1):
            nonlocal graph
            if not(graph[u]["children"]):
                graph[u]["counter"] = Counter([graph[u]["label"]])
            for v in graph[u]["children"]:
                if v != parent:
                    dfs(v, parent=u)
            counter = Counter([graph[u]["label"]])
            for v in graph[u]["children"]:
                if v != parent:
                    counter = counter + graph[v]["counter"]
            graph[u]["counter"] = counter
        
        dfs(0, parent=-1)
        
        return [graph[i]["counter"][graph[i]["label"]] for i in range(n)]
        