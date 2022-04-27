class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for k in range(n//2):
            t1 = tuple(list(matrix[k][i+k] for i in range(n-2*k)))
            t2 = tuple(list(matrix[i+k][-1-k] for i in range(n-2*k)))
            t3 = tuple(list(matrix[-1-k][-(i+1+k)] for i in range(n-2*k)))
            t4 = tuple(list(matrix[-(i+1+k)][k] for i in range(n-2*k)))
            print(t1)
            print(t2)
            print(t3)
            print(t4)
            for i in range(n-2*k):
                matrix[k][i+k] = t4[i]
                matrix[i+k][-1-k] = t1[i]
                matrix[-1-k][-(i+1+k)] = t2[i]
                matrix[-(i+1+k)][k] = t3[i]
