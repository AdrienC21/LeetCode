class Solution:
    def rowsValid(self, board: List[List[str]]) -> bool:
        for li in board:
            s = set()
            for v in li:
                if v != ".":
                    if v in s:
                        return False
                    else:
                        s.add(v)
        return True
    def colsValid(self, board: List[List[str]]) -> bool:
        for j in range(9):
            s = set()
            for i in range(9):
                v = board[i][j]
                if v != ".":
                    if v in s:
                        return False
                    else:
                        s.add(v)
        return True
    def blocksValid(self, board: List[List[str]]) -> bool:
        for q in range(9):
            i = q // 3
            j = q % 3
            s = set()
            for k in range(3):
                for l in range(3):
                    v = board[3*i+k][3*j+l]
                    if v != ".":
                        if v in s:
                            return False
                        else:
                            s.add(v)         
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.rowsValid(board) and self.colsValid(board) and self.blocksValid(board)