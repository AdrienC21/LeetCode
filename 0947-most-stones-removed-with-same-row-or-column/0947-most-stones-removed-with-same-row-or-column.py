# Disjoint Set implementation: see here:
# https://stackoverflow.com/questions/54039935/disjoint-set-implementation-in-python
class DisjointSet:
    def __init__(self, parent):
        self.parent = parent

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            res = self.find(self.parent[item])
            self.parent[item] = res
            return res

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2

class Solution:
    # 10**4 max value of xi, yi
    def removeStones(self, stones: List[List[int]]) -> int:
        ds = DisjointSet(list(range(20000)))
        for stone in stones:
            ds.union(stone[0], stone[1]+10000);
 
        s = set()
        for stone in stones:
            s.add(ds.find(stone[0]))
        return len(stones) - len(s)
