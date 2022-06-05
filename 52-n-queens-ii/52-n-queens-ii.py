class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        board = [["." for _ in range(n)] for _ in range(n)]

        rows = set()
        diagUp = set()
        diagDown = set()

        def recSearch(j: int) -> None:
            nonlocal res, board
            if j == n:
                res += 1
                return
            for i in range(n):
                if not((i in rows) or ((i + j) in diagUp) or ((i - j) in diagDown)):
                    # try this pos and add a queen
                    rows.add(i)
                    diagUp.add(i + j)
                    diagDown.add(i - j)
                    board[i][j] = "Q"
                    recSearch(j + 1)
                    rows.discard(i)
                    diagUp.discard(i + j)
                    diagDown.discard(i - j)
                    board[i][j] = "."  # remove queen after
        recSearch(0)
        return res
