# UnionFind
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = n * [0]
        self.n = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.n -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def is_connected(self) -> bool:
        return self.n == 1

    def __repr__(self) -> str:
        return str(self.parent)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        to_keep = 0

        for edge_type, u, v in edges:
            if edge_type == 3:
                # call the first 2 unions
                b1 = alice.union(u-1, v-1)
                b2 = bob.union(u-1, v-1)
                if b1 or b2:
                    to_keep += 1
        
        for edge_type, u, v in edges:
            if edge_type == 1:
                if alice.union(u-1, v-1):
                    to_keep += 1
            elif edge_type == 2:
                if bob.union(u-1, v-1):
                    to_keep += 1
        
        if alice.is_connected() and bob.is_connected():
            return len(edges) - to_keep  # number of edges we can remove
        return -1
