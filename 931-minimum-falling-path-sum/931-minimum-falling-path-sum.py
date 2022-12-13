class Solution:
    # for loop instead and dynamic programming
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return min(matrix[0])
        dp = [[None for _ in range(n)] for _ in range(2)]  # we only need two rows
        for j in range(n):
            dp[1][j] = matrix[m-1][j]
        for i in range(m-2, -1, -1):
            for j in range(n):
                min_val = sys.maxsize
                for k in range(max(0, j-1), min(n, j+2)):
                    min_val = min(min_val, dp[1][k])
                dp[0][j] = min_val + matrix[i][j]
            for j in range(n):
                dp[1][j] = dp[0][j]
        return min(dp[1])

    # RecursionError: maximum recursion depth exceeded in comparison
    """
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[None for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[m-1][j] = matrix[m-1][j]
        def recSearch(i: int, j: int) -> int:
            nonlocal dp
            if dp[i][j]:
                return dp[i][j]
            min_val = sys.maxsize
            for k in range(max(0, j-1), min(n, j+2)):
                min_val = min(min_val, recSearch(i, k))
            dp[i][j] = min_val + matrix[i][j]
            return dp[i][j]
        min_path = sys.maxsize
        for j in range(n):
            min_path = min(min_path, recSearch(0, j))
        return min_path
    """
