class NumMatrix:
    # calculate accumulated sums!! O(n2) and then O(1)!
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[None for _ in range(n)] for _ in range(m)]
        self.dp[0] = list(accumulate(matrix[0]))
        for i in range(1, m):
            self.dp[i][0] = self.dp[i-1][0] + matrix[i][0]
        for i in range(1, m):
            for j in range(1, n):
                self.dp[i][j] = matrix[i][j] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not(row1) and not(col1):
            return self.dp[row2][col2]
        if not(row1):
            return self.dp[row2][col2] - self.dp[row2][col1-1]
        if not(col1):
            return self.dp[row2][col2] - self.dp[row1-1][col2]
        return self.dp[row2][col2] - self.dp[row1-1][col2] - self.dp[row2][col1-1] + self.dp[row1-1][col1-1]
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# recursive solution with dynamic programming, but time limit exceeded
"""
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[[[None for _ in range(n)] for _ in range(m)] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.dp[i][j][i][j] = matrix[i][j]
    def calculate(self, i: int, j: int, k: int, l: int) -> int:
        if not(self.dp[i][j][k][l] is None):
            return self.dp[i][j][k][l]
        if i == k:  # l greater than j
            sub_res = self.calculate(i, j, k, l-1)
            sub_res += self.matrix[k][l]
            self.dp[i][j][k][l] = sub_res
            return sub_res
        if j == l:  # k greater than i
            sub_res = self.calculate(i, j, k-1, l)
            sub_res += self.matrix[k][l]
            self.dp[i][j][k][l] = sub_res
            return sub_res
        if not(self.dp[i][j][k-1][l] is None):  # row under already calculated
            # add row k
            sub_res = self.dp[i][j][k-1][l]
            for a in range(j, l+1):
                sub_res += self.matrix[k][a]
            self.dp[i][j][k][l] = sub_res
            return sub_res
        if not(self.dp[i][j][k][l-1] is None):  # column under already calculated
            # add column l
            sub_res = self.dp[i][j][k][l-1]
            for a in range(i, k+1):
                sub_res += self.matrix[a][l]
            self.dp[i][j][k][l] = sub_res
            return sub_res
        # recursive call
        # + add row k
        sub_res = self.calculate(i, j, k-1, l)
        for a in range(j, l+1):
            sub_res += self.matrix[k][a]
        self.dp[i][j][k][l] = sub_res
        return sub_res
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.calculate(row1, col1, row2, col2)
"""

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)