# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -sys.maxsize
        def recSearch(root):
            nonlocal res
            if not(root):
                return -sys.maxsize

            l = recSearch(root.left)
            r = recSearch(root.right)
            l2 = l + root.val
            r2 = r + root.val
            tot = l + r + root.val
            max_node = max(l2, r2, tot, root.val)
            res = max(res, max_node)
            return max(root.val, l2, r2)

        recSearch(root)
        return res

# missread the problem
"""
class Solution:
    def floydWarshall(self, graph):
        V = list(graph.keys())
        ids = {v: i for i, v in enumerate(graph.keys())}
        # init distances
        dist = [[sys.maxsize for _ in range(len(V))] for _ in range(len(V))]
        for i in range(V):
            dist[i][i] = 0
            for v in graph[V[i]]:
                dist[i][ids[v]] = 1

        for k in range(V):  # for all k
            for i in range(V):  # for all i
                for j in range(V):  # if k is on the shortest path from i to j => update
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        graph = defaultdict(list)
        def buildGraph(root):
            nonlocal graph
            if not(root):
                return
            if root.left:
                buildGraph(root.left)
                graph[root.left].append(root)
                graph[root].append(root.left)
            if root.right:
                buildGraph(root.right)
                graph[root.right].append(root)
                graph[root].append(root.right)
        buildGraph(root)
        dist = self.floydWarshall(graph)
        res = -sys.maxsize
        n = len(dist)
        for i in range(n):
            for j in range(n):
                if dist[i][j] != sys.maxsize:
                    res = max(res, dist[i][j])
        return res
"""
