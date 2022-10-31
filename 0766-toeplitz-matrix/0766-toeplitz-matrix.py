class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            val = matrix[i][0]
            for k in range(1, min(m, n)):
                if (i+k) >= m:
                    break
                if matrix[i+k][k] != val:
                    return False
        for j in range(1, n):
            val = matrix[0][j]
            for k in range(1, min(m, n)):
                if (j+k) >= n:
                    break
                if matrix[k][j+k] != val:
                    return False
        return True
