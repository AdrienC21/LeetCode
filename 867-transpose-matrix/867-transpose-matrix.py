
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        new_matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_matrix[i][j] = matrix[j][i]
        return new_matrix
    # using numpy
    """
    import numpy as np
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(np.array(matrix).T)
    """
