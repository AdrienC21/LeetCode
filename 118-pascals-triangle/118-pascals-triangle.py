class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1 for _ in range(1, i+1)] for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
        return pascal