class UnionFind:
    # Disjoint-set data structure
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = n * [0]
    
    def find(self, i: int) -> int:
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, a: int, b: int) -> bool:
        a_node = self.find(a)
        b_node = self.find(b)
        
        if a_node == b_node:
            return False
        if self.rank[a_node] < self.rank[b_node]:
            self.parent[a_node] = b_node
            self.rank[b_node] += self.rank[a_node]
        else:
            self.parent[b_node] = a_node
            self.rank[a_node] += self.rank[b_node]
        return True

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # list of nodes for a certain value
        val_to_index = defaultdict(list)
        for i, value in enumerate(vals):
            val_to_index[value].append(i)
        
        res = 0
        n = len(vals)
        uf = UnionFind(n)
        for value in sorted(val_to_index.keys()):
            # extend the UnionFind (nodes connected together)
            for u in val_to_index[value]:
                for v in graph[u]:
                    if vals[v] <= vals[u]:
                        uf.union(v, u)
        
            count = defaultdict(int)
            for u in val_to_index[value]:
                count[uf.find(u)] += 1
                res += count[uf.find(u)]
        return res
