class Solution:
    def checkRow(self, board: List[List[str]], i: int, n: str) -> bool:
        return not(n in board[i])
    def checkCol(self, board: List[List[str]], j: int, n: str) -> bool:
        for i in range(9):
            if board[i][j] == n:
                return False
        return True
    def checkSquare(self, board: List[List[str]], q: int, n: str) -> bool:
        i = q // 3
        j = q % 3
        for k in range(3):
            for l in range(3):
                if board[3*i+k][3*j+l] == n:
                    return False
        return True
    def recSolve(self, board: List[List[str]], case: int) -> bool:
        if case == 81:
            return True
        i = case // 9
        j = case % 9
        if board[i][j] != ".":
            return self.recSolve(board, case+1)
        res = False
        for c in range(1, 10):
            if res:
                return True
            car = str(c)
            if self.checkRow(board, i, car) and self.checkCol(board, j, car):            
                q = 3 * (i // 3) + (j // 3)
                if self.checkSquare(board, q, car):
                    board[i][j] = car
                    res2 = self.recSolve(board, case+1)
                    if res2:
                        res = res2
                    else:
                        board[i][j] = "."
        return res
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solved = self.recSolve(board, 0)