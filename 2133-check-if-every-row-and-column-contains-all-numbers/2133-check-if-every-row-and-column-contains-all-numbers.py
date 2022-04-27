class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for li in matrix:
            s = set()
            for v in li:
                if (v < 1) or (v > n) or (v in s):
                    return False
                else:
                    s.add(v)
            
        for j in range(n):
            s = set()
            for i in range(n):
                v = matrix[i][j]
                if (v < 1) or (v > n) or (v in s):
                    return False
                else:
                    s.add(v)
        return True