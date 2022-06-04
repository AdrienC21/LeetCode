class Solution:
    # recursive solution (backtracking), but this time use set instead of adding "x" to the board
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        
        rows = set()
        diagUp = set()
        diagDown = set()
        
        def recSearch(j: int) -> None:
            nonlocal res, board
            if j == n:
                new_board = ["".join(l) for l in board]
                res.append(new_board)
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
# First recursive solution, but time limit exceeded for n=9
"""
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        def recSearch(j: int):
            nonlocal res, board
            if j == (n-1):
                for i in range(n):
                    if board[i][j] == ".":
                        board[i][j] = "Q"
                        res.append(copy.deepcopy(board))
                        board[i][j] = "."

            else:
                for i in range(n):
                    if board[i][j] == ".":  # try this pos
                        board[i][j] = "Q"
                        # add cross j+1 and after and keep them in memory
                        to_replace = []
                        for l in range(j+1, n):
                            to_replace.append((i, l))
                            shift = l - j
                            if (i + shift) < n:
                                to_replace.append((i + shift, l))
                            if (i - shift) >= 0:
                                to_replace.append((i - shift, l))
                        for (k, l) in to_replace:
                            board[k][l] = "x"
                        # call recSearch
                        recSearch(j+1)
                        # replace cross and queen
                        for (k, l) in to_replace:
                            board[k][l] = "."
                        board[i][j] = "."
        recSearch(0)
        
        # modify res to obtain results in the proper way
        for i, board in enumerate(res):
            for k in range(n):
                for l in range(n):
                    if board[k][l] == "x":
                        board[k][l] = "."
            board = list(map(lambda l: "".join(l), board))
            res[i] = board
        return res
"""
