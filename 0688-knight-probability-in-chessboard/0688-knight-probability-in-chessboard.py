class Solution:
    def get_moves(self, i: int, j: int) -> List[Tuple[int]]:
        res = []
        for d1 in (-1, 1):
            for d2 in (-2, 2):
                res.append((i+d1, j+d2))
                res.append((i+d2, j+d1))
        return res

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[None for _ in range(k)] for _ in range(n)] for _ in range(n)]
        
        def recSearch(i: int, j: int, l: int) -> float:
            nonlocal n, dp, k

            if (i < 0) or (i >= n) or (j < 0) or (j >= n):
                return 0.
            if l >= k:
                return 1.
            if dp[i][j][l] is not None:
                return dp[i][j][l]
            res = 0.
            for a, b in self.get_moves(i, j):
                res += (1 / 8) * recSearch(a, b, l+1)
            dp[i][j][l] = res
            return res

        return recSearch(row, column, 0)
