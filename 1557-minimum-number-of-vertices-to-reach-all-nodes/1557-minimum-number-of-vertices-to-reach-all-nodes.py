class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = set(list(range(n)))
        for u, v in edges:
            if v in res:
                res.remove(v)
        return list(res)
