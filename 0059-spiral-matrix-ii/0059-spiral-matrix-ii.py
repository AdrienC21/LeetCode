class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        c = 1
        for k in range((n + 1) // 2):
            for j in range(k, n-1-k):
                matrix[k][j] = c
                c += 1
            for i in range(k, n-1-k):
                matrix[i][n-1-k] = c
                c += 1
            for j in range(n-1-k, k, -1):
                matrix[n-1-k][j] = c
                c += 1
            for i in range(n-1-k, k, -1):
                matrix[i][k] = c
                c += 1
        if n % 2 == 1:  # fill the value at the middle
            a = n // 2
            matrix[a][a] = c
        return matrix
