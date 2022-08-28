class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if n >= m:
            for i in range(m-1, 0, -1):
                values = []  # values to sort
                len_diag = m - i
                for k in range(len_diag):
                    values.append(mat[i+k][k])
                values.sort()
                for k in range(len_diag):
                    mat[i+k][k] = values[k]
            for j in range(n - m + 1):  # complete diagonals
                values = []  # values to sort
                len_diag = m
                for k in range(len_diag):
                    values.append(mat[k][j+k])
                values.sort()
                for k in range(len_diag):
                    mat[k][j+k] = values[k]
            for j in range(n - m + 1, n):
                values = []  # values to sort
                len_diag = n - j
                for k in range(len_diag):
                    values.append(mat[k][j+k])
                values.sort()
                for k in range(len_diag):
                    mat[k][j+k] = values[k]
        else:  # n < m
            for i in range(m-1, m - n, -1):
                values = []  # values to sort
                len_diag = m - i
                for k in range(len_diag):
                    values.append(mat[i+k][k])
                values.sort()
                for k in range(len_diag):
                    mat[i+k][k] = values[k]
            for i in range(m - n, -1, -1):  # complete diagonals
                values = []  # values to sort
                len_diag = n
                for k in range(len_diag):
                    values.append(mat[i+k][k])
                values.sort()
                for k in range(len_diag):
                    mat[i+k][k] = values[k]
            for j in range(1, n):
                values = []  # values to sort
                len_diag = n - j
                for k in range(len_diag):
                    values.append(mat[k][j+k])
                values.sort()
                for k in range(len_diag):
                    mat[k][j+k] = values[k]
        return mat
