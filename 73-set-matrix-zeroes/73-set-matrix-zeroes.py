class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        setRows = set()
        setCols = set()
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if v == 0:
                    setRows.add(i)
                    setCols.add(j)
        for i in setRows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in setCols:
            for i in range(len(matrix)):
                matrix[i][j] = 0