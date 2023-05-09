class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        k = min(m, n) // 2  # number of full spirals
        numbers = 0
        if not(k):  # just a column of a row
            if m == 1:  # row
                return matrix[0]
            # column
            return [x[0] for x in matrix]
        res = []
        for l in range(k):  # iterate over the spirals
            for j in range(l, n-1-l):
                res.append(matrix[l][j])
                numbers += 1
            for i in range(l, m-l-1):
                res.append(matrix[i][n-1-l])
                numbers += 1
            for j in range(n-l-1, l, -1):
                res.append(matrix[m-1-l][j])
                numbers += 1
            for i in range(m-l-1, l, -1):
                res.append(matrix[i][l])
                numbers += 1
        # last row, column, or single element at the middle
        if ((m % 2 == 1) or (n % 2 == 1)) and (numbers != (m * n)):
            if n >= m:
                for j in range(k, n-k):
                    res.append(matrix[k][j])
            else:
                for i in range(k, m-k):
                    res.append(matrix[i][k])
        return res
