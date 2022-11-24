class Solution:
    def add_tuple(self, u: Tuple[int,int], v: Tuple[int,int]) -> Tuple[int,int]:
        return (u[0] + v[0], u[1] + v[1])
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        len_w = len(word)
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def recSearch(i: int, j: int, seen: set, k: int):
            if k == (len_w - 1):
                return board[i][j] == word[k]
            if board[i][j] == word[k]:
                seen.add((i, j))
                for d in directions:
                    coord = self.add_tuple((i, j), d)
                    if (coord[0] >= 0) and (coord[0] < m) and (coord[1] >= 0) and (coord[1] < n) and (coord not in seen):
                        if recSearch(coord[0], coord[1], seen, k+1):
                            return True
                seen.remove((i, j))
            return False
        for i in range(m):
            for j in range(n):
                if recSearch(i, j, set(), 0):
                    return True
        return False
