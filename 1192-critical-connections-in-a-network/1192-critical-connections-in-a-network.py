from collections import defaultdict
class Solution:
    # initial idea: test for all edge if after removing it, when performing DFS, we explore all the nodes. But complexity O(|E|*(|V| + |E|))
    
    # Tarjan algorithm O(|V|+|E|) to find strongly connected components algorithm
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # build the graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Disc: time when a node is visited 1st time while DFS traversal
        disc = [None for i in range(n)]
        # Low value of a node tells the topmost reachable ancestor (with minimum possible Disc value) via the subtree of that node.
        low = [None for i in range(n)]

        cur = 0

        def dfs(node, parent):
            nonlocal cur
            if disc[node] is None:
                disc[node] = cur
                low[node] = cur
                cur += 1
                for n in graph[node]:
                    if disc[n] is None:
                        dfs(n, node)

                if parent is not None:
                    l = min([low[i] for i in graph[node] if i != parent] + [low[node]])
                else:
                    l = min([low[i] for i in graph[node]] + [low[node]])
                low[node] = l

        dfs(0, None)

        res = []
        for u, v in connections:
            if (low[u] > disc[v]) or (low[v] > disc[u]):
                res.append([u, v])
        return res